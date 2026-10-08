# TASK novelty_score_001

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2610.07846
  pool: crossdomain
  title: Scen-Opt: A Scenario Optimization Toolbox for Data-Driven Convex Programming
  abstract: The scenario approach is a well-established statistical framework for data-driven decision-making. In particular, in data-driven optimization, the scenario approach unveils how the problem structure governs out-of-sample generalization, and offers a principled basis for assessing and certifying the reliability of the optimal solution as per constraint satisfaction. Despite its strong theoretical development and wide applicability, no software toolbox has been available to date that enables user-friendly, data-driven convex optimization within the scenario-approach framework. In this paper, we introduce Scen-Opt, an open-source software tool that integrates convex programming with data sample
- id: arxiv:2610.08681
  pool: crossdomain
  title: Juicy Interactive Visualization: Evaluating How Excessive Feedback Design Shapes Visualization Engagement
  abstract: Visualization research has long examined embellishment and animation, while the design of rich interaction-contingent feedback remains under-articulated as a systematic design space. We introduce JuicyVIS, a theory-informed operationalization of juicy feedback for interactive visualization that translates ideas from game studies into a visualization-centered framework. JuicyVIS introduces three dimensions, interaction type, feedback timing, and feedback intensity, which we explore through 26 controlled prototypes, grounded in established visualization interaction categories and prior work on juicy feedback in games. We evaluate the juicy design space through three exploratory mixed-methods o
- id: arxiv:2610.09225
  pool: crossdomain
  title: Lyapunov-Inspired LyRIC Activation and GLARE Attention in Chaos-Guided State Space Modeling for EMG-To-Speech (ETS) Synthesis
  abstract: Electromyography-to-Speech (ETS) synthesis is typically a non-linear, chaotic dynamical system. However, no prior work has studied the chaotic behavior of ETS synthesis to date. Yet, prior works strictly rely on standard reconstruction metrics with parameter-heavy transformers that systematically over-smooth natural acoustic dynamics. To close this gap, for the first time, we propose a chaos-inspired Lyapunov-derived activation function (LyRIC) with two novel chaotic loss functions, Lyapunov Exponent Regularization and Multi-Scale Detrended Fluctuation Analysis, to explicitly capture the deterministic chaos of human phonation. In addition, we introduce a compressed novel encoder, GLAME, whic
- id: arxiv:2610.08263
  pool: crossdomain
  title: CA-Observability of Discrete Event Systems under Cyber Attacks
  abstract: In a previous paper, we investigate the control problem of discrete event systems under cyber attacks, where CA-controllability and CA-observability are proposed. We prove that a discrete event system can be controlled to generate a specification language K if and only if K is CA-controllable and CA-observable. While CA controllability can be "converted" to (conventional) controllability, CA-observability cannot be "converted" to (conventional) observability. In this paper, we further investigate CA-observability. We develop a method and an algorithm to check CA-observability. The method involves constructing an augmented automaton whose states are pairs of the current state and state estima
- id: arxiv:2610.07970
  pool: crossdomain
  title: A Private IPFS Data Sanctuary for Verifiable Digital Collection Objects
  abstract: Background: Galleries, libraries, archives and museums (GLAM) increasingly produce scientific collection data whose digital state must remain identifiable, recoverable, and verifiable after acquisition. A staging architecture should provide redundancy without requiring every measurement to depend on one workstation or storage path. Methods: We evaluated a private seven-node InterPlanetary File System (IPFS) deployment at the Museum für Naturkunde Berlin. Five Raspberry Pi 5 edge peers and two archive-class peers contributed NVMe-backed repositories across two wired zones linked by a shared wireless path. Two real raw-acquisition folders were recovered by content identifier (CID), a large mac
