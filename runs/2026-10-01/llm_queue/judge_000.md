# TASK judge_000

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A1-1001-01  (A1)  Comprehension-verified scam warnings with tamper-evident 'reasonable steps' receipts
Problem: Scam-reimbursement regimes (Australia's AFCA scam rules, UK APP reimbursement) judge banks on whether they took reasonable steps, yet banks cannot prove a warning was understood. Research shows standard security notifications fail users with intellectual and developmental disabilities, and such users are over-represented among victims.
Mechanism: When a payment triggers a scam warning, a rendering engine picks the warning format from the customer's accessibility profile and recent interaction signals: plain-language chunks, pictograms, read-aloud audio, or a step-by-step version. It then asks one comprehension question generated from the specific risk, for example 'Who told you to make this payment?' with three choices including 'someone I met online'. The answer, the response time and the format shown are hashed with the payment digest into a signed warning receipt and appended to a tamper-evident log. A wrong or rushed answer escalates to a human call-back. Receipts are later produced as evidence of reasonable steps in disputes and regulatory reviews.
Claim core: A method comprising selecting a warning presentation format based on an accessibility profile of a user, presenting a risk-specific comprehension query before authorising a flagged payment, generating a signed receipt binding the format, the response and a digest of the payment, appending the receipt to a tamper-evident log, and escalating the payment upon an incorrect or below-threshold-time response.
Closest prior art found:
  - [paper sim=0.725] doi:10.2139/ssrn.7426879 | Beyond Successful Authentication: Reconstructing the Evidentiary Architecture of Payment-fraud Liability under PSD2 in Light of Eurobank Bulgaria and the Pendin | 
    &lt;div&gt; Payment Service Providers (PSPs) may treat the successful completion of SCA as conclusive evidence that a disputed payment was authorised by the payer. On this basis, they may consider their evidentiary burden under Article 72 of PSD2 to have been satisfied and, consequently, avoid the obligation under Article 73 to provide an immediate refund. This article undertakes a doctrinal analysis of the relationship between authentication, SCA, and authorisation under PSD2. It examines how the CJEU’s judgment in Eurobank Bulgaria (C-409/22) and Advocate General Rantos’s Opinion in the pending Tukowiecka (C-70/25) reference place limits on the practice of treating successful SCA as conclu
  - [patent sim=0.720] patent:US20260006044A1 | IDENTIFYING AND REMEDIATING SCAM ELECTRONIC MESSAGES | RANGERS.AI
    One embodiment provides a computer-implemented method that includes receiving, by a processor, an indication of messaging applications to monitor, specifying a risk threshold. The processor further provides a notification to at least one device. The notification includes an identified scam message from the messaging applications. The processor additionally provides step-by-step guidance on actions to take to the at least one device.
CLAIM 1: A computer-implemented method comprising: receiving, by a processor, an indication of one or more messaging applications to monitor, specifying a risk threshold; providing, by the processor, at least one notification to one or more devices, wherein the a
  - [patent sim=0.713] patent:US20250069082A1 | Electronic Devices and Corresponding Methods for Presenting Fraud Warnings for Transaction Reversal Requests | Motorola Mobility LLC
    An electronic device includes a communication device, a user interface, and one or more processors operable with the communication device and the user interface. In response to the communication device receiving a financial transaction communication and a financial transaction reversal request communication, optionally within a predefined time duration threshold, the one or more processors cause the user interface to deliver a prompt comprising a fraud warning indicating that the financial transaction reversal request is likely fraudulent.
CLAIM 1: A method in an electronic device, the method comprising: receiving, by a communication device, first electronic signals delivering an indication 

### A1-1001-02  (A1)  Payee-label semantics: scam narratives revealed by the names victims are told to give payees
Problem: Bank staff stopped a £13,500 scam only because the victim's payees were labelled 'Donald Trump', 'Kim Kardashian' and 'Jennifer Lawrence'. Each payment passed every automated check; the narrative the scammer planted lived only in free-text fields that no model reads.
Mechanism: At payee creation and payment time, an on-device or server classifier reads the user-entered payee nickname and payment reference and compares them with the confirmation-of-payee legal name. Signals include: the label names a public figure, a celebrity or a government agency; the label suggests an investment, customs fee, release fee or 'unlock' payment; and the semantic distance between the label and the legal name is large. These label features are combined with the cumulative flows to such payees over the session, so a series of individually ordinary payments is caught as one pattern. Hits trigger a narrative-specific warning ('A celebrity will never ask you for money') and a human call-back.
Claim core: A method comprising receiving a user-entered label and reference for a payee, classifying the label against a public-figure and scam-narrative lexicon and its semantic distance to a verified legal name of the payee account, aggregating flows to payees with flagged labels over a session, and intervening when the aggregate satisfies a condition.
Closest prior art found:
  - [paper sim=0.686] arxiv:2607.17586 | Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification | 
    Money mule accounts are critical facilitators of financial fraud, yet detecting them at scale remains challenging due to the heterogeneous nature of transactional and behavioural data. We present an end-to-end pipeline for customer-level mule detection comprising three stages: (1) a LightGBM classifier trained on 280 engineered features spanning transaction patterns, account demographics, network topology, and temporal behaviour; (2) a TreeSHAP attribution layer that decomposes each prediction into feature contributions; and (3) a large language model (LLM) module that converts SHAP attributions into analyst-facing natural-language narratives. We evaluate across three open-weight LLM familie
  - [paper sim=0.677] arxiv:2608.24127 | Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate | 
    Telephone fraud is pervasive and costly, but its inner workings are rarely observed at scale. We analyze a complete corpus of 10,211 inbound scam and spam calls -- 913 hours of audio and 330,956 transcribed turns from 5,780 distinct numbers -- collected over 54 days by an AI voice-agent honeypot that answered callers and kept them talking, and introduced in a companion data descriptor. We separate outright scams, which solicit sensitive information, from the larger stream of predatory but legal lead generation ("spam") that feeds them. Scam operations keep office hours (6.6x more calls per weekday than weekend day); thousands of disposable numbers run a small catalog of recycled scripts (thi
  - [paper sim=0.674] arxiv:2608.17715 | Communicating Credit Risk with Large Language Models: Evaluation of Explanations from Standard and Alternative Data-Based Models | 
    Credit decisioning is a high-stakes task in which model outputs must be accurate and explainable to support compliant decisions. Although modern credit risk models such as eXtreme Gradient Boosting (XGBoost) and Graph Neural Networks (GNNs) improve predictive performance, their explanations are often too technical for stakeholders creating communication gaps that can shape approvals, denials, and fairness judgments. We examine whether Large Language Models (LLMs) can serve as explanation layers that translate post-hoc explanation artefacts into stakeholder-appropriate risk narratives. Using Freddie Mac single-family loan-level data, we develop three pipelines: standard tabular (XGBoost + SHA

### A1-1001-03  (A1)  Blendshape-residual liveness: detecting real-time deepfake avatars in video KYC from motion that a low-rank face basis cannot express
Problem: Video-based customer onboarding (India's V-CIP, remote account opening) is attacked with real-time animated avatars. New research shows such avatars can be closely approximated by a small, identity-independent linear blendshape basis, which makes cheap live deepfakes practical.
Mechanism: During the video call, the system fits a low-rank blendshape model to the tracked face mesh in each frame and measures the residual deformation it cannot explain. Real faces produce persistent non-linear residuals: skin compression, wrinkles, asymmetric micro-expressions. Blendshape-driven avatars leave near-zero residual. The session also issues randomised physical-deformation challenges designed to maximise residual on real faces, such as pressing a finger into the cheek, puffing one cheek or pulling the lower lip. Liveness is scored from the residual energy against the challenge timeline; a low residual under deformation challenges flags a synthetic face.
Claim core: A method comprising tracking a face mesh in video frames of a remote identity session, fitting a low-rank blendshape model to each frame, computing residual deformation energy unexplained by the model, presenting physical-deformation challenges, and determining liveness from the residual energy during the challenges.
Closest prior art found:
  - [paper sim=0.812] s2:87674657f4a9664d97d372cfe1c0f10b25d30731 | Real-Time Deepfake Recognition | 
    Deepfake technology has grown rapidly with the advancement of artificial intelligence and deep learning techniques, enabling the creation of highly realistic manipulated images and videos that are often difficult to distinguish from genuine content. While this technology has useful applications in media and entertainment, its misuse has raised serious concerns in areas such as identity verification, digital communication, and financial transactions. The increasing spread of fake videos across social media platforms has led to misinformation, identity fraud, and cyber security risks. Traditional verification methods are often slow and unreliable, especially when dealing with large volumes of 
  - [patent sim=0.809] patent:US12300035B1 | Liveness detection based on motion, face, and context cues | Amazon Technologies, Inc.
    Techniques for liveness detection using a motion, face, and context cues. The techniques can be implemented to prevent against successful presentation attacks, video injection attacks, and deepfake attacks. In some examples, the techniques encompass receiving a set of video frames from a personal computing device. A first liveness determination can be made using a motion-based model based on the received video frames. A second liveness determination can be made using a face-based model based on the received video frames. A third liveness determination can be made using a context-based model based on the received video frames. A final liveness determination can be made based on the first, sec
  - [paper sim=0.806] s2:11f5300964aab5cd85dfc9b035f7a8071879c3a9 | 3D Spatiotemporal Model for Detection of Compressed Deepfake Videos | 
    Deepfake content poses a significant threat to digital media integrity, driven by rapid advances in generative deep learning models that manipulate facial identities and expressions with increasing realism. The resulting synthetic videos facilitate the spread of misinformation, financial fraud, and privacy violations, underscoring the urgent need for robust detection methods. Most existing deepfake detectors experience significant performance degradation when processing compressed videos commonly distributed on social media platforms. To address this challenge, we propose a fully three-dimensional deep learning architecture that integrates a 3D-Convolutional Neural Network (3D-CNN) backbone 

### A1-1001-04  (A1)  Collusion-resistant aggregation of crowd-sourced scam reports for pre-payment payee checks
Problem: Pre-payment payee checks increasingly use crowd reports of scam accounts and numbers (national reporting portals, bank-app 'report this payee'). Scammers can poison them in both directions: mass-flagging legitimate competitors, or vouching for their own mules.
Mechanism: Each report is modelled as a rater-item edge in a bipartite graph. Rater reliability is estimated with peer-assessment integrity methods: agreement with later ground truth (confirmed fraud reports, account closures), detection of collusive rater clusters (synchronised timing, shared devices, reciprocal patterns), and down-weighting of raters whose reports concentrate on a single item. Each payee receives a reliability-weighted scam score with a confidence interval. The payee check returns the score band and confidence instead of a raw report count, and the bank logs which raters' reports were discounted and why.
Claim core: A method comprising receiving scam reports linking reporters to payee identifiers, estimating reporter reliability from agreement with confirmed outcomes and detection of collusive reporter clusters, computing a reliability-weighted risk score with confidence for a payee, and returning the score in response to a pre-payment check.
Closest prior art found:
  - [patent sim=0.784] patent:US20260212362A1 | SYSTEM AND METHOD FOR REAL-TIME ONLINE REVIEW FRAUD DETECTION USING FRAUD-AWARE SELECTIVE ATTENTION WITH MULTI-TIER VERIFICATION | LEVENTOGLU; ÖNDER
    A system and method for real-time detection of fraudulent online reviews using fraud-aware selective attention that allocates computation according to a fraud probability density over textual segments and metadata. Calibrated confidence, adapted to platform base rates, enables dynamic routing among lightweight models, complex models, and a multi-tier human review path. Coordinated fraud is detected by aggregating temporal, textual, network, and behavioral features into a coordination score. Verification outcomes are committed as incremental Merkle proofs with batched anchoring to a ledger without storing personally identifiable information, providing audit-suitable evidence for regulatory co
  - [paper sim=0.774] doi:10.2139/ssrn.7478298 | BankGuard-CGR: A Conformal Graph-Rule Framework for Fraud and Anti-Money-Laundering Detection in Banking Payment Systems | 
    Banking payment platforms operate under two pressures that rarely align. They must catch a small share of fraudulent and money-laundering transfers while keeping analyst queues short enough to review every alert. This paper presents BankGuard-CGR, a framework that combines gradient-boosted scoring on tabular transaction features, graph-based rule boosts on the account transfer network, and Mondrian conformal calibration by channel. The design gives operations teams a probability that is meaningful under drift, a threshold that respects a fixed daily alert budget, and a coverage guarantee on the positive class. Using a synthetic payment ledger of 120,000 transactions across 15,000 accounts an
  - [paper sim=0.772] s2:764eb9e9efc690177710684ac9bf0fee3aff0325 | Multisource Fraud Intelligence Using Graph Neural Networks for Merchant, Account, and Transaction Risk Assessment | 
    Fraud intelligence in payment platforms is inherently relational: a transaction belongs to an account, reaches a merchant, and inherits risk from prior behavior on both sides. Yet graph models can underperform strong tabular learners when fraud labels are scarce or when new accounts appear after training. This paper evaluates that trade-off with a leakage-controlled heterogeneous graph experiment on a 10,000-transaction public BankSim extract containing 6,021 customer accounts, 899 merchants, 16 categories, and 78 frauds. Transactions are ordered by simulation step; steps 1–110 train the models, steps 111–145 select thresholds and graph-fusion weight, and steps 146–180 form a locked future t

### A2b-1001-01  (A2b)  Exception-only merchant re-KYC for payment aggregators using signed government data trails
Problem: Payment aggregators are asking RBI for more time on merchant re-KYC deadlines. Re-verifying millions of small merchants by documents and video is slow and expensive, although most merchants already leave signed digital trails.
Mechanism: For each merchant the aggregator automatically gathers digitally signed government and network records: GST e-invoice IRN signatures, GSTR filing status, Udyam registration, settlement-account ownership confirmed through account-aggregator consent, and UPI collection patterns. A rules-plus-model engine compares them with the merchant's onboarding KYC. Consistent, signature-verified merchants are re-KYC'd automatically and receive a signed re-KYC record. Only mismatches (name or PAN drift, a dormant GST registration, a settlement account in a different name, a sudden category change) go to manual or video re-KYC.
Claim core: A method comprising retrieving digitally signed records associated with a merchant from government and payment-network sources, verifying the signatures, comparing record attributes with stored onboarding identity attributes, generating a signed re-verification record when consistent, and routing the merchant to manual verification upon an inconsistency.
Closest prior art found:
  - [paper sim=0.729] s2:23c7490b635031b1fc5fd493192e786acdeaee2a | Instant Fraud Detection Gateway for Secure Digital Transactions | 
    The rapid expansion of digital payments in India, led by the Unified Payments Interface (UPI), has significantly enhanced financial accessibility and transaction efficiency, processing over 12 billion transactions per month in 2024. However, this growth has been accompanied by a sharp rise in fraud, with reported losses exceeding INR 1,400 crore in 2023–24, primarily due to phishing, identity spoofing, money mule networks, and exploitation of dormant or fraudulent accounts. This paper presents an Instant Fraud Detection Gateway, a real-time pre-transaction security layer that integrates seamlessly with existing payment infrastructures. The system performs recipient validation against authori
  - [patent sim=0.713] patent:US12725159B2 | Methods and systems for identifying a re-routed transaction | MASTERCARD INTERNATIONAL INCORPORATED
    Embodiments provide methods and systems for identifying a re-routed transaction. Method performed by processor includes retrieving a plurality of transaction windows from a transaction database. Each transaction window includes a transaction declined under a restricted MCC. The method includes accessing a plurality of features associated with each transaction of each transaction window from the transaction database. The method includes predicting an output dataset of a plurality of reconstructed transaction windows based on feeding the input dataset to a trained neural network model. The method includes computing a corresponding reconstruction loss value for each transaction of each transact
  - [patent sim=0.706] patent:US20140156531A1 | System and Method for Authenticating Transactions Through a Mobile Device | SALT Technology Inc.
    A user may claim to have not made or allowed a transaction and that the transaction was made in error. Where it appears the user has not authorized the transaction, the funds of the transaction are returned to the user, or are charged back. Systems and methods provide a way to confirm whether or not a transaction was actually authorized by the user, thereby settling a chargeback dispute for a previously executed transaction. The method comprises receiving the dispute regarding the transaction including associated transaction data, and retrieving a digital signature associated with the transaction data, the digital signature computed by signing the transaction data. The digital signature is t

### A2b-1001-02  (A2b)  Recovery-scam shield: protected mode and a signed official recovery channel for people who were just scammed
Problem: 'The bigger problem comes after the scam': victims who report fraud are re-targeted by fake 'fund recovery' agents, lawyers and police impersonators asking for processing fees. Modern syndicates move faster than defences, and victims cannot tell genuine recovery contact from a second scam.
Mechanism: When a customer reports a scam (bank channel, 1930/NCRP or a similar portal), their account enters a time-boxed protected mode. New payees whose label, reference or merchant category matches recovery, legal-fee, tax-clearance or 'release' narratives trigger a hard stop with a call-back. Large transfers to first-time payees get a mandatory delay. Every genuine recovery communication from the bank or partner law-enforcement agency is delivered as a signed message in the bank app's 'official recovery' inbox, with the case ID and the next steps. Any outside contact claiming to be about recovery can be checked in-app against that inbox, and the app states plainly that genuine recovery never asks for fees.
Claim core: A method comprising, upon receipt of a fraud report for an account, setting the account to a protected state for a period in which payments to new payees matching recovery-scam narrative features are blocked pending verification, and delivering case communications as digitally signed messages verifiable within an application of the account holder.
Closest prior art found:
  - [patent sim=0.692] patent:US20250069082A1 | Electronic Devices and Corresponding Methods for Presenting Fraud Warnings for Transaction Reversal Requests | Motorola Mobility LLC
    An electronic device includes a communication device, a user interface, and one or more processors operable with the communication device and the user interface. In response to the communication device receiving a financial transaction communication and a financial transaction reversal request communication, optionally within a predefined time duration threshold, the one or more processors cause the user interface to deliver a prompt comprising a fraud warning indicating that the financial transaction reversal request is likely fraudulent.
CLAIM 1: A method in an electronic device, the method comprising: receiving, by a communication device, first electronic signals delivering an indication 
  - [paper sim=0.689] s2:926e1e4e972143e875d9d59981e5cd562fd24896 | Online Financial Fraud in India: A Legal and Criminological Study | 
    India’s rapid transition to digital banking, mobile wallets, payment cards and the Unified Payments Interface has expanded financial inclusion while creating new opportunities for online financial fraud. This paper examines the principal forms of online financial fraud in India and evaluates whether the existing criminal, procedural, evidentiary, regulatory and consumer-protection framework can deliver timely prevention, investigation and victim redress. It adopts a doctrinal and qualitative analytical method, supported by criminological perspectives including routine activity, rational choice, differential association and victimology. The analysis covers phishing, vishing, smishing, UPI fra
  - [patent sim=0.684] patent:US20260006044A1 | IDENTIFYING AND REMEDIATING SCAM ELECTRONIC MESSAGES | RANGERS.AI
    One embodiment provides a computer-implemented method that includes receiving, by a processor, an indication of messaging applications to monitor, specifying a risk threshold. The processor further provides a notification to at least one device. The notification includes an identified scam message from the messaging applications. The processor additionally provides step-by-step guidance on actions to take to the at least one device.
CLAIM 1: A computer-implemented method comprising: receiving, by a processor, an indication of one or more messaging applications to monitor, specifying a risk threshold; providing, by the processor, at least one notification to one or more devices, wherein the a

### A2b-1001-03  (A2b)  Member-attributed reserve tranches for multi-issuer shared stablecoins
Problem: A shared stablecoin backed by a consortium (Open USD with Coinbase, Mastercard, Stripe and Visa committing $1B of liquidity) pools reserves contributed and custodied by many members. If one member's custodian fails or is seized, holders cannot see which tokens are affected, and the consortium has no automatic rule for who absorbs the loss.
Mechanism: Each member's reserve contribution is recorded as a tranche with its own signed custodian attestation feed. A consortium contract maintains the mapping from circulating supply to tranches pro rata, plus an attestation freshness and health score for each tranche. When a tranche's attestation goes stale or fails a check, that member's minting is suspended automatically. Recapitalisation calls are issued to the remaining members under pre-agreed waterfall rules, and a public proof shows that supply is still fully backed by healthy tranches. Redemptions draw from healthy tranches first.
Claim core: A system maintaining reserve tranches attributed to consortium members of a token, receiving signed custodian attestations per tranche, computing tranche health, suspending minting by a member whose tranche fails a health condition, issuing recapitalisation requests under a waterfall rule, and publishing a proof that circulating supply is covered by healthy tranches.
Closest prior art found:
  - [paper sim=0.733] s2:f8438a437b44d2122255f7988f1a22aa7eddace2 | Stablecoins as private money: a policy agenda | 
    Stablecoins are rapidly expanding as money-like assets for payments, trading, settlement, and cross-border transfer. This paper argues that stablecoins should be understood as emerging systems of private money rather than merely as crypto-assets. Once viewed through that lens, the relevant policy questions extend beyond issuer-level regulation, customer protection, and financial-integrity safeguards to the systemic and institutional conditions under which stablecoins can become a beneficial part of the monetary and payments system. Drawing on monetary theory, recent market developments, our own analytical work, and the broader academic literature, we develop a research-based policy agenda fo
  - [paper sim=0.731] s2:32dbafb611b0dfd2476686b6a18aee1b249299ff | Reserve-backed tokens : A money for the future? | 
    Exactly what form the money of the future will take remains an open question. Central bank digital currencies (CBDCs), tokenised deposits and stablecoins have been discussed as potential candidates. This paper argues that reserve-backed tokens (RBTs) — backed solely and fully by central bank reserves — also represent a credible solution. RBTs pose a unique combination of benefits. Notably, they are safer than, and can crowd out, the unstable breeds of stablecoins. They can adopt a more flexible design than retail CBDCs and thus foster greater competition and innovation. Furthermore, compared with bank deposits, RBTs are immune to runs and are unencumbered by legacy features. Naturally, there
  - [paper sim=0.729] s2:ab0cd7f404898f818f079d6a5ed2c86288383563 | Stablecoins as a New Monetary Layer: Market Structure, Reserve Design, and the Competition with Tokenized Deposits | 
    Stablecoins have evolved from liquidity tools for crypto trading into a form of tokenized private money with implications for payments, cross-border transfers, short-term funding markets, and the architecture of money itself. The literature on stablecoins has expanded rapidly but remains fragmented across stability, reserve design, banking, payments, and regulation. This paper synthesizes that literature into a single integrative argument: stablecoins should be analyzed as a distinct monetary layer within tokenized finance, evaluated against the BIS framework of singleness, elasticity, and integrity, and compared with tokenized deposits as their most relevant institutional alternative. Drawi

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

Write the answer to: runs/2026-10-01/llm_responses/judge_000.json
