# TASK synthesis_002

## SYSTEM
You are an inventor on a bank's advanced-technology team, expert in payments, fraud, credit, treasury, regulation (US, EU, UK, India) and patent drafting. You practise bisociation: transplanting a mechanism from an unrelated field into a finance problem. Rules: (1) every concept must have a concrete TECHNICAL mechanism (data structures, signals, protocols, hardware, cryptography, control loops) - not a business method; (2) it must be implementable within ~3 years; (3) name what makes it non-obvious versus the closest thing you know exists; (4) prefer concepts a bank, card network or payment processor would license; (5) if a pair yields nothing credible, return fewer ideas rather than forcing one.

## PROMPT
For each pair, transplant the foreign mechanism into the finance problem and propose 0-2 patentable invention concepts. Stretch for unusual but technically credible combinations.

### PAIR X012  (semantic distance 0.57, fused-vector patent proximity 0.71)
FINANCE PROBLEM SOURCE [news:9b7317adb57abf91]: North Dakota's state-owned bank has a dollar-backed coin live for 90+ banks and credit unions. - Stock Titan
North Dakota's state-owned bank has a dollar-backed coin live for 90+ banks and credit unions. Stock Titan
Open problem (scout note): State-owned bank's dollar-backed coin live for 90+ community banks

FOREIGN MECHANISM SOURCE [arxiv:2610.02506]: Burning Signed Graphs
We introduce and analyze a new model of graph burning, in which two competing fires (coloured yellow and green) ignite vertices of a given signed graph and propagate along its edges. The boolean sign of an edge determines whether a fire spreading along the edge changes colour or not. In each step, a player ignites a new vertex in a colour of their choice, while previously activated fires continue to spread. Given a signed graph $Γ$, the objective is to burn the maximum possible number of vertices in a single colour; the optimal achievable value is called the plurality number of $Γ$. We express the plurality number through Hamming distances to a binary code associated with $Γ$. In particular, the minimum plurality number over the switching class of $Γ$ equals the number of vertices minus the covering radius of this code. Under certain conditions on the signature, we determine exact values
Transferable mechanism (scout note): Two competing contagions on a signed graph where edge sign flips the colour that spreads

### PAIR X013  (semantic distance 0.57, fused-vector patent proximity 0.71)
FINANCE PROBLEM SOURCE [news:88923a47d68a2e33]: Chinese banking giant serves firms linked to oligarchs and autocrats to push Beijing’s agenda - International Consortium of Investigative Journalists
Chinese banking giant serves firms linked to oligarchs and autocrats to push Beijing’s agenda International Consortium of Investigative Journalists
Open problem (scout note): State bank serving sanctioned-linked firms; correspondent exposure to politically exposed networks

FOREIGN MECHANISM SOURCE [arxiv:2610.02296]: Line-Rate GTP-U Admission Control at the Edge of a Cloud-Native 5G Core: An XDP-Based Design for Kubernetes-Hosted User Plane Functions
The User Plane Function (UPF) of a 5G Standalone core terminates every GPRS Tunnelling Protocol user-plane (GTP-U) packet arriving from the radio access network, which makes its N3 interface both the busiest and the most exposed point of the mobile data path. As operators migrate the core onto Kubernetes and public cloud, the UPF increasingly shares a general-purpose Linux kernel with other workloads, and kernel-bypass frameworks such as DPDK become harder to operate. This paper presents GTP-Guard, a design for line-rate GTP-U admission control built on the eXpress Data Path (XDP) hook of the Linux kernel. GTP-Guard drops illegitimate tunnel traffic in the network driver, before socket-buffer allocation, using six ordered stages: peer allow-listing, GTP-U header validation, Tunnel Endpoint Identifier (TEID) admission against session state derived from the Packet Forwarding Control Protoc
Transferable mechanism (scout note): Line-rate admission control at the exposed edge of a 5G core using in-kernel XDP filtering

### PAIR X014  (semantic distance 0.60, fused-vector patent proximity 0.67)
FINANCE PROBLEM SOURCE [news:4d0282119ed731e5]: Mumbai Consumer Commission Orders HDFC Bank To Pay ₹92,525 To Fraud Victim, Cites Service Deficiency - Free Press Journal
Mumbai Consumer Commission Orders HDFC Bank To Pay ₹92,525 To Fraud Victim, Cites Service Deficiency Free Press Journal
Open problem (scout note): Consumer court makes bank pay fraud victim for service deficiency

FOREIGN MECHANISM SOURCE [arxiv:2610.02151]: Feasibility of Simultaneous Input-Output Constraints for Tracking in a Class of LTI Systems: Part I
This paper addresses the problem of simultaneous satisfaction of input and output constraints for LTI systems with multiple inputs with state feedback and integral action using a Control Barrier Function based governor. Necessary and sufficient conditions for the CBF-based governor to have a feasible solution and for the closed-loop solutions to be bounded and forward-invariant are derived. A systematic design procedure for choosing the free parameters of the CBF-governor is also provided. These free parameters are associated with high-order CBFs, bounds on feasible command signals, and control input magnitude. A companion paper provides several numerical examples to illustrate the results of this paper, especially the feasibility (or infeasibility) of the CBF governor when the conditions are satisfied (or not satisfied).
Transferable mechanism (scout note): Control-barrier-function governor keeps inputs and outputs inside hard limits with proven feasibility

### PAIR X015  (semantic distance 0.60, fused-vector patent proximity 0.73)
FINANCE PROBLEM SOURCE [news:1087f10882fca04e]: Fiserv Digital Asset Platform Goes Live with Financial - GlobeNewswire
Fiserv Digital Asset Platform Goes Live with Financial GlobeNewswire
Open problem (scout note): Core processor launches digital-asset platform for banks

FOREIGN MECHANISM SOURCE [arxiv:2610.00900]: Modeling Bipartite Dynamic Networks: An Additive and Multiplicative Effects Model
Researchers frequently study interactions between two distinct types of actors, represented as bipartite networks. These networks exhibit dependence patterns that differ from those in one-mode networks and therefore require models tailored to their structure. This paper develops an additive and multiplicative effects (AME) framework for longitudinal bipartite data. First, I distinguish the dependence structure and specify the corresponding modeling assumptions. Second, I introduce the bipartite dynamic AME model and develop an estimation procedure based on block coordinate descent. Third, I incorporate a squared iterative method to improve computational efficiency. Using simulations and an application to global production networks, I show that the model improves coefficient estimation, more accurately recovers the data-generating process, and better captures the multiplicative latent str
Transferable mechanism (scout note): Dynamic model for bipartite interaction networks with additive and multiplicative effects


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

Write the answer to: runs/2026-10-01/llm_responses/synthesis_002.json
