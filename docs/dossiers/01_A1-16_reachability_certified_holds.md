# #1 · A1-16 — Reachability-certified pre-emptive holds: intercepting stolen funds *ahead* of the money

| | |
|---|---|
| **Origin** | Approach 1 bisociation: *India 1930 cyber-fraud helpline strengthened* (news) × *Adversarially Robust Geometric Safety Certificates for Nonholonomic Robots Against Maneuvering Obstacles* (arXiv 2609.37126). Distributed solve from *Windowed & Quantized Group ADMM* (arXiv 2609.37069). |
| **Domain** | Fraud recovery / payments infrastructure (UPI, IMPS, FedNow, Faster Payments, Pix) |
| **Scores** | final **7.42** (rank 1 of 69) · novelty 8 · non-obviousness 7 · utility 9 · eligibility 6 · crazy 7 · length-controlled max patent similarity 0.710 (distinct band) |
| **Verdict** | **Pursue.** Survived the stage-2 deep check |

## 1. Problem, framed technically
Once a victim reports fraud (India: 1930 / NCRP → CFCFRMS; UK: APP claim; Brazil: MED), the reporting system places liens hop by hop, following transactions that have *already happened*. Mule layering (split, rail-hop, cash-out at ATMs, crypto on-ramps or merchant cash-back) completes in minutes, while each lien needs an API round-trip to a different bank. The recovery system is a **pursuer that is always one hop behind**. Industry tools predict whether a single account is a mule (NICE Actimize, Mastercard, Kumo), but none computes where the money *can* be by time *t* and blocks those places first.

## 2. The invention
### 2.1 Core mechanism
Treat the stolen funds as a **manoeuvring adversary with bounded capability**, as in robust safety certificates against obstacles that can manoeuvre within known limits:

1. **Time-expanded payment graph.** Nodes are accounts and cash-out points (ATM networks, crypto on-ramps, cash-back merchants, prepaid instruments). Edges carry per-rail minimum latency (UPI ≈ seconds, NEFT batch windows, RTGS hours), per-account velocity and limit caps, new-beneficiary cooling periods, and per-institution **hold-activation latency** (how long a hold takes to take effect at that bank).
2. **Reachability.** Compute the earliest-arrival time *a(v)* of value at every node (time-dependent shortest path). Compute an upper bound on transferable value *U(v)* from a max-flow over the time-expanded network with capacity caps.
3. **Capture certificate.** Solve for a minimum-cost set *H* of hold nodes that forms a time-respecting separator between the source and every cash-out sink within horizon *T*. A node is admissible only if *now + activation_latency(v) < a(v)*, meaning the hold lands before the money can. Cost per node reflects customer-friction risk (account legitimacy score, activity, vulnerability flags). The certificate is the separator plus the arrival-time bounds that prove it.
4. **Signed, scoped holds.** Each selected institution receives a hold request signed by the coordinator (for example I4C/CFCFRMS under an LEA authorisation token). The request carries an amount cap equal to *U(v)*, not a full freeze, an expiry, and the certificate hash for audit and proportionality review.
5. **Monotone refinement.** As fresh transaction events arrive, the graph is re-solved and holds that are no longer in any separator are released automatically. Holds that capture value are escalated to formal liens.
6. **Privacy-preserving distributed solve.** Each bank solves its sub-problem over its own accounts. Only boundary variables (flows and arrival times on inter-bank edges) are exchanged, through ADMM iterations, so no raw transaction data is pooled.

### 2.2 System components (for claim drafting)
Fraud-report intake API · rail-parameter registry (latencies, limits, cooling rules) · time-expanded graph builder · reachability engine · separator solver (ILP or greedy with approximation bound) · certificate generator · hold-request signer and dispatcher · bank-side hold executor with amount cap and auto-expiry · event-stream re-solver · distributed ADMM coordinator.

### 2.3 Technical effect (evidence to generate for a US SMED / India technical-effect argument)
- Fraction of reported value intercepted versus the hop-by-hop baseline, at equal or fewer held accounts.
- Median time from report to last necessary hold.
- Number of innocent accounts held (friction), and computation time (seconds) for realistic graph sizes.
- Network messages exchanged: the distributed solve against a centralised data pool.

