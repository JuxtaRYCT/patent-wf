# TASK judge_008

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A2b-12  (A2b)  Attenuable delegation chains for multi-agent payments: macaroon-style caveats that sub-agents can only narrow, verified by the issuer
Problem: 'Agentic commerce is an authorisation problem.' A user's agent delegates to a travel agent-bot, which delegates to an airline's agent. Today's mandates are single-hop and cannot express how authority narrows along the chain.
Mechanism: The user's bank issues a root capability token for an agent: a chained-HMAC or signature caveat list covering budget, categories, merchants, time window and number of uses. Each agent can derive a child token for a sub-agent by appending caveats. It can only add restrictions, never remove them, and the chain structure proves this. The final agent presents the full caveat chain with the authorisation. The issuer verifies the chain against the root key in constant time per caveat and evaluates all caveats against the transaction. Revoking any link revokes all its descendants, and every hop is visible for dispute attribution.
Claim core: A method comprising: issuing a root payment capability comprising caveats bound by a chained keyed hash; deriving child capabilities by appending caveats; receiving at an issuer an authorisation request with a capability chain; verifying the chain and evaluating all caveats against the transaction; and approving only if all caveats are satisfied.
Closest prior art found:
  - [paper sim=0.781] arxiv:2609.00060 | A Formal Analysis of Agent Payment Protocols | 
    Agent payment protocols are emerging as a key transaction layer for autonomous commerce, enabling AI agents to purchase goods and services and execute payments on users'behalf. Unlike conventional payment flows, they distribute user intent, delegated authority, credential use, settlement, and fulfillment across multiple actors and stages, creating security dependencies that no single message or participant can enforce. Yet these guarantees remain largely implicit across evolving specifications, schemas, and reference implementations, with little systematic formal analysis. We formalize four representative agent payment protocols: x402, MPP, ACP, and AP2 in Tamarin. Using a common abstraction
  - [paper sim=0.759] arxiv:2605.00071 | Compliance-Aware Agentic Payments on Stablecoin Rails | 
    
  - [patent sim=0.758] patent:US20260154681A1 | AGENTIC MICROTRANSACTIONS THROUGH VERIFIABLE PAYMENT DELEGATION | Mastercard International Incorporated
    A method for agentic microtransactions through verifiable payment delegation includes, during a single Internet Protocol session between a client and a server in which content hosted by the server is being or is to be accessed by the client, receiving, at a facilitator, a transaction request message including a transaction identifier, a transaction amount, a personal account number (PAN), and a cryptographic signature transmitted to the server from the client as part of the session; generating, at the facilitator, an authorization request message including at least the PAN and the cryptographic signature; sending, by the facilitator, the authorization request message to a payment network; re

### A2b-13  (A2b)  Consumer-signed permissible-purpose tokens for credit report pulls
Problem: 356k complaints about improper use of reports. Pulls happen without verifiable consumer authorisation, and freezes are blunt on/off switches.
Mechanism: A consumer's wallet issues short-lived pull tokens bound to the requesting lender's identity, the permissible purpose, the product and the time window, signed by a device key. The bureau releases a report only against a valid token, or an explicit statutory exception, which is logged separately. Tokens can be one-time, limited to a soft or hard pull, and revoked. Consumers see a signed access log. Lenders integrate through a redirect or QR flow similar to account-aggregator consent artefacts.
Claim core: A method comprising generating on a consumer device a signed access token specifying a requesting entity, purpose and validity, receiving at a credit bureau a report request with the token, verifying token signature and scope, and releasing report data only upon verification.
Closest prior art found:
  - [patent sim=0.706] patent:US20160371741A1 | SYSTEM AND METHOD FOR PULLING A CREDIT OFFER ON BANK'S PRE-APPROVED PROPERTY | Segmint Inc.
    A method of providing a personalized advertisement campaign purpose includes: receiving from a financial institution anonymized customer data associated with a plurality of customers of the financial institution and a prospective unique customer identification code associated with the plurality of customers of the financial institution; creating key lifestyle indicators, which describe customer attributes, from the anonymized customer data; receiving from the financial institution an authenticated unique customer identification code that is matched to authenticated data from at least one prospective customer of the plurality of customers of the financial institution; matching the prospective
  - [patent sim=0.700] patent:US12700034B2 | Method and system for offering a credit product by a credit issuer to a consumer at a point-of-sale | PayPal, Inc.
    A method for offering at least one credit product by at least one credit issuer to a consumer at a point-of-sale between a merchant and the consumer. The method includes the steps of: providing a credit issuer data set including a plurality of data fields to a central database; initiating a transaction between the consumer and the merchant at the point-of-sale; offering, to the consumer at the point-of-sale, the at least one credit product; and presenting, to the consumer at the point-of-sale, at least one data field in the credit issuer data set. The at least one data field presented to the consumer is populated with data directed to the credit product, the credit issuer, or any combination
  - [patent sim=0.695] patent:US20260037943A1 | METHOD OF PULL-BASED REAL TIME PAYMENT AUTHORIZATION | American Express Travel Related Services Company, Inc.
    Disclosed herein are system, apparatus, article of manufacture, method and/or computer program product embodiments, and/or combinations and sub-combinations thereof, for allowing an account holder to authorize an entity to issue pull requests for funds to be transferred using real time payment rails. A first account representing a store of central bank digital currency (CBDC) of a first user may be linked with a second account representing a store of central bank digital currency (CBDC) of a second user. A request may be received, from one of the first and second user, to transfer CBDC from the first account to the second account. From another of the first and second user, an authorization m

