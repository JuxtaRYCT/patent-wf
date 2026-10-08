"""Operator novelty scores, run 2026-10-07 (catch-up, queue mode)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
R = "2026-10-07"
low = lambda ids, note="No transferable finance mechanism", tag="off-topic": "\n".join(f"{i} | 2 | 1 | {note} | {tag}" for i in ids.split())
scores(R, "novelty_score_000", f"""
arxiv:2610.09730 | 5 | 4 | Find the weakest trust assumptions under which a protocol still meets its security goal | minimal-trust,protocol-verification
arxiv:2610.10075 | 5 | 4 | Differentially private heavy-node detection in hierarchies with tiny error | differential-privacy,hierarchical-counts
arxiv:2610.09632 | 4 | 3 | Age of information when multiple server streams merge | data-freshness,queueing
arxiv:2610.09697 | 3 | 2 | Hardware attacks in automotive threat analysis | hardware-security
arxiv:2610.10148 | 4 | 3 | Reconcile bottom-up and top-down carbon accounting | carbon-accounting,reconciliation
arxiv:2610.09262 | 2 | 1 | Reading-position baseline for highlights | recommender
{low("arxiv:2610.09398 arxiv:2610.09617 arxiv:2610.10001 arxiv:2610.09379 arxiv:2610.09327 arxiv:2610.10517 arxiv:2610.09883 arxiv:2610.09285 arxiv:2610.09334 arxiv:2610.09580 arxiv:2610.09766 arxiv:2610.09315 arxiv:2610.09855 arxiv:2610.09776 arxiv:2610.09747 arxiv:2610.09405 arxiv:2610.10441 arxiv:2610.10096 arxiv:2610.10487 arxiv:2610.09619 arxiv:2610.09583 arxiv:2610.09744 arxiv:2610.09936 arxiv:2610.09815")}
""")
scores(R, "novelty_score_001", f"""
arxiv:2610.09911 | 3 | 2 | Validated scale for perceived value alignment | hci
arxiv:2610.10173 | 4 | 4 | Exposure is not attention: audit the gap between shown, noticed and consumed | exposure-attention-gap,audit
arxiv:2610.10386 | 3 | 2 | Fault characterisation in self-stabilising protocols | distributed-systems
news:7ce7fb272a3f1e50 | 3 | 3 | Central bank studies local-currency stablecoin with a private issuer | stablecoins,central-bank
news:987173c42cad1f3f | 3 | 3 | ERP vendor adds wires and stablecoin payments | erp-payments
news:45d7100a082ef625 | 4 | 5 | Agent payment approvals bound to the exact payment executed | agentic-payments,approval-binding
news:ed190321ab8e7af3 | 3 | 4 | Recurring check-fraud pattern hitting insurance agencies weekly | check-fraud
news:2399e1ffd51bd1a2 | 3 | 3 | Agentic order-to-cash automation raises funding | agentic-finance-ops
news:1aa254b641506f27 | 4 | 4 | Logistics operational data used to extend SMB credit | alt-data-lending,smb
arxiv:2610.10010 | 6 | 6 | A secret issued for one purpose usually grants a larger capability; define and enforce purpose-limited secrets | purpose-limited-keys,least-privilege,cryptography
arxiv:2610.10149 | 4 | 4 | Telegram pump-and-dump schemes combined with honeypot tokens that trap buyers | crypto-scams,honeypot-tokens
arxiv:2610.09581 | 5 | 5 | Forensic reconstruction of agent logs must bind each finding to supporting evidence | agent-forensics,evidence-binding
{low("arxiv:2610.10430 arxiv:2610.10044 arxiv:2610.09928 arxiv:2610.10054 arxiv:2610.10486 news:a487a879854db8c7 news:a5c059701ac8434c news:0580ce9fa226f474 news:837c4defe564bd14 gh:accomplish999/position-sizer news:dc78d5a3bb8b0991 arxiv:2610.10476", "Off-topic, duplicate or low-information")}
""")
