# TASK synthesis_000

## SYSTEM
You are an inventor on a bank's advanced-technology team, expert in payments, fraud, credit, treasury, regulation (US, EU, UK, India) and patent drafting. You practise bisociation: transplanting a mechanism from an unrelated field into a finance problem. Rules: (1) every concept must have a concrete TECHNICAL mechanism (data structures, signals, protocols, hardware, cryptography, control loops) - not a business method; (2) it must be implementable within ~3 years; (3) name what makes it non-obvious versus the closest thing you know exists; (4) prefer concepts a bank, card network or payment processor would license; (5) if a pair yields nothing credible, return fewer ideas rather than forcing one.

## PROMPT
For each pair, transplant the foreign mechanism into the finance problem and propose 0-2 patentable invention concepts. Stretch for unusual but technically credible combinations.

### PAIR X000  (semantic distance 0.55, fused-vector patent proximity 0.71)
FINANCE PROBLEM SOURCE [news:6c09a24e018c4ffd]: Banks face an impossible bind in AFCA’s proposed ‘Scam Rules’ - Banking Day
Banks face an impossible bind in AFCA’s proposed ‘Scam Rules’ Banking Day
Open problem (scout note): Australia's proposed scam rules leave banks unable to prove 'reasonable steps' — evidence gap

FOREIGN MECHANISM SOURCE [arxiv:2610.02374]: "I'm trying not to get hacked:" How Adults with Intellectual and Developmental Disabilities Navigate Security and Privacy Notifications
Security and privacy notifications, such as login alerts, spam email warnings, and cookie consent requests, play a critical role in shaping users' responses to digital risks. Yet most notifications overlook cognitive accessibility, limiting their effectiveness for people with intellectual and developmental disabilities (IDD). We investigate how adults with IDD perceive and respond to common security and privacy notifications across mobile and web applications. Through a formative user study with seven adults with IDD, we identify three factors shaping understanding and decision-making: (1) interpretation is influenced by task and interface context; (2) unfamiliar terms, both technical and non-technical, are grounded in everyday concepts; and (3) uncertainty about outcomes leads to hesitation, avoidance, diagnostic exploration, or support-seeking. These findings lead to three design impli
Transferable mechanism (scout note): Security notifications (login alerts, warnings) fail adults with intellectual disabilities; cognitive accessibility of warnings

### PAIR X001  (semantic distance 0.59, fused-vector patent proximity 0.66)
FINANCE PROBLEM SOURCE [news:9a1f83320fe7bc8b]: Lloyds Bank staff save man from being conned out of £13,500 - after scam involving sending money to names including 'Donald Trump' 'Kim Kardashian' and 'Jennifer Lawrence' - Peterborough Telegraph
Lloyds Bank staff save man from being conned out of £13,500 - after scam involving sending money to names including 'Donald Trump' 'Kim Kardashian' and 'Jennifer Lawrence' Peterborough Telegraph
Open problem (scout note): Victim paying payees named after celebrities; staff caught it — payee-name semantics as a scam signal

FOREIGN MECHANISM SOURCE [arxiv:2610.02056]: Local Consistency Does Not Guarantee Global Conservation: Auditing Zero-Shot Composition of Airway Flow Operators
Neural operators approximate PDE solutions within a geometry family, but independently learned local operators need not form a consistent global simulator. We study frozen, single-pass composition for steady incompressible flow in idealized two-dimensional airway trees. Separate Tube, bifurcation, and trifurcation DeepONets are trained on 4,872 primitive CFD cases using field supervision and auxiliary divergence, port-flux, component-balance, and port-pressure penalties. The validation-selected deployment is frozen before whole-tree CFD fields are inspected and assembled without tree training, iterative coupling, flux correction, or CFD-informed adjustment. It retains major flow patterns and controlled pathology responses with 0.204-0.215 s CPU inference, but has a 22.68% prescribed-inlet-normalized external residual. A post-hoc sensitivity protocol, frozen before new training and evalua
Transferable mechanism (scout note): Independently learned local models that are each consistent need not conserve a global quantity when composed; audit for conservation

### PAIR X002  (semantic distance 0.56, fused-vector patent proximity 0.69)
FINANCE PROBLEM SOURCE [news:38825d01bb7f5e23]: 40 million Americans are unnecessarily locked out of open banking - American Banker
40 million Americans are unnecessarily locked out of open banking American Banker
Open problem (scout note): 40 million Americans locked out of open banking connections

FOREIGN MECHANISM SOURCE [arxiv:2610.02506]: Burning Signed Graphs
We introduce and analyze a new model of graph burning, in which two competing fires (coloured yellow and green) ignite vertices of a given signed graph and propagate along its edges. The boolean sign of an edge determines whether a fire spreading along the edge changes colour or not. In each step, a player ignites a new vertex in a colour of their choice, while previously activated fires continue to spread. Given a signed graph $Γ$, the objective is to burn the maximum possible number of vertices in a single colour; the optimal achievable value is called the plurality number of $Γ$. We express the plurality number through Hamming distances to a binary code associated with $Γ$. In particular, the minimum plurality number over the switching class of $Γ$ equals the number of vertices minus the covering radius of this code. Under certain conditions on the signature, we determine exact values
Transferable mechanism (scout note): Two competing contagions on a signed graph where edge sign flips the colour that spreads

