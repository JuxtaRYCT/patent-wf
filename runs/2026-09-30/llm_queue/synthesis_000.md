# TASK synthesis_000

## SYSTEM
You are an inventor on a bank's advanced-technology team, expert in payments, fraud, credit, treasury, regulation (US, EU, UK, India) and patent drafting. You practise bisociation: transplanting a mechanism from an unrelated field into a finance problem. Rules: (1) every concept must have a concrete TECHNICAL mechanism (data structures, signals, protocols, hardware, cryptography, control loops) - not a business method; (2) it must be implementable within ~3 years; (3) name what makes it non-obvious versus the closest thing you know exists; (4) prefer concepts a bank, card network or payment processor would license; (5) if a pair yields nothing credible, return fewer ideas rather than forcing one.

## PROMPT
For each pair, transplant the foreign mechanism into the finance problem and propose 0-2 patentable invention concepts. Stretch for unusual but technically credible combinations.

### PAIR X000  (semantic distance 0.62, fused-vector patent proximity 0.70)
FINANCE PROBLEM SOURCE [news:ac85f85a216502df]: Italy's biggest private bank wires $108M to scammers who clone a lawyer's voice with AI - VnExpress International
Italy's biggest private bank wires $108M to scammers who clone a lawyer's voice with AI VnExpress International
Open problem (scout note): Bank wired $108M after scammers cloned a lawyer's voice: high-value instruction authentication via voice is broken

FOREIGN MECHANISM SOURCE [arxiv:2609.34531]: Frequency Measurement Practices for Inertia Assessment in Inverter Based Resources Dominated Power Systems
Transmission system operators and protective relays compute the rate of change of frequency (RoCoF) from frequency averaged over tens to hundreds of milliseconds, as standards and grid codes specify. Any response delivered inside that window lowers the measured RoCoF, so the inferred inertia depends on the window and the responses in service. This paper defines the windowed inertia estimate and derives an exact identity the system inertia divided by one minus the fraction of the disturbance energy delivered inside the window and a closed-form prediction that applies the same estimator to the trajectory of a linear response model. Eleven IEEE 9-bus RMS runs synchronous, grid-following and grid-forming configurations, disturbance sizes and parameter sweeps are reproduced by that model, and the identity closes on the measured response powers. Fast frequency response inflates the estimate mo
Transferable mechanism (scout note): Inferred inertia depends on the averaging window used for rate-of-change-of-frequency; fast responses inside the window hide true inertia

### PAIR X001  (semantic distance 0.61, fused-vector patent proximity 0.69)
FINANCE PROBLEM SOURCE [news:ef870829fd7d3811]: East TN woman mistakenly jailed for months after A.I. flagged her as bank fraud suspect, lawsuit says - WVLT
East TN woman mistakenly jailed for months after A.I. flagged her as bank fraud suspect, lawsuit says WVLT
Open problem (scout note): AI fraud flag caused a months-long wrongful jailing: identity disambiguation and contestability failure

FOREIGN MECHANISM SOURCE [arxiv:2609.36196]: People effects on IoT indoor wireless channel characterization
Wireless communication under 1 GHz is suitable for Internet of Things (IoT) applications due to larger coverage capability with less power consumption. Bearing in mind that people and elements contained in the environment can cause variations in the channel, this paper aims to evaluate the effect of the presence of people on a 900-MHz indoor narrowband wireless channel, as we characterize the small-scale phenomena. With the increase in the number of people, a greater variation in the communication channel was noticed, which is reflected in the parameters of the probability distributions used in the characterization of the random part of the signal. In addition, second-order statistics were used to analyze the data and an adherence test was applied to confirm the behavior of the signal in relation to the distributions.
Transferable mechanism (scout note): Presence and movement of people measurably changes an indoor sub-GHz radio channel

### PAIR X002  (semantic distance 0.59, fused-vector patent proximity 0.69)
FINANCE PROBLEM SOURCE [news:4f4357e6fce4f96d]: AI messaging scam costs Italy's top bank Intesa millions, sources say - AOL.ca
AI messaging scam costs Italy's top bank Intesa millions, sources say AOL.ca
Open problem (scout note): AI-generated messaging scam costs top bank millions: authorised-instruction impersonation

FOREIGN MECHANISM SOURCE [arxiv:2609.30960]: Packet iSlip
This paper examines input/output buffered crossbar switches under combined packet and cell data. Our switch architecture uses input buffering with Virtual Output Queues to avoid Head of Line Blocking. The switch fabric is a crossbar with no speedup. We use a modified iSlip [McKeown] crossbar scheduler geared towards packet data, called piSlip. Cell ports are largely unmodified from standard iSlip behavior. For packet output ports, we introduce changes to the grant pointer which minimizes output latency caused by packet reassembly. Our model uses several output states, including packet cut-through. From simulation results, we show that piSlip with virtual cut-through offers latency characteristics significantly better than unmodified iSlip with similar packet port interfaces. Simulation further shows that piSlip and iSlip have similar maximum and average buffering requirements.
Transferable mechanism (scout note): Virtual output queues plus iterative matching avoid head-of-line blocking in a crossbar switch carrying mixed packet sizes