- id: arxiv:2610.09226
  pool: crossdomain
  title: FLoRa: Flight-Assisted Data Collection from Duty Cycling LoRa Nodes under Energy Constraints
  abstract: Data collection using Unmanned Aerial Vehicles (UAVs) is challenging when LoRa IoT Devices (IoTDs) duty-cycle to conserve battery. Under energy constraints, a UAV must decide which IoTDs to visit, in what order, where to hover, and how many times to probe each node, while time-based data freshness decays. Tractably solving this problem requires a multi-level optimization architecture: discrete combinatorial optimization for routing, continuous global optimization for spatial positioning, and sequential decision-making under uncertainty. We propose FLoRa, a Flight-assisted LoRa data collection architecture using Simulated Annealing (SA) for path planning, Covariance Matrix Adaptation Evolutio
- id: arxiv:2610.08929
  pool: crossdomain
  title: Part of the Strassen algorithm can speed up matrix multiplication in a parallel pebbling game
  abstract: We present a novel variant of the Strassen algorithm called the Partial Strassen algorithm, which uses a fraction of the Strassen steps to perform matrix multiplication in less time than traditional implementations. The memory footprint required to implement this algorithm is provably small whether used with a single thread or in a multi-threaded context. Data comparing the Partial Strassen algorithm at depths one, two, and three with BLAS matrix multiplication show that the three-level Partial Strassen algorithm is able to perform matrix multiplication in $80\%$ the time of BLAS with $2.25$ times the memory requirement, with a theoretical improvement of $75\%$ for sufficiently large matrice
- id: arxiv:2610.09069
  pool: crossdomain
  title: Localized Thermal Management of Induction-Heated Microrobots for Hyperthermia Applications
  abstract: Induction-heated microrobots face a fundamental thermal management challenge: the alternating magnetic fields required for localized hyperthermia simultaneously generate parasitic ohmic heating within the actuation coils. Conventional cooling approaches can fail because conductive cooling structures placed near the coil can couple to the time-varying field, generating additional electromagnetic losses. This paper addresses this architectural limitation by evaluating two liquid-cooling frameworks designed to isolate the electromagnetic workspace: an indirect configuration utilizing an external copper water block, and a direct architecture routing coolant internally through a hollow helical co
- id: arxiv:2610.08977
  pool: crossdomain
  title: SNR-Gated LSTM-Conditioned Diffusion Model for MIMO Channel Estimation
  abstract: Accurate and low latency channel estimation is critical for modern MIMO systems, particularly under mobility, where channels exhibit structured sparsity and strong temporal correlation. This paper proposes a time-series conditioned diffusion framework for channel estimation that performs denoising in the angular domain. Starting from least squares (LS) observations, we train a diffusion denoiser whose conditioning information is encoded by a long short-term memory (LSTM) network over a short observation sequence, enabling the model to exploit temporal dynamics beyond per-snapshot estimation. To robustly balance observation fidelity and learned generative priors across a wide signal-to-noise 
- id: arxiv:2610.07953
  pool: crossdomain
  title: Benchmarking System One Models in Online Moderation
  abstract: Online moderation systems must apply changing platform policies, community rules, and prior decisions while producing decisions that can be audited and routed to human review. We evaluate whether System One Models, which accept natural-language context but return typed choices, probabilities, or scores, can support this setting. Across five moderation benchmarks, Jev is competitive with specialized reference systems, matching or exceeding them in several policy-grounded and harmful-content settings. We then use controlled information conditions to separate written rules, retrieved precedents, and restrictions on the candidate answer space. Jev generally benefits from retrieved precedents, im
- id: arxiv:2610.08787
  pool: crossdomain
  title: Algebraic Tensor Network Renormalization and Holographic duality
  abstract: Emergent generalized symmetries and the holographic principle play very important roles in understanding quantum phase transitions. In recent years, tensor-network renormalization with generalized symmetry and the corresponding fixed-point tensor formulation have been proposed as a discrete spacetime framework for reformulating conformal field theory. Nevertheless, a complete holographic formulation within this framework is still lacking, and the current formulation does not directly accommodate sector partition functions that are modular covariant in general. In this work, we formulate $\mathcal{R}$-TNR, which builds the categorical constraints of a fusion category $\mathcal{R}$ into local 
