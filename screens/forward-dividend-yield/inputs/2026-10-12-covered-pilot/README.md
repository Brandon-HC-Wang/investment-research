# Covered-company dividend pilot — 2026-10-12

## Scope and interpretation

This is an explicitly requested exploratory run for four covered companies: Crete (3213, rugged computers/channels), Chien Kuo (5515, construction projects), Capital Securities (6005, brokerage/trading/financing and associate asset management), and Lang (6165, live/social platforms). Existing company theses and annual EPS forecasts remain authoritative; this worksheet derives conservative screen scenarios rather than replacing those models.

Execution and information cutoff: **2026-10-12**. Common verified completed-session price: **2026-10-08**. Forecast period: **FY2026E**, with estimated cash distributions in **2027**. The CLI `--as-of 2026-10-08` represents the price date only. This uses information accessed through 2026-10-12 and is **not an 2026-10-08 point-in-time backtest**. Financial observations are through 2026 H1 except Capital Securities' September self-profit anchor in its existing model. No full-market collection or complete post-coverage company refresh is claimed.

The owner's authorization covers the pilot and the sector/history methodology. The new cash assumptions are analyst-prepared, conditional estimates; the owner has not separately approved their numeric values. The two computable rows exercise the arithmetic with warning flags and still require human analytical review. Their consolidated cash proxies do not verify parent-only distributable cash. This run cannot establish production eligibility, a completed analytical pipeline, or strategy efficacy.

## Result

Run: [2026-10-12-covered-pilot-v1](../../runs/2026-10-12-covered-pilot-v1/summary.md). Status **partial**: 4 supplied companies, 2 numerically evaluated, 0 retained among those 2, **50.00%** input coverage. This falls below the unchanged **95%** completeness requirement. Two rows are unevaluated; zero retained rows is not a finding of zero qualifying companies across the four-company sample or the market. Refresh state must not advance.

| Ticker | Price TWD | Normalized diluted EPS base/downside | Estimated 2027 cash DPS base/downside | Forward yield base/downside | EPS / required DPS | Outcome |
|---|---:|---:|---:|---:|---:|---|
| 3213 | 123.50 | 12.07 / 9.30 | 6.00 / 2.65 | 4.86% / 2.15% | 1.40× | Both cash-yield thresholds fail under conditional estimates |
| 5515 | 52.70 | 3.77 / 2.78 | 2.05 / 1.40 | 3.89% / 2.66% | 1.02× | Both cash-yield thresholds and EPS coverage fail |
| 6005 | 32.05 | Not admitted | Not admitted | Not assessed | Not assessed | Mandatory industrial FCF field is inapplicable |
| 6165 | 47.90 | Not admitted | Not admitted | Not assessed | Not assessed | Forward cash capacity/DPS not adequately supported |

Thresholds: base cash yield **7%**, downside cash yield **5%**, normalized diluted EPS divided by required DPS **1.25×**. Required DPS is price × 7%; it is not estimated actual DPS. [Exact input](input.csv), [calculations](calculations.json), [row diagnostics](diagnostics.csv), [three-year dividend history](dividend-history.csv), [source register and SHA-256](sources.json), [input checksum](checksums.json).

## Dividend history and earnings quality

Raw historical DPS below is associated with the earnings year; the corresponding ordinary distribution years are **2024 / 2025 / 2026**. These are declared historical dividends, separate from estimated FY2026 distributions in 2027. DPS is TWD/share; monetary totals and shares are TWD million/million unless stated.

| Company | FY2023 cash DPS | FY2024 cash DPS | FY2025 cash DPS | Material qualification |
|---|---:|---:|---:|---|
| Crete | 5.40 | 6.00 | 7.00 | Cash payout/basic EPS: 68.79% / 71.09% / 94.59%; stock DPS 0 / 0 / 0 |
| Chien Kuo | 1.00 | 2.15 | 3.30 | Use total cash/parent earnings across the 2024 share reduction: 74.44% / 63.58% / 73.62%; separate capital refund 504.000 in cash-flow FY2024 |
| Capital Securities | 1.33 | 1.50 | 0.40 | Cash payout on original historical EPS: 70.00% / 66.67% / 15.15%; FY2025 stock DPS 1.31 adds 13.1% shares and is not cash |
| Lang | 0.40 | 0.60 (rounded filing value) | 5.00 | FY2024 exact ex-dividend DPS not reconciled; FY2025 total cash 367.928 exceeds parent earnings 308.271; stock-distribution completeness remains unverified |

