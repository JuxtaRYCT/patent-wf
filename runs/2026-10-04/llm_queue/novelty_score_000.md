# TASK novelty_score_000

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2610.05475
  pool: crossdomain
  title: Poor Privacy Practices Of The Apple App Store: Cookies, Advertising and Tracking Of Users
  abstract: We analyse the data that the Apple App Store sends to and receives from Apple servers. We find that multiple cookies are sent by Apple servers and stored on the handset. Adverts with tracking identifiers are also stored on the handset, and we observe that adverts are selected by Apple servers using GDPR special category personal data such as sexuality, religious beliefs and health. User interactions with the Apple App Store (apps and adverts viewed, buttons clicked, searches made etc) are transmitted to Apple servers alongside identifiers linking this data to the individual user and device. We show that much of this data storage and transmission is not essential for the service requested by 
- id: arxiv:2610.06994
  pool: crossdomain
  title: TARE: Weigh a Never-Poisoned Twin Before Reading Backdoor-Defense Costs
  abstract: Backdoor-defense leaderboards print a clean-accuracy drop and read it as removal cost. Measured on the poisoned victim alone, the drop cannot separate removal from what the defense does to any model, and inherits the victim's start, which for three of BackdoorBench's sixteen attacks is a configuration file: WaNet, BPP and Input-Aware ship a MultiStepLR that never fires, so their victims never anneal and are the least accurate in 30/31 public CIFAR cells at $\leq$5%. On PreAct-ResNet18, fine-tuning-family defenses return a low start to their own level, so there the published cost is negative, the benchmark's rating clips the "gain" to zero, and 2 of 48 citing defense papers we read rest a no-
- id: arxiv:2610.05339
  pool: crossdomain
  title: Nonlinear Tensor Decomposition for Pattern Discovery
  abstract: The CANDECOMP/PARAFAC (CP) decomposition is widely used for revealing the underlying patterns from multiway data (also referred to as a higher-order tensor). When the data is clipped or saturated, however, the linear CP model becomes unreliable. Several remedies exist such as treating the clipped entries as missing or imputation; however, both fall short in different scenarios. We propose a nonlinear CP model (NCP) for pattern discovery in this setting, extending ideas from nonlinear matrix decompositions to tensors, and solve it using a flexible ADMM (Alternating Direction Method of Multipliers)-based framework that can accommodate a variety of nonlinearities. Using synthetic data with know
- id: arxiv:2610.07013
  pool: crossdomain
  title: A numerical and efficient model for thermo-field electron emission calculations
  abstract: As electron sources are reduced in size, fabricated in new materials, or pushed for performance, the analytical formulations for thermo-field electron emission, namely Fowler-Nordheim and Murphy-Good equations and their JWKB-based extensions, are increasingly applied out of the range of conditions for which they were derived. We present GETELEC-3, an open-source code that replaces them with a direct numerical solution of the one-dimensional time-independent Schrödinger equation (1D-TISE). Several methods to solve the 1D-TISE have been implemented to test for speed, robustness, and solution's uncertainty. The Noumerov algorithm is found to be quickest, with the solution uncertainty below 1%, 
- id: arxiv:2610.05246
  pool: crossdomain
  title: What a Policy Gate Can and Cannot Know: Measured Boundaries of Cross-Platform Command Adjudication
  abstract: Gateways that adjudicate an agent's actions before they execute are only as good as their understanding of the action. We study a policy gate that never parses shell syntax: it consumes a typed, realised action (verb, operands, resolved zones, program-object identity) and decides ALLOW, ASK or DENY. Working on a Linux twin of the Windows benchmark of our previous study [1], we ask how faithfully it adjudicates, what survives translation, and whether deciding stays affordable as the system is used. A frozen 61-case table scores 61/61 in two rounds with no false allow; a 50-operator mutation campaign kills 46 of 50 mutants (92.0%), with all four surviving mutants classified. An 82-row audit yi
