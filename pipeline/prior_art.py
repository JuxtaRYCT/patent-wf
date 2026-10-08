"""Prior-art check for generated ideas (shared by Approach 1 and Approach 2 - "Filtration & novelty").

For each idea:
  1. local search  : dense similarity to every patent / paper already in the knowledge base
  2. live USPTO    : BRS queries built from the idea's *distinctive* terms (TF-IDF weight relative to
                     the patent KB, i.e. words the idea uses that patents rarely use), title-embedding
                     pre-rank, then abstract + claim 1 fetched for the best hits and embedded
  3. live papers   : Semantic Scholar relevance search on the idea title
  novelty_pa = 1 - max similarity to anything found; closest 5 are kept for human/LLM review.
Fetched patents are added to the KB so every later run starts from a larger prior-art base.
"""
from __future__ import annotations

import itertools
import json
import re

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from . import embed, store
from .common import IDEAS, dump_json, log, run_dir
from .sources import papers as paper_src
from .sources.ppubs import PPUBS, to_item

L = log("prior_art")
ANCHOR = "(bank OR banking OR payment OR financial OR transaction OR account OR credit)"


def idea_text(i: dict) -> str:
    return ". ".join(str(i.get(k, "")) for k in ("title", "problem", "mechanism", "claim_core") if i.get(k))


FIRST_RUN = "2026-09-30"   # first run kept its idea files at the top of ideas/; later runs use ideas/<date>/


def idea_files(run: str | None = None) -> list:
    files = [(FIRST_RUN, f) for f in sorted(IDEAS.glob("A*.json"))]
    files += [(d.name, f) for d in sorted(IDEAS.iterdir()) if d.is_dir() for f in sorted(d.glob("A*.json"))]
    return [(r, f) for r, f in files if run is None or r == run]


def load_ideas(run: str | None = None) -> list[dict]:
    """Ideas of one run, or of every run up to the as-of date (run=None)."""
    from .common import today
    ideas = []
    for r, f in idea_files(run):
        if r > today():
            continue
        d = json.loads(f.read_text())
        for i in d["ideas"]:
            i["arm"], i["run"] = d["arm"], r
            ideas.append(i)
    return ideas


class TermPicker:
    """Distinctive-term extractor: idea terms weighted by IDF over the patent KB."""

    def __init__(self, patent_texts: list[str]):
        self.tf = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1, max_df=0.2,
                                  token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z-]{2,}\b")
        self.tf.fit(patent_texts)
        self.vocab = np.array(self.tf.get_feature_names_out())
        self.generic = set("method system systems methods data user users device devices based using "
                           "computing computer plurality configured one first second value values information "
                           "determine determining include including real time".split())

    def terms(self, text: str, k: int = 6) -> list[str]:
        v = self.tf.transform([text]).toarray().ravel()
        out = []
        for j in v.argsort()[::-1]:
            if v[j] <= 0 or len(out) >= k:
                break
            t = self.vocab[j]
            if any(w in self.generic for w in t.split()) or any(t in o or o in t for o in out):
                continue
            out.append(t)
        return out


def brs(term: str) -> str:
    w = term.split()
    return w[0] if len(w) == 1 else "(" + " ADJ ".join(w) + ")"


def check(ideas: list[dict], per_query: int = 40, fetch_top: int = 12) -> list[dict]:
    patents = store.fetch("kind='patent'")
    lit = store.fetch("kind='paper'")
    Xpat, Xlit = embed.ensure(patents), embed.ensure(lit)
    picker = TermPicker([embed.doc_text(p, 1200) for p in patents])
    api = PPUBS()
    Xi = embed.encode([idea_text(i) for i in ideas])
    known = {p["meta"].get("doc_id") for p in patents}
    results = []
    for n, (idea, xi) in enumerate(zip(ideas, Xi)):
        terms = picker.terms(idea_text(idea))
        queries = [f"{brs(a)} AND {brs(b)}" for a, b in itertools.combinations(terms[:4], 2)][:5]
        queries.append(f"({' OR '.join(brs(t) for t in terms[:3])}) AND {ANCHOR}")
        cand = {}
        for q in queries:
            docs, _ = api.search(q + " AND @pd>=20100101", per_query, sort="score desc")
            for d in docs:
                cand.setdefault(d["documentId"], d["title"] or "")
        ranked = []
        if cand:
            ids = list(cand)
            tv = embed.encode([cand[i] for i in ids])
            ranked = [ids[j] for j in np.argsort(-(tv @ xi))[:fetch_top] if ids[j] not in known]
        fetched = [to_item(d, "prior_art", f"idea:{idea['id']}") for d in api.details(ranked)] if ranked else []
        if fetched:
            store.upsert(fetched)
            known |= {f["meta"]["doc_id"] for f in fetched}
        # live literature
        s2 = paper_src.arxiv_search(terms, 15) + paper_src.arxiv_search(terms[1:4], 10) + \
            paper_src.s2_search(idea["title"], 10)
        pool = [(p, "patent") for p in patents] + [(p, "paper") for p in lit]
        X = [Xpat, Xlit]
        extra = [(f, "patent") for f in fetched] + [(dict(p, source="semantic_scholar"), "paper") for p in s2 if p.get("text")]
        if extra:
            X.append(embed.encode([embed.doc_text(p) for p, _ in extra]))
            pool += extra
        Xall = np.vstack(X)
        sims = Xall @ xi
        order = np.argsort(-sims)[:8]
        closest = [{"id": pool[j][0]["id"], "type": pool[j][1], "sim": round(float(sims[j]), 4),
                    "title": pool[j][0]["title"][:160], "url": pool[j][0].get("url"),
                    "who": (pool[j][0].get("meta") or {}).get("applicant") or (pool[j][0].get("meta") or {}).get("assignee")}
                   for j in order]
        is_pat = np.array([t == "patent" for _, t in pool])
        max_pat = float(sims[is_pat].max()) if is_pat.any() else 0.0
        max_pap = float(sims[~is_pat].max()) if (~is_pat).any() else 0.0
        results.append({"id": idea["id"], "arm": idea["arm"], "title": idea["title"], "terms": terms,
                        "queries": queries, "uspto_candidates": len(cand), "fetched": len(fetched),
                        "max_sim_patent": round(max_pat, 4), "max_sim_paper": round(max_pap, 4),
                        "novelty_pa": round(1 - max(max_pat, max_pap), 4), "closest": closest})
        L.info("[%d/%d] %s max_pat=%.3f max_pap=%.3f cand=%d fetched=%d", n + 1, len(ideas), idea["id"],
               max_pat, max_pap, len(cand), len(fetched))
        # refresh KB matrices so later ideas also see newly fetched patents
        if fetched:
            patents += fetched
            Xpat = np.vstack([Xpat, X[2][:len(fetched)]])
    return results


def main(arms: list[str] | None = None):
    from .common import today
    ideas = [i for i in load_ideas(today()) if not arms or i["arm"] in arms]
    res = check(ideas)
    out = run_dir()
    prev = {}
    f = out / "prior_art.json"
    if f.exists():
        prev = {r["id"]: r for r in json.loads(f.read_text())}
    prev.update({r["id"]: r for r in res})
    dump_json(list(prev.values()), f)
    L.info("prior-art results for %d ideas -> %s", len(res), f)
    return res


if __name__ == "__main__":
    import sys
    main(sys.argv[1:] or None)
