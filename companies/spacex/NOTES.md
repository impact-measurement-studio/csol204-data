# SpaceX (company_slug: spacex) — search log, 4 Nov 2026

**Bottom line:** As of 4 Nov 2026 I found **no corporate GHG inventory published by SpaceX**: no Scope 1, Scope 2 (location or market), or Scope 3 figures for any year, no sustainability report, and no CDP response. `emissions.csv` therefore has only a header row. SpaceX became an SEC registrant in June 2026 (Nasdaq: SPCX), so audited revenue now exists. That revenue is in `financials.csv` and `segments.csv`.

## Documents used for the CSV rows
- **SpaceX Final Prospectus (Form 424B4), filed 12 Jun 2026.** https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm
  - Consolidated Statements of Operations, p. F-6, row "Revenue" (USD millions): FY2025 18,674; FY2024 14,015; FY2023 10,387. The auditor is PricewaterhouseCoopers LLP.
  - Note 3 - Revenue, p. F-23: FY2025 revenue by segment is Connectivity 11,387, AI 3,201 and Space 4,086, which sum to the total of 18,674.
  - Note 19 - Segments: FY2025 revenue by geography is USA 12,966, Ireland 1,827, Canada 764 and All Other 3,117. I read the page as F-60, but the text extraction was ambiguous, so please check it.
  - **Boundary quirk:** the financial statements are **recast to include xAI and X (Twitter)** as entities under common control, for all periods shown. The "AI" segment covers xAI and X advertising. FY2023 and FY2024 revenue is therefore **not** historical standalone SpaceX revenue. Any future SpaceX emissions figure would need the same boundary check.
- The 424B4 is a web page with no PDF page numbers. Pages are the printed F-page numbers, so students should use their browser's find function on the quoted row label.

## Search log (all searches and fetches done 4 Nov 2026)
| # | Source checked | Search terms / URL | Result |
|---|---|---|---|
| 1 | Web search | "SpaceX IPO S-1 filing SEC 2026" | News reports of an S-1 filed 19–20 May 2026, priced at $135 on 11 Jun 2026, and listed on Nasdaq as SPCX |
| 2 | SEC EDGAR submissions API | https://data.sec.gov/submissions/CIK0001181412.json | CIK 1181412 is Space Exploration Technologies Corp, ticker SPCX. Filings: DRS (30 Mar 2026), S-1 (19 May), S-1/A (29 May, 2 Jun), 424B4 (12 Jun), 10-Q Q2 (4 Aug), 10-Q Q3 (22 Oct). **No 10-K yet**; the first one, for FY2026, is expected in early 2027 |
| 3 | S-1 (19 May 2026) | .../000162828026036936/spaceexplorationtechnologi.htm | Same FY2023–25 revenue as the 424B4. I used the 424B4 because it is the final prospectus |
| 4 | 424B4, word search on the parts I read (chars 100k–300k and 1.1M–1.4M of about 1.5M) | "greenhouse", "climate", "carbon", "emissions", "Scope" | No GHG figures. Two passages mention the topic: the Risk Factors section mentions "growing concern over the potential environmental effects of emissions and other byproducts from rocket launches". The risk factor "Environmental laws, regulations, litigation, liabilities and proceedings may adversely affect our operations..." mentions "air emissions" permitting. **I did not read the whole document**, but no climate metrics section was found |
| 5 | 10-Q for the quarter ended 30 Sep 2026 (filed 22 Oct 2026) | .../000162828026066880/spcx-20260930.htm (first 100k of 370k chars) | No GHG, climate or Scope mentions in the part I read. Q3 2026 revenue was $14,575M, which includes the newly consolidated businesses. Not added to the CSVs because it is not a full year |
| 6 | spacex.com | https://www.spacex.com/sustainability, plus site search "site:spacex.com sustainability OR environment OR emissions" | The page is JavaScript-rendered and gave no content. The site search found no SpaceX sustainability or ESG page |
| 7 | CDP | https://www.cdp.net/en/responses?queries[name]=spacex, plus web search "CDP SpaceX non-responder" | The CDP page could not be fetched (client error). The web search found no CDP response by SpaceX. **Unverified:** a student should search CDP's public response page directly |
| 8 | EPA GHGRP (Envirofacts PUB_DIM_FACILITY) | facility_name containing "SPACEX", "SPACE EXPLORATION", "STARBASE", "COLOSSUS"; parent_company containing "SPACE EXPLORATION" | **No records** for any search. A control query, parent "TESLA", returned 12 records, so the search method works. A search for "XAI" matched unrelated names such as PRAXAIR and is inconclusive. The xAI Memphis sites were not checked under other possible names |
| 9 | FAA environmental reviews | see the proxy list below | Facility- and programme-level GHG **estimates prepared under NEPA**. These are not SpaceX corporate disclosures |
| 10 | News | cryptobriefing.com "OpenAI, Anthropic, and SpaceX head toward IPOs with almost no emissions data on the table" | Found by search but the page failed to load. The headline is consistent with what I found |

