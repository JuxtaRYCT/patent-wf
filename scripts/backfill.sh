#!/usr/bin/env bash
# Catch up missed days: one gather for the whole gap, then one complete daily run per missed day.
#   bash scripts/backfill.sh 2026-10-01 2026-10-09
# Each day only sees data first available on or before that day (seen_day as-of filtering), so the outputs
# match what the daily job would have produced. Live prior-art searches use today's patent databases.
# With an Anthropic API key every stage completes unattended; in queue mode each LLM stage writes prompt
# packets to runs/<day>/llm_queue/ and the day must be re-run after they are answered.
set -euo pipefail
cd "$(dirname "$0")/.."
source .venv/bin/activate
FROM=$1; TO=$2
export PATENTS_WF_EXECUTED_ON=$(date +%F)
mkdir -p runs/$TO
echo "=== gather $FROM .. $TO"
PATENTS_WF_DATE=$TO PATENTS_WF_BACKFILL_FROM=$FROM python -m pipeline.gather >> runs/$TO/backfill_gather.log 2>&1
d=$FROM
while [[ "$d" < "$TO" || "$d" == "$TO" ]]; do
  echo "=== run $d"
  export PATENTS_WF_DATE=$d
  for stage in novelty synthesis scanner prior_art evaluate graph digest; do
    python -m pipeline.$stage >> runs/$d/pipeline.log 2>&1
  done
  d=$(python3 -c "import datetime as t;print(t.date.fromisoformat('$d')+t.timedelta(days=1))")
done
