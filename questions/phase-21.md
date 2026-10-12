# Phase 21 — Orders, statuses, invoices and refunds

**Original tasks:** 42 · **Range:** Q0720–Q0761 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Build in short increments. Every question needs MCQ training, runnable code, expected results, automated coverage where feasible and verified completion before its box is checked.


## order aggregate and immutable line snapshots

- [ ] **Q0720 — How would you design order aggregate and immutable line snapshots with precise requirements for SKU, unit price, tax and shipping copied at order time?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** product renamed/deleted after order.
  - **Proof scenario:** historical order remains readable.

- [ ] **Q0721 — How would you implement order aggregate and immutable line snapshots with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** product renamed/deleted after order.
  - **Proof scenario:** historical order remains readable.

- [ ] **Q0722 — How would you connect order aggregate and immutable line snapshots to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** product renamed/deleted after order.
  - **Proof scenario:** historical order remains readable.

- [ ] **Q0723 — How would you reproduce and handle product renamed/deleted after order for order aggregate and immutable line snapshots without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** product renamed/deleted after order.
  - **Proof scenario:** historical order remains readable.

- [ ] **Q0724 — How would you test order aggregate and immutable line snapshots with historical order remains readable, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** product renamed/deleted after order.
  - **Proof scenario:** historical order remains readable.

- [ ] **Q0725 — How would you optimize, secure and make order aggregate and immutable line snapshots observable without changing accepted behavior?**
  - **Acceptance:** Performance/security review and regression coverage.
  - **Edge case:** product renamed/deleted after order.
  - **Proof scenario:** historical order remains readable.


## order status state machine

- [ ] **Q0726 — How would you design order status state machine with precise requirements for pending, paid, processing, shipped, completed, canceled?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** illegal transition like shipped to pending.
  - **Proof scenario:** allowed/rejected transition table.

- [ ] **Q0727 — How would you implement order status state machine with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** illegal transition like shipped to pending.
  - **Proof scenario:** allowed/rejected transition table.

- [ ] **Q0728 — How would you connect order status state machine to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** illegal transition like shipped to pending.
  - **Proof scenario:** allowed/rejected transition table.

- [ ] **Q0729 — How would you reproduce and handle illegal transition like shipped to pending for order status state machine without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** illegal transition like shipped to pending.
  - **Proof scenario:** allowed/rejected transition table.

- [ ] **Q0730 — How would you test order status state machine with allowed/rejected transition table, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** illegal transition like shipped to pending.
  - **Proof scenario:** allowed/rejected transition table.

- [ ] **Q0731 — How would you optimize, secure and make order status state machine observable without changing accepted behavior?**
  - **Acceptance:** Performance/security review and regression coverage.
  - **Edge case:** illegal transition like shipped to pending.
  - **Proof scenario:** allowed/rejected transition table.


## order creation and lookup endpoints

- [ ] **Q0732 — How would you design order creation and lookup endpoints with precise requirements for customer ownership, merchant scoping and sorting?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** one customer reads other's order.
  - **Proof scenario:** customer and admin order APIs.

- [ ] **Q0733 — How would you implement order creation and lookup endpoints with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** one customer reads other's order.
  - **Proof scenario:** customer and admin order APIs.

- [ ] **Q0734 — How would you connect order creation and lookup endpoints to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** one customer reads other's order.
  - **Proof scenario:** customer and admin order APIs.

- [ ] **Q0735 — How would you reproduce and handle one customer reads other's order for order creation and lookup endpoints without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** one customer reads other's order.
  - **Proof scenario:** customer and admin order APIs.

- [ ] **Q0736 — How would you test order creation and lookup endpoints with customer and admin order APIs, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** one customer reads other's order.
  - **Proof scenario:** customer and admin order APIs.


## payment and shipping order associations

- [ ] **Q0737 — How would you design payment and shipping order associations with precise requirements for payment reference, shipment tracking and totals?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** shipment created for unpaid order.
  - **Proof scenario:** order paid/shipped trace.

- [ ] **Q0738 — How would you implement payment and shipping order associations with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** shipment created for unpaid order.
  - **Proof scenario:** order paid/shipped trace.

- [ ] **Q0739 — How would you connect payment and shipping order associations to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** shipment created for unpaid order.
  - **Proof scenario:** order paid/shipped trace.

- [ ] **Q0740 — How would you reproduce and handle shipment created for unpaid order for payment and shipping order associations without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** shipment created for unpaid order.
  - **Proof scenario:** order paid/shipped trace.

