"""Operator examiner judgments, run 2026-10-06 (catch-up). A2b-1006-01 got a stage-2 web deep check."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import judge
judge("2026-10-06", {
"A1-1006-01": (5, 4, 7, 7, 6, 8, 6, "refine", "The mechanism source itself (Contextual Chain, arXiv 2610.08262) gives the continuity-authentication primitive; device binding and transaction-history knowledge questions are known. Residue: a ratcheted per-session context chain with random-depth challenges used as a payment-time continuity factor against cloned or re-enrolled banking apps. Narrow but technically eligible."),
"A2b-1006-01": (5, 4, 7, 8, 7, 8, 7, "refine", "DEEP CHECK: LLM-agent traffic and timing fingerprinting is published: FP-Agent (arXiv 2605.01247), 'Whose Agent Are You?' (2606.20910), 'Known By Their Actions' UI-trace timing (2605.14786), and inter-request-interval analysis (2510.07176). The coupling between response length and next-request delay is a narrower feature that is likely obvious next to those. The length-inflation tarpit that exploits reading cost is the most defensible element. Keep as a dependent-claim set or a defensive publication."),
})
