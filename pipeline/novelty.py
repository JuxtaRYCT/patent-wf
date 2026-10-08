"""Step 2 - Filtration & novelty detection.

For every *incoming* item (published inside the look-back window) we measure how far it is
from the *knowledge base* (prior-art patents + older literature + anything seen on earlier runs):

  dense_max   max cosine similarity to KB (bge-base embeddings)
  dense_top5  mean of 5 nearest KB neighbours (robust to a single lucky neighbour)
  lex_max     max TF-IDF cosine to KB (catches shared rare terminology embeddings blur)
  novelty     1 - (w_d * dense_max + w_l * lex_max)
  buzz        # of other incoming items with cosine > 0.80 (trend / hotness, not novelty)

Items above the configured novelty percentile (per pool) form the shortlist that goes to LLM scoring.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from . import embed, llm, store
from .common import days_ago, dump_json, load_config, log, run_dir, today

L = log("novelty")


def split_incoming_kb(lookback: int) -> tuple[list[dict], list[dict]]:
    since = days_ago(lookback).isoformat()
    rows = store.fetch("kind != 'idea'")
    incoming, kb = [], []
    for r in rows:
        pub = (r.get("published") or "")[:10]
        is_new = r["kind"] in ("paper", "news", "repo", "post") and (not pub or pub >= since)
        first_seen_today = (r.get("fetched") or "")[:10] >= today()
        if is_new and first_seen_today and r["pool"] in ("finance", "crossdomain"):
            incoming.append(r)
        else:
            kb.append(r)          # patents, regulations, older papers, items from earlier runs
    return incoming, kb


def score(incoming: list[dict], kb: list[dict], cfg: dict) -> pd.DataFrame:
    nv = cfg["novelty"]
    Xi, Xk = embed.ensure(incoming), embed.ensure(kb)
    sims = Xi @ Xk.T
    top = np.sort(sims, axis=1)[:, ::-1]
    arg = sims.argmax(axis=1)
    tf = TfidfVectorizer(stop_words="english", min_df=2, max_df=0.4, ngram_range=(1, 2), sublinear_tf=True)
    tf.fit([embed.doc_text(x) for x in kb + incoming])
    Ti, Tk = tf.transform([embed.doc_text(x) for x in incoming]), tf.transform([embed.doc_text(x) for x in kb])
    lex = (Ti @ Tk.T).max(axis=1).toarray().ravel()
    self_sims = Xi @ Xi.T
    np.fill_diagonal(self_sims, 0)
    buzz = (self_sims > 0.80).sum(axis=1)
    df = pd.DataFrame({
        "id": [x["id"] for x in incoming], "pool": [x["pool"] for x in incoming],
        "kind": [x["kind"] for x in incoming], "source": [x["source"] for x in incoming],
        "title": [x["title"] for x in incoming], "published": [x.get("published") for x in incoming],
        "field": [x.get("query") or "" for x in incoming],
        "dense_max": top[:, 0], "dense_top5": top[:, :5].mean(axis=1), "lex_max": lex,
        "nearest_kb": [kb[j]["id"] for j in arg], "nearest_kb_title": [kb[j]["title"][:120] for j in arg],
        "buzz": buzz})
    df["novelty"] = 1 - (nv["dense_weight"] * df.dense_max + nv["lexical_weight"] * df.lex_max)
    df["near_duplicate"] = df.dense_max > nv["near_duplicate_threshold"]
    # relevance gate: distance-novelty alone rewards off-topic noise (politics, celebrity news ...)
    A = embed.encode(nv["anchors"], query=True)
    df["relevance"] = (Xi @ A.T).max(axis=1)
    df["eligible"] = np.where(
        df.pool == "finance", df.relevance >= nv["relevance_min"],
        (df.kind == "paper") & np.array([len(x.get("text") or "") >= nv["crossdomain_min_chars"] for x in incoming]))
    # genre-stratified shortlist: news/posts are lexically far from a paper+patent KB by genre alone,
    # so papers are ranked against papers and news against news (finding from run 1)
    df["genre"] = np.where(df.kind == "paper", "paper", "news")
    pct = nv["shortlist_percentile"]
    df["shortlisted"] = False
    for _, g in df[df.eligible & ~df.near_duplicate].groupby(["pool", "genre"]):
        thr = np.percentile(g.novelty, pct)
        df.loc[g.index[g.novelty >= thr], "shortlisted"] = True
    return df.sort_values("novelty", ascending=False)


LLM_SYSTEM = ("You are a patent strategist and research scout for a bank's innovation lab. You score "
              "incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as "
              "raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers "
              "score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract "
              "principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.")

LLM_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["scores"],
    "properties": {"scores": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["id", "novelty", "usefulness", "mechanism_or_problem", "tags"],
        "properties": {
            "id": {"type": "string"},
            "novelty": {"type": "integer", "description": "1-10 novelty of the core idea"},
            "usefulness": {"type": "integer", "description": "1-10 value as input for finance inventions"},
            "mechanism_or_problem": {"type": "string", "description": "<=30 words"},
            "tags": {"type": "array", "items": {"type": "string"}}}}}}}


CAPS = {("finance", "paper"): 90, ("finance", "news"): 70, ("crossdomain", "paper"): 150}


def llm_score(df: pd.DataFrame, items_by_id: dict, batch: int = 30) -> pd.DataFrame:
    """LLM-score the most novel shortlisted items (capped per pool x genre to bound cost / reading load)."""
    parts = []
    for k, g in df[df.shortlisted].groupby(["pool", "genre"]):
        g = g.sort_values("novelty", ascending=False)
        if k[0] == "crossdomain":   # stratify by source field so every discipline contributes mechanisms
            per = int(np.ceil(CAPS[k] / max(g.field.nunique(), 1)))
            g = g.groupby("field").head(per)
        parts.append(g.head(CAPS.get(k, 50)))
    sl = pd.concat(parts)
    results = {}
    ids = list(sl.id)
    for b in range(0, len(ids), batch):
        chunk = ids[b:b + batch]
        lines = []
        for i in chunk:
            it = items_by_id[i]
            lines.append(f"- id: {i}\n  pool: {it['pool']}\n  title: {it['title']}\n  abstract: {(it['text'] or '')[:700]}")
        task = f"novelty_score_{b // batch:03d}"
        prompt = "Score each item. Return one entry per id.\n\n" + "\n".join(lines)
        ans = llm.ask_json(task, LLM_SYSTEM, prompt, LLM_SCHEMA, effort="medium")
        if ans:
            for s in ans["scores"]:
                results[s["id"]] = s
    df = df.copy()
    for k in ("novelty", "usefulness"):
        df[f"llm_{k}"] = df.id.map(lambda i: results.get(i, {}).get(k))
    df["llm_note"] = df.id.map(lambda i: results.get(i, {}).get("mechanism_or_problem"))
    df["llm_tags"] = df.id.map(lambda i: ",".join(results.get(i, {}).get("tags", [])))
    return df


def main():
    cfg = load_config()
    incoming, kb = split_incoming_kb(cfg["run"]["lookback_days"])
    L.info("incoming %d | knowledge base %d", len(incoming), len(kb))
    df = score(incoming, kb, cfg)
    byid = {x["id"]: x for x in incoming}
    df = llm_score(df, byid)
    out = run_dir()
    df.to_csv(out / "novelty_incoming.csv", index=False)
    store.save_scores([(r.id, today(), "novelty", k, float(getattr(r, k)))
                       for r in df.itertuples() for k in ("novelty", "dense_max", "lex_max", "buzz")])
    summary = {"incoming": len(incoming), "kb": len(kb), "eligible": int(df.eligible.sum()),
               "shortlisted": int(df.shortlisted.sum()),
               "near_duplicates": int(df.near_duplicate.sum()),
               "by_pool": df.groupby("pool").agg(n=("id", "size"), shortlisted=("shortlisted", "sum"),
                                                 novelty_mean=("novelty", "mean")).reset_index().to_dict("records"),
               "llm_pending": len(llm.pending())}
    dump_json(summary, out / "novelty_summary.json")
    L.info("novelty summary: %s", json.dumps(summary, default=str)[:500])
    return df


if __name__ == "__main__":
    main()
