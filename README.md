# Shopify — Java E-commerce Built From Scratch

> A hands-on, interview-driven reconstruction of a Shopizer-class e-commerce application. This repository is **not** the Shopify commercial platform; `Shopify` is the user-chosen repository name.

## Jump directly into the course

- **[Master index — all 28 phases and 1,025 questions](questions/MASTER-INDEX.md)**
- **[Phase 00 — start at Q0001](questions/phase-00.md)**
- [Live per-question progress register](tracking/PROGRESS.csv) · [Current task](tracking/CURRENT_TASK.md)
- [Phase progress](tracking/PHASE_STATUS.md) · [Editable execution order](tracking/EXECUTION_ORDER.md)
- [Add or revise questions](changes/CHANGE-REQUEST-TEMPLATE.md) · [Discovered gaps](changes/DISCOVERED-GAPS.md) · [Change log](changes/CHANGELOG.md)
- [New question IDs beyond Q1025](questions/extensions/README.md) · [Quality gates](docs/QUALITY-GATES.md)
- [Reference feature coverage](docs/REFERENCE-COVERAGE.md) · [Roadmap validation workflow](.github/workflows/roadmap-validation.yml)

## Mission

Build an original, working Java 21 + Spring Boot e-commerce system by finishing sequenced development questions. Each question represents a verifiable implementation/design task, not a trivia question. After reviewing a question, generate diverse MCQs, explain runnable code and expected output, implement it in IntelliJ IDEA, verify it, and commit the result. The aim is functional coverage of **backend, customer storefront, and admin dashboard**, not blind copying.

## Reference repositories (pinned for repeatability)

- Backend: https://github.com/shopizer-ecommerce/shopizer at `6a4a0a65a3408ee8f62597b51d1b3aac24b77dee`
- Admin: https://github.com/shopizer-ecommerce/shopizer-admin at `3e144ed2c145d365f8593d05c7a370400fe5c2ff`
- Storefront: https://github.com/shopizer-ecommerce/shopizer-shop-reactjs at `455b4bc6b4a542fe4542d6660dafe3b68f1131c3`

The reference code includes older dependencies and configurations. Our build uses Java 21 and an independently tested compatible Spring Boot version. The reference backend has five Maven modules; those are *modules*, not five independently deployed microservices. The original licenses and attribution requirements must be respected if copying code/assets.

## Planned curriculum

- **28 phases**, initially **1,025 development questions** (IDs `Q0001`–`Q1025`)
- Phase-specific, numbered **canonical question files** in `questions/`
- **Progress tracking** in `tracking/`, change requests in `changes/`
- More questions can be added **without renumbering existing IDs**.
- The number 1,025 is an initial curriculum scope estimate, **not** a historical Shopizer implementation count.

## Learning protocol

1. Paste the next canonical question ID + its full wording into ChatGPT.
2. Generate a diverse MCQ lesson (Java code, expected output, internals, debugging, real scenarios, interview answer).
3. Implement incrementally in IntelliJ IDEA. Explain every new file/line; do not silently skip setup.
4. Verify code, tests and acceptance gates; record evidence.
5. **Only once confirmed complete**, commit code, lesson and progress; then move to the next question.
6. Use the change workflow if the plan needs more questions or a different order.

## Rules for edits

- **IDs are permanent**: never reuse or renumber a published question.
- The questions are a *living plan*: wording, scope, order, prerequisites, acceptance criteria and phase membership may change with an entry in `changes/CHANGELOG.md`.
- To insert a task, allocate the **next unused ID** and set `after:` / `before:` relationships in the change request. IDs reflect creation, **not** immutable execution order.
- To split a task, mark the original `SPLIT` and allocate child IDs; to remove one, mark `RETIRED`. Never delete completed evidence.
- Do **not** fabricate passing tests or completed commits.
- Reference mapping means domain/feature correspondence, **not** line-by-line source-code equivalence.

## Planned stacks

Java 21, Spring Boot, Maven, Spring Data JPA, MySQL, Spring Security, REST/JSON, JUnit 5, Mockito, Testcontainers, React storefront, Angular admin, Docker and GitHub Actions. Payment processing is sandbox-only during training. External services and search infrastructure are introduced when justified, not required for the first runnable app.

**Current status (2026-10-12):** Initial 28-phase / 1,025-question baseline is committed and indexed. **0/1,025 tasks completed.** Next task: Q0001. The question bank is intentionally editable through change requests; no application code is claimed finished.
