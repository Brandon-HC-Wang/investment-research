# EPS scenarios

Model date 2026-09-24. Amounts TWD million; shares million; EPS TWD/share. Analyst estimates, not management forecasts or verified consensus. [Inputs and full-precision outputs](scenario-inputs.json); actuals from [financials](02_financials.md). Forecast confidence is medium for 2026, low-to-medium for 2027 and low for 2028.

## Outputs

| Year / 年 | Case / 情境 | Revenue / 營收 | Rugged / 強固 | Commercial / 商用 | Other / 其他 | Diluted EPS / 稀釋 | Basic EPS / 基本 |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026 | downside | 3,480 | 2,000 | 1,400 | 80 | 9.38 | 9.48 |
| 2026 | base | 3,800 | 2,250 | 1,465 | 85 | 12.15 | 12.28 |
| 2026 | upside | 4,100 | 2,500 | 1,510 | 90 | 14.26 | 14.41 |
| 2027 | downside | 3,480 | 2,000 | 1,400 | 80 | 8.01 | 8.10 |
| 2027 | base | 4,300 | 2,700 | 1,510 | 90 | 13.86 | 14.01 |
| 2027 | upside | 4,900 | 3,250 | 1,560 | 90 | 17.62 | 17.81 |
| 2028 | downside | 3,400 | 1,930 | 1,390 | 80 | 7.23 | 7.31 |
| 2028 | base | 4,620 | 2,970 | 1,555 | 95 | 14.53 | 14.69 |
| 2028 | upside | 5,500 | 3,800 | 1,600 | 100 | 19.71 | 19.92 |

## Assumptions and bridge

| Year / 年 | Case / 情境 | Period / 適用期間 | GM / 毛利率 | Opex / 營業費用 | Nonop / 業外 | Tax / 稅率 | NCI / 非控制淨利 |
|---|---|---|---:|---:|---:|---:|---:|
| 2026 | downside | H2 | 32.5% | 210 | -25 | 28% | 12 |
| 2026 | base | H2 | 35.0% | 210 | 25 | 25% | 12 |
| 2026 | upside | H2 | 37.0% | 220 | 35 | 23% | 15 |
| 2027 | downside | FY | 32.0% | 420 | 0 | 28% | 24 |
| 2027 | base | FY | 35.5% | 440 | 50 | 25% | 30 |
| 2027 | upside | FY | 37.0% | 470 | 60 | 23% | 35 |
| 2028 | downside | FY | 31.0% | 425 | 0 | 28% | 24 |
| 2028 | base | FY | 35.0% | 475 | 50 | 25% | 32 |
| 2028 | upside | FY | 37.0% | 525 | 60 | 23% | 40 |

`Revenue = rugged + commercial + repair/other`

`Parent net income = (revenue × gross margin − opex + net nonoperating) × (1 − tax rate) − noncontrolling profit`

`EPS = parent net income / weighted-average shares`

For 2026, apply the forecast bridge only to H2 revenue, then add actual H1 parent profit 329.540. Divide the full-year sum by assumed full-year diluted shares 59.316 or basic shares 58.685; do not add rounded half-year EPS. For 2027 and 2028 apply parameters to the full year. Diluted shares match H1 reported dilution as a conservative modeling convention; actual employee-compensation dilution may change.

The 2026 base H2 bridge is revenue 2,063.992 → gross profit 722.397 → operating profit 512.397 → pretax 537.397 → parent profit 391.048; full-year parent profit 720.588 and diluted EPS 12.15. The 2027 base is revenue 4,300 → gross profit 1,526.500 → operating profit 1,086.500 → pretax 1,136.500 → tax 284.125 → minority profit 30 → parent profit 822.375 → diluted EPS 13.86.

Downside combines shipment deferral, lower rugged mix, component-cost pressure and weaker nonoperating income; 2026 H2 nonoperating -25 can represent recurring net income 25 offset by FX loss 50. The 2027 downside nonoperating 0 could include recurring income 40 offset by FX loss 40. Upside needs completed capacity, faster deliveries and retained pricing. Base tax 25% is above the 2025 effective rate but below H1 2026; it is explicitly unresolved, not an assumed statutory reset. Depreciation, compensation, inventory provisions and expansion staffing remain within margins/opex.

## Earnings quality and sensitivity

Actual H1 includes a small FX gain; removing it at assumed 25% tax reduces modeled 2026 EPS by about 0.04. No FVOCI equity-disposal gains enter EPS. No unsupported tax benefit or new AI/drone profit is added. Future nonoperating income includes ordinary investment returns after finance costs; forecast FX is neutral in the base, adverse in the downside.

At the 2027 base, a 1 percentage-point gross-margin change affects EPS by about 0.54; a 5 percentage-point tax-rate increase reduces EPS by about 0.96. Holding H2 2026 tax at 28.51% instead of 25% reduces full-year EPS by about 0.32. The company discloses approximately 14.895 of after-tax sensitivity to a 1% parallel currency movement at the H1 balance sheet, equivalent to roughly 0.25 per diluted share if fully attributable; this is a static exposure, not a currency forecast.

Cash-flow feasibility is conditional: H1 working-capital absorption means growth requires inventory conversion, prepayments or existing liquid assets. No new equity issuance or debt is assumed. The 2028 figures are a duration stress test and are not used for the headline valuation. Review assumptions in [the register](assumptions.md) and [open questions](07_open_questions.md).
