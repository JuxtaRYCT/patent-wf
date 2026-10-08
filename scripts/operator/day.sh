#!/usr/bin/env bash
# operator helper: run one pipeline stage for a catch-up day in queue mode.  day.sh 2026-10-02 novelty
cd "$(dirname "$0")/../.."
source .venv/bin/activate
export PATENTS_WF_DATE=$1 PATENTS_WF_EXECUTED_ON=${PATENTS_WF_EXECUTED_ON:-$(date +%F)} PATENTS_WF_LLM=queue
python -m pipeline.$2 2>&1 | grep -E " INFO (novelty summary|incoming|problem pool|pairs|themes|evaluation|graph:|digest|\[[0-9]+/[0-9]+\])|Error|Traceback" | cut -c1-260