History guides the cash-allocation assumptions; it is not a mechanical average-DPS forecast. Capital reduction and stock dividends cannot be counted as recurring cash income. Lang's rounded 0.60 is retained exactly as printed in the audited note, without substituting an unverified adjusted value.

## 3213

Business/earnings basis: rugged-system demand and channel sales drive recurring profit. Preserve normal operating costs; exclude small H1 fund FVTPL and FX gains for a neutral normalized screen sensitivity. The [existing model](../../../../companies/3213-crete/04_eps_model.md) gives FY2026 diluted base/downside **12.14828882595 / 9.3808437521**. At an assumed **25%** marginal tax, subtract `(2.962 + 3.275) × 75% / 59.316 = 0.07886152134` EPS. This gives **12.06942730461 / 9.30198223076**. The downside model already includes H2 FX losses; do not remove them a second time. Future MilDef disposal proceeds are excluded from recurring earnings/cash projections here.

Historical conventional FCF is operating cash flow less cash PPE (including prepayments) and intangibles, before lease principal: **24.131 / 481.375 / 602.504** for cash-flow FY2023/FY2024/FY2025. Ordinary cash dividends paid in those same cash-flow years are **211.268 / 316.902 / 352.113**. Three-year sum coverage is **1.25869748706×**. These payment-year totals deliberately differ from the earnings-year DPS table. A historical ratio is a review diagnostic, not evidence of FY2026 conversion.

**Conditional cash scenario:** disclosed H1 group liquidity **1,823.151**, less leases **72.262**, declared dividends payable **410.799**, current tax **196.264**, and an analyst working-capital reserve **1,000.000** leaves **143.826**. The reserve is an estimate already discussed in company valuation, not a disclosed cash restriction. Assume incremental H2 FCF equals half the three-year median annual FCF (**481.375 / 2**) in base, or half the lowest annual FCF (**24.131 / 2**) in downside. These are explicit cash-recovery hypotheses despite H1 CFO **-373.577**, not mechanical earnings annualization or reported H2 cash.

Cash ceilings are `(143.826 + 481.375 / 2) / 58.685 = 6.55215983641` in base and `(143.826 + 24.131 / 2) / 58.685 = 2.65641134873` in downside. Base DPS is the lower of **50%** normalized basic EPS, historical median ordinary DPS **6.00**, and the base ceiling: **6.00**. Downside DPS is the lower of **40%** normalized basic EPS and the downside ceiling, rounded down: **2.65**. Convert diluted EPS to basic earnings capacity using **59.316 / 58.685** shares; do not use diluted shares for the cash payout denominator.

**P-3213-CASH — Open, confidence 30%, expected verification FY2026 statements / 2027 proposal.** Claim: working-capital conversion plus retained liquidity can support the scenario cash distribution after existing commitments. Supporting evidence: historical positive FCF and disclosed liquidity. Contradiction: negative H1 CFO, inventory/advances, and unverified parent-only liquidity. Confirm with H2 collections, parent cash/remittance availability and board cash allocation; reject if inventory/receivables absorb the reserve or parent restrictions reduce cash capacity. This proxy supports exploratory arithmetic only; parent distributable reserves, subsidiary transfers and actual cash-generation timing remain required before production admission.

## 5515

Business/earnings basis: construction backlog, recognition and collections drive recurring income. Use the lower endpoints of the [existing normalized basic EPS ranges](../../../../companies/5515-chien-kuo-construction/04_eps_model.md): **3.8 / 2.8**, with FVTPL, disposal and compensation gains already excluded. Convert to diluted using disclosed H1 weighted shares **201.600 / 203.161**: **3.77080246701 / 2.77848602832**. These are full-year assumptions using the latest verified diluted-share proxy, not company guidance.

