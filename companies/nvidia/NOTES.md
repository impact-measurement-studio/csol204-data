# NVIDIA Corporation: starter data notes

## Documents used
- NVIDIA Sustainability Report Fiscal Year 2026: https://images.nvidia.com/aem-dam/Solutions/documents/NVIDIA-Sustainability-Report-Fiscal-Year-2026.pdf
  - Emissions: Sustainability Indicators, "Energy, Efficiency, and Climate" table, printed p. 30 (columns FY26, FY25, FY24; header "GHG Emissions (MT CO2e)*").
  - Use-of-sold-products target, and the Category 1 method change: printed p. 12.
- NVIDIA Corporation Form 10-K for the fiscal year ended January 25, 2026 (SEC EDGAR): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
  - Total revenue comes from Item 8, Consolidated Statements of Income ("In millions").
  - Segment revenue comes from Item 7 MD&A, "Revenue by Reportable Segments".

I read both documents with WebFetch. A direct download of the PDF was blocked, so I couldn't tell the PDF page numbers. Pages are given as printed pages (`p. 30`). The 10-K HTML has no printed page numbers that I could extract, so its locations are given as section headings.

## Availability (FY2024 to FY2026; fiscal years end in late January)
| | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| Scope 1 | yes | yes | yes |
| Scope 2 location | yes | yes | yes |
| Scope 2 market | yes (568) | yes (printed 0) | yes |
| Scope 3 total | yes | yes | yes |
| Scope 3 by category | Cats 1-8 only | Cats 1-8 only | Cats 1-8 only |

- Categories 9 to 15 do not appear in the table and I found no relevance or exclusion statement, so they are recorded as `not_disclosed`. That includes Category 11 (use of sold products), even though p. 12 sets a target: "Reduce Scope 3 emissions intensity from use of sold GPU products by 75% per PFLOP by FY30" (FY23 base, measured per PFLOPS).
- The printed Scope 3 total equals the sum of Categories 1-8 in every year (I checked this in the script).
- The report has no emissions split by segment, region or site. segments.csv therefore holds FY2026 revenue by reportable segment from the 10-K: Compute & Networking $193,479M and Graphics $22,459M. These sum to the $215,938M total (additive = y).
- Fiscal year ends: FY2026 ended 2026-01-25, FY2025 ended 2025-01-26 and FY2024 ended 2024-01-28. These come from the 10-K income statement periods.

## Restatements, method changes and quirks
- The table footnote says that "due to improved data collection and calculation methodology", some prior-year values "no longer directly match" earlier reports. These prior-year values are not assured. The FY2025 and FY2024 rows therefore have restated = y. I did not compare them against the earlier reports.
- FY26 Category 1 moved from a full spend-based approach to supplier-specific activity data for key components (p. 12).
- Only the FY26 Scope 1 and Scope 2 figures have limited assurance.

## Questions for students
1. Category 11 is missing even though use-phase emissions are probably NVIDIA's largest footprint. How can the company set a per-PFLOP target with no Category 11 figure, and what would a Category 11 estimate need?
2. FY26 Scope 2 location-based is 308,891 t but market-based is 568 t, and FY25 market-based is 0. What instruments (renewable energy purchases or certificates) explain this gap, and how credible are they?
3. Category 1 nearly tripled from FY24 to FY26 while the method changed. How much of the growth is real and how much comes from the method, and how does emissions intensity per $ of revenue change?

## Rows and validation
- emissions.csv: 57 rows. For each of the 3 years: Scope 1, Scope 2 location, Scope 2 market, 15 Scope 3 categories and a Scope 3 total.
- financials.csv: 3 rows.
- segments.csv: 2 rows.
- All files were written with Python's csv module. Every row matched the header's field count.
