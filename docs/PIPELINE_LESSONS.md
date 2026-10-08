# What running the pipeline taught us: failure modes found and fixed (run 2026-09-30)

The first run exposed several ways an automated "novelty" pipeline goes wrong. Each one is a real design lesson for anyone building this, so they are recorded here with the fix that now sits in the code.

| # | Stage | What went wrong | Why it happens | Fix in code |
|---|---|---|---|---|
| 1 | Novelty filter | The most "novel" finance items were politics, celebrity and sports news. | Distance from a banking KB is largest for things that have nothing to do with banking. **Novelty without relevance ranks noise first.** | Relevance gate: max cosine to 16 finance anchor queries must be ≥ 0.51, calibrated on the data (off-topic < 0.50, bank-relevant ≥ 0.52) — `novelty.py`, `config.novelty.anchors` |
| 2 | Novelty filter | After gating, 99% of the finance shortlist was news; only 3 papers got through. | Short headlines are lexically and semantically far from a KB of papers and patents **because of genre**, not because of content. | Genre-stratified shortlist: papers are ranked against papers, news against news |
| 3 | Mechanism pool | The most novel cross-domain items were string theory and spin chains. | The farthest from finance is also the least transferable to it. | The mechanism pool is stratified by field (top-N per arXiv category / PubMed topic), so each discipline contributes its best candidates |
| 4 | Scanner v1 | Noise clusters (conference promos, Federal Register paperwork notices, OFAC licence notices) scored as top "opportunities". | Nobody patents noise, so noise looks like **whitespace**. Small clusters also get extreme z-scores. | Paperwork/meeting/notice filter, the same relevance gate on signals, a minimum theme size, and log-scaled features |
| 5 | Scanner v1 | Every CFPB complaint issue fell into one mega-theme, which dominated on raw pain. | The pseudo-documents shared a templated sentence, so they embedded close together. | Label-only complaint documents (they now cluster by topic), with log-scaled pain |
| 6 | Scanner v2 | Credit-report disputes (2.2M complaints) showed *negative* whitespace. | The whitespace query used generic unigrams ("report AND information AND incorrect"), which matched 43k unrelated patents. | Phrase-first queries (`incorrect ADJ information`) → 50 hits, a far more accurate measure of whitespace |
| 7 | Scanner v2 | One AP wire story republished by 40 outlets counted as 40 signals. | Syndication. | Near-duplicate collapse (cos > 0.93). The syndication count is kept as a log-weighted signal |
| 8 | Data | CFPB complaint *narratives* are no longer served by the public API (the field is empty and rejected as a search field). | API change. | The scanner uses issue/sub-issue volume × growth lift. Narrative code is kept for when they return |
| 9 | Data | Google Patents' JSON endpoint returned "Sorry…" 503s after a burst, then recovered roughly an hour later. | Bot protection. | Circuit breaker, plus USPTO PPUBS as the primary source. Google is used opportunistically (it gave 1,140 global patents on the second attempt) |
| 10 | Data | USPTO PPUBS sessions silently expire after **30 minutes**. After that every call failed and backed off, and a 3,013-document fetch stalled for an hour. | Server session TTL (`sessionTimeOutTime: 1800`). | Proactive token refresh every 20 minutes, refresh on repeated 5xx, and saving every 300 documents so a crash never loses work |
| 11 | Data | USPTO announced that PPUBS will **require login from 2026-11-07**. | Policy change. | `USPTO_PPUBS_TOKEN` support. Documented in README |
| 12 | Prior-art | Anonymous Semantic Scholar search throttles to about 1 request per minute under load, which put prior-art checks at ~90 min per run. | Shared anonymous pool. | arXiv relevance search on the idea's distinctive terms is now the primary literature check, with S2 opportunistic behind a circuit breaker. A free S2 API key removes the limit |
| 13 | Synthesis | Only **23 of 60** bisociation pairs produced a credible invention (hit rate 38%). 37 pairs produced nothing; three were folded into stronger sibling ideas. | Most random cross-field pairings do not bridge. This is expected and healthy: forcing an idea per pair gives nonsense. | The prompt explicitly allows 0 ideas per pair. The hit rate is reported as a metric |

## The general lesson
Every stage that measures "distance from what exists" is also measuring distance from *relevance*, *genre* and *format*. An automated novelty pipeline needs:
1. a relevance gate before the novelty ranking,
2. comparisons within the same genre,
3. deduplication of syndicated signals, and
4. specific (phrase-level) prior-art queries.

Without these it confidently promotes noise. These fixes are the difference between the v1 and v3 scanner outputs in `runs/2026-09-30/`.
