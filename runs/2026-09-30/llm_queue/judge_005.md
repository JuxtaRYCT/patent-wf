# TASK judge_005

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A2a-18  (A2a)  Event-aware ATM cash forecasting
Problem: ATM cash-outs and idle cash.
Mechanism: Forecast using local event calendars and weather.
Claim core: 
Closest prior art found:
  - [patent sim=0.689] patent:US20150081483A1 | INTRADAY CASH FLOW OPTIMIZATION | International Business Machines Corporation
    Embodiments relate to intraday cash flow optimization. Transactions are accessed on a business-to-business integration network from a plurality of sources linked with payment delivery system data from a financial service system. The transactions are associated with two or more compartmentalized entities. The transactions are characterizes based on the payment delivery system data and an analysis of customer profile data. The transactions associated with two or more compartmentalized entities are linked as integrated information based on the characterizing of the transactions. An intraday receivables prediction engine and an intraday payables prediction engine are applied to the integrated in
  - [patent sim=0.683] patent:US20150081491A1 | INTRADAY CASH FLOW OPTIMIZATION | International Business Machines Corporation
    Embodiments relate to intraday cash flow optimization. Transactions are accessed on a business-to-business integration network from a plurality of sources linked with payment delivery system data from a financial service system. The transactions are associated with two or more compartmentalized entities. The transactions are characterizes based on the payment delivery system data and an analysis of customer profile data. The transactions associated with two or more compartmentalized entities are linked as integrated information based on the characterizing of the transactions. An intraday receivables prediction engine and an intraday payables prediction engine are applied to the integrated in
  - [patent sim=0.676] patent:US20240221023A1 | SYSTEMS AND METHODS FOR LINKING ATM TO RETAILER TRANSACTION TO PRESERVE ANONYMITY | Wells Fargo Bank, N.A.
    A method for providing cash back to a customer from a linked automated teller machine (ATM) after a purchase transaction. The method includes receiving, by a provider computing system associated with a provider, a cash back request including a cash back amount from a point-of-sale computing system associated with the purchase transaction, the provider computing system acting as an intermediary computing system between the point-of-sale computing system and a linked ATM associated with the provider; in response to receiving the cash back request, transmitting, by the provider computing system, cash back information to the linked ATM, the cash back information including the cash back amount an

### A2a-19  (A2a)  Dispute escrow window for instant payments
Problem: Instant account-to-account payments are irrevocable, fuelling scams.
Mechanism: Optional escrow window where funds are credited but locked, releasable early by payer confirmation or reversed by dispute.
Claim core: 
Closest prior art found:
  - [paper sim=0.677] doi:10.2139/ssrn.7213458 | The Instant Payment Gap: Reforming the EFTA for Authorized Push Payment Fraud | 
    &lt;p&gt;&lt;span&gt;Instant payment systems have transformed consumer finance—but U.S. law has not kept pace. The Electronic Fund Transfer Act (“EFTA”) provides robust protection against unauthorized transactions, yet leaves consumers without a federal statutory right to reimbursement for authorized push payment (“APP”) fraud, in which deception induces consumers to initiate transfers themselves. This gap has two dimensions. The first is doctrinal: APP fraud falls outside the EFTA’s unauthorized transfer framework. The second is practical: the near-immediate finality of instant payments makes recovery difficult even where legal rights formally exist. Together, these features expose consumer
  - [patent sim=0.673] patent:US20210174348A1 | ELECTRONIC ESCROW SYSTEM | LeBlanc; Gina
    The invention relates to an escrow system that can be between any number of parties to sell and purchase goods or services or online downloads. The system utilizes secure one-time passwords to verify that all parties have completed the terms of the contract.
CLAIM 1: A method of managing an escrow transaction with regards to a two-party sale contract, the method comprising: a. creating the escrow transaction in at least one sending account, the escrow transaction having at least one term and at least one payment related to said sale contract and said sale contract value having a value in escrow monies; b. adding at least one receiving account to the at least one sending account to the sale c
  - [patent sim=0.668] patent:US11100482B2 | Visible and accessible escrow systems and methods | Capital One Services, LLC
    Disclosed herein are systems and methods for processing financial instruments in ATMs or other processing devices. A user can deposit financial instruments, such as cash or a check, into the ATM, to be processed to determine the monetary value of the financial instruments. Once counted and valued, the financial instruments can be dropped into an escrow chamber. The escrow chamber can have a door or gate such that the financial instruments are visible, but not accessible during the transaction. If the customer discovers an error during the transaction, the door or gate can transition to an open state allowing the customer to retrieve the financial instruments.
