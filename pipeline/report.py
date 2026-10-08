"""Charts for docs (matplotlib PNG). Palette: validated reference categorical slots 1-3 (all-pairs pass),
every mark direct-labelled (slot 3 aqua is < 3:1 on the light surface -> labels are mandatory)."""
from __future__ import annotations

import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .common import EXPORTS, ROOT, log, run_dir

L = log("report")
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"
ARM_COLOR = {"A2a": "#2a78d6", "A2b": "#eb6834", "A1": "#1baf7a"}
ARM_NAME = {"A2a": "A2a  AI scanner, zero-shot", "A2b": "A2b  AI scanner, signal-grounded",
            "A1": "A1   Literature cross-pollination"}
ORDER = ["A2a", "A2b", "A1"]
FIG = ROOT / "docs" / "figures"


def _style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9, length=0)
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def novelty_strip(df: pd.DataFrame):
    """Two small multiples: raw full-text novelty (length-confounded) vs length-controlled novelty."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.6), facecolor=SURFACE, sharey=True)
    rng = np.random.default_rng(3)
    panels = [("novelty_pa", "Raw: full idea text vs prior art\n(confounded — short ideas look novel)"),
              ("novelty_sf", "Length-controlled: equal 45-word short form\n(fair comparison)")]
    df = df.copy()
    df["novelty_sf"] = 1 - df["max_sim_patent_sf"]
    for ax, (col, title) in zip(axes, panels):
        _style(ax)
        for y, arm in enumerate(ORDER[::-1]):
            v = df.loc[df.arm == arm, col].dropna().values
            if not len(v):
                continue
            ax.scatter(v, y + rng.uniform(-0.18, 0.18, len(v)), s=24, color=ARM_COLOR[arm],
                       edgecolor=SURFACE, linewidth=1.2, zorder=3)
            med = np.median(v)
            ax.plot([med, med], [y - 0.32, y + 0.32], color=INK, linewidth=2, zorder=4)
            ax.text(med, y + 0.36, f"median {med:.3f}", ha="center", va="bottom", fontsize=8, color=INK)
        ax.set_title(title, loc="left", fontsize=9.5, color=INK)
        ax.set_xlabel("1 − max cosine similarity to prior art", fontsize=8.5, color=INK2)
    axes[0].set_yticks(range(len(ORDER)))
    axes[0].set_yticklabels([ARM_NAME[a] for a in ORDER[::-1]], fontsize=9, color=INK)
    fig.suptitle("Embedding novelty barely separates the approaches once text length is controlled",
                 x=0.01, ha="left", fontsize=11.5, color=INK)
    fig.tight_layout()
    fig.savefig(FIG / "novelty_by_arm.png", dpi=180)
    plt.close(fig)


def arm_metrics(summary: list[dict]):
    s = {r["arm"]: r for r in summary}
    for r in summary:
        r["pursue_share"] = r["pursue"] / r["n"] if r["n"] else 0
        r["anticipated_share"] = r["drop_anticipated"] / r["n"] if r["n"] else 0
    panels = [("anticipated_share", "Judged already existing", "{:.0%}"),
              ("judge_novelty_mean", "Examiner novelty (1–10)", "{:.1f}"),
              ("vendi_sf_per_idea", "Diversity (Vendi ÷ n)", "{:.2f}"),
              ("pursue_share", "'Pursue' after deep check", "{:.0%}")]
    fig, axes = plt.subplots(1, 4, figsize=(12, 2.9), facecolor=SURFACE, sharey=True)
    for ax, (k, title, fmt) in zip(axes, panels):
        _style(ax)
        arms = [a for a in ORDER if a in s]
        vals = [s[a].get(k, 0) or 0 for a in arms]
        ys = np.arange(len(arms))[::-1]
        ax.barh(ys, vals, height=0.56, color=[ARM_COLOR[a] for a in arms], edgecolor=SURFACE, linewidth=2)
        for y, v in zip(ys, vals):
            ax.text(v, y, "  " + fmt.format(v), va="center", fontsize=9, color=INK)
        ax.set_title(title, fontsize=10, color=INK, loc="left")
        ax.set_xlim(0, max(vals) * 1.45 if max(vals) else 1)
        ax.set_xticks([])
        ax.spines["bottom"].set_visible(False)
        ax.grid(False)
    axes[0].set_yticks(np.arange(len(ORDER))[::-1])
    axes[0].set_yticklabels([ARM_NAME[a] for a in ORDER], fontsize=9, color=INK)
    fig.suptitle("Does each approach produce novel, diverse, pursuable ideas?", x=0.01, ha="left",
                 fontsize=11.5, color=INK)
    fig.tight_layout()
    fig.savefig(FIG / "arm_metrics.png", dpi=180)
    plt.close(fig)


def themes_chart(themes: pd.DataFrame, top: int = 15):
    t = themes.sort_values("opportunity", ascending=False).head(top).iloc[::-1]
    fig, ax = plt.subplots(figsize=(9, 0.36 * top + 1.2), facecolor=SURFACE)
    _style(ax)
    labels = [", ".join(x.split(", ")[:3]) for x in t.terms]
    ax.barh(range(len(t)), t.opportunity, height=0.62, color="#2a78d6", edgecolor=SURFACE, linewidth=2)
    for i, v in enumerate(t.opportunity):
        ax.text(v if v >= 0 else 0, i, f"  {v:.2f}", va="center", fontsize=8.5, color=INK)
    ax.set_yticks(range(len(t)))
    ax.set_yticklabels([f"T{int(th):02d}  {lab}" for th, lab in zip(t.theme, labels)], fontsize=8.5, color=INK)
    ax.axvline(0, color=INK2, linewidth=0.8)
    ax.set_xlabel("opportunity score = weighted z-scores of pain, pull, momentum, push, whitespace",
                  fontsize=8.5, color=INK2)
    ax.set_title("Approach 2 scanner — top opportunity themes", loc="left", fontsize=11.5, color=INK)
    fig.tight_layout()
    fig.savefig(FIG / "scanner_themes.png", dpi=180)
    plt.close(fig)


def main():
    """Figures for the arm comparison documented in docs/ (pinned to the first, full 45-day run)."""
    FIG.mkdir(parents=True, exist_ok=True)
    out = ROOT / "runs" / "2026-09-30"
    if (EXPORTS / "idea_register.csv").exists():
        df = pd.read_csv(EXPORTS / "idea_register.csv")
        if "run" in df:
            df = df[df.run == "2026-09-30"]
        novelty_strip(df)
    if (out / "evaluation.json").exists():
        arm_metrics(json.loads((out / "evaluation.json").read_text())["arms"])
    if (out / "scanner_themes.csv").exists():
        themes_chart(pd.read_csv(out / "scanner_themes.csv"))
    L.info("figures -> %s", FIG)


if __name__ == "__main__":
    main()
