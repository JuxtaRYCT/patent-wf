# #5 · A2b-08 — Agent-herding detection: scam storefronts revealed by AI shopping agents converging on them

| | |
|---|---|
| **Origin** | Approach 2 scanner, theme T03 (opportunity 1.24). Signals: *"Banks warn AI shopping bots raise scam, fraud and data-privacy risks"* (Reuters, syndicated widely, Sept 2026) · *"AI Shopping Agents Raise New Fraud and Payment Risks for Banks"* |
| **Domain** | Card-network / issuer / acquirer risk for agentic commerce |
| **Scores** | final **6.57** · novelty 6 · utility 8 · commercial 8 · crazy 7 |
| **Verdict** | **Pursue with a narrowed claim.** The deep check found generic "monitor transaction spikes" advice and agentic merchant-onboarding products, but not this signal |

## 1. Problem, framed technically
The Merchant Risk Council finds that legitimate and fraudulent AI agents produce identical behavioural signals. Device, browser and biometric features disappear when an agent checks out. The fraud surface also shifts: scammers no longer need to deceive each human, only the **retrieval pipeline** that many agents share (agent-SEO, pages with injected instructions). One fake storefront can capture thousands of users' agents within hours.

## 2. The invention
The payment network can see something no merchant or single agent platform can: **how many distinct principals' agents start paying the same new merchant, and how fast**.

1. **Agent-labelled authorisations.** Use the agentic token or requestor identifiers already carried by agentic-commerce frameworks (agent platform ID, agent instance attestation) to separate agent-initiated from human-initiated authorisations.
2. **Human-discovery baseline.** For each merchant, a hierarchical Bayesian model (by MCC, merchant age, geography and acquirer) estimates the expected rate of *new distinct customers* from human-initiated traffic. Human discovery is gradual and diverse.
3. **Convergence statistic.** In sliding windows, compute `N_new_agents(m, w)`, the number of distinct principals whose agents transact with merchant *m* for the first time. Score = posterior tail probability of that count under the human baseline, weighted by:
   - **merchant thinness** (age, history volume),
   - **platform concentration** (Herfindahl index across agent platforms: convergence driven by one platform's retrieval is more suspicious),
   - **retrieval-signal overlap** where available (shared referral or query tokens reported by the platform).
4. **Graduated response.** Above threshold, the merchant is placed on **agent-hold**: agent-initiated transactions need principal confirmation, acquirer settlement for agent transactions is delayed or reserved, and the agent platforms involved receive a signed alert with the retrieval signals, so they can de-rank the storefront. Human-initiated traffic is not affected.
5. **Cluster extension.** Newly onboarded merchants that share registrant, hosting or payout-account attributes with an agent-held merchant inherit elevated priors.

### Technical effect / evidence
Detection lead time (hours from first agent transaction to hold, against chargeback-based detection taking weeks). Loss avoided in simulated agent-SEO campaigns. False-hold rate on legitimately viral merchants, which humans also discover quickly, so they are separated by the human baseline and the platform-concentration term.

## 3. Prior art and differences
| Reference | Discloses | Does **not** disclose |
|---|---|---|
| Stripe US12597035B2 (merchant fraud via event timing) | ML on API event timing for merchant fraud | Agent-vs-human baselines, convergence of distinct principals' agents |
| Forter US20260052155A1 (agent authentication protocols) | Security requirements per agent operation, reputation of the agent's principal | Network-level merchant convergence signal |
| Merchant cohort clustering US20240211965A1 | Merchant-level fraud via cohorts | Agentic signal |
| Industry commentary (MRC, Riskified, Signifyd), Ballerine "agentic detection" | "Monitor transaction spikes", onboarding checks | This specific normalised statistic and response |

## 4. Draft claims
**Claim 1.** A method comprising: receiving authorisation requests each comprising an indicator of whether the request was initiated by an autonomous software agent on behalf of a principal; for a merchant, computing over a time window a count of distinct principals whose agents initiated a first transaction with the merchant; computing a baseline rate of new distinct customers for the merchant from human-initiated transactions of comparable merchants; computing a convergence score from the count relative to the baseline, weighted by a concentration of agent platforms among the agent-initiated requests; and, when the score exceeds a threshold, applying to subsequent agent-initiated requests for the merchant a restriction comprising principal confirmation or settlement deferral while leaving human-initiated requests unrestricted.
**Dependent:** Herfindahl concentration across agent platforms · a merchant-age/thinness weighting · a signed alert to agent platforms including retrieval metadata · propagation of elevated risk to merchants sharing onboarding attributes · the hierarchical Bayesian baseline · automatic release when convergence subsides and dispute rates stay low.

## 5. Eligibility
Frame it as network-level processing of labelled authorisation streams with differential handling by traffic class, a system behaviour. Merchant risk scoring in the abstract is weak, so emphasise the message flags, the per-class routing and the platform-alert protocol.

## 6. Commercial path
Card networks (Visa Intelligent Commerce, Mastercard Agent Pay), large acquirers and PSPs (Stripe, Adyen, Worldpay), and NPCI if UPI adds agentic mandates.

## 7. PoC (4 weeks)
A simulator of human discovery plus agent retrieval with injected scam storefronts. Compare the convergence statistic against velocity rules and chargeback-lag detection.

## 8. Risks
Agent labelling must be reliable. Unlabelled agents can be inferred through token-requestor patterns. Legitimately viral products need calibration of the human baseline.
