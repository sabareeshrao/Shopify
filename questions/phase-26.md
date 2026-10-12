# Phase 26 — Testing, resilience and security hardening

**Questions:** 45 · **IDs:** Q0943–Q0987 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop

Each question is a real build/test task. A box is checked only after concrete code, an observed outcome, and a matching tracker commit.


## JUnit 5 isolated domain tests

- [ ] **Q0943 — How would you specify JUnit 5 isolated domain tests with explicit contracts for assertions, parameterized input and fixtures and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** false positive assertions or static-state leakage.
  - **Verification:** pricing and policy test suite.

- [ ] **Q0944 — How would you implement JUnit 5 isolated domain tests with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** false positive assertions or static-state leakage.
  - **Verification:** pricing and policy test suite.

- [ ] **Q0945 — How would you integrate JUnit 5 isolated domain tests into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** false positive assertions or static-state leakage.
  - **Verification:** pricing and policy test suite.

- [ ] **Q0946 — How would you detect and recover from false positive assertions or static-state leakage while implementing JUnit 5 isolated domain tests?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** false positive assertions or static-state leakage.
  - **Verification:** pricing and policy test suite.

- [ ] **Q0947 — How would you demonstrate pricing and policy test suite with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** false positive assertions or static-state leakage.
  - **Verification:** pricing and policy test suite.


## Mockito service and interaction tests

- [ ] **Q0948 — How would you specify Mockito service and interaction tests with explicit contracts for dependencies, argument captors and test isolation and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** mocking business rules instead of dependencies.
  - **Verification:** service failure and interaction tests.

- [ ] **Q0949 — How would you implement Mockito service and interaction tests with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** mocking business rules instead of dependencies.
  - **Verification:** service failure and interaction tests.

- [ ] **Q0950 — How would you integrate Mockito service and interaction tests into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** mocking business rules instead of dependencies.
  - **Verification:** service failure and interaction tests.

- [ ] **Q0951 — How would you detect and recover from mocking business rules instead of dependencies while implementing Mockito service and interaction tests?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** mocking business rules instead of dependencies.
  - **Verification:** service failure and interaction tests.

- [ ] **Q0952 — How would you demonstrate service failure and interaction tests with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** mocking business rules instead of dependencies.
  - **Verification:** service failure and interaction tests.


## Testcontainers MySQL repository tests

- [ ] **Q0953 — How would you specify Testcontainers MySQL repository tests with explicit contracts for real schema migrations, CRUD and query behavior and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** H2 passes but MySQL fails.
  - **Verification:** repeatable DB integration suite.

- [ ] **Q0954 — How would you implement Testcontainers MySQL repository tests with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** H2 passes but MySQL fails.
  - **Verification:** repeatable DB integration suite.

- [ ] **Q0955 — How would you integrate Testcontainers MySQL repository tests into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** H2 passes but MySQL fails.
  - **Verification:** repeatable DB integration suite.

- [ ] **Q0956 — How would you detect and recover from H2 passes but MySQL fails while implementing Testcontainers MySQL repository tests?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** H2 passes but MySQL fails.
  - **Verification:** repeatable DB integration suite.

- [ ] **Q0957 — How would you demonstrate repeatable DB integration suite with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** H2 passes but MySQL fails.
  - **Verification:** repeatable DB integration suite.


## Spring MVC API contract tests

- [ ] **Q0958 — How would you specify Spring MVC API contract tests with explicit contracts for MockMvc, validation, response body and error codes and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** 200 returned for forbidden request.
  - **Verification:** contract tests across HTTP cases.

- [ ] **Q0959 — How would you implement Spring MVC API contract tests with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** 200 returned for forbidden request.
  - **Verification:** contract tests across HTTP cases.

- [ ] **Q0960 — How would you integrate Spring MVC API contract tests into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** 200 returned for forbidden request.
  - **Verification:** contract tests across HTTP cases.

- [ ] **Q0961 — How would you detect and recover from 200 returned for forbidden request while implementing Spring MVC API contract tests?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** 200 returned for forbidden request.
  - **Verification:** contract tests across HTTP cases.

- [ ] **Q0962 — How would you demonstrate contract tests across HTTP cases with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** 200 returned for forbidden request.
  - **Verification:** contract tests across HTTP cases.


## security authorization and vulnerability tests

- [ ] **Q0963 — How would you specify security authorization and vulnerability tests with explicit contracts for JWT tampering, IDOR, upload and injection threats and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** merchant data leakage and malicious filenames.
  - **Verification:** negative security regression suite.