## Availability
- Scope 1, Scope 2 location, Scope 2 market, Scope 3 total, Scope 3 by category: **none, for any year**.
- Emissions split by segment, region or site: none. Revenue by segment and region (FY2025) is included instead.

## External proxy sources (NOT SpaceX-reported; label them as such in any analysis)
These are U.S. government NEPA estimates for parts of SpaceX's operations, mainly Starship at named sites. They cover expected emissions at a permitted launch rate, not measured company inventories. They mostly cover direct combustion and venting at the site, and leave out Falcon, Starlink, facilities, purchased electricity and xAI.
1. **FAA, Final Programmatic EA for SpaceX Starship/Super Heavy at the Boca Chica Launch Site (June 2022).** https://www.faa.gov/sites/faa.gov/files/2022-06/PEA_for_SpaceX_Starship_Super_Heavy_at_Boca_Chica_FINAL.pdf. Section 3.4 Climate, **Table 3-3 "Estimated Carbon Dioxide Equivalent Emissions Comparison"**, printed pp. 53–54. "Starship/Super Heavy Operations Annual Total" is **43,892 metric tons CO2e/yr**, assuming 5 orbital launches per year. Methane venting accounts for 23,000 t of that.
2. **FAA, Final Tiered EA for Starship/Super Heavy Increased Cadence at Boca Chica (April 2025).** https://www.faa.gov/media/94346. Section 3.2.2 Climate, **Table 4 "Proposed Action GHG Emission Rates Compared to 2022 PEA"**: total **97,342 t CO2e/yr** for up to 25 launches per year, of which launches are 58,450 and methane venting 35,051. Table 5 compares this with Texas, U.S. and world totals. The extraction gave pp. 22–23; check whether these are PDF or printed pages.
3. **FAA, Final EIS for Starship/Super Heavy at KSC Launch Complex 39A (Jan 2026).** https://www.faa.gov/space/stakeholder_engagement/spacex_starship_ksc/SpaceX-SSH-LC-39A-Final-EIS-Volume-I.pdf. Climate is in **Section 3.12**, and the air-quality inputs are in Volume II Appendix C2 (listed at https://www.faa.gov/space/stakeholder_engagement/spacex_starship_ksc). I did not extract figures; the Executive Summary, p. ES-28, lists climate as having no substantive or significant effects.
4. **Found but not opened:** the Starship EIS at Cape Canaveral SLC-37 (https://www.faa.gov/space/stakeholder_engagement/spacex_starship_ccsfs) and the FAA Final EA/FONSI for the SpaceX Falcon Program (https://www.patrick.spaceforce.mil/Portals/14/FAA%20Final%20EA%20and%20FONSI%20for%20SpaceX_Falcon_Program.pdf). Verify these before use.
5. **EPA GHGRP FLIGHT** (https://ghgdata.epa.gov/ghgp/): currently no SpaceX-named facility. A useful exercise is explaining why. The 25,000 tCO2e/yr facility threshold and source-category coverage are a likely reason; the Starbase estimates above are above the threshold, but rocket launches are not a GHGRP source category.

## Questions for students
1. With no inventory, how would you build a screening-level Scope 1 estimate from the FAA tables? What is left out: Falcon, Starlink manufacturing, purchased electricity, xAI data centres? Is methane venting Scope 1?
2. How does the xAI/X recast change the meaning of "SpaceX" as a reporting boundary, and of revenue-based intensity, in FY2023–25?
3. As a newly listed U.S. company with large operations in California, would SpaceX fall under California SB 253 Scope 1/2 reporting, which begins in 2026? What would change if it did?

## Files and validation
- emissions.csv: header only, 0 data rows (no SpaceX-published GHG figures).
- financials.csv: 3 rows (FY2023–FY2025 revenue).
- segments.csv: 7 rows (FY2025 revenue: 3 by segment, 4 by region; each set adds up to $18,674M).
- Written with Python's csv module. Validation passed: every row has the same number of fields as the header.
