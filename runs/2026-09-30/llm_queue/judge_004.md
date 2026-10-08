# TASK judge_004

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A2a-10  (A2a)  Checkout affordability digital twin
Problem: Customers take on purchases/BNPL they cannot afford.
Mechanism: Simulate the customer's next 90 days of balances with the proposed purchase on a financial digital twin and show probability of overdraft before approval.
Claim core: 
Closest prior art found:
  - [paper sim=0.724] s2:24a4c492f34ea6556e777a576d7982e55b75de00 | Buy Now Pay Later (BNPL) Systems: Innovation, Risks, and Regulatory Transformation in Digital Finance | 
    Buy now pay later, or BNPL, instruments have become one of the fastest-rising phenomena in contemporary finance, introducing innovative approaches to consumer credit. Integrated into e-commerce platforms, BNPL options allow customers to make purchases with flexible payment terms and do not charge additional fees for such transactions. This chapter discusses the theoretical framework of the BNPL concept, its nature, and the different methods and regulations used. Moreover, the mechanisms that drive the adoption and usage of BNPL products by consumers will also be presented. The impact of buy now pay later services on the financial and digital ecosystems of societies will be highlighted. The c
  - [paper sim=0.721] s2:9a822af24312ba9d7a438567e80c43fcbed736b8 | Real-Time Credit Risk Decisioning at Checkout for Short-Term Installment Products: Feature Availability Constraints, Adverse Action Explainability, and Portfoli | 
    Extending credit at the moment of purchase compresses an underwriting decision that traditionally takes minutes or days into a window measured in milliseconds, and every part of the decision has to change to fit. This paper sets out an architecture for checkout-time credit decisioning on short-term installment products, organised around three constraints that shape it. The first is feature availability: a highly predictive signal is worth nothing at checkout if it cannot be obtained, validated, and consumed inside the time budget, so availability, freshness, and latency must be treated as first-class properties of a feature rather than as engineering details discovered late. The second is ad
  - [paper sim=0.704] s2:d8b27ad0dea6b4e0b446d610d675824555d39104 | Unseen Liabilities: Conceptualizing Ghost Debt and Financial Vulnerability in BNPL Ecosystems—A Systematic Review | 
    This study systematically reviews how BNPL ecosystem design interacts with information asymmetry and behavioral biases to produce what this review conceptualizes as “ghost debt,” an author-developed construct distinguished from related notions—debt opacity, hidden debt, over-indebtedness, debt stacking, financial fragility, repayment burden, and credit invisibility. Following PRISMA 2020 guidelines, a Boolean search (“buy now pay later” OR “BNPL”) was run in Scopus (TITLE-ABS-KEY field; English-language, peer-reviewed journal articles, 2010–2026) for studies addressing BNPL design, consumer decision-making, debt opacity, or financial vulnerability. Of 179 records screened, 26 studies passed 

### A2a-11  (A2a)  SKU-level carbon footprint card
Problem: Card carbon trackers use coarse merchant-category averages.
Mechanism: Parse itemised e-receipts linked to card transactions and compute SKU-level emissions.
Claim core: 
Closest prior art found:
  - [patent sim=0.799] patent:US20210224819A1 | CARBON FOOTPRINT TRACKER | International Business Machines Corporation
    In an approach to carbon footprint tracking, responsive to determining that a transaction to purchase an item for a user is detected by a computer, a total carbon emissions for the original item is calculated. One or more alternatives to the original item are located. The total carbon emissions for each alternative to the original item is calculated. The user is notified of the total carbon emissions for the original item and the total carbon emissions for each alternative to the original item where the carbon emissions are lower for the alternative item than for the original item. An indication of a final item chosen by the user is received, where the final item is either the original item 
  - [patent sim=0.796] patent:US10902484B1 | System and method for carbon footprint determination | Morgan Stanley Services Group Inc.
    A system and method may determine or display the carbon emissions impact for transactions, by for example receiving from transaction data sources data items describing transactions, each transaction associated with a user, a merchant, and an amount; for each transaction receiving or creating carbon emissions impact data for the merchant associated with the transaction; and deriving from the amount associated with the transaction and the carbon emissions impact data for the merchant associated with the transaction a carbon emission value associated with the transaction. Each data item may include a transaction amount and a merchant identifier, and/or other information. Calculating carbon emis
  - [patent sim=0.783] patent:US20110213690A1 | CARBON FOOTPRINT DETERMINATIONS | BANK OF AMERICA CORPORATION
    Described herein are various apparatuses, methods, and computer program products for providing a carbon-footprint modeling environment that determines a consumer's carbon footprint based on the consumer's acquisition of goods and/or services, as indicated by the consumer's transaction data. For example, the carbon-footprint modeling environment collects the consumer's transaction data for a predefined period of time and identifies transaction data that indicates the consumer's acquisition of goods and/or services that, when produced and/or consumed, result in greenhouse gas emissions. According to some embodiments, the carbon-footprint modeling environment categorizes goods and/or services i

