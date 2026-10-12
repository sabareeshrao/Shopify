# Phase 12 — Prices, promotions and discounts

**Tasks:** 42 · **Range:** Q0382–Q0423 · **Status:** NOT STARTED

**Shopizer reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core

Each item is an original, independently verifiable build/interview task. MCQ lessons and implementation commits are added only when tackled.


## monetary value objects

- [ ] **Q0382 — How would you design monetary value objects with explicit contracts for BigDecimal, scale, rounding and currency identity?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** floating point precision loss.
  - **Proof focus:** tax/price arithmetic invariant tests.

- [ ] **Q0383 — How would you implement monetary value objects from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** floating point precision loss.
  - **Proof focus:** tax/price arithmetic invariant tests.

- [ ] **Q0384 — How would you connect monetary value objects across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** floating point precision loss.
  - **Proof focus:** tax/price arithmetic invariant tests.

- [ ] **Q0385 — How would you handle floating point precision loss in monetary value objects without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** floating point precision loss.
  - **Proof focus:** tax/price arithmetic invariant tests.

- [ ] **Q0386 — How would you prove monetary value objects is correct with tax/price arithmetic invariant tests and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** floating point precision loss.
  - **Proof focus:** tax/price arithmetic invariant tests.

- [ ] **Q0387 — How would you evaluate performance, security and backward compatibility of monetary value objects before approving the implementation?**
  - **Acceptance:** Recorded technical tradeoffs and a regression test.
  - **Edge case:** floating point precision loss.
  - **Proof focus:** tax/price arithmetic invariant tests.


## product base and special prices

- [ ] **Q0388 — How would you design product base and special prices with explicit contracts for price types, effective dates, store price policy?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** overlapping dates or negative price.
  - **Proof focus:** price changes by date.

- [ ] **Q0389 — How would you implement product base and special prices from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** overlapping dates or negative price.
  - **Proof focus:** price changes by date.

- [ ] **Q0390 — How would you connect product base and special prices across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** overlapping dates or negative price.
  - **Proof focus:** price changes by date.

- [ ] **Q0391 — How would you handle overlapping dates or negative price in product base and special prices without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** overlapping dates or negative price.
  - **Proof focus:** price changes by date.

- [ ] **Q0392 — How would you prove product base and special prices is correct with price changes by date and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** overlapping dates or negative price.
  - **Proof focus:** price changes by date.

- [ ] **Q0393 — How would you evaluate performance, security and backward compatibility of product base and special prices before approving the implementation?**
  - **Acceptance:** Recorded technical tradeoffs and a regression test.
  - **Edge case:** overlapping dates or negative price.
  - **Proof focus:** price changes by date.


## customer/quantity price tiers

- [ ] **Q0394 — How would you design customer/quantity price tiers with explicit contracts for tier priority, minimum quantity and eligible segments?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** tier conflict for same quantity.
  - **Proof focus:** price selected for boundary quantity.

- [ ] **Q0395 — How would you implement customer/quantity price tiers from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** tier conflict for same quantity.
  - **Proof focus:** price selected for boundary quantity.

- [ ] **Q0396 — How would you connect customer/quantity price tiers across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** tier conflict for same quantity.
  - **Proof focus:** price selected for boundary quantity.

- [ ] **Q0397 — How would you handle tier conflict for same quantity in customer/quantity price tiers without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** tier conflict for same quantity.
  - **Proof focus:** price selected for boundary quantity.

- [ ] **Q0398 — How would you prove customer/quantity price tiers is correct with price selected for boundary quantity and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** tier conflict for same quantity.
  - **Proof focus:** price selected for boundary quantity.


## coupon codes and redemption rules

- [ ] **Q0399 — How would you design coupon codes and redemption rules with explicit contracts for uniqueness, validity windows, usage caps and eligibility?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** double redemption under concurrency.
  - **Proof focus:** single-use redemption test.

- [ ] **Q0400 — How would you implement coupon codes and redemption rules from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** double redemption under concurrency.
  - **Proof focus:** single-use redemption test.

- [ ] **Q0401 — How would you connect coupon codes and redemption rules across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** double redemption under concurrency.
  - **Proof focus:** single-use redemption test.

