# TASK judge_001

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A1-09  (A1)  Threshold-calibrated decoy mule seeding: capturing laundering networks by pushing instrumented accounts past the network's own adoption threshold
Problem: Laundering networks (one allegedly moved $6.9B through global banks) route around individual freezes. Closing accounts one by one never reaches the network's structure.
Mechanism: Under law-enforcement authorisation, a bank consortium exposes instrumented decoy accounts to mule-recruitment channels (job-scam ads, recruiter channels). A threshold population model, adapted from gene-drive replacement dynamics where a trait spreads only after its release fraction crosses an unstable threshold, estimates the decoy share of the active mule pool above which recruiters' preferential reuse of 'reliable' accounts makes flows route predominantly through decoys. Decoys are engineered to be the most reliable: fast, never frozen, high limits. The optimiser schedules releases (count, timing, geography, persona mix) to cross the threshold at minimum cost. Past it, a growing share of laundered value passes through controlled settlement, exposing upstream and downstream nodes, and funds are held for recovery.
Claim core: A method comprising: estimating, from observed recruitment and routing behaviour of a laundering network, a threshold fraction of instrumented accounts above which routing preferentially selects instrumented accounts; scheduling creation and exposure of instrumented accounts to exceed the threshold; and monitoring flows through the instrumented accounts to identify network nodes and hold funds.
Closest prior art found:
  - [paper sim=0.781] s2:9553c7f08cd59d661b917332ba3e388f1c48f2f9 | A Comprehensive Review of Money Mule Networks and Financial Fraud Detection Techniques | 
    The fast growth of digital financial systems has greatly multiplied the scale and complexity of financial crimes based on money mule networks. The money mule acts as the intermediary in these operations, helping to move stolen funds from accounts they were directly paid into, to more legitimate pathways utilized by bankers and financial institutions. With financial institutions and regulators increasing the pressure to combat fraud, an understanding of how money mules are recruited and operate is invaluable. This paper provides a literature review of current studies on money mule activity and monetary fraud detection. The review is a synthesis of papers that focus on recruitment strategies, 
  - [paper sim=0.751] arxiv:2609.20737 | An Interpretable Approach to Money Laundering Detection in Transaction Graphs using Pass-Through Templates | 
    Layering is a key stage of the money laundering process in which assets are moved through intermediate entities to obscure their origin. We model this movement as a transaction graph, a labeled directed multigraph where nodes represent entities, such as individuals or organizations, and edges represent transactions between them. This work addresses the detection of layering patterns in transaction graphs. We define pass-through templates, a class of transaction graphs whose structure is indicative of a specific layering pattern in which entities receive funds and rapidly forward them. We formulate detecting instances of these templates within a larger transaction graph as a maximum-cardinali
  - [paper sim=0.748] s2:15afa59581075e6a0fa82875875a9b92778a0333 | Fraud–AML Convergence: Integrating Fraud and AML Detection, Shared Typologies, and Unified Case Management. | 
    Fraud and anti–money laundering (AML) programs have historically evolved as separate control functions, often operating on different data, tools, and investigative workflows. However, converging threat landscapes where scams, synthetic identities, mule networks, account takeovers, and laundering chains intersect are forcing financial institutions to rethink fragmented detection and response models. This paper examines the concept of fraud–AML convergence as an integrated approach to identifying illicit activity across the full customer and transaction lifecycle. It analyzes how shared typologies (e.g., authorized push payment fraud feeding mule accounts, trade-based laundering enabled by inv

### A1-10  (A1)  Scam-script phylogenetics: reconstructing the family tree of scam messages, calls and malicious apps to predict and pre-block the next variants
Problem: Bank anti-scam systems (such as newly launched 'guardian' protections) react to each new lure after victims report it. Scam operators mutate templates constantly (brand swaps, lure swaps, new APK wrappers).
Mechanism: Scam artefacts are collected from customer reports, telco and SMS gateways, call transcripts, phishing landing pages and APK static features, and embedded into aligned feature sequences. Lineage trees are reconstructed with quartet-based methods that reweight redundant quartets. These scale to millions of samples and tolerate missing features, which pairwise-distance clustering cannot. Ancestral-state reconstruction infers the template at each internal node. Mutation operators observed along branches (entity substitution, URL-shortener rotation, lure-theme shifts, permission-set drift) are learned per clade and applied forward to generate likely descendant variants. The system then pre-emptively deploys detection signatures and messaging-filter rules for those variants and attributes each new sample to an operator clade for coordinated takedown.
Claim core: A method comprising: embedding scam artefacts into feature representations; reconstructing a lineage tree using weighted quartet scores; inferring ancestral templates and branch mutation operators; generating predicted descendant variants by applying the operators; and deploying detection rules for the predicted variants before they are observed.
Closest prior art found:
  - [paper sim=0.760] arxiv:2608.24127 | Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate | 
    Telephone fraud is pervasive and costly, but its inner workings are rarely observed at scale. We analyze a complete corpus of 10,211 inbound scam and spam calls -- 913 hours of audio and 330,956 transcribed turns from 5,780 distinct numbers -- collected over 54 days by an AI voice-agent honeypot that answered callers and kept them talking, and introduced in a companion data descriptor. We separate outright scams, which solicit sensitive information, from the larger stream of predatory but legal lead generation ("spam") that feeds them. Scam operations keep office hours (6.6x more calls per weekday than weekend day); thousands of disposable numbers run a small catalog of recycled scripts (thi
  - [paper sim=0.755] arxiv:2609.29528 | A Corpus of Real Scam- and Spam-Call Conversations from an Active Voice-Agent Honeypot | 
    Real conversations between fraudsters and their targets are among the most informative artifacts for studying telephone scams, yet also the scarcest: passive honeypots overwhelmingly capture automated messages and hang-ups, large-scale studies characterize call metadata rather than dialogue, and manual scam-baiting does not scale. We present a dataset of real scam-call conversations collected by an active voice-agent honeypot. Dedicated numbers are seeded into the lead-generation channels fraud operations harvest; inbound callers are answered by a low-latency conversational agent that adopts a plausible target persona and sustains the interaction while every call is recorded, transcribed, an
  - [paper sim=0.750] s2:fbd1210664008be37081c77b408906606b831f18 | Lifting the Grey Curtain: Analyzing the Ecosystem of Android Scam Apps | 
    Mobile applications (apps) are extensively involved in online scams. Previous studies mainly target malicious apps that either compromise victims’ devices (e.g., malware and ransomware), or lead to privacy leakage and abuse (e.g., creepware). Recently, an emerging kind of app makes profits by providing scam services rather than compromising devices or abusing privacy . We name these apps as scamware due to their deceptive behavior, which poses a new threat to (mobile) users. However, the characteristics and the ecosystem of scamware remain mysterious. This article takes the first step toward systematically studying scamware. In total, 1,262 ground-truth scamware are collected from December 1

### A1-11  (A1)  Constraint-aware factor-graph estimation of mobile device compromise for banking apps
Problem: Malicious apps (fake hospital-appointment apps, adult-content lures) empty accounts by abusing accessibility services, overlays and SMS access. Banking SDK signals are sparse, noisy and often missing, so rule engines misfire both ways.
Mechanism: The banking SDK observes a sparse set of signals: accessibility-service enablement and event rates, overlay-window presence, notification-listener or SMS-read capability, screen-share state, input-event timing, installed-package risk and OS patch level. A factor graph links hidden compromise-state variables (overlay attack, SMS interception, remote control, benign) to these observations. Hard factors encode OS permission logic, for example that SMS interception is impossible without READ_SMS or notification access, and overlays require SYSTEM_ALERT_WINDOW. Soft factors are learned likelihoods. Neural message passing with hard-constraint projection gives calibrated posteriors even when most observations are missing. These posteriors gate specific flows: SMS-OTP flows are disabled when P(SMS interception) is high, and payee addition when P(remote control) is high.
Claim core: A method comprising: collecting device observations by a banking application; performing inference on a factor graph linking hidden compromise states to the observations, the graph comprising hard factors encoding operating-system permission constraints and learned soft factors; and restricting a transaction flow according to posterior probabilities of the compromise states.
Closest prior art found:
  - [paper sim=0.768] doi:10.2139/ssrn.7478298 | BankGuard-CGR: A Conformal Graph-Rule Framework for Fraud and Anti-Money-Laundering Detection in Banking Payment Systems | 
    Banking payment platforms operate under two pressures that rarely align. They must catch a small share of fraudulent and money-laundering transfers while keeping analyst queues short enough to review every alert. This paper presents BankGuard-CGR, a framework that combines gradient-boosted scoring on tabular transaction features, graph-based rule boosts on the account transfer network, and Mondrian conformal calibration by channel. The design gives operations teams a probability that is meaningful under drift, a threshold that respects a fixed daily alert budget, and a coverage guarantee on the positive class. Using a synthetic payment ledger of 120,000 transactions across 15,000 accounts an
  - [paper sim=0.765] arxiv:2609.10350 | Cyber-Financial Contagion: Modeling the Propagation of an AI Vendor Compromise Through the Banking System | 
    The banking system now depends on a small set of shared artificial intelligence vendors for fraud screening, credit decisioning, anti-money-laundering triage, customer analytics, and internal decision support. This paper studies how a compromise inside one of those vendors can propagate along a chain of operational, informational, and financial linkages until it triggers losses that look, from the outside, like a classical banking crisis. We build a four-layer heterogeneous network that couples AI vendors, financial institutions, interbank exposures, and customer accounts, and we propose CFC-Prop, a stochastic epidemic-and-clearing model that runs on that network. On a synthetic dataset with
  - [paper sim=0.761] s2:b66446022276f3dc7f8e20d38a818e47cc97a720 | AI-Driven Fraud Detection in IoT-Enabled Payment Ecosystems: Challenges, Hybrid Edge-Cloud Framework, and Emerging Trends | 
    Financial fraud in IoT-enabled payment systems has emerged as a significant challenge due to the rapid adoption of digital transactions, real-time processing requirements, and the increasing sophistication of fraud schemes. Fraud detection involves identifying unauthorized, anomalous, or suspicious transactions to prevent monetary losses and safeguard user trust. Traditional detection approaches, such as rule-based systems and classical machine learning (ML) models like Logistic Regression (LR), Random Forest (RF), and XGBoost (XGB), provide a baseline capability for flagging simple or known patterns. However, these methods often struggle with temporal transaction dynamics, networked collusi

### A1-12  (A1)  Channel-watermarked OTPs with honey-session diversion: proving SMS interception and harvesting mule accounts instead of just blocking
Problem: Fake apps steal SMS OTPs. Blocking a suspicious login tips the attacker off, and the bank learns nothing about where the money was going.
Mechanism: Each authentication challenge is issued with a different code per delivery channel (SMS, push, email, voice), all valid for the same session. The code that comes back reveals which channel delivered it. If the SMS-channel code is submitted from a device other than the bound device, or from a known phishing relay, SMS interception is proven. The session is then diverted into a high-fidelity honey session: a sandboxed copy of the account with synthetic balances, where the attacker's actions run against a shadow ledger. Beneficiary accounts they add, device fingerprints and cash-out paths are harvested and shared with the mule-intelligence network, and the real account is locked quietly. In parallel, speculative pre-execution computes the risk of the pending transaction while the user is still entering the code, so honest users see no added latency.
Claim core: A method comprising: generating distinct authentication codes for respective delivery channels for a session; receiving a submitted code and identifying its delivery channel; determining channel compromise based on the channel and a submitting device; and in response routing the session to a sandboxed environment backed by a shadow ledger while recording beneficiary and device data.
Closest prior art found:
  - [paper sim=0.768] arxiv:2601.09232 | The Tragedy of Convenience: Cascading User-Data Leakage from SMS-Delivered URLs | 
    
  - [paper sim=0.739] arxiv:2609.29528 | A Corpus of Real Scam- and Spam-Call Conversations from an Active Voice-Agent Honeypot | 
    Real conversations between fraudsters and their targets are among the most informative artifacts for studying telephone scams, yet also the scarcest: passive honeypots overwhelmingly capture automated messages and hang-ups, large-scale studies characterize call metadata rather than dialogue, and manual scam-baiting does not scale. We present a dataset of real scam-call conversations collected by an active voice-agent honeypot. Dedicated numbers are seeded into the lead-generation channels fraud operations harvest; inbound callers are answered by a low-latency conversational agent that adopts a plausible target persona and sustains the interaction while every call is recorded, transcribed, an
  - [paper sim=0.732] arxiv:2608.24127 | Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate | 
    Telephone fraud is pervasive and costly, but its inner workings are rarely observed at scale. We analyze a complete corpus of 10,211 inbound scam and spam calls -- 913 hours of audio and 330,956 transcribed turns from 5,780 distinct numbers -- collected over 54 days by an AI voice-agent honeypot that answered callers and kept them talking, and introduced in a companion data descriptor. We separate outright scams, which solicit sensitive information, from the larger stream of predatory but legal lead generation ("spam") that feeds them. Scam operations keep office hours (6.6x more calls per weekday than weekend day); thousands of disposable numbers run a small catalog of recycled scripts (thi

### A1-13  (A1)  Robust MPC ledger-convergence controller for sponsor-bank / fintech (BaaS) omnibus accounts
Problem: After Synapse, regulators are resetting guidance. The core failure was a divergence between fintech sub-ledgers and the bank's FBO (for-benefit-of) omnibus balance that nobody saw until it was too large to close.
Mechanism: The system models the gap between the omnibus balance and the sum of end-user sub-ledger balances as a dynamical state. Disturbances (pending card settlements, ACH returns, chargebacks, timing mismatches) are bounded by learned envelopes. A robust variable-horizon model-predictive controller recomputes funding transfers, holds and payout throttles every few minutes so that the gap 'lands' on a moving target: zero at each settlement cut-off event, whose timing moves. It keeps a guaranteed tube around the planned trajectory. Each sub-ledger update must carry a Merkle inclusion proof, so the controller's state is verifiable by the bank. If the MPC becomes infeasible, meaning the gap cannot be closed by the next cut-off under worst-case disturbances, the system raises a pre-shortfall alert days before a Synapse-style hole appears.
Claim core: A system comprising a state estimator computing a divergence between an omnibus account balance and aggregated verified sub-ledger balances, and a robust model-predictive controller computing funding and hold actions over a variable horizon ending at a settlement event such that the divergence reaches a target within a guaranteed bound, and generating an alert upon infeasibility.
Closest prior art found:
  - [paper sim=0.777] arxiv:2609.23272 | On Control of Drawdown: Robust Invariance and Optimality | 
    Mitigating \emph{drawdown}, the decline in wealth from its running peak, presents a canonical problem in path-dependent risk control. In this paper, we develop a finite-horizon control framework that enforces a prescribed maximum percentage drawdown limit in multi-asset stochastic systems. Our first result is an exact robust-invariance theorem characterizing every control action that preserves a prescribed drawdown limit against all supported returns. We show that every robustly safe control admits a \emph{drawdown-modulated} form: the product of the current drawdown \emph{cushion} and a feasible \emph{normalized direction}. This yields a complete parameterization of robustly drawdown-safe p
  - [paper sim=0.756] s2:a85d96b7f8e7e24a51bb766b5ed9ced889866321 | Systemic Runs and the Dimension of Financial Fragility | 
    Financial institutions meet withdrawals by selling overlapping portfolios, so creditor runs and market prices are jointly determined. I derive an exact asset-market representation. A local architecture rank bounds propagation dimensions for queries that factor through bank-cushion shocks and withdrawal outcomes. One-mode alignment delivers a global scalar representation, while one dominant mode emerges near local spectral instability. A date-0 maturity measure supplies liabilities across cumulative stress windows. Liquidity, depth, and recovery jointly determine local amplification and a hump-shaped uniqueness envelope. Runnable maturity and common-asset exposure can be locally excessive in 
  - [paper sim=0.755] arxiv:2609.03741 | Bayesian Confidence Recalibration and Research-Equilibrium Criticality: Temporal Support in Robust Portfolios | 
    Robust portfolio rules that reconstruct confidence sets after learning need not preserve the evaluator obtained by prior-by-prior Bayesian transport. In the Gaussian model, this discrepancy is summarized by natural-coordinate displacement: inherited transport preserves it whereas fresh reconstruction can replace it. We price evaluator replacement and trace the resulting optimized curvature through endogenous research. Optimized robust value represents protocol regret as a functional Bregman divergence, while a within-vintage rectangular Gaussian benchmark with constant absolute risk aversion (CARA) yields a stopped recalibration tax. In a versioned model-release economy, validated history pr

### A1-14  (A1)  Grid-forming liquidity buffer for DLT-to-RTGS settlement bridges (droop-controlled central bank money injection for atomic-settlement bursts)
Problem: Central banks now settle tokenised securities through DLT-RTGS bridges (e.g. the ECB's Pontes). Atomic DvP settlement creates step-like intraday liquidity demands that can gridlock participants.
Mechanism: A buffer agent at the bridge holds pre-positioned central-bank-money tokens and acts like a grid-forming inverter. It sets the reference intraday liquidity 'frequency', the internal price of immediate liquidity, and responds to the rate of change of pending DvP obligations with droop control: each participant's pre-agreed droop coefficient sets how much liquidity it automatically draws or supplies as the frequency deviates. Current-limiting caps per participant stop any single node from destabilising the network. A network energy function with provable dissipation certifies that the system returns to equilibrium after any bounded burst. Injections are collateralised automatically from pledged tokenised assets on the DLT side.
Claim core: A settlement system comprising a bridge between a distributed ledger and a real-time gross settlement system, and a liquidity buffer controller that computes a liquidity reference signal from a rate of change of pending settlement obligations and allocates automatic liquidity transfers to participants according to respective droop coefficients subject to per-participant limits.
Closest prior art found:
  - [paper sim=0.781] s2:aa0a79f14c49b5124b65ec4668f1ff4bd205ea50 | Managing settlement risks in tokenised money: Applying the Principles for Financial Market Infrastructures to digital assets | 
    The rise of stablecoins, tokenised bank deposits, and central bank digital currencies (CBDCs) is reshaping the mechanics of settlement in modern financial systems. While debate has focused on technological innovation — programmability, atomic execution, and 24/7 availability — the risk implications of tokenised money depend less on token design than on the settlement architecture that governs it. This paper argues that real-time gross settlement (RTGS) systems provide the appropriate benchmark for evaluating tokenised arrangements from a risk lens, because tokenised transfers operate on a gross, transaction-by-transaction basis and therefore inherit RTGS-level expectations of legal finality,
  - [paper sim=0.756] s2:3f30aee1571ec23f611791cf43070dc64ca410a3 | Tokenisation and the reconfiguration of capital market infrastructure : T+0 settlement, mathematical trust, and multi-currency yield curves | 
    Tokenisation is increasingly influencing the structure of monetary and capital market infrastructure by enabling new forms of settlement, asset representation, and market accessibility. This paper examines how the synchronisation of programmable forms of tokenised money and tokenised yield-bearing assets alters the dynamics of capital utilisation by enabling broader participation in financial markets. As a result, this new infrastructure creates new distribution channels and revenue models for financial institutions. Within such a framework, both the payment leg and the asset leg of a transaction can interact on a shared infrastructure, enabling atomic delivery-versus-payment (DvP) settlemen
  - [patent sim=0.749] patent:US20260004352A1 | DYNAMIC GRID CURVES FOR GASLESS DECENTRALIZED TOKEN SWAPS | 1inch Limited
    Systems and methods for transferring resources using dynamic grid curves are disclosed. A system receives a transfer request specifying an input resource type, a target resource type, an amount of input resources, and an identifier of a storage application associated with the user. The system determines a plurality of current transfer rates, each corresponding to a respective blockchain. The system may query each blockchain to determine an on-chain computation overhead for processing the transfer. Utilizing a maximal current transfer rate and the determined computation overhead, the system generates a grid curve representing the amount of target resources available for transfer as a function

### A1-15  (A1)  Forecast-sized offline mandates for machine and agent payments using physics-informed connectivity forecasts
Problem: Machine and agent payments (network 'Agent Pay for Machines', first bank agentic transactions) assume connectivity. Vehicles, drones, ships and rural IoT go offline. Over-sized offline allowances create double-spend and fraud exposure; under-sized ones strand the machine.
Mechanism: Before a mission or route, the issuer predicts the timing and length of connectivity gaps along the agent's planned path. The forecast is built from public satellite-constellation geometry, weather attenuation, cellular coverage maps and routing data, using a physics-informed link-state forecaster. The issuer then provisions time-boxed offline credentials (pre-authorised token bundles or offline CBDC value) sized to the expected consumption during each forecast gap plus a risk margin. Each credential expires at the forecast reconnection time plus tolerance and is valid only within the forecast geographic corridor. On reconnection, spend is reconciled and the forecaster is updated with the realised gaps.
Claim core: A method comprising: obtaining a planned route of an autonomous payer; forecasting connectivity gaps along the route from orbital, weather and coverage data; provisioning offline payment credentials whose value, validity time and geographic scope are determined from the forecast gaps; and reconciling spend upon reconnection.
Closest prior art found:
  - [paper sim=0.751] arxiv:2609.26696 | Reading the Sky to Forecast the Ground: Physics-Informed Link-State Forecasting for LEO Networks at Any Location | 
    In this paper, we introduce Gnomon, a physics-informed system that forecasts user-perceived low-Earth-orbit (LEO) downlink throughput, uplink throughput, and round-trip time (RTT) under different levels of trace availability. Gnomon's physics layer reconstructs the serving geometry and four-leg bent-pipe attenuation from public weather, orbital, routing, and licensing data. Based on what is available, Gnomon conditions on the target terminal's own history (Mode 1), measurements from nearby publicly reachable dishes (Mode 2), or the physical covariates alone (Mode 3) to predict the link state: Modes 1 and 2 share a fine-tuned time-series foundation model, while Mode 3 uses a compact boosted-t
  - [paper sim=0.750] arxiv:2608.01341 | 402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments | 
    Programmable-payment protocols such as x402 enable per-request micropayments, but they do not determine which payable service an autonomous agent should buy under a finite wallet. We formulate this buyer-side problem as agent-native payment decision-making: contextual provider selection under wallet pressure, chosen-only paid feedback, and changing market conditions. We propose 402Pilot, a protocol-agnostic buyer-side decision layer between autonomous agents and payment execution that implements purchasing policies for selecting among payable providers. We instantiate it with PA-DCT, a payment-aware discounted contextual Thompson-sampling policy that adapts purchasing decisions under wallet 
  - [paper sim=0.746] arxiv:2609.25960 | CausalLoss-Fin: Attributing Financial-Agent Loss to Decisions and Infrastructure Faults | 
    When an agent handling a payment exception loses money, the agent-step attribution methods this paper compares against will name one of its actions. They will do so even when a settlement message was dropped and the agent never had a chance: they intervene on agent actions and do not expose infrastructure faults as intervenable variables, so every dollar they explain is charged to a decision. We take a benchmark whose fault process is explicit and replayable, decompose each episode's realised delivery schedule into named, individually repairable messages, and intervene on both the agent's choices and the infrastructure's. A telescoping identity splits any policy's loss exactly three ways: an

### A1-16  (A1)  Reachability-certified pre-emptive holds: intercepting stolen funds ahead of the money instead of chasing hops
Problem: Cyber-fraud reporting systems (India's 1930 helpline and CFCFRMS, UK APP reimbursement) place liens hop by hop after the money has moved. Mule layering outruns them within minutes, and the 'golden hour' is lost.
Mechanism: When fraud is reported, the system models the stolen funds as an adversary with bounded manoeuvring capability on the inter-bank payment graph. The bounds are per-rail latency, per-account velocity and limits, new-payee cooling periods, and cash-out points (ATMs, crypto on-ramps, merchant cash-back). From these it computes the forward reachable set of accounts over time. It then solves for the minimum set of accounts to place under short, auto-expiring holds now, such that every reachable cash-out path is covered before the funds could arrive: a capture certificate, analogous to robust safety certificates against manoeuvring obstacles. Hold requests are signed, scoped and time-limited, and are issued to participating banks. Each bank solves its part through a distributed ADMM formulation, so no raw transaction data leaves the bank. Unused holds release automatically.
Claim core: A method comprising: receiving a fraud report identifying a source account and amount; computing, over a payment graph with per-edge timing and capacity constraints, a time-indexed reachable set of accounts and cash-out nodes; selecting a minimal set of accounts whose temporary hold intercepts all reachable cash-out paths before the funds can arrive; and transmitting signed, time-limited hold requests to institutions holding the selected accounts.
Closest prior art found:
  - [paper sim=0.757] s2:9553c7f08cd59d661b917332ba3e388f1c48f2f9 | A Comprehensive Review of Money Mule Networks and Financial Fraud Detection Techniques | 
    The fast growth of digital financial systems has greatly multiplied the scale and complexity of financial crimes based on money mule networks. The money mule acts as the intermediary in these operations, helping to move stolen funds from accounts they were directly paid into, to more legitimate pathways utilized by bankers and financial institutions. With financial institutions and regulators increasing the pressure to combat fraud, an understanding of how money mules are recruited and operate is invaluable. This paper provides a literature review of current studies on money mule activity and monetary fraud detection. The review is a synthesis of papers that focus on recruitment strategies, 
  - [paper sim=0.753] s2:e3db443b55fbb1960ad2a9005fbe397ff9273a07 | Adaptive Graph-Based Risk Scoring for Real-Time Instant Payment Systems | 
    Instant payment rails and mobile money platforms such as UPI, Pix, and FedNow require fraud decisions in a few hundred milliseconds, but most deployed and published fraud models are batch oriented and sequence only. They are trained and evaluated offline, treat each account in isolation, and provide limited visibility into mule networks and collusive cash out structures. This paper presents a graph based streaming risk scoring architecture that brings graph neural network (GNN) style inference into the authorization path while respecting a sub 300 ms end to end service level objective. The system maintains a dynamic transaction graph over accounts, devices, merchants, and institutions, updat
  - [paper sim=0.752] s2:23c7490b635031b1fc5fd493192e786acdeaee2a | Instant Fraud Detection Gateway for Secure Digital Transactions | 
    The rapid expansion of digital payments in India, led by the Unified Payments Interface (UPI), has significantly enhanced financial accessibility and transaction efficiency, processing over 12 billion transactions per month in 2024. However, this growth has been accompanied by a sharp rise in fraud, with reported losses exceeding INR 1,400 crore in 2023–24, primarily due to phishing, identity spoofing, money mule networks, and exploitation of dormant or fraudulent accounts. This paper presents an Instant Fraud Detection Gateway, a real-time pre-transaction security layer that integrates seamlessly with existing payment infrastructures. The system performs recipient validation against authori

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

Write the answer to: runs/2026-09-30/llm_responses/judge_001.json
