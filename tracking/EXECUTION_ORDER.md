# Editable execution order

**Do not use IDs as hard-coded prerequisites.** IDs are permanent identity, not an immutable timetable. The base execution order is initially the numeric order, `Q0001` through `Q1025`, because it follows dependency-aware phases.

## Current overrides

_None. The baseline sequence applies._

## How to insert a newly discovered prerequisite

1. Open a change request in `changes/` and allocate the next unused ID, e.g. `Q1026`.
2. Add the full new question in `questions/extensions/` using `QUESTION-TEMPLATE.md`.
3. Record `after: Qnnnn` and `before: Qmmmm` with an explanation. Explicit dependency constraints win over the original numeric order.
4. Add a tracker row in `PROGRESS.csv`; update any affected existing question and `changes/CHANGELOG.md`.
5. Verify with `python scripts/validate_roadmap.py` and commit.

## Overrides format

| Question ID | Execute after | Execute before | Reason | Change ID |
|---|---|---|---|---|
| _example Q1026_ | _Q0234_ | _Q0235_ | _An omitted prerequisite_ | _CR-0001_ |

The example is illustrative and not an actual created question.
