# TASK judge_006

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A2a-26  (A2a)  Cross-retailer return-fraud linkage
Problem: Serial return fraud spans retailers.
Mechanism: Card-network level linking of refunds across merchants.
Claim core: 
Closest prior art found:
  - [patent sim=0.723] patent:US20240221023A1 | SYSTEMS AND METHODS FOR LINKING ATM TO RETAILER TRANSACTION TO PRESERVE ANONYMITY | Wells Fargo Bank, N.A.
    A method for providing cash back to a customer from a linked automated teller machine (ATM) after a purchase transaction. The method includes receiving, by a provider computing system associated with a provider, a cash back request including a cash back amount from a point-of-sale computing system associated with the purchase transaction, the provider computing system acting as an intermediary computing system between the point-of-sale computing system and a linked ATM associated with the provider; in response to receiving the cash back request, transmitting, by the provider computing system, cash back information to the linked ATM, the cash back information including the cash back amount an
  - [patent sim=0.715] patent:US12657589B1 | Identity linkage systems and methods for fraud detection | Experian Information Solutions, Inc.
    Embodiments are disclosed of a system for detecting potential online transaction fraud. The system can receive transaction data associated with an online transaction. In some embodiments, the system can determine consumer identification data and payment instrument data from the transaction data. The system can compare the consumer identification data and the payment instrument data associated with the online transaction against consumer profiles generated based on existing consumer information and payment instrument information. Based on the comparison, the system can generate a match score indicative of a likelihood that the online transaction is fraudulent.
CLAIM 1: A system for online tra
  - [patent sim=0.698] patent:US12743697B2 | Implementing fraud controls on a hybrid network | MASTERCARD INTERNATIONAL INCORPORATED
    A computer implemented method of assessing the probability of fraudulent activity in an account to account payment is provided. The method comprises determining, based on previous credit balance settlement transactions between a first account and a card settlement account, that a first set of payment credentials is associated with the first account. It is determined that a second set of payment credentials are associated with the merchant account. A database comprising historical data indicating details of past payment transactions between the holder of the first set of payment credentials to the holder of the second set of payment credentials is accessed. A fraud probability engine is used 

### A2a-27  (A2a)  Telco SIM-swap signals for ATO
Problem: SIM swap enables account takeover.
Mechanism: Query telco network APIs for recent SIM swap before OTP delivery.
Claim core: 
Closest prior art found:
  - [patent sim=0.695] patent:US10178223B1 | Fraudulent subscriber identity module (SIM) swap detection | Symantec Corporation
    Detecting a fraudulent subscriber identity module (SIM) swap may be performed by a mobile app executing on a mobile computing device. A network connectivity state is determined for the mobile computing device to a mobile telephony network provided by a mobile network operator. The mobile computing device is associated with a SIM which is associated with the mobile network operator. A signal strength is determined at the mobile computing device of the mobile telephony network provided by the mobile network operator. A likelihood is determined that a SIM swap has taken place involving the SIM based on the signal strength and the network connectivity state. In some embodiments, a probe request 
  - [patent sim=0.690] patent:US11902786B1 | SIM swap fraud prevention | T-Mobile USA, Inc.
    A carrier network may detect and prevent completion of SIM swap frauds. For example, a carrier network may, based at least in part on a SIM swap request to replace a first SIM associated with a subscriber with a second SIM, store first information associated with the first SIM. Subsequent to the execution of a SIM swap to replace the first SIM with the second SIM, the carrier network may perform fraud detection on the SIM swap based at least in part on the first information associated with the first SIM stored based at least in part on the SIM swap request and based at least in part on second information associated with the second SIM and based at least in part on the SIM swap being detected
  - [patent sim=0.669] patent:US20220141669A1 | SIM swap scam protection via passive monitoring | EXFO Solutions SAS
    Subscriber identity module (SIM) swap scam detection include receiving wireless network data based on passive monitoring of a wireless network; identifying a subscriber identity module, SIM, card change in user equipment, UE, based on changes in identifiers in the wireless network data; identifying a commercial user communication with the UE after the SIM card change; and detecting potentially fraudulent activity for the UE based on a combination of the SIM card change, the commercial user communication, and a time period therebetween. The steps can further include providing an alert of the potentially fraudulent activity identifying the commercial user communication as a possible SIM swap s