### A2a-12  (A2a)  Revocable consent tokens with deletion proofs
Problem: Open banking users cannot verify data was deleted after revoking consent.
Mechanism: User-held consent tokens; data recipients must return a signed deletion attestation anchored in a transparency log upon revocation.
Claim core: 
Closest prior art found:
  - [patent sim=0.662] patent:US12719671B1 | Consent chain certification | Cohen-White; Noreen
    A method is disclosed for generating a signature token by receiving at least one consent artifact from a user, validating the user's identity based on a plurality of identity verification artifacts and the consent artifact, generating a consent certificate that associates a verification request with the identity and consent artifacts, and applying a binding operation to produce the signature token.
CLAIM 1: A method for generating a signature token for a consent event, the method comprising: receiving a verification request of an identity of a first user; detecting the consent event for the verification request of the identity; receiving at least one consent artifact for the consent event, w
  - [patent sim=0.654] patent:US12717952B2 | System and method of processing a data access request | The Toronto-Dominion Bank
    Computing platforms, methods, and storage media for processing a data access request are disclosed. Exemplary implementations may: generate, at the computing platform and based on a received data access request, a revocable 1:1:1 token that authorizes data sharing for a specific combination of third party application-aggregator-institution for a user associated with a communication device; and cause display of a user interface including a list of a plurality of third party applications for which data access is currently granted and for which a revocable 1:1:1 token is stored, the user interface enabling selective revocation of data access from among the listed plurality of third party applic
  - [patent sim=0.652] patent:US20110287748A1 | Consent, Signature and Recording Retention in a Certified Communications System | 
    System has consent, signature, recording and retention functions. Near post-sessional data acquisition gathers nominal comm device information from participants. Active online phones are sent a SMS with the recorded event ID, a hyperlink and password for system access. Otherwise, data is acquired for another text message enabled phone or user email. If disconnected, the user is called for additional data. A contractual relationship is established with these functions. With an ACK-consent upon system access, an ACK-consent by the parties, a RECORD ON command, and a recorded intent-to-contract, the system creates an enforceable contract by storing the ACKs and recorded session.
CLAIM 1: A meth

### A2a-13  (A2a)  Cross-chain stablecoin redemption router
Problem: Stablecoin redemption to fiat is fragmented across chains and banks.
Mechanism: Router atomically burns on source chain and settles on instant bank rails, choosing path by liquidity and fees.
Claim core: 
Closest prior art found:
  - [patent sim=0.712] patent:US20260268400A1 | CRYPTO BASED MONETARY SYSTEM OF TRADE WITH PROTOCOL ENFORCED CROSS CHAIN ATOMIC SETTLEMENT | Swopblock LLC
    The disclosed system operates across first and second blockchains. An exchange medium resides at native addresses on each. Nodes bind declared face value to a base cryptocurrency and reassign it between base cryptocurrencies while preserving total declared face value. Wallets submit buy and sell reservations that place protocol holds on identified amounts. A single signed fill references the reservations and, when validated, simultaneously disburses the held exchange medium and delivers a native asset. A relay consensus computes relay proofs from participating networks, selects a maximum proof that satisfies a release threshold, and triggers release of all holds without time locks or custodi
  - [patent sim=0.706] patent:US20240112155A1 | METHOD FOR PROVIDING STABLECOIN SERVICES OVER THE BLOCKCHAIN NETWORK AND BLOCKCHAIN SYSTEM USING THE SAME | Wemade Co., Ltd.
    A method for providing stablecoin services over the blockchain network, includes steps of: (a) issuing n*m second-type stablecoins to thereby supply them to liquidity pool; and (b) instructing stabilizer to withdraw j first-type stablecoins from treasury electronic wallet to stabilizer electronic wallet, exchange the withdrawn j first-type stablecoins for j*i second-type stablecoins according to exchange ratio i, and burn the j*m second-type stablecoins, or issue k second-type stablecoins to the stabilizer electronic wallet through minter, and exchange the issued k second-type stablecoins for k/i first-type stablecoins according to exchange ratio i, and to stake j*|i-m| second-type stablecoi
  - [patent sim=0.704] patent:US20260236898A1 | STABLECOIN AS A MEDIUM OF EXCHANGE ON A BLOCKCHAIN-BASED TRANSACTION NETWORK | Ceres Coin LLC
    Aspects of this disclosure relate to various systems and methods for use in a regulated industry and using an SEC qualified stablecoin as a store of value and medium of exchange on a blockchain-based transaction network. The system includes a stablecoin blockchain system with a stablecoin blockchain framework, a stablecoin ecosystem, and a stablecoin blockchain transaction network. The stablecoin blockchain system facilitates transactions between stablecoin blockchain participants within the stablecoin ecosystem. The stablecoin ecosystem conducts transactions across a stablecoin blockchain transaction network and a distributed blockchain ledger.
