# TASK novelty_score_000

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2610.09398
  pool: crossdomain
  title: IVG-UAV: An Intelligent Voice-Guided UAV System for Autonomous Ripe Fruit Harvesting with Vision-Based Classification and Adaptive Path Planning
  abstract: In tropical regions, their agricultural sectors remain highly dependent on manual labor for fruit harvesting. On large-scale farms, this dependency often results in significant labor cost and logistic complexities. This project presents the development and simulation of a voice-controlled Unmanned Aerial Vehicle (UAV) system designed to automate harvesting tasks in extensive plantations. The proposed system integrates speech recognition using Whisper [1] and LLM, computer vision-based ripeness classification, and adaptive path planning within a unified framework. The entire system is modeled and validated in a Gazebo simulation environment, allowing performance evaluation under controlled ag
- id: arxiv:2610.09617
  pool: crossdomain
  title: Second-order optimization of variable projection SVM models and road abnormality detection
  abstract: We introduce a novel second-order optimization framework for minimizing so-called variable projection functionals. We demonstrate that the proposed framework is especially usefulfor the training of variable projection based kernel methods. In particular, the problem of efficiently training variable projection support vector machines (VP-SVMs) is considered. We show the effectiveness of the proposed training methodology in a real-world application, namely we demonstrate how second-order trust region algorithms can be used to train VPSVM models to recognize road surface abnormalities based on 1D signals obtained from a tire sensor.
- id: arxiv:2610.10001
  pool: crossdomain
  title: Cotunneling-Assisted Redistribution of Nonpassivity in a Photosynthetic Junction
  abstract: We investigate how cotunneling affects passive-state ordering in a Photosystem II reaction center modelled as a nonequilibrium molecular junction. We use a full pigment excitation manifold, with excitonic and charge-transfer rates computed within a Nakajima-Zwanzig formalism using realistic spectral densities. Cotunneling is introduced through a microscopically constructed doubly reduced acceptor state obtained from relevant quinone-side two-electron configurations, while photoexcitation is allowed into the full excitonic manifold. Passive-state permutations are quantified through ergotropy and energetic capacitance. We find that thermodynamic smoothness in ergotropy and energetic capacitanc
- id: arxiv:2610.09379
  pool: crossdomain
  title: Unified Relative Orbital Element Framework for Eccentric Formation Flying
  abstract: Quasi-nonsingular relative orbital elements (qnsROE) are among the most widely used state representations for formation flying and rendezvous in near-circular inclined orbits. They admit closed-form perturbed state transition matrices (STMs) and a direct geometric mapping, which underpins eccentricity/inclination (E/I)-vector separation for passive safety. Existing eccentric extensions of the qnsROE resolve this geometry in the radial--tangential--normal frame, where a residual semimajor-axis difference makes the E/I separation margin phase dependent. This paper introduces eccentric ROE that reduce to the qnsROE as \(e\to0\) and whose first-order geometry is resolved in the velocity--normal-
- id: arxiv:2610.09327
  pool: crossdomain
  title: MCFR: A Mask-Guided Coarse-to-Fine Regression Framework for Robust Multi-Variant Board-to-Board Connector Assembly
  abstract: Automated insertion of board-to-board (BTB) connectors in 3C manufacturing requires both high visual accuracy and strong deployment robustness. This problem remains challenging because multi-variant connectors exhibit significant morphological and appearance variations, making stable cross-variant generalization difficult, while the mismatch between training and deployment under fixed-view inspection settings induces background spurious correlation and degrades real-world performance. To address these issues, this paper proposes MCFR, a Mask-Guided Coarse-to-Fine Regression framework for multi-variant BTB connector assembly. By introducing an object-aware mask prior and explicit photometric 
- id: arxiv:2610.09262
  pool: crossdomain
  title: Reading Position Is the Baseline to Beat: A Time-Ordered Evaluation of Personalised Highlight Prediction
  abstract: A reader's first highlights on a page are the cheapest personal signal a reading product has. The natural plan is to suggest what similar earlier readers marked, and to judge the result against popularity. We argue that the baseline to beat is reading position. In a time-ordered evaluation on one social highlighting platform (7,343 reader-page pairs on 1,511 pages after one highlight), ranking the sentences just below a reader's first highlight, with no other reader's data, puts the next highlight in the top five 47% of the time, against 26% for popularity and 29% for the better of two similarity methods. The baseline depends on the target: over all later highlights that ranking loses to pop
