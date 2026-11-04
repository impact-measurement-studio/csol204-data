# Tesla, Inc. starter data: notes

## Status: emissions NOT collected (documents could not be opened)

None of Tesla's Impact Report PDFs could be opened from this environment, so `emissions.csv` holds the header only (0 rows). No emissions value was estimated or copied from a secondary source.

What was tried (4 Nov 2026):
- https://www.tesla.com/impact: opens, but it is a JavaScript page. The fetched text only mentions "Read our 2025 Impact Report." (meta description) and lists an archive for 2020–2024. No 2025 PDF link and no emissions data appear in the retrievable text.
- Archive PDFs listed on that page all failed with a site-side client error (likely bot blocking):
  - https://www.tesla.com/ns_videos/2024-extended-version-tesla-impact-report.pdf
  - https://www.tesla.com/ns_videos/2024-tesla-impact-report-highlights.pdf
  - https://www.tesla.com/ns_videos/2023-tesla-impact-report.pdf (the brief's emissions table "around p. 147")
  - the same paths on tesla.com (no www) and www.tesla.cn: also failed
- Guessed 2025 PDF paths (`2025-tesla-impact-report.pdf`, `2025-extended-version-tesla-impact-report.pdf`, `2025-tesla-impact-report-highlights.pdf`): failed. I could not confirm a real 2025 PDF URL. News coverage (notateslaapp.com, evwire.com, teslanorth.com) links only to tesla.com/impact. evwire mentions a third-party Scribd copy, which I did not use.
- web.archive.org copy: blocked. Bash/curl to www.tesla.com: refused by the egress proxy (403 CONNECT).
- Third-party mirrors (manuals.plus, sustainabilityreports.com, driveteslacanada.ca) were not used, because the brief allows company-published sources only and students need to be able to check numbers against Tesla's own page.

Avoided emissions: coverage of the 2025 report highlights about 37 million tCO2e "avoided" by customers in 2025, and about 470,000 t avoided by Megapack. Those are avoided-emissions claims, not inventory figures. They must stay out of emissions.csv even after the inventory rows are added.

To finish this company: open the 2023 Extended Impact Report (emissions table around printed p. 147) and the 2024 Extended Version (or the 2025 report, once its PDF URL is known) in a normal browser, then add the Scope 1, Scope 2 (location and market), and Scope 3 category rows, including Category 11 as reported.

## Documents used
- Tesla, Inc. Form 10-K for fiscal year ended December 31, 2025 (filed 2026), PDF hosted on Tesla IR: https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf (SEC copy: https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm)
  - Consolidated Statements of Operations, printed p. 50: Total revenues 2025 $94,827M, 2024 $97,690M, 2023 $96,773M.
  - Note 16 "Segment Reporting and Information about Geographic Areas", printed p. 93: segment revenues and revenues by geographic area.
  - Page numbers are the printed 10-K page numbers (`p.`). I could not determine the PDF page indices.

## Availability
- Scope 1, Scope 2 location, Scope 2 market, Scope 3 total, Scope 3 by category: not collected for any year (see above). From Tesla's disclosure history, the Extended Impact Reports are expected to contain these. This is unverified here.
- Emissions split: unknown. As a fallback, segments.csv gives 2025 revenue by reportable segment (Automotive segment $82,056M; Energy generation and storage segment $12,771M; sums to $94,827M) and by region (United States, China, Other international; sums to $94,827M).
- Boundary note: the 10-K income statement line "Total automotive revenues" ($69,526M in 2025) is not the same as the "Automotive segment" revenue ($82,056M). The segment also includes services and other revenue. segments.csv uses the segment figure. Energy generation and storage is $12,771M on both bases.

## Questions for students (once emissions are added)
1. How big is Category 11 (use of sold products) relative to Category 1? How does Tesla define the grid electricity used by its vehicles? How does that differ from "avoided emissions"?
2. How wide is the gap between market-based and location-based Scope 2? What renewable procurement explains it?
3. Did Tesla restate prior years or change Scope 3 methods between the 2023, 2024, and 2025 reports?

## Rows and validation
- emissions.csv: 0 data rows (header only)
- financials.csv: 3 rows (2023–2025)
- segments.csv: 5 rows (2 segment, 3 region; 2025, revenue)
- CSVs were written with Python's csv module. Validation passed: every row has the header's field count.