- [ ] **Q0741 — How would you test payment and shipping order associations with order paid/shipped trace, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** shipment created for unpaid order.
  - **Proof scenario:** order paid/shipped trace.


## order audit trail and status history

- [ ] **Q0742 — How would you design order audit trail and status history with precise requirements for actor, transition time and explanation?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** status transition with no event record.
  - **Proof scenario:** timeline consistently recorded.

- [ ] **Q0743 — How would you implement order audit trail and status history with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** status transition with no event record.
  - **Proof scenario:** timeline consistently recorded.

- [ ] **Q0744 — How would you connect order audit trail and status history to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** status transition with no event record.
  - **Proof scenario:** timeline consistently recorded.

- [ ] **Q0745 — How would you reproduce and handle status transition with no event record for order audit trail and status history without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** status transition with no event record.
  - **Proof scenario:** timeline consistently recorded.

- [ ] **Q0746 — How would you test order audit trail and status history with timeline consistently recorded, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** status transition with no event record.
  - **Proof scenario:** timeline consistently recorded.


## cancellation and stock restoration

- [ ] **Q0747 — How would you design cancellation and stock restoration with precise requirements for cancellation eligibility, reserved stock and refund trigger?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** late cancel after fulfillment.
  - **Proof scenario:** refund/stock consistent outcome.

- [ ] **Q0748 — How would you implement cancellation and stock restoration with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** late cancel after fulfillment.
  - **Proof scenario:** refund/stock consistent outcome.

- [ ] **Q0749 — How would you connect cancellation and stock restoration to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** late cancel after fulfillment.
  - **Proof scenario:** refund/stock consistent outcome.

- [ ] **Q0750 — How would you reproduce and handle late cancel after fulfillment for cancellation and stock restoration without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** late cancel after fulfillment.
  - **Proof scenario:** refund/stock consistent outcome.

- [ ] **Q0751 — How would you test cancellation and stock restoration with refund/stock consistent outcome, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** late cancel after fulfillment.
  - **Proof scenario:** refund/stock consistent outcome.


## invoice generation and durable download

- [ ] **Q0752 — How would you design invoice generation and durable download with precise requirements for invoice number, purchase snapshot and access control?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** invoice regenerate changes totals.
  - **Proof scenario:** download invoice after product change.

- [ ] **Q0753 — How would you implement invoice generation and durable download with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** invoice regenerate changes totals.
  - **Proof scenario:** download invoice after product change.

- [ ] **Q0754 — How would you connect invoice generation and durable download to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** invoice regenerate changes totals.
  - **Proof scenario:** download invoice after product change.

- [ ] **Q0755 — How would you reproduce and handle invoice regenerate changes totals for invoice generation and durable download without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** invoice regenerate changes totals.
  - **Proof scenario:** download invoice after product change.

- [ ] **Q0756 — How would you test invoice generation and durable download with download invoice after product change, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** invoice regenerate changes totals.
  - **Proof scenario:** download invoice after product change.


## return/refund order flows

- [ ] **Q0757 — How would you design return/refund order flows with precise requirements for partial quantities, refund totals and compensating updates?**
  - **Acceptance:** Documented component/domain/API contracts, dependencies and invariants.
  - **Edge case:** duplicate refund or return exceeds purchased quantity.
  - **Proof scenario:** partial/full return integration.

- [ ] **Q0758 — How would you implement return/refund order flows with correct Java classes, durable state and transactional boundaries?**
  - **Acceptance:** Compiling implementation and step-by-step file changes.
  - **Edge case:** duplicate refund or return exceeds purchased quantity.
  - **Proof scenario:** partial/full return integration.

- [ ] **Q0759 — How would you connect return/refund order flows to API/service/integration boundaries so the entire business flow works?**
  - **Acceptance:** Live integration and captured expected response or UI state.
  - **Edge case:** duplicate refund or return exceeds purchased quantity.
  - **Proof scenario:** partial/full return integration.

- [ ] **Q0760 — How would you reproduce and handle duplicate refund or return exceeds purchased quantity for return/refund order flows without breaking the user journey or data integrity?**
  - **Acceptance:** Explicit failure response, recovery behavior and no lost state.
  - **Edge case:** duplicate refund or return exceeds purchased quantity.
  - **Proof scenario:** partial/full return integration.

- [ ] **Q0761 — How would you test return/refund order flows with partial/full return integration, including success, invalid input and failure paths?**
  - **Acceptance:** Passing automated tests and reproducible manual check.
  - **Edge case:** duplicate refund or return exceeds purchased quantity.
  - **Proof scenario:** partial/full return integration.
