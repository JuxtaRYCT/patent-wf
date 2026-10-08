# TASK novelty_score_002

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2609.38105
  pool: crossdomain
  title: FORM: Robot Manipulation through Direct Material Law Identification
  abstract: When interacting with an unfamiliar deformable material, a robot lacks prior knowledge of its physical properties and how it will respond to applied forces and motion. Rapid online identification is therefore essential for reliable manipulation. We present FORM (From Observed Response to Material laws), which identifies material properties from a single robot interaction and reuses the recovered model to plan manipulation under new actions and geometries. We use weak-form momentum balance to convert observed material motion and contact forces into linear equations in the unknown material parameters. These equations are assembled using the same material point method discretization as the forw
- id: arxiv:2609.36566
  pool: crossdomain
  title: On the Lack of Periodicity of Walker Satellite Constellation Routing Tables
  abstract: In a referential that rotates with Earth, the dynamics of the configurations of satellites in a Delta Walker constellation can be analyzed as a dynamical system as a function of a translation on the torus. This paper extends this type of analysis to routing over a Walker constellation, leveraging fixed ground relays. It considers any deterministic, time-invariant routing rule on such a collection of satellites and relays. The main object of interest is the routing table associated with this rule, which specifies, for all source-destination pairs, a route made of satellites and relays between them, for instance the shortest, together with angular information on next hop at each step of the ro
- id: arxiv:2609.08776
  pool: crossdomain
  title: Hi-M imaging of chromatin architecture in adult Drosophila brain cryosections
  abstract: Hi-M combines fluorescence in situ hybridization (FISH), automated microfluidics, sequential imaging, and computational chromatin tracing to measure the three-dimensional organization of selected genomic regions in single cells. This chapter describes a Hi-M workflow adapted for cryosections of adult Drosophila melanogaster brains, enabling chromatin tracing while preserving tissue architecture and cell identity. The protocol covers Oligopaint library design and amplification, fixation, brain dissection, cryoprotection, cryosectioning, sequential RNA-FISH for cell-type identification, sequential DNA-FISH labeling, automated acquisition, and chromatin trace reconstruction. We also provide pra
- id: arxiv:2609.30960
  pool: crossdomain
  title: Packet iSlip
  abstract: This paper examines input/output buffered crossbar switches under combined packet and cell data. Our switch architecture uses input buffering with Virtual Output Queues to avoid Head of Line Blocking. The switch fabric is a crossbar with no speedup. We use a modified iSlip [McKeown] crossbar scheduler geared towards packet data, called piSlip. Cell ports are largely unmodified from standard iSlip behavior. For packet output ports, we introduce changes to the grant pointer which minimizes output latency caused by packet reassembly. Our model uses several output states, including packet cut-through. From simulation results, we show that piSlip with virtual cut-through offers latency characteri
- id: arxiv:2609.38054
  pool: crossdomain
  title: Pow3R-SLAM: Real-Time RGB-D SLAM with 3D Reconstruction Priors
  abstract: We present Pow3R-SLAM, a real-time RGB-D simultaneous localization and mapping (SLAM) system that uses Pow3R for tracking and mapping. Inspired by MASt3R-SLAM, a recent work on monocular SLAM using two-view 3D reconstruction priors, we extend the work to incorporate depth as a prior on the network's prediction, rather than as geometry to fuse. Where traditional RGB-D SLAM systems struggle with sparsity in the depth images, Pow3R utilizes the available depth to give a better-conditioned pointmap, while inferring the depths in empty regions from the two-view photometric, depth, and intrinsic data. Evaluated against MASt3R-SLAM following its protocol on 24 sequences from TUM, 7-Scenes, and Repl
- id: arxiv:2609.30356
  pool: crossdomain
  title: AlphaEarth distinguishes cities but compresses urban variation
  abstract: Cities differ in built form, land cover and development history, complicating comparison across places and time. Satellite foundation models map Earth's surface onto common numerical representations. Yet the tasks and targets used to shape them typically do not focus on cities: globally consistent labels for urban function do not exist, and many datasets - especially land cover and land use classifications - collapse the built environment into few classes. Here we audit the representation, focusing on AlphaEarth but with broader applicability to other Earth embeddings, by probing the geometry and geography of embeddings for 1,000 urban areas in 162 countries. We find that cities occupy a shi
