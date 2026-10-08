# TASK judge_003

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A2a-02  (A2a)  Bounded-intent mandates for AI shopping agents
Problem: AI agents that pay on a user's behalf can overspend or be prompt-injected into paying the wrong merchant.
Mechanism: User signs a machine-verifiable spending policy (merchant category, price ceiling, time window, item class); the network token carries a policy hash and the issuer verifies a policy-compliance proof on every agent-initiated authorisation.
Claim core: 
Closest prior art found:
  - [paper sim=0.750] arxiv:2609.11757 | Signing the Transaction but Not the Decision: Whisper Attacks and a Binding Defense for AP2 | 
    Software agents are beginning to shop and pay on a person's behalf. Agent payment protocols such as AP2 produce cryptographically valid signatures for completed purchases, yet do not constrain the decisions that lead to them. Consequently, ordinary product-description text can steer a shopping agent into forming a cart that passes every protocol check but no longer matches the user's request. In this paper, we show that this vulnerability enables three related attacks. In the first attack, the agent is steered into fetching another user's payment credentials. In the second, it assembles a cryptographically valid cart whose contents do not match what the user was shown. In the third, a single
  - [paper sim=0.748] arxiv:2608.23858 | Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2) | 
    The Agent Payments Protocol (AP2), introduced by Google, enables large language model (LLM)-driven shopping agents to authorize and execute payments on behalf of users. Its signed Checkout and Payment Mandates protect the integrity of transaction data after signing. Agent interactions and external inputs that shape a transaction before authorization remain outside that protection, including Agent-to-Agent Protocol (A2A) messages and Model Context Protocol (MCP) tool calls. Prior work identified replay and prompt-injection attacks in AP2 v0.1. AP2 v0.2 addresses some of these issues but adds capabilities and deployment assumptions that require renewed analysis. We present a systematic securit
  - [paper sim=0.746] arxiv:2609.00060 | A Formal Analysis of Agent Payment Protocols | 
    Agent payment protocols are emerging as a key transaction layer for autonomous commerce, enabling AI agents to purchase goods and services and execute payments on users'behalf. Unlike conventional payment flows, they distribute user intent, delegated authority, credential use, settlement, and fulfillment across multiple actors and stages, creating security dependencies that no single message or participant can enforce. Yet these guarantees remain largely implicit across evolving specifications, schemas, and reference implementations, with little systematic formal analysis. We formalize four representative agent payment protocols: x402, MPP, ACP, and AP2 in Tamarin. Using a common abstraction

### A2a-03  (A2a)  Critical-slowing-down deposit-run early warning
Problem: Digital bank runs (e.g. SVB 2023) unfold in hours, faster than supervisory liquidity monitoring.
Mechanism: Compute rolling autocorrelation and variance of intraday deposit outflows by segment (early-warning signals of a phase transition), fuse with social-media sentiment velocity, and automatically pre-position collateral at the central bank discount window when the combined index crosses a threshold.
Claim core: 
Closest prior art found:
  - [paper sim=0.745] s2:b9334b24770609574acf15ce5d78f8b45b0b49a7 | A Multi-Dimensional Integrated Analysis of Behavioural Finance and Digital Bank Runs: A Case Study of the Failure of Silicon Valley Bank | 
    With the development of the digital economy, traditional theories of bank runs have shown some limitations and fail to fully explain the rapid spread of bank runs in the digital era. Taking the failure of Silicon Valley Bank (SVB) as an example, this paper reviews related research on traditional bank run theory, behavioural finance, and digital communication mechanisms to construct a new analytical framework of "traditional vulnerabilities - behavioural biases - digital dissemination". The causes of the SVB event can be understood as the combined effects of traditional vulnerabilities, depositor behaviour, and Internet-based information dissemination. Liquidity mismatch and a high proportion
  - [paper sim=0.740] doi:10.2139/ssrn.7270940 | Speed, Fraud, and Bank Liquidity: The Operational Architecture of Real-Time Payment Systems | 
    A real-time payment system settles each payment within seconds, around the clock, with finality. The defining design choice is to drive the settlement window to zero. This paper shows that the zero window shuts off two stabilizers at once. A universal settlement delay buys time to screen fraud before settlement, and it restores the netting that real-time settlement takes away from banks, so one design primitive acts on a fraud channel and a bank-liquidity channel together and the welfare-optimal architecture must weigh it against both. The fraud side adds two suspension tools, targeted and system-wide, by analogy to speed bumps and circuit breakers in equity markets; the liquidity side adds 
  - [paper sim=0.736] doi:10.2139/ssrn.7117550 | Bounding a Digital Run: Realized Stablecoin Runs and CBDC Holding Limits for the Digital Euro | 
    A retail CBDC lets depositors move into central-bank money instantly, so the digital euro proposes a per-person holding limit whose design turns on the household flight-to-safety schedule. That schedule has never been observed, because no retail CBDC run has occurred, and every existing calibration assumes it. We first recover the schedule from realized stablecoin runs, the closest observed flights from a digital par claim, measuring it at wallet level on the March 2023 USDC depeg and confirming its direction on the May 2022 USDT and 2020 money-market-fund runs. This replaces the assumed run process with a standing, updatable, measured input. We then separate the stock a holding limit bounds

