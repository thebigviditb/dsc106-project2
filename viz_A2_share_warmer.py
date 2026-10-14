"""Visualization A2 ("it's real"): percentage of countries warmer than their 1951-1980 average, by year.

For every year, count how many countries had a positive anomaly (warmer than their own
baseline) and divide by how many countries had data that year.

Persuasive choices (documented in design_decisions.md):
  * share of countries, not degrees, so one country counts the same whether it is 0.1 or 3 C warmer
  * dashed 50% line as the "nothing is happening" level
  * red fill under the line, and only the low year and 2024 are labelled
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).parent

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e3df"
WARM = "#c62828"
FILL = "#f6d3d0"

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "text.color": INK,
})

data = pd.read_csv(ROOT / "data_clean.csv", keep_default_na=False, na_values=[""])
countries = data[~data.is_aggregate].dropna(subset=["value"])

by_year = countries.groupby("year")["value"].agg(countries="size", warmer=lambda s: int((s > 0).sum()))
by_year["share"] = by_year["warmer"] / by_year["countries"]
by_year.to_csv(ROOT / "share_warmer_by_year.csv")

years = by_year.index.values
pct = 100 * by_year["share"].values
low_year = by_year["share"].idxmin()
low_pct = 100 * by_year.loc[low_year, "share"]
last_year = years.max()
all_since = by_year.index[by_year["share"] < 1].max() + 1  # first year of the unbroken 100% run

fig, ax = plt.subplots(figsize=(10, 6), dpi=200, facecolor=SURFACE)
ax.set_facecolor(SURFACE)
fig.subplots_adjust(left=0.09, right=0.97, top=0.80, bottom=0.12)

ax.fill_between(years, 0, pct, color=FILL)
ax.plot(years, pct, color=WARM, lw=2.2)
ax.axhline(50, color="#999999", lw=1.2, ls="--")

ax.set_xlim(1961, last_year + 0.6)
ax.set_ylim(0, 100)
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
ax.set_xticks([1961, 1970, 1980, 1990, 2000, 2010, last_year])
ax.tick_params(labelsize=12, length=0, colors=INK_2)
ax.grid(axis="y", color=GRID)
ax.set_axisbelow(True)
for side in ["top", "right", "left"]:
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#bbbbbb")
ax.set_ylabel("Percentage of countries", fontsize=12, labelpad=10, color=INK_2)

ax.plot([low_year], [low_pct], "o", color=WARM, ms=7)
ax.annotate(f"{low_year}: only {low_pct:.0f}% of countries\nwere warmer than their average",
            (low_year, low_pct), xytext=(1979, 22), fontsize=11.5, va="center",
            arrowprops=dict(arrowstyle="-", color="#888888", lw=1, connectionstyle="arc3,rad=0.25"))
ax.plot([last_year], [100], "o", color=WARM, ms=7, clip_on=False)
ax.annotate(f"{last_year}: 100% of countries\nwere warmer than their average",
            (last_year, 100), xytext=(last_year - 2, 84), fontsize=11.5, ha="right", va="top",
            color=WARM, fontweight="bold")
ax.text(1998, 52, "50% = half of all countries", fontsize=11, color="#777777", va="bottom", ha="center")

fig.text(0.09, 0.93, "Each year, how many countries were warmer than normal?",
         fontsize=17, fontweight="bold")
fig.text(0.09, 0.855,
         "Percentage of countries whose yearly temperature was above their own 1951–1980 average.\n"
         f"{countries.iso3.nunique()} countries and territories, {years.min()}–{last_year}.",
         fontsize=11.5, color=INK_2, va="center", linespacing=1.5)
fig.text(0.09, 0.02,
         "Source: IMF Climate Change Indicators Dashboard, Annual Surface Temperature Change (FAO)",
         fontsize=9, color=INK_2)

fig.savefig(ROOT / "viz_A2_share_warmer.png", facecolor=SURFACE)
print(f"saved viz_A2_share_warmer.png  ({low_year}: {low_pct:.0f}%, 100% every year since {all_since})")
