# Canonical development question template

> Copy into the owning phase file or `questions/extensions/`; assign a never-used ID.

- [ ] **QNNNN — How would you [specific implementation question that creates an observable capability]?**
  - **Phase / feature:** Pxx / specific area
  - **Dependencies:** Qxxxx, Qyyyy (or none)
  - **Reference area:** pinned Shopizer path or documented extension
  - **Build:** classes, files, schema, API routes, UI screens or documentation to create
  - **Acceptance:** precise behavior a developer can reproduce (not "understand it")
  - **Failure cases:** invalid input, security, concurrency or recovery as relevant
  - **Test evidence:** automated test names, command and expected output
  - **Interview depth:** core Java; libraries/frameworks; code-output traps; debugging; real-world trade-offs
  - **Status:** NOT_STARTED | IN_PROGRESS | BLOCKED | VERIFIED | RETIRED | SPLIT

## MCQ lesson generation contract

When the learner pastes QNNNN, generate varied MCQs including foundations, internals, runnable Java code with `// Voice:` comments, correct expected output, APIs, database questions, production failures, security/performance trade-offs and interview-ready spoken answers. Choose volume by complexity: commonly 8–15, up to 35 for deep topics. Explain answers; do not inflate with repeats.

The question's build scope may be revised before or during implementation. Preserve ID, record changes, and do not label a question completed before code/tests are checked.
