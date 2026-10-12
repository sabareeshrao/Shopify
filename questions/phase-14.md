# Phase 14 — Product search, filters and indexing

**Tasks:** 36 · **Range:** Q0458–Q0493 · **Status:** NOT STARTED

**Shopizer reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop

Each item is an original, independently verifiable build/interview task. MCQ lessons and implementation commits are added only when tackled.


## SQL-backed initial product search

- [ ] **Q0458 — How would you design SQL-backed initial product search with explicit contracts for tokenization, LIKE limits, normalized search fields?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** slow unbounded wildcard search.
  - **Proof focus:** query plan and paginated search.

- [ ] **Q0459 — How would you implement SQL-backed initial product search from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** slow unbounded wildcard search.
  - **Proof focus:** query plan and paginated search.

- [ ] **Q0460 — How would you connect SQL-backed initial product search across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** slow unbounded wildcard search.
  - **Proof focus:** query plan and paginated search.

- [ ] **Q0461 — How would you handle slow unbounded wildcard search in SQL-backed initial product search without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** slow unbounded wildcard search.
  - **Proof focus:** query plan and paginated search.

- [ ] **Q0462 — How would you prove SQL-backed initial product search is correct with query plan and paginated search and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** slow unbounded wildcard search.
  - **Proof focus:** query plan and paginated search.

- [ ] **Q0463 — How would you evaluate performance, security and backward compatibility of SQL-backed initial product search before approving the implementation?**
  - **Acceptance:** Recorded technical tradeoffs and a regression test.
  - **Edge case:** slow unbounded wildcard search.
  - **Proof focus:** query plan and paginated search.


## filterable product listing

- [ ] **Q0464 — How would you design filterable product listing with explicit contracts for merchant, category, price range and availability filters?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** filter injection or wrong tenant results.
  - **Proof focus:** combinatorial filter test cases.

- [ ] **Q0465 — How would you implement filterable product listing from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** filter injection or wrong tenant results.
  - **Proof focus:** combinatorial filter test cases.

- [ ] **Q0466 — How would you connect filterable product listing across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** filter injection or wrong tenant results.
  - **Proof focus:** combinatorial filter test cases.

- [ ] **Q0467 — How would you handle filter injection or wrong tenant results in filterable product listing without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** filter injection or wrong tenant results.
  - **Proof focus:** combinatorial filter test cases.

- [ ] **Q0468 — How would you prove filterable product listing is correct with combinatorial filter test cases and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** filter injection or wrong tenant results.
  - **Proof focus:** combinatorial filter test cases.


## stable sort and pagination

- [ ] **Q0469 — How would you design stable sort and pagination with explicit contracts for sort whitelist, keyset/offset decisions and total counts?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** duplicate records across pages.
  - **Proof focus:** page stability during concurrent inserts.

- [ ] **Q0470 — How would you implement stable sort and pagination from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** duplicate records across pages.
  - **Proof focus:** page stability during concurrent inserts.

- [ ] **Q0471 — How would you connect stable sort and pagination across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** duplicate records across pages.
  - **Proof focus:** page stability during concurrent inserts.

- [ ] **Q0472 — How would you handle duplicate records across pages in stable sort and pagination without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** duplicate records across pages.
  - **Proof focus:** page stability during concurrent inserts.

- [ ] **Q0473 — How would you prove stable sort and pagination is correct with page stability during concurrent inserts and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** duplicate records across pages.
  - **Proof focus:** page stability during concurrent inserts.


## search response DTOs

- [ ] **Q0474 — How would you design search response DTOs with explicit contracts for facets, highlights, counts and user-selected filters?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** empty result or invalid sort field.
  - **Proof focus:** search schema contract tests.

- [ ] **Q0475 — How would you implement search response DTOs from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** empty result or invalid sort field.
  - **Proof focus:** search schema contract tests.

- [ ] **Q0476 — How would you connect search response DTOs across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** empty result or invalid sort field.
  - **Proof focus:** search schema contract tests.

- [ ] **Q0477 — How would you handle empty result or invalid sort field in search response DTOs without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** empty result or invalid sort field.
  - **Proof focus:** search schema contract tests.

- [ ] **Q0478 — How would you prove search response DTOs is correct with search schema contract tests and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** empty result or invalid sort field.
  - **Proof focus:** search schema contract tests.


## dedicated search index integration

- [ ] **Q0479 — How would you design dedicated search index integration with explicit contracts for index mappings and application-to-index sync?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** index out of service or stale documents.
  - **Proof focus:** index/reindex integration scenarios.

- [ ] **Q0480 — How would you implement dedicated search index integration from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** index out of service or stale documents.
  - **Proof focus:** index/reindex integration scenarios.

- [ ] **Q0481 — How would you connect dedicated search index integration across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** index out of service or stale documents.
  - **Proof focus:** index/reindex integration scenarios.

- [ ] **Q0482 — How would you handle index out of service or stale documents in dedicated search index integration without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** index out of service or stale documents.
  - **Proof focus:** index/reindex integration scenarios.

- [ ] **Q0483 — How would you prove dedicated search index integration is correct with index/reindex integration scenarios and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** index out of service or stale documents.
  - **Proof focus:** index/reindex integration scenarios.


## slug-based discovery and routing

- [ ] **Q0484 — How would you design slug-based discovery and routing with explicit contracts for friendly URLs, redirects and duplicate slug policy?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** renamed slug breaking bookmarks.
  - **Proof focus:** old and new URL tests.

- [ ] **Q0485 — How would you implement slug-based discovery and routing from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** renamed slug breaking bookmarks.
  - **Proof focus:** old and new URL tests.

- [ ] **Q0486 — How would you connect slug-based discovery and routing across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** renamed slug breaking bookmarks.
  - **Proof focus:** old and new URL tests.

- [ ] **Q0487 — How would you handle renamed slug breaking bookmarks in slug-based discovery and routing without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** renamed slug breaking bookmarks.
  - **Proof focus:** old and new URL tests.

- [ ] **Q0488 — How would you prove slug-based discovery and routing is correct with old and new URL tests and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** renamed slug breaking bookmarks.
  - **Proof focus:** old and new URL tests.


## search relevance and tuning

- [ ] **Q0489 — How would you design search relevance and tuning with explicit contracts for synonyms, boosting, typo handling and metrics?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** irrelevant top results or runaway cost.
  - **Proof focus:** measured relevance evaluation set.

- [ ] **Q0490 — How would you implement search relevance and tuning from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** irrelevant top results or runaway cost.
  - **Proof focus:** measured relevance evaluation set.

- [ ] **Q0491 — How would you connect search relevance and tuning across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** irrelevant top results or runaway cost.
  - **Proof focus:** measured relevance evaluation set.

- [ ] **Q0492 — How would you handle irrelevant top results or runaway cost in search relevance and tuning without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** irrelevant top results or runaway cost.
  - **Proof focus:** measured relevance evaluation set.

- [ ] **Q0493 — How would you prove search relevance and tuning is correct with measured relevance evaluation set and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** irrelevant top results or runaway cost.
  - **Proof focus:** measured relevance evaluation set.