## 3. Prior art found and how this differs
| Reference | What it discloses | What it does **not** disclose |
|---|---|---|
| Industry mule prediction (NICE Actimize "Mule Defense", Mastercard, Kumo.ai) | Scoring individual accounts as mules and withholding their *inbound* funds | Adversarial reachable sets, minimum separators, pre-emptive multi-bank holds, certificates |
| PixSim (arXiv 2609.30684) | Simulator of instant-payment fraud, recovery and interdiction | A certified pre-emptive hold protocol |
| CFCFRMS / 1930 (India), MED (Brazil) | Reactive multi-hop lien marking after the transfers | Computing *where money can go* and holding it first |
| TCH real-time payments (US11694168B2) | Participant position tracking in RTP | Unrelated to fraud interception |
| Adaptive graph risk scoring for instant payments (retrieved paper) | Per-transaction graph risk | Time-expanded reachability separators |

## 4. Draft claims
**Claim 1 (method).** A computer-implemented method comprising:
(a) receiving a fraud report identifying a source account, an amount and a time of a fraudulent transfer;
(b) constructing a time-expanded graph over a horizon, the graph comprising nodes representing accounts and cash-out endpoints held at a plurality of institutions and edges annotated with payment-rail latencies, per-account transfer caps, beneficiary cooling periods and per-institution hold-activation latencies;
(c) computing, for each node, an earliest-arrival time of value originating at the source account and an upper bound of value transferable to the node;
(d) selecting a set of hold nodes forming a minimum-cost time-respecting separator between the source account and the cash-out endpoints, wherein a node is eligible only if the current time plus its hold-activation latency precedes its earliest-arrival time;
(e) generating, for each hold node, a digitally signed hold request comprising an amount cap derived from the upper bound, an expiry and a digest of a separator certificate; and
(f) transmitting the hold requests to the institutions holding the hold nodes.

**Claim 2.** The method of claim 1, further comprising receiving subsequent transaction events, re-solving steps (c)–(d), and transmitting release messages for hold nodes no longer in the separator.
**Claim 3.** The method of claim 1, wherein step (d) is solved by an alternating-direction method of multipliers in which each institution optimises over its own accounts and exchanges only flow and arrival-time variables on inter-institution edges.
**Claim 4.** The method of claim 1, wherein the cost of a hold node is a function of a legitimacy score, transaction activity and a vulnerable-customer indicator of the account.
**Claim 5.** The method of claim 1, wherein cash-out endpoints include ATM withdrawal networks, virtual-asset on-ramps and merchant cash-back acceptance points.
**Claim 6.** The method of claim 1, wherein each hold request further comprises an authorisation token of a law-enforcement or regulatory authority and is executed as a lien limited to the amount cap.
**Claim 7.** The method of claim 1, wherein the upper bound of value is computed as a maximum flow over the time-expanded graph subject to the transfer caps.
**Claim 8.** The method of claim 1, wherein the separator certificate comprises the set of arrival-time bounds proving that every path to a cash-out endpoint within the horizon traverses a hold node after its activation.
**Claim 9 (system)** and **Claim 10 (CRM)** mirroring claim 1.

## 5. Eligibility notes
- **US:** A bare claim to "identifying and holding suspicious accounts" is a fundamental economic practice (Alice). Anchor the claim in the distributed computation and messaging protocol: the time-expanded graph, the latency-constrained separator, signed scoped messages and the ADMM exchange. Keep benchmark evidence (seconds of compute, message counts, interception rate) for a SMED.
- **India §3(k):** Present as an improvement in the functioning of an inter-bank transaction-processing network (latency-aware distributed control), not as "better fraud information". The CRI Guidelines 2025 distinguish improved technical systems from improved informational outputs.
- **EPO:** The technical character lies in the distributed network-control protocol. The fraud purpose alone does not carry inventive step, so claim the protocol.

## 6. Commercial path
Licence to national switches and fraud-registry operators: NPCI / I4C (India; RBI's Digital Payment Intelligence Platform), Pay.UK and UK Finance, BCB Pix (MED), and TCH / FedNow for the US. Also licensable to large banks as an internal cross-rail engine.

## 7. Proof-of-concept plan (6 weeks)
1. Calibrate on PixSim (open source) and the IBM synthetic AML transaction datasets, and add UPI/IMPS latency and limit parameters.
2. Baseline: hop-by-hop lien marking with realistic API latencies.
3. Implement reachability, then the ILP separator (OR-Tools), then a greedy heuristic, then the ADMM distributed version.
4. Report interception %, holds per case, innocent-hold rate and compute time. These numbers are the SMED evidence.

## 8. Risks
Legal authority to hold funds pre-emptively: Indian banks currently seek RBI powers to freeze without LEA orders. Design holds as short, LEA-authorised, amount-capped liens. Data-sharing governance. Adversary adaptation (slower layering); the horizon *T* and the cost function absorb this.
