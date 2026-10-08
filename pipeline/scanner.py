"""Approach 2 - AI Opportunity Scanner (problem-first, signal-grounded).

Where Approach 1 starts from *solutions looking for problems* (new research), the scanner starts from
*demand*: where are customers hurting, where is regulation forcing change, where is technology ready,
and where is the patent landscape still thin?

  signal corpus   Federal Register rules/notices, central-bank & industry news, Hacker News,
                  CFPB complaint-issue trends (as pseudo-documents weighted by volume x lift)
  themes          KMeans clusters of the signal corpus (bge embeddings)
  per theme       pain       CFPB volume x growth lift + consumer-facing news/HN mentions
                  pull       regulatory documents (rules, proposed rules, notices)
                  momentum   share of theme items from the last 14 days
                  push       novel finance papers near the theme centroid (technology readiness)
                  whitespace 1 - patent density near the centroid (KB) blended with live USPTO hit counts
  opportunity     weighted sum of z-scores -> top themes go to the LLM for invention generation
"""
from __future__ import annotations

import json
import re

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

from . import embed, llm, store
from .common import IDEAS, days_ago, dump_json, load_config, log, run_dir

L = log("scanner")
WEIGHTS = {"pain": 1.0, "pull": 0.8, "momentum": 0.5, "push": 0.7, "whitespace": 1.2}


def cfpb_pseudo_docs(trends: list[dict], min_recent: int = 500) -> list[dict]:
    """Label-only text so complaint issues cluster by *topic* with related news/regulation
    (v1 used a templated sentence and all complaints collapsed into one mega-theme)."""
    docs = []
    for t in trends:
        if t["field"] != "issue" or t["recent"] < min_recent:
            continue
        label = t["key"].replace(" > ", ": ")
        docs.append({"id": f"cfpbtrend:{t['key'][:80]}", "kind": "complaint_trend", "pool": "signal",
                     "source": "cfpb", "title": f"[CFPB {t['recent']:,} complaints, lift {t['lift']:.2f}] {label}",
                     "text": label, "published": "", "meta": {"recent": t["recent"], "lift": t["lift"]}})
    return docs


NOISE_TITLES = re.compile(r"information collection|paperwork|sunshine act|meeting|privacy act of 1974|system of records|"
                          r"viticultural|general license|techcrunch disrupt|hearing|correction|extension of comment",
                          re.I)
GENERIC = set("2025 2026 2027 com news times new https www said says million billion bank banks india inf "
              "rule rules proposed federal board complaints lift cfpb problem".split())


def signal_corpus() -> list[dict]:
    """Relevance-gated demand signals: substantive regulation + finance-relevant news/posts."""
    cfg = load_config()["novelty"]
    rows = [r for r in store.fetch("kind IN ('regulation','news','post')") if not NOISE_TITLES.search(r["title"])]
    X = embed.ensure(rows)
    A = embed.encode(cfg["anchors"], query=True)
    rel = (X @ A.T).max(axis=1)
    keep = [i for i, v in enumerate(rel) if v >= cfg["relevance_min"]]
    # collapse syndicated copies (one wire story re-published by 40 outlets is one signal, not 40)
    Xk = X[keep]
    S = Xk @ Xk.T
    rep, out = {}, []
    for a in range(len(keep)):
        dup = next((b for b in rep if S[a, b] > 0.93), None)
        if dup is None:
            rep[a] = 1
        else:
            rep[dup] += 1
    for a, n in rep.items():
        r = dict(rows[keep[a]])
        r["meta"] = dict(r["meta"], syndication=n)
        out.append(r)
    L.info("signals: %d relevant -> %d after collapsing syndicated duplicates", len(keep), len(out))
    return out


def z(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, float)
    return (x - x.mean()) / (x.std() + 1e-9)


def build_themes(k: int = 30) -> tuple[pd.DataFrame, list[dict], np.ndarray, np.ndarray]:
    out = run_dir()
    trends = json.loads((out / "cfpb_trends.json").read_text()) if (out / "cfpb_trends.json").exists() else []
    signals = signal_corpus()
    pseudo = cfpb_pseudo_docs(trends)
    L.info("signal corpus: %d relevance-gated signals + %d complaint issues", len(signals), len(pseudo))
    corpus = signals + pseudo
    X = np.vstack([embed.ensure(signals), embed.encode([embed.doc_text(d) for d in pseudo])]) if pseudo \
        else embed.ensure(signals)
    km = KMeans(n_clusters=k, n_init=10, random_state=7).fit(X)
    C = km.cluster_centers_ / np.linalg.norm(km.cluster_centers_, axis=1, keepdims=True)
    labels = km.labels_
    tf = TfidfVectorizer(stop_words="english", max_df=0.3, min_df=3, ngram_range=(1, 2))
    T = tf.fit_transform([embed.doc_text(d, 400) for d in corpus])
    vocab = np.array(tf.get_feature_names_out())

    papers = store.fetch("kind='paper' AND pool='finance'")
    Xpap = embed.ensure(papers)
    patents = store.fetch("kind='patent'")
    Xpat = embed.ensure(patents)
    recent = days_ago(14).isoformat()
    rows = []
    for c in range(k):
        idx = np.where(labels == c)[0]
        members = [corpus[i] for i in idx]
        ranked = vocab[np.asarray(T[idx].mean(axis=0)).ravel().argsort()[::-1][:30]].tolist()
        terms = [t for t in ranked if not any(w in GENERIC or w.isdigit() for w in t.split())][:8]
        sims_to_c = X[idx] @ C[c]
        reps = [members[i] for i in np.argsort(-sims_to_c)[:8]]
        cf = [m for m in members if m["kind"] == "complaint_trend"]
        pain = sum(m["meta"]["recent"] * min(m["meta"]["lift"], 5) for m in cf) ** 0.5 + \
            sum(1 + np.log1p(m["meta"].get("syndication", 1) - 1) for m in members
                if m["kind"] in ("post",) or "scam" in m["title"].lower() or "fraud" in m["title"].lower())
        rows.append({
            "theme": c, "size": len(idx), "terms": ", ".join(terms),
            "pain": pain, "pull": sum(1 for m in members if m["kind"] == "regulation"),
            "momentum": np.mean([(m.get("published") or "") >= recent for m in members]),
            "push": int(((Xpap @ C[c]) > 0.72).sum()),
            "patent_density": int(((Xpat @ C[c]) > 0.72).sum()),
            "representatives": [f"[{m['kind']}] {m['title'][:140]}" for m in reps],
            "member_ids": [m["id"] for m in members]})
    df = pd.DataFrame(rows)
    return df, corpus, X, C


