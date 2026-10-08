# Research brief — the evidence behind the pipeline design

Date: 2026-09-30. Everything below was checked against sources on this date; links at the end of each section.

---

## 1. Does AI-generated ideation actually produce *novel* ideas?

This question decides whether Approach 2 ("AI Opportunity Scanner") works on its own. The published evidence is mixed. It says an LLM needs retrieval and prior-art checking wrapped around it, not that it should be trusted directly.

| Study | What they did | Finding relevant to us |
|---|---|---|
| **Si, Yang & Hashimoto (2024)**, *Can LLMs Generate Novel Research Ideas?* (ICLR 2025) | 100+ NLP researchers blind-reviewed LLM ideas vs expert ideas | LLM ideas were rated **more novel** (5.64 vs 4.84 / 10, p<0.05) but slightly **less feasible**. They also found **LLM self-evaluation fails** and **generations lack diversity**. When you generate many ideas, a large fraction are duplicates. |
| **Si, Hashimoto & Yang (2025)**, *The Ideation–Execution Gap* (ICLR 2026) | 43 experts spent 100+ h each executing randomly assigned LLM vs human ideas | After execution, LLM-idea scores **fell significantly more** on every metric (novelty, excitement, effectiveness). Rankings **flipped** on several metrics. Ideas that "sound novel" on paper can fail when built. |
| **Gupta & Pruthi (2025)**, *All That Glitters is Not Novel* (ACL 2025, Outstanding Paper) | 13 experts hunted for sources of LLM-generated research proposals | **24%** were paraphrased or heavily borrowed from existing work, with a 1-to-1 methodological mapping. Another **32%** partially overlapped with prior work. Standard plagiarism detectors **did not catch them**. So an "AI opportunity scanner" can hand you someone else's idea without saying so. |
| **Doshi & Hauser (2024)**, *Science Advances* | Writers with and without GenAI ideas | GenAI raises each person's creativity but **reduces collective diversity**, because outputs converge on the model's modes. If every bank asks an LLM for "novel fintech ideas", they get the same ideas. |
| **Wang et al. — SciMON (ACL 2024)** | Literature-grounded idea generation with explicit novelty optimisation | Plain GPT-4 ideas had **low technical depth and novelty**. **Retrieving inspirations and iterating against prior papers** partly fixed this. This supports Approach 1's design. |
| **Novelty checkers (2025)**: Idea Novelty Checker (retrieve → rerank → facet-based LLM judgement), RAG-Novelty, SchNovel, RINoBench | Automated novelty assessment | Retrieval-grounded checking beats a bare LLM judgement by about 13% agreement with experts. A novelty verdict is only as good as the prior art you retrieved. |
| **Kelly, Papanikolaou, Seru & Taddy (2021)**, *AER: Insights* | 9M US patents, TF-IDF text similarity | Defines a significant patent as one **dissimilar to prior patents** (novel) and **similar to later ones** (impactful). This is the basis of our embedding + lexical novelty score. |
| **Swanson (1986) → LBD surveys (2025)** | Literature-based discovery, ABC model | A–B and B–C links exist in separate literatures while A–C is unpublished. That gap is the classic mechanism for cross-domain discovery, and it is what Approach 1 step 3 automates. |

**What this means for the design**

1. **Never accept an LLM's own claim that an idea is novel.** Every idea from every arm goes through the same external prior-art check: USPTO full text, a local patent KB and Semantic Scholar.
2. **Measure diversity directly** (Vendi score, cross-arm similarity), because the known failure is mode collapse.
3. **Ground generation in fresh, specific inputs.** New papers, complaint trends and regulations push the model off its default modes. This is the difference between arms A2b / A1 and the zero-shot arm A2a.
4. **Treat "novel on paper" as provisional.** The ideation–execution gap means the top ideas need a feasibility pass before filing: claim drafting and a proof-of-concept path.