- id: arxiv:2610.10517
  pool: crossdomain
  title: Unsupervised Maneuver-Aware Acoustic Fault Detection for Autonomous Drones
  abstract: This paper presents a maneuver-aware acoustic fault detection framework for autonomous drones that integrates Noise2Noise-inspired deep learning denoising with maneuver-conditioned reconstruction. A key practical constraint motivating this work is that labeled faulty-flight data are difficult and potentially unsafe to collect; the proposed framework therefore follows an unsupervised learning paradigm in which only nominal flight recordings are required for training. In flight environments, acoustic signals acquired from unmanned aerial vehicles are subject to variability arising both from environmental noise and from structured, maneuver-dependent aerodynamic effects. To address these challe
- id: arxiv:2610.09883
  pool: crossdomain
  title: Adjusting for Social Groups in Spatial Point Process Models for Waiting Pedestrian Configurations
  abstract: The spatial distribution of waiting pedestrians has two primary drivers: environmental preference and interaction with other pedestrians. Spatial point processes naturally capture both spatial heterogeneity and repulsive interaction. In previous work (Sickert Karam et al., arXiv:2606.14532, 2026), we proposed a Gibbs model with inhomogeneous intensity and a modified Diggle-Gates-Stibbard interaction function, which reproduces many phenomena in replicated patterns of pedestrians waiting at a train station. Its single interaction function acts as an effective interaction, averaging over behavioral regimes such as interactions within social groups and among strangers. In this article, we show h
- id: arxiv:2610.09285
  pool: crossdomain
  title: LeCuration: A Tiny World Model as a Data Curation Multi-Tool
  abstract: Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior. Examples include robots working in a warehouse and agents moving around in a video game. In order to better organize, filter, and curate data for physical AI applications, we propose a new approach centered on the unique settings and physical laws of individual datasets. We train LeCuration, a small world model intended to serve as a data curation tool for a separate, larger downstream model. To build this model, we choose LeWorldModel (LeWM)as our latent encoder and predictor, adding a diffusion transformer (DiT) decoder to add visuals to autoregressive
- id: arxiv:2610.09334
  pool: crossdomain
  title: VM-ARRAYDPS: Virtual Microphone Augmented Diffusion Posterior Sampling for Unsupervised Blind Speech Separation
  abstract: Blind Source Separation(BSS) is a fundamental problem in signal processing, aiming to separate multiple source signals from their mixtures without prior knowledge of the sources or the mixing process. Traditional approaches, such as Independent Vector Analysis (IVA) exploits statistical independence of sources. Recently, diffusion-based approaches have emerged as a promising alternative by leveraging powerful generative priors. Among them, ArrayDPS formulates BSS problem as a posterior sampling problem, and utilizes a pretrained speech diffusion model to guide the recovery of clean source signals. A key factor behind its separation capability is the multi-channel consistency (MC) objective, 
- id: arxiv:2610.09580
  pool: crossdomain
  title: Beyond FAIR: A Fitness Function Framework for Sustainable Research Software
  abstract: Research software sustainability is often assessed through the FAIR principles: findability, accessibility, interoperability and reusability. While important, FAIR does not cover all relevant sustainability concerns. Research software should also be environmentally responsible and secure over time. Excessive resource consumption increases environmental cost, while insecure software creates maintenance overhead, technical debt and barriers to reuse. To this end, in this paper, we extend a previously proposed fitness function framework for sustainable research software beyond FAIR. We introduce two additional sets of fitness functions: environmental functions targeting resource efficiency and 
- id: arxiv:2610.09766
  pool: crossdomain
  title: Performance Portable $\mathrm{SU}(N)$ Lattice Gauge Theory Simulation with Kokkos
  abstract: The increasing diversity of high performance computing systems makes separate, architecture specific implementations of lattice gauge theory algorithms costly to maintain. We present \texttt{kwqft}, a performance portable Kokkos implementation of Wilson pure gauge Monte Carlo simulation for $\mathrm{SU}(N)$ Yang-Mills theory in an arbitrary number of space-time dimensions. The gauge group order $N$ and the dimension $D$ are compile time parameters. A single source targets the Serial, OpenMP, CUDA, HIP, and SYCL execution spaces, with MPI halo exchange overlapped with interior updates. The implementation reproduces the exact two-dimensional plaquette and published three and four dimensional v
