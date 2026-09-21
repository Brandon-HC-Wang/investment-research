# Forward Dividend Income

## Current status

- **Validation state:** `testing`
- **Confidence:** Medium
- **Time horizon:** Cash dividends distributed in 2027 from 2026 earnings
- **Linked screen:** [`../../screens/forward-dividend-yield/`](../../screens/forward-dividend-yield/README.md)

## Testable claim

**Hypothesis:** A company is more likely to sustain a forward cash yield above the target when normalized attributable earnings and parent-company distributable cash conservatively cover the required DPS. Selection by exchange-displayed historical yield alone should produce more false positives because it may capitalize one-off earnings, non-earnings distributions, or a depressed price.

The mechanism is:

`business and revenue durability → normalized attributable EPS → parent cash capacity → supportable DPS → forward cash yield`

## Evidence for and against

**Supporting evidence:** Dividend capacity is constrained by distributable earnings, liquidity, leverage, reinvestment needs, and legal or regulatory capital. A coverage-based screen therefore tests a causal constraint rather than extrapolating the last distribution.

**Contradicting evidence and uncertainty:** Boards may change payout policy, parent-company cash may differ from consolidated cash flow, capital-surplus distributions may be intentional, and cyclical or project businesses may distribute cash despite low current-period normalized EPS. Sector-specific models and point-in-time validation are required.

## Validation requirement

The strategy remains `testing` for at least three annual dividend cohorts and 100 point-in-time company-year observations. Initial acceptance criteria are at least 70% forecast-interval coverage, median absolute DPS error no greater than 15%, at least 60% precision among candidates forecast above 7%, and precision at least 10 percentage points better than a displayed-yield-only baseline. Historical tests must use only information available on each recorded screen date and must disclose source coverage, false-positive causes, and sector concentration.

Moving to `validated` does not create a recommendation. It means the defined mechanism passed its predeclared point-in-time evidence tests.

## History

- **2026-09-10 — `testing`:** Initial definition created from the forward-dividend-yield methodology. No completed formal screen run or outcome validation exists yet.
- **2026-09-14 — `testing`:** Predeclared minimum sample and outcome metrics were added before the first formal run. Thresholds remain hypotheses to test rather than evidence of efficacy.