### A2a-04  (A2a)  Zero-knowledge income attestation from bank sessions
Problem: Lenders demand full bank statements, exposing far more data than needed.
Mechanism: zkTLS proof generated over the user's live online-banking session proves 'average monthly income > X for 6 months' without revealing transactions; lender verifies proof against bank's TLS certificate.
Claim core: 
Closest prior art found:
  - [patent sim=0.739] patent:US20150052041A1 | METHOD, SYSTEM, SERVICE, AND COMPUTER PROGRAM PRODUCT FOR VERIFICATION AND DELIVERY OF EMPLOYMENT AND INCOME INFORMATION | PointServ, Inc.
    A technique of employment and income verification for making a lending decision is disclosed that does not require requesting manual employment and income verification and performing a manual comparison of the results of such verification to payroll documents provided by the borrower. The borrower provides authentication information (e.g., login credentials), which a verification service utilizes to obtain the borrower's employment and income information from a payroll provider. The verification service delivers verified employment and income data and payroll documents to the lender, which can be provided securely in a tamper proof form. Techniques to provide privacy protection for the borro
  - [patent sim=0.739] patent:US20150213550A1 | METHOD, SYSTEM, SERVICE, AND COMPUTER PROGRAM PRODUCT FOR VERIFICATION AND DELIVERY OF EMPLOYMENT AND INCOME INFORMATION | PointServ, Inc.
    A technique of employment and income verification for making a lending decision is disclosed that does not require requesting manual employment and income verification and performing a manual comparison of the results of such verification to payroll documents provided by the borrower. The borrower provides authentication information (e.g., login credentials), which a verification service utilizes to obtain the borrower's employment and income information from a payroll provider. The verification service delivers verified employment and income data and payroll documents to the lender, which can be provided securely in a tamper proof form. Techniques to provide privacy protection for the borro
  - [patent sim=0.727] patent:US20150052033A1 | METHOD, SYSTEM, SERVICE, AND COMPUTER PROGRAM PRODUCT FOR VERIFICATION AND DELIVERY OF INCOME TAX RETURN INFORMATION | PointServ, Inc.
    A technique of income verification for making a lending decision is disclosed that does not require requesting tax transcripts from the Internal Revenue Service and performing a manual comparison of the tax transcripts to tax returns provided by the borrower. The borrower provides authentication information (e.g., login credentials), which a verification service utilizes to obtain the borrower's tax information from an E-file tax preparation provider. An optional checking process can be used to check that the tax return has not been amended. The verification service delivers verified income data and tax returns to the lender, which can be provided securely in a tamper proof form. Techniques 