- id: arxiv:2610.07012
  pool: crossdomain
  title: Frequency-Dependent Breakdown of Litz-Wire Insulation Under Repetitive Bipolar Square-Wave Voltages
  abstract: This paper investigates the dielectric breakdown behavior of Litz wire insulation subjected to repetitive fast-edge bipolar square-wave voltages representative of wide-bandgap (WBG) power converter stress. Two conductor sizes, 14 AWG and 16 AWG, were tested in a twisted-pair configuration over frequencies ranging from 1 kHz to 30 kHz using a controlled high-voltage pulse generator with 200 ns rise time. The breakdown voltages obtained at each frequency were statistically analyzed using the weighted two-parameter Weibull method in accordance with IEEE Std 930-2004. Between 1 and 30 kHz, the mean breakdown voltage decreases by approximately 10.7% for the 14 AWG construction and 20.0% for the 1
- id: arxiv:2610.05511
  pool: crossdomain
  title: Rank-one variance inflation in polynomial estimation of signal parameters with a sign-preserving fractional-power basis
  abstract: The polynomial maximization method estimates signal parameters in non-Gaussian noise from a finite description of the noise by its moments and cumulants, without a density. Known accuracy results assume that these noise characteristics are known, or use a design in which estimating them jointly costs no accuracy. In practice they are estimated from the residuals of a preliminary fit, and the effect of this substitution on accuracy is unknown. We treat the feasible scheme as a two-step estimator and, for a general smooth signal model in a fixed design, find the increment of its asymptotic covariance in closed form: $Σ_{\rm fe}-Σ_{\rm or}=c_2(1-g_{\rm or}) Q^{-1}\bar{d}\bar{d}^{\top}Q^{-1}$, a
- id: arxiv:2610.05458
  pool: crossdomain
  title: Measuring and Reducing Cross-Vendor Mismatch in Language Models
  abstract: Running the same language model on different graphics processing unit (GPU) vendors can produce different logits, even when the model weights and inputs are the same. We analyze cross-vendor mismatch in two dense and two mixture-of-experts (MoE) models with five metric families, namely bitwise equality, logit differences, top-K consistency, token agreement, and task accuracy. We trace one source of the mismatch to accumulation order inside vendors' matrix instructions. Upcasting to FP32 reduces the dense model's logit error by 43% at three times the runtime, yet keeping only the MLPs in BF16 retains 94% of this gain at 1.3 times the runtime, so most of the cost of full upcasting buys little.
- id: arxiv:2610.05455
  pool: crossdomain
  title: Social Navigation for Tour-guide Robot
  abstract: We propose a force-based model for social navigation of a tour-guide robot. Social forces due to various factors like obstacles, user position and heading, have been accounted for in the model. We claim that each one of these forces makes the robot more sociable to the user and we design an experimental setup for evaluation. In the experiment, the user follows an autonomous robot to a destination in a known map, while undertaking a few simple sub-tasks in the middle, which serve as distractions. For each participant, we run several rounds of the experiment, each with different forces and a shortest path, A*-search baseline model. Using per-round subjective indicators, we propose to study the
- id: arxiv:2610.05470
  pool: crossdomain
  title: Altruism as Infrastructure: Volunteer Moderation in a Bangladeshi Higher Education Facebook Group
  abstract: Aspiring international students across Asian countries increasingly depend on commercial education agents to navigate scholarships, documentation, and visas. Alongside this commercial infrastructure, volunteer-run Facebook groups have emerged. Unpaid admins and moderators, often under their real identities, vet information, screen scams, and guide members through scholarships, visas, and departure logistics. We study one such Bangladeshi group, \textit{HigherStudyAbroad: Global Hub of Bangladeshis}, founded in 2010. Drawing on semi-structured interviews with 17 volunteer admins and moderators, we found that altruism becomes an organizing logic. It shapes moderators' identities, sustains invi
- id: arxiv:2610.05561
  pool: crossdomain
  title: Beyond Monolithic Perturbation: Heterogeneous Mechanism Design for Multi-Attribute Metric Differential Privacy
  abstract: Multi-attribute user records are inherently heterogeneous, often combining continuous, categorical, and binary attributes, and they frequently exhibit strong cross-attribute dependencies. Designing high-utility metric differential privacy (mDP) mechanisms for such records is challenging. Simple predefined mechanisms, such as distance-based noise, may be poorly aligned with task-specific utility loss, whereas fully optimization-based mechanisms can be computationally prohibitive for multi-attribute records. We propose Dependency-aware Heterogeneous Data Perturbation (DepHDP)}, a framework for multi-attribute mDP that combines dependency-aware attribute grouping with heterogeneous perturbation
