"""Operator novelty scores, run 2026-10-06 (catch-up, queue mode)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
R = "2026-10-06"
low = lambda ids, note="No transferable finance mechanism", tag="off-topic": "\n".join(f"{i} | 2 | 1 | {note} | {tag}" for i in ids.split())
scores(R, "novelty_score_000", f"""
arxiv:2610.08410 | 5 | 4 | Invariant descriptors admit decoys: distinct surfaces with the same descriptor, measured by fibre radius | descriptor-collisions,decoys,biometric-templates
arxiv:2610.08730 | 3 | 3 | A static sliding-scale correction cannot control a shifted system however it is tuned | static-rules,control-failure
arxiv:2610.07854 | 4 | 4 | Real-time backup triggers placed by ransomware lifecycle stage | ransomware,resilience
arxiv:2610.08262 | 6 | 6 | Continuity authentication for intermittently connected devices that makes memory, not computation, the attacker's bottleneck | continuity-auth,offline-devices,memory-hard
arxiv:2610.07976 | 3 | 3 | Privacy posture of operator network profiles | telecom-privacy
arxiv:2610.08067 | 4 | 4 | Frontline staff do invisible work bridging automated decisions and user expectations | human-mediation,automated-decisions
arxiv:2610.08229 | 4 | 3 | Contextual priors reverse confidence ordering when confidence is read from reshaped scores | calibration,priors
arxiv:2610.08297 | 3 | 3 | Concept-drift mitigation using historic data | drift
arxiv:2610.08274 | 3 | 2 | Multi-cloud network telescope | measurement
arxiv:2610.08962 | 3 | 2 | Detect and fix Go deadlocks | concurrency
arxiv:2610.07759 | 6 | 5 | A replica that loses its state can sign conflicting values and break Byzantine quorum safety; tight conditions | bft,stateless-recovery,validator-safety
{low("arxiv:2610.08542 arxiv:2610.07542 arxiv:2610.09022 arxiv:2610.09006 arxiv:2610.09028 arxiv:2610.08488 arxiv:2610.08692 arxiv:2610.07934 arxiv:2610.08305 arxiv:2610.07669 arxiv:2610.08469 arxiv:2610.08603 arxiv:2610.09068 arxiv:2610.09224 arxiv:2610.07827 arxiv:2610.08391 arxiv:2610.07794 arxiv:2610.07619 arxiv:2610.08041")}
""")
scores(R, "novelty_score_001", f"""
arxiv:2610.07846 | 4 | 4 | Scenario-optimisation toolbox with probabilistic guarantees for data-driven decisions | scenario-optimisation,stress-testing
arxiv:2610.08263 | 4 | 3 | Observability of event systems under cyber attack | cyber-physical
arxiv:2610.07970 | 4 | 3 | Private IPFS sanctuary keeps digital objects verifiable over time | verifiable-records
arxiv:2610.07953 | 4 | 4 | Benchmarking fast models for policy-following, auditable moderation decisions | auditable-decisions,policy-following
arxiv:2610.07623 | 4 | 3 | Faster sequential calibration bounds | calibration
arxiv:2610.07747 | 5 | 4 | Preserve weak reports in cooperative sensing instead of discarding them locally | weak-evidence,cooperative-fusion
news:04d2676d6b7dbebd | 3 | 4 | Government launches month-long anti-fraud drive after data breaches | post-breach-fraud
news:b791b9bfc807236e | 2 | 2 | Court cautions on bank-appointed arbitrators | disputes
hn:49979793 | 3 | 3 | Charting tool built for users' own AI agents | agent-trading
news:326605b593ac771a | 3 | 3 | Fintechs want direct access to central bank payment rails | rail-access
news:abae7c82421f8712 | 4 | 5 | Banks to test real-time fraud warnings before payments clear | pre-clearing-warning,malaysia
news:6d78610b227a4ac5 | 2 | 2 | Card network fraud detection upgrade | fraud
news:83081d153381adac | 2 | 2 | Credit unions and instant payments | instant-payments
arxiv:2610.09141 | 4 | 4 | Model cognitive biases exploited in affinity and romance-investment fraud | romance-scam,cognitive-bias
arxiv:2610.07967 | 5 | 5 | Benchmark of deception by autonomous LLM agents pursuing task performance | agent-deception,benchmark
{low("arxiv:2610.08681 arxiv:2610.09225 arxiv:2610.09226 arxiv:2610.08929 arxiv:2610.09069 arxiv:2610.08977 arxiv:2610.08787 arxiv:2610.08265 arxiv:2610.07724 news:a5b40a6ab3eec88d news:9210d65bbbe70fc2 news:cece1cb691505fd3 news:b2bdd6f6ae12ede1 arxiv:2610.08631", "Off-topic or event listing")}
""")
