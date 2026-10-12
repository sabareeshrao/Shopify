# Phase 10 — Product attributes, options and variants

**Tasks:** 45 · **Range:** Q0305–Q0349 · **Status:** NOT STARTED

**Shopizer reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Each item is an original, independently verifiable build/interview task. MCQ lessons and implementation commits are added only when tackled.


## product option metadata

- [ ] **Q0305 — How would you design product option metadata with explicit contracts for size/color/memory option definitions, data types and display order?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** duplicate option names or unsupported type.
  - **Proof focus:** option validation and stable labels.

- [ ] **Q0306 — How would you implement product option metadata from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** duplicate option names or unsupported type.
  - **Proof focus:** option validation and stable labels.

- [ ] **Q0307 — How would you connect product option metadata across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** duplicate option names or unsupported type.
  - **Proof focus:** option validation and stable labels.

- [ ] **Q0308 — How would you handle duplicate option names or unsupported type in product option metadata without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** duplicate option names or unsupported type.
  - **Proof focus:** option validation and stable labels.

- [ ] **Q0309 — How would you prove product option metadata is correct with option validation and stable labels and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** duplicate option names or unsupported type.
  - **Proof focus:** option validation and stable labels.


## product option values

- [ ] **Q0310 — How would you design product option values with explicit contracts for allowed values and per-product applicability?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** variant references a deleted value.
  - **Proof focus:** create and list scoped values.

- [ ] **Q0311 — How would you implement product option values from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** variant references a deleted value.
  - **Proof focus:** create and list scoped values.

- [ ] **Q0312 — How would you connect product option values across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** variant references a deleted value.
  - **Proof focus:** create and list scoped values.

- [ ] **Q0313 — How would you handle variant references a deleted value in product option values without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** variant references a deleted value.
  - **Proof focus:** create and list scoped values.

- [ ] **Q0314 — How would you prove product option values is correct with create and list scoped values and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** variant references a deleted value.
  - **Proof focus:** create and list scoped values.


## attribute sets and variant axes

- [ ] **Q0315 — How would you design attribute sets and variant axes with explicit contracts for option combinations and required choice constraints?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** missing axis or duplicate combination.
  - **Proof focus:** valid and invalid variant selections.

- [ ] **Q0316 — How would you implement attribute sets and variant axes from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** missing axis or duplicate combination.
  - **Proof focus:** valid and invalid variant selections.

- [ ] **Q0317 — How would you connect attribute sets and variant axes across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** missing axis or duplicate combination.
  - **Proof focus:** valid and invalid variant selections.

- [ ] **Q0318 — How would you handle missing axis or duplicate combination in attribute sets and variant axes without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** missing axis or duplicate combination.
  - **Proof focus:** valid and invalid variant selections.

- [ ] **Q0319 — How would you prove attribute sets and variant axes is correct with valid and invalid variant selections and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** missing axis or duplicate combination.
  - **Proof focus:** valid and invalid variant selections.


## variant SKU and identity

- [ ] **Q0320 — How would you design variant SKU and identity with explicit contracts for parent product, variant identifier and unique SKU?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** two variants with same SKU.
  - **Proof focus:** variant uniqueness in a store.

- [ ] **Q0321 — How would you implement variant SKU and identity from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** two variants with same SKU.
  - **Proof focus:** variant uniqueness in a store.

- [ ] **Q0322 — How would you connect variant SKU and identity across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** two variants with same SKU.
  - **Proof focus:** variant uniqueness in a store.

- [ ] **Q0323 — How would you handle two variants with same SKU in variant SKU and identity without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** two variants with same SKU.
  - **Proof focus:** variant uniqueness in a store.

- [ ] **Q0324 — How would you prove variant SKU and identity is correct with variant uniqueness in a store and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** two variants with same SKU.
  - **Proof focus:** variant uniqueness in a store.


## variant-specific price overrides

- [ ] **Q0325 — How would you design variant-specific price overrides with explicit contracts for base price versus option surcharge and currency?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** negative surcharge or precision mismatch.
  - **Proof focus:** variation total calculation.

- [ ] **Q0326 — How would you implement variant-specific price overrides from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** negative surcharge or precision mismatch.
  - **Proof focus:** variation total calculation.

