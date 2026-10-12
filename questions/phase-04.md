# Phase 04 — Shared models, DTOs and API contracts

**Canonical IDs:** Q0091 onward · **Planned tasks:** 25 · **Status:** NOT STARTED

**Reference area:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model

Questions are development tasks, not MCQ answers. Implementation generates separate MCQs later. A checked box must have code/artifact evidence and an updated tracker.


## request and response DTO conventions

- [ ] **Q0091 — How would you design request and response DTO conventions including public API contracts isolated from JPA entities, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** accidental entity exposure or recursive serialization.
  - **Proof focus:** stable JSON schema tests.

- [ ] **Q0092 — How would you implement request and response DTO conventions in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** accidental entity exposure or recursive serialization.
  - **Proof focus:** stable JSON schema tests.

- [ ] **Q0093 — How would you connect request and response DTO conventions through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** accidental entity exposure or recursive serialization.
  - **Proof focus:** stable JSON schema tests.

- [ ] **Q0094 — How would you handle accidental entity exposure or recursive serialization in request and response DTO conventions without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** accidental entity exposure or recursive serialization.
  - **Proof focus:** stable JSON schema tests.

- [ ] **Q0095 — How would you prove request and response DTO conventions works by testing stable JSON schema tests, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** accidental entity exposure or recursive serialization.
  - **Proof focus:** stable JSON schema tests.


## Jakarta Bean Validation and error reporting

- [ ] **Q0096 — How would you design Jakarta Bean Validation and error reporting including required fields, length, range and nested validation, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** invalid payload accepted or sensitive error exposed.
  - **Proof focus:** 400 response with field-level validation details.

- [ ] **Q0097 — How would you implement Jakarta Bean Validation and error reporting in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** invalid payload accepted or sensitive error exposed.
  - **Proof focus:** 400 response with field-level validation details.

- [ ] **Q0098 — How would you connect Jakarta Bean Validation and error reporting through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** invalid payload accepted or sensitive error exposed.
  - **Proof focus:** 400 response with field-level validation details.

- [ ] **Q0099 — How would you handle invalid payload accepted or sensitive error exposed in Jakarta Bean Validation and error reporting without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** invalid payload accepted or sensitive error exposed.
  - **Proof focus:** 400 response with field-level validation details.

- [ ] **Q0100 — How would you prove Jakarta Bean Validation and error reporting works by testing 400 response with field-level validation details, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** invalid payload accepted or sensitive error exposed.
  - **Proof focus:** 400 response with field-level validation details.


## DTO mapping and transformations

- [ ] **Q0101 — How would you design DTO mapping and transformations including MapStruct or explicit mapping including nested records, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** null mapping or over-posting server-owned fields.
  - **Proof focus:** unit tests for every mapped boundary.

- [ ] **Q0102 — How would you implement DTO mapping and transformations in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** null mapping or over-posting server-owned fields.
  - **Proof focus:** unit tests for every mapped boundary.

- [ ] **Q0103 — How would you connect DTO mapping and transformations through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** null mapping or over-posting server-owned fields.
  - **Proof focus:** unit tests for every mapped boundary.

- [ ] **Q0104 — How would you handle null mapping or over-posting server-owned fields in DTO mapping and transformations without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** null mapping or over-posting server-owned fields.
  - **Proof focus:** unit tests for every mapped boundary.

- [ ] **Q0105 — How would you prove DTO mapping and transformations works by testing unit tests for every mapped boundary, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** null mapping or over-posting server-owned fields.
  - **Proof focus:** unit tests for every mapped boundary.


## HTTP status, pagination and API versioning

- [ ] **Q0106 — How would you design HTTP status, pagination and API versioning including resource URLs, PATCH/PUT semantics, sorting and cursor/page responses, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** breaking older consumers or returning inconsistent totals.
  - **Proof focus:** OpenAPI and MockMvc contract tests.

- [ ] **Q0107 — How would you implement HTTP status, pagination and API versioning in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** breaking older consumers or returning inconsistent totals.
  - **Proof focus:** OpenAPI and MockMvc contract tests.

- [ ] **Q0108 — How would you connect HTTP status, pagination and API versioning through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** breaking older consumers or returning inconsistent totals.
  - **Proof focus:** OpenAPI and MockMvc contract tests.

- [ ] **Q0109 — How would you handle breaking older consumers or returning inconsistent totals in HTTP status, pagination and API versioning without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** breaking older consumers or returning inconsistent totals.
  - **Proof focus:** OpenAPI and MockMvc contract tests.

- [ ] **Q0110 — How would you prove HTTP status, pagination and API versioning works by testing OpenAPI and MockMvc contract tests, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** breaking older consumers or returning inconsistent totals.
  - **Proof focus:** OpenAPI and MockMvc contract tests.


## shared exception and result envelopes

- [ ] **Q0111 — How would you design shared exception and result envelopes including domain error codes, exceptions and correlation identifiers, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** unhandled exceptions exposing internal details.
  - **Proof focus:** uniform responses for 400, 401, 403, 404 and 409.

- [ ] **Q0112 — How would you implement shared exception and result envelopes in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** unhandled exceptions exposing internal details.
  - **Proof focus:** uniform responses for 400, 401, 403, 404 and 409.

- [ ] **Q0113 — How would you connect shared exception and result envelopes through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** unhandled exceptions exposing internal details.
  - **Proof focus:** uniform responses for 400, 401, 403, 404 and 409.

- [ ] **Q0114 — How would you handle unhandled exceptions exposing internal details in shared exception and result envelopes without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** unhandled exceptions exposing internal details.
  - **Proof focus:** uniform responses for 400, 401, 403, 404 and 409.

- [ ] **Q0115 — How would you prove shared exception and result envelopes works by testing uniform responses for 400, 401, 403, 404 and 409, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** unhandled exceptions exposing internal details.
  - **Proof focus:** uniform responses for 400, 401, 403, 404 and 409.