- id: arxiv:2609.37069
  pool: crossdomain
  title: Windowed and Quantized Group-Based ADMM for Distributed Optimization in Heterogeneous Edge Networks
  abstract: Distributed optimization in edge networks is constrained by heterogeneous client computing capabilities and limited communication resources. We propose the Windowed and Quantized Group-Based Alternating Direction Method of Multipliers (WQ-GADMM) to coordinate group updates under limited activation capacity and reduce communication costs. Clients are grouped by estimated computation time. Each window activates a limited number of groups per round, and the cloud updates the global model after all groups have updated once. The method quantizes both downlink and uplink model exchanges to reduce communication costs and allows bounded model staleness and inexact proximal local updates. For smooth 
- id: arxiv:2609.20101
  pool: crossdomain
  title: Competing for a Finite Pool of Attention in Social Media? How a New Geopolitical Conflict Reshapes Engagement in Bluesky
  abstract: Major geopolitical crises can rapidly reshape online public attention. Yet population-level increases in discussion volume about a new crisis reveal little about how users accommodate this new demand for attention. We study the onset of the Iran-US-Israel conflict, triggered on 28 February 2026, using longitudinal repost activity from Bluesky across four consecutive approximately three-month windows spanning the period before and after its onset; the data comprise 91.0 million unique posts and 645.5 million repost observations. We find that the new conflict reorganized participation through both reallocation among existing conflict participants and substantial activation of previously low-co
- id: arxiv:2609.37560
  pool: crossdomain
  title: RoboFin3D: A Sim-to-Real Platform for Robotic Surface Finishing
  abstract: Grinding and sanding are fundamental processes in industrial robotic surface finishing. However, physical trials are expensive and consume workpieces, making reproducible experiments difficult. We present RoboFin3D, a sim-to-real platform built on Isaac Sim and the Newton physics engine, that provides physics-based grinding and sanding simulation for cheap and repeatable robotic surface finishing experiments. RoboFin3D utilizes a signed distance field (SDF) to model the changing geometry of the workpiece, enabling contact computation, live updates and rendering without an intermediate mesh. It additionally uses a separate surface field to model progressive surface appearance change during sa
- id: arxiv:2609.34956
  pool: crossdomain
  title: Models of Ecological Fitting
  abstract: Ecological fitting describes a situation where species interact despite no shared evolutionary history. It is both a null model for adaptation and an important process in its own right, for example, the establishment of a non-native species is ecological fitting, and it is a major mechanism in the formation of Novel Ecosystems. In this paper we introduce and analyse a model of ecological fitting. We demonstrate both analytically and through simulation that the main factors determining invasion success are the invaded ecosystem's population and diversity, which set the size of the barrier for invaders. We also study the situation where many evolutionarily unrelated species simultaneously colo
- id: arxiv:2609.26696
  pool: crossdomain
  title: Reading the Sky to Forecast the Ground: Physics-Informed Link-State Forecasting for LEO Networks at Any Location
  abstract: In this paper, we introduce Gnomon, a physics-informed system that forecasts user-perceived low-Earth-orbit (LEO) downlink throughput, uplink throughput, and round-trip time (RTT) under different levels of trace availability. Gnomon's physics layer reconstructs the serving geometry and four-leg bent-pipe attenuation from public weather, orbital, routing, and licensing data. Based on what is available, Gnomon conditions on the target terminal's own history (Mode 1), measurements from nearby publicly reachable dishes (Mode 2), or the physical covariates alone (Mode 3) to predict the link state: Modes 1 and 2 share a fine-tuned time-series foundation model, while Mode 3 uses a compact boosted-t
- id: arxiv:2609.18289
  pool: crossdomain
  title: Linking Speakers of the German Parliament to Wikidata: Scope and Coverage of Metadata
  abstract: This paper links all individuals who spoke in the German Bundestag between 1949 and 2021 to Wikidata, creating a longitudinal dataset that connects parliamentary speech transcripts with structured biographical metadata. We evaluate the coverage, composition, and potential biases of the retrieved properties and statements, with particular attention to gender, professional background, historical legacies, and transnational dimensions such as place of birth, languages, and foreign awards. The results demonstrate both the analytical potential of combining GermaParl with Wikidata and the importance of critically assessing uneven metadata coverage in open knowledge graphs.