- [ ] **Q0327 — How would you connect variant-specific price overrides across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** negative surcharge or precision mismatch.
  - **Proof focus:** variation total calculation.

- [ ] **Q0328 — How would you handle negative surcharge or precision mismatch in variant-specific price overrides without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** negative surcharge or precision mismatch.
  - **Proof focus:** variation total calculation.

- [ ] **Q0329 — How would you prove variant-specific price overrides is correct with variation total calculation and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** negative surcharge or precision mismatch.
  - **Proof focus:** variation total calculation.


## variant stock and availability

- [ ] **Q0330 — How would you design variant stock and availability with explicit contracts for per-variant quantity, backorder policy and availability?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** cart selects out-of-stock combination.
  - **Proof focus:** concurrent reservation per variant.

- [ ] **Q0331 — How would you implement variant stock and availability from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** cart selects out-of-stock combination.
  - **Proof focus:** concurrent reservation per variant.

- [ ] **Q0332 — How would you connect variant stock and availability across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** cart selects out-of-stock combination.
  - **Proof focus:** concurrent reservation per variant.

- [ ] **Q0333 — How would you handle cart selects out-of-stock combination in variant stock and availability without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** cart selects out-of-stock combination.
  - **Proof focus:** concurrent reservation per variant.

- [ ] **Q0334 — How would you prove variant stock and availability is correct with concurrent reservation per variant and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** cart selects out-of-stock combination.
  - **Proof focus:** concurrent reservation per variant.


## product variation API

- [ ] **Q0335 — How would you design product variation API with explicit contracts for option set DTOs, create/update/read and validation?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** invalid combination sent through REST.
  - **Proof focus:** positive and 422/400 cases.

- [ ] **Q0336 — How would you implement product variation API from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** invalid combination sent through REST.
  - **Proof focus:** positive and 422/400 cases.

- [ ] **Q0337 — How would you connect product variation API across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** invalid combination sent through REST.
  - **Proof focus:** positive and 422/400 cases.

- [ ] **Q0338 — How would you handle invalid combination sent through REST in product variation API without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** invalid combination sent through REST.
  - **Proof focus:** positive and 422/400 cases.

- [ ] **Q0339 — How would you prove product variation API is correct with positive and 422/400 cases and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** invalid combination sent through REST.
  - **Proof focus:** positive and 422/400 cases.


## product variant images

- [ ] **Q0340 — How would you design product variant images with explicit contracts for image per variation, fallback and asset metadata?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** deleted images and broken references.
  - **Proof focus:** selected-color image renders correctly.

- [ ] **Q0341 — How would you implement product variant images from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** deleted images and broken references.
  - **Proof focus:** selected-color image renders correctly.

- [ ] **Q0342 — How would you connect product variant images across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** deleted images and broken references.
  - **Proof focus:** selected-color image renders correctly.

- [ ] **Q0343 — How would you handle deleted images and broken references in product variant images without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** deleted images and broken references.
  - **Proof focus:** selected-color image renders correctly.

- [ ] **Q0344 — How would you prove product variant images is correct with selected-color image renders correctly and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** deleted images and broken references.
  - **Proof focus:** selected-color image renders correctly.


## variant change propagation

- [ ] **Q0345 — How would you design variant change propagation with explicit contracts for rename/delete options while preserving order history?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** retiring a variant referenced by order.
  - **Proof focus:** legacy order and historical SKU invariants.

- [ ] **Q0346 — How would you implement variant change propagation from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** retiring a variant referenced by order.
  - **Proof focus:** legacy order and historical SKU invariants.

- [ ] **Q0347 — How would you connect variant change propagation across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** retiring a variant referenced by order.
  - **Proof focus:** legacy order and historical SKU invariants.

- [ ] **Q0348 — How would you handle retiring a variant referenced by order in variant change propagation without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** retiring a variant referenced by order.
  - **Proof focus:** legacy order and historical SKU invariants.

- [ ] **Q0349 — How would you prove variant change propagation is correct with legacy order and historical SKU invariants and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** retiring a variant referenced by order.
  - **Proof focus:** legacy order and historical SKU invariants.