- [ ] **Q0964 — How would you implement security authorization and vulnerability tests with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** merchant data leakage and malicious filenames.
  - **Verification:** negative security regression suite.

- [ ] **Q0965 — How would you integrate security authorization and vulnerability tests into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** merchant data leakage and malicious filenames.
  - **Verification:** negative security regression suite.

- [ ] **Q0966 — How would you detect and recover from merchant data leakage and malicious filenames while implementing security authorization and vulnerability tests?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** merchant data leakage and malicious filenames.
  - **Verification:** negative security regression suite.

- [ ] **Q0967 — How would you demonstrate negative security regression suite with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** merchant data leakage and malicious filenames.
  - **Verification:** negative security regression suite.


## purchase lifecycle end-to-end tests

- [ ] **Q0968 — How would you specify purchase lifecycle end-to-end tests with explicit contracts for catalog to cart, sandbox payment, order and refund and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** webhook race and duplicate orders.
  - **Verification:** full purchase and cancellation flow.

- [ ] **Q0969 — How would you implement purchase lifecycle end-to-end tests with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** webhook race and duplicate orders.
  - **Verification:** full purchase and cancellation flow.

- [ ] **Q0970 — How would you integrate purchase lifecycle end-to-end tests into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** webhook race and duplicate orders.
  - **Verification:** full purchase and cancellation flow.

- [ ] **Q0971 — How would you detect and recover from webhook race and duplicate orders while implementing purchase lifecycle end-to-end tests?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** webhook race and duplicate orders.
  - **Verification:** full purchase and cancellation flow.

- [ ] **Q0972 — How would you demonstrate full purchase and cancellation flow with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** webhook race and duplicate orders.
  - **Verification:** full purchase and cancellation flow.


## load and performance benchmarking

- [ ] **Q0973 — How would you specify load and performance benchmarking with explicit contracts for representative traffic, p95 latency and query counts and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** connection pool saturation or GC pauses.
  - **Verification:** repeatable load report.

- [ ] **Q0974 — How would you implement load and performance benchmarking with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** connection pool saturation or GC pauses.
  - **Verification:** repeatable load report.

- [ ] **Q0975 — How would you integrate load and performance benchmarking into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** connection pool saturation or GC pauses.
  - **Verification:** repeatable load report.

- [ ] **Q0976 — How would you detect and recover from connection pool saturation or GC pauses while implementing load and performance benchmarking?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** connection pool saturation or GC pauses.
  - **Verification:** repeatable load report.

- [ ] **Q0977 — How would you demonstrate repeatable load report with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** connection pool saturation or GC pauses.
  - **Verification:** repeatable load report.


## fault injection and idempotency tests

- [ ] **Q0978 — How would you specify fault injection and idempotency tests with explicit contracts for timeouts, retries, crash recovery and outbox and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** duplicate payment or lost inventory.
  - **Verification:** deterministic fault recovery tests.

- [ ] **Q0979 — How would you implement fault injection and idempotency tests with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** duplicate payment or lost inventory.
  - **Verification:** deterministic fault recovery tests.

- [ ] **Q0980 — How would you integrate fault injection and idempotency tests into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** duplicate payment or lost inventory.
  - **Verification:** deterministic fault recovery tests.

- [ ] **Q0981 — How would you detect and recover from duplicate payment or lost inventory while implementing fault injection and idempotency tests?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** duplicate payment or lost inventory.
  - **Verification:** deterministic fault recovery tests.

- [ ] **Q0982 — How would you demonstrate deterministic fault recovery tests with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** duplicate payment or lost inventory.
  - **Verification:** deterministic fault recovery tests.


## coverage quality and release gates

- [ ] **Q0983 — How would you specify coverage quality and release gates with explicit contracts for meaningful coverage, static analysis and dependency scanning and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** green build despite critical missing tests.
  - **Verification:** CI fails on controlled regression.

- [ ] **Q0984 — How would you implement coverage quality and release gates with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** green build despite critical missing tests.
  - **Verification:** CI fails on controlled regression.

- [ ] **Q0985 — How would you integrate coverage quality and release gates into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** green build despite critical missing tests.
  - **Verification:** CI fails on controlled regression.

- [ ] **Q0986 — How would you detect and recover from green build despite critical missing tests while implementing coverage quality and release gates?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** green build despite critical missing tests.
  - **Verification:** CI fails on controlled regression.

- [ ] **Q0987 — How would you demonstrate CI fails on controlled regression with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** green build despite critical missing tests.
  - **Verification:** CI fails on controlled regression.
