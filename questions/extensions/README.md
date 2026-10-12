# Newly discovered questions and replacements

Keep the **baseline Q0001–Q1025** in `questions/phase-00.md` through `phase-27.md`. New gaps discovered while implementing must be recorded here. **Next free extension ID: Q1026.** If a newer extension has been added, take the next unused global ID instead.

Create `questions/extensions/Q1026.md` using `questions/QUESTION-TEMPLATE.md` (and repeat for new questions). Give the question a `Phase:` attribute and explicitly state the `after:` and `before:` task IDs. Update tracking/PROGRESS.csv and tracking/EXECUTION_ORDER.md as needed. Record the request in changes/CHANGELOG.md.

When one task becomes too large, mark the original as SPLIT in tracking and add smaller replacement questions with new IDs. When a question is unnecessary, mark RETIRED with a reason; never delete it. Completed implementation/test/lesson commits remain linked to their original IDs.
