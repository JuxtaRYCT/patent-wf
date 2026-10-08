"""Operator answers to judge_* packets (queue mode, 2026-09-30): examiner-persona judgments.
Written by Claude Opus 5.5 after reading each idea next to the closest prior art retrieved by prior_art.py,
plus domain knowledge of commercial products, standards and regulator proposals (cited in the rationale).
Scale 1-10: novelty, non_obviousness, utility, feasibility, commercial, eligibility, crazy."""
import json
import re
from pathlib import Path

J = {}
def j(i, nov, nob, uti, fea, com, eli, cra, verdict, why):
    J[i] = dict(id=i, novelty=nov, non_obviousness=nob, utility=uti, feasibility=fea, commercial=com,
                eligibility=eli, crazy=cra, verdict=verdict, rationale=why)

# ---- A1 cross-pollination
j("A1-01", 8, 8, 6, 5, 7, 8, 9, "pursue", "No retrieved patent or paper uses live grid-frequency (ENF) references as a real-time liveness factor for payment instructions; ENF is known only for post-hoc audio forensics. Physical-signal claim is strongly eligible. Risk: narrowband codecs attenuate hum, so position as an additional factor for wideband/VoIP and branch/desk calls; needs a targeted ENF-deepfake literature check.")
j("A1-02", 6, 5, 6, 7, 6, 8, 6, "refine", "Closest: Truist gesture-recognition security in banking environments, NCR frictionless monitoring, BoA non-contact authentication. None uses RF channel occupancy to drive ATM transaction-state changes, but sensing-at-ATM is crowded; claim the occupancy-conditioned PIN/dispense state machine and the non-identifying evidence trace.")
j("A1-03", 6, 5, 5, 8, 5, 7, 5, "refine", "No payment-verification scheduler using VOQ/iterative matching found. The technical effect (no HOL blocking, bounded verification delay) is real but the commercial pull is modest; better as a dependent feature of a payment-hub patent.")
j("A1-04", 6, 6, 7, 6, 7, 8, 6, "refine", "UWB proximity payment (Samsung US20260203741A1) and proximity dual authentication (BoA US12731184B2) are close. Novel residue: mutually signed co-presence receipts kept as evidence for disputes and exculpation, plus concurrent multi-device ranging in lobbies. Claim narrowly around the receipt and its evidentiary use.")
j("A1-05", 8, 8, 8, 6, 8, 7, 8, "pursue", "Nearest hits are papers on adversarial multi-agent finance and instant-payment interdiction; nothing on latent-space equalisation between independently trained models for cross-institution fraud sharing. Strong fit with UK Online Fraud Charter and telco-bank data-sharing pressure. Eligibility: frame as a data-transport and model-interoperability system.")
j("A1-06", 8, 7, 8, 6, 8, 9, 8, "pursue", "Visa trusted-QR (US12705599B2) authenticates the QR via certificates but has no liveness channel; screen-camera communication research is not applied to payment tamper-evidence. High value for India's QR ecosystem. Feasibility caveat: event sensors are not yet in phones, so provide a high-frame-rate CMOS fallback embodiment.")
j("A1-07", 6, 6, 7, 6, 7, 7, 7, "refine", "Agent-payment safety is crowded (AP2 mandates; PACE policy-attested execution; formal analyses of AP2). The cumulative ℓ2 deviation certificate enforced in the TEE and attested in the token is a distinguishable residue; claim that specifically.")
j("A1-08", 3, 3, 5, 7, 4, 7, 4, "drop-anticipated", "Comparing accelerometer data of two devices to authorise a transaction is disclosed (US20110189981A1). Wearable co-location unlock is common. Body-kinematic consensus is an obvious variant.")
j("A1-09", 6, 7, 6, 3, 4, 3, 9, "refine", "Mule-detection patents (BioCatch US12380455B2) are detection-only. Threshold-sized decoy seeding is conceptually new but legally constrained (entrapment, bank secrecy) and weak on eligibility. Better as a defensive publication or a law-enforcement methods paper.")
j("A1-10", 7, 7, 7, 7, 7, 7, 7, "pursue", "Retrieved art studies scam calls and scam-app ecosystems descriptively; malware phylogeny exists, but predictive descendant-variant generation from ancestral reconstruction for multimodal scam artefacts was not found. Claim the prediction and pre-deployment loop.")
j("A1-11", 5, 5, 7, 8, 6, 7, 4, "refine", "Mobile threat defence is crowded; the hard-constraint factor graph encoding OS permission semantics is a modest technical twist. Worth a narrow claim.")
j("A1-12", 6, 6, 7, 7, 7, 7, 7, "refine", "Deception environments and transaction-bound OTPs exist separately; per-channel distinct codes that reveal which channel leaked, coupled to a shadow-ledger honey session, was not found. Prior art on 'decoy session for fraudster' likely exists at large banks and needs a targeted search.")
j("A1-13", 6, 6, 7, 6, 6, 5, 6, "refine", "No reconciliation-as-control art found. Eligibility is medium (a ledger-system control loop). Strong regulatory timing post-Synapse.")
j("A1-14", 7, 7, 5, 4, 5, 5, 8, "refine", "BIS/PFMI papers discuss tokenised settlement risk; no droop-controlled liquidity buffer found. Adoption requires central banks. A good research or central-bank partnership concept rather than a near-term licensing asset.")
j("A1-15", 7, 6, 6, 7, 6, 6, 7, "refine", "No art sizing offline payment credentials from connectivity forecasts. Useful for machine payments and remote regions; value depends on how agent-to-machine commerce evolves.")
j("A1-16", 8, 7, 9, 6, 8, 6, 7, "pursue", "Retrieved art covers graph risk scoring and recovery simulation (PixSim), not adversarial reachable-set pre-emptive holds. Directly addresses India's golden-hour problem (1930/CFCFRMS) and UK APP reimbursement. Frame the claim around the distributed computation and signed time-limited hold protocol for eligibility.")
j("A1-17", 6, 6, 5, 6, 3, 2, 6, "drop-weak", "Novel framing but essentially a statistical allocation rule; §101 / §3(k) exposure is high and the commercial buyer is unclear.")
j("A1-18", 6, 6, 7, 7, 6, 5, 6, "refine", "Graph-based payee risk is crowded; the specific reverse-bait-edge inversion and semi-monotone centrality is a narrow, defensible feature.")
j("A1-19", 5, 5, 7, 6, 7, 6, 5, "refine", "Close art: rollback governance for AI-agent payments, offline-verifiable evidence for agent messaging, AP2 analyses. Intent inference plus evidentiary bundle is incremental; combine with A1-07 into one agent-payment filing.")
j("A1-20", 5, 4, 5, 7, 4, 2, 4, "drop-weak", "EWA patents (PayActiv US20160086261A1, US8751338B2) cover access mechanics; MPC sizing is a financial computation with weak eligibility.")
j("A1-21", 4, 4, 5, 5, 4, 6, 6, "drop-anticipated", "Offline CBDC protocols (Fluency US11935065B2) and mesh or delay-tolerant payment relaying are known; the carrier-selection twist is obvious.")
j("A1-22", 3, 3, 7, 8, 6, 7, 3, "drop-anticipated", "BioCatch's patent families on remote-access/automation detection through input-timing behaviour (and vishing detection US12101354B2) anticipate the core.")
j("A1-23", 5, 5, 7, 6, 7, 5, 6, "refine", "'Optimal Control of Reserve Asset Portfolios for Stablecoins' (arXiv 2508.09429) and RWA-PoB cover much of this. The residue is the adversarial invariant-set certificate published on-chain; merge with A2b-03.")

