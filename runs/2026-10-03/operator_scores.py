"""Operator novelty scores, run 2026-10-03 (catch-up, queue mode)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
scores("2026-10-03", "novelty_score_000", """
arxiv:2610.04514 | 3 | 1 | Sub-THz CMOS frequency multiplier | rf-hardware
arxiv:2610.04192 | 3 | 1 | Perceptual thresholds for layered opacity | visualisation
arxiv:2610.04762 | 2 | 1 | EHR satisfaction trends | health-it
arxiv:2610.04388 | 3 | 1 | Ga2O3 Schottky diodes | semiconductors
arxiv:2610.06935 | 3 | 1 | Persistent random walk bounds | probability
arxiv:2610.04186 | 3 | 2 | Schedule-dependent reliability in multi-pass dispensing | scheduling
arxiv:2610.04775 | 3 | 2 | Distributed force control of soft robots | robotics
arxiv:2610.04222 | 3 | 1 | Respiratory mask dynamics | medical
arxiv:2610.04319 | 6 | 5 | Sanitise least-significant bits of model weights to strip hidden payloads in third-party transformers (model supply chain) | model-supply-chain,steganography,sanitisation
arxiv:2610.04526 | 4 | 3 | Generative stress tests of network overload monitoring from proxy records | stress-testing,generative
arxiv:2610.04764 | 4 | 3 | Robots coordinate pushing without any communication, using only local force | communication-free-coordination
arxiv:2610.04582 | 3 | 2 | Category-theoretic model hierarchies for control | control-theory
arxiv:2610.04242 | 3 | 2 | Predictive control for chronic disease management | mpc,health
arxiv:2610.04662 | 4 | 3 | Differentiable three-valued temporal-logic specifications for learning controllers | temporal-logic,specification
arxiv:2610.04163 | 4 | 4 | Fully homomorphic encryption for collaborative statistical modelling | fhe,privacy
arxiv:2610.04798 | 4 | 4 | Forecast cyber incidents from geopolitical signals with LLMs | cyber-risk,forecasting
arxiv:2610.04747 | 3 | 2 | Formal ethics of lying in speech acts | ethics
arxiv:2610.04213 | 4 | 3 | Vital-sign sensing in 6G FR3 band | rf-sensing
arxiv:2610.04337 | 3 | 2 | Smoothing calibration landscapes for traffic twins | calibration
arxiv:2610.04630 | 2 | 1 | Relay energy minimisation | telecom
arxiv:2610.04818 | 5 | 5 | Hardware-accelerated malicious-secure function secret sharing for private lookups | function-secret-sharing,private-retrieval
news:42c50560a1d1703e | 2 | 3 | Central bank cautious on private crypto, open to the technology | crypto-policy,india
gh:ltoinel/Carbure | 4 | 5 | Household budget app exposes synced bank data to AI agents through a read-only MCP server | agent-data-access,mcp,least-privilege
s2:8f9459269f44ea3bbb70023c490fe465ebb53c0a | 1 | 1 | HR analytics | off-topic
arxiv:2610.04699 | 6 | 6 | LLMs cannot decide which agent rules a fixed check can verify and which need a judge | agent-verification,rule-decidability
s2:bb24df99a2bcbf5ed20e009f60f68c4d5110da87 | 2 | 2 | Silk carbon credits | carbon-credits
arxiv:2610.04693 | 6 | 6 | Adversarial search finds regulatory-obligation violations by agents where breaches leave no lexical trace | agent-compliance,adversarial-search,regulatory-obligations
""")
