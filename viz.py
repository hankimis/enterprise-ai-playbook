"""Charts for the Enterprise AI Adoption Playbook, from the verified numbers.
Run with a matplotlib-capable python. Outputs PNGs (+ one GIF) to paper/figs/."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

FIGS = Path(__file__).resolve().parent / "paper" / "figs"
FIGS.mkdir(parents=True, exist_ok=True)
GREEN, GOLD, RED, BLUE, GREY = "#2a7f3f", "#c9962a", "#c0392b", "#2e6fb0", "#888888"
plt.rcParams.update({"font.family": "DejaVu Sans", "figure.dpi": 130})

def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", alpha=0.25)

# Fig 1 (money shot): perception gap (METR)
def perception_gap():
    fig, ax = plt.subplots(figsize=(7.4, 5))
    bars = ax.bar(["What developers\nbelieved", "What actually\nhappened (RCT)"], [20, -19],
                  color=[GREEN, RED], width=0.55)
    ax.axhline(0, color="#333", lw=1)
    for b, v in zip(bars, [20, -19]):
        ax.text(b.get_x()+b.get_width()/2, v + (2 if v>0 else -2), f"{'+' if v>0 else ''}{v}%",
                ha="center", va="bottom" if v>0 else "top", fontsize=15, weight="bold",
                color=GREEN if v>0 else RED)
    ax.set_ylim(-28, 30)
    ax.set_ylabel("Change in task completion time")
    ax.set_title("The AI productivity gap\nSkilled developers felt 20% faster, were 19% slower",
                 fontsize=12.5, weight="bold")
    ax.text(0.5, -0.20, "METR randomized controlled trial, 2025 (experienced open-source devs)",
            transform=ax.transAxes, ha="center", fontsize=8.5, color=GREY)
    style(ax); fig.tight_layout()
    fig.savefig(FIGS/"fig1_perception_gap.png", bbox_inches="tight")
    print("fig1_perception_gap.png")

    # animated reveal
    fig2, ax2 = plt.subplots(figsize=(7.4, 5))
    def frame(i):
        ax2.clear()
        vals = [20, -19]
        shown = [vals[0]] if i == 0 else vals
        cols = [GREEN, RED][:len(shown)]
        labs = ["What developers\nbelieved", "What actually\nhappened (RCT)"][:len(shown)]
        bars = ax2.bar(labs, shown, color=cols, width=0.55)
        for b, v in zip(bars, shown):
            ax2.text(b.get_x()+b.get_width()/2, v+(2 if v>0 else -2), f"{'+' if v>0 else ''}{v}%",
                     ha="center", va="bottom" if v>0 else "top", fontsize=15, weight="bold",
                     color=GREEN if v>0 else RED)
        ax2.axhline(0, color="#333", lw=1); ax2.set_ylim(-28, 30)
        ax2.set_xlim(-0.6, 1.6)
        ax2.set_ylabel("Change in task completion time")
        ax2.set_title("The AI productivity gap\nSkilled developers felt 20% faster, were 19% slower",
                      fontsize=12.5, weight="bold")
        style(ax2)
    ani = animation.FuncAnimation(fig2, frame, frames=2, interval=1400)
    ani.save(FIGS/"fig1_perception_gap.gif", writer=animation.PillowWriter(fps=0.8))
    print("fig1_perception_gap.gif")

# Fig 2: ROI reality
def roi_reality():
    labels = ["Companies that scrapped\nmost AI projects (2025)",
              "M365 Copilot pilots\nthat scaled",
              "Orgs with meaningful\nGenAI ROI",
              "Orgs with meaningful\nAI-agent ROI"]
    vals = [42, 6, 29, 23]
    cols = [RED, RED, GOLD, GOLD]
    fig, ax = plt.subplots(figsize=(8, 4.6))
    y = np.arange(len(labels))[::-1]
    ax.barh(y, vals, color=cols, height=0.6)
    for yi, v in zip(y, vals):
        ax.text(v+1, yi, f"{v}%", va="center", fontsize=12, weight="bold")
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, 50); ax.set_xlabel("Percent")
    ax.set_title("Pilots are easy. Production and ROI are hard.", fontsize=12.5, weight="bold")
    ax.text(1.0, -0.16, "S&P Global · Gartner · WRITER 2026", transform=ax.transAxes,
            ha="right", fontsize=8.5, color=GREY)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.grid(axis="x", alpha=0.25); fig.tight_layout()
    fig.savefig(FIGS/"fig2_roi_reality.png", bbox_inches="tight"); print("fig2_roi_reality.png")

# Fig 3: AI code insecurity
def code_insecurity():
    labels = ["AI code with a\nvulnerability", "XSS tasks\nfailed", "Log-injection\ntasks failed", "Java tasks\ninsecure"]
    vals = [45, 86, 88, 72]
    fig, ax = plt.subplots(figsize=(7.8, 4.8))
    bars = ax.bar(labels, vals, color=RED, width=0.6, alpha=0.85)
    for b, v in zip(bars, vals):
        ax.text(b.get_x()+b.get_width()/2, v+1.5, f"{v}%", ha="center", fontsize=12, weight="bold")
    ax.set_ylim(0, 100); ax.set_ylabel("Percent insecure")
    ax.set_title("AI writes insecure code, and bigger models don't fix it\n2.74x more vulnerabilities than human-written",
                 fontsize=12, weight="bold")
    ax.text(1.0, -0.18, "Veracode 2025 GenAI Code Security Report (100+ LLMs)", transform=ax.transAxes,
            ha="right", fontsize=8.5, color=GREY)
    style(ax); fig.tight_layout()
    fig.savefig(FIGS/"fig3_code_insecurity.png", bbox_inches="tight"); print("fig3_code_insecurity.png")

# Fig 4: model by difficulty + pricing
def model_difficulty():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 4.2))
    d = ["<15 min", "1-4 hr", ">4 hr*"]; v = [93, 74, 67]
    bars = a1.bar(d, v, color=[GREEN, GOLD, RED], width=0.6)
    for b, val in zip(bars, v):
        a1.text(b.get_x()+b.get_width()/2, val+1.5, f"{val}%", ha="center", fontsize=12, weight="bold")
    a1.set_ylim(0, 100); a1.set_ylabel("SWE-bench resolve rate")
    a1.set_title("Match the model tier to task difficulty", fontsize=11, weight="bold")
    a1.text(0.5, -0.17, "vals.ai SWE-bench by duration  (*>4hr: n=3, not significant)",
            transform=a1.transAxes, ha="center", fontsize=8, color=GREY)
    style(a1)
    tiers = ["Everyday\n($20/mo)", "Heavy\n($200/mo)"]; tv = [20, 200]
    bars2 = a2.bar(tiers, tv, color=[BLUE, "#7a4fb0"], width=0.55)
    for b, val in zip(bars2, tv):
        a2.text(b.get_x()+b.get_width()/2, val+5, f"${val}", ha="center", fontsize=12, weight="bold")
    a2.set_ylim(0, 240); a2.set_ylabel("USD / month")
    a2.set_title("Spend by intensity, not by default", fontsize=11, weight="bold")
    a2.text(0.5, -0.17, "Cursor · Copilot · Claude Code · Windsurf (2026)",
            transform=a2.transAxes, ha="center", fontsize=8, color=GREY)
    style(a2); fig.tight_layout()
    fig.savefig(FIGS/"fig4_model_pricing.png", bbox_inches="tight"); print("fig4_model_pricing.png")

# Fig 5: when AI helps vs hurts (context-dependent effect)
def when_ai_helps():
    rows = [
        ("Greenfield task\n(Copilot RCT, n=95)*", 55.8, GREEN),
        ("Brownfield, students\n(ICER 2025, n=10)", 35.0, GREEN),
        ("New devs, 2026\n(METR update)", -4.0, GOLD),
        ("Skilled devs, mature repo\n(METR 2025, n=16)", -19.0, RED),
    ]
    labels = [r[0] for r in rows]; vals = [r[1] for r in rows]; cols = [r[2] for r in rows]
    y = np.arange(len(rows))[::-1]
    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    ax.barh(y, vals, color=cols, height=0.6)
    ax.axvline(0, color="#333", lw=1)
    for yi, v in zip(y, vals):
        ax.text(v + (2 if v >= 0 else -2), yi, f"{'+' if v>0 else ''}{v:g}%",
                va="center", ha="left" if v >= 0 else "right", fontsize=12, weight="bold",
                color=GREEN if v >= 0 else RED)
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(-30, 70); ax.set_xlabel("Change in speed / completion time")
    ax.set_title("AI is an amplifier, not a universal accelerator\nThe sign flips with task, codebase, and seniority",
                 fontsize=12.5, weight="bold")
    ax.text(1.0, -0.17, "*vendor-affiliated, single greenfield task. Bars are not directly comparable across study designs.",
            transform=ax.transAxes, ha="right", fontsize=7.5, color=GREY)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.grid(axis="x", alpha=0.25); fig.tight_layout()
    fig.savefig(FIGS/"fig5_when_ai_helps.png", bbox_inches="tight"); print("fig5_when_ai_helps.png")

# Fig 6: the agentic reality gap
def agent_reality():
    labels = ["Enterprises exploring\nAI agents*", "Deployed in\nproduction*",
              "Projects to be canceled\nby end of 2027 (Gartner)"]
    vals = [99, 11, 40]; cols = [BLUE, GREEN, RED]
    y = np.arange(len(labels))[::-1]
    fig, ax = plt.subplots(figsize=(8.2, 4.0))
    ax.barh(y, vals, color=cols, height=0.6)
    for yi, v in zip(y, vals):
        ax.text(v + 1.5, yi, f"{v}%{'+' if v==40 else ''}", va="center", fontsize=12, weight="bold")
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, 110); ax.set_xlabel("Percent")
    ax.set_title("The agentic reality: exploring is easy, production is hard",
                 fontsize=12.5, weight="bold")
    ax.text(1.0, -0.20, "*industry-survey/blog estimates;  40% is a Gartner prediction (2025-06).  Beware 'agent washing'.",
            transform=ax.transAxes, ha="right", fontsize=7.5, color=GREY)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.grid(axis="x", alpha=0.25); fig.tight_layout()
    fig.savefig(FIGS/"fig6_agent_reality.png", bbox_inches="tight"); print("fig6_agent_reality.png")

if __name__ == "__main__":
    perception_gap(); roi_reality(); code_insecurity(); model_difficulty(); when_ai_helps(); agent_reality()
