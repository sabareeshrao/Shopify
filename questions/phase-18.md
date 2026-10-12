# Phase 18 — Tax, currency and totals calculation

**Tasks:** 30 · **IDs:** Q0600–Q0629 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Each numbered question is a standalone implementation checkpoint. Preserve IDs on edits and record evidence before checking a task.


## tax class and rate entities

- [ ] **Q0600 — How would you design tax class and rate entities with rules for jurisdiction, category applicability and effective date and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** overlapping or missing tax rule.
  - **Verify:** rate lookup by region.

- [ ] **Q0601 — How would you implement tax class and rate entities in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** overlapping or missing tax rule.
  - **Verify:** rate lookup by region.

- [ ] **Q0602 — How would you expose and connect tax class and rate entities through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** overlapping or missing tax rule.
  - **Verify:** rate lookup by region.

- [ ] **Q0603 — How would you handle overlapping or missing tax rule while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** overlapping or missing tax rule.
  - **Verify:** rate lookup by region.

- [ ] **Q0604 — How would you prove tax class and rate entities with rate lookup by region using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** overlapping or missing tax rule.
  - **Verify:** rate lookup by region.


## tax-inclusive versus tax-exclusive pricing

- [ ] **Q0605 — How would you design tax-inclusive versus tax-exclusive pricing with rules for calculation order and rounding conventions and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** double-counting embedded tax.
  - **Verify:** inclusive/exclusive worked examples.

- [ ] **Q0606 — How would you implement tax-inclusive versus tax-exclusive pricing in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** double-counting embedded tax.
  - **Verify:** inclusive/exclusive worked examples.

- [ ] **Q0607 — How would you expose and connect tax-inclusive versus tax-exclusive pricing through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** double-counting embedded tax.
  - **Verify:** inclusive/exclusive worked examples.

- [ ] **Q0608 — How would you handle double-counting embedded tax while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** double-counting embedded tax.
  - **Verify:** inclusive/exclusive worked examples.

- [ ] **Q0609 — How would you prove tax-inclusive versus tax-exclusive pricing with inclusive/exclusive worked examples using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** double-counting embedded tax.
  - **Verify:** inclusive/exclusive worked examples.


## order item and cart tax calculation

- [ ] **Q0610 — How would you design order item and cart tax calculation with rules for taxable basis after discounts and per-line rounding and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** penny drift across grouped items.
  - **Verify:** line-sum reconciles to total.

- [ ] **Q0611 — How would you implement order item and cart tax calculation in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** penny drift across grouped items.
  - **Verify:** line-sum reconciles to total.

- [ ] **Q0612 — How would you expose and connect order item and cart tax calculation through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** penny drift across grouped items.
  - **Verify:** line-sum reconciles to total.

- [ ] **Q0613 — How would you handle penny drift across grouped items while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** penny drift across grouped items.
  - **Verify:** line-sum reconciles to total.

- [ ] **Q0614 — How would you prove order item and cart tax calculation with line-sum reconciles to total using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** penny drift across grouped items.
  - **Verify:** line-sum reconciles to total.


## multi-currency display and conversion boundaries

- [ ] **Q0615 — How would you design multi-currency display and conversion boundaries with rules for store price currency, exchange input and transaction snapshot and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** mixing monetary values across currencies.
  - **Verify:** cross-currency invalid operations rejected.

- [ ] **Q0616 — How would you implement multi-currency display and conversion boundaries in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** mixing monetary values across currencies.
  - **Verify:** cross-currency invalid operations rejected.

- [ ] **Q0617 — How would you expose and connect multi-currency display and conversion boundaries through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** mixing monetary values across currencies.
  - **Verify:** cross-currency invalid operations rejected.

- [ ] **Q0618 — How would you handle mixing monetary values across currencies while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** mixing monetary values across currencies.
  - **Verify:** cross-currency invalid operations rejected.

- [ ] **Q0619 — How would you prove multi-currency display and conversion boundaries with cross-currency invalid operations rejected using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** mixing monetary values across currencies.
  - **Verify:** cross-currency invalid operations rejected.


## shipping tax and exemption policies

- [ ] **Q0620 — How would you design shipping tax and exemption policies with rules for taxable shipping flags and approved exemption data and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** unverified exemption accepted.
  - **Verify:** shipping taxed/untaxed tests.

- [ ] **Q0621 — How would you implement shipping tax and exemption policies in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** unverified exemption accepted.
  - **Verify:** shipping taxed/untaxed tests.

- [ ] **Q0622 — How would you expose and connect shipping tax and exemption policies through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** unverified exemption accepted.
  - **Verify:** shipping taxed/untaxed tests.

- [ ] **Q0623 — How would you handle unverified exemption accepted while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** unverified exemption accepted.
  - **Verify:** shipping taxed/untaxed tests.

- [ ] **Q0624 — How would you prove shipping tax and exemption policies with shipping taxed/untaxed tests using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** unverified exemption accepted.
  - **Verify:** shipping taxed/untaxed tests.


## order totals and calculation audit

- [ ] **Q0625 — How would you design order totals and calculation audit with rules for subtotal, discount, shipping, tax and payable total and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** negative payable or inconsistent calculations.
  - **Verify:** total invariants across checkout.

- [ ] **Q0626 — How would you implement order totals and calculation audit in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** negative payable or inconsistent calculations.
  - **Verify:** total invariants across checkout.

- [ ] **Q0627 — How would you expose and connect order totals and calculation audit through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** negative payable or inconsistent calculations.
  - **Verify:** total invariants across checkout.

- [ ] **Q0628 — How would you handle negative payable or inconsistent calculations while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** negative payable or inconsistent calculations.
  - **Verify:** total invariants across checkout.

- [ ] **Q0629 — How would you prove order totals and calculation audit with total invariants across checkout using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** negative payable or inconsistent calculations.
  - **Verify:** total invariants across checkout.
