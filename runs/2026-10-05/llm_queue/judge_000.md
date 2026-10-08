# TASK judge_000

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A1-1005-01  (A1)  Identity-transition continuity credentials: updating KYC across banks after a name or gender change without freezes or full re-KYC
Problem: When a person's legal identity attributes change (gender transition, marriage, name correction, a PAN/Aadhaar update), linked identity systems fall out of sync. Banks see a KYC mismatch, freeze accounts or demand full re-KYC, and the harm falls on people least able to absorb it. People also cannot easily prove to a caller or a bank that the 'old' and 'new' identity are the same person.
Mechanism: The authority that records the change (a registrar, ID agency or first-updating bank) issues a signed transition credential. It binds a commitment to the old attribute set to the new attribute set and states the effective date and the issuing authority, but does not reveal the old attributes to anyone who has not already seen them. A bank holding the old record verifies the credential with a zero-knowledge equality proof that its stored old attributes match the commitment. It then updates the record in place and keeps account history, mandates and credit history continuous, with no freeze. Linked systems such as the credit bureau and payee-verification name tables receive the same credential, so confirmation-of-payee and bureau matching do not fail. The customer holds the credential in a wallet and can re-present it to any later institution.
Claim core: A method comprising receiving a signed credential binding a commitment to prior identity attributes with updated identity attributes, verifying the issuer signature, verifying by a zero-knowledge proof that stored attributes of an existing customer record match the commitment, updating the record to the updated attributes while preserving account linkages, and propagating the credential to linked verification systems.
Closest prior art found:
  - [patent sim=0.747] patent:US20150280924A1 | REISSUE OF CRYPTOGRAPHIC CREDENTIALS | INTERNATIONAL BUSINESS MACHINES CORPORATION
    Effecting reissue in a data processing system of a cryptographic credential certifying a set of attributes, the credential being initially bound to a first secret key stored in a first processing device. A backup token is produced using the first device and comprises a commitment to said set of attributes and first proof data permitting verification that the set of attributes in said commitment corresponds to the set of attributes certified by said credential. At a second processing device, a second secret key is stored and blinded to produce a blinded key. A credential template token produced from the backup token and the blinded key is sent to a credential issuer where said verification is
  - [patent sim=0.743] patent:US20160269397A1 | REISSUE OF CRYPTOGRAPHIC CREDENTIALS | International Business Machines Corporation
    Effecting reissue in a data processing system of a cryptographic credential certifying a set of attributes, the credential being initially bound to a first secret key stored in a first processing device. A backup token is produced using the first device and comprises a commitment to said set of attributes and proof data permitting verification that the set of attributes in said commitment corresponds to the set of attributes certified by said credential. At a second processing device, a second secret key is stored and blinded to produce a blinded key. A credential template token produced from the backup token and the blinded key is sent to a credential issuer where said verification is perfo
  - [patent sim=0.730] patent:US20260212346A1 | System, Method, and Computer Program Product for Automatically Updating Credentials | Visa International Service Association
    Provided is a system, method, and computer program product for automatically updating credentials. The system includes at least one processor programmed or configured to receive, from a first issuer system, a migration request identifying an original account identifier, a new account identifier, and a credential request history associated with the original account identifier, analyze the credential request history to identify at least one provisioned credential associated with the original account identifier, the at least one provisioned credential including at least one of a card-on-file merchant credential and a device token, and in response to identifying the at least one provisioned cred

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

Write the answer to: runs/2026-10-05/llm_responses/judge_000.json