### A2a-05  (A2a)  Shelf-life-weighted post-quantum migration planner
Problem: Banks cannot migrate all cryptography to PQC at once; harvest-now-decrypt-later threatens long-lived data.
Mechanism: Network scanner fingerprints TLS/HSM/key usage, tags each flow with the confidentiality shelf-life of the data it carries, and computes a migration order that minimises quantum-exposure = shelf-life x traffic volume x algorithm weakness.
Claim core: 
Closest prior art found:
  - [paper sim=0.749] s2:4839f2b68c0291f350d4351b22dba3a8724fb2c3 | Post-Quantum Cryptography for Secure Banking Transactions | 
    Quantum computers are growing faster every year, and that progress puts today’s classical encryption at serious risk. Once these machines reach full power, staple protocols like RSA and elliptic-curve cryptography SSDs become tomorrow's digital lockpicks, threatening the secrecy of everyday online banking. In response, many researchers are rallying behind post-quantum cryptography (PQC), a fresh toolkit meant to shrug off quantum decoding tricks. This paper examines how prepared the banking world is for that shift, using a systematic review of literature, pilots, regulations, and benchmarks issued between 2018 and 2025. Results show firms are already alert, testing hybrid systems alongside N
  - [paper sim=0.743] s2:77e84be095811502ff0794b284927b1ef79924f8 | Decision Framework for Selection of Post Quantum Cryptographic Algorithms and Libraries | 
    With the emergence of quantum computing, conventional cryptographic primitives, which are currently deployed in enterprise applications, are becoming increasingly vulnerable to compromise. To become quantum resilient, these methods must be replaced with Post-Quantum Cryptographic (PQC) algorithms. At present, only a limited number of quantum-safe algorithms have been officially approved, while many others remain under evaluation. However, multiple implementations of these algorithms are emerging from both open-source communities and commercial vendors. The support features offered by these libraries and the performance of the PQC algorithm implementations can vary significantly across these 
  - [paper sim=0.740] arxiv:2605.17955 | Operationalising Post Quantum TLS Automated Configuration Profiling and Hybrid PQC Deployment in Financial Infrastructure | 
    Organisations are upgrading their cryptographic infrastructure to become quantum safe before large scale quantum computers materialise. Post quantum cryptography (PQC) standards now exist for key exchange and digital signatures, but the urgent question for adopters is how to operationalise PQC in complex environments with confidence. In banking, Transport Layer Security (TLS), for example, protects data in transit across public facing channels and internal services, and is terminated at many heterogeneous endpoints (web servers, API gateways, load balancers, reverse proxies), each a potential quantum vulnerable component and migration target. We argue that the bottleneck is operational rathe

### A2a-06  (A2a)  Mule-network epidemiology (R0 for money mules)
Problem: Money-mule recruitment spreads socially; banks close accounts one at a time.
Mechanism: Estimate a reproduction number for mule recruitment from temporal transaction graphs, identify superspreader recruiter accounts, and prioritise interventions to push R below 1.
Claim core: 
Closest prior art found:
  - [patent sim=0.753] patent:US20250315834A1 | Money mule detection using link prediction | Actimize Ltd.
    A system is adapted to identify suspected mule accounts. It includes a processor configured to select seed entities, and identify a network of accounts associated with each seed entity. For networks that includes at least one known mule account, the processor computes a similarity score between each pair of accounts and, based on the similarity scores, clusters the accounts, labels the clusters as to whether they are high-mule-rate clusters, and uses the clusters to train a link prediction model. The processor then, in real time, receives a transaction for an entity, identifies a second network of accounts associated with the entity and, with the link prediction model, for each pair of accou
  - [patent sim=0.739] patent:US20250315834A1 | MONEY MULE DETECTION USING LINK PREDICTION | ACTIMIZE LTD.
    A system is adapted to identify suspected mule accounts. It includes a processor configured to select seed entities, and identify a network of accounts associated with each seed entity. For networks that includes at least one known mule account, the processor computes a similarity score between each pair of accounts and, based on the similarity scores, clusters the accounts, labels the clusters as to whether they are high-mule-rate clusters, and uses the clusters to train a link prediction model. The processor then, in real time, receives a transaction for an entity, identifies a second network of accounts associated with the entity and, with the link prediction model, for each pair of accou
  - [patent sim=0.692] patent:TR2025004325A2 | A BROKER ACCOUNT DETECTION SYSTEM | Tuerkiye Garanti Bankasi Anonim Sirketi
    This invention relates to a system (1) that enables the classification of bank customers using classification algorithms and the detection of whether customers have mule accounts.