Conventional FCF uses the same pre-lease definition: CFO less PPE, intangibles and equipment prepayments. FY2023: `1,564.574 - 10.620 - 1.258 - 6.296 = 1,546.400`; FY2024: `516.202 - 94.961 - 6.020 - 1.781 = 413.440`; FY2025: `2,653.424 - 7.891 - 5.452 - 1.545 = 2,638.536`. Ordinary cash paid in those cash-flow years is **252.000 / 252.000 / 433.440**, excluding the separate **504.000** capital refund. Sum coverage is **4.90524833589×**. Customer advances can temporarily inflate CFO; this is not an unrestricted parent cash measure. Lease/ROU cash and future project guarantees require additional review rather than being called free cash for distribution.

**Conditional cash scenario:** do not treat the FVTPL portfolio or all client advances as distributable cash. Assume full-year available ordinary cash generation is capped at the lowest positive annual FCF in the three-year history: **413.440**, or **2.05079365079** per current **201.600** million issued shares; downside reduces that proxy **20%**. Base payout **60%** is below each of the three historical total-cash/parent-profit ratios; downside uses **50%**. Base DPS `min(3.8 × 60%, 413.440 / 201.600)` rounds down to **2.05**; downside `min(2.8 × 50%, 2.05079365079 × 80%) = 1.40`. This is an analyst cap, not verified FY2026 parent cash or a forecast of client advances. Existing H1 dividend payable is not counted again as available cash.

**P-5515-CASH — Open, confidence 30%, expected verification FY2026 statements / 2027 proposal.** Claim: project collections net of funding, lease/capex and reserve requirements support at least the conditional cash-generation envelope. Supporting evidence: three years of positive disclosed CFO/FCF. Contradiction: advance-funded CFO, guarantees, and unverified parent excess liquidity. Confirm using parent cash, reserve restrictions, contract collection schedules and funding requirements; reject if advances reverse, collections delay or guarantees require cash retention. Parent-only cash and guarantee/funding review remain gates before production admission.

## 6005

The brokerage model retains operating trading FVTPL with economically related hedge legs. Selected noncore disposal/liability-release sensitivity subtracts `(1,178.667 + 43.295) × 80% / 2,459.319 = 0.39749605480` from existing FY2026 diluted **4.69 / 3.69**. CSV cash assumptions **1.64 / 0.55** are the existing allocation scenarios, not newly approved dividends. The row is not admitted: mandatory `fcf_dividend_coverage_x` has no economically valid industrial-company value for a brokerage and is deliberately blank. Capital adequacy, financing liquidity, required reserves and parent cash/stock budgeting must be modeled directly; neither a made-up zero nor capital ratio relabeled as FCF is acceptable. Resolve a sector-aware input contract without changing historical runs. [Existing cash-allocation question Q-2026-004](../../../../companies/6005-capital-securities/07_open_questions.md).

## 6165

Platform operating growth does not make the declared **5.00** cash DPS a repeatable forward estimate. FY2025 CFO **264.550** was below cash payout **367.928** even before PPE **688.951**. H1 cash **837.010**, bank debt **820.000**, leases **9.051** and dividend payable **367.928** do not establish a funded future distribution. Preserve the existing normalized-EPS scenarios in the company model, but leave mandatory forward EPS/DPS/FCF cells unadmitted here pending a coherent parent-cash and tax/share-count bridge; blanks are missing inputs, not zero forecasts. Resolve debt refinancing, ordinary versus non-earnings payout, capex, parent distributable reserves and exact dividend/share adjustments. [Existing questions](../../../../companies/6165-lang/07_open_questions.md).

## Next run and retained evidence

Do not lower thresholds or the 95% coverage gate to manufacture success. Complete parent-cash checks for the conditional rows, then support Lang's forward cash model and decide how a sector-specific financial cash/capital field will be represented. Obtain human analytical review of those concrete inputs before production use; append a new run with a new ID. Keep this incomplete exploratory run unchanged.

The [source register](sources.json) records publisher, title, publication/data date, access date, section and SHA-256 for primary artifacts and canonical model inputs. Dates not independently captured are explicitly unknown. Price JSON, Crete's dividend table and newly needed FY2024 filing are retained here; other filings remain in company source categories with recorded hashes. Exact URL for the retained Chien Kuo H1 document was not recaptured; the audited/reviewed local artifact is linked rather than an invented URL. This is a manually enriched pilot, not an automated filing-retrieval pipeline.
