# Nestlé (nestle) — starter data notes

Reporting entity: Nestlé S.A. group, calendar years (period_end 31 Dec). Built 4 Nov 2026.

## Documents used
- Nestlé Non-Financial Statement 2025 (published Feb 2026): https://www.nestle.com/sites/default/files/2026-02/non-financial-statement-2025.pdf. GHG tables are on printed pp. 51 (by Scope), 52 (value chain split and net), 53 (by GHG Protocol category), 54 (Emissions disclosures: location-based figures) and 55 (removals).
- Nestlé Non-Financial Statement 2024 (Feb 2025): https://www.nestle.com/sites/default/files/2025-02/non-financial-statement-2024.pdf. Used for 2024 and 2023: chart "Nestlé GHG footprint breakdown by Scope" on p. 39 and "Emissions disclosures" on p. 41.
- Corporate Governance Report, Compensation Report and Financial Statements 2025: https://www.nestle.com/sites/default/files/2026-02/corp-governance-compensation-financial-statements-2025-en.pdf. Used for Sales 2025 and 2024 (income statement, p. 80), operating segments (Note 3.1, p. 96) and geographic areas (Note 3.4, p. 101).
- Financial Statements 2024: https://www.nestle.com/sites/default/files/2025-02/2024-financial-statements-en.pdf. Used for Sales 2023 (p. 80).

Page numbers are the printed footer pages ("Non-Financial Statement 2025 51"), written `p. N`. I couldn't confirm the PDF page index.

## Which boundary each total uses (read this first)
- **All Scope 3 totals in emissions.csv use the SBTi / net zero target boundary.** No full-footprint Scope 3 total is used.
  - 2025: 66.01 Mt is "Gross Scope 3" (p. 51). It equals the "In scope" categories on p. 53 plus 2.79 Mt "Non-integrated into Nestlé's Information System", a block not yet allocated to a GHG Protocol category. That block is in scope but has no category row.
  - 2024 and 2023: the value is "Scope 3 (in scope for Net Zero Roadmap)", 71.35 and 72.93 Mt. The same chart prints "Scope 3 (not in scope for Net Zero Roadmap)" separately, at 9.69 Mt in both years. Those amounts are not in the CSV. The full footprint printed in the chart (Scopes 1, 2 market and 3 together) is 84.38 Mt for 2024 and 86.10 Mt for 2023.
  - Nestlé says the targets cover 100% of Scope 1 and 2 and 90% of Scope 3. For 2025 the NFS gives no total for out-of-scope Scope 3 and no full-footprint total. The out-of-scope category rows (purchased services 5.33, Cat 2 2.72, Cat 8 0.11, Cat 11 direct use 0.40, Cat 15 0.22) are in the CSV with a method_note. Optional "indirect use of sold products" (8.19 Mt, footnote 25) is not in the CSV.
- Scope 1 and both Scope 2 rows cover the whole group. Nestlé's totals and targets use market-based Scope 2.
- Group totals as printed for 2025 (context only, not CSV rows): 69.04 Mt gross Scopes 1–3 market-based (p. 51) and 71.31 Mt location-based (p. 54). For 2024: 74.69 market-based and 77.02 location-based (2024 NFS p. 41).

## Removals (kept out of the emissions rows)
- The headline "net" figures subtract removals. These come from insetting on farms supplying Nestlé and in sourcing landscapes.
  - 2025: removals 3.31 Mt (3.02 FLAG supply chain plus 0.29 sourcing landscape, p. 53). Net is 65.74 Mt and the net reduction is 24.52% vs the restated 2018 baseline (p. 52).
  - 2024 NFS: removals were 1.64 Mt for 2024 and 0.76 Mt for 2023 (p. 43), with 2024 net at 73.05 Mt and a 20.38% reduction. The 2025 NFS removals chart (p. 55) shows 2024 at **1.51 Mt**, so 2024 removals were revised.
- Nestlé says it does not use carbon credits "disconnected from our value chain" toward net zero. Biogenic CO2 outside Scope 1 is reported separately: 0.77 Mt in 2025 and 0.74 Mt in 2024. It is not in the CSV.

## Availability
| Year | Scope 1 | Scope 2 location | Scope 2 market | Scope 3 total (target boundary) | Scope 3 by category |
|---|---|---|---|---|---|
| 2025 | yes | yes | yes | yes | yes (p. 53) |
| 2024 | yes | yes | yes | yes | no |
| 2023 | yes | not found | yes | yes | no |

- **Scope 3 categories (2025 only).** Category 1 has **two rows** because Nestlé prints purchased goods (51.10, in scope) and purchased services (5.33, out of scope) on separate lines. Categories 10, 13 and 14 are "Not relevant for Nestlé".
- **No category data for 2024 or 2023.** The 2024 NFS lists category names but splits Scope 3 only by Dairy and livestock, Soil and forests, and Other.
- **Emissions split.** There are no emissions by segment or region. The only split is the gross footprint by value chain step, in percent (SBTi scope, p. 52), for 2018 and 2025. Its parts sum to about 100%.
  - The chart prints two unlabeled sets of percentages. I assigned the first set to 2018 and the second to 2025 from the order in the extracted text, so check this on the chart.
  - segments.csv also includes 2025 revenue by operating segment (7 rows, summing to 89,490) and by geographic area (AMS, AOA and EUR).

## Gaps and quirks
- **2025 baseline restatement.** The 2025 NFS restated the 2018 baseline for acquisitions, divestitures and better emission factors. Its 2018 figures are Scope 1 3.21, Scope 2 market 1.94, Scope 3 81.94, total 87.09. The 2024 NFS had 3.28, 2.02, 86.44 (in scope) and 91.74. The 2025 NFS shows 2024 only in a bar chart with no readable values, so the 2024 and 2023 rows come from the 2024 NFS (restated=n, with a method_note) and are **not directly comparable** with 2025.
- **2023 location-based Scope 2.** It isn't in the 2024 NFS, and I didn't use older reports for it.
- **Year label on p. 54.** The 2025 "Emissions disclosures" block on p. 54 prints no year next to its rows. I treated it as 2025 because its market-based total, 69.04, matches 2025.
- **Revenue.** The 2024 revenue comes from the 2025 financial statements. The income statement isn't marked restated, but the segment note says 2024 segment figures were restated.

## Questions for students
1. How much of Nestlé's apparent 2024→2025 Scope 3 drop (71.35 → 66.01 Mt) is real, and how much comes from re-baselining and new emission factors? Compare the two reports' 2018 baselines.
2. Which categories sit outside the SBTi boundary, about 8.8 Mt in 2025 plus 8.19 Mt optional indirect use? What would the footprint look like with them in? How does the "net" headline (24.52% reduction) change once removals (3.31 Mt) are taken out?
3. What drives the Scope 2 method gap? Location-based is 2.48 Mt and market-based 0.22 Mt in 2025, roughly 11×. What do renewable electricity purchases contribute to the reported 88.9% Scope 2 cut?

## Files and validation
- emissions.csv: 27 rows. 2025 has 21 rows (S1, S2 location, S2 market, 16 category rows, S3 total). 2024 has 4 rows and 2023 has 3.
- financials.csv: 3 rows (2025, 2024, 2023).
- segments.csv: 20 rows (10 value-chain emissions shares, 7 operating-segment revenues, 3 geographic revenues).
- All files were written with Python's csv module and re-read to check that every row has the header's field count. Validation passed.
- Values were read through WebFetch text extraction, because direct download was blocked by the proxy. Each table was checked against its raw extracted tokens and the arithmetic sums.