### A2a-07  (A2a)  Ultrasonic liveness nonce for voice-channel authentication
Problem: Voice deepfakes defeat call-centre voice biometrics.
Mechanism: During a call the bank app on the customer's registered phone emits an inaudible ultrasonic nonce; the call-centre audio stream must contain the acoustic echo of that nonce, proving a live person co-located with the registered device.
Claim core: 
Closest prior art found:
  - [patent sim=0.725] patent:US20260261614A1 | VOICE AUTHENTICATION BASED ON BACKGROUND AUDIO | Wells Fargo Bank, N.A.
    Systems and techniques may generally be used for verifying a caller is authentic. An example technique may include receiving an authentication request during an audio call with a caller, playing, during the audio call, a set of sounds, capturing audio received from the caller during the audio call, and processing the audio to generate a voice portion including the voice data and to attempt to generate a background portion including a reverb of the set of sounds. The example technique may include determining whether the background portion including the reverb was generated, and in response to determining that the background portion including the reverb was not generated, outputting an indicat
  - [patent sim=0.722] patent:EP4706037A2 | Active voice liveness detection system | Pindrop Security, Inc.
    Disclosed are systems and methods including software processes executed by a server that detect audio-based synthetic speech ("deepfakes") in a call conversation. Embodiments include systems and methods for detecting fraudulent presentation attacks using multiple functional engines that implement …
  - [patent sim=0.715] patent:US20260179621A1 | AUDIO AUTHENTICATION HARDWARE KEY AND DETECTION ECOSYSTEM AND MIXED REALITY ARTIFICIAL INTELLIGENCE TRIP PLANNER | Meta Platforms, Inc.
    Methods, apparatuses, and computer program products for the authentication of human speech through the registration and verification of public and private keys associated with audio. This audio authentication hardware key and detection ecosystem may enable casual users and public figures alike to provide a positive verification that a person is who they say they are and endorse their speech. The audio code underlaying the human speech gets encoded with identifiers that effectively watermark the audio code to make it recognizable to a server and the human speech verifiable. To display this verification at a system-level within a social media platform, news channel, podcast library, or video s

### A2a-08  (A2a)  Sensor-attested programmable escrow for trade finance
Problem: Trade finance relies on paper documents that are easy to forge.
Mechanism: Tokenized deposit escrow releases automatically when IoT sensor attestations (GPS, container seal, temperature) signed by hardware roots of trust satisfy the letter-of-credit conditions.
Claim core: 
Closest prior art found:
  - [patent sim=0.740] patent:US20220300964A1 | SYSTEMS AND METHODS FOR BLOCKCHAIN-BASED ESCROW MANAGEMENT | RoeketBC, Limited
    Systems and methods are disclosed for verifying and processing financial transactions. In certain embodiments, the techniques involve receiving transaction data corresponding to a financial transaction from a sender and detecting and verifying transaction terms from the transaction data. The system then receives a second set of transaction data corresponding to the financial transaction from a receiver and verifying that the first set of transaction data corresponds to the second set of transaction data. Based on that verification, the system initiates the transfer of cryptocurrency or other digital assets associated with the financial transaction.
CLAIM 1: A system for transaction managemen
  - [patent sim=0.735] patent:US20250384410A1 | PROACTIVE IN-VEHICLE PAYMENT SYSTEM USING SENSOR DATA WITH MACHINE LEARNING | Car IQ Inc.
    Aspects of the present disclosure describe a system comprising a processor and memory storing instructions, which when executed by the processor, enable the system to detect a payment-related event using vehicle sensors, such as a camera or GPS unit. The detection can involve a machine learning model trained to recognize objects associated with the payment-related event while minimizing false positives. Upon detecting the event, the system can handle the electronic payment by utilizing an in-vehicle digital wallet to execute the payment and recording the transaction on a blockchain-based ledger.
