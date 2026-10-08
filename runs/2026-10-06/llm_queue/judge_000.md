# TASK judge_000

## SYSTEM
You are a senior patent examiner (USPTO art unit 3690s / 3620s, EPO, and Indian Patent Office experience) and a bank's head of innovation. For each idea you see the idea and the closest prior art retrieved automatically. Judge strictly: if the closest prior art discloses the core mechanism, novelty <= 3 and verdict 'drop-anticipated'. Eligibility: 10 = clear technical effect (improves how a computer, network, sensor or cryptographic system works); 1 = pure business method / mental process. 'crazy' rewards ideas that are surprising yet credible. Verdicts: pursue | refine | drop-anticipated | drop-weak.

## PROMPT
Judge each idea.

### A1-1006-01  (A1)  Session-continuity chain: proving at payment time that the device holds the history of earlier sessions, which cloned or remote devices lack
Problem: Banks are moving to real-time fraud warnings before payments clear, but the strongest attacks run from a device that looks legitimate: cloned app credentials, a replayed device binding, or a fresh device enrolled with stolen OTPs. Device binding proves possession of a key, and keys can be extracted or re-enrolled.
Mechanism: The banking app keeps a rolling local chain. After each session it stores a small context record (hashes of the session's transaction IDs, UI event digests, server nonces and coarse timing), keyed by a ratchet that advances every session, and sends the server only a commitment. On a high-risk payment the server challenges the device to open a random subset of past records, chosen at different depths in the chain. The genuine long-lived installation answers instantly. A cloned or newly enrolled device lacks the history, and a remote-access attacker would need to have exfiltrated the whole store. This makes storage and history, not computational hardness, the attacker's bottleneck. The response feeds the pre-clearing risk decision as a continuity score, and a failed proof escalates to an out-of-band check.
Claim core: A method comprising storing on a client device, after each session, a context record ratcheted from a prior record and transmitting a commitment to a server; upon a payment request, issuing a challenge identifying randomly selected prior records; receiving openings of the records; verifying them against stored commitments; and conditioning payment authorisation on a continuity score derived from the verification.
Closest prior art found:
  - [paper sim=0.794] arxiv:2610.08262 | Contextual Chain: Lightweight Continuity Authentication for Intermittently Connected Devices | 
    Can authentication make memory, rather than computational hardness, the attacker's bottleneck? Contextual Chain is a lightweight continuity protocol for intermittently connected devices that share evolving physical or operational context. An honest device follows one realized history, updating a compact accumulator and fixed hash-based readiness lanes; outages cause pause or bounded rollback, not branch search. After the epoch is frozen, a fresh challenge selects one lane under a short deadline. An outsider that missed context may therefore need to prepare for many mature histories before learning which one will be tested. In the standard random-oracle model, a causal counting theorem lower-
  - [paper sim=0.778] arxiv:2610.02838 | Axient: Manifest-Bound Evidence for On-Chain Financial Protocols: Seven-Layer Derivation, Correlation, Tamper Rejection, and Reproducible Claim Promotion | 
    Hybrid on-chain financial protocols are frequently evaluated with evidence that is individually useful but collectively insufficient: a unit test, transaction receipt, screenshot, service response, or several matching hashes may be presented as proof of a complete workflow even when the layers share one generated source or omit the financial authority that matters. This paper develops a manifest-bound evidence architecture for such systems. A sealed execution manifest binds declared system identities, roles, schemas, and release identity. Seven evidence layers are retained with registered derivations and linked by a common correlation identity. A conjunctive claim-promotion rule requires pro
  - [patent sim=0.768] patent:US20260289570A1 | SYSTEMS AND METHODS FOR TRANSACTION-TRIGGERED ISSUANCE AND AUTOMATED ROTATION OF VIRTUAL PAYMENT CARDS TO PREVENT PAYMENT FRAUD | Secure Purchase LLC
    Systems and methods are for preventing payment fraud using transaction-triggered issuance and automated rotation of virtual payment card credentials. A system maintains a secure association between a user account and underlying payment credentials issued by financial institutions. The system generates a randomized virtual payment card credential and transmits the same for use at a payment interface. Upon completion of an authorized transaction or satisfaction of a predefined usage condition, the randomized virtual payment card credential is automatically invalidated to prevent reuse. A replacement randomized virtual payment card credential is generated without user intervention. The security

### A2b-1006-01  (A2b)  Read-time coupling: detecting autonomous LLM attack agents from how their next-request delay scales with the length of the response they just read
Problem: South Korea reports AI agents appear to have been used to hack its banks. LLM-driven attack agents now probe bank web and API surfaces with human-like, varied requests that defeat rate limits and bot signatures built for scripts.
Mechanism: An LLM agent has to ingest each server response before it acts, so its think time scales with the token count of what it just read and with its tool-call loop. Scripts react almost instantly regardless of length; humans skim and scale only weakly with length. For every session the edge gateway records pairs of (tokenised length of response k, delay before request k+1) and fits a per-session coupling slope, intercept and residual pattern. It adds secondary features: whether request k+1 quotes or paraphrases content from response k, and burstiness typical of tool-call loops. A classifier labels sessions as human, script or LLM agent. Unregistered LLM-agent sessions on sensitive surfaces (login, password reset, payee management, internal APIs) get tarpitted with deliberately long responses, which raises their cost because think time grows with length. Registered agents carrying valid agent credentials are allowed.
Claim core: A method comprising, for a client session, recording for successive server responses a response length and a delay until the client's next request, estimating a coupling between response length and delay, classifying the session as driven by a language-model agent based on the coupling, and in response applying a mitigation comprising lengthening subsequent responses or restricting access to designated endpoints.
Closest prior art found:
  - [paper sim=0.808] s2:f0888a645148559fc788a0efb5a1c3f4cfd99d92 | LLM-Based Agents for Cybersecurity: A Systematic Review of Architectures, Applications, and Open Challenges | 
    The rapid evolution of Large Language Models (LLMs) has opened new frontiers in cybersecurity automation, enabling intelligent agents capable of multi-step reasoning, tool invocation, and autonomous decision-making across complex security tasks. While individual applications have emerged across threat intelligence, vulnerability assessment, penetration testing, and security operations center (SOC) automation, a systematic understanding of the LLM-based agent paradigm in cybersecurity—encompassing both single-agent and multi-agent architectures—remains lacking. This paper presents a systematic literature review following PRISMA guidelines, identifying records through 59 structured web-search 
  - [paper sim=0.801] arxiv:2609.05911 | Structurally Close, Temporally Distant: Measuring Security Exposure in Long-Horizon LLM Agents | 
    Long-horizon LLM agents interact with untrusted content, persistent memory, external state, and sensitive tools. Existing analyses often characterize attacks by the number of execution steps between malicious input and a downstream action. We show that temporal remoteness can overstate security separation in stateful agents. We introduce a provenance-aware execution graph linking agent events through deterministic state, identifier, and tool provenance, and define \emph{influence distance} $\DI$ as the shortest structural path from an untrusted source to a sensitive action. We compare it with \emph{sequence distance} $\DT$, the shortest injection--sink path in the ordered trajectory. Since t
  - [paper sim=0.799] s2:c95ac9afc251c89f70846c87b2b2a1bb4aaf57c5 | Security Risk Assessment and Layered Protection Strategies for Large Language Model Banking Chatbots with Privacy Considerations | 
    Abstract But now, given the AI revolution and increased interest in bringing virtual agents and assistants to life banks too are testing LLM-powered AI agents that may assist customers, explain and customize products as well as simplify operational work done by bank employees in the background. But similar systems are susceptible to prompt injection, insecure output handling, and other LLM-specific threats that had only become more prevalent since these publications. Existing surveys and frameworks survey the generic security space of LLMs but do not propose reach an end-to-end, banking-specific threat model nor deployable defense architecture for assistants in line with systems from core in

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

Write the answer to: runs/2026-10-06/llm_responses/judge_000.json
