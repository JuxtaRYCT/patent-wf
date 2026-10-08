# TASK judge_002

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A1-17  (A1)  Proportionality-bounded mass enforcement: compensatory review allocation before automated fraud actions hit hundreds of thousands of people
Problem: Mass automated fraud determinations (760,000 insurance cancellations; people jailed after AI flags) concentrate false positives on particular segments. The error accumulates across segments in the same way apportionment rounding bias accumulates across districts.
Mechanism: Before a batch of automated adverse actions is executed, the system computes for each segment (region, age band, channel, language) the gap between its share of actions and its share of evidence-weighted fraud likelihood. It uses probabilistic seat-vote discrepancy bounds to predict the accumulated disproportionality across all segments. It then allocates a fixed number of 'compensatory' human-review slots or deferred-action slots to over-actioned segments, so that the maximum disproportionality stays under a configured bound, and executes the rest. A signed proportionality certificate is logged for audit and appeal.
Claim core: A method comprising: receiving a batch of proposed automated adverse actions across segments; computing per-segment discrepancies between action shares and evidence shares; allocating a bounded number of review slots to segments to reduce a maximum discrepancy below a threshold; and executing the remaining actions while logging a certificate.
Closest prior art found:
  - [paper sim=0.759] s2:cec476b59809bdb02ace7de065687840ecf453c2 | Auditable Credit Risk Intelligence for the U.S. Financial System: A Scalable Explainable-AI Framework Reconciling Predictive Performance with ECOA, FCRA, and Mo | 
    Machine-learning credit underwriting in the United States operates under three families of obligation that are not reducible to one another: a statutory prohibition on discrimination, a statutory duty to disclose the specific principal reasons for an adverse action, and prudential expectations for model risk management. Prevailing practice reconciles these demands by sacrificing model capacity, deploying low-capacity scorecards whose interpretability is structural rather than earned. This study argues that the United States regulatory realignment of 2025 and 2026 makes that settlement less defensible, not more. The Consumer Financial Protection Bureau withdrew the interpretive circulars gove
  - [patent sim=0.752] patent:US12743707B2 | AI-enabled fraud analysis | KPMG International Services Ltd
    Methods, apparatus, and computer program products described herein provide for calculation of a score representative of the risk of fraud by a target entity. A set of financial ratios, lens model scores, risk area scores, and academic scores are all calculated in relation to the target entity and a group of peer entities. These calculated scores are all indicative of the risk of fraud by the target entity. The calculated scores and other market data related to the target entity are displayed to a user to evaluate the risk of fraud by the target entity.
CLAIM 1: A computer-implemented method for calculating a score representative of the risk of fraud by a target entity, the method comprising,
  - [paper sim=0.750] arxiv:2609.01040 | Causal Evidentiary Governance for High-Risk Machine Learning Systems | 
    Machine learning systems deployed for credit, hiring, and resource distribution are increasingly subject to regulatory oversight from policies such as the EU AI Act and GDPR. Current fairness governance practices rely on observational fairness metrics, post-hoc explainability, and immutable audit logs, but provide limited support for causal attribution and efficient evidentiary verification. We introduce Causal Evidentiary Governance (CEG), a framework in which regulated institutions commit to a versioned directed acyclic graph (DAG) that partitions causal pathways into allowable and disallowed groups. The Causal Harm Rate measures prediction variation attributable to disallowed causal pathw