CLAIM 1: A financial instrument 

### A2a-20  (A2a)  Bank-backed metering tokens for AI API micro-payments
Problem: AI agents need to pay per API call.
Mechanism: Prepaid bank-issued metering tokens redeemed per call with batched settlement.
Claim core: 
Closest prior art found:
  - [patent sim=0.706] patent:US20260134420A1 | AI AGENT TOOLKIT ENABLING LLMS FOR FINANCIAL TRANSACTIONS AND AUTONOMOUS AGENT SERVICES THROUGH BLOCKCHAIN TECHNOLOGY | Pappas; Derek Edwin
    Systems and methods for a transaction. Including sending a request for a service from a consumer agent to a producer agent, wherein the consumer agent and the producer agent are agents of one or more of Artificial Intelligence (AI) agents, finite state machine controlled agents, and/or graph based controller agents. Further including receiving a quote from the producer agent for completing the service. Further including providing a digital signature from the consumer agent for a digital contract, wherein the digital contract comprises terms for fulfilling the service and stipulates a payment method for the service, wherein the digital contract is signed by the producer agent. Further includi
  - [patent sim=0.702] patent:US20260268396A1 | AI and Smart Contract-Based Autonomous Banking System | BEI; FURONG
    This invention describes a novel AI-driven autonomous banking and asset tokenization system that integrates blockchain, smart contracts, decentralized governance, and cross-chain interoperability. The system autonomously tokenizes assets, fractionalizes them into NFTs, manages collateralized loans, performs real-time risk assessments, and ensures regulatory compliance using artificial intelligence without continuous human intervention. Through dynamic AI modeling, multi-signature security, and decentralized decision-making, the invention enables secure, transparent, and efficient financial and asset operations across heterogeneous blockchain networks.
CLAIM 1: An autonomous banking system co
  - [paper sim=0.689] s2:5321198f9c6ce42e0aaaf4250200dde78b46fbde | BLOCKCHAIN IN THE AGENT ECONOMY: IDENTITY, AUTHORIZATION, AND MACHINE-TO-MACHINE SETTLEMENT | 
    Autonomous AI agents increasingly conduct economic transactions on behalf of individuals and organizations. This paper examines which payment architecture is most suitable for such transactions. Using a conceptual research design grounded in transaction cost economics, it separates agent based payments into three functions: identity, authorization, and settlement. It then compares delegated fiat, managed on chain, and native on chain architectures. The analysis shows that identity and authorization do not inherently require blockchain technology. Its distinctive contribution lies in enabling settlement through a shared ledger that is not controlled by a single institution. This feature is mo

### A2a-21  (A2a)  Biometric-bound offline CBDC wallet
Problem: Offline CBDC risks double spending.
Mechanism: Secure-element monotonic counters and biometric binding; reconciliation on reconnection detects double spend.
Claim core: 
Closest prior art found:
  - [paper sim=0.792] arxiv:2512.10636 | Objectives and Design Principles in Offline Payments with Central Bank Digital Currency (CBDC) | 
    
  - [paper sim=0.792] arxiv:2512.10636 | Objectives and Design Principles in Offline Payments with Central Bank Digital Currency (CBDC) | 
    
  - [paper sim=0.763] arxiv:2509.25469 | Balancing Compliance and Privacy in Offline CBDC Transactions Using a Secure Element-based System | 
    

### A2a-22  (A2a)  Life-event-triggered KYC refresh
Problem: Periodic KYC refresh is wasteful.
Mechanism: Infer life events from transactions and refresh KYC only when risk-relevant events occur.
Claim core: 
Closest prior art found:
  - [patent sim=0.652] patent:US20190370367A1 | OPTIMIZING DATA REFRESH TIMING BASED ON TELEMETRY | MICROSOFT TECHNOLOGY LICENSING, LLC
    Methods, computer systems, computer-storage media, and graphical user interfaces are provided for facilitating enhancement of data refresh timing. In one embodiment, user data indicating a user pattern for accessing a dataset is obtained. A data refresh duration indicating a duration of time used to perform data refreshes can be identified. Using the user data and the data refresh duration, a future time at which to perform a data refresh is determined. Generally, the future time is predicted to enable the data refresh to occur prior to a user accessing the dataset. Thereafter, a data refresh can be automatically initiated at the determined future time.
