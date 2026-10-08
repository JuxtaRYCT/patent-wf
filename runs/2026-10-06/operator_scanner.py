"""Operator answers, scanner packet of run 2026-10-06. T13 (fresh: AI agents used to hack Korean banks) -> 1 invention;
T07/T27 (tokenized-deposit network news) and T01 (conference/listing noise) -> nothing new."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import write
write("2026-10-06", "scanner", {
"T13": [dict(
    title="Read-time coupling: detecting autonomous LLM attack agents from how their next-request delay scales with the length of the response they just read",
    problem="South Korea reports AI agents appear to have been used to hack its banks. LLM-driven attack agents now probe bank web and API surfaces with human-like, varied requests that defeat rate limits and bot signatures built for scripts.",
    mechanism="An LLM agent has to ingest each server response before it acts, so its think time scales with the token count of what it just read and with its tool-call loop. Scripts react almost instantly regardless of length; humans skim and scale only weakly with length. For every session the edge gateway records pairs of (tokenised length of response k, delay before request k+1) and fits a per-session coupling slope, intercept and residual pattern. It adds secondary features: whether request k+1 quotes or paraphrases content from response k, and burstiness typical of tool-call loops. A classifier labels sessions as human, script or LLM agent. Unregistered LLM-agent sessions on sensitive surfaces (login, password reset, payee management, internal APIs) get tarpitted with deliberately long responses, which raises their cost because think time grows with length. Registered agents carrying valid agent credentials are allowed.",
    technical_effect="A behavioural signal that is intrinsic to how LLM agents compute (reading cost proportional to response length), independent of payload content or IP reputation, plus a tarpit that exploits the same property.",
    why_non_obvious="Bot detection uses fixed timing, headless-browser and reputation signals. Measuring the coupling between server response length and the client's next-request latency as a model-inference signature, and then exploiting it with length-inflated tarpitting, is specific to the new class of LLM attackers.",
    claim_core="A method comprising, for a client session, recording for successive server responses a response length and a delay until the client's next request, estimating a coupling between response length and delay, classifying the session as driven by a language-model agent based on the coupling, and in response applying a mitigation comprising lengthening subsequent responses or restricting access to designated endpoints.",
    keywords="AI agent attack detection, LLM agent fingerprinting, bot detection, timing analysis, response latency, tarpit, bank cybersecurity",
    domain="fraud")],
})