# ---- A2a zero-shot scanner
j("A2a-01", 3, 3, 8, 8, 7, 5, 3, "drop-anticipated", "Vishing and coaching detection (BioCatch family), RBI's April 2026 trusted-person proposal and banks' active-call detection cover it.")
j("A2a-02", 3, 3, 8, 8, 7, 6, 3, "drop-anticipated", "AP2 intent and cart mandates, Mastercard Agentic Tokens and Visa Intelligent Commerce controls implement this.")
j("A2a-03", 5, 5, 7, 6, 6, 3, 6, "refine", "Early-warning signals in finance are an academic literature and digital-run papers were retrieved; the automatic collateral pre-positioning link is modest. Weak eligibility.")
j("A2a-04", 3, 3, 7, 7, 6, 7, 4, "drop-anticipated", "zkTLS income proofs exist (DECO 2020, Reclaim/zkPass products); income-verification patents (PointServ) are retrieved.")
j("A2a-05", 4, 3, 7, 8, 6, 5, 3, "drop-anticipated", "Mosca's inequality (shelf-life + migration time > quantum horizon) and commercial crypto-inventory tools cover it.")
j("A2a-06", 5, 5, 6, 6, 5, 4, 6, "refine", "Mule detection via link prediction (Actimize US20250315834A1) is close; an R0 estimate for recruitment is a new metric but weakly eligible.")
j("A2a-07", 3, 3, 6, 6, 5, 8, 5, "drop-anticipated", "Pindrop 'Active voice liveness detection' (EP4706037A2) and Wells Fargo background-audio authentication are directly on point.")
j("A2a-08", 2, 2, 6, 6, 5, 6, 3, "drop-anticipated", "IoT-attested blockchain escrow for trade finance is heavily patented (e.g. US20220300964A1, Wells Fargo trade-finance blockchain).")
j("A2a-09", 2, 2, 6, 8, 6, 3, 2, "drop-anticipated", "Cash-flow underwriting and dynamic limits are standard.")
j("A2a-10", 4, 3, 6, 7, 5, 3, 4, "drop-weak", "Affordability simulation at checkout is a known BNPL practice; business-method exposure.")
j("A2a-11", 2, 2, 4, 7, 4, 4, 2, "drop-anticipated", "SKU-level footprint from receipts is offered commercially (e.g. Doconomy/Cogo-style trackers).")
j("A2a-12", 5, 5, 6, 6, 5, 6, 5, "refine", "Consent-chain certification (US12719671B1) and data-access consent patents are adjacent; signed deletion attestations in a transparency log are a moderately new combination.")
j("A2a-13", 3, 3, 6, 7, 6, 6, 3, "drop-anticipated", "Cross-chain burn/mint and atomic settlement patents and live products (CCTP) cover it.")
j("A2a-14", 4, 4, 8, 6, 6, 6, 4, "drop-anticipated", "Cognitive-decline detection from device interaction (Panasonic US20210186410A1; finger-interaction frameworks) plus elder-exploitation monitoring exists.")
j("A2a-15", 3, 3, 7, 8, 6, 5, 3, "drop-anticipated", "Digital-footprint-age synthetic ID detection is a commercial product category.")
j("A2a-16", 2, 2, 7, 7, 6, 6, 2, "drop-anticipated", "MPC/privacy-enhancing-tech fraud consortia are known and deployed.")
j("A2a-17", 2, 2, 6, 8, 5, 3, 2, "drop-anticipated", "Counterfactual adverse-action explanations are well documented.")
j("A2a-18", 1, 1, 5, 9, 4, 3, 1, "drop-anticipated", "ATM cash forecasting with exogenous data is standard.")
j("A2a-19", 3, 3, 7, 7, 6, 5, 3, "drop-anticipated", "RBI's proposed 1-hour cancellable delay (Apr 2026) and escrow patents (Capital One US11100482B2).")
j("A2a-20", 3, 3, 6, 7, 6, 6, 3, "drop-anticipated", "x402 and Mastercard 'agentic microtransactions through verifiable payment delegation' cover it.")
j("A2a-21", 2, 2, 6, 7, 5, 7, 2, "drop-anticipated", "Offline CBDC with secure-element counters is the standard design (multiple papers and patents).")
j("A2a-22", 3, 3, 6, 8, 5, 3, 2, "drop-anticipated", "Event-driven or perpetual KYC is an established product category.")
j("A2a-23", 2, 2, 5, 8, 4, 3, 2, "drop-anticipated", "RL-personalised nudging is well known.")
j("A2a-24", 2, 2, 7, 8, 5, 5, 2, "drop-anticipated", "Transliteration-aware fuzzy sanctions screening is a mature product area.")
j("A2a-25", 3, 3, 6, 7, 5, 5, 3, "drop-anticipated", "Satellite collateral monitoring for agri and industrial lending exists.")
j("A2a-26", 3, 3, 5, 6, 4, 4, 3, "drop-anticipated", "Cross-retailer return-fraud networks exist.")
j("A2a-27", 1, 1, 7, 9, 5, 6, 1, "drop-anticipated", "SIM-swap checks via telco APIs (CAMARA SIM Swap, Prove) are deployed.")
j("A2a-28", 2, 2, 5, 7, 4, 3, 2, "drop-anticipated", "Savings-group credit scoring is known in fintech practice.")
j("A2a-29", 1, 1, 5, 8, 4, 4, 1, "drop-anticipated", "Liquidity-saving mechanisms with queue optimisation are standard RTGS features.")
j("A2a-30", 2, 2, 6, 8, 5, 4, 2, "drop-anticipated", "Chargeback prediction is standard.")

