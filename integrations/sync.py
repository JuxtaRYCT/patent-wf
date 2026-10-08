"""Push the idea register to Notion, Airtable, or a Make.com / Zapier webhook.

Every target is optional and activated purely by environment variables, so the daily job can run
unattended and skip what is not configured:

  NOTION_TOKEN + NOTION_DATABASE_ID     Notion database with properties:
                                        Name (title), Arm (select), Domain (select), Score (number),
                                        Novelty (number), Status (select), Closest prior art (rich_text),
                                        Mechanism (rich_text)
  AIRTABLE_TOKEN + AIRTABLE_BASE_ID + AIRTABLE_TABLE   table with the same field names
  MAKE_WEBHOOK_URL / ZAPIER_WEBHOOK_URL  receives one JSON POST per idea (Make "Custom webhook" /
                                        Zapier "Catch Hook" -> route to Notion, Coda, Sheets, Slack ...)

Usage:  python -m integrations.sync [--dry-run]
Source: exports/idea_register.csv (written by pipeline.evaluate).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "exports" / "idea_register.csv"


def _rows() -> list[dict]:
    df = pd.read_csv(REGISTER).fillna("")
    return df.to_dict("records")


def _txt(s, n=1900):
    return str(s)[:n]


def notion(rows: list[dict], dry: bool):
    tok, db = os.environ.get("NOTION_TOKEN"), os.environ.get("NOTION_DATABASE_ID")
    if not (tok and db):
        return "notion: skipped (NOTION_TOKEN / NOTION_DATABASE_ID not set)"
    h = {"Authorization": f"Bearer {tok}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
    n = 0
    for r in rows:
        props = {
            "Name": {"title": [{"text": {"content": _txt(f"{r['id']} {r['title']}", 200)}}]},
            "Arm": {"select": {"name": r["arm"]}},
            "Domain": {"select": {"name": _txt(r.get("domain") or "other", 90)}},
            "Score": {"number": float(r.get("final_score") or 0)},
            "Novelty": {"number": float(r.get("novelty_pa") or 0)},
            "Status": {"select": {"name": _txt(r.get("verdict") or "new", 90)}},
            "Closest prior art": {"rich_text": [{"text": {"content": _txt(r.get("closest_prior_art"))}}]},
            "Mechanism": {"rich_text": [{"text": {"content": _txt(r.get("mechanism"))}}]},
        }
        if dry:
            n += 1
            continue
        resp = requests.post("https://api.notion.com/v1/pages", headers=h, timeout=30,
                             json={"parent": {"database_id": db}, "properties": props})
        n += resp.ok
    return f"notion: {n}/{len(rows)} pages {'(dry run)' if dry else 'created'}"


def airtable(rows: list[dict], dry: bool):
    tok, base, table = (os.environ.get(k) for k in ("AIRTABLE_TOKEN", "AIRTABLE_BASE_ID", "AIRTABLE_TABLE"))
    if not (tok and base and table):
        return "airtable: skipped (AIRTABLE_TOKEN / AIRTABLE_BASE_ID / AIRTABLE_TABLE not set)"
    url = f"https://api.airtable.com/v0/{base}/{requests.utils.quote(table)}"
    h = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
    n = 0
    for b in range(0, len(rows), 10):            # Airtable: max 10 records per request
        recs = [{"fields": {"Name": f"{r['id']} {r['title']}", "Arm": r["arm"], "Domain": r.get("domain"),
                            "Score": float(r.get("final_score") or 0), "Novelty": float(r.get("novelty_pa") or 0),
                            "Status": r.get("verdict") or "new", "Closest prior art": _txt(r.get("closest_prior_art")),
                            "Mechanism": _txt(r.get("mechanism"))}} for r in rows[b:b + 10]]
        if dry:
            n += len(recs)
            continue
        resp = requests.post(url, headers=h, json={"records": recs, "typecast": True}, timeout=30)
        n += len(recs) if resp.ok else 0
    return f"airtable: {n}/{len(rows)} records {'(dry run)' if dry else 'created'}"


def webhooks(rows: list[dict], dry: bool):
    msgs = []
    for name in ("MAKE_WEBHOOK_URL", "ZAPIER_WEBHOOK_URL"):
        url = os.environ.get(name)
        if not url:
            msgs.append(f"{name}: skipped")
            continue
        ok = 0
        for r in rows:
            if dry:
                ok += 1
                continue
            ok += requests.post(url, json=r, timeout=30).ok
        msgs.append(f"{name}: {ok}/{len(rows)} posted")
    return "; ".join(msgs)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-score", type=float, default=0.0)
    a = ap.parse_args()
    if not REGISTER.exists():
        sys.exit(f"{REGISTER} missing - run `python -m pipeline.evaluate` first")
    rows = [r for r in _rows() if float(r.get("final_score") or 0) >= a.min_score]
    for fn in (notion, airtable, webhooks):
        print(fn(rows, a.dry_run))
