# Rivian Automotive, Inc. – starter data notes

## Documents used
- **Rivian 2025 Impact Report** (published 2026; covers 1 Jan–31 Dec 2025). Appendix 6.3.1 "Select environmental metrics", printed p. 74, has 2024 and 2025 values. https://downloads.rivian.com/2md5qhoeajym/5SG64WrtEOtpeZIB8jxWdF/ff90a99a12fc3c66bb7594ec75dac277/Rivian_2025_Impact_Report.pdf
- **FY23 Environmental and Social Metrics Report** (covers 2022 base year and 2023). Consolidated Statement of Environmental Metrics is on printed p. 11, Scope 3 by category on p. 18, and the category relevance notes on pp. 14–15. https://assets.rivian.com/2md5qhoeajym/1SBXlQiRdPUBrfRzkw5zoj/f06b69a2609ef61f9c401cba6346da76/FY23_Environmental_and_Social_Metrics_Report.pdf
- **Form 10-K, FY2025**: revenue for 2023–2025 and Note 18 Segment Information. https://www.sec.gov/Archives/edgar/data/1874178/000187417826000008/rivn-20251231.htm
- **Form 10-K, FY2024**: 2022 revenue. https://www.sec.gov/Archives/edgar/data/1874178/000187417825000007/rivn-20241231.htm

Page numbers are the printed footer numbers (`p. N`). I could not see PDF page indices. In the FY23 report the cover appears unnumbered, so the PDF page is probably the printed page + 1.

## Availability (calendar years, ending 31 Dec)
| Year | Scope 1 | S2 location | S2 market | S3 total | S3 by category | Source |
|---|---|---|---|---|---|---|
| 2025 | y | y | y | y | y (10 categories) | 2025 Impact Report |
| 2024 | y | y | y | y | y (10 categories) | 2025 Impact Report |
| 2023 | y | y | y | y | y (10 categories) | FY23 E&S Metrics Report |
| 2022 (base year) | y | y | y | y | y (10 categories) | FY23 E&S Metrics Report |

- Rivian reports Scope 3 categories 1–7, 9, 11 and 12.
- For 2022–2023, categories 8, 10, 13, 14 and 15 are `not_relevant`, with the company's reasons quoted from pp. 14–15.
- For 2024–2025 the same categories are `not_disclosed`: they are simply missing from the Impact Report table, which gives no relevance statement.
- No emissions split by segment, site or region was found. segments.csv therefore holds 2025 revenue by reportable segment: Automotive $3,830M and Software and Services $1,557M. Together they equal the $5,387M total ("There are no inter-segment revenues").

## Could not open or find
- **FY25 and FY24 Environmental Metrics Reports.** The scaling-responsibly page lists them without links, and I found no company-hosted URL. These reports hold the full methodology, the Apex review report, and any restatement notes for 2024. The 2024 values come from the 2025 Impact Report, so they are the latest published, but I could not check them against the FY24 report.
- **2024 Impact Goals Update Report.** The fetch from ctfassets.net failed.
- **2022 Impact Report and FY22 metrics report.** These are available only by email request, so I could not check whether the 2022 values in the FY23 report were restated. The FY23 report has no restatement note, so every row is `restated=n`.
- **10-K page numbers.** The HTML filing showed no printed page numbers. The FY25 Item 8 index lists the Statement of Operations at p. 75.

## Quirks
- Boundary: operational control, GHG Protocol. Scope 1 and 2 are prepared "in accordance with" the GHG Protocol; Scope 3 is calculated "with reference to" it.
- Assurance: limited assurance or review by Apex Companies LLC. For 2025 this covers the figures marked with an asterisk.
- Category 11 (Use of sold products) is lifetime charging emissions per model multiplied by vehicles sold. It is the largest or second-largest category in every year, so it moves with deliveries and grid factors.
- The FY23 category rows sum to 1 t below the printed totals in both years (rounding). The 2024 and 2025 rows sum exactly.
- The two 10-K revenue tables split revenue differently. The Statement of Operations shows Automotive / Software and services of 3,830 / 1,557, while Note 4 disaggregation shows Software and services at 1,551. I used the Statement of Operations and segment figures.
- Revenue jumped from $1,658M (2022) to $4,434M (2023) as production ramped, so intensity ratios shift a lot.

## Questions for students
1. **Scope 2 method gap flips sign.** Market-based is above location-based in 2024 (143,672 vs 134,669) but below it in 2025 (102,702 vs 109,241). What contractual instruments changed? The report has a "-6,539" line for "Impacts of contractual instruments and MBM emission factors".
2. **Use of sold products swings.** Category 11 was 790,186 t (2022), 2,056,691 (2023), 2,108,889 (2024) and 1,450,500 (2025). How much of the drop is fewer vehicles sold, grid decarbonisation, or a method change? This needs the FY25 Environmental Metrics Report.
3. **Category status changes.** The FY23 report calls categories 8, 10, 13, 14 and 15 not relevant, but the 2025 Impact Report is silent on them. Also, Capital goods rose from 138,274 t (2023) to 353,945 t (2025): R2 / Normal plant expansion, or a method change?

## Rows written
- emissions.csv: 76 rows (4 years × 19)
- financials.csv: 4 rows
- segments.csv: 2 rows

CSV validation passed: every row has the header's field count.
