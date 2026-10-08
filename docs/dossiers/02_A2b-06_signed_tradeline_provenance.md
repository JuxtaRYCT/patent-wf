# #2 · A2b-06 — Signed tradeline provenance: credit-report disputes resolved by cryptographic record comparison

| | |
|---|---|
| **Origin** | Approach 2 scanner, theme T24 (opportunity 1.31, whitespace +1.12). CFPB signal: *"Problem with a company's investigation into an existing problem"* — 468,136 complaints in 120 days; sub-issue *"Investigation took more than 30 days"* 238,472 complaints, **share lift 1.41×**; *"Their investigation did not fix an error"* 207,417 |
| **Domain** | Credit reporting / regtech (US FCRA; India CICRA + RBI CIC directions) |
| **Scores** | final **7.05** (rank 2) · novelty 7 · utility 9 · commercial 8 · eligibility 7 · length-controlled max patent sim 0.719 |
| **Verdict** | **Pursue.** Survived the stage-2 deep check |

## 1. Problem, framed technically
Dispute reinvestigation between bureaus and furnishers runs over coded messages (e-OSCAR ACDV/AUD). The bureau cannot verify that the furnisher actually checked its source-of-truth record, so "verified as reported" answers are unverifiable. Regulators have criticised this "parroting". Investigations miss the 30-day window at growing rates. There is no machine-checkable link from a reported field back to the source record it came from.

## 2. The invention
### 2.1 Core mechanism
1. **Provenance envelope per reported field group.** When furnishing (Metro 2 base segment: account status, balance, date of first delinquency, payment-history profile), the furnisher attaches `{furnisher_id, source_system_id, record_locator = H(internal_account_key ‖ version), field_hash = H(value ‖ salt), source_record_root = Merkle root of the canonicalised source record snapshot, timestamp, signature}`. The bureau stores envelopes append-only with each tradeline version.
2. **Provenance challenge.** A consumer dispute of field *f* on version *v* triggers an automatic challenge to the furnisher's endpoint: "produce the source-record fields supporting *f*@*v*".
3. **Selective-disclosure response.** The furnisher returns the relevant source-record fields with Merkle inclusion proofs against `source_record_root`. It does not need to send the whole record.
4. **Deterministic adjudication.** The dispute engine verifies the signature, the inclusion proofs, and the **derivation rules** (for example, date of first delinquency must follow from the payment-history fields; the reported balance must equal the source balance at the as-of date). The outcomes are:
   - *verified*: the consumer receives an evidentiary receipt listing which source fields support the value;
   - *corrected*: on mismatch, the reported value is replaced automatically with the proven source value;
   - *suppressed*: with no valid proof inside the SLA timer, the field is suppressed instead of defaulting to "verified".
5. **Status streaming.** Each state transition is pushed to the consumer, which addresses the "was not notified of investigation status" sub-issue (12,791 complaints).

### 2.2 Components
Furnisher-side envelope signer (HSM key per furnisher) · canonicalisation and Merkle builder · bureau envelope store (append-only, versioned) · challenge API · derivation-rule verifier · SLA timer and auto-suppression · consumer receipt service.

### 2.3 Technical effect / evidence to generate
Fraction of disputes resolved without human handling. Median resolution time against e-OSCAR baselines. Error rate in "verified" outcomes, which is measurable because proofs are auditable. Payload size of selective disclosure compared with full-record exchange.

## 3. Prior art and differences
| Reference | Discloses | Does **not** disclose |
|---|---|---|
| State Farm US11893634B2 / US11232518B1 | ML models to detect and correct errors in Metro 2 data | Signed field-level provenance, a challenge-response protocol, automatic suppression on proof failure |
| Bridgeforce US20250094408A1 | Conformance checking of data values against protocols | Cryptographic binding to source records |
| Finicity US20200211099A1 | Consumer-held verifiable credentials to *bypass* bureaus | Bureau-furnisher dispute provenance |
| Amex "Tradeline fingerprint" US11276115B1 | Linking tradelines to signers/co-signers | Provenance or dispute adjudication |
| e-OSCAR / Metro 2 tooling | Coded dispute exchange and format validation | Verifiable evidence of source-record checks |

## 4. Draft claims
**Claim 1.** A method comprising: receiving, from a data furnisher, a tradeline data field and a provenance record comprising a digital signature over a hash of the field value and a commitment to a source record from which the field was derived; storing the provenance record in association with a version of the tradeline; upon receiving a dispute of the field, transmitting a challenge identifying the version and field; receiving a response comprising source-record elements and inclusion proofs against the commitment; verifying the signature, the inclusion proofs and a derivation rule relating the source-record elements to the field value; and automatically (i) confirming the field and generating a receipt identifying the supporting elements, (ii) replacing the field with a value derived from the source-record elements upon mismatch, or (iii) suppressing the field upon failure to receive a verifiable response within a time limit.
**Dependent:** Merkle commitment over a canonicalised source record · derivation rules for date of first delinquency, balance and payment-history profile · per-furnisher HSM keys with rotation · consumer notification at each state transition · selective disclosure that reveals only the supporting elements · linkage to the entity-resolution split of dossier #4 for "belongs to someone else" disputes · an audit export for supervisors.

## 5. Eligibility
This is data-integrity and verification between independent computer systems (cryptographic commitments, selective disclosure, deterministic verification). It resembles improvements to data-exchange protocols that are routinely eligible, so avoid claiming "resolving disputes" in the abstract. For India, frame it as a technical improvement to the data-exchange system between credit institutions and CICs.

## 6. Commercial path
- **US:** the three bureaus, the largest furnishers (card issuers, auto lenders, servicers) and the e-OSCAR operator. Regulatory tailwind: CFPB scrutiny of reinvestigation.
- **India:** CICs (TransUnion CIBIL, Experian, Equifax, CRIF High Mark) and banks. RBI circular **RBI/2023-24/72** (26 Oct 2023, effective 26 Apr 2024) makes credit institutions and CICs pay **₹100 per day** of delay beyond 30 days (21 days for the CI and 9 for the CIC). In **August 2026 RBI penalised TransUnion CIBIL (₹26.8 lakh), CRIF High Mark and Equifax** for non-compliance, so dispute latency is now a direct, enforced cost. ([CIBIL framework](https://www.cibil.com/framework-for-compensation), [Fox Mandal](https://foxmandal.in/News/rbi-releases-compensation-framework-for-delay-in-updating-credit-information/), [Aug 2026 penalties](https://www.indianpaycalculator.in/govt-news/rbi-fines-credit-bureaus-cibil-equifax-100-per-day-rule-2026))

## 7. PoC plan (4–6 weeks)
Synthetic Metro 2 generator, then the envelope signer, then the dispute engine with derivation rules. Simulate furnisher response latencies and error injection. Measure automated resolution rate and time, and correctness of corrections.

## 8. Risks
Furnisher adoption, since this needs a standard (CDIA / Metro 2 extension or RBI/CIC data format). Key management at small furnishers can be handled through a hosted signing service. Legal effect of auto-suppression needs a regulatory safe harbour.
