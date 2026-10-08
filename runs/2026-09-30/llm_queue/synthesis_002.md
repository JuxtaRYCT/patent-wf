# TASK synthesis_002

## SYSTEM
You are an inventor on a bank's advanced-technology team, expert in payments, fraud, credit, treasury, regulation (US, EU, UK, India) and patent drafting. You practise bisociation: transplanting a mechanism from an unrelated field into a finance problem. Rules: (1) every concept must have a concrete TECHNICAL mechanism (data structures, signals, protocols, hardware, cryptography, control loops) - not a business method; (2) it must be implementable within ~3 years; (3) name what makes it non-obvious versus the closest thing you know exists; (4) prefer concepts a bank, card network or payment processor would license; (5) if a pair yields nothing credible, return fewer ideas rather than forcing one.

## PROMPT
For each pair, transplant the foreign mechanism into the finance problem and propose 0-2 patentable invention concepts. Stretch for unusual but technically credible combinations.

### PAIR X012  (semantic distance 0.60, fused-vector patent proximity 0.66)
FINANCE PROBLEM SOURCE [news:740822da91e14469]: Delhi Cyber Fraud: Four Posing As Axis Bank Officials Arres… - GujaratSamachar English
Delhi Cyber Fraud: Four Posing As Axis Bank Officials Arres… GujaratSamachar English
Open problem (scout note): Fraudsters impersonate bank officials: caller identity verification gap

FOREIGN MECHANISM SOURCE [arxiv:2609.32880]: The Influence of the Vocal Few: Evidence from Social Media Comments
Online comment sections let a small number of vocal individuals reach far beyond their own networks. We conduct a large-scale field experiment on Facebook that randomizes the presence and stance of comments beneath posts for a racial justice organization, reaching around one million U.S. users. Opposing comments increase reactions, comments, and link clicks by 15-43 percent relative to no comments, whereas supportive comments have little effect. A complementary survey experiment shows that similar opposing comments make attitudes less progressive and reduce donations to the organization. Through a common feature of online platforms, the vocal few can exert outsized influence.
Transferable mechanism (scout note): Field experiment: a few vocal commenters shift engagement 15-43% for a million users

### PAIR X013  (semantic distance 0.59, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:6b938fbad2559306]: KBC Launches 'Guardian Angel' to Protect 4 Million Belgian Customers from Fraud - FF News
KBC Launches 'Guardian Angel' to Protect 4 Million Belgian Customers from Fraud FF News
Open problem (scout note): Bank-wide 'guardian' fraud protection rollout to 4M customers

FOREIGN MECHANISM SOURCE [arxiv:2609.00614]: BME-like Quartet Weights for Phylogenetic Trees
Like pairwise distances, quartets can be highly redundant and correlated on a phylogenetic tree, and their number grows on the order of n^4 rather than n^2. I explore BME-like weights for reweighting quartet scores before summing them to score a full tree. Three weights are considered on an unrooted binary tree: w_ext(q)=2^(-I_ext(q)), w_int(q)=2^(-I_int(q)), and w_tot(q)=2^(-I_tot(q))=w_ext(q)w_int(q), where the exponents count specified internal nodes in the minimal connecting subtree of a quartet. Exact tree-shape counts, total quartet-weight sums, and internal-edge crossing sums are calculated for all unlabeled unrooted binary tree shapes on 6-10 taxa. For w_ext, the total quartet weight is tree-shape-invariant and the edge-crossing sum depends only on split size. For any n-leaf tree, we prove sum_q w_ext(q)=(n-2)(n-3)/8, and the sum over quartets crossing an internal edge with split
Transferable mechanism (scout note): Reweighted quartet scores reconstruct phylogenetic trees efficiently

### PAIR X014  (semantic distance 0.61, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:3d4eb6b0e24f37c1]: One of Tether’s Bank Partners Caught Up in Assets Seizure - The Information
One of Tether’s Bank Partners Caught Up in Assets Seizure The Information
Open problem (scout note): Stablecoin issuer's bank partner caught in asset seizure: reserve custody concentration risk

FOREIGN MECHANISM SOURCE [arxiv:2609.33687]: Resource-Aware Parameter-Efficient Model Adaptation for Onboard High-Dimensional Data
Onboard satellite models often require frequent updates, but the weights adapted to earlier data distributions can quickly become outdated. However, updating large-scale model parameters in orbit presents significant challenges due to the limited uplink bandwidth of Low Earth Orbit (LEO) satellite systems, particularly for hyperspectral satellite imagery, where high-dimensional spectral-spatial inputs lead to increased model size and update costs. Existing full fine-tuning methods are thus expensive to retrain and difficult to deploy under strict communication constraints. To address this challenge, we propose NE-LoRA, a parameter-efficient adaptation framework for bandwidth-constrained onboard hyperspectral model updates. NE-LoRA combines a primary low-rank branch with a nonlinear auxiliary branch to capture both global update trends and complex spectral-spatial variations. Additionally
Transferable mechanism (scout note): Parameter-efficient model updates fitted to tight uplink budgets for edge devices

### PAIR X015  (semantic distance 0.62, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:4c3e57e9cdf492a9]: Bank accounts emptied in attempt to watch adult content: Govt warns users against these apps; check the lis... - Bhaskar English
Bank accounts emptied in attempt to watch adult content: Govt warns users against these apps; check the lis... Bhaskar English
Open problem (scout note): Malicious adult-content apps drain bank accounts