- id: arxiv:2610.07623
  pool: crossdomain
  title: Explicit Asymptotic Bounds for Sequential Calibration Beyond $T^{2/3}$
  abstract: Probability forecasts are calibrated when predicted probabilities match empirical outcome frequencies: among events assigned a probability $p$, we'd hope that the fraction of positive outcomes is close to $p$. We study the problem of sequential forecasting of binary outcomes. The classical $O(T^{2/3})$ bound on expected cumulative $\ell_1$-calibration error established by Foster and Vohra stood for over two decades until Dagan et al. reduced the exponent $2/3$ by an unspecified constant. We establish a new two-phase recursive labeling strategy for the sign-preservation-with-reuse game that yields the bound $O(n^αt^β)$ for all choices of space and time. We then sharpen the reduction from uppe
- id: arxiv:2610.07747
  pool: crossdomain
  title: When Weak Reports Matter: Staged Anchored Fusion for Cooperative UAV Sensing
  abstract: Local multipath rejection can erase evidence needed for cooperative sensing. We propose staged anchored recovery: preserve strong-only confirmations, then query compatible weak reports using unused strong anchors. For any number of sensing nodes, we prove lossless residual screening and derive corroboration and bidirectional cost laws. In 1,024 five-UAV drops, recovery adds 30 matched targets and three false outputs over strict consensus, matching one-pass anchored confirmation's detection counts while reducing weak uploads by 97.4%. Equal-sized cue/report records yield 4.5% less payload than uploading all eligible reports. Independent validation recovers four additional targets with no obse
- id: arxiv:2610.08265
  pool: crossdomain
  title: Closed analytical form of many-body free volume and thermodynamics of monodisperse hard disks
  abstract: The hard disk model is a fundamental reference system for excluded volume physics, liquid structure, and 2D ordering. Yet, despite its apparent simplicity, an analytical formulation of its thermodynamics has remained difficult because the free volume available to disks centers has a highly nontrivial many-body geometry. Here we show that this geometry admits a closed and exact representation: for any given hard disk configuration, the free volume can be analytically expressed through intersection areas of up to five exclusion disks. This provides a direct geometrical route from particle coordinates to the configurational partition function and entropy. We prove that the N disk partition func
- id: arxiv:2610.07724
  pool: crossdomain
  title: Shape theorem for excited random walks on the integer lattice
  abstract: We study the limit shape of the range of the random walk excited to the center on $\mathbb Z^d$, with $d\geq2$. A cookie is placed at each nonzero vertex. On its first visit to such a vertex, the walker consumes the cookie and takes its next nearest-neighbor step with a bias toward the origin. On a visit to the origin, or on later visits to a nonzero vertex, no cookie is available and the walker moves to a neighbor uniformly at random. We prove that the set of vertices visited up to time $n$, rescaled by $n^{-1/(d+1)}$, converges in probability in Hausdorff distance to an explicit $\ell^1$ ball. This answers a question raised by Kozma (2007).
- id: news:a5b40a6ab3eec88d
  pool: finance
  title: Top bank conferences to attend in 2027
  abstract: Connecting with peers and competitors may offer the gut-check that banking leaders need so they can innovate in a way that lets customers and shareholders both prosper.
- id: news:04d2676d6b7dbebd
  pool: finance
  title: Gov't issues consumer alert, launches monthlong effort to prevent fraud after data breaches - The Korea Times
  abstract: Gov't issues consumer alert, launches monthlong effort to prevent fraud after data breaches The Korea Times
- id: news:9210d65bbbe70fc2
  pool: finance
  title: Bancassurance advantage deepens as career banker takes ICICI Life helm - Insurance Business
  abstract: Bancassurance advantage deepens as career banker takes ICICI Life helm Insurance Business
- id: news:b791b9bfc807236e
  pool: finance
  title: Delhi High Court Asks RBI To Caution Banks After Axis Bank's Unilaterally Appointed Arbitrator Handles... - LiveLawBiz
  abstract: Delhi High Court Asks RBI To Caution Banks After Axis Bank's Unilaterally Appointed Arbitrator Handles... LiveLawBiz
