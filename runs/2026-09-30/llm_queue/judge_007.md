# TASK judge_007

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A2b-04  (A2b)  Taint-granular freezing for payment stablecoins: encumbering only the traced sanctioned value rather than whole addresses, with court-signed release
Problem: Issuers must be able to freeze and seize, and must meet BSA/sanctions standards. Address-level blacklists freeze innocent downstream holders and push commerce away from stablecoins.
Mechanism: The token contract tracks value lineage with a configurable taint policy (FIFO or haircut) over transfers. When the issuer receives a sanctions or court order for identified inflows, the contract places an encumbrance equal to the traced tainted amount on each current holder, blocking only that amount. It emits verifiable lineage proofs, so the holder can transact their untainted balance normally. Release or seizure requires a threshold signature from the issuer compliance key and a court or agency key. Holders can submit a counter-proof, such as a purchase from a licensed exchange before the listing date, to contest.
Claim core: A token ledger maintaining per-holder lineage records of value derived from flagged inflows under a taint policy, applying partial encumbrances equal to traced amounts upon a signed order, permitting transfers of unencumbered balance, and releasing encumbrances upon threshold signatures.
Closest prior art found:
  - [paper sim=0.760] arxiv:2602.17842 | StableAML: Machine Learning for Behavioral Wallet Detection in Stablecoin Anti-Money Laundering on Ethereum | 
    Global illicit fund flows exceed an estimated $3.1 trillion annually, with stablecoins emerging as a preferred laundering medium due to their liquidity. While decentralized protocols increasingly adopt zero-knowledge proofs to obfuscate transaction graphs, centralized stablecoins remain critical transparent choke points for compliance. Leveraging this persistent visibility, this study analyzes an Ethereum dataset to establish an empirical baseline for behavioral AML detection. Our findings demonstrate that domain-informed tree ensemble models achieve higher Macro-F1 score, significantly outperforming graph neural networks, which struggle with the increasing fragmentation of transaction netwo
  - [paper sim=0.728] arxiv:2608.09378 | Scaling laws of Stablecoin Transactions: Evidence from USDT and USDC on the Ethereum blockchain | 
    Stablecoins have rapidly emerged as an important class of digital assets and a component of the digital financial ecosystem. Despite their growing importance, the statistical properties of stablecoin transaction activity remain largely unexplored. To the best of our knowledge, this is the first study to investigate scaling behavior in stablecoin transaction data, focusing on USDT and USDC. We analyze approximately 370 million USDT and USDC transactions recorded on the Ethereum blockchain across six periods spanning June 2024 to February 2026. Based on interactions between Externally Owned Accounts (EOAs) and Smart Contracts (SCs), we classify transactions into four categories: EOA-EOA, EOA-S
  - [paper sim=0.726] arxiv:2608.25600 | Defending the Peg: Real-Time Dynamic Protection and Anomaly Detection in DeFi Stablecoins | 
    With the rapid evolution of the Decentralized Finance (DeFi) ecosystem, stablecoins have emerged as a critical infrastructure bridging the cryptocurrency market with traditional financial paradigms. However, stablecoin systems rely heavily on smart contracts to execute automated operations. The immutable nature of these systems post-deployment means that the exploitation of security vulnerabilities can lead to irreversible, massive economic losses and potentially trigger systemic financial risks. Current research on stablecoin smart contract security faces challenges such as a lack of domain-specific targeting and the obsolescence of static defense models. To address this, this paper systema

