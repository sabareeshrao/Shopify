# Phase 00 — Reference investigation and system design

**Canonical baseline:** Q0001–Q0012 · **12 questions** · **Status:** NOT STARTED

**References pinned:**
- Backend: https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee
- Admin: https://github.com/shopizer-ecommerce/shopizer-admin/tree/3e144ed2c145d365f8593d05c7a370400fe5c2ff
- React store: https://github.com/shopizer-ecommerce/shopizer-shop-reactjs/tree/455b4bc6b4a542fe4542d6660dafe3b68f1131c3

**Phase objective:** Produce a reliable source-based architectural plan and learning governance before implementing code. These tasks are not marked finished merely because preliminary exploration has occurred.

## Q0001 — How would you inventory the pinned Shopizer backend, Angular admin and React storefront repositories and distinguish their actual deployment and runtime boundaries?

- [ ] **Q0001 — How would you inventory the pinned Shopizer backend, Angular admin and React storefront repositories and distinguish their actual deployment and runtime boundaries?**
  - **Acceptance:** Create docs/architecture/repository-inventory.md listing repo URL, pinned SHA, languages, entrypoints, build commands, main modules and generated artifacts.
  - **Verify:** Show each repository's top-level tree; do not assume five Maven modules are five microservices.
  - **Failure to avoid:** Treating files in the backend repository as deployed frontend applications.
  - **Prerequisite:** None.

## Q0002 — How would you trace a real user request from product search through cart, checkout, payment and final order confirmation across frontend, REST, domain services and persistence?

- [ ] **Q0002 — How would you trace a real user request from product search through cart, checkout, payment and final order confirmation across frontend, REST, domain services and persistence?**
  - **Acceptance:** Draw docs/architecture/purchase-flow.md with request URLs, ownership boundaries, database writes, external callbacks and alternative failure paths.
  - **Verify:** Trace a guest and authenticated purchase; identify where checkout can fail or be retried.
  - **Failure to avoid:** Skipping webhook timing, client-controlled prices or inventory races.
  - **Prerequisite:** Q0001.

## Q0003 — How would you reconstruct the Maven reactor and the dependency graph for sm-core-model, sm-core-modules, sm-core, sm-shop-model and sm-shop?

- [ ] **Q0003 — How would you reconstruct the Maven reactor and the dependency graph for sm-core-model, sm-core-modules, sm-core, sm-shop-model and sm-shop?**
  - **Acceptance:** Create a module graph with parent POM, dependency direction, bootstrap module, shared classes and example imports.
  - **Verify:** Use actual pinned pom.xml files; show how one API endpoint reaches the core service.
  - **Failure to avoid:** Mistaking module dependencies for independent service deployments.
  - **Prerequisite:** Q0001.

## Q0004 — How would you classify the pinned source code into entity/model, repository, service, facade, DTO, mapper, controller/API, integration and security layers?

- [ ] **Q0004 — How would you classify the pinned source code into entity/model, repository, service, facade, DTO, mapper, controller/API, integration and security layers?**
  - **Acceptance:** Publish docs/architecture/layer-map.md with at least one actual source path, responsibility and example interaction per layer.
  - **Verify:** Locate representative Java files and explain the call chain without copy-pasting an entire class.
  - **Failure to avoid:** Leaking JPA entities directly into public REST responses.
  - **Prerequisite:** Q0001.

## Q0005 — How would you design our own Java 21 e-commerce architecture while preserving Shopizer's core business capabilities without blindly copying outdated Spring configuration?

- [ ] **Q0005 — How would you design our own Java 21 e-commerce architecture while preserving Shopizer's core business capabilities without blindly copying outdated Spring configuration?**
  - **Acceptance:** Record a proposed parent Maven project, module boundaries, Java 21 configuration and compatible Spring Boot/Jakarta migration decision.
  - **Verify:** Explain old pom.xml Java/Spring settings versus proposed replacement and verify available dependency compatibility.
  - **Failure to avoid:** Unreviewed replacement of javax classes or outdated authentication libraries.
  - **Prerequisite:** Q0001.

## Q0006 — How would you derive an initial relational ER diagram connecting merchant stores, users, customers, categories, products, variants, inventory, carts, payments and orders?

