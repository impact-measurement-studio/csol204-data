# Microsoft Corporation: starter data notes (CSOL 204 Lab 2)

Fiscal years end 30 June. Years covered: FY2022 to FY2025. FY2025 is the latest year, reported in the 2026 Fact Sheet.

## Documents used
- **2026 Environmental Data Fact Sheet** (covers FY20 to FY25). This is the source for every emissions value. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf
  - Table 1A "GHG emissions by scope (mtCO2e)" is on pdf 4. Table 3 "GHG emissions by region" is on pdf 6. The reasons categories are not relevant are in Section 1.9 "Methodologies and emission factors", pdf 18. The note on spot EACs is in Section 1.8 "Information on metrics", pdf 10.
- **2025 Environmental Data Fact Sheet** (FY20 to FY24). I used it only to find restatements, by comparing it with the 2026 values. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2025-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf
- **2026 Environmental Sustainability Report**, used for narrative context only. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Sustainability-Report-PDF.pdf
- **Form 10-K for FY2025**, the source for revenue FY2023 to FY2025 and segment revenue FY2025 and FY2024. https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm
- **Form 10-K for FY2024**, the source for FY2022 revenue and for the segment figures as originally reported. https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm

Access: the aka.ms short links on the sustainability report page are blocked (robots.txt and proxy). I opened the cdn-dynmedia PDFs directly with WebFetch. FY2025 revenue in the Fact Sheet's Table 4 ($281,724M) matches the 10-K.

## Availability (FY2022 to FY2025)

| Item | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|
| Scope 1 | y | y | y | y |
| Scope 2 location-based | y | y | y | y |
| Scope 2 market-based | y | y | y | y |
| Scope 3 total ("Subtotal emissions (Scope 3)") | y | y | y | y |
| Scope 3 by category | y | y | y | y |

- Scope 3 categories reported: 1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13.
- Categories 8, 10, 14 and 15 have no row in Table 1A. The methodology section calls each one "Not relevant", so they are status=not_relevant with the company's own reason quoted.
- Emissions split: by **region**, for Scope 1, Scope 2 location-based and Scope 2 market-based only. The regions are Asia; Europe, Middle East, Africa; Latin America; North America. There is no regional split for Scope 3, and no split by business segment.
- segments.csv holds the regional emissions for FY25 and FY24. The scope is written into split_label, for example "Scope 1: Asia". Each scope's regions add up to that scope's total.
- segments.csv also holds 10-K revenue by reportable segment for FY25 and FY24, for context.

## Restatements and method changes
- **Scope 3 was restated upward for FY22 to FY24.** Categories 1, 2, 3, 4 and 9 changed between the 2025 and 2026 Fact Sheets. For example, the FY24 Scope 3 subtotal went from 15,140,000 to 16,290,000. Footnotes give the reasons:
  - the Activision Blizzard King acquisition (Categories 1 and 2)
  - the Service-Level Accounting update (Category 1)
  - the latest supplier emission coefficients (Categories 1, 2 and 4)
  - residual emission factors (Category 3)
  - EcoTransIT (Category 4)
  - revised assumptions (Category 9)
- These rows are restated=y, and method_note gives the previously reported value. Scope 1, Scope 2 and Categories 5, 6, 7, 11, 12 and 13 did not change.
- The 2025 Fact Sheet itself had restated earlier years. It moved to an LCA-based method for some categories and, from FY24, dropped PC accessories that Microsoft no longer sells.
- **Two bases.** Table 1A follows the GHG Protocol; I used it for every row. Table 1B uses "management's criteria", which nets sustainable fuel certificates, SAFc and renewable electricity in Categories 4, 6 and 11. That gives a lower FY25 total: 20,290,000, against 21,121,000 under the GHG Protocol. The report's headline of "increased 25% year over year" matches the management's-criteria totals (about 25.1%). The GHG Protocol totals rise about 26.5%.
- Scope 3 totals are stated as market-based and rounded to the nearest thousand.
- The Fact Sheet states a recalculation policy for "significant" changes but gives no numeric threshold.
- Assurance: Deloitte did a limited review of Section 1 for FY25.

## Segment revenue recast
The FY2025 10-K shows FY2024 segment revenue under the new segment structure:

| Segment | FY2024 in FY2025 10-K (recast) | FY2024 in FY2024 10-K (original) |
|---|---|---|
| Productivity and Business Processes | 106,820 | 77,728 |
| Intelligent Cloud | 87,464 | 105,362 |
| More Personal Computing | 50,838 | 62,032 |

Total revenue (245,122) is the same either way. segments.csv uses the recast figures.

## Caveats
- **Page numbers** are PDF page positions, inferred from the page footers ("2026 Environmental Data Fact Sheet 4" means pdf 4). The table of contents numbers the pages one lower, so it lists Table 1A as p. 3. Students should check this.
- **10-K locations** are given as section headings (HTML filing), not page numbers.
- **source_quote** values are row labels plus the year column. The Fact Sheet extract shows "Fuel- and EnergyRelated" with the hyphen lost in the PDF text. I normalised it to "Fuel- and Energy-Related".

## Promising questions for students
1. **Scope 2 market-based rose more than tenfold in FY25**, from 259,090 to 2,707,428 tCO2e, while location-based rose about 21%. Microsoft says it stopped buying spot (unbundled) EACs from FY25. How much of the gap between the two methods was due to unbundled certificates? Look at North America's market-based figure (1,232) against Asia's (2,048,573).
2. **Restatements.** FY24 Scope 3 went up by 1.15 Mt between two reports. Which categories drove it, and does the restatement change the year-on-year trend?
3. **GHG Protocol vs management's criteria.** Category 11 drops from 1,540,000 to 826,000 under management's criteria, and certificates reduce Categories 4 and 6. Which basis supports the headline claims? Separately, Category 2 (capital goods, mostly datacenter build-out) grew from 4.8 Mt to 9.0 Mt between FY22 and FY25.

## Output
- emissions.csv: 76 rows. That is 4 years times (Scope 1 + Scope 2 location + Scope 2 market + 15 Scope 3 categories + Scope 3 total).
- financials.csv: 4 rows.
- segments.csv: 30 rows (24 regional emissions rows and 6 segment revenue rows).
- Validation passed. All files were written with Python's csv module, and every row has the header's field count. Category sums equal the Scope 3 subtotals, regional sums equal the scope totals, and segment revenue sums to total revenue.