CLAIM 1: A computing system comprising
  - [patent sim=0.652] patent:US20260212336A1 | SYSTEMS AND METHODS FOR AUTONOMOUSLY TRANSITIONING RECURRING AUTOPAYMENT EVENTS BETWEEN PAYMENT ACCOUNTS | Wells Fargo Bank, N.A.
    Systems, apparatuses, methods, and computer program products are disclosed for providing overdraft protection during transitions between payment accounts. An example method includes identifying a set of historical transactions associated with a legacy payment account of a user and deriving a set of recurring autopayment events from the set of historical transactions. The example method further includes executing a proactive protection protocol. The proactive protection protocol includes analyzing a new payment account, evaluating whether a deadline associated with the unscheduled recurring autopayment event falls within a predefined threshold time period, assessing whether the legacy payment
  - [patent sim=0.651] patent:US20260187612A1 | AUTOMATED EVENT TRACKING AND CONDITIONAL ASSET TRANSFER | Block, Inc.
    Systems and methods for conditional asset transfers based on outcomes of events are provided. An event-based transfer system stores a record for a conditional asset transfer based on an outcome of an event based on a corresponding request. The system monitors information sources and/or feeds (e.g., of sensors, news sources, social media, etc.) to monitor and/or track the status of the event. The system determines when the outcome of the event becomes settled, and determines, based on the record, a direction of the conditional asset transfer based on the settled outcome of the event. The system automatically alerts user device(s) of user(s) participating in the transfer, and automatically fac

### A2a-23  (A2a)  RL-driven financial wellness nudges
Problem: Generic savings nudges are ignored.
Mechanism: Reinforcement learning chooses nudge timing and framing per user.
Claim core: 
Closest prior art found:
  - [paper sim=0.702] arxiv:2609.32772 | Learnable Randomization as Commitment Against Adaptive Optimizers | 
    A pricing page can walk the posted price up to the last amount a buyer still accepts, a recommender can hold back a better item for a barely acceptable promoted one, and a classifier can shift its boundary once applicants change their features. The system predicts the response and then picks the menu that serves its own objective, so the surplus above the user's cutoff is taken. Playing the single best action publishes that cutoff, while noise on actions the user would never take throws away payoff and teaches the platform that a worse menu is still acceptable. We study unpredictable near-optimal policies (UNOP), which mix uniformly on near-best actions that remain individually rational. The
  - [paper sim=0.701] arxiv:2609.02014 | Insights on Time-consistent Deep Hedging under Elicitable Dynamic Risk Measures | 
    We study deep hedging in the context of dynamics risk measures, where sequential decisions are time-consistent. Whereas the literature in such context mainly considers low-dimensional problems with simple environment dynamics, we tackle the high-dimensional problem of basket option hedging; we show that the approach is feasible and can be used conveniently in the presence of more complex state spaces. We rely on the conditional elicitability of spectral risk measures to represent the optimization objective. We provide insights on how the choice of scoring function impacts the training of the hedging agent. Lastly, the time-consistent hedging strategies are benchmark against deep hedging appr
  - [paper sim=0.700] s2:0564c241a546e9f0d16ea2409d5fb277ad62587c | Adaptive UI/UX Using Reinforcement Learning in Banking Apps: A Comprehensive Research Framework | 
    A complete reinforcement learning (RL) research methodology for adaptive UI/UX in banking applications is presented in this study. The proposed system includes user demographics, contextual factors, behavioural history, current session data, and financial profiles in its rich state space and an extensive action space for UI adaptations like layout, navigation, feature prominence, interaction patterns, and notification strategies. A multi-objective reward function balances job completion, efficiency, error reduction, engagement, and business value. Implementation uses a modified Deep QNetwork (DQN) with Double DQN, duelling architecture, prioritised experience replay, and noisy networks, back

