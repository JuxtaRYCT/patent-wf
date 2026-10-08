# TASK novelty_score_001

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2610.09911
  pool: crossdomain
  title: A Scale For Value Alignment In Human-AI Interaction
  abstract: Value alignment is a central objective in AI and HCI research, yet no validated instrument measures how users perceive it. This gap hampers the comparison and accumulation of findings and limits the effectiveness of applications, where understanding users' viewpoints is critical. We construct and evaluate a 13-item psychometric scale that measures perceived value alignment across two components: value understanding and value manifestation. It is based on a large item pool drawn from prior empirical studies, filtered by experts, and finally assessed by users (N=607) across diverse AI scenarios. Confirmatory factor analysis on an independent sample (N=259) confirmed the two-factor structure an
- id: arxiv:2610.10173
  pool: crossdomain
  title: When Exposure Is Not Attention: Auditing the Preference-Exposure-Consumption Gap in Personalized News Recommenders
  abstract: Personalized news platforms are often evaluated as if stated preferences, logged recommendation exposure, and click consumption form a single coherent pipeline. Collapsing these layers can distort audit conclusions: a platform may appear more aligned or diverse than observed click consumption supports, which can misdirect diversity governance or algorithmic intervention. We introduce a reusable Preference-Exposure-Consumption (PEC) audit framework that separates stated preference, observed weighted profile state, logged recommendation exposure, app-surface pathways, and click consumption under explicit observability boundaries. Using six months of logs from a deployed mobile news application
- id: arxiv:2610.10430
  pool: crossdomain
  title: Conditional Flow Matching for Generation of 3D Multi-variable Instantaneous Urban Microclimate Fields
  abstract: Rapid and accurate prediction of urban wind and temperature fields is important for urban microclimate design and climate adaptation. Large-eddy simulation (LES) effectively resolves these instantaneous fields, but its application is limited in iterative design of urban microclimate applications due to high computational cost. Existing regressive data-driven models offers quick outputs, but they produce only deterministic point predictions that inherently fail to represent turbulent stochasticity. This paper adopts a novel generative framework of Conditional Flow Matching (CFM) that uses building geometry and mean flow as guidance to generate plausible three-dimensional instantaneous velocit
- id: arxiv:2610.10044
  pool: crossdomain
  title: CANDO: Cooperative Agentic Network for Layout Design Optimization
  abstract: Layout generation for real-world facilities is a challenging problem, requiring reasoning over irregular site boundaries, heterogeneous orientations, access-aware placements, and motion-planning feasibility. Yet, most existing layout benchmarks in the generative AI space target simpler placements over rectangular domains and rely on distributional metrics such as FID and IoU that reward conformity to dataset priors, thus discounting design innovation. Motivated by these gaps, we introduce ALPS-Bench, a benchmark of $1,000$ professionally annotated real-world facility layouts paired with an instance-specific scoring protocol grounded in a structured design manual. As a strong baseline for ALP
- id: arxiv:2610.10386
  pool: crossdomain
  title: Efficient Heuristics and Machine Learning Approach for Fault Characterization in Distributed Self-Stabilizing Programs
  abstract: Modern large-scale systems rely on distributed protocols to maximize efficiency while preserving the correctness guarantees of single-process execution. However, designing such protocols is non-trivial: adding resources to a system inherently increases its complexity, which in turn introduces faults that must be addressed during design. One such fault class, arising in systems that use distributed shared memory (e.g., replicated databases), is consistency violating fault (cvf), a fault in which a process accessing shared memory reads stale data previously written by another process. Cvfs are inherent to systems that prioritize availability over strict consistency. Prior work has shown that s
- id: arxiv:2610.09928
  pool: crossdomain
  title: Do Generative Priors Align with Human Naturalness Perception?
  abstract: Visual generative models are trained to capture the probability distributions of natural images, yet whether their native priors reflect the regularities governing human perception of image naturalness remains an open question. Here, we probe these priors through native prediction errors across 25 open image and video generators. Because raw single-image losses are dominated by scene content and visual complexity, we evaluate directional loss differences using content-preserving, paired relational interventions that selectively disrupt facial configurations or physical illumination consistency while limiting changes in low-level image statistics. Across both domains, these loss differences r
