# Phase 13 — Inventory and availability

**Tasks:** 34 · **Range:** Q0424–Q0457 · **Status:** NOT STARTED

**Shopizer reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core

Each item is an original, independently verifiable build/interview task. MCQ lessons and implementation commits are added only when tackled.


## inventory records and stock semantics

- [ ] **Q0424 — How would you design inventory records and stock semantics with explicit contracts for on-hand, reserved, available and backorder quantities?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** negative stock or inconsistent totals.
  - **Proof focus:** inventory invariants after updates.

- [ ] **Q0425 — How would you implement inventory records and stock semantics from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** negative stock or inconsistent totals.
  - **Proof focus:** inventory invariants after updates.

- [ ] **Q0426 — How would you connect inventory records and stock semantics across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** negative stock or inconsistent totals.
  - **Proof focus:** inventory invariants after updates.

- [ ] **Q0427 — How would you handle negative stock or inconsistent totals in inventory records and stock semantics without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** negative stock or inconsistent totals.
  - **Proof focus:** inventory invariants after updates.

- [ ] **Q0428 — How would you prove inventory records and stock semantics is correct with inventory invariants after updates and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** negative stock or inconsistent totals.
  - **Proof focus:** inventory invariants after updates.


## stock receiving and adjustment operations

- [ ] **Q0429 — How would you design stock receiving and adjustment operations with explicit contracts for reason codes, ledger entries and adjustment author?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** lost adjustment or missing audit trail.
  - **Proof focus:** increment/decrement and audit entries.

- [ ] **Q0430 — How would you implement stock receiving and adjustment operations from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** lost adjustment or missing audit trail.
  - **Proof focus:** increment/decrement and audit entries.

- [ ] **Q0431 — How would you connect stock receiving and adjustment operations across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** lost adjustment or missing audit trail.
  - **Proof focus:** increment/decrement and audit entries.

- [ ] **Q0432 — How would you handle lost adjustment or missing audit trail in stock receiving and adjustment operations without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** lost adjustment or missing audit trail.
  - **Proof focus:** increment/decrement and audit entries.

- [ ] **Q0433 — How would you prove stock receiving and adjustment operations is correct with increment/decrement and audit entries and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** lost adjustment or missing audit trail.
  - **Proof focus:** increment/decrement and audit entries.


## inventory availability endpoints

- [ ] **Q0434 — How would you design inventory availability endpoints with explicit contracts for product and variant availability by store?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** stale response to out-of-stock requests.
  - **Proof focus:** HTTP tests at zero available.

- [ ] **Q0435 — How would you implement inventory availability endpoints from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** stale response to out-of-stock requests.
  - **Proof focus:** HTTP tests at zero available.

- [ ] **Q0436 — How would you connect inventory availability endpoints across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** stale response to out-of-stock requests.
  - **Proof focus:** HTTP tests at zero available.

- [ ] **Q0437 — How would you handle stale response to out-of-stock requests in inventory availability endpoints without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** stale response to out-of-stock requests.
  - **Proof focus:** HTTP tests at zero available.

- [ ] **Q0438 — How would you prove inventory availability endpoints is correct with HTTP tests at zero available and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** stale response to out-of-stock requests.
  - **Proof focus:** HTTP tests at zero available.


## optimistic locking for inventory

- [ ] **Q0439 — How would you design optimistic locking for inventory with explicit contracts for entity versioning, conflict retries and boundaries?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** simultaneous last-item purchases.
  - **Proof focus:** concurrent reservation with no oversell.

- [ ] **Q0440 — How would you implement optimistic locking for inventory from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** simultaneous last-item purchases.
  - **Proof focus:** concurrent reservation with no oversell.

- [ ] **Q0441 — How would you connect optimistic locking for inventory across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** simultaneous last-item purchases.
  - **Proof focus:** concurrent reservation with no oversell.

- [ ] **Q0442 — How would you handle simultaneous last-item purchases in optimistic locking for inventory without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** simultaneous last-item purchases.
  - **Proof focus:** concurrent reservation with no oversell.

- [ ] **Q0443 — How would you prove optimistic locking for inventory is correct with concurrent reservation with no oversell and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** simultaneous last-item purchases.
  - **Proof focus:** concurrent reservation with no oversell.


## stock reservation and release

- [ ] **Q0444 — How would you design stock reservation and release with explicit contracts for cart/checkout reservation lifetime and release triggers?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** expired checkout leaves stock reserved.
  - **Proof focus:** reserve, confirm and timeout recovery.

- [ ] **Q0445 — How would you implement stock reservation and release from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** expired checkout leaves stock reserved.
  - **Proof focus:** reserve, confirm and timeout recovery.

- [ ] **Q0446 — How would you connect stock reservation and release across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** expired checkout leaves stock reserved.
  - **Proof focus:** reserve, confirm and timeout recovery.

- [ ] **Q0447 — How would you handle expired checkout leaves stock reserved in stock reservation and release without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** expired checkout leaves stock reserved.
  - **Proof focus:** reserve, confirm and timeout recovery.

- [ ] **Q0448 — How would you prove stock reservation and release is correct with reserve, confirm and timeout recovery and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** expired checkout leaves stock reserved.
  - **Proof focus:** reserve, confirm and timeout recovery.


## oversell and backorder policy

- [ ] **Q0449 — How would you design oversell and backorder policy with explicit contracts for per-item rules, thresholds and alerts?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** selling items beyond configured policy.
  - **Proof focus:** backorder enabled/disabled scenarios.

- [ ] **Q0450 — How would you implement oversell and backorder policy from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** selling items beyond configured policy.
  - **Proof focus:** backorder enabled/disabled scenarios.

- [ ] **Q0451 — How would you connect oversell and backorder policy across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** selling items beyond configured policy.
  - **Proof focus:** backorder enabled/disabled scenarios.

- [ ] **Q0452 — How would you handle selling items beyond configured policy in oversell and backorder policy without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** selling items beyond configured policy.
  - **Proof focus:** backorder enabled/disabled scenarios.

- [ ] **Q0453 — How would you prove oversell and backorder policy is correct with backorder enabled/disabled scenarios and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** selling items beyond configured policy.
  - **Proof focus:** backorder enabled/disabled scenarios.


## inventory reconciliation and monitoring

- [ ] **Q0454 — How would you design inventory reconciliation and monitoring with explicit contracts for adjustment reconciliation, alerts and audit reports?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** stock drift from orders and returns.
  - **Proof focus:** count reconciliation after canceled order.

- [ ] **Q0455 — How would you implement inventory reconciliation and monitoring from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** stock drift from orders and returns.
  - **Proof focus:** count reconciliation after canceled order.

- [ ] **Q0456 — How would you connect inventory reconciliation and monitoring across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** stock drift from orders and returns.
  - **Proof focus:** count reconciliation after canceled order.

- [ ] **Q0457 — How would you handle stock drift from orders and returns in inventory reconciliation and monitoring without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** stock drift from orders and returns.
  - **Proof focus:** count reconciliation after canceled order.
