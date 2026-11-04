# IKEA starter data: notes

Fiscal years end 31 August (for example, FY25 runs 1 Sep 2024 to 31 Aug 2025). IKEA has two separate reporting groups:
- **Ingka Group**: owns and runs most IKEA stores. It is a franchisee.
- **Inter IKEA Group**: the franchisor. It owns the IKEA range, supply and production.

Each group's figures are recorded under its own `reporting_entity`, and nothing was added across the two. Two kinds of row hold figures that the *company itself* printed as combined:
- `Ingka Group + Inter IKEA Group (combined as printed by Ingka; not summed by us)`
- `IKEA franchise system value chain (Inter IKEA Group climate report inventory)`

## Documents used
1. Ingka Group Annual Summary and Sustainability Report FY25: https://www.ikea.com/dk/da/files/pdf/c7/70/c7703fa5/ingkagroup_annualsummaryandsustainabilityreport_fy25.pdf
   - Scope 1 and 2 table and Scope 2 location/market table: p. 69.
   - Scope 3 by category table and "Our climate footprint" table: p. 70.
   - Reporting criteria: p. 72.
   - Value-chain table: p. 75.
   - Revenue: p. 8.
2. Inter IKEA Group Sustainability Statement FY25: https://www.inter.ikea.com/-/media/interikea/igi/financial-reports/fy25-financial-reports/inter-ikea-group-sustainability-statement-fy25.pdf?rev=e31e4c25b5754ad998ed49a8b62c340d&sc_lang=en
3. IKEA Climate Report FY24, published by Inter IKEA Group in Jan 2025. The GHG inventory is on p. 48. URL: https://www.ikea.com/global/en/images/IKEA_Climate_Report_FY_24_2025_01_27_9136cd2347.pdf
   - The URL only opened with the trailing "." shown, as indexed by search. Without the dot it returned a client error.
4. Inter IKEA Holding B.V. Annual Report FY25. Income statement p. 15; Note 17 p. 44. https://www.inter.ikea.com/-/media/interikea/igi/financial-reports/fy25-financial-reports/inter-ikea-holding-bv-annual-report-fy25-final.pdf?rev=10c81cc96c064789932e13ebf6229492&sc_lang=en
5. Inter IKEA Holding B.V. Annual Report FY23. Income statement p. 15. https://www.inter.ikea.com/-/media/interikea/igi/financial-reports/inter-ikea-holding-bv-annual-report-fy23-final.pdf?sc_lang=en
6. Ingka Group Annual Summary and Sustainability Report FY24. Consolidated income statement p. 127. https://www.ingka.com/static/ingkagroup_annualsummaryandsustainabilityreport_fy24.pdf

**Page numbers** are the printed page markers in each document's text, written `p. N`. Direct PDF download was blocked here, so they could not be checked against PDF page indices. The documents were read through WebFetch.

## Confirmed: Inter IKEA FY25 does not report GHG emissions
The Inter IKEA FY25 Sustainability Statement leaves GHG out:
- **BP-1, p. 3:** "we omitted our total GHG emissions from this sustainability statement". FY25 and FY26 emissions "will be reported in the sustainability statement FY26".
- **E1-7, E1-8 and E1-9, p. 30:** "We are not able to report on this metric."

The only climate figures in the statement are percentage targets against an FY16 base year.

The ikea.com sustainability-reporting page also says:
- FY25 climate data will not be included until the Inter IKEA FY26 Annual Report.
- The separate IKEA Sustainability and Climate reports "will be discontinued".

That means there is **no IKEA Climate Report FY25**. The latest Inter IKEA climate figures are FY24.

## Availability
| Entity | Scope 1 | S2 location | S2 market | S3 total | S3 by category |
|---|---|---|---|---|---|
| Ingka Group | FY23–FY25 | FY23–FY25 | FY23–FY25 | FY23–FY25 ("Scope 3 Ingka Group") | FY25 only. Cats 4, 11, 12 are N/A (Inter IKEA data deferred). Cats 10 and 14 are not material. |
| Inter IKEA Group | FY25 not disclosed | FY25 not disclosed | FY25 not disclosed | FY23–FY24 (as printed in Ingka report p. 70); FY25 not disclosed | none for Inter IKEA alone |
| Combined, as printed by Ingka | — | — | — | FY23–FY24 | FY23–FY24 |
| IKEA value-chain inventory (Climate Report FY24) | FY22–FY24 | FY22–FY24 | FY22–FY24 | no Scope 3 total printed (only a grand total of Scopes 1–3) | FY22–FY24, all 15 categories |

