# Patagonia, Inc. — starter data notes

Fiscal year runs 1 May to 30 April (the FY25 report says "fiscal year ending April 30, 2025"). Patagonia is private, so there is no 10-K.

## Documents used
1. **FY2025 Climate Risk Report (TCFD & SB 261 Disclosure)**, published Dec 2025. https://www.patagonia.com/on/demandware.static/-/Library-Sites-PatagoniaShared/default/dwc1135e01/slots/RMA/PAT_FY25_ClimateRiskReport-122225-v2.pdf
   - The FY25 emissions table is on printed p. 9. FY25 revenue is on printed p. 2. The FY2017 base year and the targets are on p. 10.
   - The cover page is unnumbered, so printed page numbers are given ("p."). I could not confirm the PDF page numbers.
   - The same FY25 table, with the period "(May 1, 2024, to April 30, 2025)", also appears on the Patagonia Climate Goals page (e.g. https://eu.patagonia.com/cy/en/climate-goals/).
2. **Climate Goals web page, FY2023 table** on Patagonia's Australia/NZ regional site: https://www.patagonia.com.au/pages/climate-goals. The section is headed "Fiscal Year 2023 Greenhouse Gas Emissions (GHG)" and covers May 1, 2022 to April 30, 2023. The same table appears at https://www.patagonia.co.nz/pages/climate-goals.
   - The total of 200,119 MT CO2e matches Patagonia's own press release "The Climate Crisis Is Our Business" (patagoniaworks.com, 15 Sep 2023): https://www.patagoniaworks.com/press/2023/9/15/the-climate-crisis-is-our-business
   - Caveat: the AU/NZ sites are Patagonia-branded regional storefronts. The US page now shows only FY25.

## Availability
| Year | Scope 1 | S2 location | S2 market | S3 total | S3 by category |
|---|---|---|---|---|---|
| FY2025 | yes (1,335) | no | yes (93) | no printed S3 total (only all-scope total 182,646) | 4 rows: mapped to Cat 1, 4, 6, 9 |
| FY2023 | combined S1+S2 only (3,725) | no | no | no (only all-scope total 200,119) | by stage, not by GHG Protocol category: only Cat 6 (Employee Travel, 562) maps cleanly |
| FY2024 | not found | | | | |
| FY2022 and earlier | not found | | | | |

- **Category mapping was done by me, not by Patagonia.** Patagonia labels its rows by stage. I mapped them using the SBTi target wording ("purchased goods and services, upstream transportation and distribution, business travel and downstream transportation and distribution"). Each mapping is explained in method_note.
- **FY2023 values I did not sum or split:**
  - Scope 1 and Scope 2 are published only combined (3,725).
  - Transportation (13,309) is not split into upstream and downstream.
  - Raw Material Manufacturing (179,119) and Finished Goods Manufacturing (3,404) are separate rows.
  - In emissions.csv these appear as not_disclosed, with the printed figures in method_note. The full stage breakdown is in segments.csv.
- **Emissions split:** segments.csv has the published stage breakdown for FY25 and FY23 (split_type=other). In each year the rows sum exactly to the printed total: 182,646 for FY25 and 200,119 for FY23.
- **Revenue:** financials.csv has one row. Patagonia itself publishes FY25 revenue: "total FY25 revenue is $1.47 billion" (CRR p. 2; 61% US / 39% international). No company-published revenue was found for FY23.

## Couldn't find or open
- **2025 "Work in Progress" impact report PDF** (https://www.patagonia.com/media/pdf/patagonia-progress-report-2025.pdf). The CRR points to its pp. 80–83 for energy, intensity per net revenue and the detailed emissions breakdown. The fetch failed (client error), as did the pat.ag short link. It may hold FY24 or earlier years, location-based Scope 2, or restated figures. It is worth opening manually.
- **FY2024 emissions:** none found on any Patagonia page I could open.
- **FY2017 base-year value:** not published in the documents I opened.
- **Not used:** the Wayback Machine (blocked), and third-party sources (OIA progress reports, ditchcarbon, press coverage).

## Restatements, method changes, boundary
- No restatement statements were found, so restated=n everywhere.
- The FY25 inventory "has not yet gone through third party assurance" and "Inventory values are subject to change."
- **Boundary:** operational control for Scope 1/2, covering 100% of global consolidated operations (CRR p. 2). Scope 1/2 covers owned and operated stores, offices and distribution centres.
- **Row structure changed between years:**
  - FY23: Scopes 1 and 2 combined; "Transportation" as one row; raw materials and finished goods as separate rows.
  - FY25: Scope 1 and Scope 2 market-based separate; upstream and downstream transport separate; raw materials and finished goods merged into one row.

## Questions for students
1. **Scope 1+2 fell from 3,725 (FY23) to 1,428 (FY25: 1,335 + 93 market-based).** How much of the drop comes from the market-based method and renewable electricity purchases (98% renewable electricity "as of FY24")? Location-based Scope 2 is not published.
2. **Raw-material vs finished-goods split.** In FY23, finished-goods manufacturing (Tier 1) was only 3,404 t against 179,119 t for raw materials. In FY25 the two are merged into 168,667. What does this say about where emissions sit, and does merging them hide trends?
3. **Missing Scope 3 categories.** Only 4 of 15 categories appear. Categories 11–12 (use and end-of-life of sold products) and Category 2 are absent. Is that consistent with GHG Protocol completeness, and with the SBTi target boundary? The reported total fell 8.7% (200,119 to 182,646) from FY23 to FY25. Can that be compared year to year given the row changes?

## Rows written and validation
- emissions.csv: 36 rows (FY2025 18, FY2023 18)
- financials.csv: 1 row
- segments.csv: 11 rows

All files were written with Python's csv module. Validation passed: every row has the header's field count, and the segment rows sum to the printed totals.

## Review note (4 Nov 2026)

The FY25 Climate Risk Report names the reporting entity as **Patagonia Works**; these files use "Patagonia, Inc.". Check that emissions and revenue cover the same entity before calculating any intensity.