- id: arxiv:2610.09315
  pool: crossdomain
  title: ClimbLab: MATLAB Simulation Platform for Legged Climbing Robotics
  abstract: This paper presents an open-sourced MATLAB simulation and analysis platform dedicated to legged climbing robots. This simulator enables the design of any limbed robotic system as an articulated multi-body with a floating base and simulates it walking and climbing in an arbitrary environment. The main variable environmental parameters are inclination, gravity, and ground stiffness, and any point cloud can be installed as the terrain map. Furthermore, the simulator employs a rigid body dynamics engine. This paper first describes the simulator structure, and the computational flow and next presents the representative simulation examples where quadrupedal robots assumed gripping on the wall or c
- id: arxiv:2610.09730
  pool: crossdomain
  title: Trust a Few: The Weakest Assumptions a Protocol Needs
  abstract: Protocol verifiers check whether a protocol meets a security goal under stated trust assumptions, such as that a key is never leaked, a value is fresh, or a channel is authentic. They do not say which of those assumptions the goal needs. Rowe, Guttman and Liskov asked for the weakest assumptions under which a protocol achieves a goal and left the question open. We answer it for assumptions about keys, values and channels. Call a run that violates the goal an attack, and the assumptions that would rule it out its stopping set. The least a protocol must trust to meet a goal is exactly the set of minimal ways to stop all of its minimal attacks. Several such sets may exist. The answer becomes un
- id: arxiv:2610.09855
  pool: crossdomain
  title: Spacetime Quasicrystals and Computational Complexity Theory in the Road Towards Quantum Gravity
  abstract: Part I: Semiclassical Gravity Efficiently Solves $\mathsf{NP}$-Complete Problems Assuming the gravitational field is classical and that it couples to quantum fields via the semiclassical Einstein field equations (EFEs), we show that the weak-field dynamics of a massive and non-relativistic qubit can in principle be used to solve an $\mathsf{NP}$-complete problem in polynomial time. We attribute this vast computational power to the non-linear qubit dynamics afforded by the semiclassical EFEs. Consequently, the above two assumptions entail a violation of the Physical Extended Church--Turing Thesis, which we regard as evidence for the quantization of gravity. Part II: Spacetime Quasicrystals We
- id: arxiv:2610.09776
  pool: crossdomain
  title: Stimulated emission for a three-level artificial atom in waveguide quantum electrodynamics
  abstract: This work is devoted to a theoretical study of the interaction of a quantum three-level ladder system with a continuous electromagnetic field in a one-dimensional open waveguide. We consider a situation closely resembling stimulated emission - the scattering of a single-photon exponential pulse by an excited three-level emitter. Using the real-space formalism, we obtain an analytical expression for the wavefunction of our system. We show that, for the low anharmonicity of a three-level system inherent to a transmon (the most common type of artificial atom), the influence of the third level can have a significant effect on the system's behavior. Namely, the presence of the third level largely
- id: arxiv:2610.09747
  pool: crossdomain
  title: A Minimal Bicomplex Extension of the Complex Scalar Algebra of Quantum Mechanics with an Ideal-Valued Sector
  abstract: Standard quantum mechanics takes the complex numbers as its scalar algebra. We ask whether this complex structure is algebraically fundamental or may instead form a distinguished embedded sector of a larger commutative and associative scalar algebra. Requiring the ordinary complex sector to remain intact while admitting an additional stable complex-like analytic sector turns the latter into a proper ideal, makes zero divisors unavoidable in finite dimension, and implies a lower bound of four real dimensions. The bicomplex algebra realizes this minimum, and under an additional compatibility assumption the four-dimensional realization is unique up to isomorphism. The resulting algebra exhibits
- id: arxiv:2610.09405
  pool: crossdomain
  title: Heat Transport of the $β$-Fermi--Pasta--Ulam--Tsingou chain in the long-wave limit
  abstract: Resolving the anomalous conductivity exponent of the symmetric $β$-Fermi--Pasta--Ulam--Tsingou chain by molecular dynamics can require very large systems because of long finite-size crossovers and thermal-contact resistance. Motivated by this computational challenge, we derive a long-wavelength continuum description and investigate whether the kinetic-theory scaling $κ\propto L^{2/5}$ becomes accessible with a moderate number of numerical degrees of freedom. The nonlinear elastic field retains the cubic stress of the microscopic interaction and exchanges heat with Langevin reservoirs. A flux-conservative spatial discretization constructs the force and energy current from the same stress, pro
