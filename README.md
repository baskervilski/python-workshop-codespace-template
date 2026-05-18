# Claims Loss Ratio Analysis

Exploratory analysis of insurance claims data across the Benelux, Germany,
and France portfolio. The notebook produces loss ratio metrics by region and
peril, and flags high-risk policies for review.

The next step is to turn this into a deployable service — batch job or API,
TBD — so underwriters can run it on fresh exports without opening a notebook.

## Data

`data/claims_sample.csv` — one row per claim, 2020–2024.

| Column | Type | Notes |
|---|---|---|
| `policy_id` | string | `POL-XXXXXX`; one policy can have multiple claims |
| `claim_date` | string | ISO 8601; some legacy rows use `DD/MM/YYYY` |
| `peril` | string | fire, flood, theft, liability, storm, water_damage |
| `region` | string | BE-BRU, BE-VLG, BE-WAL, NL-NH, NL-ZH, DE-BAY, DE-NRW, FR-IDF |
| `claim_amount` | float | log-normal distribution, 500–500 000; some values missing |
| `premium` | float | 200–5 000 |
| `loss_year` | int | year extracted from `claim_date` |

The CSV was generated with `data/generate_claims.py` (seed 42). Re-run it to
produce a fresh sample, or swap in real data with the same schema.

## Notebook

`notebooks/claims_analysis.ipynb` covers:

- data loading and cleaning (mixed date formats, missing amounts, unknown perils)
- loss ratio computation (`claim_amount / premium`) per policy
- average loss ratio aggregated by region, visualised as a bar chart
- high-risk policy flagging above a claim amount threshold
- loss ratio trend by year

## Productionising

The analysis logic in the notebook needs to become an importable, testable
package. Rough decomposition:

- **ingestion** — load a CSV or database export, normalise date formats,
  coerce types, deduplicate
- **features** — compute loss ratios, apply the high-risk threshold; pure
  functions, no I/O
- **reporting** — aggregate by region/peril/year, produce the summary table
  and charts

Whether this runs as a scheduled batch job (e.g. triggered on each monthly
export) or as a lightweight API that scores on demand is still open. Either
way the core logic should be the same module, just with a different entry
point wired around it.

## Setup

```bash
pip install -r requirements.txt
jupyter notebook notebooks/claims_analysis.ipynb
```