### A1-18  (A1)  Trust-farming-resistant payee reputation: semi-monotone graph centrality that turns scammers' bait payments into a risk signal
Problem: Romance and investment scammers 'groom' victims with small returns and route micro-payments through the payee to build reputation. Graph-based payee-trust scores rise with every added edge, so the grooming makes the scam payee look safer.
Mechanism: The payee-reputation engine uses a centrality measure constrained to be semi-monotone. Edges from clusters with synchronised creation, reciprocal micro-flows or shared devices contribute sub-linearly. Reverse 'bait' edges, where the prospective victim previously received small sums from the payee, are classified as trust-farming, and their contribution is inverted into risk. The trigger at payment time is: the payer received ≥1 small inbound payment from this payee within N weeks, the outbound amount is much larger, and the payee's recent centrality gain comes mostly from bait-like edges. This trigger produces friction and a tailored warning.
Claim core: A method comprising: maintaining a payment graph; computing a reputation for a payee using a centrality measure in which contributions of edges classified as coordinated or reverse-bait are sub-linear or negative; and upon a payment request from a payer that previously received a bait-classified payment from the payee, applying an intervention.
Closest prior art found:
  - [paper sim=0.766] arxiv:2609.24683 | Semi-Monotonicity for Spectral Centrality Measures | 
    Score monotonicity and rank monotonicity are properties describing the behavior of a centrality measure when an arc is added to a network: the former requires that the score of the target of the arc should increase, the latter that its importance with respect to the remaining nodes should not deteriorate. While in directed networks almost all classical centrality measures satisfy both properties, in undirected networks they fail for most measures: adding an edge can reduce the score or the rank of one of its endpoints. Semi-monotonicity is a recently introduced weaker property for undirected networks, requiring that at least one of the two endpoints of the new edge enjoys monotonicity, and i
  - [paper sim=0.748] s2:7d04d5323849580b64407a7bce6fc62362ad572f | AI-Based Fraud Detection and Customer Protection in Online Markets: Balancing Transaction Security and Enhancing Digital Payment Adoption | 
    The rapid global adoption of digital payments has precipitated an escalating arms race against sophisticated financial fraud, creating a critical tension between implementing robust security measures and maintaining a frictionless user experience that fosters acceptance. Advanced, current, AI-driven fraud detection systems often operate in silos, lack adaptive mechanisms against evolving threats, and fail to explicitly optimise for customer-centric outcomes like trust and satisfaction. To fill these gaps, this study proposes, develops, and validates the Adaptive Security-Trust Equilibrium (ASTE) Framework, a new AI system that aims to find a balance between security and the use of digital pa
  - [paper sim=0.747] s2:e3db443b55fbb1960ad2a9005fbe397ff9273a07 | Adaptive Graph-Based Risk Scoring for Real-Time Instant Payment Systems | 
    Instant payment rails and mobile money platforms such as UPI, Pix, and FedNow require fraud decisions in a few hundred milliseconds, but most deployed and published fraud models are batch oriented and sequence only. They are trained and evaluated offline, treat each account in isolation, and provide limited visibility into mule networks and collusive cash out structures. This paper presents a graph based streaming risk scoring architecture that brings graph neural network (GNN) style inference into the authorization path while respecting a sub 300 ms end to end service level objective. The system maintains a dynamic transaction graph over accounts, devices, merchants, and institutions, updat

### A1-19  (A1)  Principal-intent factor graph with evidentiary bundle for agent-initiated payments and dispute resolution
Problem: When an AI agent buys the wrong item or books the wrong dates, liability between merchant, issuer and agent platform is unresolved. There is no verifiable record of what the user actually intended.
Mechanism: For each agent-initiated payment, a factor graph over hidden intent variables (item class, budget, deadline, merchant constraints, substitutes allowed) combines noisy observations: the signed natural-language mandate, parsed into constraints; the user's historical approvals and rejections; context such as calendar and location; and the agent's proposed cart. Hard factors enforce explicit mandate constraints and soft factors are learned. The posterior probability that the proposed purchase lies within intent is computed. Low-probability purchases are routed to the user for confirmation. Every payment carries a signed evidentiary bundle with the posterior, the dominant factors and the hashes of the inputs, written in a form an auditor can check without trusting the agent platform's own logs. Dispute adjudication uses this bundle to allocate liability.
Claim core: A method comprising: receiving a proposed payment from an autonomous agent acting for a principal; performing inference on a factor graph relating hidden intent variables to a signed mandate, historical principal decisions and the proposed payment; routing the payment for confirmation when a posterior intent-compliance probability is below a threshold; and generating a signed evidentiary bundle for dispute resolution.
Closest prior art found:
  - [paper sim=0.779] arxiv:2609.00060 | A Formal Analysis of Agent Payment Protocols | 
    Agent payment protocols are emerging as a key transaction layer for autonomous commerce, enabling AI agents to purchase goods and services and execute payments on users'behalf. Unlike conventional payment flows, they distribute user intent, delegated authority, credential use, settlement, and fulfillment across multiple actors and stages, creating security dependencies that no single message or participant can enforce. Yet these guarantees remain largely implicit across evolving specifications, schemas, and reference implementations, with little systematic formal analysis. We formalize four representative agent payment protocols: x402, MPP, ACP, and AP2 in Tamarin. Using a common abstraction
  - [paper sim=0.778] s2:d127703cb86e99b151d2af0b0cde9d7397a4cf25 | When AI Agents Pay: A Rollback Governance Framework for Fraud and Execution Failure in Agentic Stablecoin Payments | 
    Stablecoin payment rails and agentic commerce are converging toward an environment in which autonomous AI agents initiate and settle payments on behalf of users without human authorisation of each transaction. This exposes a governance gap: chargeback mechanisms are too slow and too broad for machine speed execution failures, settlement finality precludes open-ended reversibility, and reversible-token standards supply mechanisms without a governance framework for their use. This paper develops such a framework for rollback, a risk-bounded recourse mechanism for high-confidence fraud and execution-failure events, specifying the first-level eligibility and routing logic of a three-layer recour
  - [paper sim=0.775] arxiv:2608.28542 | Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach | 
    

