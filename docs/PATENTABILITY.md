# Making finance ideas patent-eligible — drafting playbook

Finance is where software patents die most often. Alice itself was a bank-settlement case. Every idea in this repository was therefore generated and judged with an **eligibility-first** rule: *the inventive step must sit in the technical layer.* This playbook is what the examiner-judge prompt enforces, and it is what the dossiers follow.

> Not legal advice. Use this to prepare invention disclosures for a registered patent attorney or agent (US: USPTO-registered practitioner; India: registered patent agent).

## 1. The one-line test per jurisdiction

| Jurisdiction | Question the examiner asks | Pass pattern |
|---|---|---|
| **US** (§101, Alice/Mayo + USPTO guidance; *Ex parte Desjardins*, precedential Nov 2025) | Is the claim *directed to* an abstract idea (fundamental economic practice, mental process, math)? If so, does it integrate it into a **practical application** that improves a computer or another technology? | The claim recites a specific technical improvement: lower latency, fewer messages, less memory, a stronger cryptographic guarantee, better sensor accuracy, better model training behaviour. |
| **India** (§3(k), CRI Guidelines 2025) | Is it a business method, algorithm or computer program *per se*? Is there a **technical effect / technical contribution**? | It improves the **functioning of a technical system**, not only the quality of an informational output such as a score or recommendation. |
| **EPO** (Art. 52, COMVIK, G 1/19) | Which features contribute to technical character? Is the inventive step in *those* features? | The non-obvious part is technical: a protocol, signal processing, a security mechanism or a resource-usage improvement. |

## 2. Ten drafting rules we applied to every idea

1. **Lead with the technical problem, not the business problem.** Write "authorisation messages cannot carry verifiable constraints on an autonomous agent", not "customers overspend".
2. **Put a device, protocol or data structure in claim 1.** Name the concrete element: a secure enclave, a message field, a hash chain, a sensor, a model architecture, a queue discipline.
3. **State the measurable technical effect** (latency, bandwidth, false-positive rate at a fixed recall, memory, energy, attack resistance) and keep benchmark data ready. Since Dec 2025 USPTO formally weighs **Subject Matter Eligibility Declarations** (37 CFR 1.132 evidence).
4. **Avoid "determining a risk score and approving/declining"** as the point of novelty. That is the Alice fact pattern. The novelty must sit upstream (how the signal is produced or secured) or downstream (how the network or protocol behaves).
5. **Claim the ML improvement itself** where there is one (Desjardins): training procedure, architecture, update rule, drift handling. "Apply ML to fraud" is not enough.
6. **Use system and CRM (computer-readable medium) claims alongside method claims.** Each should recite the hardware interaction, not just "a processor".
7. **For cryptographic ideas**, claim the protocol messages and what each party can verify. These usually clear §101 and §3(k).
8. **For sensor or physical-world ideas** (acoustic, RF, IoT, device telemetry), claim the signal acquisition and processing chain. These are the strongest eligibility cases.
9. **Keep dependent claims as fallback positions** that each add a technical limitation, such as a specific window size, a specific cryptographic primitive or a specific hardware location.
10. **Search before drafting.** Every dossier lists the closest US prior art from USPTO full text. The claim is drafted *around* those documents, and the differences are stated explicitly.

## 3. Prior-art hygiene for AI-generated ideas

Research shows about **24% of LLM "novel" research ideas are unacknowledged paraphrases of existing work** (Gupta & Pruthi, ACL 2025). Before any idea here goes to counsel:
- read the top 3 prior-art hits in `runs/<date>/prior_art.json` in full (claims, not just abstracts);
- search Google Patents / Espacenet / InPASS (India) for non-US families, since this run's automatic search covers US full text plus literature;
- check standards bodies (EMVCo, ISO 20022, W3C, FIDO, IETF), regulator proposals (RBI, NPCI circulars, FCA, EBA) and product announcements. Regulation and product launches count as prior art: for example, RBI's April 2026 proposal of a 1-hour cancellable delay for >₹10k transfers.

## 4. Filing strategy notes
- **Provisional first** (US provisional / Indian provisional specification). This secures the date for 12 months while the proof-of-concept runs, which addresses the ideation–execution gap.
- **PCT** for ideas with a global network angle (card networks, stablecoin rails, agentic protocols).
- **Defensive publication** for ideas judged "refine" that are strategically useful but unlikely to be granted. It prevents competitors from patenting them.