# ---- A2b signal-grounded scanner
j("A2b-01", 7, 6, 8, 8, 7, 6, 6, "pursue", "Retrieved art (virtual-card rotation, multisig cosigning) is not topology-triggered, VRF-random approver selection over bank-initiated channels. Directly counters the €95M voice-clone case. Eligibility: claim the cryptographic selection and channel-binding protocol.")
j("A2b-02", 6, 6, 7, 6, 7, 7, 6, "refine", "Deepfake detection is crowded (T-Mobile US20260112373A1); sharing generation-pipeline fingerprints as LSH threat intelligence across banks is a narrower new element.")
j("A2b-03", 5, 5, 8, 6, 8, 7, 5, "refine", "RWA-PoB (credential-based proof-of-backing covering eligibility, encumbrance and liquidity) is close. The residue is ZK over signed custodian feeds with regulatory constraints and automatic mint gating; merge with A1-23.")
j("A2b-04", 4, 4, 7, 7, 6, 6, 5, "refine", "ERC-3643 already provides partial-token freezing and taint analysis is well known; the residue is contract-level lineage accounting plus threshold court release.")
j("A2b-05", 5, 5, 5, 7, 5, 5, 5, "refine", "No close art, but modest technical depth; possibly better as a design standard than a patent.")
j("A2b-06", 7, 6, 9, 6, 8, 7, 5, "pursue", "Closest art (Amex tradeline fingerprint) is about relationship linking, not signed field-level provenance driving automatic dispute resolution. Big documented pain (238k 'investigation >30 days').")
j("A2b-07", 6, 6, 8, 6, 7, 6, 5, "refine", "VC issuance/verification (Amex) and loan-file linking (Freddie Mac US12645641B1) are adjacent; consumer-signed negative constraints in entity resolution are new. Could be upgraded to pursue after a bureau-specific search.")
j("A2b-08", 7, 7, 8, 7, 8, 6, 7, "pursue", "Agentic-commerce fraud papers (ACAGS, Agentic Commerce Bench) do not use cross-user agent convergence on new merchants as a signal. It is network-scale and only possible once agent traffic is labelled.")
j("A2b-09", 6, 6, 7, 7, 7, 6, 7, "refine", "Attack taxonomies and benchmarks (AIP-Bench, AP2 security analysis) exist; a network-operated canary-merchant certification loop coupled to token scope is new but may be seen as an obvious operational use of red-teaming.")
j("A2b-10", 4, 4, 7, 7, 6, 5, 3, "refine", "The FDIC's custodial-account recordkeeping proposal essentially requires this data; patentable residue is limited to the proof mechanism.")
j("A2b-11", 5, 5, 7, 5, 6, 6, 5, "refine", "Electronic debt validation and dispute systems exist (GDR US20160328791A1); chain-of-title gating plus open-banking proof of payment is incremental.")
j("A2b-12", 5, 5, 8, 8, 8, 8, 5, "refine", "Mastercard 'verifiable payment delegation' (US20260154681A1) is adjacent; macaroon-style monotone attenuation across multi-hop agent chains, verified by the issuer, is a defensible narrower claim. High commercial value if granted.")
j("A2b-13", 4, 4, 7, 5, 5, 6, 4, "drop-anticipated", "CreditRegistry's non-repudiation OTP for credit requests (US20190012732A1) and India's consent-artefact architecture anticipate the core.")
j("A2b-14", 5, 4, 6, 8, 6, 6, 3, "refine", "No close art for signed purchase-session aggregation in UPI MDR; simple but useful. Better pitched to NPCI as a protocol change.")
j("A2b-15", 5, 5, 8, 7, 6, 5, 6, "refine", "RBI trusted-person proposals, BioCatch vishing detection and video-based transaction verification (Ironvest) are adjacent; the physically separated release ritual keyed to the coercion state is a narrow new element.")
j("A2b-16", 3, 3, 6, 8, 5, 6, 3, "drop-anticipated", "US20130151419A1 (merchant verification of in-person electronic transactions via validation data rendered on the customer device) anticipates the core.")