- id: arxiv:2610.07026
  pool: crossdomain
  title: Offline AI Modules: Voice-First Offline Architecture, Hardware Reference Stack, Quantization and Benchmarking
  abstract: The Offline AI Modules workstream enables practical, low-power, and community-accessible deployment of voice-first AI systems that operate fully offline. Designed for African language communities where speech is the dominant mode of interaction and internet connectivity is unreliable or absent, the workstream delivers three reinforcing components: a modular voice-first offline architecture, a low-cost hardware reference bill of materials, and a reproducible quantization and a reproducible quantization and benchmarking pipeline for instruction-tuned language models in the 2-5B parameter class. This paper presents the first end-to-end benchmark evaluation of the stack across two hardware tiers
- id: arxiv:2610.04869
  pool: crossdomain
  title: Your Temporal Link Predictor Is Blind to Who Is Active: A Missing Factor That Transfers Across Models
  abstract: An interaction has two parts: someone decides to act, and then chooses whom to act on. Temporal link prediction has concentrated on the second, and we show that it is blind to the first by construction: a standard negative keeps the real source and swaps the destination, and we prove that this cancels the source's activity exactly from the optimal score, so no model trained and evaluated this way is ever rewarded for learning it. Under the harder historical and inductive negatives, whose sources differ, the same factor becomes the dominant signal. We model it with Source Node Activity Modeling (SNAM), a self-exciting event intensity fitted by an exact point-process likelihood to decayed inte
- id: arxiv:2610.05545
  pool: crossdomain
  title: Reactive Constraint-Based Geolocation of Internet Hosts
  abstract: Active IP geolocation techniques rely on the responsiveness of Internet hosts, while passive techniques depend on data sources that are unevenly adopted and prone to staleness and error. In this work, we invert the active IP geolocation problem by listening at a geographically distributed set of vantage points for unsolicited Internet scans. By reactively completing connections with these scanners, we obtain round-trip time (RTT) measurements from hosts that may otherwise be unresponsive and use those measurements for geolocation. Over the course of 20 days in August 2026, we recorded 46.8 million scans from 289,746 distinct scanners, with a reactive RTT for each scan. We show that reactive 
- id: arxiv:2610.05031
  pool: crossdomain
  title: When LLMs Sit Above Diagnostic Tools: Unrealized Complementarity in Industrial Fault Diagnosis
  abstract: Large language models are increasingly used as integration layers above specialized tools, but a stronger component does not necessarily produce a stronger combined system. Across five diagnostic datasets (bearing vibration, process monitoring, semiconductor equipment), we study whether an LLM can reliably use external diagnostic information; paired repeat calls separate advice effects from output instability. In all five, conflicting external information overturned initially correct LLM judgments. Among the four datasets with direct integration comparisons, none showed a consistent advantage for implicit LLM integration over the stronger standalone source. On a Tennessee Eastman confirmatio
- id: arxiv:2610.04877
  pool: crossdomain
  title: Consumer empowerment: need, definition, quantification, outcomes and challenges
  abstract: The transition toward decentralized digitalized and lowcarbon electricity systems is fundamentally changing the role of electricity consumers Traditionally passive endusers are increasingly expected to integrate distributed energy resources DERs and participate in energy management and demand response This paper examines consumer empowerment CE in electricity networks with a specific focus on small consumers connected to distribution networks The paper first discusses the technical economic and societal drivers underlying the growing need for CE including increasing DER penetration electrification of heating and transportation network congestion and flexibility requirements A comprehensive d
