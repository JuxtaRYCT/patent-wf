# TASK synthesis_006

## SYSTEM
You are an inventor on a bank's advanced-technology team, expert in payments, fraud, credit, treasury, regulation (US, EU, UK, India) and patent drafting. You practise bisociation: transplanting a mechanism from an unrelated field into a finance problem. Rules: (1) every concept must have a concrete TECHNICAL mechanism (data structures, signals, protocols, hardware, cryptography, control loops) - not a business method; (2) it must be implementable within ~3 years; (3) name what makes it non-obvious versus the closest thing you know exists; (4) prefer concepts a bank, card network or payment processor would license; (5) if a pair yields nothing credible, return fewer ideas rather than forcing one.

## PROMPT
For each pair, transplant the foreign mechanism into the finance problem and propose 0-2 patentable invention concepts. Stretch for unusual but technically credible combinations.

### PAIR X036  (semantic distance 0.62, fused-vector patent proximity 0.71)
FINANCE PROBLEM SOURCE [news:b05d66bdce0aab7a]: Canada’s Big Six Banks Jointly Explore Digital Deposits Network - Bloomberg.com
Canada’s Big Six Banks Jointly Explore Digital Deposits Network Bloomberg.com
Open problem (scout note): Six largest Canadian banks jointly explore a shared tokenized-deposit network

FOREIGN MECHANISM SOURCE [arxiv:2609.36196]: People effects on IoT indoor wireless channel characterization
Wireless communication under 1 GHz is suitable for Internet of Things (IoT) applications due to larger coverage capability with less power consumption. Bearing in mind that people and elements contained in the environment can cause variations in the channel, this paper aims to evaluate the effect of the presence of people on a 900-MHz indoor narrowband wireless channel, as we characterize the small-scale phenomena. With the increase in the number of people, a greater variation in the communication channel was noticed, which is reflected in the parameters of the probability distributions used in the characterization of the random part of the signal. In addition, second-order statistics were used to analyze the data and an adherence test was applied to confirm the behavior of the signal in relation to the distributions.
Transferable mechanism (scout note): Presence and movement of people measurably changes an indoor sub-GHz radio channel

### PAIR X037  (semantic distance 0.62, fused-vector patent proximity 0.66)
FINANCE PROBLEM SOURCE [news:cbeab915dc24f05b]: Grandmother falsely accused of bank fraud sues Fargo, North Dakota, over AI facial recognition - CBS News
Grandmother falsely accused of bank fraud sues Fargo, North Dakota, over AI facial recognition CBS News
Open problem (scout note): Facial-recognition false match led to false bank-fraud accusation

FOREIGN MECHANISM SOURCE [arxiv:2609.33892]: Residual Learning-Based Control of Vehicle Platoons with $\ell_2$ Stability Guarantees via Recurrent Equilibrium Networks
This paper proposes a residual learning-based control framework for heterogeneous vehicle platoons subject to parametric uncertainty and external disturbances. A nominal controller designed via Linear Matrix Inequalities (LMIs), along with disturbance-observer compensation, is enhanced by a Recurrent Equilibrium Network (REN) trained offline using stored trajectories and nominal-model prediction errors. The REN is constrained to satisfy a prescribed $\ell_2$-gain bound, enabling sufficient small-gain conditions for local closed-loop stability and disturbance string stability. Experiments demonstrate reduced spacing and velocity errors relative to the nominal controller.
Transferable mechanism (scout note): Residual learned controller on top of a certified nominal controller keeps l2-stability guarantees under uncertainty

### PAIR X038  (semantic distance 0.61, fused-vector patent proximity 0.71)
FINANCE PROBLEM SOURCE [news:4adbdbb6ed51426b]: Lloyds Banking Group’s agentic strategy is often small, often deterministic and often supervised - Diginomica
Lloyds Banking Group’s agentic strategy is often small, often deterministic and often supervised Diginomica
Open problem (scout note): Big bank's agentic AI is deliberately small, deterministic and supervised: control over autonomy

FOREIGN MECHANISM SOURCE [arxiv:2609.36905]: Ternary Visible Light Communication Using Event-Based Vision Sensors
This paper proposes a ternary visible light communication method using an event-based vision sensor (EVS) and a liquid crystal display (LCD). The throughput of optical camera communication (OCC) is limited by the frame rates of conventional frame-based cameras, and EVSs are expected to overcome this limitation because their pixels asynchronously trigger events with polarity in response to brightness changes, with a temporal resolution on the order of microseconds. However, existing event-based OCC relies on binary signaling that uses only the presence or absence of events and leaves the polarity unused. The proposed method maps the three brightness transitions (increase, decrease, and no change) to ternary symbols, thereby increasing the information carried per symbol. At the transmitter, the LCD displays a marker in which the transmitted data are encoded; at the receiver, the EVS captur
Transferable mechanism (scout note): Screen-to-event-camera ternary optical link beats frame-rate limit of camera communication

