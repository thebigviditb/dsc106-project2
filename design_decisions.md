# Design Decisions: Project 2 (Climate)

The full scored design decisions and rationale for each visualization are in the report, `index.html`.
This file holds the short version used on page 3 of the checkpoint PDF (`make_checkpoint_pdf.py` reads the section below).

## Checkpoint page 3: deceptive techniques (bullets)

**Proposition:** Climate change is real: global temperatures have risen meaningfully since the mid-20th century. *(Group leaning: TBD.)*

**"It's real" side (Viz A, map):**
- Shows only 2024, the hottest year on record, instead of a multi-year average.
- Diverging color midpoint shifted below zero (−0.3 °C), so near-zero values read as warm.
- Asymmetric, clipped color domain (−1 to +3 °C) saturates the warm end and leaves the cool arm unused.
- Area-weighted map form over-represents fast-warming high-latitude countries (Russia, Canada).
- Emotive headline with an exact, earnest callout and source to lend credibility.

**"It's overstated" side (Viz B, bars):**
- Shows only year-over-year differences, hiding the cumulative ~1.9 °C rise.
- Omits any trend or cumulative line.
- Cherry-picked frequency stat ("28 of 63 years were cooler") that ignores accumulation.
- Symmetric y-axis to make warming and cooling look balanced.
- Accurate labels and source citation so the chart reads as credible.
