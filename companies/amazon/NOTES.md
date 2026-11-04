# Amazon.com, Inc. — starter data notes

## Documents used
- Amazon 2025 Sustainability Report (covers 1 Jan to 31 Dec 2025): https://sustainability.aboutamazon.com/2025-amazon-sustainability-report.pdf. "Amazon's 2019–2025 Carbon Footprint" is on printed p. 46. The methodology and assurance notes are on p. 47, and the carbon-intensity endnote 5 is on p. 50. I could not find the PDF page numbers (the text extraction only shows printed page markers), so pages are given as `p.`.
- Amazon 2024 Sustainability Report: https://sustainability.aboutamazon.com/2024-amazon-sustainability-report.pdf. I used it only to check which values were restated. Its footprint table is on p. 50.
- Carbon Methodology web page (Amazon Sustainability, July 2026): https://sustainability.aboutamazon.com/carbon-methodology
- 2025 Sustainability Reporting Framework Summary (GRI index): https://sustainability.aboutamazon.com/2025-sustainability-reporting-framework-summary.pdf. It contains no emissions figures.
- EY Scope 1 and 2 assurance statements, hosted by Amazon, with the location-based figure in a footnote. Years and URLs:
  - FY2025: https://sustainability.aboutamazon.com/2025-ghg-assurance-scope-1-2.pdf (dated 21 May 2026)
  - FY2024: https://sustainability.aboutamazon.com/2024-ghg-verification-scope-1-2.pdf (15 May 2025)
  - FY2023: https://sustainability.aboutamazon.com/2023-ghg-verification-scope-1-2.pdf (24 Jun 2024)
  - FY2022: https://sustainability.aboutamazon.com/2022-ghg-verification-scope-1-2.pdf (14 Jul 2023)
- Form 10-K for FY2025: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm. Source of revenue for 2023–2025 and of Note 10 segment net sales.
- Form 10-K for FY2024: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm. Source of 2022 revenue.

## Availability (calendar years 2022–2025)
- **Scope 1:** 2022–2025, from the report.
- **Scope 2 market-based:** 2022–2025, from the report. Amazon's row "Emissions from Purchased Electricity (Scope 2)" uses the market-based method, according to the Carbon Methodology.
- **Scope 2 location-based:** 2022–2025. It does not appear in the sustainability report or the Carbon Methodology. It appears only in a footnote of each year's EY assurance statement: 21.82 / 17.76 / 15.67 / 12.77 MMT for 2025 / 2024 / 2023 / 2022.
- **Scope 3 total:** 2022–2025. Amazon prints it as "Emissions from Indirect Sources (Scope 3)".
- **Scope 3 by category:** 2022–2025, for categories 1, 2, 3, 4, 6, 7, 9, 11 and 12.
  - Categories 5, 8, 10, 13, 14 and 15 are not in the table. The methodology gives no relevance statement for them, so they are recorded as `not_disclosed`.
  - The category names in the table are the GHG Protocol names. The EAC footnote also refers to "Scope 3.1, 3.3, 3.4" by number, so the category mapping comes from Amazon itself.
  - The category sub-rows print only four values. I assigned them to 2022–2025 because each year's column sums exactly to that year's Scope 3 total, and the YoY% column matches the change from 2024 to 2025.
- **Emissions split:** none. The report has no footprint table by segment, region or business line. segments.csv therefore holds 2025 segment revenue: North America, International and AWS. These add exactly to the total of $716,924M.
- **Not loaded:** the Scope 1 sub-rows (Fossil Fuels and Refrigerants), the total "Amazon's Carbon Footprint" (80.85 / 69.55 / 65.28 / 65.37 MMT), and carbon intensity. All three are on p. 46 if they are needed.

## Restatements, method changes and quirks
- The p. 47 note says "2022-2025 carbon footprints calculated in accordance with updated Carbon Methodology".
  - Compared with the 2024 report, categories 1 and 2 changed for 2022–2024, and so did the Scope 3 totals (2024: 50.32 → 51.62; 2023: 47.40 → 48.30; 2022: 49.02 → 49.29). Those rows are flagged restated=y.
- The Scope 1 and market-based Scope 2 figures for 2022 and 2023 differ from the values EY originally assured in those years. For example, 2022 Scope 1 was 13.40 in the 2022 statement and is now 13.02. These rows are restated=y.
- The location-based figures for 2022 and 2023 were never republished. They may still be on the pre-recalculation basis.
- Environmental Attribute Certificates (EACs) are applied in Scope 1 and in Scope 3 categories 1, 3 and 4, with a net effect of −199.4K t in 2025.
  - As a result, the 2025 Scope 1 in the report (15.37) is lower than the EY-assured 15.41, which is before the sustainable aviation fuel (SAFc) and renewable diesel (RD) certificates.
  - Fossil fuels are 15.00 in the report and 15.04 in the EY statement.
- The boundary is operational control. The Carbon Methodology's boundary also lists "customers' trips to Amazon's physical stores", but it does not say which category these fall in.
- Carbon intensity is now reported per $ of revenue (endnote 5) instead of per $ of gross merchandise sales, and figures for all years were updated. The report's 112.8 g/$ for 2025 matches 80.85 MMT ÷ $716.9B.
- 10-K page numbers were not visible in the HTML, so source_page gives the section names instead.

## Questions for students
1. In 2025, location-based Scope 2 (21.82 MMT) is almost 6 times the market-based figure Amazon reports (3.74 MMT). Why does the location-based number appear only in an auditor's footnote? How would the 2025 total change if it were used instead?
2. Six Scope 3 categories are absent and get no relevance statement: 5, 8, 10, 13, 14 and 15. Category 15 (investments) and categories 13 and 14 (leased assets and franchises) are the obvious ones to probe. Also, emissions from third-party seller products are not visible in category 1, which covers "Amazon-branded products" only.
3. Capital goods rose 43% and Scope 2 rose 34% in 2025, while revenue grew about 12%. How much of this is the data-centre and AI build-out, and how much is the methodology recalculation?

## Rows and validation
- emissions.csv: 76 rows. For each of 4 years: Scope 1, Scope 2 market, Scope 2 location, 15 Scope 3 categories and a Scope 3 total.
- financials.csv: 4 rows.
- segments.csv: 3 rows.
- All files were written with Python's csv module. Every row has the same number of fields as the header (validation passed).