CLAIM 1: A system comprising: an in-vehicle digital wallet; a processor; and a memory storing ins
  - [patent sim=0.723] patent:US12437293B2 | Intelligent method and apparatus for secure payment transaction leveraging environment sensing real-time smart hash chain sensors | Bank of America Corporation
    A real-time payment security method and system for preventing eavesdropping attacks on computing devices may include a plurality of sensors configured to detect anomaly-type behavior indicative of a security threat. The plurality of sensors may be configured to share data, and may be configured to eliminate false-positive anomaly-type behavior indicative of a security threat. The system and method may further include a hash chain network comprising a plurality of hash nodes, and a dynamic authentication mapper, wherein the dynamic authentication mapper may be powered by a cognitive artificial intelligence (AI) engine, and wherein the dynamic authentication mapper may be configured to generat

### A2a-09  (A2a)  Cash-flow-elastic credit line
Problem: Static credit limits mismatch volatile gig-worker income.
Mechanism: Credit limit recomputed daily from account-aggregator cash-flow forecasts with uncertainty bands; limit follows the lower confidence bound.
Claim core: 
Closest prior art found:
  - [paper sim=0.681] s2:d90e809e5b4e5ebab941c057428d358f3f8fb7bc | Lemons in the Labour Market: Information Asymmetry, Adverse Selection, and Credit Exclusion in India's Gig Economy | 
    India’s gig economy is projected to grow from 7.7 million workers in FY2020–21 to 23.5 million by 2029–30, yet the overwhelming majority of platform workers remain excluded from formal credit markets. The mechanism is informational, not financial: traditional credit-scoring systems cannot interpret the data that gig workers produce. Drawing on Akerlof’s (1970) model of adverse selection and Spence’s (1973) signalling theory, this paper argues that India’s gig credit market exhibits the structural properties of a lemons market, where lenders, unable to distinguish creditworthy from non-creditworthy informal borrowers, either price credit beyond reach or exit altogether. Two existing data sour
  - [paper sim=0.681] s2:8a388deb3261fb51b3428f3f21cf164a47dafe93 | From Deposits to Overdrafts: Dynamic Portfolio Adjustment and Financial Fragility in a Sraffian Supermultiplier Stock‐Flow Consistent Model | 
    This paper develops a Sraffian Supermultiplier Stock–Flow Consistent (SSM‐SFC) model in which the growth of government expenditure anchors long‐run demand‐led growth. It replaces Tobin‐style desired stocks with dynamic portfolio adjustment: households rebalance deposits, equities, and overdrafts as interest rates, expected yields, capital gains, and liquidity conditions change. The resulting deposits‐to‐overdrafts shift endogenously generates consumer debt and influences equity valuation and share issuance, as well as the paths of income distribution and public debt. The framework traces these balance‐sheet movements to firms' capital structure, banks' profitability and net worth, and govern
  - [paper sim=0.675] s2:6611e4a46c07032daa60e673813d32130b78a7e9 | Assessing Bank Earnings Quality Through Net Income and Operating Cash Flow Matching: A Case Study of Bank of America | 
    Although net income is the standard profitability measure, it offers limited insight into earnings quality in the absence of the underlying cash flow support for reported earnings. This limitation is particularly acute for large banks, which require ongoing liquidity to support lending, trading and other commitments. This study conducts a case study diagnostic analysis that first measures the Cash Flow from Operations/Net Income (CFO/NI) ratio, then decomposes the gap using the indirect method and examines the reason behind, subsequently evaluates credit risk indicators relative to those of peer banks. The study finds that Bank of America's 2025 CFO/NI ratio was roughly 0.41, with shortfall 

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

Write the answer to: runs/2026-09-30/llm_responses/judge_003.json
