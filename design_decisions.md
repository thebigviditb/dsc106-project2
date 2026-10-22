# Design Decisions: Project 2 (Climate)

The full scored design decisions and rationale for each visualization are in the report, `index.html`.
This file holds the short version used on page 3 of the checkpoint PDF (`make_checkpoint_pdf.py` reads the section below).

## Checkpoint-only charts (not in the report)

The report has one FOR and one AGAINST slot. Charts below are on the checkpoint PDF; their full rationale lives here until the group picks which ones go in the report.

### Visualization A2: "It's real" (percentage of countries warmer than their average, by year)

**What the chart shows.** For every year from 1961 to 2024, we count how many countries were warmer than their own 1951–1980 average, and divide by the number of countries that had data that year. That gives one percentage per year. In 1965 it was 11% (21 of 187 countries). In 2024 it was 100% (213 of 213). It has been 100% every year since 2013.

| # | Decision | Score |
|---|---|---|
| 1 | Count countries above their baseline instead of plotting degrees | +2 |
| 2 | Use the dataset's own 1951–1980 baseline and a cutoff of 0 °C | +2 |
| 3 | Full 0–100% y-axis with a dashed 50% line | +2 |
| 4 | No smoothing, every year is plotted as is | +1.5 |
| 5 | Red fill under the line | +1 |
| 6 | Only two points labelled: the 1965 low and 2024 | +1 |

1. **Percentage of countries, not degrees (+2).** Every country counts the same whether it was 0.1 °C or 3 °C warmer, so a few very hot countries cannot pull the number up. We used a percentage instead of a plain count because the number of countries with data jumps from about 187 to 215 after 1991, when new countries appear.
2. **The dataset's own baseline (+2).** The cutoff is 0 °C against the 1951–1980 average that comes with the data. We did not pick a colder reference period. We also tried a 0.5 °C cutoff. It still ends near 100%, but the early years no longer look like a coin flip, and that contrast is part of the story.
3. **0–100% axis and a 50% line (+2).** The axis is not cut off. The dashed line at 50% is what you would expect if nothing was happening: in any given year about half the countries would be above their average by chance. The 1960s and early 1970s bounce around that line, which makes the climb after it easy to see.
4. **No smoothing (+1.5).** The yearly ups and downs are left in. We tried a 5-year rolling average and it made the early years look calmer than they really were. The messy start next to the flat 100% ending is the point of the chart.
5. **Red fill (+1).** The chart works without the fill. The fill makes the rising percentage look like something filling up, and red reads as heat. It is a mood choice, not a data choice.
6. **Two labels only (+1).** Both numbers are exact, but they are the only numbers on the chart, so the reader's eye goes to the low start and the 100% ending and skips the noisy years in between.


## Checkpoint page 3: deceptive techniques (bullets)

**Proposition:** "Climate change is real: global temperatures have risen meaningfully since the mid-20th century."
- Set 1 (page 1) argues the proposition is true: climate change is real.
- Set 2 (page 2) argues the proposition is false: climate change is not real, or is overstated.

**Leaning toward:** the first visualization from each set, the world map (page 1, top) and the year-over-year bar chart (page 2, top).

**Set 1, top (world map, 2024):**
- Shows only 2024, the hottest year on record, instead of a multi-year average.
- Diverging color midpoint shifted below zero (−0.3 °C), so near-zero values read as warm.
- Asymmetric, clipped color domain (−1 to +3 °C) saturates the warm end and leaves the cool arm unused.
- Area-weighted map form over-represents fast-warming high-latitude countries (Russia, Canada).
- Emotive headline with an exact, earnest callout and source to lend credibility.

**Set 1, bottom (percentage of countries warmer than average, by year):**
- Counts countries above their baseline instead of showing degrees, so small warming counts the same as large warming.
- A dashed 50% line stands in for "nothing is happening", so the early years read as random and the later years as a clear change.
- Red fill under the line, and only the 1965 low and the 2024 point are labelled.
- Axes, baseline and source are all accurate; the persuasion is in the metric and the framing.

**Set 2, top (year-over-year change, World):**
- Shows only year-over-year differences, hiding the cumulative ~1.9 °C rise.
- Omits any trend or cumulative line.
- Cherry-picked frequency stat ("28 of 63 years were cooler") that ignores accumulation.
- Symmetric y-axis to make warming and cooling look balanced.
- Accurate labels and source citation so the chart reads as credible.

**Set 2, bottom (World temperature on a −5 to +5 °C axis):**
- Y-axis fixed at −5 to +5 °C, so the ~1.9 °C rise fills under a quarter of the plot.
- Symmetric axis around zero, leaving a whole "cooling" half that no data point reaches.
- Calm headline and a "within 2.2 °C" callout that are true but frame the rise as small.
- Cool blue line, no trend line, no shading under the curve.
- Accurate labels, baseline, endpoints and source, so the chart reads as credible.