### PAIR X003  (semantic distance 0.62, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:cbeab915dc24f05b]: Grandmother falsely accused of bank fraud sues Fargo, North Dakota, over AI facial recognition - CBS News
Grandmother falsely accused of bank fraud sues Fargo, North Dakota, over AI facial recognition CBS News
Open problem (scout note): Facial-recognition false match led to false bank-fraud accusation

FOREIGN MECHANISM SOURCE [arxiv:2609.33753]: Concurrent Coded Signal-Multiplexing Ranging for Half-Duplex Asynchronous Networks
Signal-multiplexing network ranging (SM-NR) shares broadcasts across node pairs, but its sequential operation leads to a ranging cycle that grows linearly with network size. This paper proposes a concurrent coded SM-NR (CC-SM-NR) framework for asynchronous half-duplex networks. Firstly, the CC-SM-NR protocol coordinates concurrent transmissions through binary transmit-listen codewords. The transmit-listen schedule defined by these codewords ensures reciprocal observations subject to a finite concurrency limit. Then, we derive the exact minimum number of transmit-listen rounds without a concurrency limit, which reveals that the minimum grows logarithmically with network size. To account for practical scenarios, we establish the necessary and sufficient conditions for the constant-weight feasibility of codewords under a finite concurrency limit. Subsequently, we propose a low-complexity sc
Transferable mechanism (scout note): Concurrent coded ranging across asynchronous half-duplex nodes cuts ranging cycle time

### PAIR X004  (semantic distance 0.59, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:b3420b55cc7d3f68]: 'Mum sent them £140,000': How to spot the signs a loved one is being scammed - BBC
'Mum sent them £140,000': How to spot the signs a loved one is being scammed BBC
Open problem (scout note): Families cannot see that a loved one is being groomed by a scammer until large sums are gone

FOREIGN MECHANISM SOURCE [arxiv:2609.33729]: Wave-Domain Semantic Equalization Using a Practical Dynamic Metasurface Antenna with Strong Mutual Coupling
Semantic mismatch between independently trained AI-native agents in heterogeneous networks can impair semantic communications. Hybrid analog-digital semantic equalization can align the incompatible latent representations without retraining the semantic transceivers. We study a practical realization of this approach based on a fabricated dynamic metasurface antenna (DMA), an emerging low-cost, low-power, ultracompact technology for hybrid analog-digital beamforming. We model the DMA-assisted channel using multiport-network theory (MNT), accounting for mutual coupling (MC), structural scattering, and binary lossy tuning states. We use the experimentally estimated MNT parameters of our fabricated 19-GHz DMA prototype with strong MC. We jointly optimize digital pre- and post-equalizers and the DMA at a reference receiver geometry for latent-space alignment, then freeze the digital stages and
Transferable mechanism (scout note): Align latent representations of independently trained AI agents in the physical channel without retraining either agent

### PAIR X005  (semantic distance 0.61, fused-vector patent proximity 0.70)
FINANCE PROBLEM SOURCE [news:b05d66bdce0aab7a]: Canada’s Big Six Banks Jointly Explore Digital Deposits Network - Bloomberg.com
Canada’s Big Six Banks Jointly Explore Digital Deposits Network Bloomberg.com
Open problem (scout note): Six largest Canadian banks jointly explore a shared tokenized-deposit network

FOREIGN MECHANISM SOURCE [arxiv:2609.36905]: Ternary Visible Light Communication Using Event-Based Vision Sensors
This paper proposes a ternary visible light communication method using an event-based vision sensor (EVS) and a liquid crystal display (LCD). The throughput of optical camera communication (OCC) is limited by the frame rates of conventional frame-based cameras, and EVSs are expected to overcome this limitation because their pixels asynchronously trigger events with polarity in response to brightness changes, with a temporal resolution on the order of microseconds. However, existing event-based OCC relies on binary signaling that uses only the presence or absence of events and leaves the polarity unused. The proposed method maps the three brightness transitions (increase, decrease, and no change) to ternary symbols, thereby increasing the information carried per symbol. At the transmitter, the LCD displays a marker in which the transmitted data are encoded; at the receiver, the EVS captur
Transferable mechanism (scout note): Screen-to-event-camera ternary optical link beats frame-rate limit of camera communication


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

Write the answer to: runs/2026-09-30/llm_responses/synthesis_000.json
