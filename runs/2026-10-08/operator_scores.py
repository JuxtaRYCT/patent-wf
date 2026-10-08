"""Operator novelty scores, run 2026-10-08 (catch-up, queue mode). arXiv had not announced 2026-10-08 submissions."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
scores("2026-10-08", "novelty_score_000", """
news:99f462098638dcb8 | 1 | 1 | Trading platform market-data feed | noise
news:8bd60aaccabfe379 | 4 | 5 | Phone maker builds USDC remittances into 82M devices | device-wallet,stablecoin-remittance
news:f2b18c6af685c972 | 2 | 2 | Payments leader joins Swift board | governance
news:dc739f346c29ab41 | 4 | 5 | A third-party software error made thousands of clients pay wrong tax amounts through a money app | systematic-error,third-party-software,payment-amount-integrity
news:db8dae245241457c | 1 | 1 | Cash fund product | noise
news:8e83090540056464 | 1 | 1 | Orchestration partnership | noise
news:c1530df043e14db6 | 3 | 3 | Bitcoin-backed loans for tuition and working capital | crypto-lending
news:2f95c498043b5544 | 2 | 3 | Identity vendor partners with credit bureau | identity
news:bf99403d283ad5da | 1 | 1 | Board appointments | noise
news:40d4d8ddd194b5ca | 1 | 1 | Bank M&A | noise
news:92bc0dc348fcce55 | 1 | 1 | Vendor appointment | noise
news:b961e624450b1648 | 1 | 1 | Exchange investment | noise
news:0507254167f82cc1 | 1 | 1 | Corporate debt settlement | noise
news:681cdb137d34b95a | 4 | 4 | Programmable payment controls extended to FedNow and RTP | payment-controls,instant-payments
news:6ce08bc06942f26a | 2 | 2 | Digital-asset infrastructure partnership | noise
news:64831dcb3099060b | 4 | 5 | A fraud control that works perfectly but seconds too late is the most expensive one | control-latency,instant-payments
s2:49ec3db39774465f094aef9c2bf2fa9e5acd7ff5 | 2 | 1 | Central bank consultation process on stablecoins | regulation
""")