def live_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """USPTO full-text hit count for each theme's top terms since 2023 (lower = whiter space)."""
    try:
        from .sources.ppubs import PPUBS
        api = PPUBS()
    except Exception as e:
        L.warning("PPUBS unavailable (%s) - using KB density only", e)
        df["uspto_hits"] = np.nan
        return df
    hits = []
    for terms in df.terms:
        # phrases first: unigrams like "report" / "information" hit tens of thousands of unrelated patents
        tl = [w for w in re.split(r",\s*", terms) if len(w) > 3 and "complaints" not in w and "lift" not in w]
        phrases = [w for w in tl if " " in w][:2] or tl[:3]
        q = " AND ".join(f"({' ADJ '.join(w.split())})" for w in phrases) + " AND @pd>=20230101"
        _, n = api.search(q, 1)
        hits.append(n)
    df["uspto_hits"] = hits
    return df


def score(df: pd.DataFrame, min_size: int = 8) -> pd.DataFrame:
    """log-scaled z-scores (v1 let one complaint mega-theme dominate on raw pain)."""
    df = df[df["size"] >= min_size].copy()
    dens = z(np.log1p(df.patent_density))
    if "uspto_hits" in df and df.uspto_hits.notna().any():
        dens = 0.5 * dens + 0.5 * z(np.log1p(df.uspto_hits.fillna(df.uspto_hits.median())))
    df["whitespace"] = -dens
    feats = {"pain": z(np.log1p(df.pain)), "pull": z(np.log1p(df.pull)), "momentum": z(df.momentum),
             "push": z(np.log1p(df.push)), "whitespace": df.whitespace}
    df["opportunity"] = sum(WEIGHTS[k] * feats[k] for k in WEIGHTS)
    return df.sort_values("opportunity", ascending=False)


SYSTEM = (
    "You are an AI opportunity scanner for a bank's patent program. You receive opportunity themes built "
    "from live demand signals (consumer complaints, new regulation, industry news) with a whitespace score "
    "(how thin the patent landscape is). For each theme propose inventions that (1) solve the demand signal "
    "with a concrete technical mechanism, (2) avoid the obvious approaches incumbents already patent, and "
    "(3) are patent-eligible (technical effect, not a business method).")

IDEA_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["ideas"],
    "properties": {"ideas": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["theme", "title", "problem", "mechanism", "technical_effect", "why_non_obvious",
                     "claim_core", "keywords", "domain"],
        "properties": {k: {"type": "string"} for k in
                       ["theme", "title", "problem", "mechanism", "technical_effect", "why_non_obvious",
                        "claim_core", "keywords", "domain"]}}}}}


def generate(df: pd.DataFrame, top: int = 12, per_packet: int = 4) -> list[dict]:
    ideas = []
    sel = df.head(top)
    for b in range(0, len(sel), per_packet):
        chunk = sel.iloc[b:b + per_packet]
        blocks = []
        for r in chunk.itertuples():
            blocks.append(f"### THEME T{r.theme:02d}  opportunity={r.opportunity:.2f} whitespace={r.whitespace:.2f} "
                          f"pain={r.pain:.1f} regulatory_pull={r.pull} tech_push={r.push} patent_density={r.patent_density}\n"
                          f"Key terms: {r.terms}\nRepresentative signals:\n" + "\n".join(f"  - {x}" for x in r.representatives))
        prompt = "Propose 2-3 invention concepts per theme.\n\n" + "\n\n".join(blocks)
        ans = llm.ask_json(f"scanner_{b // per_packet:03d}", SYSTEM, prompt, IDEA_SCHEMA, effort="high")
        if ans:
            ideas += ans["ideas"]
    return ideas


def main(k: int = 30):
    out = run_dir()
    df, corpus, X, C = build_themes(k)
    df = score(live_whitespace(df))
    df.drop(columns=["member_ids"]).to_csv(out / "scanner_themes.csv", index=False)
    dump_json(df.to_dict("records"), out / "scanner_themes.json")
    ideas = generate(df)
    for n, idea in enumerate(ideas, 1):
        idea["id"] = f"A2b-{n:02d}"
    if ideas:
        dump_json({"arm": "A2b", "name": "Approach 2 - AI Opportunity Scanner, signal-grounded", "run": out.name,
                   "ideas": ideas}, IDEAS / "A2b_signal_scanner.json")
    L.info("themes %d -> ideas %d (pending LLM tasks: %d)", len(df), len(ideas), len(llm.pending()))


if __name__ == "__main__":
    main()
