# TASK novelty_score_001

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2610.04128
  pool: crossdomain
  title: What Gradients Add to Text Leakage in Split Language Models, Counted per Token and per Document
  abstract: Split learning lets a client train a language model on a server without sending its text. The client runs the first layers itself and sends the server only their output, a vector of numbers for each token. During training, the server sends gradients back. We show that an observer at the split can rebuild most of the client's text from this traffic, and we measure how much the gradients help. On GPT-2, an attacker who holds only the publicly released weights of the client's layers recovers 94.20% of tokens from the activations alone and 97.38% when it also sees the gradients, 3.17 percentage points more 95% interval [2.72, 3.64]. Counted by document, the difference is much larger. The attacke
- id: arxiv:2610.03643
  pool: crossdomain
  title: SAC-Controlled RIS-Assisted Monopulse Radar for Multipath-Robust Vital-Sign Localization
  abstract: Contactless radar sensing offers a promising approach to continuous vital-sign monitoring. However, indoor multipath can distort direction estimates and generate ghost responses. This paper presents a reconfigurable intelligent surface (RIS)-assisted monopulse radar whose RIS phase configuration is controlled by a soft actor-critic agent to improve angular localization. The proposed framework combines simultaneous sum and difference beams with a programmable reflected path, enabling a single radar node to adapt the propagation environment without relying on multiple synchronized sensors. A compact multipath model formulates RIS control as a continuous-action reinforcement-learning problem wh
- id: arxiv:2610.03105
  pool: crossdomain
  title: A Benchmark for Spatially Grounded Gesture Generation
  abstract: Communication in shared space interweaves verbal and non-verbal signals, and pointing gestures anchor language to the environment: "put the cup on that one" is uninterpretable without the gesture that fixes the referent. Yet no common framework exists for evaluating whether generated gestures indicate their intended referent; distributional metrics reward a gesture aimed at the wrong object as long as it looks natural. We introduce a benchmark for spatially grounded gesture generation, comprising ~2K pointing-annotated clips from naturalistic VR dialogue with ground-truth 3D referents, a task in which systems must decide when, how and where to point within conversational speech, and a protoc
- id: arxiv:2610.03032
  pool: crossdomain
  title: Secrecy Performance of an Artificial Noise Aided Dual-Hop SWIPT MIMO-NOMA Network in Presence of Practical Impairments
  abstract: This paper investigates the secrecy performance of a cooperative non-orthogonal multiple access (NOMA) network under practical impairments. In the considered system, the source employs orthogonal space-time block coding (OSTBC) transmission, legitimate users adopt receive antenna selection (RAS), and the eavesdropper utilizes maximal-ratio combining (MRC) scheme. Moreover, an energy-constrained amplify-and-forward relay harvests energy from the received signal and allocates the harvested energy to information forwarding and artificial noise (AN) generation. To capture the realistic performance of a more practical transmission scenario, channel estimation errors (CEE), feedback delay (FBD), i
- id: arxiv:2610.03995
  pool: crossdomain
  title: viaCross: A Pen-Based Technique for Selecting Objects and Attributes of Interest using Crossing-Based Gestures
  abstract: Crossing-based selection is well-studied, yet past research has overlooked multi-object and attribute selection with crossing gestures. We present viaCross, a pen-based technique in which crossing strokes define attribute constraints, paired with attribute widgets that visualize and allow subsequent edits to these constraints. A controlled study compared viaCross with traditional WIMP filter panels. Results show that viaCross was more efficient for complex object-level selections, requiring fewer strokes and maintaining efficiency as task difficulty increased. WIMP panels were faster and more intuitive for simple attribute-based selections, but participants encountered repeated deselections 
