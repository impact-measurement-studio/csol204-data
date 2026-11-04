# csol204-data

Shared, growing data set of company greenhouse-gas disclosures for CSOL 204 (Carbon Accounting & Lifecycle Analysis, UC Berkeley Master of Climate Solutions). Every number carries its document, URL, page and a short quote so anyone can check it.

| File | What it is |
|---|---|
| `companies/<slug>/emissions.csv` | Scope 1, Scope 2 (location and market, separate rows), Scope 3 by category and total |
| `companies/<slug>/financials.csv` | Revenue for the same periods |
| `companies/<slug>/segments.csv` | Splits by segment, region or business line (emissions where reported; otherwise revenue as context) |
| `companies/<slug>/NOTES.md` | Documents used, gaps, quirks, questions worth investigating |
| [`SCHEMA.md`](SCHEMA.md) | Column definitions and the five rules |
| [`AVAILABILITY.md`](AVAILABILITY.md) | What each company reports, by year |
| [`SOURCES.md`](SOURCES.md) | Every document cited |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add data by pull request |

**Status (4 Nov 2026):** starter data was compiled with AI assistance from company documents. Treat every value as something to verify against its page. Spot-checked against the source PDF (3 values each, Scope 1, market-based Scope 2, Scope 3): Amazon, John Deere, Microsoft (the FY2025 Scope 3 total appears on pdf 3, not pdf 4 as cited), Tesla (all values). Not yet spot-checked: IKEA, Nestlé, NVIDIA, Patagonia, PepsiCo, Rivian. Known gaps: John Deere FY2022–FY2024, Patagonia FY2024 and earlier, Tesla 2022 and earlier, SpaceX (no public inventory located).

Check the data: `python tools/validate.py`