- id: hn:49979793
  pool: finance
  title: Show HN: OpenChart – OSS TradingView alternative with your own AI agent
  abstract: Hi HN, I'm Weilun, cofounder of OpenChart. We built OpenChart because we wanted Claude and Codex to interface with the markets, like most of humans do, through charts rather than through CLIs. With your existing AI plans, your agent can work directly with your charts: annotate a setup, write an indicator, investigate a market move, or create an alert. The chart, conversation, and research live in the same workspace. OpenChart alerts on any market move: draw any shape on a chart and attach an alert. When price crosses it, the alert triggers your agent to investigate the move and save the research in your workspace. The agents can work with charts, indicators, and alerts. Custom indicators and
- id: news:326605b593ac771a
  pool: finance
  title: Fintechs press for Fed access
  abstract: Stripe and Ramp executives highlighted their companies’ need for more access to the Federal Reserve’s payment rails during a Fed conference.
- id: news:abae7c82421f8712
  pool: finance
  title: Malaysia's Banks to Test Real-Time Fraud Warnings Before Payments Clear - https://www.briefasia.com/
  abstract: Malaysia's Banks to Test Real-Time Fraud Warnings Before Payments Clear https://www.briefasia.com/
- id: news:cece1cb691505fd3
  pool: finance
  title: Payments conferences for 2027
  abstract: Real-time payments, stablecoins and AI use cases are expected to be among the hot topics at next year’s industry events.
- id: news:6d78610b227a4ac5
  pool: finance
  title: Visa sharpens fraud detection - Gadget
  abstract: Visa sharpens fraud detection Gadget
- id: news:83081d153381adac
  pool: finance
  title: Credit Unions Must Offer Instant Payments to Keep Up With Gen Z: Report - CUTimes
  abstract: Credit Unions Must Offer Instant Payments to Keep Up With Gen Z: Report CUTimes
- id: news:b2bdd6f6ae12ede1
  pool: finance
  title: Bayer's Courtroom Win and Q3 Test: JPMorgan, Deutsche Bank Split on the Quarter but Agree on the Tar - AD HOC NEWS
  abstract: Bayer's Courtroom Win and Q3 Test: JPMorgan, Deutsche Bank Split on the Quarter but Agree on the Tar AD HOC NEWS
- id: arxiv:2610.09141
  pool: finance
  title: A Cognitive-Aware QML-CRL Framework for Detecting Affinity and Romance-Investment Fraud
  abstract: We present a hybrid quantum-classical framework that detects affinity and romance-investment fraud by modelling the cognitive biases in a manipulative conversation. In our proposed framework, cognitive biases central to this fraud class are carried by dedicated qubits in a structured parameterized quantum circuit, together with a frame qubit makes the encoding sensitive to the temporal order of manipulative reframing, and a narrative qubit that aggregates co-occurrence through a trainable entanglement layer. The circuit parameters are trained jointly with a classical reinforcement-learning agent that decides, turn by turn, whether to flag the conversation, modeled as an optimal stopping prob
- id: arxiv:2610.07967
  pool: finance
  title: DecepEval: A Benchmark for Evaluating Deception in LLM Agents
  abstract: As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a benchmark comprising 1,532 instances across 3 task families and 28 professional scenarios. Drawing on classical fraud theories, we propose the LLM Deception Diamond framework, which characterizes four external conditions that may induce deception: pressure, incentive, opportunity, and
- id: arxiv:2610.08631
  pool: finance
  title: Exponential investors with weakly mean-reverting prices
  abstract: We investigate a continuous-time financial market where the asset price exhibits weak (sublinear) mean reversion and has a nonzero drift. Complementing earlier work on strong (superlinear) mean reversion, we show that, for an investor maximizing expected exponential utility, the certainty equivalent grows as $O(T^{2β+1})$ where $0<β<1$ is the strength of mean reversion. An explicit asymptotically optimal strategy is also given.

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

Write the answer to: runs/2026-10-06/llm_responses/novelty_score_001.json
