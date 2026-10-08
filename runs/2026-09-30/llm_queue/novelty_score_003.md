# TASK novelty_score_003

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2609.35662
  pool: crossdomain
  title: Dynamic Wakeup under Costly Collisions
  abstract: The wakeup problem captures a fundamental symmetry-breaking challenge among devices sharing a communication channel. We study the dynamic setting, where packets become active at arbitrary times on a time-slotted multiple access channel. In each slot, a transmission succeeds if and only if exactly one packet transmits; two or more simultaneous transmissions cause a collision. The goal is to obtain a successful transmission quickly. Prior work on wakeup has largely focused on the number of slots until the first success, referred to as the latency. However, a collision may incur substantial additional delay, represented by a per-collision cost $C$. We therefore seek to control both latency and 
- id: arxiv:2609.36236
  pool: crossdomain
  title: Maximizing Social Influence in Almost Linear Time
  abstract: Influence maximization is a central algorithmic challenge in network analysis, aiming to identify a set of $k$ seed nodes in a graph with $n$ nodes and $m$ edges that maximizes the expected cascade of information under standard diffusion models. The seminal work of Borgs, Brautbar, Chayes, and Lucier (SODA'14) yielded a fundamental breakthrough\footnote{The conference version of their paper originally claimed a runtime of $\tilde O_ε(n+m)$, but this was subsequently corrected to a runtime of $\tilde O_ε((n+m)k)$ in an updated version of the paper that is available online. We validate the necessity of this additional factor $k$ in Section~\ref{sec:lowerbound} by demonstrating that if their al
- id: arxiv:2609.22300
  pool: crossdomain
  title: The Cross-Substrate Access Assay: What an Indicator Test Must Declare to Travel from Brain to Language Model
  abstract: Testing an artificial system for a property linked to consciousness means applying a measurement developed on brains to a system that is not one. Such a transfer must re-examine five parts of the procedure: the competing statistical models, how they are fitted, the unit the inference generalizes over, the quantity the uncertainty interval is about, and the rule that turns a result into a verdict. The Cross-Substrate Access Assay declares all five. Because brain and model signals share no physical scale, every model is scored by the cross-entropy it assigns to held-out data, in nats per trial. The test case is the global neuronal workspace theory, which predicts that near threshold a stimulus
- id: arxiv:2609.38048
  pool: crossdomain
  title: A QCQP-Representable IMU Pre-Integration Factor for Certifiable State Estimation
  abstract: We propose a QCQP-representable IMU pre-integration factor that enables certifiable estimation with pre-integrated inertial measurements. To the best of our knowledge, this is the first work to directly incorporate IMU pre-integration into certifiable estimation. Inertial sensing is a common and reliable modality in robotics, and incorporating it broadens the practical scope of certifiable estimation. The main challenges are obtaining the required algebraic structure and a sufficiently tight convex relaxation. Standard IMU pre-integration relies on the exponential map, which does not admit an exact polynomial representation. Moreover, obtaining a QCQP formulation requires auxiliary lifting v
- id: arxiv:2609.00614
  pool: crossdomain
  title: BME-like Quartet Weights for Phylogenetic Trees
  abstract: Like pairwise distances, quartets can be highly redundant and correlated on a phylogenetic tree, and their number grows on the order of n^4 rather than n^2. I explore BME-like weights for reweighting quartet scores before summing them to score a full tree. Three weights are considered on an unrooted binary tree: w_ext(q)=2^(-I_ext(q)), w_int(q)=2^(-I_int(q)), and w_tot(q)=2^(-I_tot(q))=w_ext(q)w_int(q), where the exponents count specified internal nodes in the minimal connecting subtree of a quartet. Exact tree-shape counts, total quartet-weight sums, and internal-edge crossing sums are calculated for all unlabeled unrooted binary tree shapes on 6-10 taxa. For w_ext, the total quartet weight
- id: arxiv:2609.30905
  pool: crossdomain
  title: Network Analysis in Communication Research: Research Topics, Knowledge Organization, and Research Practices
  abstract: Communication network research explains access to information, patterns of participation, and the organization of public meaning through different relationships and observations. This integrative review connects research topics, knowledge organization, and research practices, using bibliographic analysis of a Web of Science candidate pool to guide selective reading. Three judgments emerge from the comparisons. First, the relevance of a connection depends on the task and the criterion of value: team members anticipate consulting colleagues whose expertise they recognize, while journalists distinguish monitoring sources, using their information, and citing them. Second, commonality at one leve
- id: pubmed:41062022
  pool: crossdomain
  title: Human papillomavirus driving cervical cancer: A mathematical model with persistent infection, cancer progression, and spontaneous remission.
  abstract: Human papillomavirus (HPV), a DNA virus, causes cervical cancer, which is the most common cancer among Japanese women in their forties. Upon infection, HPV temporarily proliferates but is usually eliminated by the immune system. However, if the virus enters the nuclei of epithelial cells, it can evade immune detection and establish a persistent infection. In this state, HPV inhibits apoptosis and allows genomic mutations to accumulate. Over many years, this can lead to dysplasia, genetic abnormalities, and eventually, invasive cancer with metastasis. While many individuals with persistent HPV infections experience spontaneous remission, a small proportion develop cervical cancer. In this stu
- id: arxiv:2609.32098
  pool: crossdomain
  title: Robust Game-theoretic Motion Planning over Extended Time Horizons
  abstract: This work presents a solution to nonconvex, game-theoretic motion planning problems subject to disturbances over long time horizons. The problem is posed as a partially-decoupled generalized Nash equilibrium problem, in which each agent's dynamics depend only on its own state and control, admitting fast solution methods for competitive multi-agent motion planning. An algorithm, WOLF, is developed that applies receding-horizon model predictive control to an open-loop differential games solver based on sequential convexification. In contrast to robust formulations that fix the uncertainty description offline, the robustness tube here is itself a dynamic state, co-optimized with the trajectory,
- id: arxiv:2609.36157
  pool: crossdomain
  title: Encoder-Sharing Hierarchical Federated Multi-Task Learning for VANETs
  abstract: Most federated learning frameworks for vehicular ad hoc networks assume that all vehicles collaboratively train a single model for a common task. This assumption limits their applicability to practical vehicular environments, where vehicles may perform heterogeneous but related perception tasks with different output spaces. This paper proposes encoder-sharing hierarchical multi-task federated learning (EN-HMTFL), which integrates cluster-based hierarchical federated learning with a globally shared encoder and vehicle-local decoders. EN-HMTFL enables vehicles performing different tasks to collaboratively learn a transferable feature representation while preserving their task-specific models l
- id: arxiv:2609.33687
  pool: crossdomain
  title: Resource-Aware Parameter-Efficient Model Adaptation for Onboard High-Dimensional Data
  abstract: Onboard satellite models often require frequent updates, but the weights adapted to earlier data distributions can quickly become outdated. However, updating large-scale model parameters in orbit presents significant challenges due to the limited uplink bandwidth of Low Earth Orbit (LEO) satellite systems, particularly for hyperspectral satellite imagery, where high-dimensional spectral-spatial inputs lead to increased model size and update costs. Existing full fine-tuning methods are thus expensive to retrain and difficult to deploy under strict communication constraints. To address this challenge, we propose NE-LoRA, a parameter-efficient adaptation framework for bandwidth-constrained onbo
- id: arxiv:2609.30472
  pool: crossdomain
  title: Moment-guided edge sampling
  abstract: Edge sampling makes local decisions to achieve graph-level objectives, such as preserving structural properties. This creates a fundamental challenge: \textit{how can the effect of a local edge edit (i.e., edge addition or removal) on global graph structure be quantified and controlled?} We address this challenge with a \textit{moment-guided edge sampling framework} based on spectral moments of the random-walk transition matrix. We compute exact moment changes through two complementary methods: a combinatorial method with closed-form updates for low-order moments, and a low-rank method that exploits \textit{locality} and \textit{cyclic trace invariance} to compress computations to edited end
- id: news:4ec6c2fd5e8a7c90
  pool: finance
  title: Saturday bank holiday: Are banks open or closed this Saturday, September 12, 2026? - The Economic Times
  abstract: Saturday bank holiday: Are banks open or closed this Saturday, September 12, 2026? The Economic Times
- id: news:06c301528ee43296
  pool: finance
  title: Trump administration cancels insurance for 760,000, alleging fraud - upi.com
  abstract: Trump administration cancels insurance for 760,000, alleging fraud upi.com
- id: news:bed8eeca800d4219
  pool: finance
  title: 3 days left to save up to $200 and make impactful connections at TechCrunch Disrupt 2026
  abstract: 3 days to save up to $200 on your TechCrunch Disrupt 2026 pass, plus 50% off a second. Make impactful connections with 10,000+ tech leaders. Last day to save is September 25 at 11:59 p.m. PT. Register today.
- id: news:4a3f4eae688fd57e
  pool: finance
  title: XRP Ledger starts carrying fund records from Brazil operator overseeing $4 trillion
  abstract: 
- id: news:1a2cd4870e5cc308
  pool: finance
  title: IPID Raises $16M Series A to Expand Global Payment Intelligence - citybiz
  abstract: IPID Raises $16M Series A to Expand Global Payment Intelligence citybiz
- id: news:ef870829fd7d3811
  pool: finance
  title: East TN woman mistakenly jailed for months after A.I. flagged her as bank fraud suspect, lawsuit says - WVLT
  abstract: East TN woman mistakenly jailed for months after A.I. flagged her as bank fraud suspect, lawsuit says WVLT
- id: news:f1a015cfc91ac455
  pool: finance
  title: ​Police Bust Army Recruitment Scam In Uttarakhand, Arrest 2 ‘Fraudsters’ ​ - etvbharat.com
  abstract: ​Police Bust Army Recruitment Scam In Uttarakhand, Arrest 2 ‘Fraudsters’ ​ etvbharat.com
- id: news:063a67665071188a
  pool: finance
  title: Apple lawsuit becomes class action
  abstract: The tech giant could face claims from thousands of card issuers that paid Apple Pay fees for payments made via Apple’s devices as part of a California lawsuit.
- id: news:6b938fbad2559306
  pool: finance
  title: KBC Launches 'Guardian Angel' to Protect 4 Million Belgian Customers from Fraud - FF News
  abstract: KBC Launches 'Guardian Angel' to Protect 4 Million Belgian Customers from Fraud FF News
- id: news:5bdc455cceb76626
  pool: finance
  title: North Dakota veterans targeted as scams get smarter - bignewsnetwork.com
  abstract: North Dakota veterans targeted as scams get smarter bignewsnetwork.com
- id: news:901a4387f423d0d2
  pool: finance
  title: Lloyds Bank’s new free £200 offer has an easy-to-miss direct debit rule that rules you out - LADbible
  abstract: Lloyds Bank’s new free £200 offer has an easy-to-miss direct debit rule that rules you out LADbible
- id: news:ca45d135c9b229d3
  pool: finance
  title: Deutsche Bank upgrades Astrazeneca to 'hold' - Sharecast.com
  abstract: Deutsche Bank upgrades Astrazeneca to 'hold' Sharecast.com
- id: news:3d0f7309baad0014
  pool: finance
  title: MoonPay Expands into APAC with MoonPay Korea and Major Banking Partnerships - FF News
  abstract: MoonPay Expands into APAC with MoonPay Korea and Major Banking Partnerships FF News
- id: news:3c4a723e5216b0b6
  pool: finance
  title: Keralam Police warn of fake hospital appointment apps used in financial fraud - ThePrint
  abstract: Keralam Police warn of fake hospital appointment apps used in financial fraud ThePrint
- id: news:3d4eb6b0e24f37c1
  pool: finance
  title: One of Tether’s Bank Partners Caught Up in Assets Seizure - The Information
  abstract: One of Tether’s Bank Partners Caught Up in Assets Seizure The Information
- id: news:cc3156e2e80b9214
  pool: finance
  title: Barclays to open new branches in UK as it gives major update - Wales Online
  abstract: Barclays to open new branches in UK as it gives major update Wales Online
- id: news:7b206fca21e31dfe
  pool: finance
  title: Husch Blackwell Adds Cross River Bank Fintech Lawyer Subramanian - Bloomberg Law News
  abstract: Husch Blackwell Adds Cross River Bank Fintech Lawyer Subramanian Bloomberg Law News
- id: news:9fdad6db0e35ae4b
  pool: finance
  title: LendingPoint Drove Coastal's $42M Q2 Loss
  abstract: OCC's Brutal Denial of bunq's Application: What Can Other Charter Hopefuls Learn?
- id: news:ecd7907644b315a6
  pool: finance
  title: [Snapdragon Summit] Qualcomm, Mastercard Announce Agentic Commerce Partnership - thelec.net
  abstract: [Snapdragon Summit] Qualcomm, Mastercard Announce Agentic Commerce Partnership thelec.net

## OUTPUT JSON SCHEMA
```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "scores"
 ],
 "properties": {
  "scores": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "id",
     "novelty",
     "usefulness",
     "mechanism_or_problem",
     "tags"
    ],
    "properties": {
     "id": {
      "type": "string"
     },
     "novelty": {
      "type": "integer",
      "description": "1-10 novelty of the core idea"
     },
     "usefulness": {
      "type": "integer",
      "description": "1-10 value as input for finance inventions"
     },
     "mechanism_or_problem": {
      "type": "string",
      "description": "<=30 words"
     },
     "tags": {
      "type": "array",
      "items": {
       "type": "string"
      }
     }
    }
   }
  }
 }
}
```

Write the answer to: runs/2026-09-30/llm_responses/novelty_score_003.json