CLAIM 1: A system for providing a blockchain-b

### A2a-14  (A2a)  Cognitive-decline signals for elder abuse prevention
Problem: Elderly customers with cognitive decline are exploited financially.
Mechanism: Longitudinal drift in digital-banking interaction patterns (navigation errors, typing speed, repeated actions) flags decline; triggers trusted-contact escalation and lower transfer limits.
Claim core: 
Closest prior art found:
  - [patent sim=0.697] patent:US20210186410A1 | COGNITIVE DECLINE DETECTION SYSTEM | PANASONIC INTELLECTUAL PROPERTY MANAGEMENT CO., LTD.
    Cognitive decline detection system includes obtainment unit and determination unit. Obtainment unit obtains the amount of movement during a sleep period and the amount of movement during a non-sleep period of a user for each day, the non-sleep period being the period other than the sleep period. Determination unit determines that the cognitive function of the user is lower during a determination period than during a comparison period set before the determination period when the frequency of days when a movement amount ratio falls below a predetermined ratio among days constituting the determination period is higher than that among days constituting the comparison period, the movement amount 
  - [paper sim=0.685] s2:bb33f02a3a6cf85bdd3c272ab557490a2877c04d | Determinants of older adults' central bank digital currency use behaviour in Nigeria: implications for inclusive and sustainable finance | 
    The study aimed to extend the Unified Theory of Acceptance and Use of Technology (UTAUT) to identify the determinants of Central Bank Digital Currency (CBDC) use behaviour among older adults by introducing components of self-transcendence and conservation values from the theory of basic human value. The moderating effect of Security value and the mediating effects of intention were also examined. Quantitative data were collected from 310 older adults in Southwestern Nigeria. The data were analyzed using partial least squares structural equation modelling (PLS-SEM). Performance expectancy was the most significant determinant of CBDC use behaviour. Behavioural intention mediated the relationsh
  - [patent sim=0.682] patent:US11219404B2 | Cognitive decline detection system | PANASONIC INTELLECTUAL PROPERTY MANAGEMENT CO., LTD.
    Cognitive decline detection system includes obtainment unit and determination unit. Obtainment unit obtains the amount of movement during a sleep period and the amount of movement during a non-sleep period of a user for each day, the non-sleep period being the period other than the sleep period. Determination unit determines that the cognitive function of the user is lower during a determination period than during a comparison period set before the determination period when the frequency of days when a movement amount ratio falls below a predetermined ratio among days constituting the determination period is higher than that among days constituting the comparison period, the movement amount 

### A2a-15  (A2a)  Identity-age inconsistency for synthetic ID detection
Problem: Synthetic identities combine real SSNs with fake details.
Mechanism: Compare age of digital footprint (email, phone, device history) with claimed age and credit-file depth; inconsistency score flags synthetic identity.
Claim core: 
Closest prior art found:
  - [patent sim=0.732] patent:US20200084239A1 | Auto-generated Synthetic Identities for Simulating Population Dynamics to Detect Fraudulent Activity | Capital One Services, LLC
    Embodiments disclosed herein generally relate to a system and method for detecting fraudulent computer activity. A computing system generates a plurality of synthetic identities. Each of the plurality of synthetic identities mimics information associated with a verified identity. The computing system receives, from a user, an input attempt. The input attempt includes a synthetic identity of the plurality of synthetic identities. The computing system compares input information in the input attempt to the plurality of synthetic identities. The computing system determines that the input information in the input attempt includes information from the plurality of synthetic identities, if it does,
  - [patent sim=0.730] patent:US11470116B2 | Auto-generated synthetic identities for simulating population dynamics to detect fraudulent activity | Capital One Services, LLC
    Embodiments disclosed herein generally relate to a system and method for detecting fraudulent computer activity. A computing system generates a plurality of synthetic identities. Each of the plurality of synthetic identities mimics information associated with a verified identity. The computing system receives, from a user, an input attempt. The input attempt includes a synthetic identity of the plurality of synthetic identities. The computing system compares input information in the input attempt to the plurality of synthetic identities. The computing system determines that the input information in the input attempt includes information from the plurality of synthetic identities, if it does,
  - [patent sim=0.730] patent:US20190281086A1 | Auto-generated Synthetic Identities for Simulating Population Dynamics to Detect Fraudulent Activity | Capital One Services, LLC
    Embodiments disclosed herein generally relate to a system and method for detecting fraudulent computer activity. A computing system generates a plurality of synthetic identities. Each of the plurality of synthetic identities mimics information associated with a verified identity. The computing system receives, from a user, an input attempt. The input attempt includes a synthetic identity of the plurality of synthetic identities. The computing system compares input information in the input attempt to the plurality of synthetic identities. The computing system determines that the input information in the input attempt includes information from the plurality of synthetic identities, if it does,

