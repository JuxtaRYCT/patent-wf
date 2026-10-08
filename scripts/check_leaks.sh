#!/usr/bin/env bash
# Scan what is staged for secrets, personal data and local paths. Exit 1 on any hit.
cd "$(dirname "$0")/.."
PAT='gh[pousr]_[A-Za-z0-9]{20,}|sk-ant-|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|eyJ[A-Za-z0-9_-]{30,}|PRIVATE KEY|/Users/|/home/[a-z]|/private/tmp|@gmail\.com|claude\.ai/artifact|x-access-token: [A-Za-z0-9]'
hits=$(git grep --cached -I -n -E "$PAT" -- . ':!scripts/check_leaks.sh' | cut -c1-160)
bad=$(git diff --cached --name-only | grep -E '\.(sqlite|log|env|pem|key)$|^\.venv/|__pycache__')
big=$(git diff --cached --name-only | while read -r f; do [ -f "$f" ] && [ $(wc -c < "$f") -gt 20000000 ] && echo "$f"; done)
if [ -n "$hits$bad$big" ]; then echo "LEAK CHECK FAILED"; echo "$hits"; echo "$bad"; echo "$big"; exit 1; fi
echo "leak check passed ($(git diff --cached --name-only | wc -l | tr -d ' ') staged files)"