- id: arxiv:2609.24683
  pool: crossdomain
  title: Semi-Monotonicity for Spectral Centrality Measures
  abstract: Score monotonicity and rank monotonicity are properties describing the behavior of a centrality measure when an arc is added to a network: the former requires that the score of the target of the arc should increase, the latter that its importance with respect to the remaining nodes should not deteriorate. While in directed networks almost all classical centrality measures satisfy both properties, in undirected networks they fail for most measures: adding an edge can reduce the score or the rank of one of its endpoints. Semi-monotonicity is a recently introduced weaker property for undirected networks, requiring that at least one of the two endpoints of the new edge enjoys monotonicity, and i
- id: arxiv:2609.31864
  pool: crossdomain
  title: AirLog: Store-Level Indoor Life Logging Made Easy
  abstract: This paper presents AirLog, a smartphone-based life journaling system that automatically reconstructs users' store visits in shopping malls and summarizes them into human-readable journals. Unlike conventional indoor localization systems, AirLog avoids labor-intensive radio-map construction and dedicated wireless localization infrastructure and algorithm calibrations. Instead, it repurposes two cues already available in commercial spaces: semantic information exposed by ambient Wi-Fi SSIDs and indoor directory images. AirLog converts directory images into spatial maps and fuses Wi-Fi semantic anchors with inertial dead reckoning to recover store-level trajectories, which are then summarized 
- id: arxiv:2609.25908
  pool: crossdomain
  title: User Influence Analysis Based on Blogs
  abstract: Rumor and word of mouth spread at the same speed as the highway of information diffusion in the age of the internet. Social networks play quite an important role in the huge internet. Nowadays, social networks have become indispensable in our lives, especially for the government and enterprises. A social network becomes a complex information diffusion network with users working as nodes and the relationships between users working as the vehicle. In this paper, we propose three kinds of algorithms for computing user influence based on the behavior of a user's forwarding microblogs and the symbol of @ in microblogs. We evaluate the effectiveness of the algorithms by comparing the results of ou
- id: arxiv:2609.37126
  pool: crossdomain
  title: Adversarially Robust Geometric Safety Certificates for Nonholonomic Robots Against Maneuvering Obstacles
  abstract: Safe navigation against obstacles that can actively maneuver within bounded capabilities remains challenging: robust control barrier function methods typically treat obstacle actions as generic disturbances, while differential-game approaches are computationally expensive for online navigation. We propose an adversarially robust geometric certificate that accounts for the worst-case effect of admissible obstacle maneuvers directly in the safe-set geometry through a closed-form contraction of the certificate parameters. The construction exploits a structural property of line-of-sight (LoS) certificates: the robot and obstacle actions enter the certificate through a common state-dependent geom
- id: arxiv:2609.02365
  pool: crossdomain
  title: Beyond species area curves: a theoretical approach to the relationship between diversity and area
  abstract: Species area curves, which describe the number of species present as a function of area, have long been used to understand biodiversity and inform conservation efforts. While understanding the number of species is important, it leaves out information about the population sizes of each species. In this work, we examine the relationship between the effective number of species from different diversity indices, like Simpson's index and the Shannon index, and area. These effective number of species are also referred to as Hill numbers. Using a spatial and neutral model that has previously been used to understand species area curves, we show through a combination of theory and simulations that the
- id: arxiv:2609.36156
  pool: crossdomain
  title: Traffic Congestion Awareness and On-Demand Distribution in Vehicular Delay-Tolerant Networks in California I-210 Freeway
  abstract: In vehicular networks under edge computing environments, vehicle-to-vehicle delay-tolerant networking (V-DTN) can disseminate congestion warnings to other vehicles via a store-carry-forward mechanism, helping them proactively choose suitable routes. However, most existing in-vehicle information dissemination methods rely on flooding or limited flooding strategies, broadcasting alerts across the entire network whenever congestion is detected. This leads to excessive redundant copies and consumes node cache space. To address this issue, this paper proposes a congestion-event- aware on-demand message dissemination mechanism. By considering the recurrence and duration of congestion, the mechanis