Sources: [Si et al. 2024](https://arxiv.org/abs/2409.04109) · [Si et al. 2025](https://arxiv.org/abs/2506.20803) · [Gupta & Pruthi 2025](https://aclanthology.org/2025.acl-long.1249) · [Doshi & Hauser 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532) · [SciMON](https://arxiv.org/abs/2305.14259) · [Idea Novelty Checker](https://arxiv.org/html/2506.22026v1) · [RAG-Novelty / SchNovel](https://arxiv.org/html/2409.16605v1) · [Kelly et al.](https://www.nber.org/papers/w25266) · [LBD survey 2025](https://arxiv.org/pdf/2506.12385)

---

## 2. Can banking/finance ideas be patented? (state of the law, Sept 2026)

Finance is the hardest field for software patents. The ideas therefore have to be **engineered for eligibility**: each needs a concrete technical mechanism that improves how a computer, network, sensor or cryptographic system works, not a better way to decide who gets a loan.

### United States
- **Alice Corp. v. CLS Bank (2014)** is a banking case: an intermediated-settlement *method* is an abstract idea. "Fundamental economic practices" (hedging, escrow, credit decisions, risk scoring) are abstract on their own.
- **USPTO Aug 4 2025 memo** ("Reminders on evaluating subject matter eligibility") tells examiners not to over-reject, and to treat as eligible claims that recite an improvement to computer functionality or another technology.
- **Ex parte Desjardins** (Appeals Review Panel under Director Squires, Sept 2025; **precedential Nov 2025**): ML claims that improve how the model itself operates are eligible. Examples are reduced complexity, better multi-task learning and avoiding catastrophic forgetting. MPEP updated in Dec 2025.
- **Dec 2025 memos on Subject Matter Eligibility Declarations (SMEDs, 37 CFR 1.132)**: applicants can file **technical evidence** (benchmarks, latency, memory, false-positive rates) to overcome §101 rejections.
- ⇒ Drafting rule: claim the **system-level technical effect** (fewer messages, lower latency, lower memory use, stronger cryptographic guarantee, a sensor-fusion result). Keep benchmark data ready for a SMED.

### India (relevant: Indian applicant, RBI/NPCI context)
- **Patents Act §3(k)** excludes mathematical and business methods and computer programs *per se*.
- **CRI Guidelines 2025** (issued 29 Jul 2025, 62 pp + 73-pp annexure of examples) test for **technical effect / technical contribution**. An invention that **improves the functioning of a technical system can qualify; one that only produces a better informational output generally cannot.** The guidelines include specific sections on AI/ML, blockchain and quantum. Courts: *Ferid Allani* (Delhi HC 2019) and *Microsoft v. Asst. Controller* (Delhi HC 2023) read "per se" narrowly.
- ⇒ Frame each claim as a technical system: a device, a protocol or a hardware-software combination with a measurable technical effect.

### Europe (EPO)
- "Any hardware" gets past Art. 52, but under **COMVIK** only features that contribute to technical character count for inventive step. A new business rule implemented on a computer is not inventive. **G 1/19** confirms that simulations and other computer-implemented processes need a technical effect beyond ordinary computer operation.
- ⇒ The same drafting rule: the inventive step has to sit in the technical layer.

Sources: [Desjardins coverage (Bloomberg Law)](https://news.bloomberglaw.com/ip-law/ai-patent-eligibility-has-shifted-with-one-machine-learning-case) · [USPTO SME page](https://www.uspto.gov/patents/laws/examination-policy/subject-matter-eligibility) · [USPTO Aug 2025 memo](https://www.uspto.gov/sites/default/files/documents/memo-101-20250804.pdf) · [Venable: §101 reset for 2026](https://www.venable.com/insights/publications/2025/12/the-101-reset-for-2026) · [SMED guidance](https://www.patentnext.com/2026/01/uspto-issues-guidance-on-subject-matter-eligibility-declarations-smed/) · [India CRI Guidelines 2025 analysis](https://conventuslaw.com/report/india-a-detailed-analysis-of-indias-new-cri-guidelines-2025/) · [SFLC.in on CRI 2025](https://sflc.in/?p=13592)

---

## 3. Where banking is moving (demand side, Sept 2026)

| Vector | Status (verified) | Why it creates patent space |
|---|---|---|
| **Agentic payments** | Mastercard Agent Pay (Apr 2025, "Agentic Tokens"; *Agent Pay for Machines* Jun 2026), Visa Intelligent Commerce Connect (Apr 2026, live in OpenAI experiences since Jun 2026), Google AP2 and Stripe tooling (2025). IMF Note 2026/004 on agentic payments. | **Liability after an agent's mistake is unresolved** once a dispute goes beyond plain fraud (wrong item, wrong dates). A fourth party, the agent, has entered the four-party model. |
| **Stablecoins / tokenized deposits** | GENIUS Act (Jul 2025). Treasury NPRM on issuance (18 Aug 2026), Fed proposals (29 Sep 2026), FDIC proposal. Effective **Jan 2027**. 1:1 reserves, redemption at par within 2 business days, no retail yield. FDIC: tokenized deposits = deposits. | Redemption, reserve attestation, bank-to-chain interoperability and run dynamics all need new infrastructure before Jan 2027. |
| **Fraud** | APP scams are the dominant cross-border fraud pattern (BIS CPMI 2026). Deepfake fraud up >700%. UK: 207k mule accounts flagged (+22%). India: cyber fraud cases rose from 2.6 lakh (2021) to ~28 lakh (2025), ₹22,931 cr. RBI MuleHunter.AI is live at 29 banks. RBI proposals (Apr 2026): **1-hour delay with payer cancel for transfers >₹10k** and **trusted-person approval for seniors' high-value payments**. | Regulators are now mandating friction. The patent space is in doing it with **less friction and fewer false positives**, not in the friction itself, which is now prior art via regulation. |
| **Credit reporting disputes** (CFPB data, this run) | 2.3M complaints in 120 days about credit reporting. The "investigation took >30 days" sub-issue grew **1.41× in share** (238k complaints). | The dispute pipeline is overwhelmed, largely by templated or automated disputes. The need is technical triage, provenance and verification. |
| **Post-quantum** | NIST FIPS 203/204/205 (Aug 2024). Banks are in crypto-inventory and migration phases. | Migration orchestration and hybrid signatures in payment messaging (ISO 20022, EMV) are still immature. |

Sources: [Mastercard Agent Pay](https://www.mastercard.com/global/en/business/artificial-intelligence/mastercard-agent-pay.html) · [Agent Pay for Machines](https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html) · [Worldpay: agentic liability](https://www.worldpay.com/en/insights/articles/agentic-commerce-liability-is-still-being-written) · [IMF Note 2026/004](https://www.elibrary.imf.org/view/journals/068/2026/004/article-A001-en.xml) · [FDIC GENIUS proposal](https://www.fdic.gov/news/press-releases/2026/fdic-approves-proposal-implement-genius-act-requirements-and-standards) · [GENIUS one year on](https://tazapay.com/blog/genius-act-one-year-later-stablecoin-rules-2026) · [RBI safeguards Apr 2026](https://visionias.in/current-affairs/news-today/2026-04-11/economy/rbi-proposes-new-safeguards-to-curb-rising-digital-payment-frauds) · [NPCI AI fraud](https://www.eweek.com/news/npci-ai-payments-fraud-rules-apac-india/) · [Mule/APP 2026](https://amlwatcher.com/blog/money-mule-detection-app-fraud-aml/) · [FRBS 2026 risk officer survey](https://www.frbservices.org/binaries/content/assets/crsocms/news/research/2026-risk-officer-survey.pdf)

---

## 4. Existing "AI opportunity scanner" tools (what Approach 2 competes with)

Commercial tools include PatSnap Eureka (agentic whitespace exploration), IPRally, Cypris, PatSeer, XLSCOUT and Project PQ. They map **patent whitespace**: areas where few patents exist. They do not check that the whitespace has **demand**, and most do not generate cross-domain mechanisms. A patent desert can simply be an area nobody needs. Our A2b scanner adds demand signals (complaints, regulation, news momentum) and technology readiness (fresh papers) to the whitespace measure. A1 adds cross-domain mechanisms the landscape tools never see.

Sources: [PatSnap whitespace](https://www.patsnap.com/resources/blog/articles/ai-white-space-identification-for-patent-strategy/) · [XLSCOUT](https://xlscout.ai/how-rd-teams-use-ai-to-identify-patent-whitespace-before-filing/) · [Solve Intelligence tool round-up](https://www.solveintelligence.com/blog-posts/top-patent-analysis-tools)