FOREIGN MECHANISM SOURCE [arxiv:2609.35246]: Hard-Constrained Probabilistic Factor Graph Neural Network for Distribution System State Estimation under Non-Gaussian Uncertainty
Robust and accurate state estimation is fundamental for the reliable operation and monitoring of active distribution networks. Conventional numerical estimators, such as weighted least squares, are computationally slower and often suffer from convergence issues in the presence of sparse measurements affected by non-Gaussian noise. Physics-informed neural networks have recently emerged as a promising alternative by incorporating physical principles through residual-based penalty terms in the objective, which can improve robustness to noise and computational efficiency. However, such penalty-based approaches do not guarantee strict enforcement of physical constraints during inference and provide limited support for principled uncertainty modeling. To address these limitations, we propose a novel Hard-Constrained, Physics-Informed Factor Graph Neural Network (HCP-PINN) that formulates distr
Transferable mechanism (scout note): Factor-graph neural net with hard physical constraints does state estimation from sparse non-Gaussian measurements

### PAIR X016  (semantic distance 0.62, fused-vector patent proximity 0.69)
FINANCE PROBLEM SOURCE [news:3c4a723e5216b0b6]: Keralam Police warn of fake hospital appointment apps used in financial fraud - ThePrint
Keralam Police warn of fake hospital appointment apps used in financial fraud ThePrint
Open problem (scout note): Fake hospital-appointment apps used to steal banking credentials

FOREIGN MECHANISM SOURCE [arxiv:2609.34370]: Spexis: Speculative Lookahead Scheduling for LLM Inference
Spexis is a multi-GPU LLM inference framework that improves the efficiency of pipeline and tensor parallelism through speculative parallelism. Rather than using speculative decoding only to accelerate token generation, Spexis runs speculation in parallel with normal execution, introducing a new parallelism axis without increasing KV-cache memory usage. This improves memory efficiency and helps mitigate the bottlenecks of multi-GPU inference. Spexis further uses lookahead scheduling to predict speculation quality and future memory pressure, allowing it to reduce wasted speculation, KV-cache eviction, and recomputation. Built on top of vLLM, Spexis largely improves serving performance across a range of GPU configurations, achieving speedups of up to 34% over a baseline that uses the optimal combination of pipeline and tensor parallelism. Spexis's source code is publicly available at https:
Transferable mechanism (scout note): Speculative execution runs alongside normal execution as a new parallelism axis

### PAIR X017  (semantic distance 0.61, fused-vector patent proximity 0.69)
FINANCE PROBLEM SOURCE [news:98d170fad608d39b]: Regulators Move To Rescind Post-Synapse Risk Guidance, Lay Groundwork For Fintech Standards
Why Chime is Acquiring Stride, NuBank vs. Revolut, Block Seeks to Charter “Builders Bank & Trust”
Open problem (scout note): Post-Synapse: ledger reconciliation failures between fintech and sponsor bank; regulators reset guidance

FOREIGN MECHANISM SOURCE [arxiv:2609.34574]: Robust Variable-Horizon MPC for Landing a Multirotor UAV on a Moving Platform
Landing a multirotor Unmanned Aerial Vehicle (UAV) on a moving platform is challenging because a UAV is underactuated and the desired landing state is generally a non-equilibrium state. Shrinking- and variable-horizon approaches are promising for reaching such non-equilibrium targets, but often lack robustness to disturbances. Robust Variable-Horizon Model Predictive Control (VH-MPC) addresses this limitation but is computationally complex for a high-dimensional system such as a multirotor UAV. This paper presents a computationally efficient robust Variable-Horizon MPC method for reaching non-equilibrium targets under bounded disturbances. The online horizon search is restricted to a neighborhood of the previously selected horizon, while maintaining recursive feasibility under bounded disturbances. A fixed robust positively invariant tube provides horizon-independent constraint tightenin
Transferable mechanism (scout note): Robust variable-horizon MPC lands a vehicle on a moving, non-equilibrium target despite disturbances


## OUTPUT JSON SCHEMA
```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "ideas"
 ],
 "properties": {
  "ideas": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "pair",
     "title",
     "problem",
     "mechanism",
     "technical_effect",
     "why_non_obvious",
     "claim_core",
     "keywords",
     "domain"
    ],
    "properties": {
     "pair": {
      "type": "string",
      "description": "pair id used"
     },
     "title": {
      "type": "string"
     },
     "problem": {
      "type": "string"
     },
     "mechanism": {
      "type": "string",
      "description": "how it works, 80-150 words"
     },
     "technical_effect": {
      "type": "string"
     },
     "why_non_obvious": {
      "type": "string"
     },
     "claim_core": {
      "type": "string",
      "description": "draft independent-claim essence, 1-2 sentences"
     },
     "keywords": {
      "type": "string",
      "description": "prior-art search keywords"
     },
     "domain": {
      "type": "string",
      "description": "payments|fraud|credit|treasury|regtech|wealth|insurance|crypto|identity"
     }
    }
   }
  }
 }
}
```

Write the answer to: runs/2026-09-30/llm_responses/synthesis_002.json
