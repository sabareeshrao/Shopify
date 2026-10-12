# Phase 03 — MySQL, JPA and persistence foundations

**Canonical IDs:** Q0059 onward · **Planned tasks:** 32 · **Status:** NOT STARTED

**Reference area:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core

Questions are development tasks, not MCQ answers. Implementation generates separate MCQs later. A checked box must have code/artifact evidence and an updated tracker.


## MySQL schema and connection pool

- [ ] **Q0059 — How would you design MySQL schema and connection pool including connection URL, HikariCP sizing and least-privilege credentials, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** connection exhaustion and invalid timezone encoding.
  - **Proof focus:** database health check and connection failure recovery.

- [ ] **Q0060 — How would you implement MySQL schema and connection pool in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** connection exhaustion and invalid timezone encoding.
  - **Proof focus:** database health check and connection failure recovery.

- [ ] **Q0061 — How would you connect MySQL schema and connection pool through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** connection exhaustion and invalid timezone encoding.
  - **Proof focus:** database health check and connection failure recovery.

- [ ] **Q0062 — How would you handle connection exhaustion and invalid timezone encoding in MySQL schema and connection pool without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** connection exhaustion and invalid timezone encoding.
  - **Proof focus:** database health check and connection failure recovery.

- [ ] **Q0063 — How would you prove MySQL schema and connection pool works by testing database health check and connection failure recovery, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** connection exhaustion and invalid timezone encoding.
  - **Proof focus:** database health check and connection failure recovery.


## versioned database migrations

- [ ] **Q0064 — How would you design versioned database migrations including Flyway or Liquibase baseline, constraints and repeatable environment setup, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** migration checksum mismatch or incompatible schema.
  - **Proof focus:** empty-database bootstrap and repeated migration run.

- [ ] **Q0065 — How would you implement versioned database migrations in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** migration checksum mismatch or incompatible schema.
  - **Proof focus:** empty-database bootstrap and repeated migration run.

- [ ] **Q0066 — How would you connect versioned database migrations through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** migration checksum mismatch or incompatible schema.
  - **Proof focus:** empty-database bootstrap and repeated migration run.

- [ ] **Q0067 — How would you handle migration checksum mismatch or incompatible schema in versioned database migrations without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** migration checksum mismatch or incompatible schema.
  - **Proof focus:** empty-database bootstrap and repeated migration run.

- [ ] **Q0068 — How would you prove versioned database migrations works by testing empty-database bootstrap and repeated migration run, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** migration checksum mismatch or incompatible schema.
  - **Proof focus:** empty-database bootstrap and repeated migration run.


## JPA entity identity and lifecycle

- [ ] **Q0069 — How would you design JPA entity identity and lifecycle including primary keys, generation strategy, dirty checking and entity states, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** detached entities and accidental overwrites.
  - **Proof focus:** persist, load and update integration tests.

- [ ] **Q0070 — How would you implement JPA entity identity and lifecycle in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** detached entities and accidental overwrites.
  - **Proof focus:** persist, load and update integration tests.

- [ ] **Q0071 — How would you connect JPA entity identity and lifecycle through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** detached entities and accidental overwrites.
  - **Proof focus:** persist, load and update integration tests.

- [ ] **Q0072 — How would you handle detached entities and accidental overwrites in JPA entity identity and lifecycle without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** detached entities and accidental overwrites.
  - **Proof focus:** persist, load and update integration tests.

- [ ] **Q0073 — How would you prove JPA entity identity and lifecycle works by testing persist, load and update integration tests, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** detached entities and accidental overwrites.
  - **Proof focus:** persist, load and update integration tests.


## commerce entity relationships

- [ ] **Q0074 — How would you design commerce entity relationships including one-to-many, many-to-one, join tables, cascades and ownership, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** orphan deletion and circular serialization.
  - **Proof focus:** relationship integration tests with real MySQL.