### A1-20  (A1)  Payday-landing controller for earned wage access: advance sizing with a robust no-cycle guarantee
Problem: Earned wage access (EWA) products are being sued as disguised high-cost loans because users fall into repeat-advance cycles.
Mechanism: Before offering an advance, the provider runs a robust variable-horizon MPC over the worker's projected balance until payday. Inflows are the remaining earned wages, and outflows are known bills, typical spend and bounded disturbances. The controller computes the largest advance and the fee-free timing that guarantee the balance 'lands' non-negative at payday after repayment, with no second advance needed under worst-case disturbances. The feasibility certificate is stored per advance as ability-to-repay evidence.
Claim core: A method computing an advance amount by solving a robust model-predictive control problem over a projected account balance trajectory ending at a pay date subject to a terminal non-negativity constraint and a no-repeat-advance constraint under bounded disturbances.
Closest prior art found:
  - [patent sim=0.746] patent:US20250259233A1 | EARNED COMPENSATION ACCESS SYSTEM WITH INTERNAL AND EXTERNAL FUNDING OPTIONS FOR COMPENSATION PAYMENT BEFORE PAYDAY | Alturki; Sultan Abdulaziz
    The invention relates to an Earned Compensation Access system that allows employees to access a portion of their earned compensation, such as wages, allowances, bonuses, commissions, and stock options, before payday without borrowing. The system offers two funding options: internal funding from the employer or related entities and external funding from approved banks, financial institutions, or other entities. The process is fully automated, from the employee's request submission to eligibility checks, funding source approvals, and fund transfers. The system manages fees, supports periodic subscriptions, and allows potential revenue sharing. In cases of internal funding, fees can be shared b
  - [paper sim=0.721] arxiv:2608.23060 | Atomic Common-Day Invoice Clearing under Causal Daily Scheduling: Path-Enabled and Bounded-Cycle Policies | 
    Late payment propagates working-capital pressure through supply networks because firms are simultaneously creditors and debtors. We develop an atomic-record temporal invoice-graph method for path-enabled clearing and compares it with complete-candidate bounded-cycle netting under a causal daily greedy schedule. Each invoice remains a residual record with its issue date, due date, amount, and identifier. A candidate is executable through source capacity active on every supporting edge on one common day. A non-bilateral two-edge path reduces two invoice legs, creates a direct settlement instruction between the endpoints, and preserves net positions for all participants on the combined invoice-
  - [patent sim=0.715] patent:US20160086261A1 | METHOD AND SYSTEM FOR PROVIDING JUST IN TIME ACCESS TO EARNED BUT UNPAID INCOME AND PAYMENT SERVICES | PAYACTIV Inc.
    Methods and systems (including associated devices) are disclosed herein that allow for the providing of one or more financial services, including the facilitating of access to accrued but unpaid earnings, to users such as employees of employers. In at least some embodiments, the extent to which services can be accessed or used is determined at least in part based upon one or more risk determinations. For example, in the case of a service for distributing accrued but unpaid earnings before an end of a pay period to an employee (sometimes in the absence of immediate access to a number of hours the employee has worked), risk factors such as a number of future repayments promised as well as a cu