### PAIR X003  (semantic distance 0.58, fused-vector patent proximity 0.67)
FINANCE PROBLEM SOURCE [news:9b7317adb57abf91]: North Dakota's state-owned bank has a dollar-backed coin live for 90+ banks and credit unions. - Stock Titan
North Dakota's state-owned bank has a dollar-backed coin live for 90+ banks and credit unions. Stock Titan
Open problem (scout note): State-owned bank's dollar-backed coin live for 90+ community banks

FOREIGN MECHANISM SOURCE [arxiv:2610.01030]: Correlation Analysis between Terrain Features and eLoran Spatial ASF according to DEM Spatial Resolution
The ASF is a major source of positioning error in eLoran system and is affected by terrain characteristics along the signal propagation path. This study analyzes the correlations between spatial ASF and path-based terrain features using NASA SRTM 30m and NGII 90m DEMs. Path mean elevation and path mean slope were extracted along the propagation paths from the Gwangju eLoran transmitter to measurement locations in the Incheon and Pyeongtaek port areas. The results show that both terrain features are strongly correlated with spatial ASF, with the higher-resolution NASA SRTM DEM generally exhibiting stronger correlations, particularly for path mean slope. These findings demonstrate the importance of DEM spatial resolution in terrain-based spatial ASF analysis and provide a basis for selecting terrain data for future machine-learning-based ASF prediction
Transferable mechanism (scout note): eLoran terrestrial timing/positioning as a GNSS-independent reference; terrain-driven error mapping

### PAIR X004  (semantic distance 0.55, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:4d0282119ed731e5]: Mumbai Consumer Commission Orders HDFC Bank To Pay ₹92,525 To Fraud Victim, Cites Service Deficiency - Free Press Journal
Mumbai Consumer Commission Orders HDFC Bank To Pay ₹92,525 To Fraud Victim, Cites Service Deficiency Free Press Journal
Open problem (scout note): Consumer court makes bank pay fraud victim for service deficiency

FOREIGN MECHANISM SOURCE [arxiv:2610.02296]: Line-Rate GTP-U Admission Control at the Edge of a Cloud-Native 5G Core: An XDP-Based Design for Kubernetes-Hosted User Plane Functions
The User Plane Function (UPF) of a 5G Standalone core terminates every GPRS Tunnelling Protocol user-plane (GTP-U) packet arriving from the radio access network, which makes its N3 interface both the busiest and the most exposed point of the mobile data path. As operators migrate the core onto Kubernetes and public cloud, the UPF increasingly shares a general-purpose Linux kernel with other workloads, and kernel-bypass frameworks such as DPDK become harder to operate. This paper presents GTP-Guard, a design for line-rate GTP-U admission control built on the eXpress Data Path (XDP) hook of the Linux kernel. GTP-Guard drops illegitimate tunnel traffic in the network driver, before socket-buffer allocation, using six ordered stages: peer allow-listing, GTP-U header validation, Tunnel Endpoint Identifier (TEID) admission against session state derived from the Packet Forwarding Control Protoc
Transferable mechanism (scout note): Line-rate admission control at the exposed edge of a 5G core using in-kernel XDP filtering

### PAIR X005  (semantic distance 0.57, fused-vector patent proximity 0.68)
FINANCE PROBLEM SOURCE [news:88923a47d68a2e33]: Chinese banking giant serves firms linked to oligarchs and autocrats to push Beijing’s agenda - International Consortium of Investigative Journalists
Chinese banking giant serves firms linked to oligarchs and autocrats to push Beijing’s agenda International Consortium of Investigative Journalists
Open problem (scout note): State bank serving sanctioned-linked firms; correspondent exposure to politically exposed networks

FOREIGN MECHANISM SOURCE [arxiv:2610.02151]: Feasibility of Simultaneous Input-Output Constraints for Tracking in a Class of LTI Systems: Part I
This paper addresses the problem of simultaneous satisfaction of input and output constraints for LTI systems with multiple inputs with state feedback and integral action using a Control Barrier Function based governor. Necessary and sufficient conditions for the CBF-based governor to have a feasible solution and for the closed-loop solutions to be bounded and forward-invariant are derived. A systematic design procedure for choosing the free parameters of the CBF-governor is also provided. These free parameters are associated with high-order CBFs, bounds on feasible command signals, and control input magnitude. A companion paper provides several numerical examples to illustrate the results of this paper, especially the feasibility (or infeasibility) of the CBF governor when the conditions are satisfied (or not satisfied).
Transferable mechanism (scout note): Control-barrier-function governor keeps inputs and outputs inside hard limits with proven feasibility


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

Write the answer to: runs/2026-10-01/llm_responses/synthesis_000.json
