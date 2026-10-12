# Phase 15 — Customers, profiles and reviews

**Tasks:** 40 · **IDs:** Q0494–Q0533 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Each numbered question is a standalone implementation checkpoint. Preserve IDs on edits and record evidence before checking a task.


## customer identity and store membership

- [ ] **Q0494 — How would you design customer identity and store membership with rules for account ID, email uniqueness and merchant scoping and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** duplicate accounts across stores.
  - **Verify:** create and lookup by merchant.

- [ ] **Q0495 — How would you implement customer identity and store membership in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** duplicate accounts across stores.
  - **Verify:** create and lookup by merchant.

- [ ] **Q0496 — How would you expose and connect customer identity and store membership through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** duplicate accounts across stores.
  - **Verify:** create and lookup by merchant.

- [ ] **Q0497 — How would you handle duplicate accounts across stores while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** duplicate accounts across stores.
  - **Verify:** create and lookup by merchant.

- [ ] **Q0498 — How would you prove customer identity and store membership with create and lookup by merchant using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** duplicate accounts across stores.
  - **Verify:** create and lookup by merchant.


## customer registration and confirmation

- [ ] **Q0499 — How would you design customer registration and confirmation with rules for self-service registration and email verification and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** email enumeration and unverified access.
  - **Verify:** verified versus unverified login.

- [ ] **Q0500 — How would you implement customer registration and confirmation in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** email enumeration and unverified access.
  - **Verify:** verified versus unverified login.

- [ ] **Q0501 — How would you expose and connect customer registration and confirmation through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** email enumeration and unverified access.
  - **Verify:** verified versus unverified login.

- [ ] **Q0502 — How would you handle email enumeration and unverified access while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** email enumeration and unverified access.
  - **Verify:** verified versus unverified login.

- [ ] **Q0503 — How would you prove customer registration and confirmation with verified versus unverified login using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** email enumeration and unverified access.
  - **Verify:** verified versus unverified login.


## customer profile updates

- [ ] **Q0504 — How would you design customer profile updates with rules for name, contact data, timezone and edit permissions and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** editing another user's profile.
  - **Verify:** owner-only profile API.

- [ ] **Q0505 — How would you implement customer profile updates in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** editing another user's profile.
  - **Verify:** owner-only profile API.

- [ ] **Q0506 — How would you expose and connect customer profile updates through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** editing another user's profile.
  - **Verify:** owner-only profile API.

- [ ] **Q0507 — How would you handle editing another user's profile while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** editing another user's profile.
  - **Verify:** owner-only profile API.

- [ ] **Q0508 — How would you prove customer profile updates with owner-only profile API using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** editing another user's profile.
  - **Verify:** owner-only profile API.


## multiple customer addresses

- [ ] **Q0509 — How would you design multiple customer addresses with rules for shipping/billing defaults and ownership and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** deleting address used by historical order.
  - **Verify:** address snapshot and ownership.

- [ ] **Q0510 — How would you implement multiple customer addresses in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** deleting address used by historical order.
  - **Verify:** address snapshot and ownership.

- [ ] **Q0511 — How would you expose and connect multiple customer addresses through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** deleting address used by historical order.
  - **Verify:** address snapshot and ownership.

- [ ] **Q0512 — How would you handle deleting address used by historical order while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** deleting address used by historical order.
  - **Verify:** address snapshot and ownership.

- [ ] **Q0513 — How would you prove multiple customer addresses with address snapshot and ownership using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** deleting address used by historical order.
  - **Verify:** address snapshot and ownership.


## customer password reset workflow

- [ ] **Q0514 — How would you design customer password reset workflow with rules for single-use short-lived reset tokens and rate limits and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** reset token replay and account enumeration.
  - **Verify:** invalid/expired token tests.

- [ ] **Q0515 — How would you implement customer password reset workflow in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** reset token replay and account enumeration.
  - **Verify:** invalid/expired token tests.

- [ ] **Q0516 — How would you expose and connect customer password reset workflow through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** reset token replay and account enumeration.
  - **Verify:** invalid/expired token tests.

- [ ] **Q0517 — How would you handle reset token replay and account enumeration while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** reset token replay and account enumeration.
  - **Verify:** invalid/expired token tests.

- [ ] **Q0518 — How would you prove customer password reset workflow with invalid/expired token tests using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** reset token replay and account enumeration.
  - **Verify:** invalid/expired token tests.


## customer preference and consent

- [ ] **Q0519 — How would you design customer preference and consent with rules for newsletter opt-in, language preferences and consent record and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** no proof of consent or unsubscribed emails.
  - **Verify:** consent transitions and audit.

- [ ] **Q0520 — How would you implement customer preference and consent in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** no proof of consent or unsubscribed emails.
  - **Verify:** consent transitions and audit.

- [ ] **Q0521 — How would you expose and connect customer preference and consent through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** no proof of consent or unsubscribed emails.
  - **Verify:** consent transitions and audit.

- [ ] **Q0522 — How would you handle no proof of consent or unsubscribed emails while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** no proof of consent or unsubscribed emails.
  - **Verify:** consent transitions and audit.

- [ ] **Q0523 — How would you prove customer preference and consent with consent transitions and audit using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** no proof of consent or unsubscribed emails.
  - **Verify:** consent transitions and audit.


## product reviews and ratings

- [ ] **Q0524 — How would you design product reviews and ratings with rules for review author, product link, moderation and visibility and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** fake review or duplicate order review.
  - **Verify:** approved review appears on product.

- [ ] **Q0525 — How would you implement product reviews and ratings in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** fake review or duplicate order review.
  - **Verify:** approved review appears on product.

- [ ] **Q0526 — How would you expose and connect product reviews and ratings through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** fake review or duplicate order review.
  - **Verify:** approved review appears on product.

- [ ] **Q0527 — How would you handle fake review or duplicate order review while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** fake review or duplicate order review.
  - **Verify:** approved review appears on product.

- [ ] **Q0528 — How would you prove product reviews and ratings with approved review appears on product using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** fake review or duplicate order review.
  - **Verify:** approved review appears on product.


## customer data export and removal policy

- [ ] **Q0529 — How would you design customer data export and removal policy with rules for authorization, privacy constraints and order retention and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** PII exposed in export or deleted records required for orders.
  - **Verify:** verified export and retention behavior.

- [ ] **Q0530 — How would you implement customer data export and removal policy in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** PII exposed in export or deleted records required for orders.
  - **Verify:** verified export and retention behavior.

- [ ] **Q0531 — How would you expose and connect customer data export and removal policy through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** PII exposed in export or deleted records required for orders.
  - **Verify:** verified export and retention behavior.

- [ ] **Q0532 — How would you handle PII exposed in export or deleted records required for orders while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** PII exposed in export or deleted records required for orders.
  - **Verify:** verified export and retention behavior.

- [ ] **Q0533 — How would you prove customer data export and removal policy with verified export and retention behavior using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** PII exposed in export or deleted records required for orders.
  - **Verify:** verified export and retention behavior.
