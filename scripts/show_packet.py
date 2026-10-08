"""Compact viewer for queued LLM prompt packets (operator aid in queue mode)."""
import sys
from pathlib import Path

for f in sys.argv[1:]:
    t = Path(f).read_text()
    body = t.split("## PROMPT")[1].split("## OUTPUT")[0]
    print(f"##### {Path(f).stem}")
    for blk in body.split("\n- id: ")[1:]:
        lines = blk.split("\n")
        get = lambda k: next((l.split(k + ":", 1)[1].strip() for l in lines if l.strip().startswith(k + ":")), "")
        print(f"{lines[0]} [{get('pool')[:3]}] {get('title')[:120]} || {get('abstract')[:380]}\n")