- [ ] **Q0075 — How would you implement commerce entity relationships in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** orphan deletion and circular serialization.
  - **Proof focus:** relationship integration tests with real MySQL.

- [ ] **Q0076 — How would you connect commerce entity relationships through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** orphan deletion and circular serialization.
  - **Proof focus:** relationship integration tests with real MySQL.

- [ ] **Q0077 — How would you handle orphan deletion and circular serialization in commerce entity relationships without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** orphan deletion and circular serialization.
  - **Proof focus:** relationship integration tests with real MySQL.

- [ ] **Q0078 — How would you prove commerce entity relationships works by testing relationship integration tests with real MySQL, including a positive and negative case?**
  - **Acceptance:** Automated tests passing against appropriate dependencies.
  - **Edge/failure to consider:** orphan deletion and circular serialization.
  - **Proof focus:** relationship integration tests with real MySQL.


## Spring Data repository queries

- [ ] **Q0079 — How would you design Spring Data repository queries including derived queries, JPQL, projections and pagination, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** N+1 query or incorrect count query.
  - **Proof focus:** repository tests for filtering and paging.

- [ ] **Q0080 — How would you implement Spring Data repository queries in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** N+1 query or incorrect count query.
  - **Proof focus:** repository tests for filtering and paging.

- [ ] **Q0081 — How would you connect Spring Data repository queries through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** N+1 query or incorrect count query.
  - **Proof focus:** repository tests for filtering and paging.

- [ ] **Q0082 — How would you handle N+1 query or incorrect count query in Spring Data repository queries without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** N+1 query or incorrect count query.
  - **Proof focus:** repository tests for filtering and paging.


## transactional service boundaries

- [ ] **Q0083 — How would you design transactional service boundaries including Spring @Transactional, isolation, rollback and optimistic locking, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** self-invocation, checked exceptions and lost update.
  - **Proof focus:** simulated rollback and concurrent update test.

- [ ] **Q0084 — How would you implement transactional service boundaries in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** self-invocation, checked exceptions and lost update.
  - **Proof focus:** simulated rollback and concurrent update test.

- [ ] **Q0085 — How would you connect transactional service boundaries through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** self-invocation, checked exceptions and lost update.
  - **Proof focus:** simulated rollback and concurrent update test.

- [ ] **Q0086 — How would you handle self-invocation, checked exceptions and lost update in transactional service boundaries without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** self-invocation, checked exceptions and lost update.
  - **Proof focus:** simulated rollback and concurrent update test.


## SQL optimization and persistence diagnostics

- [ ] **Q0087 — How would you design SQL optimization and persistence diagnostics including indexes, explain plans, query logging and connection tracing, with clearly documented data contracts and invariants?**
  - **Acceptance:** Data model/interface design and explicit invariants.
  - **Edge/failure to consider:** slow scans, oversized fetches and hot locks.
  - **Proof focus:** before/after query plan and measured latency.

- [ ] **Q0088 — How would you implement SQL optimization and persistence diagnostics in the correct Java module, with compilable code and clear dependency boundaries?**
  - **Acceptance:** Compiling production code and a visible file-by-file build sequence.
  - **Edge/failure to consider:** slow scans, oversized fetches and hot locks.
  - **Proof focus:** before/after query plan and measured latency.

- [ ] **Q0089 — How would you connect SQL optimization and persistence diagnostics through repository, service and API layers, including real persisted data rather than mock responses?**
  - **Acceptance:** Working end-to-end request or service call with expected result.
  - **Edge/failure to consider:** slow scans, oversized fetches and hot locks.
  - **Proof focus:** before/after query plan and measured latency.

- [ ] **Q0090 — How would you handle slow scans, oversized fetches and hot locks in SQL optimization and persistence diagnostics without corrupting data or leaking internal implementation details?**
  - **Acceptance:** Reproducible failure case, explicit error behavior and safe state.
  - **Edge/failure to consider:** slow scans, oversized fetches and hot locks.
  - **Proof focus:** before/after query plan and measured latency.
