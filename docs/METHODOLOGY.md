# Methodology — how both approaches were implemented and run

This document maps each box of the original brief to the code that implements it, records what was verified about each data source on 2026-09-30, and explains the design decisions.

```
                    ┌──────────────────────── APPROACH 1 ────────────────────────┐
 arXiv, S2, PubMed, │ 1 gather ─► 2 novelty filter ─► 3 bisociation synthesis ─┐ │
 Crossref, USPTO,   │   (SQLite)   (dense+lexical vs KB,   (problem × mechanism   │ │
 RSS, HN, GitHub ───┤              LLM scoring)            pairs, MMR, LLM)      │ │
                    └──────────────────────────────────────────────────────────┼─┘
                    ┌──────────────────────── APPROACH 2 ─────────────────────┐ │
 CFPB, Fed. Reg.,   │ 1 opportunity scanner                                    │ │
 news, HN, USPTO ───┤   A2a zero-shot LLM (frozen baseline)                    │ │
                    │   A2b themes = clusters × pain/pull/push/momentum/       │ │
                    │        whitespace → LLM ideas                            │ │
                    └──────────────────────────────────────────────────────────┤ │
                                                                               ▼ ▼
                    2 FILTRATION & NOVELTY DETECTION (shared, prior_art.py)
                      local KB + live USPTO full text + Semantic Scholar → novelty_pa
                      LLM examiner judge vs closest prior art → verdict
                                       │
                    4 STORAGE & KNOWLEDGE GRAPH → SQLite, GraphML/JSON, HTML graph,
                      CSV register → Notion / Airtable / Make / Zapier (integrations/sync.py)
```

## Approach 1

### 1. Data gathering — `pipeline/gather.py`, `pipeline/sources/*`
| Brief item | Implemented with | Verified status (2026-09-30) |
|---|---|---|
| 1a arXiv API | `papers.arxiv_query` — 8 finance queries (q-fin.*, bank/payment/fraud/credit/AML/stablecoin/agentic in cs.*) + 18 "unrelated" categories (quant-ph, q-bio.PE/NC/MN, physics.soc-ph, nlin.AO, cs.RO, eess.SY …) for the mechanism pool | ✅ works, 3 s pacing as arXiv requests |
| 1a Semantic Scholar | `/paper/search/bulk`, 20 finance queries, sorted by publication date | ✅ works; throttles anonymous callers (429) → retry/backoff built in |
| 1a PubMed | E-utilities esearch+efetch, 10 biology-mechanism queries (immune memory, quorum sensing, epidemic tracing, circadian/voice/typing biomarkers …) | ✅ works |
| (extra) Crossref, OpenAlex | journals with abstracts; OpenAlex used only for ad-hoc search | ✅ Crossref; ⚠️ OpenAlex now rate-limits anonymous search (free key needed) |
| 1b Google Patents RSS | **No RSS exists any more.** Used the `xhr/query` JSON endpoint behind patents.google.com | ⚠️ works but Google serves a "Sorry…" 503 captcha after a burst → pipeline has a circuit breaker and falls back to USPTO |
| 1b USPTO dumps | **USPTO Patent Public Search (PPUBS) JSON API** — discovered and wrapped in `sources/ppubs.py` (session token → BRS query → full abstract + claims) ; ODP API wrapper for when `USPTO_API_KEY` is set | ✅ PPUBS works anonymously **until 2026-11-07**, when USPTO requires login (set `USPTO_PPUBS_TOKEN`). ODP API returns 401 without key. PatentsView legacy API is gone. |
| 1b competitor filings | 20 assignee queries (JPMorgan, BofA, Capital One, Wells, Visa, Mastercard, Amex, PayPal, Stripe, Coinbase, Citi, TD, RBC, Block, Truist, US Bank, Infosys, TCS, Barclays, HSBC) — latest publications | ✅ |
| 1c RSS / Feedly / Inoreader | 19 direct feeds (Finextra, PYMNTS, Financial Brand, Banking/Payments Dive, TechCrunch fintech, CoinDesk, Fed, ECB, RBI, FCA, BoE, Fintech Business Weekly, Net Interest, Medianama …) + 11 Google News RSS searches. Feedly/Inoreader are paid wrappers over the same feeds — not required. | ✅ 15/19 feeds live; 4 dead URLs logged (Fintech Futures 403, BIS 404, Brainfood 404, Inc42 404) |
| 1c GitHub trending | trending page scrape + GitHub search API (topics: fintech, banking, payments, fraud-detection, open-banking, stablecoin, defi, credit-scoring, aml; created in last 90 days) using the local `gh` token | ✅ (anonymous API limit hit immediately — token required) |
| (extra) Hacker News | Algolia API, 7 finance queries, points>20 | ✅ |

All items land in `data/patents_wf.sqlite` (`items`, `vectors`, `scores` tables) with first-seen dates, so each day's run knows what is genuinely new.

### 2. Filtration & novelty detection — `pipeline/novelty.py`
- **Knowledge base (KB)** = every patent + regulation + literature older than the look-back window + everything seen on earlier runs.
- **Incoming** = papers/news/repos/posts first seen today and published within 45 days.
- **Vector embeddings**: `BAAI/bge-base-en-v1.5` (768-d, runs locally on Apple-silicon GPU via MPS; vectors cached in SQLite).
- **Similarity thresholding**: `dense_max` (nearest KB neighbour), `dense_top5`, and `lex_max` (TF-IDF 1–2-gram cosine). The lexical term catches shared rare terminology that embeddings blur. `novelty = 1 − (0.75·dense_max + 0.25·lex_max)`. Near-duplicates (cos > 0.92) are dropped. `buzz` counts near neighbours within the incoming batch: a trend signal, kept separate from novelty.
- **Shortlist**: top 20% novelty per pool (finance / cross-domain).
- **LLM scoring of the shortlist**: the top 150 per pool are scored for novelty (1–10) and usefulness (1–10). For cross-domain items the LLM extracts the **transferable mechanism**; for finance items, the **open problem**.

