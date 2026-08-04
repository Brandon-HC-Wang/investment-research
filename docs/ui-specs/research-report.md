# Investment Research Report UI Specification

## Purpose

This specification defines a reusable HTML presentation system for long-form company research. The interface should make evidence, uncertainty, causal relationships, scenario differences, and verification work easier to understand without converting the research into a promotional dashboard.

The report is a derived reading artifact. Canonical company, industry, model, and research-log records remain the source of truth.

## Product profile

| Attribute | Standard |
|---|---|
| Product type | Long-form investment-research report with data-dashboard elements |
| Primary reader | Human analyst reviewing an AI-maintained research record |
| Default language | Traditional Chinese for the rendered reading artifact |
| Implementation | One self-contained HTML file with embedded CSS and minimal JavaScript |
| Network dependency | None required for layout, typography, icons, or interaction |
| Primary use | Desktop reading, mobile review, printing, and PDF export |
| Research posture | Neutral, evidence-led, scenario-based, and non-promotional |

## Information architecture

The visual structure follows the repository reasoning chain:

1. Report identity, information cutoff, stage, and confidence.
2. Executive view and boundaries of the conclusion.
3. Business model and customer value.
4. Competitive advantage and evidence quality.
5. Financial profile and earnings quality.
6. Revenue and EPS drivers.
7. Backlog, pipeline, replacement drivers, and future visibility.
8. Operating scenarios and EPS bridge.
9. Timing delay versus permanent economic impairment.
10. The one or two primary risks, warning signals, and open questions.
11. Thesis, confirmation, falsification, and valuation status.
12. Sources, methodology, and report limitations.

Valuation must not precede the business, earnings-quality, visibility, and risk sections. The report must not include buy, sell, or hold instructions.

## Visual principles

### Data-dense, not crowded

Use a dashboard grid for comparisons and a document flow for reasoning. KPI cards summarize already-explained measures; they do not replace causal analysis. Tables are reserved for exact mappings, multi-period comparisons, scenario inputs, or durable identifiers.

### Evidence is visible

Use text labels in addition to color:

| Evidence class | Label | Visual role |
|---|---|---|
| Reported fact | `Fact` | Blue |
| Analyst estimate | `Estimate` | Amber |
| Testable hypothesis | `Hypothesis` | Violet or neutral outline |
| Analytical opinion | `Opinion` | Neutral |
| Open question | `Open` | Amber |
| Material downside mechanism | `Risk` | Red |

Management guidance and third-party forecasts retain attribution and must not receive a `Fact` label merely because they contain precise figures.

### Confidence is not sentiment

Research confidence indicates evidence quality. It should appear near the information cutoff and use text such as `Low`, `Medium`, or `High`; do not use bullish or bearish styling.

## Design tokens

### Light theme

| Token | Value | Use |
|---|---:|---|
| `--bg` | `#F4F7FB` | Page background |
| `--paper` | `#FFFFFF` | Main surfaces |
| `--paper-soft` | `#F8FAFC` | Nested cards and table headers |
| `--ink` | `#14213D` | Primary text |
| `--muted` | `#526176` | Secondary text; maintain WCAG AA contrast |
| `--line` | `#DBE3EF` | Borders and dividers |
| `--blue` | `#1E40AF` | Facts, navigation, primary data |
| `--blue-2` | `#2563EB` | Active and interactive states |
| `--blue-soft` | `#E8EFFF` | Blue-tinted surfaces |
| `--amber` | `#B45309` | Estimates and uncertainty |
| `--amber-soft` | `#FFF7E6` | Estimate callouts |
| `--red` | `#B42318` | Material downside mechanisms |
| `--red-soft` | `#FFF0EE` | Risk callouts |

### Dark theme

Use near-navy surfaces rather than pure black. Primary text must remain near white, muted text must remain readable, and borders must be visible. The supplied template contains the canonical dark values.

### Typography

- Use a system sans-serif stack with `Noto Sans TC`, `PingFang TC`, and `Microsoft JhengHei` fallbacks for offline Traditional Chinese rendering.
- Use the system monospace stack for tickers, dates, units, identifiers, chart values, and section kickers.
- Do not require web fonts. External fonts may improve consistency but violate the default offline contract.
- Body line height: `1.65–1.75`.
- Body text: at least `15px` on mobile and `16px` for long desktop passages where space permits.
- Use tabular numerals for financial tables and KPI values.

### Geometry

| Element | Standard |
|---|---|
| Content width | Maximum `1180px` |
| Main section radius | `18px` desktop, `16px` mobile |
| Nested card radius | `12–14px` |
| Section spacing | `24px` |
| Interactive transition | `150–250ms`; color, border, or opacity only |
| Shadow | Soft navy shadow; remove for print |

## Component contract

### Floating toolbar

Show the ticker, report name, information cutoff, and compact actions. Supported actions are theme toggle and print or PDF export. The toolbar is sticky with visible edge spacing and must not cover anchored headings.