### A2a-28  (A2a)  ROSCA participation credit scoring
Problem: Thin-file borrowers lack credit history.
Mechanism: Digitised rotating savings groups produce repayment histories used for credit scoring.
Claim core: 
Closest prior art found:
  - [paper sim=0.717] s2:80b842c2c827848989d0617bb95192ded696e6f6 | An Empirical Comparison of Feature Engineering Strategies from Non-Traditional Data for Thin-File Borrower Credit Assessment | 
    Approximately 45 million adults in the United States lack sufficient credit history for conventional scoring, limiting their access to fair lending opportunities. Non-traditional data sources—including behavioral payment patterns, temporal transaction sequences, and relational signals—present promising avenues for assessing these thin-file borrowers, yet the relative predictive contribution of each feature category remains unclear. This study conducts a systematic empirical comparison of feature engineering strategies derived from non-traditional data on the Home Credit Default Risk dataset (307,511 applications across seven linked tables). We define a taxonomy of three feature categories—be
  - [paper sim=0.712] arxiv:2608.26837 | Interpretable hybrid credit scoring for thin-file and underbanked populations | 
    We extend a residual-learning hybrid credit scoring framework (logistic regression scorecard plus a gradient-boosting correction on its residuals, decomposed at each prediction into an interpretability ratio $ρ(x)$ that measures the share attributable to the linear branch) along three axes: an East African empirical instantiation on the Zindi Financial Inclusion in Africa data (Kenya, Rwanda, Tanzania, Uganda); a fairness audit at the granularity of the framework's three interpretability regions; and a thin-file segmentation analysis. On the Taiwan Credit Default benchmark retained for continuity, the calibrated hybrid attains AUC $= 0.776$ ($Δ\mathrm{AUC} = +0.057$ vs.\ standalone logistic 
  - [paper sim=0.705] arxiv:2111.13666 | On the combination of graph data for assessing thin-file borrowers' creditworthiness | 
    

### A2a-29  (A2a)  RTGS gridlock resolution by queue reordering
Problem: Intraday liquidity gridlock.
Mechanism: Optimise payment queue ordering to minimise liquidity needs.
Claim core: 
Closest prior art found:
  - [paper sim=0.685] arxiv:2608.23060 | Atomic Common-Day Invoice Clearing under Causal Daily Scheduling: Path-Enabled and Bounded-Cycle Policies | 
    Late payment propagates working-capital pressure through supply networks because firms are simultaneously creditors and debtors. We develop an atomic-record temporal invoice-graph method for path-enabled clearing and compares it with complete-candidate bounded-cycle netting under a causal daily greedy schedule. Each invoice remains a residual record with its issue date, due date, amount, and identifier. A candidate is executable through source capacity active on every supporting edge on one common day. A non-bilateral two-edge path reduces two invoice legs, creates a direct settlement instruction between the endpoints, and preserves net positions for all participants on the combined invoice-
  - [patent sim=0.679] patent:US20150081491A1 | INTRADAY CASH FLOW OPTIMIZATION | International Business Machines Corporation
    Embodiments relate to intraday cash flow optimization. Transactions are accessed on a business-to-business integration network from a plurality of sources linked with payment delivery system data from a financial service system. The transactions are associated with two or more compartmentalized entities. The transactions are characterizes based on the payment delivery system data and an analysis of customer profile data. The transactions associated with two or more compartmentalized entities are linked as integrated information based on the characterizing of the transactions. An intraday receivables prediction engine and an intraday payables prediction engine are applied to the integrated in
  - [paper sim=0.674] arxiv:2609.26606 | Liquidity Provision and Rebate Design in Option Markets | 
    We provide a model for the nested optimisation problem of market making and rebate design problems in option markets and find optimal strategies. A single market maker trades multiple European call options in a local-stochastic volatility option market with both make and take strategies, modeled, respectively, as continuous and impulse controls. Her objective is to maximize, over all admissible make-take strategies, net profit of option portfolio value and cumulative rebate revenue, subject to a penalty on residual portfolio delta and vega. In addition, we demonstrate how an exchange can incentivize a market maker to improve market liquidity by setting suitable fee rebates, thereby resolving

