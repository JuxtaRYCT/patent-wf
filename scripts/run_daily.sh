#!/usr/bin/env bash
# Daily run of the full patents-wf pipeline (both approaches).
# Schedule with launchd (scripts/com.patentswf.daily.plist), cron, or .github/workflows/daily.yml.
#
# LLM stages: with ANTHROPIC_API_KEY (or an `ant auth login` profile) they run automatically;
# otherwise prompt packets are queued in runs/<date>/llm_queue/ for an operator / Claude Code session,
# and re-running this script after answering them completes the remaining stages.
set -euo pipefail
cd "$(dirname "$0")/.."
source .venv/bin/activate
DATE=$(date +%F)
LOG=runs/$DATE/pipeline.log
mkdir -p runs/$DATE

step() { echo "=== $(date +%T) $*" | tee -a "$LOG"; }

step "1  gather (papers, patents, news, signals)"
python -m pipeline.gather >>"$LOG" 2>&1

step "2  novelty filtration (Approach 1 step 2)"
python -m pipeline.novelty >>"$LOG" 2>&1

step "3  synthesis / cross-pollination (Approach 1 step 3)"
python -m pipeline.synthesis >>"$LOG" 2>&1

step "A2 opportunity scanner (Approach 2 step 1)"
python -m pipeline.scanner >>"$LOG" 2>&1

step "F  prior-art filtration of all ideas (Approach 1+2 novelty detection)"
python -m pipeline.prior_art >>"$LOG" 2>&1

step "E  judge + evaluation"
python -m pipeline.evaluate >>"$LOG" 2>&1

step "4  knowledge graph + exports"
python -m pipeline.graph >>"$LOG" 2>&1
python -m pipeline.digest >>"$LOG" 2>&1
python -m pipeline.report >>"$LOG" 2>&1 || true
python -m integrations.sync --min-score 6.5 >>"$LOG" 2>&1 || true

PENDING=$(ls runs/$DATE/llm_queue 2>/dev/null | wc -l | tr -d ' ')
step "done. LLM packets queued (no API key): $PENDING"
