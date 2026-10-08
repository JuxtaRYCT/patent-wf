"""Operator helper (queue mode): write a novelty_score response from compact rows.
Row format per line:  id | novelty | usefulness | note | tag1,tag2"""
import json, sys
from pathlib import Path
task, src = sys.argv[1], sys.argv[2]
rows = []
for line in Path(src).read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    i, n, u, note, tags = [x.strip() for x in line.split("|")]
    rows.append({"id": i, "novelty": int(n), "usefulness": int(u), "mechanism_or_problem": note,
                 "tags": [t.strip() for t in tags.split(",") if t.strip()]})
out = Path("runs/2026-09-30/llm_responses") / f"{task}.json"
out.write_text(json.dumps({"scores": rows}, indent=1))
print(task, len(rows))
