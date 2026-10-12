# Phase 19 — Payment providers and lifecycle

**Tasks:** 42 · **IDs:** Q0630–Q0671 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-modules

Each numbered question is a standalone implementation checkpoint. Preserve IDs on edits and record evidence before checking a task.


## payment abstraction and status model

- [ ] **Q0630 — How would you design payment abstraction and status model with rules for authorize, capture, fail, refund and cancel states and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** illegal status transition.
  - **Verify:** payment state machine tests.

- [ ] **Q0631 — How would you implement payment abstraction and status model in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** illegal status transition.
  - **Verify:** payment state machine tests.

- [ ] **Q0632 — How would you expose and connect payment abstraction and status model through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** illegal status transition.
  - **Verify:** payment state machine tests.

- [ ] **Q0633 — How would you handle illegal status transition while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** illegal status transition.
  - **Verify:** payment state machine tests.

- [ ] **Q0634 — How would you prove payment abstraction and status model with payment state machine tests using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** illegal status transition.
  - **Verify:** payment state machine tests.


## Stripe sandbox payment intent integration

- [ ] **Q0635 — How would you design Stripe sandbox payment intent integration with rules for payment intents, secure credentials and customer actions and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** client-supplied payable amount trusted.
  - **Verify:** sandbox capture with server total.

- [ ] **Q0636 — How would you implement Stripe sandbox payment intent integration in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** client-supplied payable amount trusted.
  - **Verify:** sandbox capture with server total.

- [ ] **Q0637 — How would you expose and connect Stripe sandbox payment intent integration through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** client-supplied payable amount trusted.
  - **Verify:** sandbox capture with server total.

- [ ] **Q0638 — How would you handle client-supplied payable amount trusted while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** client-supplied payable amount trusted.
  - **Verify:** sandbox capture with server total.

- [ ] **Q0639 — How would you prove Stripe sandbox payment intent integration with sandbox capture with server total using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** client-supplied payable amount trusted.
  - **Verify:** sandbox capture with server total.


## payment webhook verification

- [ ] **Q0640 — How would you design payment webhook verification with rules for signature verification, event IDs and audit and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** forged or replayed webhook.
  - **Verify:** duplicate and invalid signature tests.

- [ ] **Q0641 — How would you implement payment webhook verification in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** forged or replayed webhook.
  - **Verify:** duplicate and invalid signature tests.

- [ ] **Q0642 — How would you expose and connect payment webhook verification through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** forged or replayed webhook.
  - **Verify:** duplicate and invalid signature tests.

- [ ] **Q0643 — How would you handle forged or replayed webhook while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** forged or replayed webhook.
  - **Verify:** duplicate and invalid signature tests.

- [ ] **Q0644 — How would you prove payment webhook verification with duplicate and invalid signature tests using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** forged or replayed webhook.
  - **Verify:** duplicate and invalid signature tests.


## payment idempotency and concurrency

- [ ] **Q0645 — How would you design payment idempotency and concurrency with rules for idempotency key, order relation and retry scope and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** double charging on timeout.
  - **Verify:** concurrent retry charges once.

- [ ] **Q0646 — How would you implement payment idempotency and concurrency in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** double charging on timeout.
  - **Verify:** concurrent retry charges once.

- [ ] **Q0647 — How would you expose and connect payment idempotency and concurrency through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** double charging on timeout.
  - **Verify:** concurrent retry charges once.

- [ ] **Q0648 — How would you handle double charging on timeout while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** double charging on timeout.
  - **Verify:** concurrent retry charges once.

- [ ] **Q0649 — How would you prove payment idempotency and concurrency with concurrent retry charges once using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** double charging on timeout.
  - **Verify:** concurrent retry charges once.


## PayPal-compatible provider adapter

- [ ] **Q0650 — How would you design PayPal-compatible provider adapter with rules for provider-neutral interface and result mapping and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** provider response format mismatch.
  - **Verify:** mock gateway adapter contract.

- [ ] **Q0651 — How would you implement PayPal-compatible provider adapter in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** provider response format mismatch.
  - **Verify:** mock gateway adapter contract.

