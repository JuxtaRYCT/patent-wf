"""Evaluation: does each approach actually produce novel, useful, patentable ideas?

Arms compared (same filtration engine for all):
  A2a  AI Opportunity Scanner, zero-shot   (LLM parametric knowledge only; frozen before data collection)
  A2b  AI Opportunity Scanner, grounded    (demand signals + patent whitespace)
  A1   Literature cross-pollination        (novel papers -> bisociation pairs)

Metrics
  novelty_pa      1 - max cosine similarity to retrieved prior art (patents + papers)       [automatic]
  anticipated     share of ideas whose closest patent is in the calibrated "same invention" band
                  (max_sim_patent >= 0.80; runs/<date>/similarity_calibration.json: same-invention
                  abstract-vs-claim p25 = 0.79, different-invention same-CPC p95 = 0.78)      [automatic]
  overlap         share with max_sim_patent >= 0.75 (strong overlap band)                     [automatic]
  vendi           Vendi score = effective number of distinct ideas in the arm (Friedman & Dieng 2023)
  cross_arm_sim   mean similarity of an idea to its nearest idea in the *other* arms (homogenisation)
  judge_*         LLM-as-judge (patent examiner persona) reading the idea next to its closest prior art:
                  novelty, non_obviousness, utility, feasibility, commercial, eligibility (1-10), verdict
  final_score     0.25 judge novelty + 0.20 non-obviousness + 0.15 utility + 0.10 feasibility
                  + 0.15 commercial + 0.10 eligibility + 0.05 * 10 * novelty_pa (normalised to 0-10)
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from . import embed, llm, store
from .common import EXPORTS, IDEAS, dump_json, log, run_dir
from .prior_art import idea_text, load_ideas

L = log("evaluate")

JUDGE_SYSTEM = (
    "You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office "
    "experience) and a bank's head of innovation. For each idea you see the idea and the closest prior "
    "art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, "
    "novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a "
    "computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. "
    "'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.")

JUDGE_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["judgments"],
    "properties": {"judgments": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["id", "novelty", "non_obviousness", "utility", "feasibility", "commercial", "eligibility",
                     "crazy", "verdict", "rationale"],
        "properties": {
            "id": {"type": "string"},
            **{k: {"type": "integer"} for k in ["novelty", "non_obviousness", "utility", "feasibility",
                                                "commercial", "eligibility", "crazy"]},
            "verdict": {"type": "string", "enum": ["pursue", "refine", "drop-anticipated", "drop-weak"]},
            "rationale": {"type": "string"}}}}}}

ANTICIPATED, OVERLAP = 0.80, 0.75     # calibrated bands (see docstring)
# Length-controlled variant. Run-1 finding: zero-shot ideas are ~26 words vs ~150 for grounded ones, and short
# text is less similar to *everything*, which made the least novel arm look most novel. Every idea is reduced to
# the same short form (title + first sentence of problem + first sentence of mechanism, <= 45 words) and compared
# with the (now enlarged) KB. Short-form calibration: same-invention p5 = 0.80, different-invention p95 = 0.74.
ANTICIPATED_SF, OVERLAP_SF = 0.78, 0.72


def short_form(i: dict) -> str:
    import re
    first = lambda t: re.split(r"(?<=[.;:])\s", (t or "").strip(), maxsplit=1)[0]
    return " ".join(f"{i['title']}. {first(i.get('problem'))} {first(i.get('mechanism'))}".split()[:45])


def length_controlled(ideas: list[dict]) -> dict:
    pats, lit = store.fetch("kind='patent'"), store.fetch("kind='paper'")
    Xp, Xl = embed.ensure(pats), embed.ensure(lit)
    Xi = embed.encode([short_form(i) for i in ideas])
    Sp, Sl = Xi @ Xp.T, Xi @ Xl.T
    return {i["id"]: {"max_sim_patent_sf": float(Sp[n].max()), "max_sim_paper_sf": float(Sl[n].max()),
                      "closest_patent_sf": pats[int(Sp[n].argmax())]["id"]} for n, i in enumerate(ideas)}
W = {"novelty": .25, "non_obviousness": .20, "utility": .15, "feasibility": .10, "commercial": .15,
     "eligibility": .10}


def vendi(X: np.ndarray) -> float:
    if len(X) < 2:
        return float(len(X))
    K = (X @ X.T) / len(X)
    ev = np.clip(np.linalg.eigvalsh(K), 1e-12, None)
    return float(np.exp(-(ev * np.log(ev)).sum()))


def prior_art_snippets(pa: dict, k: int = 3) -> str:
    ids = [c["id"] for c in pa["closest"][:k]]
    rows = {r["id"]: r for r in store.fetch(f"id IN ({','.join('?' * len(ids))})", tuple(ids))} if ids else {}
    out = []
    for c in pa["closest"][:k]:
        r = rows.get(c["id"])
        body = (r["text"][:700] if r else "")
        out.append(f"  - [{c['type']} sim={c['sim']:.3f}] {c['id']} | {c['title']} | {c.get('who') or ''}\n    {body}")
    return "\n".join(out)


def judge(ideas: list[dict], pa: dict, batch: int = 8) -> dict:
    res = {}
    for b in range(0, len(ideas), batch):
        chunk = ideas[b:b + batch]
        blocks = []
        for i in chunk:
            blocks.append(f"### {i['id']}  ({i['arm']})  {i['title']}\nProblem: {i.get('problem', '')}\n"
                          f"Mechanism: {i.get('mechanism', '')}\nClaim core: {i.get('claim_core', '')}\n"
                          f"Closest prior art found:\n{prior_art_snippets(pa[i['id']]) if i['id'] in pa else '  (none)'}")
        ans = llm.ask_json(f"judge_{b // batch:03d}", JUDGE_SYSTEM, "Judge each idea.\n\n" + "\n\n".join(blocks),
                           JUDGE_SCHEMA, effort="high")
        if ans:
            res.update({j["id"]: j for j in ans["judgments"]})
    return res


def main():
    out = run_dir()
    ideas = load_ideas()
    pa = {r["id"]: r for r in json.loads((out / "prior_art.json").read_text())}
    J = judge(ideas, pa)
    X = embed.encode([idea_text(i) for i in ideas])
    LC = length_controlled(ideas)
    arms = np.array([i["arm"] for i in ideas])
    S = X @ X.T
    rows = []
    for n, i in enumerate(ideas):
        other = S[n][arms != i["arm"]]
        p = pa.get(i["id"], {})
        j = J.get(i["id"], {})
        row = {"id": i["id"], "arm": i["arm"], "title": i["title"], "domain": i.get("domain", ""),
               "problem": i.get("problem", ""), "mechanism": i.get("mechanism", ""),
               "claim_core": i.get("claim_core", ""),
               "novelty_pa": p.get("novelty_pa"), "max_sim_patent": p.get("max_sim_patent"),
               "max_sim_paper": p.get("max_sim_paper"),
               "closest_prior_art": " || ".join(f"{c['id']} ({c['sim']:.2f}) {c['title'][:80]}"
                                                for c in p.get("closest", [])[:3]),
               "cross_arm_sim": float(other.max()) if other.size else None,
               "words": len(idea_text(i).split()), **LC[i["id"]]}
        row.update({f"judge_{k}": j.get(k) for k in list(W) + ["crazy"]})
        row["verdict"], row["rationale"] = j.get("verdict"), j.get("rationale")
        if j:
            npa = row["novelty_pa"] or 0
            # automatic prior-art term: 10 at max_sim <= 0.65 (random-pair level), 0 at >= 0.85 (same invention)
            auto = float(np.clip((0.82 - row["max_sim_patent_sf"]) / 0.20 * 10, 0, 10))
            row["final_score"] = round(sum(W[k] * j[k] for k in W) + 0.05 * auto, 3)
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = []
    for arm, g in df.groupby("arm"):
        Xa = X[arms == arm]
        summary.append({
            "arm": arm, "n": len(g),
            "novelty_pa_mean": round(g.novelty_pa.mean(), 4), "novelty_pa_median": round(g.novelty_pa.median(), 4),
            "anticipated_rate": round((g.max_sim_patent >= ANTICIPATED).mean(), 3),
            "overlap_rate": round((g.max_sim_patent >= OVERLAP).mean(), 3),
            "max_sim_patent_median": round(g.max_sim_patent.median(), 4),
            "words_median": int(g.words.median()),
            "max_sim_patent_sf_median": round(g.max_sim_patent_sf.median(), 4),
            "anticipated_rate_sf": round((g.max_sim_patent_sf >= ANTICIPATED_SF).mean(), 3),
            "overlap_rate_sf": round((g.max_sim_patent_sf >= OVERLAP_SF).mean(), 3),
            "vendi": round(vendi(Xa), 2), "vendi_per_idea": round(vendi(Xa) / len(g), 3),
            "vendi_sf_per_idea": round(vendi(embed.encode([short_form(i) for i in ideas if i["arm"] == arm])) / len(g), 3),
            "cross_arm_sim_mean": round(g.cross_arm_sim.mean(), 4),
            **{f"judge_{k}_mean": round(g[f"judge_{k}"].mean(), 2) for k in list(W) + ["crazy"] if g[f"judge_{k}"].notna().any()},
            "pursue": int((g.verdict == "pursue").sum()), "refine": int((g.verdict == "refine").sum()),
            "drop_anticipated": int((g.verdict == "drop-anticipated").sum()),
            "drop_weak": int((g.verdict == "drop-weak").sum()),
            "final_score_mean": round(g.final_score.mean(), 3) if "final_score" in g else None})
    df = df.sort_values("final_score", ascending=False) if "final_score" in df else df
    EXPORTS.mkdir(exist_ok=True)
    df.to_csv(EXPORTS / "idea_register.csv", index=False)
    dump_json({"arms": summary, "judged": len(J), "pending": len(llm.pending())}, out / "evaluation.json")
    L.info("evaluation: %s", json.dumps(summary, default=str))
    return df, summary


if __name__ == "__main__":
    main()