- id: arxiv:2610.10075
  pool: crossdomain
  title: BetweenCut: Private Heavy-Node Classification with Doubly Logarithmic Error in Tree Height
  abstract: Finding heavy nodes in a tree---those whose counts exceed a given threshold---is a building block for analysis and learning over structured data. Achieving record-level differential privacy (DP) without sacrificing accuracy is challenging because each record contributes to counts along an entire root-to-leaf path, allowing privacy costs to accumulate across levels. Existing methods account for the multiple threshold comparisons for each record incur additive error margins of $Ω_{\varepsilon,δ}(\log h)$ or $Ω_{\varepsilon,δ}(\sqrt{\log h})$ for tree height $h$. We introduce \textsc{BetweenCut}, an $(\varepsilon,δ)$-DP algorithm with an additive error margin of $O_{\varepsilon,δ}(\log\log h)$,
- id: arxiv:2610.09632
  pool: crossdomain
  title: Age of Information in Queueing Systems with Merging Server Streams
  abstract: We present a novel analytical framework for evaluating the age of information (AoI) in multi-path queueing topologies where output streams from multiple servers converge into a single pipeline. This theoretical scenario finds immediate application in ultra-reliable low-latency networks and edge computing architectures, where multi-path routing and stream merging can be vital strategies for maintaining fresh status updates. Specifically, we investigate two setups: a split-merge network and a duplicate-merge network. The split-merge case has been addressed in prior work, but we show that existing studies are incorrect, and our approach provides instead an exact analytical formulation. Moreover
- id: arxiv:2610.10441
  pool: crossdomain
  title: CrossWeave: Bridging Perspectives Across Online Communities with a Dual-Pane Design
  abstract: Social media systems typically display conversations among already familiar contributors, which can be predictable and one-sided. In civic discourse, this design narrows discussion, reinforces divides, and distorts the perception of public opinion. To encourage cross-community engagement, we present CrossWeave, an AI-powered bridging system that augments the standard social media feed. As the user reads a post, CrossWeave surfaces diverse relevant posts from other threads in a side pane and highlights the connections. Users are invited to venture out of their echo chamber, explore a broader range of views and arguments, and ``click across'' to engage with their authors. When they do, CrossWe
- id: arxiv:2610.09697
  pool: crossdomain
  title: Automotive Hardware Attacks: An Architect's Guide to TARA
  abstract: Threat analysis and risk assessment (TARA) according to ISO/SAE 21434 treats implementation-level hardware attacks inconsistently. We show that two of the three attack-feasibility approaches exemplified in the standard rate every attack path that requires physical access as very low by construction, independent of the implementation, while the third can assign the same path any of the four ratings, depending on the assumed state of attacker knowledge and on the attacker profile. This paper presents a hardware-aware extension of the TARA that covers side-channel analysis (SCA), fault-injection attacks (FIA), and abuse of debug and test interfaces. It adds an attacker model for physical access
- id: arxiv:2610.10096
  pool: crossdomain
  title: Revealing more on complex energy landscapes by passing less local information: Cavity approach with trust region in non-convex optimization problems
  abstract: Energy landscapes of non-convex optimization problems are high-dimensional surfaces that are difficult to reveal, visualize, or analyze. Message-passing algorithms, or equivalently cavity approaches in statistical physics, may fail to identify local minima as messages do not converge owing to the ruggedness of the energy landscapes. Here we aim to reveal the characteristics of these complex energy landscapes by limiting the amount of information passed in local messages, improving the convergence of messages for local minima. By studying a routing optimization problem with its convexity governed by a single parameter, we introduce a cavity message-passing algorithm with a trust region, and s
- id: arxiv:2610.10148
  pool: crossdomain
  title: Reconciling Bottom-Up Metrics with Top-Down Reporting for Cloud Carbon Accounting
  abstract: Organizations seeking to reduce the carbon footprint of their cloud applications must rely on two largely disconnected ways of measuring it, each with important limitations. Bottom-up metrics like Software Carbon Intensity (SCI) provide signals for carbon-aware optimization, but tenants lack the information needed to account for many provider-side overheads. Top-down reports by cloud providers provide a more comprehensive view of a tenant's carbon footprint but are coarse and methodologically opaque. Because the two approaches differ in scope and reporting frequency, the current state of the art treats them as decoupled: bottom-up metrics for optimization, top-down reports for corporate disc
- id: arxiv:2610.10487
  pool: crossdomain
  title: LOCAA: An Agentic System for Automated Lossy Compressor Tuning
  abstract: Large-scale scientific simulations generate substantial data volumes, making lossy compression essential for reducing storage and data movement costs. However, users configure compressors through numerical error bounds (EBs) while often evaluating results using quality metrics and end-to-end performance. Because the relationship between an EB and these outcomes varies across datasets and compressors, identifying a suitable configuration typically requires exhaustive search, which can be time-consuming and computationally demanding. We present LOCAA, an Large language model-based scientific lossy compression auto-tuning agent that performs compression-in-the-loop search using tool-integrated 
