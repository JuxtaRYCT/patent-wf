# #7 · A1-04 — Cryptographic co-presence receipts from concurrent UWB ranging

| | |
|---|---|
| **Origin** | Approach 1 bisociation: *Grandmother falsely accused of bank fraud via AI facial recognition sues Fargo* (CBS) × *Concurrent Coded Signal-Multiplexing Ranging for Half-Duplex Asynchronous Networks* (arXiv 2609.33753) |
| **Domain** | Identity / card-present / corporate approvals / dispute evidence |
| **Scores** | final **6.44** · novelty 6 · utility 7 · eligibility 8 (hardware / physical-layer) |
| **Verdict** | **Refine → file narrowly** on the evidentiary-receipt and concurrent-lobby-ranging elements |

## 1. Problem, framed technically
Several bank-security questions come down to *was this person's registered device physically present?* This covers relay attacks on contactless cards, cardless-cash abuse, remote CEO fraud on approvals, and, more and more, **false accusations from biometric misidentification**. UWB secure ranging can answer that question in the moment, but **nothing keeps a verifiable record**. Ranging many phones one after another in a crowded branch lobby is also slow, because the ranging cycle grows linearly with the number of devices.

## 2. The invention
1. **Concurrent coded ranging.** Terminals (ATMs, branch tablets, POS, office anchors) use binary transmit/listen codes so that many registered phones can range at the same time within one cycle, together with IEEE 802.15.4z scrambled-timestamp-sequence secure ranging for distance bounding.
2. **Mutually signed co-presence receipt.** For each transaction the terminal's secure element and the phone's secure element both sign `{terminal_id, device_key_id, distance_upper_bound, ranging_session_id, timestamp, H(transaction)}`.
3. **Authorisation uses.** Card-present or cardless transactions require a receipt within *X* m. High-value corporate releases require approvers' receipts at office anchors.
4. **Evidentiary log with selective disclosure.** Only commitments (hashes) go to an append-only transparency log operated by the bank or a consortium. In a dispute or investigation, the device owner reveals the receipt; the verifier checks both signatures and the log inclusion proof. Absence of a matching receipt for the accused person's device, and presence of a different device's receipt, is **exculpatory evidence** independent of face recognition.
5. **Privacy.** Receipts are unlinkable without owner consent: pairwise device keys per terminal family, with only commitments logged.

### Technical effect / evidence
Lobby-scale ranging throughput (devices per second) against sequential ranging. Relay-attack rejection rate. Receipt verification cost.

## 3. Prior art and differences
| Reference | Discloses | Does **not** disclose |
|---|---|---|
| Samsung US20260203741A1 (UWB payment) | UWB-based proximity payment with signal-strength threshold messages | Mutually signed receipts, evidentiary log, concurrent multi-device ranging |
| BoA US12731184B2 | Proximity-based dual authentication of a shopping-agent representative and a customer | Receipts as evidence, UWB distance bounds |
| Verified human presence US20260238643A1 | Biometric proof of human presence in digital interactions | Physical co-presence with a terminal |
| UWB secure ranging patents (e.g. US11184153, US12245024) and 802.15.4z | Secure ranging primitives | Financial evidentiary use |

## 4. Draft claims
**Claim 1.** A method comprising: performing, by a terminal, a coded concurrent ranging exchange with a plurality of mobile devices within a ranging cycle; determining a distance upper bound for a mobile device associated with a transaction; generating a co-presence receipt comprising the distance upper bound, a time and a digest of the transaction, signed by a secure element of the terminal and by a secure element of the mobile device; conditioning authorisation of the transaction on the distance upper bound; and publishing a commitment to the receipt in an append-only log such that the receipt can later be verified against the commitment upon disclosure by the device owner.
**Dependent:** STS-based secure ranging · pairwise device keys per terminal family · office anchors for corporate approvals · receipt-based dispute adjudication · a merchant-side receipt check for cardless cash · a consent-gated disclosure protocol.

## 5. Eligibility
Strong in every jurisdiction: physical-layer ranging, secure-element signatures and log commitments.

## 6. Commercial path
ATM and POS OEMs (NCR Atleos, Diebold Nixdorf, Ingenico, PAX), handset and SE vendors, and FiRa-consortium members. Corporate banking applies it to approvals.

## 7. PoC (6–8 weeks)
Qorvo/NXP UWB dev kits, a concurrent-ranging MAC scheduler, a receipt signer on a secure element (or a TEE emulation), and a transparency log (Trillian).

## 8. Risks
UWB phone penetration: iPhone and flagship Android now, but not budget Android, which matters in India. Legal weight of receipts as evidence. Privacy perception.