### A2b-05  (A2b)  Provable-fairness redemption queue for stablecoins under stress (2-business-day par redemption)
Problem: The GENIUS Act requires timely redemption at par. Under a run, how the redemption queue is ordered becomes contentious, and a first-mover advantage accelerates the run itself.
Mechanism: Redemption requests are committed on-chain with a timestamp and randomness beacon. The issuer processes them in batches whose ordering rule is fixed in advance (pro-rata within time buckets, with small-holder priority up to a cap) and publishes a Merkle proof of each batch's allocation. Holders can verify their queue position and expected settlement time. Because the ordering rule removes the benefit of redeeming seconds earlier inside a bucket, it damps panic dynamics.
Claim core: A method comprising committing redemption requests with timestamps, grouping them into time buckets, allocating available liquidity within each bucket by a pre-committed rule, and publishing proofs of allocation verifiable by each requester.
Closest prior art found:
  - [paper sim=0.715] s2:b1b6aed5f7486f588a4b92869d9a812f27e03ce3 | Stablecoins and the Upcoming Battle for Depositors | 
    We lay out the research questions raised by the GENIUS Act of 2025 which creates a federal framework in the United States for payment stablecoins that may compete for balances with bank deposits. We first set out the motivating facts: what stablecoins are used for, what the Act does and leaves open, why a bank deposit is one leg of a bundle rather than a standalone product, and what happened when a previous innovation, namely money market funds, competed for deposits. These facts pose three policy questions relating to payment stablecoins and their issuers— payment of interest or rewards; access to Federal Reserve settlement systems; and obtaining national trust bank charters— and two analyt
  - [paper sim=0.703] arxiv:2609.15373 | Resolution Is Not Settlement, Part II: Protocol Finality and Observed Redemption on Polymarket | 
    An Oracle result is not yet a protocol payout, a redeemable position is not yet collateral in a holder's account, and a redemption event is not a complete measure of economic entitlement. This companion paper develops an event-sourced framework for Polymarket conditions from preparation through protocol finality and observed holder realization. The empirical design uses three Conditional Tokens Framework event families derived from a pinned contract application binary interface (ABI): ConditionPreparation, ConditionResolution, and PayoutRedemption. It separates the contract-wide acquisition universe from the frozen Polymarket adapter-question cohort. The exact bridge contains 108,638 linked 
  - [paper sim=0.698] s2:e18086e4e4cf2a163ecfe6b2bbf831ac811f7237 | Banks in the Age of Stablecoins: Some Possible Implications for Deposits, Credit, and Financial Intermediation | 
    The rapid growth of stablecoins, accelerated by regulatory frameworks like the Genius Act, has raised important questions about their impact on traditional banking. As these digital tokens gain mainstream acceptance, they could fundamentally reshape the structure and functions of banking and influence the established intermediation role of banks.

### A2b-06  (A2b)  Signed tradeline provenance: turning credit-report dispute investigations into cryptographic record comparison with automatic correction on SLA miss
Problem: Credit-reporting disputes are overwhelmed. 'Investigation took more than 30 days' reached 238k complaints in 120 days, growing 1.41× in share, and 207k say the investigation did not fix the error. Investigations are code exchanges (e-OSCAR) with no record of source-of-truth.
Mechanism: Each tradeline field a furnisher reports (balance, status, dates, payment history) carries a signed provenance envelope: a hash of the source-system record, the furnisher key, a timestamp and a version. When a consumer disputes a field, the bureau automatically requests the furnisher's signed source record for that version. If the furnisher returns a record whose hash matches and whose content supports the reported value, the dispute is resolved with an evidentiary receipt to the consumer. If it cannot produce a matching signed record within the SLA, the field is suppressed automatically, not merely 'verified'. Mismatches between the reported value and the signed source trigger correction. Status is pushed to the consumer at each step.
Claim core: A method comprising: receiving tradeline data fields each associated with a signed provenance record of a source-system record; upon a dispute of a field, requesting a signed source record from the furnisher; comparing the source record against the reported field and provenance hash; and correcting or suppressing the field automatically upon mismatch or non-response within a time limit.
Closest prior art found:
  - [patent sim=0.749] patent:US11276115B1 | Tradeline fingerprint | AMERICAN EXPRESS TRAVEL RELATED SERVICES COMPANY, INC.
    Improved systems and methods are provided for identifying financial relationships. In particular, financial relationships may be identified by associating tradelines with one or more people who sign or co-sign on the tradeline. In various embodiments a method is provided comprising, receiving, at a computer-based system for credit data analysis comprising a processor and a tangible, non-transitory memory, credit reporting data relating to a tradeline, parsing, by the computer-based system, the credit reporting data to yield primary debtor data and secondary debtor data, and linking, by the computer-based system, the tradeline with the primary debtor data and the secondary debtor data.
