# patents-wf — automated novel-idea discovery for banking & finance patents

This repository implements both approaches from the brief and runs them end to end:

- **Approach 1**: gather (papers, patents, news) → novelty filtration → cross-pollination synthesis → knowledge graph
- **Approach 2**: AI Opportunity Scanner → filtration & novelty detection. It is run twice, zero-shot and signal-grounded, to test whether it actually produces novel concepts.

Results of the first run (2026-09-30) are in **`docs/REPORT.md`**. An interactive version is `exports/report.html` (open it in a browser). The best inventions, with draft claims and prior-art analysis, are in **`docs/dossiers/`**.

## Layout

```
config/config.yaml        every query, source, threshold and weight
pipeline/
  sources/papers.py       arXiv · Semantic Scholar · PubMed · Crossref · OpenAlex
  sources/ppubs.py        USPTO Patent Public Search (full-text US patents, abstract + claims)
  sources/patents.py      patent collection (PPUBS primary, Google Patents w/ circuit breaker, USPTO ODP)
  sources/news.py         RSS feeds · Google News RSS · Hacker News · GitHub search + trending
  sources/signals.py      CFPB complaint trends · Federal Register (Approach 2 demand signals)
  gather.py               step 1: run all collectors in parallel → SQLite
  embed.py                bge-base embeddings, cached per item
  novelty.py              step 2: dense+lexical novelty vs knowledge base, shortlist, LLM scoring
  synthesis.py            step 3: bisociation engine (problem × mechanism pairs → inventions)
  scanner.py              Approach 2: opportunity themes (pain, pull, push, momentum, whitespace)
  prior_art.py            filtration of every idea against local KB + live USPTO + Semantic Scholar
  evaluate.py             examiner-judge + arm metrics (novelty, anticipated rate, Vendi diversity)
  graph.py                step 4: knowledge graph (GraphML / JSON) + CSV exports
  report.py               figures
  llm.py                  Anthropic API backend, or queue mode (prompt packets) when no key
integrations/sync.py      push register to Notion / Airtable / Make.com / Zapier webhooks
scripts/run_daily.sh      whole pipeline; launchd plist + GitHub Actions workflow for daily runs
data/patents_wf.sqlite    all gathered items, embeddings, scores
ideas/                    A2a (zero-shot, frozen + hashed), A2b (scanner), A1 (cross-pollination)
runs/<date>/              run artefacts: manifests, novelty CSV, pairs, themes, prior art, LLM packets
exports/                  idea_register.csv, graph.graphml, graph.json, knowledge_graph.html
docs/                     REPORT, METHODOLOGY, RESEARCH_BRIEF, APPROACH2_ANALYSIS, PATENTABILITY, dossiers/
```

## Run it

```bash
uv venv --python 3.12 .venv && source .venv/bin/activate && uv pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # optional; without it LLM steps queue prompt packets
bash scripts/run_daily.sh           # or run the steps one at a time:
python -m pipeline.gather           # 1  data
python -m pipeline.novelty          # 2  filtration
python -m pipeline.synthesis        # 3  cross-pollination (Approach 1)
python -m pipeline.scanner          # A2 opportunity scanner
python -m pipeline.prior_art        # novelty detection for all ideas
python -m pipeline.evaluate         # judge + metrics → exports/idea_register.csv
python -m pipeline.graph && python -m pipeline.report
python -m integrations.sync --dry-run
```

Daily schedule: `sed "s|__REPO_DIR__|$PWD|g" scripts/com.patentswf.daily.plist > ~/Library/LaunchAgents/com.patentswf.daily.plist && launchctl load ~/Library/LaunchAgents/com.patentswf.daily.plist`

## Keys and settings (all optional)

| Variable | Used for |
|---|---|
| `ANTHROPIC_API_KEY` | LLM stages run unattended (`claude-opus-5`; override with `PATENTS_WF_MODEL`) |
| `GITHUB_TOKEN` | GitHub search. Falls back to `gh auth token` |
| `USPTO_PPUBS_TOKEN` | **Needed from 2026-11-07**, when USPTO Patent Public Search requires login |
| `USPTO_API_KEY` | USPTO Open Data Portal API |
| `NOTION_TOKEN`, `NOTION_DATABASE_ID` | Notion sync |
| `AIRTABLE_TOKEN`, `AIRTABLE_BASE_ID`, `AIRTABLE_TABLE` | Airtable sync |
| `MAKE_WEBHOOK_URL`, `ZAPIER_WEBHOOK_URL` | Make.com / Zapier (then on to Coda, Sheets, Slack …) |
