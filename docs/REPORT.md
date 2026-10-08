# Patent idea discovery for banking & finance: run report (2026-09-30)

## TL;DR
- **Both approaches were built and run end to end** on live data: 10,428 items gathered in one day (4,770 patents, 3,957 papers, 1,037 news items, 338 regulations, 274 repos, 52 posts, plus 127 CFPB complaint-issue trends), then filtered, synthesised, prior-art checked and judged.
- **69 inventions generated** across three arms. **8 filing-grade dossiers** are written (`docs/dossiers/`) with draft claims, prior-art distinctions, eligibility notes (US / India / EPO) and proof-of-concept plans.
- **Main finding:** an AI "opportunity scanner" asked directly for novel ideas mostly returns ideas that already exist (**87% already existing, 0 survivors**). Grounding the scanner in live demand signals and patent whitespace, and filtering hard with a two-stage prior-art check, gives the best surviving inventions. Cross-pollination gives the most surprising ideas, but 4 of its 5 initial winners turned out to be already published in academic work. Details are in `APPROACH2_ANALYSIS.md`.

## The 8 filing candidates

| # | ID | Invention | Why it matters | Score |
|---|---|---|---|---|
| 1 | A1-16 | **Reachability-certified pre-emptive holds.** Compute where stolen money *can* reach before it gets there, and place signed, amount-capped, auto-expiring holds on the minimum separating set of accounts across banks. | Moves fraud recovery (India 1930/CFCFRMS, UK APP, Pix MED) from chasing hops to intercepting ahead. No prior art found. | 7.42 |
| 2 | A2b-06 | **Signed tradeline provenance.** Each reported credit field carries a signed commitment to its source record. Disputes become a challenge-response proof, with automatic correction or suppression if the SLA is missed. | 238k US complaints about 'investigation took more than 30 days' (1.41× growth). RBI's ₹100/day compensation rule, with CIBIL, CRIF and Equifax penalised in Aug 2026. | 7.05 |
| 3 | A2b-01 | **Unpredictable-quorum confirmation.** An out-of-pattern treasury instruction triggers a verifiable-random draw of co-approvers, who are contacted only on bank-initiated, device-bound channels. | Direct answer to the €95M voice-clone and fake-WhatsApp transfer (Sept 2026). The attacker can't know whom else to impersonate. | 6.94 |
| 4 | A2b-07 | **Mixed-file splitting with consumer-held credentials.** A credential-bound 'not mine' becomes a persistent hard constraint in bureau entity resolution. Open-banking payment evidence blocks fake disownment. | 895k complaints in 120 days that report information belongs to someone else. | 6.61 |
| 5 | A2b-08 | **Agent-herding detection.** The network flags scam storefronts when many users' AI shopping agents suddenly converge on a thin-history merchant, measured against a human-discovery baseline and weighted by agent-platform concentration. | Banks are publicly warning about AI shopping-bot fraud, and behaviour signals disappear with agents. | 6.57 |
| 6 | A1-12 | **Channel-watermarked OTPs and a honey session.** A distinct code per delivery channel reveals which channel leaked; the compromised session is diverted into a shadow-ledger sandbox that harvests mule accounts. | India's SMS-OTP theft through fake apps. Turns blocking into intelligence. | 6.55 |
| 7 | A1-04 | **Co-presence receipts.** Concurrent UWB ranging produces mutually signed proximity receipts used for authorisation *and* as exculpatory evidence. | Relay attacks and CEO fraud, and people wrongly accused by facial-recognition matches. | 6.44 |
| 8 | A1-15 | **Forecast-sized offline mandates.** Offline credentials for machines and agents are sized, timed and geofenced from physics-based connectivity forecasts. | Machine payments (Agent Pay for Machines) and offline CBDC. | 6.34 |

Next in line: A1-02 (camera-free RF occupancy sensing at ATMs), A2b-03 + A1-23 merged (ZK GENIUS-Act reserve proofs plus a run-safe redemption controller), A1-07 + A1-19 merged (certified agent control plus an intent evidence bundle). See `WATCHLIST.md`.

## What was built (maps 1:1 to the brief)
| Brief | Implementation | Status |
|---|---|---|
| 1a Academic papers (arXiv, Semantic Scholar, PubMed) | `sources/papers.py`, plus Crossref | ✅ 3,957 papers (1,923 arXiv, 1,551 S2, 303 PubMed, 180 Crossref) |
| 1b Patents (Google Patents RSS, USPTO dumps), competitor filings | `sources/ppubs.py` (discovered the USPTO Patent Public Search JSON API; full abstract and claims) and `sources/patents.py` (Google Patents with circuit breaker) | ✅ 4,770 patents; 515 latest filings from 20 competitors (`COMPETITOR_WATCH.md`). ⚠️ Google Patents has no RSS any more and throttles; ⚠️ PPUBS requires login from 2026-11-07 |
| 1c News, newsletters, GitHub trending (Feedly/Inoreader) | `sources/news.py`: 19 direct feeds, 11 Google News searches, Hacker News, GitHub search and trending (Feedly/Inoreader not needed; they wrap the same feeds) | ✅ 1,037 news, 274 repos, 52 posts |
| 2 Filtration & novelty (embeddings, similarity thresholding, LLM scoring) | `novelty.py`: bge-base embeddings, dense+lexical novelty vs a KB of 5,943 items, **relevance gate**, **genre stratification**, LLM scoring of 261 shortlisted items | ✅ 3,705 incoming → 628 shortlisted → 261 LLM-scored |
| 3 Synthesis & cross-pollination | `synthesis.py`: bisociation pairs in a distance band, fused-vector patent pre-check, MMR, structured prompts | ✅ 60 pairs → 23 inventions |
| 4 Storage & knowledge graph, Notion/Airtable/Coda via Make/Zapier | SQLite (80 MB, all vectors), `graph.py` (428 nodes / 549 edges → GraphML, JSON, interactive HTML), `integrations/sync.py` (Notion, Airtable, Make/Zapier webhooks) | ✅ Exports in `exports/`; sync runs once tokens are set |
| Approach 2 · 1 AI Opportunity Scanner (does it work?) | Zero-shot arm (frozen and hashed) plus signal-grounded `scanner.py` (CFPB, Federal Register, news → 30 themes → pain / pull / momentum / push / whitespace) | ✅ Answered with a controlled comparison (`APPROACH2_ANALYSIS.md`) |
| Approach 2 · 2 Filtration & novelty detection | `prior_art.py` (local KB + live USPTO + arXiv/S2), `evaluate.py` (examiner judge, calibrated similarity bands, Vendi diversity), plus a stage-2 deep check | ✅ 69 ideas checked; 8 verdicts changed by the deep check |