- id: arxiv:2609.36898
  pool: crossdomain
  title: Volcanite: Commodity-Hardware Segmentation Volume Visualization for Connectomics and Beyond
  abstract: Modern imaging produces terabyte-scale segmentation volumes, assigning each voxel an object label. These categorical, boundary-sensitive and label-rich data underpin connectomics and other imaging-driven fields, yet their scale often forces interpretation through slices, approximate meshes or distributed workflows that obscure spatial context and voxel-level defects. Here we show that such volumes can be explored directly on commodity hardware with Volcanite, an open-source framework for dense-segmentation rendering. Combining compression-aware data handling, a Vulkan GPU backend and segmentation-specific rendering, Volcanite enables low-latency exploration without meshing or distributed inf
- id: arxiv:2609.34953
  pool: crossdomain
  title: From Early Participation to Later Completion: Evidence from a Large-Scale Self-Paced Learning Programme
  abstract: Large-scale learning programmes generate records that make learner participation observable across different activities. Participation points are commonly used to record and encourage such participation, but their value may extend beyond the activities for which points are awarded. Existing evaluations often examine gamification outcomes within the activities or learning environments in which the game elements are implemented, providing limited evidence about whether early participation points contain information about later participation outside the points system. This study examines whether early participation points can provide information about learners' later participation in a self-pac
- id: arxiv:2609.35331
  pool: crossdomain
  title: Reverse Sequential Proportional Approval Voting Rule: Proportionality and Approximation Guarantees
  abstract: We study the Reverse Sequential Proportional Approval Voting Rule (RevSeqPAV) in approval-based committee elections. Despite its historical prominence and practical use, its properties and guarantees are much less understood than those of Sequential PAV. We analyze it along two dimensions: proportional representation (measured by Extended Justified Representation, its approximations, and proportionality degree) and approximation of the maximum PAV score of instances. We first establish strong negative results for general, unrestricted election instances and then identify settings in which the rule provides meaningful fairness and optimization guarantees.
- id: arxiv:2609.22322
  pool: crossdomain
  title: Spike Sorting with VanillaSort
  abstract: Training spike detectors on real recordings is challenging because algorithmically generated labels can be noisy and incomplete. We propose VanillaSort, combining multichannel detection with spatially augmented, template-guided clustering. VanillaDet uses visibility-aware masking, truncated Gaussian targets and a temporally tolerant positive-bag loss, followed by conditional event-SNR gating. VanillaCluster combines HuiduRep embeddings with relative-amplitude features for Gaussian mixture clustering and refines assignments using cross-fitted waveform templates built from selected core events. VanillaDet improves detection accuracy over SimSort by two and three percentage points on the static
- id: arxiv:2609.36844
  pool: crossdomain
  title: GlassFormer: Learning Real-time Glass Segmentation using Radar-Depth Fusion
  abstract: Transparent surfaces are ubiquitous in built environments, yet they remain a persistent failure case for robotic perception. RGB cameras perceive the background behind glass rather than the surface itself, while depth sensors such as LiDAR, time-of-flight, and RGB-D often return invalid or background measurements in transparent regions. As a result, systems that rely solely on optical sensing may misinterpret glass walls, doors, or mirrors as free space, compromising safe and reliable navigation. Existing glass segmentation approaches address this by learning visual cues such as reflections, boundaries, and semantic context from RGB images. While effective under favourable lighting and viewi
- id: arxiv:2609.04441
  pool: crossdomain
  title: Stability of Collective Neutrino Oscillations -- A Distributional Approach
  abstract: We study the stability of collective neutrino oscillations using a distributional approach motivated by the statistical mechanics of Kuramoto synchronization. Treating the ensemble of neutrino flavor polarization vectors in the thermodynamic limit $N\to\infty$, we derive an exact nonlinear Fokker--Planck (continuity) equation for the one-body distribution $F(\vec{\mathbf{S}},ω,t)$ on the flavor sphere. This equation admits a two-parameter family of azimuthally symmetric stationary solutions, whose stability we analyze by linearizing around them. The resulting eigenvalue condition determines the growth or decay rate of small perturbations from \emph{any} initial distribution -- not merely fro