### A2a-16  (A2a)  MPC cross-bank payee risk consortium
Problem: Fraud intelligence is siloed across banks.
Mechanism: Secure multi-party computation of payee risk scores across banks without revealing customer data.
Claim core: 
Closest prior art found:
  - [paper sim=0.747] s2:cef96bcb07cae3199b579762fae777fe53152532 | Predictive Machine Learning Models for Detecting Financial Fraud and Credit Risk Across Digital Banking Platforms | 
    The rapid expansion of digital banking has transformed financial service delivery through mobile applications, online banking, instant payments, digital lending, and API-driven financial ecosystems. However, increased transaction volumes, interconnected platforms, and evolving customer behaviours have intensified exposure to financial fraud and credit risk, challenging conventional rule-based monitoring and static credit-scoring approaches. This study presents a predictive machine learning framework for detecting fraudulent activities and assessing credit risk across digital banking platforms. The framework integrates transactional, behavioural, demographic, account, device, and credit-histo
  - [paper sim=0.742] doi:10.71443/9789349552463-17 | Financial Fraud Prevention and Online Payment Analytics Using Machine Learning | 
    The accelerating expansion of digital payment ecosystems has intensified exposure to sophisticated financial fraud schemes, creating substantial economic losses and systemic risk across global financial infrastructures. Rapid growth in e-commerce, mobile banking, peer-to-peer transfers, and real-time payment platforms has expanded transactional complexity, data volume, and attack surfaces exploited by adversarial actors. Conventional rule-based detection mechanisms lack adaptability against evolving fraud strategies, necessitating intelligent, data-driven solutions capable of real-time risk assessment and predictive accuracy. This chapter presents a comprehensive analytical framework for fin
  - [patent sim=0.734] patent:US20260094206A1 | Apparatus and method for federated tracking of fraudulent activity | Pascal; Sebastian, Pascal; Marie France
    An apparatus and method for federated fraud risk management. Signals from multiple entities engaged in financial, transactional, or compliance data exchange are securely ingested, normalized, and enriched with external and internal data. A scoring module employs one or more analytical techniques, such as statistical methods or neural and non neural models, to compute one or more risk scores across multiple operational, transactional, or identity linked dimensions. A decision component generates and transmits alerts to authorized systems and may route, hold, or escalate operations based at least in part on the computed score. The apparatus and method support privacy preserving collaborative t

### A2a-17  (A2a)  Counterfactual adverse-action notices
Problem: Credit denials must be explained (ECOA/Reg B).
Mechanism: Generate actionable counterfactual explanations with guaranteed feasibility constraints.
Claim core: 
Closest prior art found:
  - [paper sim=0.720] arxiv:2108.00783 | CARLA: A Python Library to Benchmark Algorithmic Recourse and Counterfactual Explanation Algorithms | 
    
  - [paper sim=0.702] arxiv:2107.02776 | Counterfactual Explanations in Sequential Decision Making Under Uncertainty | 
    
  - [paper sim=0.699] arxiv:2604.19755 | Explainable AML Triage with LLMs: Evidence Retrieval and Counterfactual Checks | 
    Anti-money laundering (AML) transaction monitoring generates large volumes of alerts that must be rapidly triaged by investigators under strict audit and governance constraints. While large language models (LLMs) can summarize heterogeneous evidence and draft rationales, unconstrained generation is risky in regulated workflows due to hallucinations, weak provenance, and explanations that are not faithful to the underlying decision. We propose an explainable AML triage framework that treats triage as an evidence-constrained decision process. Our method combines (i) retrieval-augmented evidence bundling from policy/typology guidance, customer context, alert triggers, and transaction subgraphs,

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

Write the answer to: runs/2026-09-30/llm_responses/judge_004.json