CLAIM 
  - [patent sim=0.741] patent:US10497055B2 | Tradeline fingerprint | American Express Travel Related Services Company, Inc.
    Improved systems and methods are provided for identifying financial relationships. In particular, financial relationships may be identified by associating tradelines with one or more people who sign or co-sign on the tradeline. In various embodiments a method is provided comprising, receiving, at a computer-based system for credit data analysis comprising a processor and a tangible, non-transitory memory, credit reporting data relating to a tradeline, parsing, by the computer-based system, the credit reporting data to yield primary debtor data and secondary debtor data, and linking, by the computer-based system, the tradeline with the primary debtor data and the secondary debtor data.
CLAIM 
  - [patent sim=0.741] patent:US20170011458A1 | TRADELINE FINGERPRINT | American Express Travel Related Services Company, Inc.
    Improved systems and methods are provided for identifying financial relationships. In particular, financial relationships may be identified by associating tradelines with one or more people who sign or co-sign on the tradeline. In various embodiments a method is provided comprising, receiving, at a computer-based system for credit data analysis comprising a processor and a tangible, non-transitory memory, credit reporting data relating to a tradeline, parsing, by the computer-based system, the credit reporting data to yield primary debtor data and secondary debtor data, and linking, by the computer-based system, the tradeline with the primary debtor data and the secondary debtor data.
CLAIM 

### A2b-07  (A2b)  Mixed-file splitting with consumer-held verifiable credentials for 'information belongs to someone else' disputes
Problem: 895,197 complaints in 120 days say report information belongs to someone else. Mixed files and synthetic or stolen identities contaminate reports, and bureaus resolve this by fuzzy matching.
Mechanism: A consumer proves identity attributes once, with a device-bound verifiable credential issued by a bank or government ID wallet that includes a stable pseudonymous subject identifier. When disputing, the consumer signs a challenge listing the tradelines they claim. The bureau's entity-resolution engine re-clusters the file under the hard constraint that tradelines explicitly disowned by a VC-authenticated subject cannot co-reside with that subject's identifier. The disowned records are split into a separate candidate entity, which is then matched to other files and flagged for identity-theft review. The consumer receives a signed record of the split.
Claim core: A method comprising: receiving from a consumer device a signed disownment of records bound to a verifiable credential; re-executing entity resolution over a credit file with a constraint excluding the disowned records from the consumer's entity; generating a separate entity from the disowned records; and returning a signed confirmation.
Closest prior art found:
  - [patent sim=0.743] patent:US20260222392A1 | CONSUMER-AUTHORIZED CONTROLLED DISTRIBUTION OF TRUSTED SOURCE DATA | TURBOPASS CORPORATION
    Apparatus and associated methods relate to a 3rd Party Asset Verification module (3PAV module) embodied in a computer system configured to: (1) transmit a unique access code to at least one entity, the unique access code (1a) associated with a user and the user's asset information, and (1b) permits access to the user's asset information stored in the controlled access data store, and (2) in response to a request for data from a broadcasted receiver of the unique access code, the request including the unique access code, returning the user's asset information stored in the controlled access data store. In an illustrative example, the unique code may be generated upon the user providing author
  - [patent sim=0.737] patent:US20260291748A1 | ISSUANCE AND VERIFICATION OF MULTI-CLAIM VERIFIABLE CREDENTIALS AND VERIFIABLE PRESENTATIONS | American Express Travel Related Services Company, Inc.
    Disclosed are various approaches for issuing and verifying multi-claim verifiable credentials and verifiable presentations. In various embodiments, an issuer can send a request for information to a holder and obtain a response from the holder. The issuer can extract claims from the message, validate at least one of the claims, and generate a verifiable credential (VC) for the holder based at least in part on the claims, which can be sent to the holder. The holder can then generate a verifiable presentation (VP) based at least in part on the VC and send the VP to a verifier. The verifier can then verify the VP and interpret the claims within the VC.
CLAIM 1: A system, comprising: a computing 
  - [patent sim=0.735] patent:US12732380B2 | Issuance and verification of multi-claim verifiable credentials and verifiable presentations | American Express Travel Related Services Company, Inc.
    Disclosed are various approaches for issuing and verifying multi-claim verifiable credentials and verifiable presentations. In various embodiments, an issuer can send a request for information to a holder and obtain a response from the holder. The issuer can extract claims from the message, validate at least one of the claims, and generate a verifiable credential (VC) for the holder based at least in part on the claims, which can be sent to the holder. The holder can then generate a verifiable presentation (VP) based at least in part on the VC and send the VP to a verifier. The verifier can then verify the VP and interpret the claims within the VC.