## Lessons worth keeping (detail in `PIPELINE_LESSONS.md`)
1. **Novelty without relevance ranks noise first.** Politics and celebrity news were the "most novel" items until a relevance gate was added.
2. **Genre bias.** Headlines look novel against a paper/patent KB purely because of genre, so rank within genre.
3. **Length confound.** Short ideas look novel under embedding similarity. Use a length-controlled form and calibrated bands (same-invention p25 = 0.79; different-invention p95 = 0.78 on full text).
4. **Noise looks like whitespace.** Nobody patents conference promos. Filter, dedupe syndicated stories, and use phrase-level whitespace queries.
5. **LLM ideas that feel novel often already exist in academic papers.** The deep check is mandatory.

## Files
- `docs/REPORT.md` (this file) · `APPROACH2_ANALYSIS.md` · `METHODOLOGY.md` · `RESEARCH_BRIEF.md` · `PATENTABILITY.md` · `PIPELINE_LESSONS.md` · `COMPETITOR_WATCH.md` · `WATCHLIST.md` · `IDEAS_ALL.md` · `dossiers/01…08`
- `exports/idea_register.csv` (all 69 ideas with scores, verdicts and closest prior art; the Notion/Airtable import file) · `exports/knowledge_graph.html` · `exports/graph.graphml`
- `runs/2026-09-30/`: every intermediate artefact, including all LLM prompt packets and responses (fully reproducible and auditable)

## Recommended next steps
1. **Patent-attorney review of dossiers #1–#4** this month. File **provisionals** (US and/or India) to secure dates.
2. **PoCs for #1 (PixSim) and #3 (VRF quorum)**: 3–6 weeks each. They produce the technical-effect evidence needed for §101 SMEDs and India's CRI technical-effect test.
3. **Non-US prior-art sweep** (Espacenet, InPASS, CNIPA) for the top 8.
4. **Turn on the daily job** with an Anthropic API key (`scripts/run_daily.sh`, launchd or GitHub Actions) and set `USPTO_PPUBS_TOKEN` before 2026-11-07.
5. **Switch the generator to the hybrid design**: A2b chooses problems, A1 supplies mechanisms, stage-2 checks are mandatory.

## Daily runs since the first run (2026-10-01 to 2026-10-09)
The daily job was not run between 30 Sep and 9 Oct. On 9 Oct the missed days were caught up as **separate daily runs**, each restricted to the data first available on or before its own date (see METHODOLOGY, "Daily runs and catch-up"), followed by the regular run for 9 Oct. One row per day is in `docs/DAILY_LOG.md`, and each day's digest is in `runs/<date>/DIGEST.md`.

| | Value |
|---|---|
| New items gathered | 3,385 (papers, news, posts, repos, regulations) + 529 patents |
| Competitor filings caught on publication day | 138 (Oct 1, 6 and 8 USPTO publication days) |
| New inventions | 13 (A1 cross-pollination 9, A2b scanner 4) |
| Verdicts | 0 pursue · 8 refine · 5 already existing |
| Repeats of earlier ideas | 0 (cross-run similarity check) |

Best new inventions, all "refine":
- **A2b-1001-02 Recovery-scam shield.** A fraud report puts the account into a protected mode against follow-on "fund recovery" scams, and real recovery contact is delivered through a signed in-app channel.
- **A1-1001-02 Payee-label semantics.** The nicknames victims are told to give payees ("Kim Kardashian") are read as a scam-narrative signal against the confirmation-of-payee legal name.
- **A1-1002-01 Delegation-residue sweep.** When an AI agent's or a person's access is revoked, every leftover token, endpoint and data share is probed and attested as gone. It includes a safety-reset embodiment for people leaving coercive relationships.
- **A2b-1006-01 Read-time coupling.** Detects LLM attack agents (South Korea reported AI agents used against its banks) from how their delay scales with the length of the response they just read. The deep check found agent timing-fingerprinting papers, so this is narrowed to the length-inflation tarpit.

What daily operation taught us:
- **Daily novelty is thin.** One day of data gives 0–7 credible ideas, and 4 of 9 days gave none. Cross-pollination needs a large enough mechanism pool: on weekends and on the day before arXiv announces papers there was nothing to pair. A **weekly synthesis** over the accumulated week, with daily gathering and filtering, would give better pairs.
- **The scanner's delta mode works.** It ideated only on themes with fresh signals and skipped the ones already used. Most days the honest answer was "nothing new", and there were no repeated ideas.
- **The competitor watch earns its keep daily.** On publication day it surfaced JPMorgan's AI-agent identification filing. Checked against dossier #5, that filing covers a different problem.
