"""Daily digest: runs/<date>/DIGEST.md for the run day and docs/DAILY_LOG.md across all runs.

A run executed later than its as-of date (catch-up after missed days) is labelled as such; it only saw data
first available on or before that day (store.fetch as-of filtering), so its outputs match what the daily job
would have produced, except that live prior-art searches use today's patent databases.
"""
from __future__ import annotations

import collections
import datetime as dt
import json
import os

import pandas as pd

from . import store
from .common import EXPORTS, ROOT, RUNS, dump_json, log, run_dir, today

L = log("digest")


def run_info(out) -> dict:
    f = out / "run_info.json"
    if f.exists():
        return json.loads(f.read_text())
    executed = os.environ.get("PATENTS_WF_EXECUTED_ON") or dt.date.today().isoformat()
    info = {"as_of": today(), "executed_on": executed, "mode": "catch-up" if executed > today() else "daily"}
    dump_json(info, f)
    return info


def _load(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def digest(run: str | None = None) -> dict:
    out = run_dir(run)
    info = run_info(out)
    D = info["as_of"]
    new = store.fetch("seen_day = ?", (D,))
    by_kind = collections.Counter(r["kind"] for r in new)
    comp = [r for r in new if r["pool"] == "competitor"]
    nov = pd.read_csv(out / "novelty_incoming.csv") if (out / "novelty_incoming.csv").exists() else pd.DataFrame()
    ns = _load(out / "novelty_summary.json", {})
    sel = _load(out / "scanner_selected.json", [])
    ev = _load(out / "evaluation.json", {})
    reg = pd.read_csv(EXPORTS / "idea_register.csv") if (EXPORTS / "idea_register.csv").exists() else pd.DataFrame()
    today_ideas = reg[reg.run == D].sort_values("final_score", ascending=False) if len(reg) and "run" in reg else reg.iloc[0:0]

    L_ = [f"# Run {D}", ""]
    if info["mode"] == "catch-up":
        L_ += [f"> Catch-up run executed on {info['executed_on']} for the missed day {D}. Every stage saw only data "
               f"first available on or before {D}. Live prior-art searches used the patent databases as of "
               f"{info['executed_on']}.", ""]
    L_ += ["## Data that arrived this day", "",
           "| kind | items |", "|---|---|"] + [f"| {k} | {v} |" for k, v in by_kind.most_common()] + [""]
    if comp:
        L_ += [f"**Competitor filings published ({len(comp)})**", ""]
        L_ += [f"- {r['title'][:110]} — {(r['meta'].get('applicant') or '')[:40]} ({r['url']})" for r in comp[:12]] + [""]
    if ns:
        L_ += ["## Novelty filter", "",
               f"Incoming {ns.get('incoming', 0)} · relevant {ns.get('eligible', 0)} · shortlisted {ns.get('shortlisted', 0)} · "
               f"near-duplicates dropped {ns.get('near_duplicates', 0)}", ""]
    if len(nov) and "llm_usefulness" in nov:
        top = nov[nov.llm_usefulness.notna()].sort_values(["llm_usefulness", "novelty"], ascending=False)
        for pool, label in (("finance", "Most useful new finance problems"), ("crossdomain", "Most transferable new mechanisms")):
            t = top[top.pool == pool].head(5)
            if len(t):
                L_ += [f"**{label}**", ""] + [f"- ({int(r.llm_usefulness)}/10) {r.title[:110]} — {r.llm_note}"
                                               for r in t.itertuples()] + [""]
    if sel:
        L_ += ["## Scanner themes ideated today (fresh signals, not ideated before)", ""]
        L_ += [f"- T{t['theme']:02d} {t['terms'][:80]} — opportunity {t['opportunity']:.2f}, {t['new_signals']} new signals"
               for t in sel] + [""]
    if len(today_ideas):
        L_ += ["## Ideas generated today", "", "| ID | Idea | Verdict | Score | Novelty | Repeats earlier idea |",
               "|---|---|---|---|---|---|"]
        for r in today_ideas.itertuples():
            sc = f"{r.final_score:.2f}" if pd.notna(r.final_score) else "–"
            nv = int(r.judge_novelty) if pd.notna(r.judge_novelty) else "–"
            dup = r.dup_of if isinstance(r.dup_of, str) else ""
            L_.append(f"| {r.id} | {r.title} | {r.verdict or 'pending'} | {sc} | {nv} | {dup} |")
        L_.append("")
    if ev.get("arms"):
        L_ += ["## Arm statistics today", "", "| arm | n | novelty | utility | pursue | refine | dropped |", "|---|---|---|---|---|---|---|"]
        for a in ev["arms"]:
            L_.append(f"| {a['arm']} | {a['n']} | {a.get('judge_novelty_mean', '–')} | {a.get('judge_utility_mean', '–')} | "
                      f"{a['pursue']} | {a['refine']} | {a['drop_anticipated'] + a['drop_weak']} |")
        L_.append("")
    (out / "DIGEST.md").write_text("\n".join(L_))
    summary = {"run": D, "mode": info["mode"], "executed_on": info["executed_on"], "new_items": len(new),
               "new_patents": by_kind.get("patent", 0), "competitor_filings": len(comp),
               "shortlisted": ns.get("shortlisted", 0), "themes": len(sel),
               "ideas_A1": int((today_ideas.arm == "A1").sum()) if len(today_ideas) else 0,
               "ideas_A2b": int((today_ideas.arm == "A2b").sum()) if len(today_ideas) else 0,
               "pursue": int((today_ideas.verdict == "pursue").sum()) if len(today_ideas) else 0,
               "refine": int((today_ideas.verdict == "refine").sum()) if len(today_ideas) else 0,
               "dropped": int(today_ideas.verdict.astype(str).str.startswith("drop").sum()) if len(today_ideas) else 0,
               "top_idea": f"{today_ideas.iloc[0].id} {today_ideas.iloc[0].title}" if len(today_ideas) and pd.notna(today_ideas.iloc[0].final_score) else ""}
    dump_json(summary, out / "digest_summary.json")
    return summary


def daily_log():
    rows = [_load(d / "digest_summary.json", None) for d in sorted(RUNS.iterdir()) if d.is_dir()]
    rows = [r for r in rows if r]
    L_ = ["# Daily log", "", "One row per run. Each run's full digest is in `runs/<date>/DIGEST.md`. "
          "The first run (2026-09-30) is documented in `docs/REPORT.md`.", "",
          "| Run | Mode | New items | New patents | Competitor filings | Shortlisted | Themes | A1 ideas | A2b ideas | Pursue | Refine | Dropped | Best idea |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L_.append(f"| {r['run']} | {r['mode']} | {r['new_items']} | {r['new_patents']} | {r['competitor_filings']} | "
                  f"{r['shortlisted']} | {r['themes']} | {r['ideas_A1']} | {r['ideas_A2b']} | {r['pursue']} | "
                  f"{r['refine']} | {r['dropped']} | {r['top_idea'][:90]} |")
    (ROOT / "docs" / "DAILY_LOG.md").write_text("\n".join(L_) + "\n")


def main():
    s = digest()
    daily_log()
    L.info("digest %s: %s", s["run"], s)


if __name__ == "__main__":
    main()