### 3. Synthesis & cross-pollination — `pipeline/synthesis.py`
The bisociation engine (Koestler), essentially Swanson's ABC model run in reverse:
1. Problem pool P (finance, shortlisted) × mechanism pool M (cross-domain, shortlisted).
2. Semantic distance for every pair; keep the **55th–85th percentile band** ("far but bridgeable": close pairs give obvious combinations, very distant pairs give nonsense).
3. **Fused-vector prior-art pre-check**: normalise(p+m) is compared with the patent KB, and pairs whose fusion already sits next to a patent are demoted.
4. **MMR selection** of 60 pairs, with no problem or mechanism used more than twice.
5. **Structured prompt** (6 pairs per call): propose 0–2 inventions per pair with a concrete technical mechanism, the technical effect, why it is non-obvious, a claim core and search keywords.

### 4. Storage & knowledge graph — `pipeline/graph.py`, `integrations/sync.py`
- Graph nodes: ideas, sources, prior art, themes, domains, arms. Edges: DERIVED_FROM, ADDRESSES, SIMILAR_TO{sim}, IN_DOMAIN, FROM_ARM, NEAR{sim}.
- Exports: `exports/graph.graphml` (Gephi/yEd), `exports/graph.json` (node-link), `exports/knowledge_graph.html` (interactive), `exports/idea_register.csv` (the Notion/Airtable/Coda import file).
- `integrations/sync.py` pushes the register to **Notion** (API), **Airtable** (API) and **Make.com / Zapier** (webhooks). Each target is enabled by environment variables and silently skipped otherwise.

## Approach 2

### 1. AI Opportunity Scanner — two arms, run separately so they can be compared
- **A2a zero-shot** (`ideas/A2a_zero_shot_scanner.json`): the LLM asked directly for 30 novel patentable banking ideas **before any data was gathered**. The file was SHA-256-hashed at creation to prove it was not revised after seeing the data. This is the arm that tests whether *an AI opportunity scanner really works for novel concepts*.
- **A2b signal-grounded** (`pipeline/scanner.py`): the signal corpus is Federal Register rules/notices + news + HN + CFPB complaint-trend pseudo-documents. It is clustered into 30 themes, and each theme is scored on
  - **pain**: CFPB volume × growth lift, plus fraud/scam/consumer mentions
  - **pull**: regulatory documents in the theme
  - **momentum**: share of signals from the last 14 days
  - **push**: novel finance papers near the theme centroid
  - **whitespace**: inverse of patent density near the centroid (KB) blended with live USPTO hit counts for the theme's key terms
  - `opportunity = Σ w·z(score)`. The top 12 themes go to the LLM, which proposes 2–3 inventions each.

### 2. Filtration & novelty detection — `pipeline/prior_art.py`, `pipeline/evaluate.py`
The same procedure is applied to every arm:
1. **Local KB** dense search over all patents and papers.
2. **Live USPTO full-text search**. BRS queries are built from the idea's *distinctive* terms (TF-IDF weighted against the patent KB, so we search for the words that make the idea unusual). Titles are pre-ranked by embedding; the best 12 hits get abstract + claim 1 fetched, embedded and added to the KB.
3. **Live literature search** via Semantic Scholar.
4. `novelty_pa = 1 − max similarity`, and the closest 8 items are kept.
5. **LLM examiner judge**: it sees the idea next to the closest prior-art abstracts/claims and scores novelty, non-obviousness, utility, feasibility, commercial value, eligibility and "crazy" (surprising but credible), then gives a verdict: pursue / refine / drop-anticipated / drop-weak.
6. **Arm-level metrics**: novelty distribution, anticipated rate, **Vendi score** (effective number of distinct ideas), cross-arm similarity (homogenisation), judge means and verdict counts.

## The LLM stage in this run
No Anthropic API key was configured on this machine, so `pipeline/llm.py` ran in **queue mode**. Every LLM call was written as a prompt packet (`runs/2026-09-30/llm_queue/*.md`) and answered by Claude Opus 5.5 inside the Claude Code session that built the pipeline. The answers are stored verbatim in `runs/2026-09-30/llm_responses/*.json`. With `ANTHROPIC_API_KEY` set, the same packets go to the Messages API (`claude-opus-5`, JSON-schema structured output, adaptive thinking, prompt caching, server-side refusal fallback) and the pipeline runs unattended.

**Caveat, recorded honestly:** in this run the same model generated and judged the ideas. LLM self-evaluation is known to be unreliable (Si et al. 2024). That is why the *automatic* prior-art similarity (`novelty_pa`) is reported alongside the judge scores, and why the top ideas' closest patents were read and quoted by hand in the dossiers.

## Daily operation
`scripts/run_daily.sh` runs every stage. Schedule it with launchd (`scripts/com.patentswf.daily.plist`, 06:30 daily) or GitHub Actions (`.github/workflows/daily.yml`). Because first-seen dates are stored, each day's novelty filter compares only that day's new items against everything seen before.
