# Phase 23 — Bulk import/export and background jobs

**Original tasks:** 24 · **Range:** Q0789–Q0812 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core

Build in short increments. Every question needs MCQ training, runnable code, expected results, automated coverage where feasible and verified completion before its box is checked.


## product CSV import contract

- [ ] **Q0789 — How would you design product CSV import contract with precise requirements for headers, UTF-8, quoting and schema version?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** embedded comma or malformed quoted CSV.
  - **Proof scenario:** valid file and broken row samples.

- [ ] **Q0790 — How would you implement product CSV import contract with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** embedded comma or malformed quoted CSV.
  - **Proof scenario:** valid file and broken row samples.

- [ ] **Q0791 — How would you connect product CSV import contract to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** embedded comma or malformed quoted CSV.
  - **Proof scenario:** valid file and broken row samples.

- [ ] **Q0792 — How would you reproduce and handle embedded comma or malformed quoted CSV for product CSV import contract without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** embedded comma or malformed quoted CSV.
  - **Proof scenario:** valid file and broken row samples.

- [ ] **Q0793 — How would you test product CSV import contract with valid file and broken row samples, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** embedded comma or malformed quoted CSV.
  - **Proof scenario:** valid file and broken row samples.


## streaming parse and bounded persistence

- [ ] **Q0794 — How would you design streaming parse and bounded persistence with precise requirements for cursor processing, batch size and memory constraints?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** 10-GB file exhausting heap.
  - **Proof scenario:** memory bounded under large import.

- [ ] **Q0795 — How would you implement streaming parse and bounded persistence with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** 10-GB file exhausting heap.
  - **Proof scenario:** memory bounded under large import.

- [ ] **Q0796 — How would you connect streaming parse and bounded persistence to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** 10-GB file exhausting heap.
  - **Proof scenario:** memory bounded under large import.

- [ ] **Q0797 — How would you reproduce and handle 10-GB file exhausting heap for streaming parse and bounded persistence without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** 10-GB file exhausting heap.
  - **Proof scenario:** memory bounded under large import.

- [ ] **Q0798 — How would you test streaming parse and bounded persistence with memory bounded under large import, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** 10-GB file exhausting heap.
  - **Proof scenario:** memory bounded under large import.


## duplicate detection and partial-success rules

- [ ] **Q0799 — How would you design duplicate detection and partial-success rules with precise requirements for SKU uniqueness, all-or-nothing versus partial import?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** same upload repeated after crash.
  - **Proof scenario:** idempotent re-import tests.

- [ ] **Q0800 — How would you implement duplicate detection and partial-success rules with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** same upload repeated after crash.
  - **Proof scenario:** idempotent re-import tests.

- [ ] **Q0801 — How would you connect duplicate detection and partial-success rules to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** same upload repeated after crash.
  - **Proof scenario:** idempotent re-import tests.

- [ ] **Q0802 — How would you reproduce and handle same upload repeated after crash for duplicate detection and partial-success rules without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** same upload repeated after crash.
  - **Proof scenario:** idempotent re-import tests.

- [ ] **Q0803 — How would you test duplicate detection and partial-success rules with idempotent re-import tests, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** same upload repeated after crash.
  - **Proof scenario:** idempotent re-import tests.


## export products and orders as CSV

- [ ] **Q0804 — How would you design export products and orders as CSV with precise requirements for authorization, filtered pagination and streamed output?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** spreadsheet formula injection or PII leak.
  - **Proof scenario:** escaped downloadable CSV.

- [ ] **Q0805 — How would you implement export products and orders as CSV with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** spreadsheet formula injection or PII leak.
  - **Proof scenario:** escaped downloadable CSV.

- [ ] **Q0806 — How would you connect export products and orders as CSV to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** spreadsheet formula injection or PII leak.
  - **Proof scenario:** escaped downloadable CSV.

- [ ] **Q0807 — How would you reproduce and handle spreadsheet formula injection or PII leak for export products and orders as CSV without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** spreadsheet formula injection or PII leak.
  - **Proof scenario:** escaped downloadable CSV.

- [ ] **Q0808 — How would you test export products and orders as CSV with escaped downloadable CSV, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** spreadsheet formula injection or PII leak.
  - **Proof scenario:** escaped downloadable CSV.


## background job orchestration

- [ ] **Q0809 — How would you design background job orchestration with precise requirements for job states, 202 response, checkpoint and retry?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** worker crashes at 70-percent completion.
  - **Proof scenario:** resume without duplicate rows.

- [ ] **Q0810 — How would you implement background job orchestration with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** worker crashes at 70-percent completion.
  - **Proof scenario:** resume without duplicate rows.

- [ ] **Q0811 — How would you connect background job orchestration to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** worker crashes at 70-percent completion.
  - **Proof scenario:** resume without duplicate rows.

- [ ] **Q0812 — How would you reproduce and handle worker crashes at 70-percent completion for background job orchestration without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** worker crashes at 70-percent completion.
  - **Proof scenario:** resume without duplicate rows.