The FY16 base year is printed in the Ingka FY25 report and the Climate Report but was not loaded. FY17–FY21 from the Climate Report were also not loaded.

**Splits included in `segments.csv`:**
- Ingka Scope 1+2 (market-based) by site type or business, FY23–FY25 (p. 69). The parts add up to the printed totals.
- Ingka FY25 footprint by value-chain stage (p. 75). The parts add up to "Total scope 1, 2 and 3 (Ingka Group only)", 4,365,954, within 1 t of rounding.
- The Climate Report's sub-rows of Scope 3 category 1 (Materials, Food ingredients, Production, Retail equipment), FY23–FY24.
- Inter IKEA FY25 revenue by type and by region (Note 17).

## Revenue
- **Ingka:** the "Revenue" row.
  - FY25 41,451 and FY24 41,846 (FY25 report).
  - FY23 44,300 (FY24 report, 3-year income statement). The FY23 figure is not marked as restated.
- **Inter IKEA:** the "Total operating income" row in the Holding B.V. annual reports.
  - FY25 26,306; FY24 26,538; FY23 29,063; FY22 27,578 (EUR million).
  - Inter IKEA's web summary labels the same figures "Total revenues". The financial summary PDF uses "Total operating income" for *operating profit* (FY24 2,339), so read the labels carefully.
  - Net turnover alone is FY25 26,183 / FY24 26,596. It was not loaded.
- **Not loaded:** no revenue exists for the "value chain" entity. IKEA retail sales across the whole franchise system are not company revenue.

## Boundary quirks, restatements and method changes
**Ingka FY25 report:**
- Scope 3 categories in the FY16–FY24 columns include the **Inter IKEA supply chain**. The FY25 column is Ingka only (table footnote 2). Purchased goods (cat 1), for example, drops from 12.8 Mt to 1.18 Mt.
  - So those prior-year category rows are recorded under the combined entity, not Ingka.
  - Ingka-only categories for FY23/FY24 were **not derived** by subtraction.
- **Restated in the FY25 report:**
  - Cat 1: non-combustion factors.
  - Cat 2: now activity-based.
  - Cats 6 and 8: distance corrections, IKANO Bank added, China units removed.
  - Cat 15: investee Scope 3 added. This produced the reported +6142.8% vs FY16.
  - Ingka Investments Scope 1/2: restated upward.
- **Cat 13** excludes IKANO Bank B2B leases. The company estimates these at about 12,000 t (about 54%).
- **Renewable electricity** now counts only certificates that meet the updated RE100 criteria. This applies to the FY25 RE share now and to Scope 2 from FY26.

**IKEA Climate Report FY24 (p. 48):**
- The inventory covers the whole franchise system.
  - Scopes 1 and 2 are those of Inter IKEA-owned operations (p. 49 footnote).
  - Franchisees, including Ingka, appear inside Scope 3, for example cat 14 "Franchises" and cat 7 commuting.
- Cats 2, 8, 10, 13 and 15 are printed as 0 in every year, with no explanation. Ingka reports non-zero values for cats 2, 8, 13 and 15.
- The report says history is revised every year. Named restatements:
  - Transport (cat 4): +8% under the GLEC framework.
  - Use phase (cat 11): upstream energy added.
  - End of life (cat 12): e-waste correction.
  - Food ingredients: FY22–FY24 only.
- After the SBTi review, customer travel was moved "outside the scopes".

## Questions for students
1. **Why do the "IKEA total" figures differ between the two reports?**
   - Ingka's report gives FY24 total Scope 3 (Inter IKEA + Ingka) as 21,572,387 t. Inter IKEA's FY24 inventory gives a grand total of Scopes 1–3 of 21,321,480 t.
   - Ingka reports capital goods of 553k t, while the Climate Report shows cat 2 = 0.
   - What do these differences say about franchisor and franchisee boundaries, and about the risk of double counting or gaps if anyone tried to add the two groups together?
2. **Ingka Scope 2 gap.** Location-based Scope 2 is 703,221 t in FY25 and *rising*. Market-based is 21,460 t and falling. How much of the "93.7% Scope 2 reduction" comes from instrument choice, and what will the stricter RE100 criteria do from FY26?
3. **The FY25 gap.** About 80% of the IKEA footprint (Inter IKEA's cats 1, 4, 11 and 12) has no FY25 figure because Inter IKEA deferred GHG reporting. What can, and can't, be said about FY25 progress against the 50% reduction target for FY30?

## Rows and validation
| File | Data rows |
|---|---|
| `emissions.csv` | 119 |
| `financials.csv` | 7 |
| `segments.csv` | 34 |

All files were written with Python's csv module. Validation passed: every row has the header's field count.
