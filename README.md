# DSC 106 Project 2: Persuasive Visualizations (Climate)

Proposition: *"Climate change is real: global temperatures have risen meaningfully since the mid-20th century."*

Data: IMF Climate Change Indicators Dashboard, [Annual Surface Temperature Change](https://climatedata.imf.org/)
(`data/Annual_Surface_Temperature_Change.csv`). World boundaries: Natural Earth 1:50m admin-0 (`data/ne/`).

## Reproduce

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python clean_data.py          # -> data_clean.csv
.venv/bin/python viz_A_choropleth.py    # -> viz_A_choropleth.png
.venv/bin/python viz_B_yoy.py           # -> viz_B_yoy.png, viz_B_yoy_neutral.png
.venv/bin/python make_checkpoint_pdf.py # -> checkpoint_skeleton.pdf
```

## Status

- [x] Viz A: "it's real", world choropleth (2024)
- [x] Viz B: "it's overstated", year-over-year bars (World)
- [ ] Second "real" chart (ideas: share of countries above baseline per year; box plots by decade)
- [ ] Second "overstated" chart (ideas: World line on a −5 to +5 °C axis; least-warming countries)
- [ ] Final reflection (2–3 paragraphs) and author names/UCSD emails in `index.html`
- [ ] Pick which side the group is leaning toward (checkpoint page 3)

The report (course template) is `index.html`, live at https://thebigviditb.github.io/dsc106-project2/. Checkpoint page-3 bullets are in [design_decisions.md](design_decisions.md).
