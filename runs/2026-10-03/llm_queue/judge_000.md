# TASK judge_000

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A1-1003-01  (A1)  Per-agent canary fingerprints in bank data served to AI agents, to trace which agent leaked it
Problem: Personal-finance tools now expose synced bank data to AI agents (for example a read-only MCP server). Once many agents read the same transactions, a leak or resale cannot be attributed. Model-supply-chain research shows how much can hide in low-order bits that nobody inspects.
Mechanism: When bank data is served to an agent through an agent interface (MCP or an open-banking endpoint for agents), the server embeds a per-agent fingerprint in non-authoritative, low-salience fields. Examples are deterministic variations in merchant-descriptor normalisation, ordering of tied timestamps, and synthetic canary records that are flagged in the bank's own view but look real to the consumer. Each fingerprint is keyed to the agent's token. Leaked data found later (dark-web dumps, scraped datasets, model outputs) is matched against the keys to identify the leaking agent and token. The agent's access is then revoked and its developer is notified. Authoritative fields such as amounts and dates are never altered.
Claim core: A method comprising receiving a request for account data from an autonomous agent via an agent interface, generating a response in which non-authoritative fields and optional canary records encode a fingerprint keyed to the agent's credential while authoritative fields are unaltered, storing the key, and upon detection of the data outside authorised channels, decoding the fingerprint to identify the agent credential.
Closest prior art found:
  - [paper sim=0.797] arxiv:2609.00060 | A Formal Analysis of Agent Payment Protocols | 
    Agent payment protocols are emerging as a key transaction layer for autonomous commerce, enabling AI agents to purchase goods and services and execute payments on users'behalf. Unlike conventional payment flows, they distribute user intent, delegated authority, credential use, settlement, and fulfillment across multiple actors and stages, creating security dependencies that no single message or participant can enforce. Yet these guarantees remain largely implicit across evolving specifications, schemas, and reference implementations, with little systematic formal analysis. We formalize four representative agent payment protocols: x402, MPP, ACP, and AP2 in Tamarin. Using a common abstraction
  - [paper sim=0.780] arxiv:2608.25474 | Separating Disclosure from Authorization: Field-Tier Minimization for Agent Action Mediation | 
    A system that authorizes an action must see enough of it to decide, and a system that attests to its decision must record enough to be audited. Both pressures push raw action parameters -- recipients, payment memos, record identifiers -- into an append-only ledger that cannot delete them. We show the two are separable. We classify each parameter field, not each action class, into three tiers: fields a policy may legitimately match on, which cross raw; fields that are policy-relevant but identifying, which cross only as projections such as an email domain or a templated route shape; and fields with no legitimate policy use, which never leave the workload. The central property is that the ledg
  - [paper sim=0.780] arxiv:2607.21824 | Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense | 
    Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users'behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model, through prompt injection and misalignment. We show that the more consequential risks lie one layer down, in the protocol between agents and commerce services. There, vulnerabilities are structural : exploitation is deterministic and ndependent of which model an agent runs, so no model improvement removes them. Across three leading platforms we identify 33 such vulnerabilities, each succeeding deterministically regardless of the deployed 

## OUTPUT JSON SCHEMA
```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "judgments"
 ],
 "properties": {
  "judgments": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "id",
     "novelty",
     "non_obviousness",
     "utility",
     "feasibility",
     "commercial",
     "eligibility",
     "crazy",
     "verdict",
     "rationale"
    ],
    "properties": {
     "id": {
      "type": "string"
     },
     "novelty": {
      "type": "integer"
     },
     "non_obviousness": {
      "type": "integer"
     },
     "utility": {
      "type": "integer"
     },
     "feasibility": {
      "type": "integer"
     },
     "commercial": {
      "type": "integer"
     },
     "eligibility": {
      "type": "integer"
     },
     "crazy": {
      "type": "integer"
     },
     "verdict": {
      "type": "string",
      "enum": [
       "pursue",
       "refine",
       "drop-anticipated",
       "drop-weak"
      ]
     },
     "rationale": {
      "type": "string"
     }
    }
   }
  }
 }
}
```

Write the answer to: runs/2026-10-03/llm_responses/judge_000.json