- id: arxiv:2610.04037
  pool: crossdomain
  title: BitIR: Cross-Architecture Fault Injection for Resilience Analysis of Heterogeneous GPU Applications
  abstract: Modern GPU-based HPC systems rely on heterogeneous vendor stacks, yet resilience studies are largely limited to single architectures, leaving it unclear how faults behave across different GPU backends. We present \emph{BitIR}, a cross-architecture fault injection framework that injects deterministic single-bit faults at the LLVM IR level, ensuring semantically equivalent perturbations prior to backend lowering and enabling direct cross-vendor comparison across NVIDIA, Intel, and AMD GPUs. We evaluate BitIR on three production supercomputers -- Polaris (ALCF, NVIDIA A100), Aurora (ALCF, Intel GPU Max 1550), and Frontier (OLCF, AMD Instinct MI250X) -- representing the full spectrum of current 
- id: arxiv:2610.06918
  pool: crossdomain
  title: Learning from Unreliable Trajectories: Adversarially-Robust Federated Q-Learning
  abstract: We study federated reinforcement learning in which multiple agents interact with a common Markov decision process and communicate through a central server to collaboratively learn the optimal state-action value function. Our goal is to understand whether the sample-efficiency benefits of collaboration can be retained when a fraction of the agents behave adversarially and transmit arbitrarily corrupted information. To address this problem, we introduce Robust Async-Fed-Q, an epoch-based federated learning algorithm that combines variance-reduced estimation of the Bellman optimality operator at the agents with robust aggregation at the server. We establish high-probability finite-time guarante
- id: news:cb6784f470aac7a0
  pool: finance
  title: Decisions taken by the Governing Council of the ECB (in addition to decisions setting interest rates)
  abstract: 
- id: news:e15bf7944e5e2a86
  pool: finance
  title: Record-Breaking CNY 2.55 Billion in Digital Green Bonds; Tokenized Deposits Emerge as a New Solution - Moomoo
  abstract: Record-Breaking CNY 2.55 Billion in Digital Green Bonds; Tokenized Deposits Emerge as a New Solution Moomoo
- id: news:4918caec7d83900d
  pool: finance
  title: Robocall Scams: What They Are & How to Protect Your Small Business - Bitdefender
  abstract: Robocall Scams: What They Are & How to Protect Your Small Business Bitdefender
- id: news:8bd82f7e7b80af57
  pool: finance
  title: Free Instant Payments Still Need a Revenue Model - PYMNTS.com
  abstract: Free Instant Payments Still Need a Revenue Model PYMNTS.com
- id: news:a3bc7f71eb49297d
  pool: finance
  title: QuickCheck: Are scammers using AI to impersonate Bank Negara online? - The Star
  abstract: QuickCheck: Are scammers using AI to impersonate Bank Negara online? The Star
- id: news:ec8f2871a4e8e539
  pool: finance
  title: Appointment of members of the Enforcement Decision Making Committee (EDMC)
  abstract: Following an external recruitment process, the Bank of England has appointed Carlos Conceicao and Alexander Justham as members of its Enforcement Decision Making Committee, with effect from September 2026.
- id: news:7147222c0cb848a1
  pool: finance
  title: Stablecoin firm Fasset aims to be a bank for people and their AI agents - Yahoo Finance
  abstract: Stablecoin firm Fasset aims to be a bank for people and their AI agents Yahoo Finance
- id: news:32479552c4380bb4
  pool: finance
  title: How Stripe, Zerohash alums are looking to speed international payments - Banking Dive
  abstract: How Stripe, Zerohash alums are looking to speed international payments Banking Dive
- id: news:7dabdc4c4905ee00
  pool: finance
  title: Robinhood’s Agentic Trading Aims to Thread the Needle with Investors - PaymentsJournal
  abstract: Robinhood’s Agentic Trading Aims to Thread the Needle with Investors PaymentsJournal
