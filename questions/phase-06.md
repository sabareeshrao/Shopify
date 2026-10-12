# Phase 06 — Merchant stores and multi-tenancy

**Task count:** 35 · **IDs:** Q0141–Q0175 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Every checklist item is one original development question. Each must be taught with MCQs, implemented incrementally and verified before completion. Tests and evidence belong with the eventual implementation.


## merchant account domain

- [ ] **Q0141 — How would you design merchant account domain with explicit rules for merchant identifiers, ownership and activation states?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** duplicate registration or disabled merchant.
  - **Verification scenario:** merchant creation and status transitions.

- [ ] **Q0142 — How would you implement merchant account domain using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** duplicate registration or disabled merchant.
  - **Verification scenario:** merchant creation and status transitions.

- [ ] **Q0143 — How would you connect merchant account domain end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** duplicate registration or disabled merchant.
  - **Verification scenario:** merchant creation and status transitions.

- [ ] **Q0144 — How would you prevent or recover from duplicate registration or disabled merchant when building merchant account domain?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** duplicate registration or disabled merchant.
  - **Verification scenario:** merchant creation and status transitions.

- [ ] **Q0145 — How would you verify merchant account domain with merchant creation and status transitions, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** duplicate registration or disabled merchant.
  - **Verification scenario:** merchant creation and status transitions.


## store profile and contact settings

- [ ] **Q0146 — How would you design store profile and contact settings with explicit rules for name, address, logo, timezone and email?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** invalid store URLs or incomplete address.
  - **Verification scenario:** store profile create/read/update.

- [ ] **Q0147 — How would you implement store profile and contact settings using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** invalid store URLs or incomplete address.
  - **Verification scenario:** store profile create/read/update.

- [ ] **Q0148 — How would you connect store profile and contact settings end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** invalid store URLs or incomplete address.
  - **Verification scenario:** store profile create/read/update.

- [ ] **Q0149 — How would you prevent or recover from invalid store URLs or incomplete address when building store profile and contact settings?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** invalid store URLs or incomplete address.
  - **Verification scenario:** store profile create/read/update.

- [ ] **Q0150 — How would you verify store profile and contact settings with store profile create/read/update, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** invalid store URLs or incomplete address.
  - **Verification scenario:** store profile create/read/update.


## merchant-to-store relationships

- [ ] **Q0151 — How would you design merchant-to-store relationships with explicit rules for store ownership, allowed operators and uniqueness?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** cross-merchant access to stores.
  - **Verification scenario:** tenant-isolation integration test.

- [ ] **Q0152 — How would you implement merchant-to-store relationships using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** cross-merchant access to stores.
  - **Verification scenario:** tenant-isolation integration test.

- [ ] **Q0153 — How would you connect merchant-to-store relationships end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** cross-merchant access to stores.
  - **Verification scenario:** tenant-isolation integration test.

- [ ] **Q0154 — How would you prevent or recover from cross-merchant access to stores when building merchant-to-store relationships?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** cross-merchant access to stores.
  - **Verification scenario:** tenant-isolation integration test.

- [ ] **Q0155 — How would you verify merchant-to-store relationships with tenant-isolation integration test, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** cross-merchant access to stores.
  - **Verification scenario:** tenant-isolation integration test.


## store-specific currency and locale policy

- [ ] **Q0156 — How would you design store-specific currency and locale policy with explicit rules for default currency, supported languages and timezone?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** switching currency after orders exist.
  - **Verification scenario:** store configuration invariants.

- [ ] **Q0157 — How would you implement store-specific currency and locale policy using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** switching currency after orders exist.
  - **Verification scenario:** store configuration invariants.

- [ ] **Q0158 — How would you connect store-specific currency and locale policy end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** switching currency after orders exist.
  - **Verification scenario:** store configuration invariants.

- [ ] **Q0159 — How would you prevent or recover from switching currency after orders exist when building store-specific currency and locale policy?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** switching currency after orders exist.
  - **Verification scenario:** store configuration invariants.

- [ ] **Q0160 — How would you verify store-specific currency and locale policy with store configuration invariants, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** switching currency after orders exist.
  - **Verification scenario:** store configuration invariants.


## store configuration API

- [ ] **Q0161 — How would you design store configuration API with explicit rules for merchant configuration DTOs and authorization?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** non-owner editing store settings.
  - **Verification scenario:** role-scoped CRUD and validation.

- [ ] **Q0162 — How would you implement store configuration API using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** non-owner editing store settings.
  - **Verification scenario:** role-scoped CRUD and validation.

- [ ] **Q0163 — How would you connect store configuration API end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** non-owner editing store settings.
  - **Verification scenario:** role-scoped CRUD and validation.

- [ ] **Q0164 — How would you prevent or recover from non-owner editing store settings when building store configuration API?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** non-owner editing store settings.
  - **Verification scenario:** role-scoped CRUD and validation.

- [ ] **Q0165 — How would you verify store configuration API with role-scoped CRUD and validation, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** non-owner editing store settings.
  - **Verification scenario:** role-scoped CRUD and validation.


## multi-store catalog ownership

- [ ] **Q0166 — How would you design multi-store catalog ownership with explicit rules for product/category scoping by merchant store?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** cross-store product visibility leak.
  - **Verification scenario:** two merchants with overlapping SKUs.

- [ ] **Q0167 — How would you implement multi-store catalog ownership using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** cross-store product visibility leak.
  - **Verification scenario:** two merchants with overlapping SKUs.

- [ ] **Q0168 — How would you connect multi-store catalog ownership end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** cross-store product visibility leak.
  - **Verification scenario:** two merchants with overlapping SKUs.

- [ ] **Q0169 — How would you prevent or recover from cross-store product visibility leak when building multi-store catalog ownership?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** cross-store product visibility leak.
  - **Verification scenario:** two merchants with overlapping SKUs.

- [ ] **Q0170 — How would you verify multi-store catalog ownership with two merchants with overlapping SKUs, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** cross-store product visibility leak.
  - **Verification scenario:** two merchants with overlapping SKUs.


## store bootstrap and default merchant

- [ ] **Q0171 — How would you design store bootstrap and default merchant with explicit rules for initial admin/store seeding and activation?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** multiple default stores or race at startup.
  - **Verification scenario:** fresh install and repeat bootstrap.

- [ ] **Q0172 — How would you implement store bootstrap and default merchant using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** multiple default stores or race at startup.
  - **Verification scenario:** fresh install and repeat bootstrap.

- [ ] **Q0173 — How would you connect store bootstrap and default merchant end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** multiple default stores or race at startup.
  - **Verification scenario:** fresh install and repeat bootstrap.

- [ ] **Q0174 — How would you prevent or recover from multiple default stores or race at startup when building store bootstrap and default merchant?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** multiple default stores or race at startup.
  - **Verification scenario:** fresh install and repeat bootstrap.

- [ ] **Q0175 — How would you verify store bootstrap and default merchant with fresh install and repeat bootstrap, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** multiple default stores or race at startup.
  - **Verification scenario:** fresh install and repeat bootstrap.
