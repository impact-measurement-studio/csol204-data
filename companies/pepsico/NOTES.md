# PepsiCo, Inc. — starter data notes (built 4 Nov 2026)

## Documents used
- PepsiCo 2025 Climate Accounting Statement (published 2026) — https://www.pepsico.com/docs/pepsico-5v9wci20/media/Files/esg-topics/2025-climate-accounting-statement.pdf (Table 1 p. 6, Table 2 p. 7, Table 3a/3b p. 8, goal progress pp. 19–20). This is the only PepsiCo document found with absolute tCO2e by scope and category.
- PepsiCo Climate Change ESG topic page — https://www.pepsico.com/esg-topics/climate-change (rounded market-based summary: Scope 1 3.1M, Scope 2 0.06M, E&I 24M, FLAG 12M for 2025; used only as a cross-check).
- 2025 ESG Performance Metrics and Calculation Methodology — https://www.pepsico.com/docs/pepsico-5v9wci20/media/Files/esg-topics/2025-ESG-Performance-Metrics-and-Calculation-Methodology.pdf (only % progress against targets; it points to the Climate Accounting Statement for absolute values).
- 2024 ESG Performance Metrics, 2024 ESG Summary, 2023 ESG Performance Metrics, 2023 ESG Summary (report-downloads page). These give only percentages or rounded totals, so no rows were taken from them.
- PepsiCo Form 10-K fiscal 2025 — https://investor.pepsico.com/docs/pepsico-5v9wci20/media/Files/investors/q4-2025-form-10k.pdf (income statement p. 58, Note 1 segment table p. 66)
- PepsiCo Form 10-K fiscal 2024 — https://investor.pepsico.com/docs/default-source/investors/q4-2024/q4-2024-form-10k_kgcva0jf89d2927o.pdf (2022 net revenue, p. 61)

## Availability
| Year | Scope 1 | S2 location | S2 market | S3 total | S3 by category |
|---|---|---|---|---|---|
| 2025 | y (physical + market) | y | y | not printed | y (12 reported, 3 not relevant) |
| 2024 | y | y | y | not printed | y |
| 2023 | — | — | — | — | — |
| 2022 (baseline) | y | y | y | not printed | y |

- **2023 is missing.** The latest statement covers only 2025, 2024 and the 2022 baseline. The 2023 documents use the old 2015 baseline and give only percentages and an approximate total ("approximately 58 million metric tons", 2023 ESG Summary p. 25), so 2023 was left out rather than mixed in on a different basis.
- **No Scope 3 total row.** PepsiCo prints only "Subtotal Scope 3 FLAG" and "Subtotal Scope 3 E&I" (Table 2). Physical FLAG subtotals are 13,474,362 / 14,338,998 / 15,621,977 and E&I subtotals are 36,583,489 / 37,106,932 / 39,021,956 (2025 / 2024 / 2022). Table 3b gives smaller target-boundary, market-instrument subtotals, for example 2025 FLAG 11,758,491 and E&I 23,516,602. These are kept as notes per instructions and are not added as rows.
- **Emissions split:** none by segment or region. segments.csv therefore holds 2025 revenue by the six reportable segments, which sum to the $93,925M total (additive=y).

## Quirks, restatements, boundary
- **Fiscal year:** PepsiCo's fiscal year is 52/53 weeks, ending 27 Dec 2025, 28 Dec 2024 and 31 Dec 2022. Rows use period_type=fiscal with these end dates. They correspond to calendar years 2025, 2024 and 2022.
- **Category 1 is split into FLAG and E&I** in Table 2. Each category 1 row is the sum of the two printed rows; value_original shows both parts.
- **Categories 8, 11 and 13** are "No" in Table 1 (p. 6), and p. 5 says "We do not have any emissions to report in the remaining 3 categories." These rows are coded not_relevant.
- **Scope 1 has two versions.** The physical figure (is_total=y) and the market-based figure (is_total=n) differ because of biomethane and renewable-fuel EACs. Do not add them.
- **Restatement:** p. 19 says "2024 performance was restated due to updated baseline and 2024 data" and that prior-year E&I performance was affected by a "recalculated packaging baseline". The 2024 E&I share of progress fell from 12% (2024 report) to 9% (2025 report). restated=y is set on the 2024 and 2022 Scope 3 rows. Row-level earlier values were never published in absolute terms, so the exact size of each restatement can't be checked.
- **Arithmetic flag:** 2024 "Total Emissions Scope 1 + 2 + 3" is printed as 56,697,943, but its components (5,152,013 + 14,338,998 + 37,106,932) sum to 56,597,943, which is 100,000 lower. The 2025 and 2022 totals reconcile, and the 2025 E&I categories sum to 1 tCO2e above the subtotal (rounding). The 2022 biogenic CO2 figure is printed as "294.726". The 2024 extraction was re-checked, but students should confirm against the PDF.
- **Assurance:** KPMG limited assurance covers only the starred 2025 Scope 1 and 2 figures. A separate Apex statement covers 2025 Scope 3.
- **Boundary:** operational control. Excludes deconsolidated entities and Q4-2025 acquisitions. Target boundaries exclude some small-volume commodities, contract-manufacturer Scope 3 and concentrate-business agriculture.
- **Not opened:** the CDP climate responses (PepsiCo hosts only 2021–2023 responses, which cover old-baseline years). curl to pepsico.com was blocked by the proxy, so all reading was done with WebFetch text extraction, and page numbers are printed-page markers (written `p.`), not verified PDF page indices.

## Questions for students
1. Scope 2 method gap: in 2025 the location-based figure is 1,764,882 t and market-based is 61,149 t, a ~29x difference. How much of the "24% reduction" in Scope 1+2 comes from EACs and "system contribution" rather than physical cuts (5% physical)?
2. FLAG vs E&I and market instruments: why are Table 3b target subtotals (e.g. FLAG 11.76M) so far below the physical subtotals (13.47M)? What does including land-management removals (321,847 t in 2025) do?
3. The 2024 total does not reconcile, the packaging baseline was restated, and Category 15 jumped (75,165 to 446,794 to 168,125). What drove these, and how should a reader treat restated baselines?

## Row counts / validation
emissions.csv 57 rows (3 years × [2 Scope 1 + 2 Scope 2 + 15 Scope 3]); financials.csv 3 rows; segments.csv 6 rows. All files were written with Python csv, and every row matches the header field count (validation passed).
