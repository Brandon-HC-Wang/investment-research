# Novatek — EPS Model

Model date: 2026-11-05; TWD bn, shares bn, EPS TWD/share. **Conditional analyst estimates with low confidence**, not company guidance or an adopted earnings forecast. The base column is a central sensitivity anchored to recent operations; missing Q3 product economics prevent a validated forecast. Review on 2026-11-06.

## Reported reference and formula

FY2025 revenue 100.663, basic EPS 26.87; 9M2026 revenue 82.777 and diluted EPS 26.55. Model bridge:

`SoC units × price/mix + DDIC units × price/mix → sales × GM − opex + recurring non-op → pre-tax × (1 − tax) ÷ diluted shares`.

For Q4/FY2027/FY2028 use 0.612bn shares. This conservatively includes the 3m issued restricted shares and small employee dilution; it is not reported weighted-average shares. Preserve R&D, recurring compensation and inventory charges. No investment revaluation or explicit FX windfall is projected. [S2 pp. 24–25, 31, 34]

## Current-year bridge

| Q4 2026 assumption | Downside | Base sensitivity | Upside |
|---|---:|---:|---:|
| Revenue | 26.0 | 29.0 | 32.0 |
| GM | 38% | 40% | 42% |
| Opex | 6.1 | 5.8 | 5.6 |
| Recurring net non-op | 0.20 | 0.25 | 0.30 |
| Tax | 20% | 18% | 17% |
| FY2026 sales, actual 9M + Q4 | 108.8 | 111.8 | 114.8 |
| FY2026 diluted EPS, approximately | 31.8 | 34.7 | 37.6 |

Revenue brackets retrenchment below Q3 versus continued growth; margin brackets the Q3 guidance range and recent Q2 actual. Opex is anchored to quarterly TWD5.58–5.69bn plus ramp/compensation risk. Tax brackets recent effective rates and a 20% stress; no precision claim. FY2026 EPS adds reported 9M diluted EPS to Q4 modeled EPS; annual weighted-average-share rounding makes this approximate. Reported 9M retains historical investment/FX gains, so this FY2026 bridge is **not normalized full-year EPS**. [S2/S3 p. 7; S6 p. 1]

## FY2027–FY2028 operating scenarios

**Explicit anchor limitation:** Annualized Q2 product sales are SoC 58.824 and DDIC 55.960, total 114.784. These are a run-rate reference, not FY2026 segment results. FY2027 volume/mix changes below are relative to this reference; FY2028 changes are relative to each scenario's FY2027. Other revenue and returns are netted to zero, a simplification; reconcile to actual product results before adopting a forecast. Unit growth represents platform volume/share/content together because unit data are undisclosed. FX is constant within the price/mix term.

| Assumption | Downside | Base sensitivity | Upside |
|---|---|---|---|
| FY2027 SoC volume; price/mix | −10%; −3% | +5%; +2% | +15%; +4% |
| FY2027 DDIC volume; price/mix | −5%; −4% | +3%; −2% | +10%; +3% |
| FY2027 GM; opex | 37%; 23.8 | 40%; 23.8 | 43%; 24.8 |
| FY2028 SoC volume; price/mix | −5%; −2% | +8%; +2% | +15%; +3% |
| FY2028 DDIC volume; price/mix | −5%; −3% | +3%; +1% | +8%; +2% |
| FY2028 GM; opex | 36%; 24.2 | 40%; 25.3 | 43%; 27.2 |
| Annual recurring non-op, both years | 0.8 | 1.0 | 1.2 |
| Tax, both years | 20% | 18% | 17% |
| FY2027 revenue / diluted EPS | 102.4 / 19.5 | 119.5 / 33.5 | 133.8 / 46.0 |
| FY2028 revenue / diluted EPS | 94.8 / 14.0 | 128.2 / 36.1 | 153.2 / 54.1 |

Downside combines DDIC price/share erosion and SoC digestion with sticky R&D. Base assumes limited content gains and 40% GM, between FY2025 weakness and Q2 recovery. Upside requires measured multi-customer OLED/vision ramps and higher GM; the roadmap alone is insufficient. These broad outcomes demonstrate operating leverage; they are not probability-weighted forecasts. Flat recurring non-op is approximately recent interest income less finance cost, not return on all investments.