### PAIR X039  (semantic distance 0.61, fused-vector patent proximity 0.66)
FINANCE PROBLEM SOURCE [news:740822da91e14469]: Delhi Cyber Fraud: Four Posing As Axis Bank Officials Arres… - GujaratSamachar English
Delhi Cyber Fraud: Four Posing As Axis Bank Officials Arres… GujaratSamachar English
Open problem (scout note): Fraudsters impersonate bank officials: caller identity verification gap

FOREIGN MECHANISM SOURCE [arxiv:2609.30960]: Packet iSlip
This paper examines input/output buffered crossbar switches under combined packet and cell data. Our switch architecture uses input buffering with Virtual Output Queues to avoid Head of Line Blocking. The switch fabric is a crossbar with no speedup. We use a modified iSlip [McKeown] crossbar scheduler geared towards packet data, called piSlip. Cell ports are largely unmodified from standard iSlip behavior. For packet output ports, we introduce changes to the grant pointer which minimizes output latency caused by packet reassembly. Our model uses several output states, including packet cut-through. From simulation results, we show that piSlip with virtual cut-through offers latency characteristics significantly better than unmodified iSlip with similar packet port interfaces. Simulation further shows that piSlip and iSlip have similar maximum and average buffering requirements.
Transferable mechanism (scout note): Virtual output queues plus iterative matching avoid head-of-line blocking in a crossbar switch carrying mixed packet sizes

### PAIR X040  (semantic distance 0.60, fused-vector patent proximity 0.67)
FINANCE PROBLEM SOURCE [news:1a2cd4870e5cc308]: IPID Raises $16M Series A to Expand Global Payment Intelligence - citybiz
IPID Raises $16M Series A to Expand Global Payment Intelligence citybiz
Open problem (scout note): Funding for global payee/account verification intelligence

FOREIGN MECHANISM SOURCE [arxiv:2609.33729]: Wave-Domain Semantic Equalization Using a Practical Dynamic Metasurface Antenna with Strong Mutual Coupling
Semantic mismatch between independently trained AI-native agents in heterogeneous networks can impair semantic communications. Hybrid analog-digital semantic equalization can align the incompatible latent representations without retraining the semantic transceivers. We study a practical realization of this approach based on a fabricated dynamic metasurface antenna (DMA), an emerging low-cost, low-power, ultracompact technology for hybrid analog-digital beamforming. We model the DMA-assisted channel using multiport-network theory (MNT), accounting for mutual coupling (MC), structural scattering, and binary lossy tuning states. We use the experimentally estimated MNT parameters of our fabricated 19-GHz DMA prototype with strong MC. We jointly optimize digital pre- and post-equalizers and the DMA at a reference receiver geometry for latent-space alignment, then freeze the digital stages and
Transferable mechanism (scout note): Align latent representations of independently trained AI agents in the physical channel without retraining either agent

### PAIR X041  (semantic distance 0.63, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:ecd7907644b315a6]: [Snapdragon Summit] Qualcomm, Mastercard Announce Agentic Commerce Partnership - thelec.net
[Snapdragon Summit] Qualcomm, Mastercard Announce Agentic Commerce Partnership thelec.net
Open problem (scout note): Chipmaker and card network put agentic commerce on-device

FOREIGN MECHANISM SOURCE [arxiv:2609.34580]: On the Achievable Inertia Constant of Inverter Based Resources
As inverter-based resources (IBRs) displace synchronous generators, the inertia they can actually contribute to the grid becomes a critical planning parameter. Unlike synchronous machines, this contribution is bounded simultaneously by the available energy reserve, the converter power rating combined with voltage ride-through (VRT) obligations, and the inertia-emulation control scheme with its activation delay. This paper derives each bound in closed form and combines them into a unified envelope $\Heff(t,λ,V_g)=\min(\HE,\HP,\HC)$, which uses parameters accessible to the system operator to quantify how much inertia a plant can provide at a given loading $λ$, grid voltage $V_g$, and time $t$ after a disturbance. The analysis shows that below a loading-dependent critical voltage, VRT reactive-current priority does not leave active-current headroom for inertial power injection; that the con
Transferable mechanism (scout note): Synthetic inertia a converter can offer is bounded jointly by energy reserve, power rating and ride-through obligations


## OUTPUT JSON SCHEMA
```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "ideas"
 ],
 "properties": {
  "ideas": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "pair",
     "title",
     "problem",
     "mechanism",
     "technical_effect",
     "why_non_obvious",
     "claim_core",
     "keywords",
     "domain"
    ],
    "properties": {
     "pair": {
      "type": "string",
      "description": "pair id used"
     },
     "title": {
      "type": "string"
     },
     "problem": {
      "type": "string"
     },
     "mechanism": {
      "type": "string",
      "description": "how it works, 80-150 words"
     },
     "technical_effect": {
      "type": "string"
     },
     "why_non_obvious": {
      "type": "string"
     },
     "claim_core": {
      "type": "string",
      "description": "draft independent-claim essence, 1-2 sentences"
     },
     "keywords": {
      "type": "string",
      "description": "prior-art search keywords"
     },
     "domain": {
      "type": "string",
      "description": "payments|fraud|credit|treasury|regtech|wealth|insurance|crypto|identity"
     }
    }
   }
  }
 }
}
```

Write the answer to: runs/2026-09-30/llm_responses/synthesis_006.json