- [ ] **Q0006 — How would you derive an initial relational ER diagram connecting merchant stores, users, customers, categories, products, variants, inventory, carts, payments and orders?**
  - **Acceptance:** Draw entities, primary keys, foreign keys, unique constraints, cardinality and one important invariant for each aggregate.
  - **Verify:** Walk through an example customer ordering a SKU and explain historical order line snapshots.
  - **Failure to avoid:** Insufficient tenant isolation, duplicate SKU, orphaned rows or mutable order history.
  - **Prerequisite:** Q0001.

## Q0007 — How would you establish consistent REST contracts for catalog, customer, cart, checkout, payment and order APIs before writing controllers?

- [ ] **Q0007 — How would you establish consistent REST contracts for catalog, customer, cart, checkout, payment and order APIs before writing controllers?**
  - **Acceptance:** Document route naming, versions, request/response DTOs, HTTP status/error envelope, pagination and authorization defaults.
  - **Verify:** Provide example JSON for success, validation error and access-denied responses.
  - **Failure to avoid:** Using ambiguous PUT/PATCH rules or changing routes without compatibility tests.
  - **Prerequisite:** Q0001.

## Q0008 — How would you define domain boundaries and ownership invariants for merchants, catalog, pricing, inventory, customer identity, carts and orders?

- [ ] **Q0008 — How would you define domain boundaries and ownership invariants for merchants, catalog, pricing, inventory, customer identity, carts and orders?**
  - **Acceptance:** Produce a bounded-context map specifying who can mutate each resource, transaction boundaries and consistency requirements.
  - **Verify:** Explain why cross-merchant reads/writes must fail, and which data is snapshotted at checkout.
  - **Failure to avoid:** Using client-supplied merchant IDs without authorization.
  - **Prerequisite:** Q0001.

## Q0009 — How would you inventory Shopizer's external integrations and decide which adapters should be mocked, sandboxed or deferred during incremental development?

- [ ] **Q0009 — How would you inventory Shopizer's external integrations and decide which adapters should be mocked, sandboxed or deferred during incremental development?**
  - **Acceptance:** List payment, shipping, object storage, email, search, geo/location and caches with credentials, failure and rate-limit policies.
  - **Verify:** Separate must-have local adapters from later external services and record test credentials handling.
  - **Failure to avoid:** Real payments, hardcoded secrets or dependence on unavailable services for early tasks.
  - **Prerequisite:** Q0001.

## Q0010 — How would you inspect the pinned backend commit history and convert real historical fixes into targeted regression questions and tests?

- [ ] **Q0010 — How would you inspect the pinned backend commit history and convert real historical fixes into targeted regression questions and tests?**
  - **Acceptance:** Create a commit-to-risk table covering the SKU existence query, slug routing, API compatibility, Jackson dependency fixes and Maven version rollback.
  - **Verify:** Link real commit URLs and state the failure, intended regression test and owning future phase.
  - **Failure to avoid:** Assuming the 54-commit branch history is the application's original complete development history.
  - **Prerequisite:** Q0001.

## Q0011 — How would you define a verifiable Definition of Done for every future question so that compiling code, database migrations, error paths and test evidence cannot be skipped?

- [ ] **Q0011 — How would you define a verifiable Definition of Done for every future question so that compiling code, database migrations, error paths and test evidence cannot be skipped?**
  - **Acceptance:** Specify mandatory code/files, build command, test command, expected output, security checks, traceable commit SHA and learner confirmation.
  - **Verify:** Demonstrate the checklist on one planned product API and one frontend screen.
  - **Failure to avoid:** Marking a feature completed after only describing it or generating MCQs.
  - **Prerequisite:** Q0001–Q0010.

## Q0012 — How would you operationalize a living question bank that supports new prerequisites, moving tasks, splitting oversized questions and preserving previously completed work?

- [ ] **Q0012 — How would you operationalize a living question bank that supports new prerequisites, moving tasks, splitting oversized questions and preserving previously completed work?**
  - **Acceptance:** Review ID allocation Q0001–Q1025, next ID Q1026, baseline phase files, PROGRESS.csv, execution overrides, change log and CI validator.
  - **Verify:** Run the roadmap validator and perform a dry-run change proposal without assigning false completion.
  - **Failure to avoid:** Renumbering IDs, losing completed evidence or inserting a redundant task.
  - **Prerequisite:** Q0001–Q0011.