### A2a-30  (A2a)  Pre-emptive chargeback prediction
Problem: Chargebacks cost merchants.
Mechanism: Predict chargeback probability at authorisation and offer proactive refund.
Claim core: 
Closest prior art found:
  - [patent sim=0.730] patent:US11790367B1 | Systems and methods for optimizing electronic refund transactions for detected fraudulent transactions | Worldpay, LLC
    A method for optimizing refunds for suspected or detected fraudulent transactions includes receiving a chargeback analysis request for a potential chargeback transaction from a merchant or a payment processor, extracting identifying information of transactions associated with the chargeback transaction from the chargeback analysis request, searching for a chargeback analysis profile in a profile database, determining whether the chargeback analysis profile exists in the profile database, upon determining that the chargeback analysis profile does not exist in the profile database, obtaining a new fraud analysis profile, determining, based on the chargeback analysis profile, a first probabilit
  - [patent sim=0.730] patent:US20250384446A1 | SYSTEMS AND METHODS FOR OPTIMIZING ELECTRONIC REFUND TRANSACTIONS FOR DETECTED FRAUDULENT TRANSACTIONS | Worldpay, LLC
    A method for optimizing refunds for suspected or detected fraudulent transactions includes receiving a chargeback analysis request for a potential chargeback transaction from a merchant or a payment processor extracting identifying information of transactions associated with the chargeback transaction from the chargeback analysis request, searching for a chargeback analysis profile in a profile database, determining whether the chargeback analysis profile exists in the profile database, upon determining that the chargeback analysis profile does not exist in the profile database, obtaining a new fraud analysis profile, determining, based on the chargeback analysis profile, a first probability
  - [patent sim=0.726] patent:US20250384444A1 | SYSTEMS AND METHODS FOR OPTIMIZING ELECTRONIC REFUND TRANSACTIONS FOR DETECTED FRAUDULENT TRANSACTIONS | Worldpay, LLC
    A method for optimizing refunds for suspected or detected fraudulent transactions includes receiving a chargeback analysis request for a potential chargeback transaction from a merchant or a payment processor extracting identifying information of transactions associated with the chargeback transaction from the chargeback analysis request, searching for a chargeback analysis profile in a profile database, determining whether the chargeback analysis profile exists in the profile database, upon determining that the chargeback analysis profile does not exist in the profile database, obtaining a new fraud analysis profile, determining, based on the chargeback analysis profile, a first probability

### A2b-01  (A2b)  Unpredictable-quorum confirmation: bank-drawn random co-approvers contacted on bank-initiated channels for out-of-topology treasury instructions
Problem: A cloned executive voice plus a fake WhatsApp thread moved €95M overseas. Attackers script the impersonation of one or two known approvers in advance.
Mechanism: For each corporate client the bank learns the instruction topology: who instructs, through which channel, in what approval order, and for which beneficiary classes and geographies. Any instruction whose path through this graph is new (for example a first overseas beneficiary requested by voice or messaging, or an approver skipping their usual channel) is held for a quorum. At confirmation time the bank draws k co-approvers at random from the client's authorised signatory list using a verifiable random function. It contacts them only through bank-initiated channels on enrolled devices (in-app push with passkey signature), never through the channel the instruction came in on. The attacker cannot know in advance whom else to impersonate, and has to compromise several devices in real time. The VRF output is logged so the selection can be audited.
Claim core: A method comprising: maintaining an instruction-topology model for an organisation; determining that a received payment instruction follows a path absent from the model; selecting co-approvers from authorised signatories using a verifiable random function; requesting signed confirmations via bank-initiated channels to enrolled devices of the selected co-approvers; and releasing the instruction only upon a quorum of confirmations.
Closest prior art found:
  - [patent sim=0.734] patent:US20260289570A1 | SYSTEMS AND METHODS FOR TRANSACTION-TRIGGERED ISSUANCE AND AUTOMATED ROTATION OF VIRTUAL PAYMENT CARDS TO PREVENT PAYMENT FRAUD | Secure Purchase LLC
    Systems and methods are for preventing payment fraud using transaction-triggered issuance and automated rotation of virtual payment card credentials. A system maintains a secure association between a user account and underlying payment credentials issued by financial institutions. The system generates a randomized virtual payment card credential and transmits the same for use at a payment interface. Upon completion of an authorized transaction or satisfaction of a predefined usage condition, the randomized virtual payment card credential is automatically invalidated to prevent reuse. A replacement randomized virtual payment card credential is generated without user intervention. The security
  - [patent sim=0.720] patent:US12682339B1 | Techniques for cosigning blockchain transactions | Blockaid LTD
    A method and system for cosigning a blockchain transaction in a main multisignature (multisig) wallet is presented. The method includes selecting, by a cosigner executed in the main multisig wallet, a blockchain transaction, from a multiple signature (multisig) queue of a main multisig wallet; processing, by a security engine connected to the cosigner, the blockchain transaction through simulation and security validation to determine if the blockchain transaction is valid; signing, by the cosigner, the blockchain transaction when the blockchain transaction is determined to be valid; and withholding the blockchain transaction when the blockchain transaction is determined to be invalid.