### A2b-14  (A2b)  Purchase-session binding for UPI: aggregating split payments per merchant session for correct MDR and fewer false fraud flags
Problem: RBI backs MDR on UPI payments above ₹2,000, which gives merchants and payers an incentive to split payments. Banks already flag repeated ₹2,000 payments as suspicious, which hurts legitimate split payments.
Mechanism: A merchant QR or intent carries a session identifier signed by the merchant's PSP, derived from the cart/bill. Payments carrying the same session ID within a window are aggregated at the acquirer for MDR computation, removing the split-to-evade incentive. On the risk side, the payer's PSP treats payments sharing a verified session ID as one purchase, so legitimate splits (limits, multiple sources) are not flagged. Splits without a session ID, to the same payee in a short window, keep full scrutiny.
Claim core: A method comprising generating a signed session identifier for a merchant purchase, receiving multiple payments referencing the identifier, aggregating their amounts for fee computation, and applying risk scoring at the aggregated purchase level.
Closest prior art found:
  - [paper sim=0.739] s2:730b996e83ae9924d5b368c828ebe675def30c36 | PAYMENT FAILURES AND REVENUE DISRUPTION: ASSESSING THE RELIABILITY GAP IN UPI ADOPTION AMONG INDIA'S INFORMAL VENDORS | 
    Existing research on Indias Unified Payments Interface (UPI) has largely measured success through adoption, transaction volumes, and financial inclusion, treating uptake as evidence the system works. For informal vendors, running on thin margins and immediate liquidity needs, whether a payment can be depended on matters as much as whether it was accepted, a dimension that remains underexplored. This study examines how UPI payment failures affect vendors daily operations and liquidity, based on fieldwork with 55 vendors in Mira Bhayander Market, interviewed in Hindi and Marathi, alongside a survey of 56 customers.The findings identify six recurring sources of reliability failure: liquidity ac
  - [paper sim=0.735] s2:d312950cd3dc28438740b6ba825465681e820856 | A STUDY ON CONSUMER AWARENESS, USAGE, AND PREFERENCE TOWARDS UNIFIED PAYMENTS INTERFACE (UPI) IN CHENNAI CITY | 
    India’s financial transaction landscape has undergone a complete shift due to the growing number of digital payment technologies, with the Unified Payments Interface (UPI) being one of the most popular payment platforms in the country. UPI is a real-time, secure fund transfer system developed by the National Payments Corporation of India (NPCI) that allows for transfers between bank accounts via mobile devices and can be used for person-to-person (P2P) and person-to-merchant (P2M) transactions. This convenience, speed and accessibility has led consumers to be more and more inclined to opt for digital payment methods as opposed to cash-based transactions. The present study aims at evaluating 
  - [paper sim=0.732] s2:1be796025de213ef746714b0effc2513803069b9 | Digital Payment Adoption and Consumer Spending Behaviour in India: Evidence from UPI Growth, Convenience and Trust (2020–2026) | 
    Abstract The rapid expansion of digital payments has altered the way consumers purchase goods and services in India. Among the available digital payment instruments, the Unified Payments Interface (UPI) has become particularly important because it combines real-time settlement, interoperability, mobile accessibility and widespread merchant acceptance. This study examines the relationship between digital-payment development and consumer buying behaviour, with specific attention to perceived convenience, trust and spending behaviour. The research adopts a descriptive-analytical design based entirely on secondary evidence. Data are drawn from the Reserve Bank of India’s Digital Payments Index (

### A2b-15  (A2b)  'Digital arrest' coercion-state detector with physically separated release ritual
Problem: Deepfake-backed 'digital arrest' rackets keep victims on long video calls with fake police while they transfer crores. The victim is coerced, so friction inside the app is simply overridden.
Mechanism: The banking app fuses on-device signals (with consent): concurrent long-duration video call, screen sharing active, repeated balance checks, a first-time high-value payee, typing hesitation and copy-paste of beneficiary details. From these it infers a coercion state. In that state the app does not ask 'are you sure?'. It requires a release ritual that the remote coercer cannot supervise and that breaks the call: end the call, then after a mandatory 30-minute gap confirm the transfer at an ATM or branch with the physical card, or have it confirmed by a pre-registered trusted person. Meanwhile the app plays a verified-number callback from the bank's anti-fraud line.
Claim core: A method comprising determining a coercion state from concurrent communication-session and interaction signals on a user device, and upon the coercion state requiring confirmation of a pending transfer through a physically separate channel after a delay.
Closest prior art found:
  - [paper sim=0.756] s2:18e6beb7ddcf1b6e07e1410846a9dcdffbb3a31e | Digital Arrest Using Artificial Intelligence Generative Deepfake Media Content in Post-Truth Society | 
    In the present digital era, a new society is emerging, one that is often referred to as the post-truth society. In a post-truth society, facts are being eroded, and citizens are increasingly susceptible to fake information. Presently, in a post-truth society, deepfake media content can be produced with the help of artificial intelligence. Online schemers use Deepfake videos, photographs, and animated content to put victims under digital arrest. Cybercriminals create fake identities by cloning the voices of individuals and impersonating government officials to commit financial fraud.Due to an absence of awareness, the vast majority of victims fall into the situation of digital arrest. These f
  - [patent sim=0.692] patent:US20230230085A1 | User Authentication and Transaction Verification via a Shared Video Stream | IRONVEST, INC.
    A user interacts with a remote server via an end-user device, and enters transaction data. A user-facing camera of the end-user device captures a live video feed of the interacting user; which is displayed in real time on the screen of the end-user device while the user is filling-out fields and entering transaction data. The concurrent, real-time, video-feed display of the interacting user, near—or as a background layer behind—the fillable fields of the transaction data, deters at least some cyber-attacks or prevents fraud attempts. Optionally, the screen of the end-user device is also continuously shared, over a secure communication channel, via a locally-installed Screen Sharing Module, w
  - [paper sim=0.690] s2:2aeb1f0b3c37f2bab29cf61285ced11ac4ec116b | DEEPFAKE TECHNOLOGIES AS A NEW TOOL FOR COMMITTING CRIMINAL OFFENCES: A COMPARATIVE STUDY | 
    This article presents a comprehensive study of deepfake technologies as a new tool for committing criminal offences against the backdrop of the rapid development of generative artificial intelligence and the digitalisation of society. The relevance of the topic stems from the significant increase in the use of deepfake technologies in fraud, cybercrime, information and psychological operations, extortion, invasion of privacy, as well as in crimes against the foundations of national security. It is emphasised that modern deepfake materials are characterised by a high level of realism, which significantly complicates their detection, verification of authenticity, and use in criminal proceeding

### A2b-16  (A2b)  Merchant-verifiable signed payment receipts to defeat fake 'frozen-screen' UPI success screens
Problem: In the 'frozen-screen' UPI scam, fraudsters show merchants a fake or frozen success screen. Merchants without a soundbox cannot verify that a credit really arrived.
Mechanism: On successful debit, the payer app renders a receipt code: a QR or ultrasonic burst carrying a token signed by the payee's PSP that includes the merchant's session nonce, amount and UTR. The merchant's phone, or a cheap verifier, checks the signature and nonce offline against the merchant PSP's public key. A static or fake screen cannot produce a valid signature for the live nonce.
Claim core: A method comprising receiving at a payer device a payee-PSP-signed confirmation including a merchant session nonce and amount, rendering it as a machine-readable code, and verifying at a merchant device the signature and nonce before releasing goods.
Closest prior art found:
  - [patent sim=0.699] patent:US20260268299A1 | Remote Template Based Receipt Generation | Block, Inc.
    A point-of-sale (POS) device of a merchant can receive, from server(s) of a payment service, templates defining respective receipts available for use by the merchant. The POS device can receive input indicating the merchant's selection of a template and send data associated with that selection to the payment service's server(s). A payment instrument identifier can be received by the POS device from a card reader in association with a transaction between the merchant and a customer. The POS device can send a request to authorize the payment instrument to the server(s) of the payment service and receive data representing a receipt for the transaction, wherein the server(s) generate the receipt
  - [patent sim=0.699] patent:US20130151419A1 | Merchant Verification of In-person Electronic Transactions | Hitchcock; Daniel W., Canavor; Darren E., Ramalingam; Harsha, Hanson; Robert, Campbell; Brad Lee
    Validation data, such as an image selected by a merchant, is rendered on a mobile device of a customer to provide the merchant confirmation that payment for an item submitted through the mobile device of the customer was in fact received by the merchant. The merchant may establish an account on a network-accessible computing device (e.g., in the "cloud") that includes the validation data. The customer authorizes payment to the merchant from the mobile device using the network connectivity of the mobile device. When the payment is received by the merchant, the network-accessible computing device sends the validation data to the customer's mobile device. The merchant may be confident that he o
  - [patent sim=0.697] patent:US20140156531A1 | System and Method for Authenticating Transactions Through a Mobile Device | SALT Technology Inc.
    A user may claim to have not made or allowed a transaction and that the transaction was made in error. Where it appears the user has not authorized the transaction, the funds of the transaction are returned to the user, or are charged back. Systems and methods provide a way to confirm whether or not a transaction was actually authorized by the user, thereby settling a chargeback dispute for a previously executed transaction. The method comprises receiving the dispute regarding the transaction including associated transaction data, and retrieving a digital signature associated with the transaction data, the digital signature computed by signing the transaction data. The digital signature is t

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

Write the answer to: runs/2026-09-30/llm_responses/judge_008.json