- [ ] **Q0652 — How would you expose and connect PayPal-compatible provider adapter through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** provider response format mismatch.
  - **Verify:** mock gateway adapter contract.

- [ ] **Q0653 — How would you handle provider response format mismatch while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** provider response format mismatch.
  - **Verify:** mock gateway adapter contract.

- [ ] **Q0654 — How would you prove PayPal-compatible provider adapter with mock gateway adapter contract using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** provider response format mismatch.
  - **Verify:** mock gateway adapter contract.


## failed/declined payment recovery

- [ ] **Q0655 — How would you design failed/declined payment recovery with rules for decline, timeout, unknown result and reconciliation and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** order marked paid when charge failed.
  - **Verify:** safe retry with unchanged inventory policy.

- [ ] **Q0656 — How would you implement failed/declined payment recovery in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** order marked paid when charge failed.
  - **Verify:** safe retry with unchanged inventory policy.

- [ ] **Q0657 — How would you expose and connect failed/declined payment recovery through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** order marked paid when charge failed.
  - **Verify:** safe retry with unchanged inventory policy.

- [ ] **Q0658 — How would you handle order marked paid when charge failed while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** order marked paid when charge failed.
  - **Verify:** safe retry with unchanged inventory policy.

- [ ] **Q0659 — How would you prove failed/declined payment recovery with safe retry with unchanged inventory policy using positive and failure-path automated tests?**
  - **Acceptance:** Passing tests and recorded expected results.
  - **Risk:** order marked paid when charge failed.
  - **Verify:** safe retry with unchanged inventory policy.


## partial and full refunds

- [ ] **Q0660 — How would you design partial and full refunds with rules for refundable amount, reason and refund status and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** refund greater than captured amount.
  - **Verify:** partial refund then remaining refund.

- [ ] **Q0661 — How would you implement partial and full refunds in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** refund greater than captured amount.
  - **Verify:** partial refund then remaining refund.

- [ ] **Q0662 — How would you expose and connect partial and full refunds through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** refund greater than captured amount.
  - **Verify:** partial refund then remaining refund.

- [ ] **Q0663 — How would you handle refund greater than captured amount while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** refund greater than captured amount.
  - **Verify:** partial refund then remaining refund.


## payment security and compliance boundaries

- [ ] **Q0664 — How would you design payment security and compliance boundaries with rules for tokenized payment methods and redacted logging and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** credit card PAN or secret written to logs.
  - **Verify:** sensitive data never persisted.

- [ ] **Q0665 — How would you implement payment security and compliance boundaries in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** credit card PAN or secret written to logs.
  - **Verify:** sensitive data never persisted.

- [ ] **Q0666 — How would you expose and connect payment security and compliance boundaries through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** credit card PAN or secret written to logs.
  - **Verify:** sensitive data never persisted.

- [ ] **Q0667 — How would you handle credit card PAN or secret written to logs while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** credit card PAN or secret written to logs.
  - **Verify:** sensitive data never persisted.


## payment settlement and reconciliation

- [ ] **Q0668 — How would you design payment settlement and reconciliation with rules for provider event history and order/payment matching and explain the choices?**
  - **Acceptance:** Design artifact, explicit invariants and request/data contracts.
  - **Risk:** webhook arrives before local commit.
  - **Verify:** eventual reconciliation job.

- [ ] **Q0669 — How would you implement payment settlement and reconciliation in clean Java 21 classes and persist relevant state safely?**
  - **Acceptance:** Running code and required schema/configuration.
  - **Risk:** webhook arrives before local commit.
  - **Verify:** eventual reconciliation job.

- [ ] **Q0670 — How would you expose and connect payment settlement and reconciliation through APIs or service boundaries for a working request?**
  - **Acceptance:** End-to-end real execution with correct response.
  - **Risk:** webhook arrives before local commit.
  - **Verify:** eventual reconciliation job.

- [ ] **Q0671 — How would you handle webhook arrives before local commit while keeping business state and user-visible errors correct?**
  - **Acceptance:** Reproducible edge case and safe recovery or rejection.
  - **Risk:** webhook arrives before local commit.
  - **Verify:** eventual reconciliation job.
