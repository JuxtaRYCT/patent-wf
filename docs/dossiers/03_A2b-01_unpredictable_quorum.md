# #3 · A2b-01 — Unpredictable-quorum confirmation for out-of-topology treasury instructions

| | |
|---|---|
| **Origin** | Approach 2 scanner, theme T14, top opportunity (2.09; whitespace +1.12; 0 KB patents near centroid). Signal: *"Scammers used an AI voice clone and a fake WhatsApp message to move €95 million out of an Italian bank"* (Sept 2026, €53M recovered). |
| **Domain** | Corporate/treasury payments, BEC and deepfake-executive fraud |
| **Scores** | final **6.94** (rank 3) · novelty 7 · utility 8 · feasibility 8 · length-controlled max patent sim 0.685 (distinct band) |
| **Verdict** | **Pursue.** Survived the stage-2 deep check |

## 1. Problem, framed technically
Dual control and call-backs use **fixed, publicly inferable approvers**, and a call-back can be steered to an attacker-controlled channel. A voice-clone attacker scripts the impersonation of the one or two people they know must approve. The attack succeeds because the *set of verifiers is predictable* and *verification rides the same channel family as the instruction*.

## 2. The invention
1. **Instruction-topology model.** For each corporate client the bank learns a directed multigraph of historical instruction paths: (instructing role, channel, approval sequence, beneficiary class, corridor, amount band). A smoothed path model assigns a novelty score to each new instruction; the score is high for a first-time overseas corridor, a voice or messaging origin, or a skipped usual channel.
2. **Risk-sized quorum.** For novel paths, *k* (the number of co-approvers) is a function of amount × novelty.
3. **Verifiable random co-approver draw.** The bank computes `VRF(sk_bank, H(instruction) ‖ epoch)` and uses the output to select *k* co-approvers from the client's authorised signatory list. The instructing person and anyone contacted through the originating channel are excluded. The VRF proof is logged, so the client's auditors can verify afterwards that the selection was not manipulated. This also defeats a bank insider trying to route approval to an accomplice.
4. **Bank-initiated channel binding.** Selected co-approvers are contacted only through bank-initiated channels on **enrolled devices**: an in-app push requiring a FIDO2/passkey signature over a what-you-see-is-what-you-sign rendering of the instruction digest. The channel the instruction arrived on is never used.
5. **Release rule.** Funds are released only after *k* valid signatures; on timeout the instruction is held and the client's security contact is alerted.

**Why it works:** the attacker must compromise *unpredictable* additional people's enrolled devices *in real time*, which is a qualitatively harder problem than scripting one impersonation.

### Technical effect / evidence
Simulated attack success probability against *k* and the signatory-pool size. Added latency for legitimate instructions (most paths are familiar, so no quorum is needed). An audit-verification cost benchmark for the VRF proofs.

## 3. Prior art and differences
| Reference | Discloses | Does **not** disclose |
|---|---|---|
| PayPal "Dual controls" US11244314B2 / US20210319442A1 | A dual-control workflow layer over single-control systems | Random, VRF-auditable approver selection; a topology-novelty trigger; exclusion of the originating channel |
| BEC guidance (Bill.com, Cyfox, industry FAQs) | Dual approval, call-backs to known numbers | An unpredictable verifier set |
| Blockaid cosigning US12682339B1 | Transaction cosigning for multisig wallets | Corporate instruction topology, random signer draws |
| Secure Purchase virtual-card rotation US20260289570A1 | Credential rotation | Unrelated |

## 4. Draft claims
**Claim 1.** A method comprising: maintaining, for an organisation, a model of historical payment-instruction paths comprising instructing roles, channels, approval sequences and beneficiary classes; computing a novelty score for a received instruction relative to the model; when the novelty score exceeds a threshold, computing a verifiable random function output over a digest of the instruction and selecting a plurality of co-approvers from authorised signatories of the organisation according to the output, excluding an instructing party and parties associated with the channel of the instruction; transmitting, via bank-initiated channels to devices enrolled to the selected co-approvers, requests for cryptographic signatures over a rendering of the instruction; and releasing the instruction only upon receipt of valid signatures from the selected co-approvers.
**Dependent:** *k* determined from amount and novelty · storage of the VRF proof for third-party audit · a FIDO2 assertion bound to the instruction digest · time-boxed hold with escalation · re-draw on unavailability, with the re-draw logged · exclusion of signatories whose devices changed within N days · extension to vendor bank-detail change requests.

## 5. Eligibility
Claim the cryptographic selection (VRF), the device-bound signature protocol and the channel-separation logic. These are security-protocol improvements, not a business rule ("ask more people"). This framing holds up well under US, IN and EP law.

## 6. Commercial path
Corporate internet-banking platforms (Finacle, TCS BaNCS, Temenos, FIS), treasury management systems (Kyriba), and banks' corporate channels. India fits naturally, since maker-checker is already mandatory and this raises it to a verifiable-random checker.

## 7. PoC (3–4 weeks)
Instruction-path model on synthetic corporate logs, a VRF library (ECVRF, RFC 9381), a passkey approval flow, and an attack simulation.

## 8. Risks
Approver availability, handled by a larger pool and fallbacks. Some small firms have only 2 signatories: fall back to bank-side verification with a delay. Client education.