- id: arxiv:2610.05444
  pool: crossdomain
  title: Imagining a Muslim Internet: Trust, Autonomy, and Segregation in a Faith-Aligned Browser
  abstract: Religiously branded platforms raise important questions about trust, usability, and autonomy when technology is built around a specific faith. Prior HCI work on Islam and Muslim technology has focused on single-purpose tools such as prayer, scripture, and health apps, leaving infrastructures like browsers, which shape a user's relationship with the Internet, unexamined. We address this gap through semi-structured interviews with 16 users of Kahf Browser, a faith-aligned browser designed to support Muslims' online activities. Findings show religious identity motivates adoption but does not sustain it. Trust is not fixed by religious branding but shifts over time based on the browser's functio
- id: arxiv:2610.05270
  pool: crossdomain
  title: Synergizing Drone Delivery Order Pooling and Road Network Monitoring through Monitoring-Task Orderization
  abstract: This paper investigates the real-time dispatch of a shared drone fleet for on-demand food delivery and urban road network monitoring. We consider a courier-drone collaborative setting in which couriers transport orders to launchpads and drones complete the final delivery leg to kiosks. Drones may consolidate multiple origin-destination orders within one flight and make monitoring-aware route adjustments to collect real-time traffic information subject to delivery-time constraints. This yields a joint decision problem coupling dynamic order-to-drone matching, multi-order pooling, routing, and time-varying monitoring under fleet-level competition and uncertainty. We propose monitoring-task ord
- id: arxiv:2610.05510
  pool: crossdomain
  title: New and Improved Analytical Methods for Calculating Power System Adequacy Metrics
  abstract: A new analytical technique is proposed for calculating adequacy metrics for generation planning. The proposed technique is simple, direct, and provides higher accuracy than traditional discretized approaches. Additionally, a new analytical methodology is introduced for calculating loss of load days (LOL Days) as distinct from loss of load events or frequency of load loss. This paper emphasizes that, where feasible, analytical methods are preferable to Monte Carlo simulations because they yield exact closed-form solutions rather than statistical estimates.
- id: arxiv:2610.05624
  pool: crossdomain
  title: Onset of Melting in Finite Ion Crystals: The Role of Structural Isomerization
  abstract: We theoretically investigate the microscopic mechanism of melting in finite two-dimensional ion crystals confined in anisotropic traps. Building on our previous studies of melting probability as a function of temperature and anisotropy, we extend the analysis to crystal sizes ranging from $N=4$ to $N=101$ ions and examine how structural isomerization modifies the melting pathways. Using molecular dynamics simulations together with Metropolis-Hastings equilibrium sampling, we analyze radial fluctuations, angular disorder, Lindemann parameters, and isomer-dependent energy landscapes in these Coulomb crystals. We find that crystals with identical particle number and trap anisotropy can exhibit 
- id: arxiv:2610.05605
  pool: crossdomain
  title: Handling Missing Data in Performance Portability Studies
  abstract: Missing data is a common challenge in many real-world datasets, often leading to biased results or reduced accuracy. Missing data is a pervasive problem in performance efficiency datasets, particularly in high-performance computing (HPC) performance portability studies. Performance portability scores rely on complete sets of performance efficiencies as inputs to their respective metrics; however, missing values can arise due to incomplete benchmarking, hardware constraints, or implementation gaps. Many established performance portability metrics lack mechanisms for handling missing inputs, which can result in incomplete analyses or the inability to compute scores altogether. In this study, w
- id: arxiv:2610.05530
  pool: crossdomain
  title: Optimal Dynamic Resource Allocation for Multicore Real-time Systems
  abstract: We formulate a novel optimal control problem for data-driven dynamic resource allocation in multicore real-time systems. The proposed formulation accounts for hard deadline constraints and resource bounds. Under mild assumptions, we prove several results on the feasibility and existence of optimal solution for the proposed formulation. Building on these analyses, we design an algorithm to solve the multi-core dynamic resource allocation problem. We demonstrate the practical use of this new algorithm by experimentally evaluating it on a real multicore platform using four benchmarks from the literature.