**Implication:** Even central sales growth need not produce uninterrupted EPS growth: central FY2027 EPS 33.5 is below the FY2026 reported-style bridge 34.7 after removing projected revaluation windfalls and retaining R&D. No established 2–5 year earnings-compounding claim yet.

## Normalization and sensitivity

9M illustrative adjusted EPS 25.24 removes P&L financial-asset and FX gains with a 20% marginal tax assumption. A stricter operating-plus-net-interest bridge `(17.578214 + 0.721036 − 0.006967) × 80% / 0.609186` gives 24.02; this also resets tax and excludes other income, so it is a separate sensitivity, not the same adjusted measure. OCI gains are never added or subtracted from reported EPS. [02_financials.md](02_financials.md)

At FY2027 central sales, 1pp GM changes annual EPS by about TWD1.60, holding opex/tax/shares fixed. Additional TWD0.5bn annual opex reduces EPS about TWD0.67; a TWD1bn inventory write-down reduces EPS about TWD1.34 under 18% tax. At constant revenue, no separate double-counted mix-margin premium is added.

Reproducible inputs/results and boundaries: [model JSON](sources/2026-11-05-model.json). Assumptions A-2026-001–005 remain Open; sources [S1–S6](sources/README.md).

## 2026-11-05 — Follow-up: a usable FY2026 EPS estimate

**Provisional analytical reference:** approximately TWD34–35 full-year diluted EPS; central scenario about **34.7**, with a conditional scenario range **31.8–37.6**. These restate the existing scenarios, not a new forecast revision, statistical confidence interval or market consensus. Confidence remains low; the 2026-11-06 conference has not happened at this cutoff. S8 and the company's financial-news index were checked again; no Q4 company outlook was obtained.

The operating premise is modest Q4 shipment softening after Q3, with price/mix and inventory charges determining margin. The central case assumes Q4 revenue TWD29.0bn (−6.36% versus Q3), GM 40% (versus Q3 40.89%), and opex TWD5.8bn (versus Q3 5.581bn). This balances the visible operating recovery against inventory risk; it does not claim a measured probability of these outcomes. [S2 pp. 7, 15; A-2026-006]

Central bridge, TWD bn:

1. Gross profit = 29.0 × 40% = 11.6.
2. Operating profit = 11.6 − 5.8 = 5.8.
3. Pre-tax profit = 5.8 + 0.25 recurring net non-op = 6.05.
4. Parent net profit = 6.05 × (1 − 18%) = 4.961.
5. Q4 diluted EPS = 4.961 / 0.612 = 8.11.
6. Approximate full-year diluted EPS = reported 9M 26.55 + modeled Q4 8.11 = **34.66**, rounded **34.7**. Do not substitute the 9M basic EPS 26.58 into this diluted bridge.

For comparison, the downside Q4 adds about 5.20 EPS and the upside adds 11.04. Whole-year weighted-average diluted shares are not the same as Q4 shares: using an illustrative annual denominator `(0.609186 × 3 + 0.612) / 4 = 0.6098895` and actual 9M net profit TWD16.171604bn gives central annual EPS approximately 34.65. The scenarios are therefore reported as approximate rather than accounting-precise annual EPS; the denominator also depends on actual vesting/employee dilution and quarter/day weights. [S2 p. 34]

**Earnings-quality cross-check:** The central reported-style estimate retains actual 9M financial-asset/FX gains. Removing these with the prior illustrative 20% marginal-tax adjustment reduces full-year EPS by about 1.31 to **33.3**; this is a limited normalization sensitivity, not a verified measure of all sustainable earnings. OCI gains already excluded from EPS are not removed again. Ordinary inventory losses and stock compensation remain expensed. [S2 pp. 16, 25, 31–34]

**Q4 sensitivities, not annual operating run rates:** At central assumptions, Q4 GM −1pp reduces full-year EPS about 0.39; Q4 revenue −TWD1bn reduces about 0.54, holding GM/opex/tax/shares fixed. A separate TWD1bn additional write-down reduces about 1.34, but must not be counted twice if already reflected in a lower GM assumption. Large new investment/FX items could push reported results outside the scenario range.

Next evidence: 2026-11-06 Q4 outlook and October sales, followed by actual November/December sales and year-end charges. Source register S2/S3/S6/S8/S9 and [reproducible model](sources/2026-11-05-model.json). Existing scenario inputs and research maturity remain unchanged.
