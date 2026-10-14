# Design Decisions: Project 2 (Climate)

**Dataset:** IMF Climate Change Indicators Dashboard, *Annual Surface Temperature Change* (FAO FAOSTAT, derived from NASA GISS GISTEMP). Values are anomalies in °C relative to each country's 1951–1980 average, 1961–2024, for 225 countries/territories plus 5 regional aggregates and World.

**Proposition:** "Climate change is real: global temperatures have risen meaningfully since the mid-20th century."

Scores run from −2 (fully deceptive) to +2 (fully earnest).

---

## Visualization A: "It's real" (world choropleth, 2024)

| # | Decision | Score |
|---|---|---|
| 1 | Diverging midpoint shifted to −0.3 °C | −1 |
| 2 | Asymmetric, clipped color domain (−1 to +3 °C) | −1 |
| 3 | Choropleth (area-weighted) instead of a dot or bar chart | −0.5 |
| 4 | Alarming headline "Nearly Every Nation Is Running Hotter Than Its Past" | +0.5 |
| 5 | Baseline, unit, source and "213 of 213 countries with data" callout stated plainly; missing data hatched and labelled | +1.5 |

1. **Midpoint at −0.3 °C (−1).** A diverging scale implies its neutral color means "no change", but here neutral sits 0.3 °C below zero, so a country with a true anomaly of 0 already reads as light orange. We considered centering at 0, which is the honest choice, but shifting it guarantees that even the least-warmed country (Iceland, +0.035 °C) reads as clearly warm rather than neutral.
2. **Domain −1 to +3 °C, top clipped (−1).** The blue arm is short and unused (no country was below 0 in 2024), so nearly all the color resolution goes to the warm side and the map is almost entirely deep red. Everything above +3 °C (20 countries) saturates to the darkest red, and the legend reads "+3 or more" rather than showing the true maximum (+3.69 °C). A symmetric domain like −4 to +4 would make most countries a medium orange.
3. **Choropleth form (−0.5).** Maps weight countries by land area, and the largest countries (Russia, Canada) sit at high latitudes, which warm fastest. The map therefore looks redder than a per-country average would. A sorted bar or dot chart would weight Iceland and Canada equally.
4. **Headline (+0.5).** "Running hotter than its past" is emotive but literally true. In fact it understates the data, since every country with 2024 data was above its baseline. "Nearly" covers the countries the dataset omits or has no 2024 value for (e.g., Türkiye, Yemen), which makes the claim sound measured and credible.
5. **Earnest framing (+1.5).** The subtitle states the year, baseline and unit, the footer cites the IMF/FAO/NASA source, and countries without data are hatched gray and labelled in the legend instead of being colored or hidden. The "213 of 213" callout is exact and says "countries with data". These choices make the chart look rigorous and keep the deceptive color choices from drawing scrutiny.

## Visualization A2: "It's real" (percentage of countries warmer than their average, by year)

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

## Visualization B: "It's not real / overstated" (year-over-year bars, World)

| # | Decision | Score |
|---|---|---|
| 1 | Plot year-over-year change instead of the anomaly itself | −2 |
| 2 | No cumulative line or trend line | −1.5 |
| 3 | Headline "Global Temperatures Fall Almost as Often as They Rise" + "28 of 63 years were cooler" | −1 |
| 4 | Symmetric y-axis (±0.8 °C) | −0.5 |
| 5 | Accurate axis labels, source, red/blue warm/cool coloring | +1.5 |

1. **Year-over-year differences (−2).** Differencing removes the level: the World anomaly went from +0.21 °C (1961) to +2.12 °C (2024), but each bar shows only the step from the previous year. Warming years average +0.25 °C and cooling years average −0.23 °C, so the bars look like a random walk around zero. Their sum (+1.9 °C) is invisible unless a reader adds them up mentally. Plotting the anomaly directly would show the rise immediately.
2. **No cumulative or trend line (−1.5).** A running total or a fitted line would reveal the steady upward drift, so we deliberately left both out. The bars average +0.03 °C per year, which is small per bar but about 1.9 °C over the period.
3. **Headline and stat (−1).** Both are literally true: 28 of the 63 changes were negative, 34 positive and 1 (1965) zero. "Almost as often" invites the reader to treat 28 vs. 34 as a coin flip and to stop there. The count says nothing about magnitude or accumulation. The stat is colored blue to match the cooling bars, which keeps attention on them.
4. **Symmetric y-axis (−0.5).** Equal room above and below zero makes up and down swings look balanced. The real extremes (+0.60 and −0.50 °C) are not far from symmetric, so the distortion is mild, which is also why it is hard to object to.
5. **Credible scaffolding (+1.5).** The axis is labelled "Change from previous year (°C)", the subtitle says "year-over-year change", and the source is cited. Nothing on the chart is mislabelled; a careful reader could work out what is being hidden. The red/blue color scheme also mirrors the "real" side's conventions, so the chart looks like ordinary climate reporting. A single-neutral-color variant (`viz_B_yoy_neutral.png`) is included. The two-color version is more persuasive because the blue bars stand out and are easy to count.

---

## Checkpoint page 3: deceptive techniques (bullets)

**Proposition:** Climate change is real: global temperatures have risen meaningfully since the mid-20th century. *(Group leaning: TBD.)*

**"It's real" side (Viz A, map):**
- Diverging color midpoint shifted below zero (−0.3 °C), so near-zero values read as warm.
- Asymmetric, clipped color domain (−1 to +3 °C) saturates the warm end and leaves the cool arm unused.
- Area-weighted map form over-represents fast-warming high-latitude countries (Russia, Canada).
- Emotive headline with an exact, earnest callout and source to lend credibility.

**"It's real" side (Viz A2, percentage of countries by year):**
- Counts countries above their baseline instead of showing degrees, so a few very hot countries cannot drive the result, and small warming counts the same as large warming.
- A dashed 50% line stands in for "nothing is happening", so the early years read as random and the later years as a clear change.
- Red fill under the line, and only the 1965 low and the 2024 point are labelled.
- Axes, baseline and source are all accurate; the persuasion is in the metric and the framing.

**"It's overstated" side (Viz B, bars):**
- Shows only year-over-year differences, hiding the cumulative ~1.9 °C rise.
- Omits any trend or cumulative line.
- Cherry-picked frequency stat ("28 of 63 years were cooler") that ignores accumulation.
- Symmetric y-axis to make warming and cooling look balanced.
- Accurate labels and source citation so the chart reads as credible.
