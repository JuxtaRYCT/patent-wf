"""Operator aid: compact view of the closest prior art per idea (from runs/<date>/prior_art.json)."""
import json, sys
from pipeline import store
pa = {r["id"]: r for r in json.load(open("runs/2026-09-30/prior_art.json"))}
ids = sys.argv[1:]
for i in ids:
    r = pa[i]
    print(f"=== {i} | {r['title'][:110]}")
    cl = r["closest"][:4]
    rows = {x["id"]: x for x in store.fetch(f"id IN ({','.join('?' * len(cl))})", tuple(c["id"] for c in cl))}
    for c in cl:
        t = (rows.get(c["id"], {}).get("text") or "").replace("\n", " ")
        print(f"  [{c['type'][:3]} {c['sim']:.3f}] {c['id']} | {c['title'][:90]} | {c.get('who') or ''}\n      {t[:420]}")