CLAIM 
  - [paper sim=0.719] doi:10.1287/mnsc.2024.06807 | Bank Run, Interrupted: Modeling Deposit Withdrawals with Generative AI | 
    I study depositor behavior in panic-driven bank runs using an LLM-based survey simulation. I build a representative population of synthetic agents by assigning demographic attributes, expose them to a viral panic post, and randomize bank communication interventions. I validate model responses against human benchmarks and then generate systematic message variants that vary tone, strength, and content within the validated design space. I then include the estimated withdrawal propensities into a contagion model, which maps network nodes to depositor personas and propagates withdrawals through a single layer proximity network. Direct, personalized bank communications with strong reassurances and

### A2b-02  (A2b)  Synthesis-toolkit fingerprint exchange: banks share model-attribution fingerprints of voice clones used in attacks, not voiceprints of customers
Problem: The same criminal voice-cloning toolkits hit bank after bank, but each bank's deepfake detector learns on its own.
Mechanism: When a call is confirmed as a synthetic-voice attack, the bank extracts a model-attribution fingerprint: residual spectral artefacts, vocoder phase signatures and prosody-generation traces that identify the generation pipeline rather than the imitated speaker. It hashes these into locality-sensitive sketches and publishes them to a consortium index. Member banks query live calls against the index in real time. A match means the call was generated with a toolkit already seen in fraud, even if it imitates a different person. Only sketches of attacker artefacts are shared; no customer voiceprints are, which keeps it outside biometric-data restrictions.
Claim core: A method comprising: extracting from audio of a confirmed synthetic-voice attack a generation-pipeline fingerprint independent of speaker identity; encoding it as a locality-sensitive sketch; publishing it to a shared index; and scoring a live call by similarity of its fingerprint sketch to indexed sketches.
Closest prior art found:
  - [paper sim=0.824] s2:2979066a19169f4f8ee08acb8779d1460f7cef7c | AI-Enabled Voice Cloning and Spoofing Risks in Speaker Verification Systems: A Comparative Analysis of Empirical Evidence | 
    Voice-based authentication is increasingly used in banking, customer support, mobile applications, and remote identity checks because it is fast and convenient. However, recent progress in text-to-speech, voice conversion, and adversarial audio has changed the threat model of automatic speaker verification (ASV). Voice is no longer only a biological characteristic; it can also be copied, converted, replayed, or optimized by AI tools. This paper reviews empirical evidence on AI-enabled voice cloning and spoofing attacks and connects it with public fraud statistics. The comparative analysis shows that cloned and synthetic voices can be persuasive for humans, while adversarial audio can bypass 
  - [patent sim=0.791] patent:US20260112373A1 | DEEPFAKE DETECTION IN COMMUNICATION SESSIONS BASED ON VOICE SAMPLES | T-Mobile USA, Inc.
    Described herein are one or more computing devices determining, based on voice verification models, that a voice audio sample of a calling party engaging in a communication session includes characteristics of a deepfake-generated voice. In response to determining that the voice audio sample includes characteristics of a deepfake-generated voice, the one or more computing devices alert the called party about the deepfake-generated voice.