- id: arxiv:2610.10054
  pool: crossdomain
  title: Transition Path Sampling Using Koopman Operators and Exit-Time Optimal Control
  abstract: Sampling transitions between metastable states is a central problem in dynamical systems theory and molecular dynamics in particular. A key challenge is the existence of high free-energy barriers that separate the states, making transitions extremely rare. Recent machine learning-based methods cast transition path sampling (TPS) as an optimal stochastic control (OSC) problem over a fixed time horizon, and parameterize the drift bias via a neural network trained by simulation-in-the-loop, requiring repeated biased rollouts. To address computational and performance guarantee issues of these models, we propose a new approach for the problem based on Koopman operators. Because Koopman operators 
- id: arxiv:2610.10486
  pool: crossdomain
  title: A Compositional Perspective on Communication-Control Co-Design for Mobile Broadband Systems Beyond 6G
  abstract: Anticipated applications of beyond sixth-generation (B6G) mobile broadband networks will require the co-design of communication and control subsystems within the network architecture. Existing co-design approaches are predominantly optimization-driven, integrating subsystems through joint optimization problems. While this approach is effective in relatively simple systems, such formulations present challenges in (i) modular subsystem representations, (ii) tracing the propagation of requirements across subsystems, and (iii) systematically analyzing design-space feasibility, particularly as the number and complexity of interacting subsystems increase. In this article, we present a compositiona
- id: news:a487a879854db8c7
  pool: finance
  title: Results of the September 2026 survey on credit terms and conditions in euro-denominated securities financing and OTC derivatives markets (SESFOD)
  abstract: 
- id: news:7ce7fb272a3f1e50
  pool: finance
  title: National Bank of Kazakhstan, Tether, Alatau City Authority Study Tenge-Pegged Stablecoin And Tokenization - NewsCord
  abstract: National Bank of Kazakhstan, Tether, Alatau City Authority Study Tenge-Pegged Stablecoin And Tokenization NewsCord
- id: news:a5c059701ac8434c
  pool: finance
  title: Ally CEO: ‘Strategy is about choices’
  abstract: A narrower focus is driving better returns at the $200 billion-asset lender, although the credit and interest rate environment may challenge execution of Michael Rhodes’ strategy.
- id: news:0580ce9fa226f474
  pool: finance
  title: Tether and Kazakhstan’s National Bank to Explore Tenge-Pegged Stablecoin - ForkLog
  abstract: Tether and Kazakhstan’s National Bank to Explore Tenge-Pegged Stablecoin ForkLog
- id: news:987173c42cad1f3f
  pool: finance
  title: SAP expands into payments
  abstract: A new service from the software firm supports multiple payment methods, including wires and stablecoin-based transactions, the company said.
- id: news:837c4defe564bd14
  pool: finance
  title: Tether Signs MoU with the National Bank of Kazakhstan and the Alatau City Authority to Explore Stablecoin Use Cases and Asset Tokenization - Tether.io
  abstract: Tether Signs MoU with the National Bank of Kazakhstan and the Alatau City Authority to Explore Stablecoin Use Cases and Asset Tokenization Tether.io
- id: news:45d7100a082ef625
  pool: finance
  title: Agentic Authority: ChainIT Ties Every Payment Approval to the Exact Payment - The Des Moines Register
  abstract: Agentic Authority: ChainIT Ties Every Payment Approval to the Exact Payment The Des Moines Register
- id: news:ed190321ab8e7af3
  pool: finance
  title: The check fraud pattern costing agencies money every week - Insurance Business
  abstract: The check fraud pattern costing agencies money every week Insurance Business