CLAIM 1: A system, comprising: a computing 

### A2b-08  (A2b)  Agent-herding detection: flagging scam storefronts by the sudden convergence of many users' AI shopping agents on a new merchant
Problem: Banks warn that AI shopping bots raise scam and fraud risk. Fake storefronts can be tuned to rank highly in agents' retrieval (agent-SEO, or prompt-injection pages), and one fake merchant can capture thousands of agents at once.
Mechanism: The issuer or network tags agent-initiated authorisations (agentic tokens identify agent platform and instance). It maintains a streaming convergence detector: for each merchant, the rate of distinct user-agents newly transacting, normalised by the merchant's age, category and historical human traffic. Humans discover merchants gradually and diversely; agents that share retrieval pipelines converge sharply. When convergence far exceeds the human baseline for a merchant with thin history, especially from agents of one platform, the network places the merchant on agent-hold: human confirmation is required and settlement is delayed. It also notifies the agent platform with the retrieval signals involved.
Claim core: A method comprising: identifying authorisation requests initiated by autonomous agents; computing, per merchant, a rate of distinct agents newly transacting relative to a baseline for human-initiated traffic; and applying a merchant-level restriction on agent-initiated transactions when the rate exceeds a threshold.
Closest prior art found:
  - [paper sim=0.819] s2:9703a43574a0193d6686c04ce4a4f38c00d28ccb | SECURING AGENTIC COMMERCE THROUGH BEHAVIOR-AWARE FRAUD DETECTION AND CYBERSECURITY FOR TRUSTED AI-AGENT PAYMENT AUTHORIZATION | 
    The emergence of autonomous artificial intelligence (AI) agents in digital commerce introduces cybersecurity risks involving delegated authority, agent impersonation, compromised agents, malicious delegation, and unauthorized payment execution. This study proposes the Autonomous Commerce Agent Guard System (ACAGS), a behavior-aware cybersecurity framework integrating supervised machine learning, historical behavioral analysis, agent-specific authorization controls, and explainable AI for payment authorization. ACAGS was evaluated using a large-scale synthetic financial transaction dataset extended with a simulated agentic-commerce layer representing agent identity, delegated spending limits,
  - [paper sim=0.815] arxiv:2609.35886 | Agentic Commerce Bench: Measuring Fraud Detection for Agents That Spend Money | 
    AI agents now hold spend authority and settle payments without per-action human confirmation. The resulting loss is often not a security failure: a counterparty with the correct domain, the correct settlement address and a genuinely delivered service can charge more than it should, and no check keyed on identity will see it. We present three artefacts for measuring and reducing that loss. First, a taxonomy of agentic commerce fraud that separates five observation levels (agent reasoning, wire, settlement rail, counterparty, principal) from the request-level and history-level evidence available at each, and records which levels can observe which attacks. Second, Agentic Commerce Bench (ACB), 
  - [paper sim=0.797] arxiv:2606.17555 | An AI Security Agent for Banking: Multi-Vector Fraud and AML Detection Across Retail and Corporate Accounts | 
    Banks face two threat families with fundamentally different detection requirements: signature-based fraud (card-not-present attacks, account takeover, ATM cloning) and behavioural financial crime (structuring, layering, mule networks, business email compromise). Static rule engines catch high-velocity events but remain blind to BEC payment redirection, session hijacking, and laundering layering, which are engineered to resemble legitimate activity at the individual level. This paper presents an AI security agent for retail and corporate banking using a three-component fusion architecture across two parallel event streams: transactions (card fraud, ACH/wire fraud, AML) and sessions (account t

### A2b-09  (A2b)  Network-run red-team canaries: continuous certification of AI shopping agents against prompt injection using honeypot storefronts
Problem: Issuers cannot inspect agent platforms' robustness, but they carry the fraud liability when agents are manipulated.
Mechanism: The payment network runs synthetic honeypot storefronts and product listings carrying graded prompt-injection payloads, for example hidden instructions to change the shipping address, pay a different merchant, or disclose credentials. Test users' agents of each platform version are routinely directed at them through normal retrieval. Agent behaviour is scored automatically: whether the agent attempted a payment to a canary merchant ID or deviated from the mandate. The resulting robustness score is bound to the agent platform's token-requestor credentials, and issuers scale token scopes and limits to it. A regression immediately narrows scopes network-wide.
Claim core: A system comprising canary merchant endpoints presenting adversarial content, a test orchestrator directing agent instances of registered agent platforms to the endpoints, a scorer detecting payment attempts or mandate deviations toward canary identifiers, and a token service adjusting agent token scopes based on scores.
Closest prior art found:
  - [paper sim=0.840] arxiv:2608.23858 | Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2) | 
    The Agent Payments Protocol (AP2), introduced by Google, enables large language model (LLM)-driven shopping agents to authorize and execute payments on behalf of users. Its signed Checkout and Payment Mandates protect the integrity of transaction data after signing. Agent interactions and external inputs that shape a transaction before authorization remain outside that protection, including Agent-to-Agent Protocol (A2A) messages and Model Context Protocol (MCP) tool calls. Prior work identified replay and prompt-injection attacks in AP2 v0.1. AP2 v0.2 addresses some of these issues but adds capabilities and deployment assumptions that require renewed analysis. We present a systematic securit
  - [paper sim=0.839] arxiv:2607.21824 | Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense | 
    Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users'behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model, through prompt injection and misalignment. We show that the more consequential risks lie one layer down, in the protocol between agents and commerce services. There, vulnerabilities are structural : exploitation is deterministic and ndependent of which model an agent runs, so no model improvement removes them. Across three leading platforms we identify 33 such vulnerabilities, each succeeding deterministically regardless of the deployed 
  - [paper sim=0.821] arxiv:2609.00060 | A Formal Analysis of Agent Payment Protocols | 
    Agent payment protocols are emerging as a key transaction layer for autonomous commerce, enabling AI agents to purchase goods and services and execute payments on users'behalf. Unlike conventional payment flows, they distribute user intent, delegated authority, credential use, settlement, and fulfillment across multiple actors and stages, creating security dependencies that no single message or participant can enforce. Yet these guarantees remain largely implicit across evolving specifications, schemas, and reference implementations, with little systematic formal analysis. We formalize four representative agent payment protocols: x402, MPP, ACP, and AP2 in Tamarin. Using a common abstraction

