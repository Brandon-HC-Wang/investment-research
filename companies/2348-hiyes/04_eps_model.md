# EPS Model

## Model status

As of 2026-08-04, a low-confidence preliminary scenario model is established for 2026–2027. It is suitable for bounding outcomes, not for a single-point decision-grade forecast. Project sell-through, Q2 margin, attributable ownership accounting, and 2027 handover timing remain unresolved.

## Required causal model

The model will separate three streams:

| Stream | Revenue basis | Principal margin driver | Recognition approach |
|---|---|---|---|
| Brokerage and agency | Represented sales value × effective fee rate | Sell-through, personnel/site productivity, project mix | Service performance and disclosed accounting policy |
| Development | Attributable units or project value recognized | Selling price less land, construction, marketing, and financing economics | Project completion and handover policy |
| Investment projects | Attributable distributions or realized earnings | Project economics and ownership share | Project-specific; no automatic annualization |

The consolidated bridge will then include operating expenses, interest and investment income, tax, minority interests, and diluted shares.

## Scenarios

The model uses the disclosed project value multiplied by participation as an upper bound, then applies a recognition factor. Agency revenue, consolidated parent-attributable net margin, preferred dividends, and post-stock-dividend common shares are modeled separately. All amounts are TWD unless noted.

| Input | 2026 conservative | 2026 optimistic | 2027 conservative | 2027 optimistic |
|---|---:|---:|---:|---:|
| Scheduled project value × participation (TWD bn) | 8.33 | 8.33 | 9.84 | 9.84 |
| Recognition factor | 65% | 90% | 40% | 70% |
| Recognized attributable project proxy (TWD bn) | 5.42 | 7.50 | 3.93 | 6.88 |
| Agency revenue (TWD bn) | 2.40 | 2.80 | 2.40 | 3.00 |
| Consolidated revenue proxy (TWD bn) | 7.82 | 10.30 | 6.33 | 9.88 |
| Parent-attributable net margin | 12.0% | 18.0% | 11.5% | 18.0% |
| Less: annual preferred dividend (TWD bn) | 0.048 | 0.048 | 0.048 | 0.048 |
| Common shares after 2026 stock dividend (million) | 159.49 | 159.49 | 159.49 | 159.49 |
| **Preliminary EPS point estimate (TWD)** | **5.58** | **11.32** | **4.27** | **10.86** |
| **Sensitivity range (TWD)** | **4.7–6.5** | **10.1–12.7** | **3.5–5.4** | **9.4–12.2** |

The margin is an output proxy rather than a project margin. The conservative cases reflect lower handover, weak agency operating leverage, and finance costs. The optimistic cases require high sell-through and handover, construction margin recovery, and no material financing or valuation loss. The model deducts the approximately TWD 48 million annual preferred dividend because reported common EPS excludes that claim.

### Timing versus economic downside

The conservative recognition factors primarily represent **later recognition**, not cancellation or loss of the entire unrecognized project value. The current annual scenarios do not automatically carry the unrecognized balance into the following year, so the conservative 2026 and 2027 estimates should be read as stand-alone annual downside cases rather than a cumulative two-year forecast. A timing-only delay should raise a later year's EPS when units are eventually handed over.

Permanent downside is separate: lower selling prices or sell-through, higher construction and financing costs, cancellation, reduced participation, or inventory impairment would reduce cumulative project profit rather than merely move it between years. The next model revision should add an explicit project roll-forward so that opening unrecognized value plus new scheduled completions reconciles to recognized value and closing backlog.

### Reproducible point-estimate formula

```text
Common EPS = ((project upper bound × recognition factor + agency revenue)
              × parent-attributable net margin
              − preferred dividend)
             ÷ post-stock-dividend common shares
```

This is not equivalent to multiplying gross project sales by a uniform 20% margin. Official reported EPS may also restate share counts for the bonus issue under applicable EPS accounting; 159.49 million shares are used here to keep scenarios economically comparable.

## Review triggers

- Replace the 2026 margin proxy when the 2026 Q2 filing discloses construction and agency segment profit.
- Move toward the optimistic 2026 case only if cumulative construction recognition reaches at least TWD 5.0 billion by September with consolidated gross margin above 30% and finance costs not accelerating.
- Move toward the conservative 2027 case if any two major scheduled projects lack completion or handover evidence by 2027 Q2.
- Rebuild both years if disclosed project participation, sell-through, or preferred-share terms change.
- Add a project roll-forward after the Q2 filing to distinguish delayed revenue carried into 2027–2028 from permanently lost project economics.

## Assumption history

### 2026-08-04 — Model initiated

The model was intentionally left unquantified because reported EPS variability and monthly revenue lumpiness cannot be assigned reliably to recurring brokerage and project earnings using the current evidence set. This reduces false precision and makes segment reconciliation the next action.

### 2026-08-04 — Preliminary 2026–2027 scenario ranges added

New evidence from the 2025-11-25 management project schedule, the reviewed 2026 Q1 filing, and June 2026 revenue supports low-confidence boundary estimates. The prior unquantified model is superseded for scenario bounding but remains correct that a decision-grade single estimate requires Q2 margins and project-level handover data.

## Sources

- Hiyes International, “Investor Conference Presentation,” 2025-11-25, completion-method schedule with data through 2025-09-30, [MOPS-hosted PDF](https://mopsov.twse.com.tw/nas/STR/234820251125M001.pdf), accessed 2026-08-04.
- Hiyes International, “Consolidated Financial Statements and Review Report, 2026 Q1,” filed 2026-05-15, [TWSE document library](https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=2348&year=115&seamon=1&mtype=A), accessed 2026-08-04.
- Taiwan Stock Exchange, “Listed Companies Monthly Revenue Summary,” data month 2026-06, [OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L), accessed 2026-08-04.
- Taiwan Stock Exchange, “Listed Company Dividend Distributions,” 2025 earnings distribution approved 2026-06-17, [OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap45_L), accessed 2026-08-04.
