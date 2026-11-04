# Tesla, Inc. starter data: notes

## Emissions source (added 4 Nov 2026)

Tesla 2025 Impact Report (Extended Version), https://www.tesla.com/ns_videos/2025-extended-version-tesla-impact-report.pdf. Printed page numbers match PDF pages. The report's text is not selectable (outlined), so values were read from the rendered pages and need a person to check them against the page:
- p. 191 "Scope 1 and 2 GHG Emissions": 2025, 2024 and 2023 by site type (Manufacturing and Support, SSD, Other), location-based Scope 1 and 2; market-based Scope 2 for 2025 and 2024 only. Only the 2025 totals carry the assurance asterisk.
- p. 192 "Scope 3 GHG Emissions": Categories 1–9, 11, 12 and a total for 2025, 2024, 2023. Categories 14 and 15 "not applicable"; Category 13 "already accounted for in other categories"; Category 10 not mentioned.
- p. 189–190 methodology: operational control; Tesla says historical figures should be taken from the most recent report.

Things worth investigating:
- 2023 Scope 1 is printed "211,00" (a typo for 211,000, implied by its parts and the total).
- 2025 Scope 3 categories sum to 56,537,000 t but the printed total is 56,416,000 t.
- Category 11 more than doubled from 2023 (3.2 Mt) to 2025 (8.5 Mt).
- Scope 2 market-based is only about 10% below location-based (755,000 vs 837,000 t in 2025).

Avoided emissions: coverage of the 2025 report highlights about 37 million tCO2e "avoided" by customers in 2025, and about 470,000 t avoided by Megapack. Those are avoided-emissions claims, not inventory figures. They must stay out of emissions.csv even after the inventory rows are added.

To finish this company: open the 2023 Extended Impact Report (emissions table around printed p. 147) and the 2024 Extended Version (or the 2025 report, once its PDF URL is known) in a normal browser, then add the Scope 1, Scope 2 (location and market), and Scope 3 category rows, including Category 11 as reported.

## Documents used
- Tesla, Inc. Form 10-K for fiscal year ended December 31, 2025 (filed 2026), PDF hosted on Tesla IR: https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf (SEC copy: https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm)
  - Consolidated Statements of Operations, printed p. 50: Total revenues 2025 $94,827M, 2024 $97,690M, 2023 $96,773M.
  - Note 16 "Segment Reporting and Information about Geographic Areas", printed p. 93: segment revenues and revenues by geographic area.
  - Page numbers are the printed 10-K page numbers (`p.`). I could not determine the PDF page indices.

## Availability
- Scope 1, Scope 2 location, Scope 3 total and Scope 3 by category: 2023–2025. Scope 2 market: 2024–2025.
- Emissions split: Scope 1 and location-based Scope 2 by site type, 2023–2025 (segments.csv, p. 191). segments.csv also gives 2025 revenue by reportable segment (Automotive segment $82,056M; Energy generation and storage segment $12,771M; sums to $94,827M) and by region (United States, China, Other international; sums to $94,827M).
- Boundary note: the 10-K income statement line "Total automotive revenues" ($69,526M in 2025) is not the same as the "Automotive segment" revenue ($82,056M). The segment also includes services and other revenue. segments.csv uses the segment figure. Energy generation and storage is $12,771M on both bases.

## Questions for students (once emissions are added)
1. How big is Category 11 (use of sold products) relative to Category 1? How does Tesla define the grid electricity used by its vehicles? How does that differ from "avoided emissions"?
2. How wide is the gap between market-based and location-based Scope 2? What renewable procurement explains it?
3. Did Tesla restate prior years or change Scope 3 methods between the 2023, 2024, and 2025 reports?

## Rows and validation
- emissions.csv: 57 rows; validation passed
- financials.csv: 3 rows (2023–2025)
- segments.csv: 5 rows (2 segment, 3 region; 2025, revenue)
- CSVs were written with Python's csv module. Validation passed: every row has the header's field count.
