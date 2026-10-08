"""Operator helper (queue mode): write synthesis / scanner answers for a run from a dict of ideas keyed by
pair (X###) or theme (T##). Packets are matched by the ids they contain, so answers can't land in the wrong packet."""
import json, re, sys
from pathlib import Path


def write(run: str, kind: str, ideas_by_key: dict):
    q = Path("runs") / run / "llm_queue"
    r = Path("runs") / run / "llm_responses"
    r.mkdir(parents=True, exist_ok=True)
    pat = r"^### PAIR (X\d{3})" if kind == "synthesis" else r"^### THEME (T\d{2})"
    field = "pair" if kind == "synthesis" else "theme"
    used = set()
    for f in sorted(q.glob(f"{kind}_*.md")):
        keys = re.findall(pat, f.read_text(), re.M)
        out = [dict({field: k}, **i) for k in keys for i in ideas_by_key.get(k, [])]
        used |= set(keys)
        (r / f"{f.stem}.json").write_text(json.dumps({"ideas": out}, indent=1, ensure_ascii=False))
        print(f.stem, keys, len(out))
    missing = set(ideas_by_key) - used
    assert not missing, f"keys not in any packet: {missing}"


def judge(run: str, J: dict):
    """J: id -> (novelty, non_obv, utility, feasibility, commercial, eligibility, crazy, verdict, rationale)."""
    q = Path("runs") / run / "llm_queue"
    r = Path("runs") / run / "llm_responses"
    r.mkdir(parents=True, exist_ok=True)
    keys = ["novelty", "non_obviousness", "utility", "feasibility", "commercial", "eligibility", "crazy"]
    used = set()
    for f in sorted(q.glob("judge_*.md")):
        ids = re.findall(r"^### (\S+)\s+\(", f.read_text(), re.M)
        out = []
        for i in ids:
            v = J[i]
            out.append(dict(id=i, **dict(zip(keys, v[:7])), verdict=v[7], rationale=v[8]))
        used |= set(ids)
        (r / f"{f.stem}.json").write_text(json.dumps({"judgments": out}, indent=1, ensure_ascii=False))
        print(f.stem, len(out))
    assert not set(J) - used, set(J) - used