- [ ] **Q0402 — How would you handle double redemption under concurrency in coupon codes and redemption rules without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** double redemption under concurrency.
  - **Proof focus:** single-use redemption test.

- [ ] **Q0403 — How would you prove coupon codes and redemption rules is correct with single-use redemption test and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** double redemption under concurrency.
  - **Proof focus:** single-use redemption test.


## order-level percentage and amount discounts

- [ ] **Q0404 — How would you design order-level percentage and amount discounts with explicit contracts for subtotals, limits, allocation and rounding?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** discount exceeds subtotal.
  - **Proof focus:** multi-item discount allocation test.

- [ ] **Q0405 — How would you implement order-level percentage and amount discounts from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** discount exceeds subtotal.
  - **Proof focus:** multi-item discount allocation test.

- [ ] **Q0406 — How would you connect order-level percentage and amount discounts across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** discount exceeds subtotal.
  - **Proof focus:** multi-item discount allocation test.

- [ ] **Q0407 — How would you handle discount exceeds subtotal in order-level percentage and amount discounts without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** discount exceeds subtotal.
  - **Proof focus:** multi-item discount allocation test.

- [ ] **Q0408 — How would you prove order-level percentage and amount discounts is correct with multi-item discount allocation test and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** discount exceeds subtotal.
  - **Proof focus:** multi-item discount allocation test.


## stacking and promotion conflict policy

- [ ] **Q0409 — How would you design stacking and promotion conflict policy with explicit contracts for promotion priority, exclusions and combinability?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** two promotions applied twice.
  - **Proof focus:** deterministic stacking examples.

- [ ] **Q0410 — How would you implement stacking and promotion conflict policy from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** two promotions applied twice.
  - **Proof focus:** deterministic stacking examples.

- [ ] **Q0411 — How would you connect stacking and promotion conflict policy across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** two promotions applied twice.
  - **Proof focus:** deterministic stacking examples.

- [ ] **Q0412 — How would you handle two promotions applied twice in stacking and promotion conflict policy without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** two promotions applied twice.
  - **Proof focus:** deterministic stacking examples.

- [ ] **Q0413 — How would you prove stacking and promotion conflict policy is correct with deterministic stacking examples and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** two promotions applied twice.
  - **Proof focus:** deterministic stacking examples.


## promotion evaluation service

- [ ] **Q0414 — How would you design promotion evaluation service with explicit contracts for rule inputs, extensibility and audit trail?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** stale cart pricing or conflicting rules.
  - **Proof focus:** price breakdown response.

- [ ] **Q0415 — How would you implement promotion evaluation service from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** stale cart pricing or conflicting rules.
  - **Proof focus:** price breakdown response.

- [ ] **Q0416 — How would you connect promotion evaluation service across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** stale cart pricing or conflicting rules.
  - **Proof focus:** price breakdown response.

- [ ] **Q0417 — How would you handle stale cart pricing or conflicting rules in promotion evaluation service without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** stale cart pricing or conflicting rules.
  - **Proof focus:** price breakdown response.

- [ ] **Q0418 — How would you prove promotion evaluation service is correct with price breakdown response and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** stale cart pricing or conflicting rules.
  - **Proof focus:** price breakdown response.


## discount security and merchant isolation

- [ ] **Q0419 — How would you design discount security and merchant isolation with explicit contracts for ownership of codes, admin permissions and replay?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** foreign merchant coupon accepted.
  - **Proof focus:** tenant-scope and abuse tests.

- [ ] **Q0420 — How would you implement discount security and merchant isolation from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** foreign merchant coupon accepted.
  - **Proof focus:** tenant-scope and abuse tests.

- [ ] **Q0421 — How would you connect discount security and merchant isolation across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** foreign merchant coupon accepted.
  - **Proof focus:** tenant-scope and abuse tests.

- [ ] **Q0422 — How would you handle foreign merchant coupon accepted in discount security and merchant isolation without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** foreign merchant coupon accepted.
  - **Proof focus:** tenant-scope and abuse tests.

- [ ] **Q0423 — How would you prove discount security and merchant isolation is correct with tenant-scope and abuse tests and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** foreign merchant coupon accepted.
  - **Proof focus:** tenant-scope and abuse tests.