- id: arxiv:2610.03369
  pool: finance
  title: Mixture-of-Experts for Cryptocurrency Order Execution: Training Stability, Tail Risk, and Failure Modes
  abstract: Deep reinforcement-learning policies for order execution can vary substantially across training seeds, so apparent architectural gains may reflect favourable training realisations rather than reproducible properties of the architecture. We evaluate vanilla Double Deep Q-Learning (DDQL), K-means-partitioned mixtures of DDQL experts at $K \in \{2, 4, 8\}$, and dense networks parameter-matched to the $K{=}4$ and $K{=}8$ expert budgets on 5-minute mean-aggregated BTC/USDT limit order book data from Binance. No learned configuration significantly improves mean implementation shortfall over DDQL. Under the reported specification, all have higher mean shortfall than TWAP (0.39 bps) and immediate li
- id: arxiv:2610.03259
  pool: finance
  title: PaMIR: Open Benchmark of Public Credit-Default Datasets
  abstract: We release PaMIR (Public Arrival-ordered Measurement for Inference in Risk), an open benchmark for credit-default prediction when labels are scarce and arrive late. The field's reference benchmark studies use eight datasets each, only two or four of them public. PaMIR brings together 19 public datasets with binary default labels -- 1.24M loans, firms and card accounts from nine countries -- rebuilt from pinned source snapshots by one leakage-audited recipe and never redistributed; to our knowledge it is the one of its kind as of today. Every model is a single function, scored under a repeated i.i.d. split and a label-delayed stream in which each application is scored on arrival, with AUC rep
- id: arxiv:2610.03841
  pool: finance
  title: Dexy: A Simple Stablecoin Design Based on an Algorithmic Central Bank
  abstract: We consider a new algorithmic stablecoin called Dexy consisting of three components: a central bank, a secondary market in the form of a customized CP-AMM liquidity pool, and a trusted oracle. The price of the stablecoin in the liquidity pool is stabilized, relative to the oracle price, via central bank interventions. Users mint Dexy stablecoins from the bank using basecoins, the base cryptocurrency asset.
- id: arxiv:2610.03922
  pool: finance
  title: Priority Gas Auction Cadence and Searcher Competition: Evidence from Flashblocks on Base
  abstract: Flashblocks divide a block's priority gas auction into shorter sequential auctions that commit transaction order before the block is complete. We ask how this auction cadence affects bidding and competition among automated arbitrageurs, or searchers. In July 2025 Base replaced a single 2 s auction with ten 200 ms auctions. We use this change to estimate the searcher response from on-chain data alone. On an address-day panel of 3,032 searchers and 8,053 activity-matched controls, a difference-in-differences design estimates a 0.187 gwei fall in the effective priority fee (59% of the searcher pre-period mean). The share of searcher priority-fee value paid in the first tenth of block gas falls 
- id: s2:51f983ce3e69e2cfc043edbe9f59372519757e24
  pool: finance
  title: Digital insurance revisited: Digital transformation in Sri Lanka’s life insurance industry, 2023–2025
  abstract: This study follows up an earlier case study of a Sri Lankan life insurer’s shift from a paper-based, agent-dependent model to a digitally enabled operation, and examines how digital transformation evolved across the Sri Lankan life insurance industry between 2023 and 2025. It adopts a qualitative longitudinal single-case design, applying document analysis and thematic analysis to publicly available regulatory, company, industry and press documents, with the findings of the earlier study serving as a baseline. Seven themes emerged: direct-to-consumer digital distribution; artificial intelligence in customer service and claims; the regulator’s role in building shared digital infrastructure; ba
- id: arxiv:2610.03951
  pool: finance
  title: Evolving LLM-Generated Features for Interpretable Classification
  abstract: Large language models (LLMs) are increasingly used as classifiers, yet they operate as opaque systems whose decisions are difficult to interpret, which complicates their use in regulated domains such as credit scoring or medical diagnosis. We propose an evolutionary framework that iteratively discovers natural language feature definitions (rubrics) for interpretable classification. An LLM generates candidate binary features, evaluates each sample against them, and the resulting vectors can be used to train a transparent classifier such as logistic regression. The feature set evolves over multiple iterations guided by classification errors, per-class activation rates, and feature ablation sco

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

Write the answer to: runs/2026-10-02/llm_responses/novelty_score_001.json
