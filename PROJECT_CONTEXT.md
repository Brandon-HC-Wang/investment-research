# Project Context

## Mission

Build a durable, AI-native equity research system that improves with every investigation. The system exists to identify and monitor companies capable of growing sustainable earnings over the next two to five years.

The repository is the source of truth. Chat responses, temporary analyses, and external notes are incomplete until the relevant repository records are updated.

## What this system is

- A structured body of company, industry, and modeling knowledge.
- A history of hypotheses, evidence, revisions, and unresolved questions.
- A causal model connecting business activity to revenue, margins, cash flow, and EPS.
- A collaboration surface shared by humans, Codex, Claude Code, Gemini CLI, GPT, and future agents.

## What this system is not

- A daily news digest.
- A stock-price prediction service.
- A list of buy, sell, or hold calls.
- A technical-analysis or momentum-trading system.
- A collection of isolated markdown notes without shared contracts.

## Investment objective

Research should improve confidence in one central question:

> Can this company compound sustainable per-share earnings over the next two to five years, and what observable evidence would confirm or invalidate that view?

Analysis is prioritized in this order:

1. Business quality.
2. Competitive advantage.
3. Revenue drivers.
4. EPS drivers.
5. Sustainable versus non-recurring earnings.
6. Future visibility.
7. Capital allocation.
8. Valuation.

## System design principles

### Stable structure, evolving conclusions

Company filenames and core schemas are stable interfaces. Conclusions are expected to change as evidence changes. Preserve earlier assumptions and append dated revisions so future readers can reconstruct the reasoning path.

### Markdown for reasoning, YAML for state

Markdown stores narrative analysis, evidence, tables, and hypotheses. YAML stores small, machine-readable fields used for discovery, prioritization, and validation. Narrative conclusions must not be hidden only in YAML.

### One fact, one canonical home

Store company-specific facts in the company folder, reusable industry mechanics in `industries/`, analytical conventions in `models/`, and cross-company discoveries in `research-log/`. Link to canonical material instead of duplicating it.

### Evidence before confidence

Distinguish among:

- **Fact:** externally verifiable and cited.
- **Estimate:** calculated from disclosed facts and explicit assumptions.
- **Hypothesis:** plausible but not yet adequately verified.
- **Opinion:** an analytical judgment based on stated evidence.

Confidence reflects evidence quality and unresolved uncertainty, not enthusiasm.

## Durable company contract

Every directory directly under `companies/` represents one company and contains exactly the following core records:

1. `01_business.md`
2. `02_financials.md`
3. `03_growth_drivers.md`
4. `04_eps_model.md`
5. `05_timeline.md`
6. `06_notes.md`
7. `07_open_questions.md`
8. `08_thesis.md`
9. `09_valuation.md`
10. `meta.yaml`

The numbering is permanent. Add detail inside these records or in a clearly named supporting subdirectory; never change the core interface.

## Lifecycle

Research progresses through discovery, qualification, active research, monitoring, and archival. Archival means the company is no longer actively followed; it does not mean its history is deleted.

Every meaningful update should do at least one of the following:

- add or improve evidence;
- resolve or reject an open question;
- revise a model assumption while preserving the prior assumption;
- change a thesis condition, confidence level, priority, or next action;
- add a dated milestone or research-log entry.

## Definition of quality

A high-quality record lets a new analyst or AI agent determine:

- how the company makes money and why customers choose it;
- which operational variables cause revenue and EPS to change;
- how much earnings are recurring;
- what supports the next two to five years of earnings;
- which one or two risks can materially reduce EPS;
- what evidence would falsify the thesis;
- why the selected valuation method fits the economics;
- what to research next.

## Required reading order

Before modifying the repository, every agent must read:

1. `PROJECT_CONTEXT.md`
2. `AGENTS.md`
3. `.ai/context.md`
4. `docs/Framework.md`

Task-specific documents follow that sequence.