- id: gh:accomplish999/position-sizer
  pool: finance
  title: accomplish999/position-sizer
  abstract: Position size calculators for Perps and DeFi. | topics: cli, crypto, cryptocurrency, defi, impermanent-loss, perpetual-futures, position-sizing, risk, risk-analysis, risk-analytics, risk-assessment, risk-management, risk-modeling, risk-prediction, risk-scoring, typescript, uniswap
- id: news:dc78d5a3bb8b0991
  pool: finance
  title: Ex-Barclays bankers have ther interest rate fraud convictions overturned - upi
  abstract: Ex-Barclays bankers have ther interest rate fraud convictions overturned upi
- id: news:2399e1ffd51bd1a2
  pool: finance
  title: Stuut cashes in on agentic order-to-cash automation with $52.5M in funding - SiliconANGLE
  abstract: Stuut cashes in on agentic order-to-cash automation with $52.5M in funding SiliconANGLE
- id: news:1aa254b641506f27
  pool: finance
  title: Stripe, FedEx team on SMB lending
  abstract: Merging operational and financial data will offer insights into smaller businesses and guide an effort to extend capital to them, the companies said.
- id: arxiv:2610.10010
  pool: finance
  title: Defining Purpose-Limited Secrets
  abstract: A cryptographic secret is issued for a purpose but grants a capability, and the capability is usually larger: a decryption key meant for computing aggregates can read every record, and a token meant to pay one invoice can drain the account. Deployed systems state the purpose in policy and enforce only the capability. We make the purpose a property of the secret. A mechanism sees operations, not reasons, so a scheme enforces an admissible set $A(P)$ of operations that stands in for a declared intended use $I$; whether $I$ captures the human purpose is a modeling obligation that marks where policy takes over. Against the same $I$ we define three regimes: under confinement an operation outside 
- id: arxiv:2610.10476
  pool: finance
  title: From a Hierarchy of Stochastic Differential Equations to a Hierarchy of Generalized Beta Distributions
  abstract: We introduce a mean-reverting stochastic differential equation with a three-component stochastic term and show that it generates a hierarchy of steady-state (stationary) distributions. At the top level, the hierarchy is described by a modified-Beta distribution, while one- and two-parameter reductions produce compact-support, power-law-tailed, and exponential-type limiting families within a single stochastic framework. We then construct two generalized extensions of this hierarchy. In the first, the power transformation is applied directly at the level of the stochastic differential equation; in the second, the same transformation is applied only after the stationary modified-Beta hierarchy 
- id: arxiv:2610.10149
  pool: finance
  title: Pump-and-Dump meets Honeypot Tokens: Detection and Analysis of Telegram Bait-and-Trap Schemes
  abstract: While Pump-and-Dump schemes have been extensively studied on centralized exchanges (CEXs), how they operate in decentralized exchanges (DEXs) remains largely unexplored. We monitor 83 Telegram channels used to coordinate Pump-and-Dump campaigns and collect 3,677 events across the BNB Smart Chain and Ethereum. Our analysis reveals that, although these operations superficially resemble CEX-based Pump-and-Dump schemes, their underlying mechanism is fundamentally different. Rather than manipulating prices, organizers orchestrate deceptive Pump-and-Dump campaigns around honeypot tokens whose smart contracts allow Telegram subscribers to buy but prevent them from selling. Unaware of this restricti
- id: arxiv:2610.09581
  pool: finance
  title: Correct Answers, Unsupported Findings: Evidence Binding in Forensic Reconstruction of LLM Agent Logs
  abstract: Forensic reconstruction of LLM-agent actions requires not only recovering the correct value, but establishing which preserved record supports that finding. Tool logs, generated explanations, and local citation identifiers capture different parts of this evidence, yet a citation identifier does not establish a source unless its binding to a record is preserved. We audit this distinction using 64 mechanically checkable cases from saved AgentDojo Banking executions. Two LLM readers reconstruct source relationships under controlled variations in visible evidence and identifier-to-record bindings. We separately evaluate complete-record agreement, evidence-grounded findings, justified abstention, 

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

Write the answer to: runs/2026-10-07/llm_responses/novelty_score_001.json
