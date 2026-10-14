"""Visualization C ("it's overstated"): World temperature anomaly on a wide y-axis.

Persuasive choices (documented in design_decisions.md):
  * y-axis fixed at -5 to +5 C, so a ~1.9 C rise fills under a quarter of the plot
  * symmetric axis around zero, with a whole "cooling" half no data point reaches
  * calm headline + "within X C" callout that is true but frames the rise as small
  * cool blue line, no trend line, no shading under the curve
  * accurate labels, baseline, endpoints and source, so the chart reads as credible
"""
import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).parent

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e3df"
LINE = "#2a78d6"  # same COOL blue as Viz B; a cool color for a warming series

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "text.color": INK,
})

data = pd.read_csv(ROOT / "data_clean.csv", keep_default_na=False, na_values=[""])
world = data[data.iso3 == "WLD"].set_index("year").value.sort_index().dropna()

first_year, last_year = world.index.min(), world.index.max()
max_abs = world.abs().max()
# Round the "stayed within" figure up to the next 0.1 C so the callout stays true.
within = math.ceil(max_abs * 10) / 10

YLIM = 5.0  # the deceptive part of this chart

fig, ax = plt.subplots(figsize=(20, 10), dpi=150, facecolor=SURFACE)
ax.set_facecolor(SURFACE)

ax.plot(world.index, world.values, color=LINE, linewidth=2.6, zorder=3)
ax.axhline(0, color=INK_2, linewidth=1.2, zorder=2)

ax.set_ylim(-YLIM, YLIM)
ax.set_xlim(first_year - 1, last_year + 1)
ax.set_yticks(range(-5, 6))
ax.yaxis.set_major_formatter(lambda v, _: f"{v:+.0f}" if abs(v) > 1e-9 else "0")
ax.set_xticks(range(1965, 2025, 5))
ax.tick_params(colors=INK_2, labelsize=15, length=0, pad=8)
ax.grid(axis="y", color=GRID, linewidth=1, zorder=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_ylabel("Change vs. 1951–1980 average (°C)", fontsize=16, color=INK_2, labelpad=12)

# Endpoint labels: honest numbers, placed in the empty space the wide axis creates.
for yr, dy in ((first_year, -1.2), (last_year, 1.3)):
    v = world[yr]
    ax.scatter([yr], [v], s=46, color=LINE, zorder=4)
    ax.annotate(f"{yr}: {v:+.2f} °C", (yr, v), xytext=(yr, v + dy),
                ha="left" if yr == first_year else "right", va="center",
                fontsize=15, color=INK_2,
                arrowprops=dict(arrowstyle="-", color=INK_2, linewidth=0.8))

fig.text(0.06, 0.93, "Global Temperatures Have Held Within a Few Degrees of Normal",
         fontsize=34, fontweight="bold", ha="left")
fig.text(0.06, 0.885,
         f"World mean surface temperature change relative to the 1951–1980 average, "
         f"{first_year}–{last_year}",
         fontsize=19, color=INK_2, ha="left")
fig.text(0.06, 0.825,
         f"Every year since {first_year} stayed within {within:.1f} °C of the long-term average",
         fontsize=19, fontweight="bold", color=LINE, ha="left")

fig.text(0.06, 0.035,
         "Source: IMF Climate Change Indicators Dashboard, Annual Surface Temperature Change, "
         "World (FAO FAOSTAT, derived from NASA GISS GISTEMP).",
         fontsize=12, color=INK_2, ha="left")

ax.set_position([0.08, 0.12, 0.89, 0.66])
fig.savefig(ROOT / "viz_C_wide_axis.png", facecolor=SURFACE)
print(f"saved viz_C_wide_axis.png  ({first_year} {world[first_year]:+.3f} -> "
      f"{last_year} {world[last_year]:+.3f} C; rise {world[last_year] - world[first_year]:+.3f} C; "
      f"data spans {world.min():+.2f}..{world.max():+.2f} of a {2 * YLIM:.0f} C axis)")