### Section navigation

Desktop uses a sticky left rail. Mobile uses a horizontally scrollable list of short section names. Active-state highlighting may use `IntersectionObserver`; navigation remains functional without JavaScript.

### Hero

The hero contains company identity, ticker, report title, one-sentence causal summary, research stage, confidence, cutoff date, and currency. Avoid stock imagery, decorative photography, price targets, and promotional claims.

### KPI cards

Each KPI includes period, unit, classification, and a short interpretation. Never display an unlabeled figure. Limit above-the-fold cards to the two or three measures that define the current research state.

### Evidence callouts

Callouts must explain the boundary of a conclusion, a material uncertainty, or the analytical meaning of a figure. Do not use callouts for generic emphasis.

### Scenario cards and tables

Scenarios change operating mechanisms, not only valuation multiples. Show case name, forecast period, main operational assumptions, point estimate or range, and evidence required for the case. State whether cases are independent annual bounds or a cumulative forecast.

### Charts

Prefer accessible CSS or inline SVG for small offline charts. Include a visible title, unit, period, labels, and a text interpretation. Color must not be the only encoding. Avoid 3D charts, gauges, ornamental gradients, and unlabeled axes.

### Timelines

Use timelines for recognition sequences, milestones, or changes in evidence. Every item includes an ISO date or fiscal period, the event, and its analytical implication.

### Risk rows

Each risk states the mechanism:

`risk event → operating metric → revenue or margin → EPS → cash-flow or balance-sheet consequence`

Decorative severity meters are optional. When used, they must also carry a text label and must not imply unsupported precision.

### Sources

List source title, publisher, publication or filing date, access date, URL, and page or section references for long documents. Distinguish primary and secondary sources. Source links may require a network connection, but the report layout must not.

## Responsive behavior

| Width | Expected behavior |
|---:|---|
| `1440px` | Full two-column layout with sticky navigation and wide comparison grids |
| `1024px` | Two-column layout where space permits; tables scroll within their container |
| `768px` | Single-column main layout; two-column KPI grids may remain |
| `375px` | Single-column cards and scenarios; wrapped tags; no page-level horizontal scroll |

Long identifiers, URLs, and headings must wrap. Data tables use a local horizontal scroll container rather than widening the page.

## Accessibility

- Meet WCAG AA contrast for body text and meaningful controls.
- Use semantic landmarks, heading order, tables, buttons, and links.
- Provide visible `:focus-visible` states.
- Give icon-only controls accessible labels and titles.
- Use inline SVG from one consistent icon family; do not use emoji as interface icons.
- Do not use color as the only evidence or risk indicator.
- Respect `prefers-reduced-motion`.
- Images, when necessary, require meaningful alt text; decorative images use empty alt text.

## Print and offline contract

- Embed CSS, icons, and JavaScript in the HTML file.
- Do not depend on remote stylesheets, fonts, images, or chart libraries.
- Hide navigation and action controls in print.
- Remove shadows and translucent effects in print.
- Preserve meaningful background colors with `print-color-adjust` where supported.
- Avoid breaking a small card, callout, scenario block, or table row across pages when practical.
- Links remain readable when printed even if their URLs are not expanded.

## Content integrity

- The report has an explicit information cutoff.
- Facts, estimates, hypotheses, opinions, and management targets are distinguishable.
- Currency, units, fiscal periods, and reported versus adjusted status are visible.
- Revenue is bridged through margin, operating costs, financing, tax, ownership, and diluted shares before EPS.
- Recurring, cyclical, project-based, and non-recurring earnings are separated.
- Delayed recognition is distinguished from permanent loss of economics.
- The one or two primary EPS risks have observable warning signals.
- Thesis confirmation and falsification conditions are explicit.
- Valuation is deferred when normalized earnings or attributable economics are not established.

## Implementation

Use [`../../templates/reports/investment-research-report.html`](../../templates/reports/investment-research-report.html) as the canonical implementation starting point. Copy it to the requested output location and replace the generic display content. Do not edit the template with current company facts.

The template uses semantic HTML, CSS custom properties, inline SVG, a theme toggle, print support, responsive layouts, and optional active-section navigation. It intentionally uses no external dependencies.

## Pre-delivery checklist

- [ ] The content follows the repository reasoning order.
- [ ] The information cutoff and confidence are visible.
- [ ] Facts and estimates have text labels.
- [ ] Every material number has a period and unit.
- [ ] Scenarios state causal assumptions and evidence triggers.
- [ ] Sources are complete and attributed.
- [ ] No buy, sell, or hold instruction appears.
- [ ] Desktop widths of 1024px and 1440px are visually checked.
- [ ] Mobile widths of 375px and 768px are visually checked.
- [ ] There is no page-level horizontal scroll.
- [ ] Light and dark themes preserve contrast.
- [ ] Keyboard focus is visible.
- [ ] Reduced-motion behavior is respected.
- [ ] Print or PDF output is readable.
- [ ] The report works offline.