CLAIM 1: A method comprising: receiving, by one or more computing devices, a voice audio sample of a calling party engaged in a communication session with a called party; determining, by the one or more computing devices and based on voice verification models
  - [paper sim=0.790] s2:aa69292bca52bb0b0c60ba9ecd21a78a413f10cb | Anti-Spoofing Evaluation Benchmark and Layered Defense Strategy for In-Cabin Voiceprint Payment under Voice Cloning Attacks | 
    With the proliferation of voice interaction in intelligent cabins, voiceprint payment is becoming an important payment method in vehicular scenarios. However, deep learning-driven voice cloning technology has significantly lowered the barrier for generating forged speech, posing a serious threat to voiceprint authentication. The enclosed cabin environment, multi-microphone array layout, and real-time requirements make traditional anti-spoofing solutions difficult to migrate directly. This paper systematically analyzes the technological evolution of voice cloning attacks and the in-cabin threat model, constructs a multi-dimensional anti-spoofing evaluation benchmark covering detection perform

### A2b-03  (A2b)  Constraint-level zero-knowledge reserve proofs for GENIUS Act stablecoins (eligibility, maturity ≤93 days, concentration) from signed custodian feeds
Problem: GENIUS Act proposals (Treasury, Fed, FDIC) require 1:1 eligible reserves: deposits, T-bills maturing within 93 days, and qualifying repo. Today's attestations are monthly PDFs, and Merkle proofs of reserves only prove totals.
Mechanism: Custodian banks and the Treasury-bill custodian sign position feeds (CUSIP, maturity, amount; deposit balances per institution). A prover inside the issuer's infrastructure generates a zero-knowledge proof, each block or each hour, that (a) total eligible reserves ≥ outstanding supply read from the chain; (b) every T-bill in the reserve has remaining maturity ≤ 93 days; (c) no single custodian exceeds the configured concentration share; (d) repo collateral meets its eligibility constraints. It reveals none of the individual positions. The proof and the custodian key commitments are posted on-chain, where wallets, exchanges and supervisors can verify them. A failed constraint triggers automatic mint suspension.
Claim core: A system comprising custodian signing modules producing signed position records, a prover generating a zero-knowledge proof that the positions satisfy supply coverage, per-asset maturity and per-custodian concentration constraints, a verifier contract publishing the proof, and a minting controller suspending issuance upon proof failure.
Closest prior art found:
  - [paper sim=0.765] s2:b1b6aed5f7486f588a4b92869d9a812f27e03ce3 | Stablecoins and the Upcoming Battle for Depositors | 
    We lay out the research questions raised by the GENIUS Act of 2025 which creates a federal framework in the United States for payment stablecoins that may compete for balances with bank deposits. We first set out the motivating facts: what stablecoins are used for, what the Act does and leaves open, why a bank deposit is one leg of a bundle rather than a standalone product, and what happened when a previous innovation, namely money market funds, competed for deposits. These facts pose three policy questions relating to payment stablecoins and their issuers— payment of interest or rewards; access to Federal Reserve settlement systems; and obtaining national trust bank charters— and two analyt
  - [paper sim=0.758] s2:e18086e4e4cf2a163ecfe6b2bbf831ac811f7237 | Banks in the Age of Stablecoins: Some Possible Implications for Deposits, Credit, and Financial Intermediation | 
    The rapid growth of stablecoins, accelerated by regulatory frameworks like the Genius Act, has raised important questions about their impact on traditional banking. As these digital tokens gain mainstream acceptance, they could fundamentally reshape the structure and functions of banking and influence the established intermediation role of banks.
  - [paper sim=0.754] s2:80c0c58464a20a470b417cb086ae592a2c861e82 | Stablecoin Reserve Demand and Treasury Convenience Yields: Private Money, Safe-Asset Scarcity, and the Seigniorage of a Strategic Issuer | 
    A fiat-backed stablecoin issuer earns seigniorage by investing par-value liabilities in short-term Treasury securities that carry a convenience yield. Because the issuer has grown large relative to the Treasury-bill market, its reserve demand is no longer price-taking: additional issuance increases bill scarcity, raises the nonpecuniary convenience yield embedded in bills, and thereby lowers the pecuniary reserve return that funds issuer seigniorage. I embed a Krishnamurthy and Vissing-Jorgensen convenience-yield schedule inside a monopolistic private-money issuance problem in the tradition of Klein and of Li and Mayer, in a two-period, two-maturity setting with money-in-utility households w

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

Write the answer to: runs/2026-09-30/llm_responses/judge_006.json
