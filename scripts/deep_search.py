"""Targeted prior-art queries (USPTO full text via PPUBS, relevance sorted) for dossier candidates."""
import sys, json
from pipeline.sources.ppubs import PPUBS
api = PPUBS()
Q = json.loads(sys.argv[1])
for label, qs in Q.items():
    print(f"##### {label}")
    seen = set()
    for q in qs:
        docs, n = api.search(q, 12, sort="score desc")
        print(f"  q: {q}  -> {n}")
        for d in docs[:8]:
            if d["documentId"] in seen: continue
            seen.add(d["documentId"])
            print(f"     {d['documentId']:<20} {(d.get('title') or '')[:110]}")
