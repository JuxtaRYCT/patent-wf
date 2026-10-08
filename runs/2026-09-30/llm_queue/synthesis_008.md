# TASK synthesis_008

## SYSTEM
You are an inventor on a bank's advanced-technology team, expert in payments, fraud, credit, treasury, regulation (US, EU, UK, India) and patent drafting. You practise bisociation: transplanting a mechanism from an unrelated field into a finance problem. Rules: (1) every concept must have a concrete TECHNICAL mechanism (data structures, signals, protocols, hardware, cryptography, control loops) - not a business method; (2) it must be implementable within ~3 years; (3) name what makes it non-obvious versus the closest thing you know exists; (4) prefer concepts a bank, card network or payment processor would license; (5) if a pair yields nothing credible, return fewer ideas rather than forcing one.

## PROMPT
For each pair, transplant the foreign mechanism into the finance problem and propose 0-2 patentable invention concepts. Stretch for unusual but technically credible combinations.

### PAIR X048  (semantic distance 0.60, fused-vector patent proximity 0.69)
FINANCE PROBLEM SOURCE [news:4c3e57e9cdf492a9]: Bank accounts emptied in attempt to watch adult content: Govt warns users against these apps; check the lis... - Bhaskar English
Bank accounts emptied in attempt to watch adult content: Govt warns users against these apps; check the lis... Bhaskar English
Open problem (scout note): Malicious adult-content apps drain bank accounts

FOREIGN MECHANISM SOURCE [arxiv:2609.34370]: Spexis: Speculative Lookahead Scheduling for LLM Inference
Spexis is a multi-GPU LLM inference framework that improves the efficiency of pipeline and tensor parallelism through speculative parallelism. Rather than using speculative decoding only to accelerate token generation, Spexis runs speculation in parallel with normal execution, introducing a new parallelism axis without increasing KV-cache memory usage. This improves memory efficiency and helps mitigate the bottlenecks of multi-GPU inference. Spexis further uses lookahead scheduling to predict speculation quality and future memory pressure, allowing it to reduce wasted speculation, KV-cache eviction, and recomputation. Built on top of vLLM, Spexis largely improves serving performance across a range of GPU configurations, achieving speedups of up to 34% over a baseline that uses the optimal combination of pipeline and tensor parallelism. Spexis's source code is publicly available at https:
Transferable mechanism (scout note): Speculative execution runs alongside normal execution as a new parallelism axis

### PAIR X049  (semantic distance 0.62, fused-vector patent proximity 0.69)
FINANCE PROBLEM SOURCE [news:1517bc72795f1a1b]: ECB to invest part of own funds in tokenised securities, with settlement via Pontes

Open problem (scout note): Central bank invests own funds in tokenised securities settled via DLT-to-RTGS bridge (Pontes)

FOREIGN MECHANISM SOURCE [arxiv:2609.00614]: BME-like Quartet Weights for Phylogenetic Trees
Like pairwise distances, quartets can be highly redundant and correlated on a phylogenetic tree, and their number grows on the order of n^4 rather than n^2. I explore BME-like weights for reweighting quartet scores before summing them to score a full tree. Three weights are considered on an unrooted binary tree: w_ext(q)=2^(-I_ext(q)), w_int(q)=2^(-I_int(q)), and w_tot(q)=2^(-I_tot(q))=w_ext(q)w_int(q), where the exponents count specified internal nodes in the minimal connecting subtree of a quartet. Exact tree-shape counts, total quartet-weight sums, and internal-edge crossing sums are calculated for all unlabeled unrooted binary tree shapes on 6-10 taxa. For w_ext, the total quartet weight is tree-shape-invariant and the edge-crossing sum depends only on split size. For any n-leaf tree, we prove sum_q w_ext(q)=(n-2)(n-3)/8, and the sum over quartets crossing an internal edge with split
Transferable mechanism (scout note): Reweighted quartet scores reconstruct phylogenetic trees efficiently

### PAIR X050  (semantic distance 0.59, fused-vector patent proximity 0.70)
FINANCE PROBLEM SOURCE [news:fefcaf910263218b]: Mastercard Helps Danske Bank With Denmark-First Agentic Transaction - pymnts.com
Mastercard Helps Danske Bank With Denmark-First Agentic Transaction pymnts.com
Open problem (scout note): First national-market agentic transaction by a bank with card network tokens

FOREIGN MECHANISM SOURCE [arxiv:2609.35246]: Hard-Constrained Probabilistic Factor Graph Neural Network for Distribution System State Estimation under Non-Gaussian Uncertainty
Robust and accurate state estimation is fundamental for the reliable operation and monitoring of active distribution networks. Conventional numerical estimators, such as weighted least squares, are computationally slower and often suffer from convergence issues in the presence of sparse measurements affected by non-Gaussian noise. Physics-informed neural networks have recently emerged as a promising alternative by incorporating physical principles through residual-based penalty terms in the objective, which can improve robustness to noise and computational efficiency. However, such penalty-based approaches do not guarantee strict enforcement of physical constraints during inference and provide limited support for principled uncertainty modeling. To address these limitations, we propose a novel Hard-Constrained, Physics-Informed Factor Graph Neural Network (HCP-PINN) that formulates distr
Transferable mechanism (scout note): Factor-graph neural net with hard physical constraints does state estimation from sparse non-Gaussian measurements