- id: arxiv:2609.31929
  pool: crossdomain
  title: Inertia-Corrected Newton Method For Generalized Nash Equilibria in Dynamic Games with Optimality Verification
  abstract: Newton methods efficiently find Generalized Nash Equilibria (GNE) in dynamic games by solving for the KKT necessary conditions. These methods are fast and can support multi-agent Model Predictive Control (MPC) for highly dynamic robots. However, a small KKT residual alone does not certify that the returned solution satisfies the second-order sufficient conditions for a local GNE. In this paper, we propose an efficient numerical method to verify the second-order sufficient conditions (SOSC) for a local GNE. We connect the inertia of the agent KKT matrix with the positive definiteness of the reduced Hessian of the cost function, projected onto the null space of the constraints. Furthermore, we
- id: arxiv:2609.35263
  pool: crossdomain
  title: WavePP: High-Throughput Pipeline Parallel LLM Prefill under Prefix Reuse
  abstract: Pipeline parallelism can improve prefill throughput by processing multiple request chunks concurrently across different stages of the model. However, keeping the pipeline fully utilized requires efficient scheduling and request preparation. In systems where stages retain and evict cache state independently, a local cache hit does not guarantee that the same prefix can be reused across the pipeline. Here, coordination overhead can impede request admission cadence and thus reduce overall throughput. In this paper, we present WavePP, a prefill runtime built on top of TensorRT-LLM that addresses these challenges by overlapping request admission with pipeline execution. WavePP asynchronously find
- id: arxiv:2609.36878
  pool: crossdomain
  title: NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction
  abstract: LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intensity supervision and per-scene optimization. These requirements increase data-collection and fitting costs and limit reuse across simulated scenes. We present NIDAR, a feed-forward framework that synthesizes dense intensity-like observations from RGB appearance and simulator geometry. NIDAR combines pretrained pseudo-NIR translation, hierarchical intrinsic decomposition, geometry-aware modulation, and source-domain distribution calibration to transfer reflectance-related image
- id: arxiv:2609.34370
  pool: crossdomain
  title: Spexis: Speculative Lookahead Scheduling for LLM Inference
  abstract: Spexis is a multi-GPU LLM inference framework that improves the efficiency of pipeline and tensor parallelism through speculative parallelism. Rather than using speculative decoding only to accelerate token generation, Spexis runs speculation in parallel with normal execution, introducing a new parallelism axis without increasing KV-cache memory usage. This improves memory efficiency and helps mitigate the bottlenecks of multi-GPU inference. Spexis further uses lookahead scheduling to predict speculation quality and future memory pressure, allowing it to reduce wasted speculation, KV-cache eviction, and recomputation. Built on top of vLLM, Spexis largely improves serving performance across a
- id: arxiv:2609.06687
  pool: crossdomain
  title: Modeling Medea gene-drive population replacement: thresholds and release strategies
  abstract: Mosquito-borne diseases such as dengue, Zika, and yellow fever impose a substantial global health burden, motivating genetic control strategies that replace wild mosquito populations with disease-refractory ones. Maternal-effect dominant embryonic arrest (Medea) is a gene drive in which the offspring of a Medea-carrying mother die unless they inherit the Medea allele, producing biased inheritance capable of driving a linked refractory trait to high prevalence. We develop and analyze a continuous-time compartmental model of Medea dynamics in Aedes aegypti that tracks mosquito abundance by life stage and genotype, and that generalizes the drive mechanism to allow both imperfect Medea-killing a
- id: arxiv:2609.35764
  pool: crossdomain
  title: Reliability-Gated Fusion of Consumer Head and Foot IMUs for Lower-Body 3D Pose
  abstract: Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions, and streams drift or drop out. On a new 35-take single-subject benchmark pairing an earbud head inertial measurement unit (IMU) with two smart-insole foot IMUs (SAM-3D-Body pseudo-ground-truth labels), we show the reliability problem is channel-level: a channel ablation isolates foot acceleration as the most informative input (66.6 mm vs. 79.0 mm head-only) and the firmware-fused foot orientation as the liability that destroys the gain. We therefore let the model learn how much to trust each c

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

Write the answer to: runs/2026-09-30/llm_responses/novelty_score_002.json