### A2a-24  (A2a)  Cross-script transliteration graph for sanctions screening
Problem: Name transliteration defeats sanctions screening.
Mechanism: Graph of transliteration variants across scripts used for fuzzy matching.
Claim core: 
Closest prior art found:
  - [patent sim=0.665] patent:US12706905B2 | Reducing false positives in entity matching based on image-linking graphs | PayPal, Inc.
    Methods and systems are presented for performing comprehensive and accurate matching of user accounts with one or more known entities based on image-linking graphs. Images related to each known entity are retrieved from one or more online sources. Faces are extracted from the images. Based on attributes of the faces in the images, an image-linking graph is generated for the entity. When a user account is determined to be a potential match for the entity based on text-based attributes, an image associated with the account may be obtained. If the image matches with any one of the faces in the image-linking graph, an action is performed to the user account based on a position of the matched fac
  - [paper sim=0.663] arxiv:2606.24897 | Invisible to humans, visible to machines: a preregistered audit of Unicode fidelity across four biomedical bibliographic APIs | 
    Biomedical text mining, scientometrics, and the construction of training corpora for biomedical large language models (LLMs) all assume that the abstract text returned by a bibliographic API faithfully reproduces the published abstract. This pre-registered audit (OSF osf.io/269b5) tests that assumption for four widely used public APIs (PubMed E-utilities, Crossref, OpenAlex, Semantic Scholar) against PubMed Central (PMC) JATS XML as a common ground truth. From a complete enumeration of the PMC Open Access subset for 2024 (about 700,000 records), a simple random sample of 4,000 English-language research articles was drawn; for each, we recorded whether Unicode characters from four pre-specifi
  - [patent sim=0.636] patent:US20250378488A1 | SYSTEM AND METHOD FOR TRADE FINANCE OPERATIONS AND SANCTIONS SCREENING PROCESS | George; Mariya, Somasekhar; Chandrasekhar, Sasikumar; Sarath
    The present invention discloses a system and method for processing trade finance documents and performing automated compliance screening. The system comprises a computing device, and a database for storing trade finance documents. The system processes documents using OCR to extract text and positional data, generating structured document representations via a layout-aware AI model. An AI classifier module categorizes documents based on content, layout, and domain-specific roles, while a semantic verification module aligns document data with master Letter of Credit templates. A rule management module validates compliance against international trade standards, and a financial crime risk contro

### A2a-25  (A2a)  Satellite collateral monitoring for loan covenants
Problem: Collateral monitoring is manual.
Mechanism: Satellite imagery change detection on pledged farms/factories.
Claim core: 
Closest prior art found:
  - [patent sim=0.737] patent:US7707102B2 | Method and apparatus for monitoring the collateral risk analysis commodity lenders | 
    The risk of loss in individual collateral loans may be evaluated by taking into consideration the market supply and demand for the collateral/asset, as well as the amount of the loan balance in proportion to the value of the collateral. A Collateral Risk Index is determined using information regarding the total number of sales of the collateral/asset, the total number of pending listings, the total number of active listings, and the total number of expired listings in a time period. This information is used in conjunction with the loan balance versus the collateral/asset value to determine an index reflective of the risk of loss to the lender or investor.
CLAIM 1: A method of determining a c
  - [patent sim=0.714] patent:US12711544B1 | Systems and methods for communications regarding loan collateral | Federal Home Loan Mortgage Corporation
    Systems, methods, and non-transitory computer-readable storage media are provided. A central server receives collateral data and applies a set of collateral analysis rules thereto to identify a problem. The applying includes accessing, from a data source, supplemental data related to the collateral data, and detecting one or more differences exceeding discrepancy tolerances between the collateral data and the supplemental data. The central server generates a notification and a navigation link to access information from a source of problem information related to the collateral data. The central server transmits the notification to a computing device based upon a destination address. The notif
  - [patent sim=0.696] patent:US20130006844A1 | SYSTEMS AND METHODS FOR COLLATERALIZING LOANS | Sociogramics, Inc.
    Systems and methods are disclosed for collateralizing loans. Some embodiments increase the likelihood of repayment by obtaining access to a qualified attribute of a borrower by a first computer component, monitoring by a second computer component for a financial event associated with the loan to the borrower, and taking control of the qualified attribute of the borrower by a third computer component. Taking control may include notifying social contacts. Securing the loan by taking various security interests and technical countermeasures against the borrower re-obtaining access or re-taking control are disclosed. Providing loans, receiving loan applications, providing loans proceeds, processi

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

Write the answer to: runs/2026-09-30/llm_responses/judge_005.json