### A2b-10  (A2b)  Pass-through deposit-insurance ledger for fintech custodial accounts with instant per-owner coverage proofs
Problem: Post-Synapse, the FDIC's custodial-account recordkeeping proposals and the regulatory resets exist because owners of pooled for-benefit-of balances could not be identified or paid quickly after failure.
Mechanism: Each end-user balance held at a sponsor bank through a fintech is recorded in a per-owner pass-through ledger kept at the bank, not only at the fintech. It is updated from signed fintech sub-ledger deltas with Merkle inclusion proofs and reconciled daily. The ledger computes coverage per ownership category and per insured bank in real time. Each owner can obtain a signed coverage proof (insured amount, bank, category). The FDIC receives a machine-readable pass-through file that allows payout on day 1 after failure.
Claim core: A system maintaining, at a depository institution, per-owner balances derived from signed sub-ledger deltas of a third party with inclusion proofs, computing deposit-insurance coverage per owner and category in real time, and issuing signed coverage proofs.
Closest prior art found:
  - [patent sim=0.726] patent:US20230104103A1 | CUSTODIAL SYSTEMS FOR NON-FUNGIBLE TOKENS | American Express Travel Related Services Company, Inc.
    Disclosed are various embodiments for using custodial systems to maintain ownership of digital assets and facilitate transfers of digital assets between individuals. To facilitate a user taking possession of a digital asset, the custodial system could update an owner identifier for a digital asset in an asset ledger to include a public key of an asset custodian, the public key of the asset custodian indicating that the asset custodian is the owner of the digital asset. The custodial system could then provide a verifiable credential to an identity wallet, the verifiable credential being linked to the digital asset in the digital asset ledger. Subsequently, the custodial system could create an
  - [patent sim=0.723] patent:US12340365B2 | Distributed ledger based multi-currency clearing and settlement | PARTIOR PTE. LTD
    A distributed ledger system may include a first distributed ledger node associated with a first participant bank that maintains a first participant bank deposit account on a blockchain-based distributed ledger in a distributed ledger network; a second distributed ledger node associated with a second participant bank that maintains a second participant bank deposit account on the blockchain-based distributed ledger; and a third distributed ledger node associated with a liquidity provider that maintains a liquidity provider deposit account on the blockchain-based distributed ledger. A consensus algorithm operates on the distributed ledger nodes and updates the blockchain-based distributed ledg
  - [patent sim=0.720] patent:US20220374880A1 | DISTRIBUTED LEDGER BASED MULTI-CURRENCY CLEARING AND SETTLEMENT | PARTIOR PTE. LTD
    A distributed ledger system may include a first distributed ledger node associated with a first participant bank that maintains a first participant bank deposit account on a blockchain-based distributed ledger in a distributed ledger network; a second distributed ledger node associated with a second participant bank that maintains a second participant bank deposit account on the blockchain-based distributed ledger; and a third distributed ledger node associated with a liquidity provider that maintains a liquidity provider deposit account on the blockchain-based distributed ledger. A consensus algorithm operates on the distributed ledger nodes and updates the blockchain-based distributed ledg

