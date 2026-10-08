# TASK judge_000

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A1-1002-01  (A1)  Delegation-residue sweep: proving that revoked access by an AI agent or a person is actually gone
Problem: Banks are starting to give accounts and spending authority to AI agents (a stablecoin firm now wants to be 'a bank for people and their AI agents'), and to human delegates (family members, carers). Smart-home research shows that 'temporary' access quietly becomes persistent surveillance, because revocation removes the visible grant but not the residue: tokens, sessions, linked devices and copied data. In banking that residue includes network tokens on another device, OAuth refresh tokens, standing mandates, notification endpoints and data already shared.
Mechanism: Each delegation is registered as a capability graph listing everything it created: network tokens and the devices holding them, API and refresh tokens, payees and standing instructions it set up, notification endpoints (email, phone, push), consented data shares, and copies of statements delivered. On revocation, a sweep walks the graph and revokes each element. It then actively probes for residue: it attempts a zero-value token authorisation, an OAuth refresh and a notification-delivery check on every endpoint. For data held by an agent, it requires a deletion attestation produced inside the agent's trusted execution environment, with classical attestation now and certified-deletion cryptography later. The account holder receives a signed residue report; anything that cannot be confirmed revoked is listed and blocked at the network level. A 'safety reset' mode runs the same sweep for people leaving coercive relationships, where an abuser may still hold access.
Claim core: A method comprising recording, for a delegation of account authority, a graph of credentials, devices, endpoints, instructions and data shares created under the delegation; upon revocation, revoking each element and issuing probe requests to confirm each credential and endpoint is inoperative; requiring a deletion attestation from a trusted execution environment of the delegate for shared data; and generating a signed report identifying any element not confirmed revoked.
Closest prior art found:
  - [paper sim=0.741] arxiv:2609.01836 | Agent Memory Is a Surface for Endogenous Authorization Laundering | 
    Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations. When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks. We term this failure endogenous authorization laundering, where spurious permissions written into memory lead to unauthorized actions as their provenance is washed away. We then introduce EAL-Bench, which measures how accurately persistent memory preserves evolving authorization state and whether errors propagate to downstream unauthorized actio
  - [paper sim=0.740] s2:899c00b8a21efa78c2b018dc1ae4519d621c87a2 | Agent-access receipts for artificial intelligence-mediated content and application programming interface access: a reproducible synthetic security experiment | 
    Artificial intelligence (AI)-mediated web and application programming interface (API) access is often treated as a bot-management problem—identify an automated caller and then allow, block, delay, challenge, or meter the request. That framing is useful but incomplete. A disputed access decision can depend on the caller’s authenticated identity, the represented principal, delegated authority, declared purpose, and resource or API surface. It can also depend on the current policy snapshot, response sensitivity, payment or licensing state, and the survival of validation evidence after the request has completed. This article presents a reproducible synthetic experiment using an agent-access rece
  - [paper sim=0.731] arxiv:2608.29381 | Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback | 
    AI agents are moving toward persistent, stateful execution across various applications, accumulating execution state and external effects that are costly to reconstruct after failures. Checkpoint and rollback (C/R) are becoming essential for recovery, yet their security implications remain largely unexplored. Correct rollback does not imply secure recovery: a faithfully restored checkpoint may resume an execution whose states, assumptions, and external effects never coexisted in any valid history. In this paper, we present the first systematic security study of checkpoint and rollback in existing agent systems. By examining representative agent C/R systems, we characterize the design space o

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

Write the answer to: runs/2026-10-02/llm_responses/judge_000.json
