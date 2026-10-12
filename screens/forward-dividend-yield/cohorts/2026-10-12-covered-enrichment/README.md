# Eight-company sector EPS and cash-dividend enrichment

As of 2026-10-12; reference close 2026-10-08. All forward figures are analyst estimates in TWD/share. FY2026 earnings normally support 2027 payment; estimated cash dividends are not declared. This is a covered-company research supplement, not a formal screen refresh or a historical backtest.

| Company | FY2026 normalized EPS | FY2027 normalized EPS | FY2028 normalized EPS | 2027 cash DPS interval | Point | Downside | Base yield interval |
|---|---:|---:|---:|---:|---:|---:|---:|
| [3213 Crete](../../../../companies/3213-crete/model/2026-10-12-dividend-enrichment.md) | 12.07 | 13.86 | 14.53 | 7.93-9.15 | 8.54 | 6.11 | 6.42%-7.41% |
| [5515 Chien Kuo](../../../../companies/5515-chien-kuo-construction/model/2026-10-12-dividend-enrichment.md) | 3.97 | 4.13 | 4.37 | 3.55-4.72 | 4.33 | 1.81 | 6.73%-8.96% |
| [6005 Capital Securities](../../../../companies/6005-capital-securities/model/2026-10-12-dividend-enrichment.md) | 4.29 | 4.10 | 4.41 | 0.70-2.35 | 1.64 | 0.30 | 2.20%-7.33% |
| [6165 Lang](../../../../companies/6165-lang/model/2026-10-12-dividend-enrichment.md) | 3.94 | 3.94 | 4.26 | 0.71-2.88 | 1.73 | 0.00 | 1.47%-6.01% |
| [2348 Hiyes](../../../../companies/2348-hiyes/model/2026-10-12-dividend-enrichment.md) | 4.42 | 3.46 | 3.99 | 1.70-2.87 | 2.65 | 0.00 | 2.39%-4.03% |
| [2382 Quanta](../../../../companies/2382-quanta-computer/model/2026-10-12-dividend-enrichment.md) | 22.71 | 24.18 | 26.09 | 13.53-19.32 | 18.19 | 4.04 | 4.16%-5.94% |
| [2603 Evergreen Marine](../../../../companies/2603-evergreen-marine/model/2026-10-12-dividend-enrichment.md) | 36.65 | 26.48 | 26.93 | 11.27-18.33 | 17.97 | 0.00 | 4.85%-7.89% |
| [2727 Wowprime](../../../../companies/2727-wowprime/model/2026-10-12-dividend-enrichment.md) | 19.21 | 20.99 | 22.46 | 16.03-19.78 | 18.79 | 13.94 | 6.75%-8.33% |

## What is completed

All eight companies now have explicit FY2026-FY2028 operating scenarios, reported-style versus normalized EPS bridges, 2027 cash-dividend intervals/points/downside, three-year declared distribution history, retained primary parent statements and signed parent cash budgets. [Estimates CSV](estimates.csv), [calculations](calculations.json), [dividend history](dividend-history.csv) and [source register](sources.json) are reviewable. Confidence remains 35% for EPS and 30% for future cash; all future cash assumptions are Open. Accessing a parent report resolves the source-access gap, not the forecasting gap.

## Interpretation and remaining evidence

Crete, Chien Kuo, Capital Securities, Evergreen and Wowprime have a base interval that reaches 7%, satisfying the agreed range test; Quanta, Hiyes and Lang do not. None passes all three economic gates (range upper >=7%, normalized EPS / required DPS >=1.25x and downside yield >=5%). Crete narrowly misses the downside test; Chien Kuo lacks normalized EPS coverage and downside cash support; Capital Securities has capital/stock-choice constraints; Evergreen depends on remittances and retains cash in the adverse funding case; Wowprime lacks normalized EPS coverage. Passing only the range test is not full qualification. Exact unrounded calculations control boundaries.

Financial-company FCF is inapplicable, never zero. The current version-4 execution contract still requires numeric FCF; this supplemental CSV deliberately is not executable screen input. A sector cash-evidence/NA contract remains a separate integration step. No state or run manifest is marked fresh, and no market-wide refresh is executed.

Cash budgets are assumption-driven upper limits before validating legally distributable reserves. Payment timing, actual cash restrictions, subsidiary remittances, contingent guarantees and capital adequacy can invalidate them. Lang stock-distribution completeness and FY2024 exact adjusted DPS remain unverified; historical CFO classifications/parent-equity discrepancies and monthly-vs-filing revenue differences are recorded in company questions. Quanta fundraising and AUO purchase are explicitly budgeted. Do not treat these scenarios as validated 2027 dividend predictions.

## Provenance and history

The [readiness cohort](../2026-10-12-covered-expansion-readiness/README.md) remains the pre-enrichment audit at git e0bd875; do not change its hashes to match new research. The earlier pilot and its 50% evaluation coverage remain historical. Source-register references to mutable canonical model Markdown in that pilot are reconstructed from e0bd875, not current working-tree content. This cohort adds a new dated state without rewriting old runs, assumptions or quarterly snapshots.
