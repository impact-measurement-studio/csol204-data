# Deere & Company (john-deere): starter-data notes

## Documents used
- Deere & Company, *2025 Sustainability Disclosures and Metrics Report* (FY2025, 88 pp.). https://s22.q4cdn.com/253594569/files/doc_financials/2025/ar/2025-Sustainability-Disclosures-and-Metrics-Report-2.pdf. Sources: E1-8 "Greenhouse Gas Emissions Overview" table (pdf 36, "Page 36 of 88"), Scope 2 text (pdf 37), Appendix 4 "Statement of Greenhouse Gas Emissions" (pdf 82–84).
- Deere & Company Form 10-K, FY ended 2 Nov 2025. https://www.sec.gov/Archives/edgar/data/315189/000110465925122321/de-20251102x10k.htm (Statements of Consolidated Income; Note 27 Segment Data).
- Deere & Company Form 10-K, FY ended 31 Oct 2021. https://www.sec.gov/Archives/edgar/data/315189/000155837021016864/de-20211031x10k.htm (Statement of Consolidated Income).
- Checked but contains no absolute tonnes: *2024 Business Impact Report*, https://www.deere.com/assets/pdfs/common/our-company/sustainability/business-impact-report-2024.pdf. It gives only % progress: Scope 1+2 down 28%, Scope 3 Cat 1+11 down 19% vs 2021 (p. 35).

## Not opened: 2024 Data Book
https://www.deere.com/assets/pdfs/common/our-company/sustainability/data-book-2024.pdf now returns a 302 redirect to the investor sustainability-reports page. That page loads its list dynamically, so I could not find a new link. The Wayback Machine is blocked here. Because of this, **FY2022–FY2024 absolute values are missing**. To fill them, download the Data Book by hand from investor.deere.com and add those rows.

## Availability
| Year | Scope 1 | S2 location | S2 market | S3 by category | S3 total |
|---|---|---|---|---|---|
| FY2025 (ends 2025-11-02) | yes | yes | yes | Cat 1 and 11 only; others marked not_relevant | no |
| FY2021 base year (ends 2021-10-31) | yes | not printed | yes | Cat 1 and 11 only | no |

- The FY2021 numbers are base-year context printed in the FY2025 report. They were not covered by Deloitte's limited assurance. The report says it has no other prior-year comparators (BP-1). It also says historical figures in earlier reports "may reflect different scopes or methodologies." No restatement is disclosed: GRI 2-4 reads "Reported (no restatements)," and restated=n is set on that basis. I could not compare against earlier reports.
- **Scope 3 total:** none printed. The row "Scope 3 (Target Boundary)" / "Scope 3 (Category 1 and 11)" is a subtotal of Categories 1 and 11 (75,081,000 FY2025; 101,262,000 FY2021), so I did not write a total row.
- **Other Scope 3 categories:** the report says Categories 1 and 11 are "the only Scope 3 categories exceeding Deere's quantitative relevance threshold" (from the 2021 screening; the E1-8 text gives the threshold as 5%). Appendix 4 lists all other categories as exclusions (pdf 84). For FY2025 these are coded not_relevant. For FY2021 they are not_disclosed.
- **Emissions split:** none found. segments.csv therefore holds FY2025 revenue by reportable segment from Note 27. The rows are total segment net sales and revenues, which include intersegment amounts: PPA 17,753; SAT 10,432; C&F 11,642; FS 6,289. Two reconciling lines follow: corporate other income 310 and intersegment elimination −742. All rows sum to the consolidated 45,684 ($M).

## Quirks and uncertainties
- Boundary: operational control. The report notes this differs from the ESRS financial-control boundary. Entities acquired in FY2025 are excluded. About 5,000 tCO2 of biogenic CO2 is tracked internally but not reported.
- Fiscal years end on the Sunday nearest 31 Oct: FY2025 ended 2 Nov 2025 and FY2021 ended 31 Oct 2021. Appendix 5 describes the reporting period as "Oct. 2024–Nov. 2025."
- Page numbers come from the "Page N of 88" markers in the extracted text, recorded as pdf N. The 10-K is HTML, so its source_page holds the statement or note heading. The labels on the two reconciling lines in Note 27 ("External other income", "Elimination of intersegment revenues") may come from XBRL tags rather than the printed table, so check them against the filing.
- The values were read through a text-extraction tool, not from the rendered PDF. Spot-check pdf 36 and pdf 82.

## Questions for students
1. In FY2025, location-based Scope 2 is 515,300 t and market-based is 154,500 t, a gap of about 3.3×. What instruments (RECs, supplier-specific factors) drive the gap? Would the −62% Scope 2 progress hold up on a location basis?
2. Category 11 (use of sold products) is about 93% of the inventory. It is modelled from internal lifetime and usage assumptions. How sensitive is the −25% to those assumptions and to lower FY2025 sales volumes? Revenue fell from about $61.3B in FY2023 to $45.7B in FY2025.
3. Only Categories 1 and 11 are reported, based on a 2021 screening that has not been redone. Which excluded categories might now pass 5%, for example Cat 4 transport or Cat 12 end-of-life? And why might the Category 1 spend-based figure fall partly because spending fell?

## Rows written
emissions.csv 36, financials.csv 2, segments.csv 6. The csv-module validation passed: every row has the same number of fields as its header, and the segments sum to the consolidated total.
