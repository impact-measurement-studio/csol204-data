# Sony Group Corporation: starter data notes

Added 5 Nov 2026 for a team switching from SpaceX.

## Documents used
- Sony Group Sustainability Report 2026, Data Book 2026: https://www.sony.com/en/SonyInfo/csr/library/reports/SustainabilityReport2026_data_E.pdf
  - Emissions: "Climate Change" data table, pdf 9 (printed 008), columns FY2023, FY2024, FY2025.
  - Footnotes *1 to *4 for that table: pdf 11. Collection methods and emission factors: pdf 12. Scope 3 calculation notes: pdf 13–14.
- Sony Group Consolidated Financial Summary for the fiscal year ended March 31, 2026 (25q4_sony.pdf): FY2025 sales (pdf 1) and sales to customers by segment (pdf 15).
- The same summary for the fiscal year ended March 31, 2025 (24q4_sony.pdf): FY2024 and FY2023 "Sales and financial services revenue" (pdf 1).

I read the PDFs in a browser with pdf.js, so page numbers are PDF pages.

## Availability (FY2023 to FY2025; Sony's fiscal year ends 31 March, so FY2025 = April 2025 to March 2026)
| | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Scope 1 | yes | yes | yes |
| Scope 2 market (see below) | yes | yes | yes |
| Scope 2 location | not disclosed | not disclosed | not disclosed |
| Scope 3 total | yes | yes | yes |
| Scope 3 by category | 12 of 15 | 12 of 15 | 12 of 15 |

- Categories 8, 13 and 14 are printed "(N/A)" and described as "Not applicable" (Cat 8: "accounted for in other categories"), so they are `not_relevant`.
- The printed Scope 3 total equals the sum of the categories in FY2023 and FY2025; FY2024 is 1 thousand t above the sum of the rounded categories.
- Sony also prints a subtotal for Categories 2, 3, 4, 5, 6, 7, 11 and 12 (the scope of its reduction target). It is in `method_note`, not a separate row.
- Use of sold products (Cat 11) is the largest line: 7.45 Mt of 13.4 Mt in FY2025. It is the lifetime power use of products sold that year, booked in the year of sale (pdf 13).
- No emissions split by segment or region. segments.csv holds FY2025 sales to customers by segment (context, not an emissions allocation). The seven rows sum to ¥12,479,620 million.

## Boundary changes and quirks (read before comparing years)
- **Scope 2 method is not labelled.** Electricity factors are contracted-supplier rates (IEA country factors where none), and renewable electricity including certificates counts as zero (pdf 12). That is a market-based approach, so the rows are recorded as `market`. No location-based figure was found.
- **Sites, not the whole group.** Scope 1 and 2 cover "Group-wide ISO 14001 certified sites" (83 sites in FY2025). From FY2024 a site counts only while certified (footnote *2).
- **Financial Services spin-off.** Sony partially spun off its Financial Services business on 1 Oct 2025. FY2023 and FY2024 include it; FY2025 includes it only up to the spin-off (pdf 2 and footnote *3).
- **Revenue changes basis too.** FY2025 revenue is "continuing operations" sales (¥12,479,620 million), which excludes Financial Services. FY2023 and FY2024 are "sales and financial services revenue" as first reported (¥13,020,768 million and ¥12,957,064 million). The FY2025 summary restates FY2024 continuing operations at ¥12,034,917 million. Sony's printed Scope 1+2 intensity (0.082, 0.081, 0.078 t per million yen) matches these as-reported figures.
- **Emission factors.** From FY2025 Sony uses factors available at the end of the period, not the start (footnote *1).
- Scope 1 and 2 carry PwC Sustainability assurance marks in the table. Restatement flags are `n`: I didn't compare these values with earlier reports.

## Questions for students
1. Cat 11 fell from 12.3 Mt to 7.5 Mt in two years. How much is product efficiency, how much is fewer products sold, and how much is the grid factor? What would you need from Sony to separate them?
2. Sony reports market-based Scope 2 without saying so and no location-based figure. What does the renewable electricity rate (44.5% in FY2025) tell you about the gap you can't see?
3. The Financial Services spin-off changes both emissions and revenue. Which year-on-year comparisons are still fair, and how should T1 label them?

## Rows and validation
- emissions.csv: 57 rows (3 years × Scope 1, Scope 2 market, Scope 2 location, 15 categories, Scope 3 total).
- financials.csv: 3 rows. segments.csv: 7 rows.
- `python tools/validate.py sony` passes.