# ---- Stage-2 deep prior-art check (targeted USPTO BRS queries + web search of academic/industry sources),
#      applied to every idea ranked 'pursue' and to the strongest 'refine' ideas. Overrides stage-1 judgments.
j("A1-01", 5, 4, 6, 5, 6, 8, 9, "refine", "DEEP CHECK: DeFakePro (arXiv 2207.13070, 2022) and 'Deterring deepfake attacks with an ENF fingerprints approach' (Future Internet 2022) already detect deepfakes in live audio/video calls from ENF against a ground-truth reference in real time. IBM US10957355B2 authenticates recordings with emitted environment signals. Only the payment-authorisation integration (PMU region reference, multi-window RoCoF) remains; that is a dependent-claim-level addition.")
j("A1-05", 5, 5, 8, 6, 7, 7, 8, "refine", "DEEP CHECK: 'Secure Linear Alignment of Large Language Models' (arXiv 2603.18908) learns affine maps between independently trained models for privacy-preserving cross-silo inference, and LDP embedding sharing for distributed fraud prevention is published. Remaining novelty: consented cross-sector anchor sets and drift-triggered re-fitting for scam intelligence. Narrow.")
j("A1-06", 5, 5, 8, 6, 7, 9, 8, "refine", "DEEP CHECK: ScreenID (Li et al., MobiCom'20 / Infocom'21) uses screen PWM flicker as a fingerprint to reveal reproduced QR codes. Revelio (2025) and US12114003 cover imperceptible screen-to-camera data. Denso Wave US12367364B2 modulates QR cell luminance, and Datalogic US20260073171A1 reads codes with event cameras. Remaining: payee-key-authenticated rolling nonce plus relay-latency check. Narrow.")
j("A1-10", 4, 4, 7, 7, 6, 7, 7, "drop-anticipated", "DEEP CHECK: predicting future malware-variant signatures from learned family evolution is published, with months of lead time (arXiv 2507.21538). Phishing-kit lineage and scam phylogenies exist, and phylogenetic attribution is patented (HRL US9224067B1, Triad US10783247B1). Extending this to multimodal banking scams is an obvious step.")
j("A2b-12", 3, 3, 8, 8, 8, 8, 5, "drop-anticipated", "DEEP CHECK: DeepMind 'Intelligent AI Delegation' (Delegation Capability Tokens built on macaroons), the IETF draft 'Attenuating Agent Tokens' (Mar 2026), AIP (arXiv 2603.24775) and Mastercard US20260154681A1 cover attenuable delegation for agents and payments.")
j("A2b-08", 6, 6, 8, 7, 8, 6, 7, "pursue", "DEEP CHECK: industry commentary (MRC, Riskified, Signifyd) recommends 'networked intelligence and monitoring for transaction spikes', and Ballerine markets 'agentic detection' of merchant fraud. The specific signal survives: distinct-agent convergence on thin-history merchants normalised against a human-traffic baseline and by agent-platform concentration. Pursue with that narrowed claim.")
j("A2b-07", 7, 6, 8, 6, 7, 6, 5, "pursue", "DEEP CHECK: mixed files are a well-known and litigated problem (about 15% of credit-reporting complaints in 2023 per CFPB), but no bureau or patent uses consumer-signed, credential-bound disownment as a hard negative constraint in entity resolution. Upgraded to pursue.")
j("A2b-06", 7, 6, 9, 6, 8, 7, 5, "pursue", "DEEP CHECK: Metro 2/e-OSCAR tooling validates format and automates code exchange, and State Farm US11893634B2 uses ML to correct reporting errors. No signed, field-level source-record provenance driving automatic dispute resolution was found. Confirmed.")
j("A2b-01", 7, 6, 8, 8, 7, 6, 6, "pursue", "DEEP CHECK: BEC guidance recommends dual approval and out-of-band call-backs with fixed approvers. No VRF-based random co-approver selection triggered by instruction-topology novelty was found in USPTO or web sources. Confirmed.")
j("A1-16", 8, 7, 9, 6, 8, 6, 7, "pursue", "DEEP CHECK: industry practice predicts mule accounts and withholds inbound funds per account (NICE Actimize, Mastercard, Kumo), and Indian banks are seeking powers to freeze without LEA orders. No adversarial reachable-set computation of a minimal pre-emptive hold set across institutions was found. Confirmed; design holds as LEA/1930-authorised, time-limited requests.")
j("A1-12", 6, 6, 7, 7, 7, 7, 7, "refine", "DEEP CHECK: out-of-band OTP guidance stresses delivery-path integrity, but no per-channel-distinct codes used to attribute leaks, nor coupling to shadow-ledger honey sessions, was found. Survives as refine; needs a check of bank-internal deception patents.")
j("A1-04", 6, 6, 7, 6, 7, 8, 6, "refine", "DEEP CHECK: UWB secure-ranging patents (Samsung, NXP families; 802.15.4z) cover ranging and access control. No mutually signed co-presence receipts used as dispute or exculpatory evidence were found. Survives as refine.")
j("A1-02", 6, 5, 6, 7, 6, 8, 6, "refine", "DEEP CHECK: shoulder-surfing defences use cameras, eye tracking (ShouldAR) or physical shields. No RF/radar occupancy-conditioned ATM transaction state machine was found. Survives as refine.")
j("A1-18", 6, 6, 7, 7, 6, 5, 6, "refine", "DEEP CHECK: guidance describes victims' small first payments; the reverse-bait-edge inversion in payee reputation was not found. Survives as refine.")
j("A1-15", 7, 6, 6, 7, 6, 6, 7, "refine", "DEEP CHECK: offline terminal limits are static and manually configured (Square, Toast, Nexi docs). Forecast-sized, geo- and time-bounded offline credentials were not found. Survives as refine.")

out = Path(__file__).parent
for q in sorted((out / "llm_queue").glob("judge_*.md")):
    ids = re.findall(r"^### (\S+)\s+\(", q.read_text(), flags=re.M)
    (out / "llm_responses" / f"{q.stem}.json").write_text(
        json.dumps({"judgments": [J[i] for i in ids]}, indent=1, ensure_ascii=False))
    print(q.stem, len(ids))
