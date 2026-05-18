# Python Workshop — Insurance Claims Refactoring

A hands-on workshop for data scientists. You start with a messy but working
notebook, and end with production-ready Python code.

## Repo layout

```
data/
  claims_sample.csv     synthetic claims dataset (20 000 rows)
  generate_claims.py    script that produced the CSV — edit and re-run to regenerate
notebooks/
  claims_analysis.ipynb the notebook you will refactor
requirements.txt        pandas, matplotlib, ruff
```

## The dataset

`claims_sample.csv` contains one row per insurance claim across eight regions
in Belgium, the Netherlands, Germany, and France (2020–2024).

| Column | Type | Notes |
|---|---|---|
| `policy_id` | string | format `POL-XXXXXX`; a policy can appear more than once |
| `claim_date` | string | mostly ISO 8601; ~0.5 % are `DD/MM/YYYY` — intentional mess |
| `peril` | string | fire, flood, theft, liability, storm, water_damage; ~1 % are `UNKNOWN` or blank |
| `region` | string | BE-BRU, BE-VLG, BE-WAL, NL-NH, NL-ZH, DE-BAY, DE-NRW, FR-IDF |
| `claim_amount` | float | log-normal, 500–500 000; ~3 % are missing |
| `premium` | float | correlated with claim_amount, 200–5 000 |
| `loss_year` | int | year extracted from claim_date — redundant, intentional |

## The notebook

`claims_analysis.ipynb` is deliberately written as messy analyst code. It
loads the CSV, cleans it (three times, copy-pasted), computes loss ratios
(`claim_amount / premium`), plots average loss ratio per region, and flags
high-risk policies. It runs end-to-end, but contains a catalogue of
anti-patterns for participants to find and fix.

The workshop is **not** about exploration — the analysis logic is already
correct. The goal is to take that logic and turn it into something that can
be shipped.

## What we are building towards

By the end of the workshop the notebook should be replaced by a small Python
package with three responsibilities:

**1. Ingestion & cleaning** (`src/claims/io.py`)
A `load_claims(path)` function that validates the file exists, parses mixed
date formats, coerces types, drops true duplicates, and returns a clean
`DataFrame`. No business logic, no side effects.

**2. Feature computation** (`src/claims/features.py`)
Pure functions — `loss_ratio(df)`, `flag_high_risk(df, threshold)` — that
take a clean `DataFrame` and return a new one. Threshold and region lists are
module-level constants, not magic numbers buried in conditions.

**3. Reporting** (`src/claims/report.py`)
A `summary_by_region(df)` function that returns the aggregated table (using
`groupby`, not a manual loop), and a `plot_loss_ratios(summary)` function
that produces the bar chart. Plotting is separated from data work.

The package is imported by a thin `run.py` entry point (or a clean notebook)
that wires the three pieces together. It can be called from a scheduled job,
a CI pipeline, or a REST endpoint without modification.

## Getting started

```bash
# open in GitHub Codespaces — environment is pre-configured
# or locally:
pip install -r requirements.txt
python data/generate_claims.py   # regenerate the CSV if needed
jupyter notebook notebooks/claims_analysis.ipynb
```
