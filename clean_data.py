"""Clean the IMF Annual Surface Temperature Change CSV into long format.

Input:  data/Annual_Surface_Temperature_Change.csv  (IMF Climate Change Indicators
        Dashboard, wide format: one row per country/region, one column per year)
Output: data_clean.csv  (long format: country, iso3, is_aggregate, year, value)

Values are temperature anomalies in degrees Celsius relative to a 1951-1980
baseline (FAOSTAT, derived from NASA GISS GISTEMP).
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent
RAW = ROOT / "data" / "Annual_Surface_Temperature_Change.csv"
OUT = ROOT / "data_clean.csv"

# keep_default_na=False stops pandas from reading Namibia's ISO2 code "NA" as missing;
# empty strings are then the only true missing values.
raw = pd.read_csv(RAW, encoding="utf-8-sig", keep_default_na=False, na_values=[""])

year_cols = [c for c in raw.columns if c.isdigit()]

long = raw.melt(
    id_vars=["Country", "ISO3"],
    value_vars=year_cols,
    var_name="year",
    value_name="value",
).rename(columns={"Country": "country", "ISO3": "iso3"})

long["year"] = long["year"].astype(int)
long["value"] = pd.to_numeric(long["value"], errors="coerce")

# Regional aggregates use non-standard codes (AFRTMP, ASIATMP, ...) and World is WLD.
# Flag them so the map can drop them and the time series can keep World.
long["is_aggregate"] = long["iso3"].str.len().ne(3) | long["iso3"].eq("WLD")

long = long[["country", "iso3", "is_aggregate", "year", "value"]].sort_values(["iso3", "year"])
long.to_csv(OUT, index=False)

if __name__ == "__main__":
    countries = long[~long.is_aggregate]
    print(f"rows: {len(long)}  countries: {countries.iso3.nunique()}  "
          f"years: {long.year.min()}-{long.year.max()}")
    for y in (2023, 2024):
        n = countries[countries.year == y].value.notna().sum()
        print(f"countries with data in {y}: {n}")
