# Phase 16 — Shopping cart and price calculations

**Tasks:** 34 · **IDs:** Q0534–Q0567 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Each numbered question is a standalone implementation checkpoint. Preserve IDs on edits and record evidence before checking a task.


## guest shopping cart model

- [ ] **Q0534 — How would you design guest shopping cart model with rules for anonymous cart identifiers, expiry and persistence and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** guessable cart token.
  - **Verify:** guest cart survives session.

- [ ] **Q0535 — How would you implement guest shopping cart model in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** guessable cart token.
  - **Verify:** guest cart survives session.

- [ ] **Q0536 — How would you expose and connect guest shopping cart model through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** guessable cart token.
  - **Verify:** guest cart survives session.

- [ ] **Q0537 — How would you handle guessable cart token while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** guessable cart token.
  - **Verify:** guest cart survives session.

- [ ] **Q0538 — How would you prove guest shopping cart model with guest cart survives session using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** guessable cart token.
  - **Verify:** guest cart survives session.


## authenticated customer cart

- [ ] **Q0539 — How would you design authenticated customer cart with rules for customer ownership and list/detail operations and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** customer accessing another cart.
  - **Verify:** owner-only cart retrieval.

- [ ] **Q0540 — How would you implement authenticated customer cart in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** customer accessing another cart.
  - **Verify:** owner-only cart retrieval.

- [ ] **Q0541 — How would you expose and connect authenticated customer cart through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** customer accessing another cart.
  - **Verify:** owner-only cart retrieval.

- [ ] **Q0542 — How would you handle customer accessing another cart while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** customer accessing another cart.
  - **Verify:** owner-only cart retrieval.

- [ ] **Q0543 — How would you prove authenticated customer cart with owner-only cart retrieval using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** customer accessing another cart.
  - **Verify:** owner-only cart retrieval.


## add item and adjust quantities

- [ ] **Q0544 — How would you design add item and adjust quantities with rules for product/variant validation and quantity bounds and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** negative quantity or nonexistent SKU.
  - **Verify:** item add and quantity update.

- [ ] **Q0545 — How would you implement add item and adjust quantities in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** negative quantity or nonexistent SKU.
  - **Verify:** item add and quantity update.

- [ ] **Q0546 — How would you expose and connect add item and adjust quantities through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** negative quantity or nonexistent SKU.
  - **Verify:** item add and quantity update.

- [ ] **Q0547 — How would you handle negative quantity or nonexistent SKU while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** negative quantity or nonexistent SKU.
  - **Verify:** item add and quantity update.

- [ ] **Q0548 — How would you prove add item and adjust quantities with item add and quantity update using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** negative quantity or nonexistent SKU.
  - **Verify:** item add and quantity update.


## cart item removal and clearing

- [ ] **Q0549 — How would you design cart item removal and clearing with rules for remove/delete semantics and re-evaluation and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** removed item still affects totals.
  - **Verify:** empty cart and state persistence.

- [ ] **Q0550 — How would you implement cart item removal and clearing in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** removed item still affects totals.
  - **Verify:** empty cart and state persistence.

- [ ] **Q0551 — How would you expose and connect cart item removal and clearing through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** removed item still affects totals.
  - **Verify:** empty cart and state persistence.

- [ ] **Q0552 — How would you handle removed item still affects totals while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** removed item still affects totals.
  - **Verify:** empty cart and state persistence.

- [ ] **Q0553 — How would you prove cart item removal and clearing with empty cart and state persistence using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** removed item still affects totals.
  - **Verify:** empty cart and state persistence.


## guest-to-customer cart merge

- [ ] **Q0554 — How would you design guest-to-customer cart merge with rules for merge decisions and duplicate variant rules and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** lost items or double-counted quantity.
  - **Verify:** login merge scenarios.

- [ ] **Q0555 — How would you implement guest-to-customer cart merge in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** lost items or double-counted quantity.
  - **Verify:** login merge scenarios.

- [ ] **Q0556 — How would you expose and connect guest-to-customer cart merge through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** lost items or double-counted quantity.
  - **Verify:** login merge scenarios.

- [ ] **Q0557 — How would you handle lost items or double-counted quantity while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** lost items or double-counted quantity.
  - **Verify:** login merge scenarios.

- [ ] **Q0558 — How would you prove guest-to-customer cart merge with login merge scenarios using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** lost items or double-counted quantity.
  - **Verify:** login merge scenarios.


## cart pricing and line calculations

- [ ] **Q0559 — How would you design cart pricing and line calculations with rules for snapshot versus current price and promotions and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** stale sale price or invalid currency.
  - **Verify:** recalculation and precision tests.

- [ ] **Q0560 — How would you implement cart pricing and line calculations in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** stale sale price or invalid currency.
  - **Verify:** recalculation and precision tests.

- [ ] **Q0561 — How would you expose and connect cart pricing and line calculations through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** stale sale price or invalid currency.
  - **Verify:** recalculation and precision tests.

- [ ] **Q0562 — How would you handle stale sale price or invalid currency while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** stale sale price or invalid currency.
  - **Verify:** recalculation and precision tests.

- [ ] **Q0563 — How would you prove cart pricing and line calculations with recalculation and precision tests using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** stale sale price or invalid currency.
  - **Verify:** recalculation and precision tests.


## cart expiration and checkout handoff

- [ ] **Q0564 — How would you design cart expiration and checkout handoff with rules for TTL, lifecycle and optimistic state version and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** cart changes during checkout.
  - **Verify:** expired cart and concurrent update.

- [ ] **Q0565 — How would you implement cart expiration and checkout handoff in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** cart changes during checkout.
  - **Verify:** expired cart and concurrent update.

- [ ] **Q0566 — How would you expose and connect cart expiration and checkout handoff through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** cart changes during checkout.
  - **Verify:** expired cart and concurrent update.

- [ ] **Q0567 — How would you handle cart changes during checkout while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** cart changes during checkout.
  - **Verify:** expired cart and concurrent update.
