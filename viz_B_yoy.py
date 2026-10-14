"""Visualization B ("it's overstated"): year-over-year change in World temperature.

Persuasive choices (documented in design_decisions.md):
  * plots only delta[t] = value[t] - value[t-1], hiding the cumulative rise
  * symmetric y-axis so up and down swings look balanced
  * no cumulative or trend line
  * accurate labels and source citation, so the chart reads as credible

Writes two variants: red/blue bars (viz_B_yoy.png) and single neutral color
(viz_B_yoy_neutral.png).
"""
import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

ROOT = Path(__file__).parent

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e3df"
WARM = "#e0533a"
COOL = "#2a78d6"
NEUTRAL = "#7a7974"

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "text.color": INK,
})

data = pd.read_csv(ROOT / "data_clean.csv", keep_default_na=False, na_values=[""])
world = data[data.iso3 == "WLD"].set_index("year").value.sort_index()
delta = world.diff().dropna()  # 1962-2024

n_years = len(delta)
n_cooler = (delta < 0).sum()
# Symmetric limit, rounded up to the next 0.2 C, so both directions get equal room.
lim = math.ceil(delta.abs().max() / 0.2) * 0.2


def draw(colored: bool, out_name: str) -> None:
    fig, ax = plt.subplots(figsize=(20, 10), dpi=150, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)

    colors = [WARM if d > 0 else COOL for d in delta] if colored else NEUTRAL
    ax.bar(delta.index, delta.values, width=0.72, color=colors, zorder=3)
    ax.axhline(0, color=INK_2, linewidth=1.2, zorder=4)

    ax.set_ylim(-lim, lim)
    ax.set_xlim(delta.index.min() - 1, delta.index.max() + 1)
    ax.set_yticks([round(-lim + 0.2 * i, 1) for i in range(int(round(2 * lim / 0.2)) + 1)])
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:+.1f}" if abs(v) > 1e-9 else "0")
    ax.set_xticks(range(1965, 2025, 5))
    ax.tick_params(colors=INK_2, labelsize=15, length=0, pad=8)
    ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_ylabel("Change from previous year (°C)", fontsize=16, color=INK_2, labelpad=12)

    fig.text(0.06, 0.93, "Global Temperatures Fall Almost as Often as They Rise",
             fontsize=34, fontweight="bold", ha="left")
    fig.text(0.06, 0.885,
             "Year-over-year change in world mean surface temperature, 1962–2024",
             fontsize=19, color=INK_2, ha="left")
    fig.text(0.06, 0.825,
             f"{n_cooler} of {n_years} years were cooler than the year before",
             fontsize=19, fontweight="bold", color=COOL if colored else INK, ha="left")

    if colored:
        ax.legend(handles=[Patch(color=WARM, label="Warmer than previous year"),
                           Patch(color=COOL, label="Cooler than previous year")],
                  loc="lower right", frameon=False, fontsize=14, labelcolor=INK_2,
                  ncol=2, bbox_to_anchor=(1.0, 1.0))

    fig.text(0.06, 0.035,
             "Source: IMF Climate Change Indicators Dashboard, Annual Surface Temperature Change, "
             "World (FAO FAOSTAT, derived from NASA GISS GISTEMP).",
             fontsize=12, color=INK_2, ha="left")

    ax.set_position([0.08, 0.12, 0.89, 0.66])
    fig.savefig(ROOT / out_name, facecolor=SURFACE)
    print(f"saved {out_name}")


draw(colored=True, out_name="viz_B_yoy.png")
draw(colored=False, out_name="viz_B_yoy_neutral.png")
print(f"{n_cooler} of {n_years} cooler; warmer={int((delta > 0).sum())}; "
      f"sum of deltas={delta.sum():+.3f} C (hidden cumulative rise)")
