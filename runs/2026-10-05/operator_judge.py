"""Operator examiner judgments, run 2026-10-05 (catch-up)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import judge
judge("2026-10-05", {
"A1-1005-01": (5, 4, 7, 5, 6, 7, 5, "refine", "IBM US20150280924A1 / US20160269397A1 (re-issuing attribute credentials with commitments, Idemix-style) and Visa US20260212346A1 (automatic credential update on account migration) cover the cryptographic building blocks; ZK equality proofs are standard. Residue: a credential whose subject is the attribute transition, verified against each institution's own stored record to update KYC without freezes and propagated to payee-name and bureau matching. Narrow but socially valuable (India KYC-mismatch freezes, trans inclusion)."),
})
