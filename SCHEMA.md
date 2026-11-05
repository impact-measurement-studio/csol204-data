# Data schema

Every company has a folder `companies/<slug>/` with three CSV files and a `NOTES.md`. All files are UTF-8 CSV with a header row. Quote any field that contains a comma.

Slugs: `amazon`, `rivian`, `nvidia`, `john-deere`, `patagonia`, `nestle`, `ikea`, `pepsico`, `tesla`, `microsoft`, `spacex`, `sony`, `app`.

## The rules that matter most

1. **Missing is not zero.** If a company doesn't report a number, the row has a `status` other than `reported` and a **blank** value. Never type 0 for a number that isn't printed.
2. **Every reported number has a source:** document, URL, page and a short quote (the row label or ≤ 20 words) so anyone can find it.
3. **Never add Scope 2 location-based and market-based.** They are two views of the same electricity, so they go in separate rows.
4. **Take the latest report's value.** If a company restated an earlier year, use the newest figure, set `restated=y` and put the old value in `method_note`.
5. **Don't sum entities.** If a company reports for two entities (IKEA: Ingka Group and Inter IKEA Group), each row names its `reporting_entity`. Never add them together.

## emissions.csv

One row per entity × period × scope × category × method.

| Column | What goes in it |
|---|---|
| `company_slug` | Must match the folder name. |
| `reporting_entity` | The entity the report covers, as printed (e.g. `Microsoft Corporation`, `Ingka Group`). |
| `period_label` | As the company labels it: `FY2025` or `2025`. |
| `period_end` | Last day of the period, `YYYY-MM-DD` (Microsoft FY2025 → `2025-06-30`). |
| `period_type` | `fiscal` or `calendar`. |
| `scope` | `1`, `2` or `3`. |
| `scope3_category` | `1`–`15` or `total` for Scope 3; blank for Scopes 1 and 2. |
| `scope2_method` | `location` or `market` for Scope 2 (required). Blank for Scope 1 and 3, except `market` for a company's own market-based Scope 1 (PepsiCo reports one; the blank row is the physical inventory). |
| `status` | `reported`, `not_relevant` (the company says so), `not_estimated` (the company says it hasn't calculated it) or `not_disclosed` (simply absent). |
| `value_tco2e` | Metric tonnes CO2e. Blank unless `status=reported`. |
| `value_original`, `unit_original` | The number and unit exactly as printed (e.g. `15.14`, `MMT CO2e`). |
| `is_total` | `y` for a scope total or a printed Scope 3 total. Category rows are `n`. |
| `restated` | `y` if the value differs from what the company first published. |
| `method_note` | Boundary, method change, restatement, assurance: anything a reader needs to interpret the number. |
| `source_doc`, `source_url`, `source_page`, `source_quote` | Where the number is. Page as `pdf 37` (PDF page) or `p. 37` (printed page). |

## financials.csv

Total revenue for the same entity and periods: `company_slug, reporting_entity, period_label, period_end, period_type, revenue_value, currency, unit_multiplier, source_doc, source_url, source_page, source_quote`. `unit_multiplier` is usually `million`.

## segments.csv

Splits of emissions or revenue: `company_slug, reporting_entity, period_label, split_type, split_label, metric_type, value, unit, additive, source_doc, source_url, source_page, source_quote`.

- `split_type`: `segment`, `region`, `business_line` or `other`.
- `metric_type`: `emissions` or `revenue` (or another metric, named, with its `unit`).
- For an emissions split, start `split_label` with the scope: `Scope 1: Asia`.
- `additive`: `y` if the parts add up to the printed total.
- A revenue split is context, **not an emissions allocation**. Label any chart that uses it that way.

## Validation

```bash
python tools/validate.py            # all companies
python tools/validate.py microsoft  # one company
```

The same check runs automatically on every pull request.