### A2b-11  (A2b)  Debt chain-of-title ledger with open-banking proof-of-payment matching to stop collection of debts not owed
Problem: 41,086 complaints in 120 days about attempts to collect debt not owed, many where the debt had already been paid. Debts are sold repeatedly with broken documentation.
Mechanism: Every debt assignment is recorded as a hash-linked title record containing the balance, payment history digest and the seller's signature. A collector's system must present a valid chain of title from the original creditor before any collection communication is generated. When a consumer disputes, the consumer app pulls payment evidence from their bank through open-banking APIs and matches it to the creditor account by payment reference, amount and date. It then issues a signed proof-of-payment object that the ledger attaches to the debt, and further collection is blocked automatically.
Claim core: A method comprising: recording debt assignments as hash-linked signed title records; verifying a chain of title prior to generating a collection communication; receiving a consumer-generated proof of payment derived from account data retrieved via an open-banking interface; and blocking collection upon verification of the proof.
Closest prior art found:
  - [patent sim=0.726] patent:US20180268479A1 | INTERNATIONAL TRADE FINANCE BLOCKCHAIN SYSTEM | Wells Fargo Bank, N.A.
    A method includes generating a blockchain-based letter of credit (“BLC”) relating to a contract for a trade transaction between a seller and a buyer. The BLC defines documentary and supply chain flow payment trigger events. The BLC is stored and accessible via a blockchain. A plurality of documentary flow events related to the BLC are tracked and recorded on the blockchain, and are linked to the BLC. A plurality of supply chain flow events related to a physical status of a good involved in the trade transaction are tracked and recorded on the blockchain. Each of the plurality of supply chain flow events are linked to the BLC. Payment for the contract for the trade transaction is transferred 
  - [patent sim=0.714] patent:US20160328791A1 | SYSTEM AND METHOD FOR ELECTRONIC CONSUMER DEBT VALIDATION AND DISPUTE PROCESS | GDR ACQUISITION COMPANY LLC
    A system and method for universal electronic consumer debt validation and dispute resolution permits consumers to access debt information and download related documents related to debt accounts for any type of debt. Moreover, debt owners or agencies may make available debt information for a consumer in a single repository so that a consumer may search and/or evaluate and download the information and initiate resolution of the debt as may be warranted.
CLAIM 1: A system for debt validation and dispute, comprising: a server comprising a computer and a consumer access subsystem and a debt validation subsystem; a database to store debt account information searchable and identifiable by a plurali
  - [patent sim=0.712] patent:US20260187264A1 | SYSTEMS AND METHODS FOR VERIFYING DATA VIA BLOCKCHAIN | STATE FARM MUTUAL AUTOMOBILE INSURANCE COMPANY
    Methods and systems for processing a blockchain comprising a plurality of immutable sales records corresponding to sales made by agents of an entity are provided. According to certain aspects, a transaction request indicating a sale made by an agent of the entity may be received at a first node. A block including a sales record indicating the sale made by the agent may be added to a blockchain and transmitted to another node for validation. The first node may add the block to a copy of the blockchain, where the block may be identified by a hash value that references a previous block in the blockchain that includes at least one additional sales record.
CLAIM 1: A computer-implemented method o

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

Write the answer to: runs/2026-09-30/llm_responses/judge_007.json
