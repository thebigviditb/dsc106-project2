"""Visualization A ("it's real"): world choropleth of 2024 temperature change.

Persuasive choices (documented in design_decisions.md):
  * diverging midpoint shifted to -0.3 C, so near-zero countries already read warm
  * asymmetric color domain (-1 to +3 C), so the warm arm saturates
  * alarming headline, earnest subtitle with baseline + source
"""
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.patches import Patch

ROOT = Path(__file__).parent
YEAR = 2024

# --- palette: blue <-> red diverging pair with a neutral gray midpoint ---
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
NO_DATA = "#d6d5d0"
CMAP = LinearSegmentedColormap.from_list(
    "cool_warm",
    ["#1c5cab", "#8fb8ea", "#f0efec", "#f4b49a", "#e0533a", "#a3231a", "#6e1410"],
)
# Midpoint below zero + domain clipped at +3: the deceptive part of this chart.
NORM = TwoSlopeNorm(vmin=-1.0, vcenter=-0.3, vmax=3.0)

plt.rcParams.update({
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "text.color": INK,
})

# --- data ---
data = pd.read_csv(ROOT / "data_clean.csv", keep_default_na=False, na_values=[""])
latest = data[(~data.is_aggregate) & (data.year == YEAR)][["iso3", "value"]]
n_with_data = latest.value.notna().sum()
n_warmer = (latest.value > 0).sum()

world = gpd.read_file(ROOT / "data" / "ne" / "ne_50m_admin_0_countries.shp")
# ISO_A3_EH fills in codes that ISO_A3 leaves as -99 (France, Norway, ...).
world["iso3"] = world["ISO_A3_EH"].where(world["ISO_A3_EH"] != "-99", world["ADM0_A3"])
# Natural Earth splits off Somaliland and Northern Cyprus; the IMF data reports them
# as part of Somalia and Cyprus.
world["iso3"] = world["iso3"].replace({"SOL": "SOM", "CYN": "CYP"})
world = world[world["iso3"] != "ATA"]  # Antarctica: not in the dataset
world = world.merge(latest, on="iso3", how="left").to_crs("ESRI:54030")  # Robinson

# --- plot ---
fig, ax = plt.subplots(figsize=(20, 11.5), dpi=150, facecolor=SURFACE)
ax.set_facecolor(SURFACE)
ax.set_axis_off()

world[world.value.isna()].plot(ax=ax, color=NO_DATA, edgecolor=SURFACE, linewidth=0.4, hatch="////")
world[world.value.notna()].plot(
    ax=ax, column="value", cmap=CMAP, norm=NORM, edgecolor=SURFACE, linewidth=0.4
)

fig.text(0.05, 0.93, "Nearly Every Nation Is Running Hotter Than Its Past",
         fontsize=34, fontweight="bold", ha="left")
fig.text(0.05, 0.885,
         f"Surface temperature change in {YEAR} relative to each country's 1951–1980 average (°C)",
         fontsize=19, color=INK_2, ha="left")
fig.text(0.05, 0.82, f"{n_warmer} of {n_with_data}",
         fontsize=40, fontweight="bold", color="#a3231a", ha="left")
fig.text(0.05, 0.79, f"countries with data were warmer in {YEAR}\nthan their 1951–1980 average",
         fontsize=16, color=INK_2, ha="left", va="top", linespacing=1.3)

# Color bar: ticks at whole degrees; the top end is labelled "3+" because it is clipped.
cax = fig.add_axes([0.30, 0.125, 0.40, 0.022])
sm = plt.cm.ScalarMappable(cmap=CMAP, norm=NORM)
cb = fig.colorbar(sm, cax=cax, orientation="horizontal", ticks=[-1, 0, 1, 2, 3])
cb.ax.set_xticklabels(["−1", "0", "+1", "+2", "+3 or more"], fontsize=14, color=INK_2)
cb.ax.tick_params(length=0, pad=6)
cb.outline.set_visible(False)
cb.set_label("Change vs. 1951–1980 average (°C)", fontsize=14, color=INK_2, labelpad=8)

fig.legend(handles=[Patch(facecolor=NO_DATA, edgecolor=SURFACE, hatch="////", label="No data")],
           loc="lower left", bbox_to_anchor=(0.72, 0.11), frameon=False, fontsize=14,
           labelcolor=INK_2, handlelength=2.2, handleheight=1.4)

fig.text(0.05, 0.025,
         "Source: IMF Climate Change Indicators Dashboard, Annual Surface Temperature Change "
         "(FAO FAOSTAT, derived from NASA GISS GISTEMP).",
         fontsize=12, color=INK_2, ha="left")

ax.set_position([0.02, 0.18, 0.96, 0.63])
fig.savefig(ROOT / "viz_A_choropleth.png", facecolor=SURFACE)
print(f"saved viz_A_choropleth.png  ({n_warmer} of {n_with_data} countries > 0)")
