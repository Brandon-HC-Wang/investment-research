# AI Change Workflow

## 1. Load context

Read the four required files in order. For company changes, load metadata, thesis, open questions, all relevant numbered records, industry guidance, and model conventions.

## 2. Classify the input

Determine whether the new material is:

- a source fact;
- a management claim;
- an analyst estimate;
- a new or changed hypothesis;
- a correction to previous research;
- a methodology or system change.

Do not treat a press release as analysis. Extract only what changes the causal model or closes an evidence gap.

## 3. Map the impact

Trace the new information through:

`operating variable → revenue → margin → operating profit → below-the-line items → share count → EPS → cash flow → thesis/valuation`

Mark stages that are immaterial or unknown. Do not assume revenue changes flow proportionally to EPS.

## 4. Update atomically

Change all affected canonical files in one coherent edit. Preserve old assumptions in `assumptions.md` and dated history, update current summaries, and add or change open-question statuses. Update `research.yaml` for workflow state while retaining backward-compatible fields in `meta.yaml` until migration is complete.

## 5. Record provenance

Attach source metadata near the claim it supports and retain lawful artifacts under the appropriate `sources/` category. If the finding is reusable across companies, add it to the industry package, knowledge layer, thesis, or scoped research log and link back to the company record.

## 6. Challenge the conclusion

Seek evidence against the emerging view. Test alternative explanations, identify the most EPS-sensitive uncertainty, and distinguish a genuine structural change from timing, mix, accounting, or cycle effects.

## 7. Validate

Run:

```bash
python3 scripts/validate_repository.py
```

Review the diff for accidental history deletion, inconsistent dates, broken links, uncited material facts, and contradictions among the EPS model, thesis, valuation, and metadata.

## 8. Handoff

Summarize which canonical records changed, the most important conclusion, remaining uncertainty, and the next action. Do not produce a recommendation.
