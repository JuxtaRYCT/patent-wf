"""For each dossier: run BRS queries (relevance-sorted) and print abstract + claim-1 head of top hits."""
import sys, json
from pipeline.sources.ppubs import PPUBS
api = PPUBS()
Q = json.loads(sys.argv[1]); k = int(sys.argv[2]) if len(sys.argv) > 2 else 3
for label, qs in Q.items():
    print(f"##### {label}")
    ids = []
    for q in qs:
        docs, n = api.search(q, 6, sort="score desc")
        ids += [d["documentId"] for d in docs[:k] if d["documentId"] not in ids]
    for x in api.details(ids):
        print(f"  {x['doc_id']} | {x['title'][:90]} | {x['applicant'][:40]} | filed {(x['filed'] or [''])[0][:10]}")
        print(f"     ABS: {x['abstract'][:330]}")
        print(f"     C1: {x['claim1'][:330]}")
