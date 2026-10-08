# #4 · A2b-07 — Mixed-file splitting with consumer-held verifiable credentials

| | |
|---|---|
| **Origin** | Approach 2 scanner, theme T24 (credit-report disputes). CFPB: *"Incorrect information on your report: Information belongs to someone else"*: **895,197 complaints in 120 days**. Mixed files were about 15% of credit-reporting complaints in 2023. |
| **Domain** | Credit reporting, identity, entity resolution |
| **Scores** | final **6.61** (rank 4) · novelty 7 · utility 8 · commercial 7 · eligibility 6 |
| **Verdict** | **Pursue** (upgraded after the deep check found no prior art) |

## 1. Problem, framed technically
Bureaus build consumer files with probabilistic entity resolution (name, SSN/PAN, DOB, address). Common names, family members and synthetic identities cause **mixed files**. When a consumer says "this isn't mine", the bureau re-runs the same fuzzy matching with a note attached. The consumer's authenticated statement never becomes a **hard constraint** in the matching itself, so records re-merge on the next refresh. This is a known pattern in mixed-file litigation.

## 2. The invention
1. **Credential-bound subject identifier.** The consumer holds a verifiable credential (VC) issued after strong KYC: a bank, a government eID / mDL, or in India DigiLocker or Aadhaar-offline e-KYC. The VC carries a pairwise-pseudonymous subject ID specific to the bureau.
2. **Signed (dis)ownment assertion.** From the wallet, the consumer signs a structured assertion over tradeline and inquiry identifiers (*mine / not mine*, with reason codes). The signature uses the device-bound key linked to the VC.
3. **Constrained entity resolution.** The bureau's ER engine runs constrained clustering, for example correlation clustering or constrained agglomerative clustering, over the affected neighbourhood. There are **cannot-link** constraints between disowned records and the subject, and **must-link** constraints for owned records. These constraints persist, so future refreshes cannot re-merge.
4. **Split and route.** Disowned records form a new candidate entity. It is matched against other files: if it belongs to another real person, that person's file is corrected; if there is no match, it is flagged as possible identity theft and routed to the FCRA §605B block workflow.
5. **Abuse check: disowning real debts.** Before a cannot-link constraint is accepted, the engine can request open-banking or Account-Aggregator payment evidence. Recurring payments from the consumer's own account to the creditor of a disowned tradeline **contradict** the assertion, so the constraint is rejected and flagged. This turns "credit-repair" mass disputes into a checkable claim.
6. **Split receipt.** The consumer receives a signed record of the split and the constraints now in force.

### Technical effect / evidence
Re-merge rate after refresh, with and without persistent constraints. Precision of splits on labelled mixed-file cases. False-disownment detection rate using payment evidence.

## 3. Prior art and differences
| Reference | Discloses | Does **not** disclose |
|---|---|---|
| Finicity US20200211099A1 | Consumer-held VCs to prove creditworthiness *without* a bureau | Using VCs as constraints inside bureau entity resolution |
| Amex VC issuance/verification US12732380B2 | Multi-claim VC issuance | Credit-file splitting |
| Freddie Mac US12645641B1 | Linking loan data files with different ID attributes | Consumer-signed negative constraints |
| Mixed-file litigation and CFPB materials | The problem | A technical remedy |

## 4. Draft claims
**Claim 1.** A method comprising: receiving from a consumer device an assertion, signed with a key bound to a verifiable credential of the consumer, designating one or more records of a credit file as not belonging to the consumer; verifying the credential and signature; storing a persistent cannot-link constraint between the designated records and a subject identifier of the consumer; executing an entity-resolution process over records associated with the credit file subject to the constraint; generating a separate entity comprising the designated records; and transmitting to the consumer device a signed confirmation of the separation.
**Dependent:** retrieval of account payment data through an open-banking / account-aggregator interface and rejection of a constraint on detecting payments to the creditor of a designated record · must-link constraints for affirmed records · matching of the separate entity to another file and correction of that file · routing to an identity-theft block workflow when unmatched · a pairwise pseudonymous subject identifier per bureau · constraint persistence across batch refreshes.

## 5. Eligibility
Claim the constrained ER computation that keeps constraints in force across refreshes and the credential-bound signature verification. Avoid "a consumer disputes, the bureau removes". Medium strength. Evidence of reduced re-merge rates (a data-processing improvement) supports it.

## 6. Commercial path
US bureaus and identity-wallet providers. India: CICs plus DigiLocker and Account Aggregator integration (Sahamati ecosystem). Consumer-protection agencies may push adoption.

## 7. PoC (5 weeks)
Synthetic population generator with name collisions, then an ER baseline (Splink / Zingg), then the constrained variant. Measure re-merge rate, split precision and abuse detection.

## 8. Risks
Wallet adoption; the fallback is bank-app-embedded credentials. Adversarial disowners; mitigated by the payment-evidence check. Bureaus' reluctance to publish their ER.
