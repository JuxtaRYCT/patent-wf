"""Operator novelty scores, run 2026-10-02 (catch-up, queue mode)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
R = "2026-10-02"
scores(R, "novelty_score_000", """
arxiv:2610.02879 | 5 | 3 | Exclusive leases stay safe even when participants disagree about simultaneity | leases,distributed-locking
arxiv:2610.03042 | 2 | 1 | Body-area network routing | wban
arxiv:2610.03398 | 2 | 1 | Microtonal harmony app | music
arxiv:2610.02742 | 3 | 1 | Piezoelectric isolated power conversion | power-electronics
arxiv:2610.03685 | 4 | 3 | Calibrated test for background-mortality term | actuarial
arxiv:2610.03263 | 2 | 1 | Capsule endoscope antenna | antennas
arxiv:2610.03182 | 4 | 3 | Recover design intent from an IC's clock network (hardware reverse engineering) | hardware-re,tamper
arxiv:2610.03440 | 4 | 4 | Estimate a blockchain's energy use from network mapping for MiCA sustainability reporting | mica,sustainability-disclosure
arxiv:2610.03147 | 4 | 3 | Real-time detection and imputation of missing streaming data | streaming,imputation
arxiv:2610.03859 | 3 | 2 | Magnetometer calibration with inertial sensors | sensors
arxiv:2610.02688 | 5 | 6 | Technology-facilitated abuse: abusers exploit shared accounts, tracking and messaging channels to control victims | tech-facilitated-abuse,financial-abuse,coercive-control
arxiv:2610.04035 | 2 | 1 | Ising chain Casimir force | physics
arxiv:2610.04016 | 4 | 1 | Verifying treaty compliance with active interrogation | verification
arxiv:2610.02694 | 6 | 5 | Forensic reconstruction of who went where when to identify misbehaving independently operated agents | agent-forensics,byzantine,attribution
arxiv:2610.04141 | 6 | 5 | Temporary smart-home access silently becomes persistent surveillance; revocation fails | delegated-access,revocation,persistence
arxiv:2610.02936 | 2 | 1 | Timing-robust ADC | hardware
arxiv:2610.06911 | 2 | 1 | Sensor-network data gathering | wsn
arxiv:2610.03249 | 4 | 3 | Self-repairing ensembles recover a controller from sensor drift | drift,robustness
arxiv:2610.03338 | 3 | 2 | Fibre sensor placement for failure prediction | optical-networks
arxiv:2610.03210 | 2 | 1 | Classroom noise and EEG | acoustics
arxiv:2610.03504 | 2 | 1 | Magnetic B-H modelling | magnetics
arxiv:2610.02924 | 3 | 2 | Evaluator-in-the-loop tree search for protein design | search
arxiv:2610.03470 | 6 | 6 | Estimate a black-box guardrail's accuracy in production without humans viewing the data | eyes-off-evaluation,guardrails,privacy-audit
arxiv:2610.02645 | 3 | 2 | Zero-determinant strategies without discounting | game-theory
arxiv:2610.02849 | 2 | 1 | Nonlinear electrostatics | physics
arxiv:2610.03972 | 4 | 3 | Probabilistic algorithms for Ising-machine hardware | optimisation-hardware
arxiv:2610.02745 | 2 | 1 | GPU stochastic variational method | physics
arxiv:2610.02908 | 3 | 2 | Separating overlapping RF interference | rf
arxiv:2610.03590 | 6 | 5 | Certified deletion: cryptographic proof that encrypted data was deleted, now at constant rate | certified-deletion,data-erasure-proof
arxiv:2610.03478 | 2 | 1 | Minimax entropy production | physics
""")
scores(R, "novelty_score_001", """
arxiv:2610.04128 | 5 | 4 | Gradients leak extra text in split learning; per-token accounting | split-learning,privacy-leakage
arxiv:2610.03643 | 4 | 3 | Contactless radar vital-sign localisation robust to multipath | radar,vital-signs
arxiv:2610.03105 | 2 | 1 | Gesture generation benchmark | hci
arxiv:2610.03032 | 2 | 1 | NOMA secrecy | comms
arxiv:2610.03995 | 2 | 1 | Pen crossing selection | hci
arxiv:2610.04037 | 3 | 2 | Cross-GPU fault injection | reliability
arxiv:2610.06918 | 5 | 4 | Federated Q-learning robust to adversarial agents' trajectories | federated-rl,byzantine-robust
news:cb6784f470aac7a0 | 1 | 2 | ECB council decisions | central-bank
news:e15bf7944e5e2a86 | 3 | 4 | Tokenized deposits settle digital green bonds | tokenized-deposits,green-bonds
news:4918caec7d83900d | 2 | 3 | Robocall scams on small businesses | scams,smb
news:8bd82f7e7b80af57 | 3 | 4 | Free instant payments lack a revenue model | instant-payments,economics
news:a3bc7f71eb49297d | 4 | 5 | AI deepfakes impersonating the central bank to lure victims | central-bank-impersonation,deepfake
news:ec8f2871a4e8e539 | 1 | 1 | Committee appointments | noise
news:7147222c0cb848a1 | 4 | 5 | Stablecoin firm wants to bank AI agents as account holders | agent-accounts,stablecoins
news:32479552c4380bb4 | 2 | 3 | Cross-border payments startup | cross-border
news:7dabdc4c4905ee00 | 4 | 5 | Retail broker launches agentic trading with guardrails | agentic-trading,guardrails
arxiv:2610.03369 | 3 | 2 | MoE order execution tail risk | execution
arxiv:2610.03259 | 4 | 3 | Credit-default benchmark with late, scarce labels | credit-risk,benchmark
arxiv:2610.03841 | 3 | 2 | Algorithmic stablecoin with an algorithmic central bank | stablecoins
arxiv:2610.03922 | 4 | 3 | Shorter sequential priority auctions change searcher competition | mev,auctions
s2:51f983ce3e69e2cfc043edbe9f59372519757e24 | 2 | 2 | Insurer digital transformation | insurance
arxiv:2610.03951 | 5 | 4 | Evolve LLM-generated features into interpretable classifiers for regulated decisions | interpretable-features,credit
""")
