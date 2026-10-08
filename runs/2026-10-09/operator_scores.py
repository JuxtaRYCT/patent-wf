"""Operator novelty scores, run 2026-10-09 (regular daily run; little new data had arrived by run time)."""
import sys; sys.path.insert(0, "scripts/operator")
from answer import scores
scores("2026-10-09", "novelty_score_000", """
news:971760325ad6a44a | 2 | 3 | Regulator directions restricting a co-operative bank (withdrawal caps) | bank-restrictions,co-op-banks
news:57b30f431e02ddd0 | 1 | 2 | Duplicate supervisory directions to another co-operative bank | bank-restrictions
news:f1b83b0d80f13b8e | 2 | 2 | Penalty on a co-operative bank | supervision
s2:577baefa6f9e1c14a90723eb5b0d8f58f703a37b | 4 | 3 | Opponent modelling for dynamic resource trading among UAV edge servers | resource-trading,opponent-modelling
s2:e665ef02c21bca293f95a57da78621df89ad2eb4 | 4 | 3 | Incentives for workers whose quality drifts over time | incentives,non-stationary-quality
""")
