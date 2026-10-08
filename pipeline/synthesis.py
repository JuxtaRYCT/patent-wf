"""Step 3 - Synthesis & cross-pollination (the idea generator).

Bisociation engine (Koestler 1964; literature-based discovery, Swanson 1986):
  P = finance PROBLEMS   (novel finance papers/news from the shortlist, LLM-extracted open problem)
  M = foreign MECHANISMS (novel cross-domain papers: biology, physics, robotics, HCI, crypto ...)

  1. distance d(p, m) = 1 - cos(p, m). Too close -> obvious combination; too far -> nonsense.
     Keep pairs inside a percentile band ("far but bridgeable", config synthesis.distance_band).
  2. Prior-art pre-check: embed the fused vector normalise(p + m) and measure its max similarity to the
     patent KB. Pairs whose fusion already sits next to a patent are demoted (combination likely known).
  3. Maximal-marginal-relevance selection so no problem or mechanism dominates the batch.
  4. Structured prompt per batch of pairs -> LLM proposes invention concepts with a concrete technical
     mechanism, a claim-ready core, and search keywords for the prior-art check.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from . import embed, llm, store
from .common import IDEAS, dump_json, load_config, log, run_dir

L = log("synthesis")

SYSTEM = (
    "You are an inventor on a bank's advanced-technology team, expert in payments, fraud, credit, treasury, "
    "regulation (US, EU, UK, India) and patent drafting. You practise bisociation: transplanting a mechanism "
    "from an unrelated field into a finance problem. Rules: (1) every concept must have a concrete TECHNICAL "
    "mechanism (data structures, signals, protocols, hardware, cryptography, control loops) - not a business "
    "method; (2) it must be implementable within ~3 years; (3) name what makes it non-obvious versus the "
    "closest thing you know exists; (4) prefer concepts a bank, card network or payment processor would "
    "license; (5) if a pair yields nothing credible, return fewer ideas rather than forcing one.")

SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["ideas"],
    "properties": {"ideas": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["pair", "title", "problem", "mechanism", "technical_effect", "why_non_obvious",
                     "claim_core", "keywords", "domain"],
        "properties": {
            "pair": {"type": "string", "description": "pair id used"},
            "title": {"type": "string"},
            "problem": {"type": "string"},
            "mechanism": {"type": "string", "description": "how it works, 80-150 words"},
            "technical_effect": {"type": "string"},
            "why_non_obvious": {"type": "string"},
            "claim_core": {"type": "string", "description": "draft independent-claim essence, 1-2 sentences"},
            "keywords": {"type": "string", "description": "prior-art search keywords"},
            "domain": {"type": "string", "description": "payments|fraud|credit|treasury|regtech|wealth|insurance|crypto|identity"}}}}}}


def select_pairs(P: list[dict], M: list[dict], cfg: dict) -> pd.DataFrame:
    s = cfg["synthesis"]
    Xp, Xm = embed.ensure(P), embed.ensure(M)
    D = 1 - Xp @ Xm.T
    lo, hi = np.percentile(D, [s["distance_band"][0] * 100, s["distance_band"][1] * 100])
    patents = store.fetch("kind='patent'")
    Xpat = embed.ensure(patents)
    rows = []
    for i in range(len(P)):
        for j in range(len(M)):
            if lo <= D[i, j] <= hi:
                rows.append((i, j, D[i, j]))
    L.info("%d candidate pairs in distance band [%.3f, %.3f]", len(rows), lo, hi)
    if not rows:
        return pd.DataFrame()
    idx = np.array([(i, j) for i, j, _ in rows])
    fused = Xp[idx[:, 0]] + Xm[idx[:, 1]]
    fused /= np.linalg.norm(fused, axis=1, keepdims=True)
    pat_prox = np.zeros(len(rows), np.float32)
    for b in range(0, len(rows), 4096):
        pat_prox[b:b + 4096] = (fused[b:b + 4096] @ Xpat.T).max(axis=1)
    df = pd.DataFrame({"p": idx[:, 0], "m": idx[:, 1], "dist": [r[2] for r in rows], "patent_proximity": pat_prox})
    # quality prior: LLM usefulness of both ends (if scored) - defaults to 5
    pu = np.array([P[i].get("llm_usefulness") or 5 for i in range(len(P))], float)
    mu = np.array([M[j].get("llm_usefulness") or 5 for j in range(len(M))], float)
    df["prior"] = (pu[df.p] + mu[df.m]) / 20 + (1 - df.patent_proximity)
    # MMR: greedy pick maximising prior, penalising reuse of a problem or mechanism
    chosen, use_p, use_m = [], {}, {}
    lam = s["mmr_lambda"]
    cand = df.sort_values("prior", ascending=False).head(5000).copy()
    while len(chosen) < s["pairs"] and len(cand):
        pen = cand.p.map(lambda x: use_p.get(x, 0)) + cand.m.map(lambda x: use_m.get(x, 0))
        score = lam * cand.prior - (1 - lam) * pen
        k = score.idxmax()
        r = cand.loc[k]
        chosen.append(k)
        use_p[r.p] = use_p.get(r.p, 0) + 1
        use_m[r.m] = use_m.get(r.m, 0) + 1
        cand = cand.drop(k)
        cand = cand[~((cand.p.map(lambda x: use_p.get(x, 0)) >= 2) | (cand.m.map(lambda x: use_m.get(x, 0)) >= 2))]
    return df.loc[chosen].reset_index(drop=True)


def build_pools(nov: pd.DataFrame) -> tuple[list[dict], list[dict]]:
    items = {x["id"]: x for x in store.fetch("kind != 'idea'")}
    min_u = load_config()["synthesis"].get("min_usefulness", 4)
    sl = nov[nov.shortlisted & nov.llm_usefulness.notna() & (nov.llm_usefulness >= min_u)]
    P, M = [], []
    for r in sl.itertuples():
        it = dict(items[r.id])
        it["llm_usefulness"] = r.llm_usefulness
        it["llm_note"] = r.llm_note if isinstance(r.llm_note, str) else ""
        (P if r.pool == "finance" else M).append(it)
    return P, M


def generate(pairs: pd.DataFrame, P: list[dict], M: list[dict], batch: int = 6) -> list[dict]:
    ideas = []
    for b in range(0, len(pairs), batch):
        chunk = pairs.iloc[b:b + batch]
        blocks = []
        for k, r in chunk.iterrows():
            p, m = P[int(r.p)], M[int(r.m)]
            blocks.append(
                f"### PAIR X{k:03d}  (semantic distance {r.dist:.2f}, fused-vector patent proximity {r.patent_proximity:.2f})\n"
                f"FINANCE PROBLEM SOURCE [{p['id']}]: {p['title']}\n{(p['text'] or '')[:900]}\n"
                f"Open problem (scout note): {p.get('llm_note', '')}\n\n"
                f"FOREIGN MECHANISM SOURCE [{m['id']}]: {m['title']}\n{(m['text'] or '')[:900]}\n"
                f"Transferable mechanism (scout note): {m.get('llm_note', '')}\n")
        prompt = ("For each pair, transplant the foreign mechanism into the finance problem and propose 0-2 "
                  "patentable invention concepts. Stretch for unusual but technically credible combinations.\n\n"
                  + "\n".join(blocks))
        ans = llm.ask_json(f"synthesis_{b // batch:03d}", SYSTEM, prompt, SCHEMA, effort="high")
        if ans:
            for idea in ans["ideas"]:
                k = int(idea["pair"].strip("X").lstrip("0") or 0) if idea["pair"].startswith("X") else None
                if k is not None and k in pairs.index:
                    idea["sources"] = [P[int(pairs.loc[k].p)]["id"], M[int(pairs.loc[k].m)]["id"]]
                ideas.append(idea)
    return ideas


def main():
    cfg = load_config()
    out = run_dir()
    nov = pd.read_csv(out / "novelty_incoming.csv")
    P, M = build_pools(nov)
    L.info("problem pool %d | mechanism pool %d", len(P), len(M))
    pairs = select_pairs(P, M, cfg)
    pairs["p_id"] = [P[i]["id"] for i in pairs.p]
    pairs["m_id"] = [M[j]["id"] for j in pairs.m]
    pairs["p_title"] = [P[i]["title"][:100] for i in pairs.p]
    pairs["m_title"] = [M[j]["title"][:100] for j in pairs.m]
    pairs.to_csv(out / "synthesis_pairs.csv")
    ideas = generate(pairs, P, M)
    for n, idea in enumerate(ideas, 1):
        idea["id"] = f"A1-{n:02d}"
    if ideas:
        dump_json({"arm": "A1", "name": "Approach 1 - literature cross-pollination (bisociation)",
                   "run": out.name, "ideas": ideas}, IDEAS / "A1_cross_pollination.json")
    L.info("pairs %d -> ideas %d (pending LLM tasks: %d)", len(pairs), len(ideas), len(llm.pending()))


if __name__ == "__main__":
    main()
