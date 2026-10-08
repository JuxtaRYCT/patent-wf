"""LLM backend for the reasoning stages (novelty scoring, synthesis, prior-art judging).

Two backends:
  api    - Anthropic Messages API (used automatically when credentials resolve: ANTHROPIC_API_KEY,
           ANTHROPIC_AUTH_TOKEN or an `ant auth login` profile). JSON-schema structured output,
           adaptive thinking, automatic prompt caching, server-side refusal fallback.
  queue  - no credentials: every call is written as a prompt packet to runs/<date>/llm_queue/<task>.md
           and the answer is read from runs/<date>/llm_responses/<task>.json. An operator (a human, or a
           Claude Code session as in the 2026-09-30 run) answers the packets, then the stage is re-run.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from .common import ROOT, log, run_dir

L = log("llm")
MODEL = os.environ.get("PATENTS_WF_MODEL", "claude-opus-5")


def _client():
    if os.environ.get("PATENTS_WF_LLM") == "queue":
        return None
    try:
        import anthropic
        c = anthropic.Anthropic()
        return c if (c.api_key or c.auth_token) else None
    except Exception:
        return None


_CLIENT = _client()
BACKEND = "api" if _CLIENT else "queue"


def ask_json(task_id: str, system: str, prompt: str, schema: dict, effort: str = "high",
             run: str | None = None) -> dict | None:
    """Return parsed JSON matching `schema`, or None if queued / unanswered."""
    if BACKEND == "api":
        return _ask_api(system, prompt, schema, effort)
    return _ask_queue(task_id, system, prompt, schema, run)


def _ask_api(system: str, prompt: str, schema: dict, effort: str) -> dict | None:
    import anthropic
    try:
        resp = _CLIENT.beta.messages.create(
            model=MODEL,
            max_tokens=16000,
            system=system,
            thinking={"type": "adaptive"},
            output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
            cache_control={"type": "ephemeral"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.RateLimitError as e:
        L.warning("rate limited: %s", e.message)
        return None
    except anthropic.APIStatusError as e:
        L.error("API error %s: %s", e.status_code, e.message)
        return None
    except anthropic.APIConnectionError as e:
        L.error("connection error: %s", e)
        return None
    if resp.stop_reason == "refusal":
        L.warning("refused: %s", resp.stop_details)
        return None
    text = next((b.text for b in resp.content if b.type == "text"), None)
    return json.loads(text) if text else None


def _ask_queue(task_id: str, system: str, prompt: str, schema: dict, run: str | None) -> dict | None:
    d = run_dir(run)
    resp = d / "llm_responses" / f"{task_id}.json"
    if resp.exists():
        return json.loads(resp.read_text())
    q = d / "llm_queue" / f"{task_id}.md"
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(f"# TASK {task_id}\n\n## SYSTEM\n{system}\n\n## PROMPT\n{prompt}\n\n## OUTPUT JSON SCHEMA\n"
                 f"```json\n{json.dumps(schema, indent=1)}\n```\n\nWrite the answer to: {resp.relative_to(ROOT)}\n")
    return None


def pending(run: str | None = None) -> list[Path]:
    d = run_dir(run)
    return sorted(p for p in (d / "llm_queue").glob("*.md")
                  if not (d / "llm_responses" / f"{p.stem}.json").exists())