- id: arxiv:2610.09619
  pool: crossdomain
  title: Predicting activation-barrier and plasticity-onset statistics in a model of glasses
  abstract: A recently introduced anharmonic mean-field model unifiedly reproduced a broad range of low-temperature glass phenomena --- including harmonic nonphononic spectral properties, linear micromechanics and strongly driven elasto-plastic dynamics --- indicating that its underlying energy landscape is intrinsically glassy. Here, we apply a nonlinear modes framework to the model and derive analytic predictions for the asymptotic distributions of activation barriers $p(Δ{U})\!\sim\!(Δ{U})^{1/4}$ and the external force needed for the onset of plasticity $p(f_{\rm c})\sim f_{\rm c}^{2/3}$, for their extreme-value scaling and for $\langleΔ{U}\rangle$ beyond the asymptotic regime. These predictions are 
- id: arxiv:2610.09583
  pool: crossdomain
  title: Connectome-Based Modeling of Mutation-Specific Amyloid-$β$ Aggregation in Familial Alzheimer's Disease
  abstract: Familial amyloid-$β$ (A$β$) variants alter aggregation kinetics, but their interaction with structural brain connectivity remains incompletely understood. We developed a mutation-aware mechanistic model coupling a coarse-grained monomer--oligomer--fibril aggregation--fragmentation system to graph diffusion on the 540-node Budapest Reference Connectome component. Experimental A$β_{42}$ nucleation scores scaled primary nucleation rates for seven variants relative to wild type. Robustness was examined using mutation-score uncertainty, alternative kinetic mappings, global sensitivity analysis, seed and edge-weight perturbations, degree-preserving randomized connectomes, spatial propagation analy
- id: arxiv:2610.09744
  pool: crossdomain
  title: Mathematical statistics of wild mammal biomass
  abstract: Using the recently published global census of the biomass of wild terrestrial mammals, we perform a detailed mathematical statistical analysis of its distribution over $N_s=4795$ species, drawing on tools developed in economics to characterize wealth inequality. We show that the Lorenz curve of the mammal biomass distribution is characterized by a large Gini coefficient $G=0.944$ exceeding the inequality reported for wealth distribution among world countries. This distribution is compared to the predictions of the Wealth Thermalization Hypothesis (WTH), in which species biomass values are treated as energy levels populated according to a Rayleigh-Jeans (RJ) steady-state distribution. We show
- id: arxiv:2610.09936
  pool: crossdomain
  title: Heat transport in weakly anharmonic Fermi-Pasta-Ulam-Tsingou chains
  abstract: We investigate anomalous heat transport in the one-dimensional $β$-Fermi--Pasta--Ulam--Tsingou chain in the weakly anharmonic regime using large-scale equilibrium molecular dynamics. By resolving the heat current into phonon-mode contributions, we show that its long-time autocorrelation is controlled by diagonal mode correlations, whose decay is quantitatively determined by the corresponding phonon damping rates. Extrapolation to the thermodynamic limit gives $Γ_k \propto (βT)^{4/3} k^{5/3}$, with a subleading $k^2$ correction. The latter produces an extended pre-asymptotic regime, $C(t) \sim t^{-4/5}$, before the asymptotic decay $C(t) \sim t^{-3/5}$ is reached, leading to $κ(N) \sim N^{2/5
- id: arxiv:2610.09815
  pool: crossdomain
  title: Singlet sector of the vector model with angular potential
  abstract: We study the singlet sector of large-$N$, $O(N)$ vector model on $S^1_β\times S^2_r$ in presence of an angular potential $Ω$. We compute the free energy of the model both at the free fixed point as well as the non-trivial fixed point. The model undergoes a phase transition when the temperature $T$ and angular potential attain the relation $T^2r^2\sim N (1-ω^2)$, where $ω=rΩ$ and $r$ is the radius of $S^2$, with $Tr\gg1$, at both the fixed points, with different numerical coefficients. The transition was studied earlier at zero angular potential at $Tr\sim \sqrt{N}$. The holonomy eigenvalue distribution, having support on the full circle below the transition, develops a gap above it, called t

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

Write the answer to: runs/2026-10-07/llm_responses/novelty_score_000.json
