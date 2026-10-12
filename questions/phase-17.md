# Phase 17 — Shipping services, quotes and methods

**Tasks:** 32 · **IDs:** Q0568–Q0599 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-modules

Each numbered question is a standalone implementation checkpoint. Preserve IDs on edits and record evidence before checking a task.


## shipping address and service method model

- [ ] **Q0568 — How would you design shipping address and service method model with rules for region restrictions, delivery methods and eligibility and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** invalid postal code or unsupported destination.
  - **Verify:** method discovery by address.

- [ ] **Q0569 — How would you implement shipping address and service method model in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** invalid postal code or unsupported destination.
  - **Verify:** method discovery by address.

- [ ] **Q0570 — How would you expose and connect shipping address and service method model through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** invalid postal code or unsupported destination.
  - **Verify:** method discovery by address.

- [ ] **Q0571 — How would you handle invalid postal code or unsupported destination while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** invalid postal code or unsupported destination.
  - **Verify:** method discovery by address.

- [ ] **Q0572 — How would you prove shipping address and service method model with method discovery by address using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** invalid postal code or unsupported destination.
  - **Verify:** method discovery by address.


## package dimensions and shipping weights

- [ ] **Q0573 — How would you design package dimensions and shipping weights with rules for weight units, packaging and dimensional weight and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** mixed units or oversized parcel.
  - **Verify:** dimensional calculation tests.

- [ ] **Q0574 — How would you implement package dimensions and shipping weights in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** mixed units or oversized parcel.
  - **Verify:** dimensional calculation tests.

- [ ] **Q0575 — How would you expose and connect package dimensions and shipping weights through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** mixed units or oversized parcel.
  - **Verify:** dimensional calculation tests.

- [ ] **Q0576 — How would you handle mixed units or oversized parcel while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** mixed units or oversized parcel.
  - **Verify:** dimensional calculation tests.

- [ ] **Q0577 — How would you prove package dimensions and shipping weights with dimensional calculation tests using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** mixed units or oversized parcel.
  - **Verify:** dimensional calculation tests.


## flat-rate and zone shipping quotes

- [ ] **Q0578 — How would you design flat-rate and zone shipping quotes with rules for store policy, minimum spend and location rules and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** quote for unsupported zone.
  - **Verify:** zone boundary test.

- [ ] **Q0579 — How would you implement flat-rate and zone shipping quotes in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** quote for unsupported zone.
  - **Verify:** zone boundary test.

- [ ] **Q0580 — How would you expose and connect flat-rate and zone shipping quotes through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** quote for unsupported zone.
  - **Verify:** zone boundary test.

- [ ] **Q0581 — How would you handle quote for unsupported zone while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** quote for unsupported zone.
  - **Verify:** zone boundary test.

- [ ] **Q0582 — How would you prove flat-rate and zone shipping quotes with zone boundary test using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** quote for unsupported zone.
  - **Verify:** zone boundary test.


## distance- and weight-based shipping rules

- [ ] **Q0583 — How would you design distance- and weight-based shipping rules with rules for rate tables, mapping service abstraction and rounding and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** missing coordinates or invalid weight.
  - **Verify:** quoted rate example.

- [ ] **Q0584 — How would you implement distance- and weight-based shipping rules in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** missing coordinates or invalid weight.
  - **Verify:** quoted rate example.

- [ ] **Q0585 — How would you expose and connect distance- and weight-based shipping rules through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** missing coordinates or invalid weight.
  - **Verify:** quoted rate example.

- [ ] **Q0586 — How would you handle missing coordinates or invalid weight while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** missing coordinates or invalid weight.
  - **Verify:** quoted rate example.

- [ ] **Q0587 — How would you prove distance- and weight-based shipping rules with quoted rate example using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** missing coordinates or invalid weight.
  - **Verify:** quoted rate example.


## shipping provider integration interface

- [ ] **Q0588 — How would you design shipping provider integration interface with rules for carrier adapter contracts and credentials and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** provider timeout, quota or outage.
  - **Verify:** stubbed UPS/USPS quote response.

- [ ] **Q0589 — How would you implement shipping provider integration interface in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** provider timeout, quota or outage.
  - **Verify:** stubbed UPS/USPS quote response.

- [ ] **Q0590 — How would you expose and connect shipping provider integration interface through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** provider timeout, quota or outage.
  - **Verify:** stubbed UPS/USPS quote response.

- [ ] **Q0591 — How would you handle provider timeout, quota or outage while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** provider timeout, quota or outage.
  - **Verify:** stubbed UPS/USPS quote response.


## in-store pickup shipping option

- [ ] **Q0592 — How would you design in-store pickup shipping option with rules for pickup location, scheduling and zero-carrier flow and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** store pickup not offered for stock location.
  - **Verify:** pickup selection tests.

- [ ] **Q0593 — How would you implement in-store pickup shipping option in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** store pickup not offered for stock location.
  - **Verify:** pickup selection tests.

- [ ] **Q0594 — How would you expose and connect in-store pickup shipping option through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** store pickup not offered for stock location.
  - **Verify:** pickup selection tests.

- [ ] **Q0595 — How would you handle store pickup not offered for stock location while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** store pickup not offered for stock location.
  - **Verify:** pickup selection tests.


## shipping selection persistence and recalculation

- [ ] **Q0596 — How would you design shipping selection persistence and recalculation with rules for checkout quote TTL and address-change invalidation and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** stale quote after address edit.
  - **Verify:** re-quote during checkout.

- [ ] **Q0597 — How would you implement shipping selection persistence and recalculation in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** stale quote after address edit.
  - **Verify:** re-quote during checkout.

- [ ] **Q0598 — How would you expose and connect shipping selection persistence and recalculation through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** stale quote after address edit.
  - **Verify:** re-quote during checkout.

- [ ] **Q0599 — How would you handle stale quote after address edit while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** stale quote after address edit.
  - **Verify:** re-quote during checkout.
