"""Operator answers, synthesis packet of run 2026-10-05. 2 pairs -> 1 invention."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import write
write("2026-10-05", "synthesis", {
"X000": [dict(
    title="Identity-transition continuity credentials: updating KYC across banks after a name or gender change without freezes or full re-KYC",
    problem="When a person's legal identity attributes change (gender transition, marriage, name correction, a PAN/Aadhaar update), linked identity systems fall out of sync. Banks see a KYC mismatch, freeze accounts or demand full re-KYC, and the harm falls on people least able to absorb it. People also cannot easily prove to a caller or a bank that the 'old' and 'new' identity are the same person.",
    mechanism="The authority that records the change (a registrar, ID agency or first-updating bank) issues a signed transition credential. It binds a commitment to the old attribute set to the new attribute set and states the effective date and the issuing authority, but does not reveal the old attributes to anyone who has not already seen them. A bank holding the old record verifies the credential with a zero-knowledge equality proof that its stored old attributes match the commitment. It then updates the record in place and keeps account history, mandates and credit history continuous, with no freeze. Linked systems such as the credit bureau and payee-verification name tables receive the same credential, so confirmation-of-payee and bureau matching do not fail. The customer holds the credential in a wallet and can re-present it to any later institution.",
    technical_effect="Synchronises identity-attribute changes across independent KYC databases with cryptographic linkage and minimal disclosure, removing mismatch-driven freezes.",
    why_non_obvious="Verifiable credentials attest current attributes. A credential whose subject is the transition itself, bound to a commitment over the prior attributes and verified against each institution's own stored record, is a distinct construction motivated by harms documented in identity-system research.",
    claim_core="A method comprising receiving a signed credential binding a commitment to prior identity attributes with updated identity attributes, verifying the issuer signature, verifying by a zero-knowledge proof that stored attributes of an existing customer record match the commitment, updating the record to the updated attributes while preserving account linkages, and propagating the credential to linked verification systems.",
    keywords="identity attribute change, KYC update, name change, gender marker, verifiable credential, zero knowledge proof, account freeze, record linkage",
    domain="identity")],
})