### PAIR X051  (semantic distance 0.63, fused-vector patent proximity 0.65)
FINANCE PROBLEM SOURCE [news:d139d55e1e4a00fc]: Colorado Sues EarnIn, Alleging Its “Earned Wage Access” Product Is Really a High-Cost Loan - Consumer Finance Monitor
Colorado Sues EarnIn, Alleging Its “Earned Wage Access” Product Is Really a High-Cost Loan Consumer Finance Monitor
Open problem (scout note): Earned wage access classification as credit

FOREIGN MECHANISM SOURCE [arxiv:2609.34574]: Robust Variable-Horizon MPC for Landing a Multirotor UAV on a Moving Platform
Landing a multirotor Unmanned Aerial Vehicle (UAV) on a moving platform is challenging because a UAV is underactuated and the desired landing state is generally a non-equilibrium state. Shrinking- and variable-horizon approaches are promising for reaching such non-equilibrium targets, but often lack robustness to disturbances. Robust Variable-Horizon Model Predictive Control (VH-MPC) addresses this limitation but is computationally complex for a high-dimensional system such as a multirotor UAV. This paper presents a computationally efficient robust Variable-Horizon MPC method for reaching non-equilibrium targets under bounded disturbances. The online horizon search is restricted to a neighborhood of the previously selected horizon, while maintaining recursive feasibility under bounded disturbances. A fixed robust positively invariant tube provides horizon-independent constraint tightenin
Transferable mechanism (scout note): Robust variable-horizon MPC lands a vehicle on a moving, non-equilibrium target despite disturbances

### PAIR X052  (semantic distance 0.60, fused-vector patent proximity 0.71)
FINANCE PROBLEM SOURCE [news:1e85773664d92e3a]: Repeated ₹2,000 UPI payments for one purchase? Your bank could flag the pattern: What it means - Business Today
Repeated ₹2,000 UPI payments for one purchase? Your bank could flag the pattern: What it means Business Today
Open problem (scout note): Transaction splitting (repeated small UPI payments for one purchase) as evasion pattern

FOREIGN MECHANISM SOURCE [arxiv:2609.33553]: Grid-Forming E-STATCOMs for Stable Integration of Large-Scale Data Centers: Modeling and Control
The rapid expansion of large-scale AI data centers (AIDC) is introducing new stability challenges, particularly in weak or low-inertia networks characterized by fast, step-like demand variations and strict requirements on voltage and dynamic performance. This paper investigates the use of grid-forming (GFM) Enhanced STATCOMs (E-STATCOMs) to support reliable integration of such facilities. A power-admittance-based linear modelling framework is developed to capture system interactions and is validated through detailed EMT simulations. The results demonstrate that E-STATCOMs provide fast, well-damped responses to abrupt load changes while effectively mitigating low-frequency oscillations and interactions with network resonances. By enabling tunable dynamic behavior via a load balancer, virtual impedance, and coordinated active-reactive power support, the proposed approach allows precise sha
Transferable mechanism (scout note): Grid-forming compensator absorbs fast step-like demand of AI data centres in weak networks

### PAIR X053  (semantic distance 0.59, fused-vector patent proximity 0.72)
FINANCE PROBLEM SOURCE [news:3c4a723e5216b0b6]: Keralam Police warn of fake hospital appointment apps used in financial fraud - ThePrint
Keralam Police warn of fake hospital appointment apps used in financial fraud ThePrint
Open problem (scout note): Fake hospital-appointment apps used to steal banking credentials

FOREIGN MECHANISM SOURCE [arxiv:2609.31864]: AirLog: Store-Level Indoor Life Logging Made Easy
This paper presents AirLog, a smartphone-based life journaling system that automatically reconstructs users' store visits in shopping malls and summarizes them into human-readable journals. Unlike conventional indoor localization systems, AirLog avoids labor-intensive radio-map construction and dedicated wireless localization infrastructure and algorithm calibrations. Instead, it repurposes two cues already available in commercial spaces: semantic information exposed by ambient Wi-Fi SSIDs and indoor directory images. AirLog converts directory images into spatial maps and fuses Wi-Fi semantic anchors with inertial dead reckoning to recover store-level trajectories, which are then summarized into journals by an LLM. Such store-level life logs can support applications such as personal memory recall, activity reflection, and automated diary generation without requiring users to manually rec
Transferable mechanism (scout note): Phone reconstructs store-level visits in malls without radio maps or infrastructure


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

Write the answer to: runs/2026-09-30/llm_responses/synthesis_008.json