### A1-21  (A1)  Crowd-relayed settlement of offline payments via delay-tolerant store-carry-forward routing
Problem: Offline digital payments (offline CBDC, UPI Lite-style wallets) carry double-spend risk that grows with the time until settlement. Remote regions (e.g. RBI's push for credit and payments in J&K) can stay offline for days.
Mechanism: Each offline payment is packaged as an encrypted, signed bundle. Opted-in nearby devices act as carriers and store and forward bundles over BLE or Wi-Fi Direct. Routing is on-demand: a bundle goes to the carriers predicted, from their mobility history, to reach connectivity soonest, rather than flooding to everyone. The first carrier to reach the network submits the bundle. The ledger deduplicates by bundle ID and returns a signed receipt, which pays the carrier a micro-incentive and propagates back as a settlement acknowledgement. The payee's offline wallet can raise its offline limit when earlier bundles are acknowledged.
Claim core: A method comprising: generating a signed encrypted bundle for an offline payment; selecting, from nearby devices, carrier devices based on predicted time-to-connectivity; transferring the bundle to selected carriers; receiving the bundle at a ledger from a first carrier and deduplicating; and issuing a signed receipt enabling carrier compensation and payee limit restoration.
Closest prior art found:
  - [patent sim=0.822] patent:US11935065B2 | Systems and methods for implementing offline protocol in CBDC networks using collateral chain | Fluency Group Ltd.
    The invention provides techniques for enabling offline devices that do not have an active connection to an account-based CBDC network to participate in CBDC network processes such as asset transfers. This is enabled by defining an offline protocol that governs the handling of such processes in an offline state. A collateral chain is provided by the CBDC network that links together multiple accounts so that an account lower down in the collateral chain can be used to settle a transaction in the case where an account higher up the chain does not hold sufficient CBDC to settle the transaction. On the device side, offline transaction messages are exchanged that enable either device to commit the
  - [patent sim=0.819] patent:US20230075202A1 | Systems and Methods for Implementing Offline Protocol in CBDC Networks using Collateral Chain | Fluency Group Ltd.
    The invention provides techniques for enabling offline devices that do not have an active connection to an account-based CBDC network to participate in CBDC network processes such as asset transfers. This is enabled by defining an offline protocol that governs the handling of such processes in an offline state. A collateral chain is provided by the CBDC network that links together multiple accounts so that an account lower down in the collateral chain can be used to settle a transaction in the case where an account higher up the chain does not hold sufficient CBDC to settle the transaction. On the device side, offline transaction messages are exchanged that enable either device to commit the
  - [paper sim=0.765] doi:10.22214/ijraset.2026.84949 | A Secure Blockchain-Based Offline Payment System with Fraud Window Analysis | 
    The rapid growth of digital payment systems has increased the demand for secure and reliable payment mechanisms capable of operating in environments with intermittent or unavailable Internet connectivity. Conventional blockchain-based payment systems typically require continuous network access for transaction validation and settlement, which limits their applicability in rural areas, disaster-affected regions, and other low-connectivity environments. This research presents a Secure Blockchain-Based Offline Payment System with Explicit Fraud Window Analysis, which allows transactions to be created and stored locally during periods of network unavailability and synchronized with the Ethereum b

### A1-22  (A1)  Input-pipeline timing fingerprints to detect accessibility-service automation and remote-control malware in mobile banking without extra permissions
Problem: OTP-stealing and account-draining apps use accessibility services and remote-control tooling to operate the banking app as if they were the user.
Mechanism: The banking app timestamps each input event through the whole pipeline with high-resolution monotonic clocks: hardware MotionEvent timestamp, app dispatch, the view-hierarchy change, and the next vsync frame. Genuine touches show sensor-noise jitter and a characteristic hardware-to-dispatch latency distribution. Synthetic events injected through accessibility or remote-control frameworks show quantised timestamps, missing hardware noise, extra IPC hop latency and implausible inter-event regularity. A small on-device classifier on these timing features flags automated or remote sessions within a few events and triggers step-up or a block. It needs no special permissions and no data about other apps.
Claim core: A method comprising: recording, for input events received by a banking application, timestamps at multiple stages of an input pipeline; computing latency and jitter features; classifying the session as automated or remotely controlled based on the features; and restricting a transaction accordingly.
Closest prior art found:
  - [patent sim=0.751] patent:US12101354B2 | Device, system, and method of detecting vishing attacks | BioCatch Ltd.
    Devices, systems, and methods of detecting a vishing attack, in which an attacker provides to a victim step-by-step over-the-phone instructions that command the victim to log-in to his bank account and to perform a dictated banking transaction. The system monitors transactions, online operations, user interactions, gestures performed via input units, speed and timing of data entry, and user engagement with User Interface elements. The system detects that the operations performed by the victim, follow a pre-defined playbook of a vishing attack. The system detects that the victim operates under duress or under dictated instructions, as exhibited in irregular doodling activity, data entry rhyth
  - [patent sim=0.749] patent:US20240080339A1 | Device, System, and Method of Detecting Vishing Attacks | BioCatch Ltd.
    Devices, systems, and methods of detecting a vishing attack, in which an attacker provides to a victim step-by-step over-the-phone instructions that command the victim to log-in to his bank account and to perform a dictated banking transaction. The system monitors transactions, online operations, user interactions, gestures performed via input units, speed and timing of data entry, and user engagement with User Interface elements. The system detects that the operations performed by the victim, follow a pre-defined playbook of a vishing attack. The system detects that the victim operates under duress or under dictated instructions, as exhibited in irregular doodling activity, data entry rhyth
  - [patent sim=0.747] patent:US20250016199A1 | Device, System, and Method of Detecting Vishing Attacks | BioCatch Ltd.
    Devices, systems, and methods of detecting a vishing attack, in which an attacker provides to a victim step-by-step over-the-phone instructions that command the victim to log-in to his bank account and to perform a dictated banking transaction. The system monitors transactions, online operations, user interactions, gestures performed via input units, speed and timing of data entry, and user engagement with User Interface elements. The system detects that the operations performed by the victim, follow a pre-defined playbook of a vishing attack. The system detects that the victim operates under duress or under dictated instructions, as exhibited in irregular doodling activity, data entry rhyth

### A1-23  (A1)  Run-safe stablecoin redemption controller with an adversarial reachability certificate published on-chain
Problem: Stablecoin reserves spread across banks, and one partner bank can be hit by an asset seizure. The GENIUS Act requires redemption at par within 2 business days. Issuers publish point-in-time attestations, not forward-looking guarantees.
Mechanism: The issuer models redemption demand as an adversary with bounded capability: maximum redemption rate derived from holder concentration, on-chain liquidity, exchange balances and social-momentum signals. It computes the robust invariant set of reserve-liquidation policies that guarantee par redemption within the regulatory window under every admissible demand path, including single-custodian loss scenarios. A controller continuously re-tiers reserves across cash at multiple banks, T-bills and reverse repo to keep the state inside the invariant set. It publishes a machine-verifiable safety margin certificate on-chain; wallets and exchanges can read it and throttle programmatically.
Claim core: A method comprising: estimating bounds on a redemption-demand process; computing a set of reserve states from which par redemption within a time window is guaranteed under all demand paths within the bounds; rebalancing reserve assets across custodians to keep the reserve state within the set; and publishing a verifiable certificate of a safety margin.
Closest prior art found:
  - [paper sim=0.809] arxiv:2508.09429 | Optimal Control of Reserve Asset Portfolios for Stablecoins | 
    
  - [paper sim=0.794] s2:ab0cd7f404898f818f079d6a5ed2c86288383563 | Stablecoins as a New Monetary Layer: Market Structure, Reserve Design, and the Competition with Tokenized Deposits | 
    Stablecoins have evolved from liquidity tools for crypto trading into a form of tokenized private money with implications for payments, cross-border transfers, short-term funding markets, and the architecture of money itself. The literature on stablecoins has expanded rapidly but remains fragmented across stability, reserve design, banking, payments, and regulation. This paper synthesizes that literature into a single integrative argument: stablecoins should be analyzed as a distinct monetary layer within tokenized finance, evaluated against the BIS framework of singleness, elasticity, and integrity, and compared with tokenized deposits as their most relevant institutional alternative. Drawi
  - [paper sim=0.788] arxiv:2510.10469 | A Risk Mitigation Model of Monetary Ecosystem with Stablecoins | 
    

### A2a-01  (A2a)  Coercion-aware transfer friction
Problem: Authorised push payment (APP) scams: victims are coached live by a scammer on the phone while they make the transfer.
Mechanism: Detect concurrent active voice call, navigation hesitancy, copy-pasted payee details and first-time payee; dynamically insert a cooling-off delay and a callback to a pre-registered trusted contact who must confirm with a safe word.
Claim core: 
Closest prior art found:
  - [patent sim=0.726] patent:US9898719B2 | Systems, methods, and computer program products providing push payments | Godsey; Sandra Lynn
    In electronic financial transactions a receiver, or targeted recipient of funds, provides account information to a transmitter, or sender of funds. The transmitter initiates a push of funds from a transmitter funding source to the receiver's funding source processor. In some embodiments the receiver provides a payment card, similar to a credit card, which is read by an electronic device of the transmitter, such as a smart phone. In some embodiments, the receiver provides the account information by way of a bar code, such as a QR code, which is scanned and read by the transmitter's electronic device.
CLAIM 1: An electronic device, comprising: a non-transitory memory storing instructions; and 
  - [patent sim=0.725] patent:US20210042718A1 | SYSTEMS, METHODS, AND COMPUTER PROGRAM PRODUCTS PROVIDING PUSH PAYMENTS | PAYPAL, INC.
    In electronic financial transactions a receiver, or targeted recipient of funds, provides account information to a transmitter, or sender of funds. The transmitter initiates a push of funds from a transmitter funding source to the receiver's funding source processor. In some embodiments the receiver provides a payment card, similar to a credit card, which is read by an electronic device of the transmitter, such as a smart phone. In some embodiments, the receiver provides the account information by way of a bar code, such as a QR code, which is scanned and read by the transmitter's electronic device.
CLAIM 1: (canceled)
  - [patent sim=0.725] patent:US20180247282A1 | SYSTEMS, METHODS, AND COMPUTER PROGRAM PRODUCTS PROVIDING PUSH PAYMENTS | PAYPAL, INC.
    In electronic financial transactions a receiver, or targeted recipient of funds, provides account information to a transmitter, or sender of funds. The transmitter initiates a push of funds from a transmitter funding source to the receiver's funding source processor. In some embodiments the receiver provides a payment card, similar to a credit card, which is read by an electronic device of the transmitter, such as a smart phone. In some embodiments, the receiver provides the account information by way of a bar code, such as a QR code, which is scanned and read by the transmitter's electronic device.
CLAIM 1: (canceled)

## OUTPUT JSON SCHEMA
```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "judgments"
 ],
 "properties": {
  "judgments": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "id",
     "novelty",
     "non_obviousness",
     "utility",
     "feasibility",
     "commercial",
     "eligibility",
     "crazy",
     "verdict",
     "rationale"
    ],
    "properties": {
     "id": {
      "type": "string"
     },
     "novelty": {
      "type": "integer"
     },
     "non_obviousness": {
      "type": "integer"
     },
     "utility": {
      "type": "integer"
     },
     "feasibility": {
      "type": "integer"
     },
     "commercial": {
      "type": "integer"
     },
     "eligibility": {
      "type": "integer"
     },
     "crazy": {
      "type": "integer"
     },
     "verdict": {
      "type": "string",
      "enum": [
       "pursue",
       "refine",
       "drop-anticipated",
       "drop-weak"
      ]
     },
     "rationale": {
      "type": "string"
     }
    }
   }
  }
 }
}
```

Write the answer to: runs/2026-09-30/llm_responses/judge_002.json
