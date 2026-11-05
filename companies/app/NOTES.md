# APP (Asia Pulp & Paper): starter data notes

Added 5 Nov 2026 for group 11.

## Documents used
- APP Sustainability Report 2025, PT APP Purinusa Ekapersada (English): https://app.co.id/documents/20123/0/SR_PT_APP_PURINUSA_EKAPERSADA_2025_ENGLISH.pdf/adff5ea3-ee5e-ac2f-6f46-bb984e3b8b8a?t=1789224404027
  - GHG table: pdf 62–63 (printed pages match). Notes on boundaries and exclusions: pdf 63. Method changes: pdf 62. Targets: pdf 61.
  - Revenue ("Statement of Profit or Loss (Million USD)", Net Sales): pdf 24.
  - Revenue by business line (tax table, 2024 only): pdf 25.
- All APP reports, including earlier sustainability reports and CDP climate, forest and water responses: https://app.co.id/policies-and-documents

I read the PDF in a browser with pdf.js and checked the GHG and revenue tables against the rendered pages.

## Availability (calendar years 2023–2025)
| | 2025 | 2024 | 2023 |
|---|---|---|---|
| Scope 1 | yes | yes | yes |
| Scope 2 location | yes | yes | yes |
| Scope 2 market | yes | yes | yes |
| Scope 3 total | yes | yes | yes |
| Scope 3 by category | 9 of 15 | 9 of 15 | 9 of 15 |

- Categories 6 and 7 are printed "Excluded by SBTi" (3.10% of 2023 Scope 3, under SBTi's 5% threshold), so they're `not_estimated`. Categories 11, 13, 14 and 15 are "Not relevant".
- The printed Scope 3 total equals the sum of the categories in all three years.
- The printed 2025 "Total GHG (Scope 1 + Scope 2 market-based + Scope 3)" is 23,457,624 t, but the three parts sum to 23,457,426 t (198 t less). 2024 and 2023 add up. The total isn't in the CSV; the discrepancy is a small finding.
- No emissions split by mill or region. segments.csv has 2024 revenue by business line from the tax table, **including related-party revenue**, so the rows don't add to Net Sales (additive = n).

## Things to read before comparing anything
- **Entity.** The report covers PT APP Purinusa Ekapersada, APP's Indonesian holding (pulp and paper mills plus forestry companies), on an operational control basis. APP's mills in China (APP China) are a separate group and not included.
- **Biogenic emissions are large and outside the scopes.** Biogenic CO2 from burning biomass at the mills is 16.5 Mt in 2025, more than Scope 1. It's printed separately and not in the rows here.
- **Scope 3 is "Non-FLAG" only.** The notes say Scope 3 "is coming from Non-Flag Sector": emissions and removals from land use, land-use change and fibre plantations (peat, forestry) aren't in this inventory. For a pulp company that is the biggest open question.
- **Scope 2 covers fossil imported electricity only.** Most mill energy is self-generated, so it sits in Scope 1 or biogenic. Market-based treats renewable certificates as zero.
- **Method change in 2025.** Transport categories moved to a distance-based approach and DEFRA 2025 factors (pdf 62); 2023 and 2024 weren't restated, as far as the report says.
- **Targets.** SBTi-approved near-term targets (2024): Scope 1 and 2 down 54.6% and Scope 3 down 32.5% by 2033 from 2023 (pdf 61).
- **Revenue currency** is USD million; 2023 net sales were higher (8,183) than 2024 and 2025.

## Questions for students
1. Where are the land emissions? Find what APP reports on FLAG, peat and plantation emissions or removals (try the CDP forests response and the forest sections of the report), and how big they might be next to 23 Mt.
2. Biogenic emissions are 16.5 Mt and excluded from the scopes. Is that the right treatment for a mill burning wood residues, and would your answer change if the wood came from cleared natural forest?
3. Scope 1 barely moved from 2023 to 2025 while Scope 3 rose 6%. How much of the Scope 3 change is the 2025 method change?

## Rows and validation
- emissions.csv: 57 rows (3 years × Scope 1, Scope 2 location, Scope 2 market, 15 categories, Scope 3 total).
- financials.csv: 3 rows. segments.csv: 2 rows.
- `python tools/validate.py app` passes.
