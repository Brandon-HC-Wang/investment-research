# UI Specifications

This directory defines reusable presentation contracts for generated research artifacts. It stores design and interaction rules, not company evidence or current research conclusions.

## Canonical status

English Markdown files are canonical. Each has a same-directory `.zh-TW.md` reading companion under the repository bilingual Markdown contract.

## Available specifications

- [`research-report.md`](research-report.md) defines the information architecture, design tokens, components, responsive behavior, accessibility, print behavior, and quality checks for investment-research HTML reports.
- [`../../templates/reports/investment-research-report.html`](../../templates/reports/investment-research-report.html) is the self-contained implementation template.

## Usage

1. Read the research framework and the relevant canonical company records.
2. Copy the HTML template to a temporary or requested output location.
3. Replace generic display content with sourced facts, labeled estimates, hypotheses, opinions, and open questions.
4. Preserve the report section order unless the company economics make a documented exception necessary.
5. Verify content, desktop and mobile layouts, keyboard focus, contrast, print output, and offline operation.

The template is structure only. It must never become a source for company facts, forecasts, or valuation assumptions.
