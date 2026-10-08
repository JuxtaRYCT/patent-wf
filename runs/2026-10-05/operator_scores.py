"""Operator novelty scores, run 2026-10-05 (catch-up, queue mode)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
R = "2026-10-05"
low = lambda ids, note, tag: "\n".join(f"{i} | 2 | 1 | {note} | {tag}" for i in ids.split())
scores(R, "novelty_score_000", f"""
arxiv:2610.06123 | 4 | 3 | Identification codes let dense ad hoc nodes signal identity with minimal transmission | identification-codes,low-bandwidth
arxiv:2610.07343 | 5 | 5 | Identity-document transitions (name/gender changes) redistribute harm across linked ID systems | identity-mismatch,kyc,document-transition
arxiv:2610.06071 | 3 | 2 | Passive resonator localisation by gradient-field frequency | sensing
arxiv:2610.06362 | 4 | 2 | Highly nonlinear vectorial Boolean maps (S-box quality) | cryptography
arxiv:2610.06613 | 4 | 4 | Robust training of detectors with partially mislabelled data | noisy-labels
arxiv:2610.06373 | 5 | 4 | Decremental check for Braess paradox: removing links can lower equilibrium latency | braess-paradox,network-routing
arxiv:2610.07476 | 4 | 3 | Limits of verifying covert compute from external power draw | analog-verification
arxiv:2610.07345 | 4 | 4 | Interpretable IAM policy risk scoring using behavioural context | iam,cloud-security
arxiv:2610.07108 | 4 | 3 | Token-level provenance of who added, moved and deleted content | provenance,edit-lineage
arxiv:2610.06398 | 3 | 1 | MRI glioma infiltration feature | medical
arxiv:2610.07398 | 2 | 1 | Robotic trimaran | robotics
arxiv:2610.07390 | 2 | 1 | Drone-deployable buoy | robotics
arxiv:2610.07416 | 2 | 1 | Knitted strain sensors | wearables
arxiv:2610.06661 | 2 | 1 | Kramers theorem footprint | physics
arxiv:2610.07422 | 2 | 1 | Matter-wave interferometer white paper | physics
arxiv:2610.07515 | 3 | 1 | Electrosurgical cutting topology | surgery
arxiv:2610.06263 | 2 | 1 | Ultrasonic vagus stimulation earpiece | medical
{low("arxiv:2610.05820 arxiv:2610.06739 arxiv:2610.07275 arxiv:2610.05839 arxiv:2610.07512 arxiv:2610.07176 arxiv:2610.06583 arxiv:2610.06506 arxiv:2610.06546 arxiv:2610.06555 arxiv:2610.07507 arxiv:2610.07329 arxiv:2610.06475", "No transferable finance mechanism", "off-topic")}
""")
scores(R, "novelty_score_001", f"""
arxiv:2610.06777 | 3 | 2 | Cooperative guard coverage with partial observability | coverage
arxiv:2610.06028 | 4 | 2 | Near-exact tournament equity computation at scale | combinatorics
arxiv:2610.06179 | 5 | 5 | Explicit QUIC proxies let users appear in another country, bypassing server-side geo-checks | geo-evasion,quic-proxy,location-spoofing
arxiv:2610.07129 | 3 | 3 | How handler-dog teams split sensing and search decisions | human-ai-teaming
arxiv:2610.05673 | 3 | 3 | Low-complexity multi-AP indoor localisation | indoor-localisation
arxiv:2610.07407 | 5 | 5 | Simulated defence strategies against brand-targeted disinformation | disinformation,reputation-defence
news:87b0a3728b763a05 | 3 | 3 | Stablecoin card firm applies for a national trust bank charter | charters,stablecoins
news:666443a3dad5f405 | 2 | 2 | Community bank scam tips | scams
news:376b29f34c57e4e0 | 3 | 3 | Large bank's blockchain patent portfolio | competitor-ip
news:65e811b272a802ca | 3 | 3 | Dollar stablecoins outside the banking system | stablecoins
news:03c658f6e6b05b4b | 2 | 2 | POS adds fuel payments | pos
news:16423d6544bd0d30 | 2 | 2 | Lawsuit against bank regulator | regulation
arxiv:2610.07531 | 6 | 6 | People cannot verify an unexpected call claiming to be their bank; lightweight verifiable identity claims | caller-verification,impersonation,verifiable-claims
arxiv:2610.05926 | 3 | 3 | Credit-card LGD via run-off triangles vs regression | credit-risk
{low("arxiv:2610.07478 arxiv:2610.06202 arxiv:2610.07157 arxiv:2610.06720 news:0b6bfa356064cafd news:9b76a22c742d5b68 s2:85536a278758082bfc5bba8043d203b85c83ac9e s2:c54d2053bfabc12fc6ae93421a50c9f2fdc1fdbb arxiv:2610.05675", "Off-topic or duplicate", "off-topic")}
""")