- id: arxiv:2610.05122
  pool: crossdomain
  title: PB-STDG: A Prediction-Based Short-Term Decentralized Greedy Guidance Algorithm for a Drone Road System
  abstract: In recent years, Unmanned Aerial Vehicles (UAVs) or drones have been increasingly adopted in urban environments for applications such as parcel delivery, infrastructure inspection, emergency response, and drone light shows. A non-negligible issue is how to manage the increasing number of drones operated by different entities, to enable them to cooperatively avoid potential collisions and determine conflict-free short-term flight paths in urban airspace. This paper presents a Prediction-Based Short-Term Decentralized Greedy (PB-STDG) guidance algorithm for a structured Drone Road System (DRS). PB-STDG extends the original STDG algorithm by introducing a prediction mechanism that enables drone
- id: arxiv:2610.07030
  pool: crossdomain
  title: LLM-Based Multi-Agent Collaboration for Constrained Multi-Objective Container Placement
  abstract: Container placement in data centers must simultaneously minimize power consumption and maximize affinity preferences, while satisfying multi-resource capacity and anti-affinity constraints. Traditional approaches typically rely on fixed rules, which lack adaptability to dynamic cluster states and are difficult to extend for adaptive decision-making. On the other hand, meta-heuristic methods, although more flexible, are often computationally expensive, slower and prone to getting trapped in local optima. In this work, we propose an adaptive and efficient approach based on an LLM-driven multi-agent collaboration framework, where four specialized agents operate in a closed-loop ReAct cycle at e
- id: arxiv:2610.05571
  pool: crossdomain
  title: Scenario-Based Compositional Statistical Model Checking for Safety Specifications
  abstract: In safety-critical domains such as autonomous driving, systems must be evaluated across a large number of environment conditions, often represented as composite scenarios built from primitive scenarios. Existing statistical model checking (SMC) approaches analyze each composite scenario independently, requiring many expensive simulations and resulting in substantial redundant computation when scenarios share common structure. This work introduces a scenario-based compositional SMC framework for safety and co-safety specifications, enabling efficient analysis of composite scenarios. Our approach decomposes scenarios into primitives and specifications into sub-specifications, verifies each pri
- id: news:69fcd4fc5fd03ef0
  pool: finance
  title: Chrome 155 Adds JPEG XL, Post-Quantum Crypto and Wallet IDs - DigitBin
  abstract: Chrome 155 Adds JPEG XL, Post-Quantum Crypto and Wallet IDs DigitBin
- id: news:25a9dbab44a919bd
  pool: finance
  title: Crime Branch finds pattern in alleged loan fraud in multiple banks in Kochi, suspects multi-crore scam - Onmanorama
  abstract: Crime Branch finds pattern in alleged loan fraud in multiple banks in Kochi, suspects multi-crore scam Onmanorama
- id: s2:f6d7343d560103a6ecad76b893cd57b5880c36b5
  pool: finance
  title: Game theoretic translation of historical incentive architectures into modern circular sanitation contracts and commons governance in Vietnam and pre industrial England
  abstract: Modern sanitation engineering has achieved profound public health gains but at the cost of breaking the nutrient cycle, resulting in linear "flush-and-forget" systems that cause eutrophication and resource depletion. Pre-industrial cities sustained circular nutrient economies for centuries through decentralized, self-enforcing institutions. While historical technologies carried pathogen risks, their underlying incentive architectures offer design insights for closing today's nutrient loop. This paper introduces a Historical Incentive Translation Framework that uses game theory to convert documented historical institutional rules into parameterized, testable blueprints for modern circular san
- id: s2:eb14e103d4f412856b2a5347f3ece68f15ed5334
  pool: finance
  title: Segmentation of enterprise value based on regression models: integrating machine learning and financial analysis
  abstract: The article examines the theoretical and methodological foundations of segmented enterprise valuation by integrating financial analysis, statistical segmentation, and machine-learning regression models. It shows that in financial practice, universal valuation models are often applied to structurally heterogeneous groups of enterprises. At the same time, practitioners rarely conduct differentiated assessments based on specific characteristics. This article examines how machine learning can forecast enterprise value and performance. It accounts for the fact that enterprises may differ significantly in financial indicators, size, capital structure, and other characteristics. Consequently, a sin

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

Write the answer to: runs/2026-10-04/llm_responses/novelty_score_000.json
