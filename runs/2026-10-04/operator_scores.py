"""Operator novelty scores, run 2026-10-04 (catch-up, queue mode)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
scores("2026-10-04", "novelty_score_000", """
arxiv:2610.05475 | 3 | 2 | App-store tracking cookies | privacy
arxiv:2610.06994 | 5 | 4 | Measure defence cost against a never-poisoned twin, not the poisoned model | backdoor-defence,evaluation-baseline
arxiv:2610.05339 | 4 | 3 | Tensor decomposition that handles clipped or saturated data | tensor,saturation
arxiv:2610.07013 | 2 | 1 | Electron emission model | physics
arxiv:2610.05246 | 6 | 6 | Measured limits of what a pre-execution policy gate can know about an agent's commands across platforms | agent-gating,policy-enforcement,limits
arxiv:2610.07012 | 1 | 1 | Litz-wire insulation breakdown | hardware
arxiv:2610.05511 | 2 | 1 | Polynomial estimation variance | statistics
arxiv:2610.05458 | 5 | 5 | Same model and inputs give different logits on different GPU vendors; measured and reduced | reproducibility,cross-hardware,model-risk
arxiv:2610.05455 | 2 | 1 | Robot social navigation | robotics
arxiv:2610.05470 | 3 | 3 | Volunteer moderators shield students from fraudulent education agents | community-moderation,scams
arxiv:2610.05561 | 4 | 4 | Per-attribute mechanisms for metric differential privacy on mixed records | differential-privacy,heterogeneous
arxiv:2610.07026 | 4 | 4 | Voice-first AI that runs fully offline on low-power hardware | offline-ai,voice
arxiv:2610.04869 | 5 | 5 | Temporal link prediction ignores who is active; modelling activity first transfers across models | temporal-graphs,activity
arxiv:2610.05545 | 4 | 4 | Geolocate internet hosts reactively from constraints instead of stale databases | ip-geolocation
arxiv:2610.05031 | 4 | 3 | LLM layered over diagnostic tools fails to realise their complementarity | tool-integration
arxiv:2610.04877 | 2 | 2 | Electricity consumer empowerment | energy
arxiv:2610.05444 | 2 | 2 | Faith-aligned browser trust | hci
arxiv:2610.05270 | 2 | 1 | Drone delivery plus monitoring | logistics
arxiv:2610.05510 | 2 | 1 | Power adequacy metrics | power
arxiv:2610.05624 | 1 | 1 | Ion crystal melting | physics
arxiv:2610.05605 | 2 | 1 | Missing data in HPC studies | statistics
arxiv:2610.05530 | 3 | 2 | Optimal control for multicore allocation with deadlines | real-time
arxiv:2610.05122 | 2 | 1 | Drone road guidance | logistics
arxiv:2610.07030 | 3 | 2 | LLM multi-agent container placement | scheduling
arxiv:2610.05571 | 4 | 4 | Compositional statistical model checking across scenario combinations | scenario-testing,safety
news:69fcd4fc5fd03ef0 | 4 | 5 | Browser ships post-quantum TLS and native wallet digital-ID requests | digital-credentials,browser-wallet,pqc
news:25a9dbab44a919bd | 3 | 5 | Same borrowers or collateral defrauding several banks in one city | multiple-financing,loan-fraud
s2:f6d7343d560103a6ecad76b893cd57b5880c36b5 | 1 | 1 | Sanitation contracts | off-topic
s2:eb14e103d4f412856b2a5347f3ece68f15ed5334 | 2 | 1 | Enterprise value segmentation | valuation
""")
