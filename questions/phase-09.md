# Phase 09 — Products, brands, SKUs and descriptions

**Task count:** 49 · **IDs:** Q0256–Q0304 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Every checklist item is one original development question. Each must be taught with MCQs, implemented incrementally and verified before completion. Tests and evidence belong with the eventual implementation.


## product aggregate identity and lifecycle

- [ ] **Q0256 — How would you design product aggregate identity and lifecycle with explicit rules for product IDs, SKU, status and merchant scoping?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** SKU duplicate within a merchant.
  - **Verification scenario:** persist, retrieve and disable product.

- [ ] **Q0257 — How would you implement product aggregate identity and lifecycle using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** SKU duplicate within a merchant.
  - **Verification scenario:** persist, retrieve and disable product.

- [ ] **Q0258 — How would you connect product aggregate identity and lifecycle end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** SKU duplicate within a merchant.
  - **Verification scenario:** persist, retrieve and disable product.

- [ ] **Q0259 — How would you prevent or recover from SKU duplicate within a merchant when building product aggregate identity and lifecycle?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** SKU duplicate within a merchant.
  - **Verification scenario:** persist, retrieve and disable product.

- [ ] **Q0260 — How would you verify product aggregate identity and lifecycle with persist, retrieve and disable product, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** SKU duplicate within a merchant.
  - **Verification scenario:** persist, retrieve and disable product.


## manufacturer/brand domain

- [ ] **Q0261 — How would you design manufacturer/brand domain with explicit rules for brand description, association and CRUD rules?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** delete referenced brand.
  - **Verification scenario:** brand relationship constraints.

- [ ] **Q0262 — How would you implement manufacturer/brand domain using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** delete referenced brand.
  - **Verification scenario:** brand relationship constraints.

- [ ] **Q0263 — How would you connect manufacturer/brand domain end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** delete referenced brand.
  - **Verification scenario:** brand relationship constraints.

- [ ] **Q0264 — How would you prevent or recover from delete referenced brand when building manufacturer/brand domain?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** delete referenced brand.
  - **Verification scenario:** brand relationship constraints.

- [ ] **Q0265 — How would you verify manufacturer/brand domain with brand relationship constraints, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** delete referenced brand.
  - **Verification scenario:** brand relationship constraints.


## product descriptions and SEO fields

- [ ] **Q0266 — How would you design product descriptions and SEO fields with explicit rules for localized title, slug, metadata and rich text policy?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** unsafe HTML or duplicate slug.
  - **Verification scenario:** localized product DTO and safe rendering.

- [ ] **Q0267 — How would you implement product descriptions and SEO fields using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** unsafe HTML or duplicate slug.
  - **Verification scenario:** localized product DTO and safe rendering.

- [ ] **Q0268 — How would you connect product descriptions and SEO fields end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** unsafe HTML or duplicate slug.
  - **Verification scenario:** localized product DTO and safe rendering.

- [ ] **Q0269 — How would you prevent or recover from unsafe HTML or duplicate slug when building product descriptions and SEO fields?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** unsafe HTML or duplicate slug.
  - **Verification scenario:** localized product DTO and safe rendering.

- [ ] **Q0270 — How would you verify product descriptions and SEO fields with localized product DTO and safe rendering, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** unsafe HTML or duplicate slug.
  - **Verification scenario:** localized product DTO and safe rendering.


## product dimensions and units

- [ ] **Q0271 — How would you design product dimensions and units with explicit rules for weight, length, height, width and units?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** negative measures or mixed units.
  - **Verification scenario:** conversion and validation tests.

- [ ] **Q0272 — How would you implement product dimensions and units using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** negative measures or mixed units.
  - **Verification scenario:** conversion and validation tests.

- [ ] **Q0273 — How would you connect product dimensions and units end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** negative measures or mixed units.
  - **Verification scenario:** conversion and validation tests.

- [ ] **Q0274 — How would you prevent or recover from negative measures or mixed units when building product dimensions and units?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** negative measures or mixed units.
  - **Verification scenario:** conversion and validation tests.

- [ ] **Q0275 — How would you verify product dimensions and units with conversion and validation tests, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** negative measures or mixed units.
  - **Verification scenario:** conversion and validation tests.


## physical, digital and rental product types

- [ ] **Q0276 — How would you design physical, digital and rental product types with explicit rules for type-specific contracts and allowed options?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** digital product requiring shipping.
  - **Verification scenario:** type-aware validation.

- [ ] **Q0277 — How would you implement physical, digital and rental product types using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** digital product requiring shipping.
  - **Verification scenario:** type-aware validation.

- [ ] **Q0278 — How would you connect physical, digital and rental product types end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** digital product requiring shipping.
  - **Verification scenario:** type-aware validation.

- [ ] **Q0279 — How would you prevent or recover from digital product requiring shipping when building physical, digital and rental product types?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** digital product requiring shipping.
  - **Verification scenario:** type-aware validation.

- [ ] **Q0280 — How would you verify physical, digital and rental product types with type-aware validation, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** digital product requiring shipping.
  - **Verification scenario:** type-aware validation.


## product CRUD REST contract

- [ ] **Q0281 — How would you design product CRUD REST contract with explicit rules for DTO validation, status codes, idempotent updates?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** invalid merchant or missing product.
  - **Verification scenario:** POST/GET/PUT/PATCH/DELETE integration tests.

- [ ] **Q0282 — How would you implement product CRUD REST contract using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** invalid merchant or missing product.
  - **Verification scenario:** POST/GET/PUT/PATCH/DELETE integration tests.

- [ ] **Q0283 — How would you connect product CRUD REST contract end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** invalid merchant or missing product.
  - **Verification scenario:** POST/GET/PUT/PATCH/DELETE integration tests.

- [ ] **Q0284 — How would you prevent or recover from invalid merchant or missing product when building product CRUD REST contract?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** invalid merchant or missing product.
  - **Verification scenario:** POST/GET/PUT/PATCH/DELETE integration tests.

- [ ] **Q0285 — How would you verify product CRUD REST contract with POST/GET/PUT/PATCH/DELETE integration tests, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** invalid merchant or missing product.
  - **Verification scenario:** POST/GET/PUT/PATCH/DELETE integration tests.


## product discovery listing API

- [ ] **Q0286 — How would you design product discovery listing API with explicit rules for pagination, filter, sort and projection?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** unbounded result set and unstable sorting.
  - **Verification scenario:** deterministic sorted pages.

- [ ] **Q0287 — How would you implement product discovery listing API using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** unbounded result set and unstable sorting.
  - **Verification scenario:** deterministic sorted pages.

- [ ] **Q0288 — How would you connect product discovery listing API end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** unbounded result set and unstable sorting.
  - **Verification scenario:** deterministic sorted pages.

- [ ] **Q0289 — How would you prevent or recover from unbounded result set and unstable sorting when building product discovery listing API?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** unbounded result set and unstable sorting.
  - **Verification scenario:** deterministic sorted pages.

- [ ] **Q0290 — How would you verify product discovery listing API with deterministic sorted pages, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** unbounded result set and unstable sorting.
  - **Verification scenario:** deterministic sorted pages.


## product relationships and bundles

- [ ] **Q0291 — How would you design product relationships and bundles with explicit rules for related products, cross-sell and association types?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** self-reference or cyclic bundle.
  - **Verification scenario:** association and delete semantics.

- [ ] **Q0292 — How would you implement product relationships and bundles using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** self-reference or cyclic bundle.
  - **Verification scenario:** association and delete semantics.

- [ ] **Q0293 — How would you connect product relationships and bundles end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** self-reference or cyclic bundle.
  - **Verification scenario:** association and delete semantics.

- [ ] **Q0294 — How would you prevent or recover from self-reference or cyclic bundle when building product relationships and bundles?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** self-reference or cyclic bundle.
  - **Verification scenario:** association and delete semantics.

- [ ] **Q0295 — How would you verify product relationships and bundles with association and delete semantics, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** self-reference or cyclic bundle.
  - **Verification scenario:** association and delete semantics.


## SKU existence query and database constraint

- [ ] **Q0296 — How would you design SKU existence query and database constraint with explicit rules for existsBySku semantics and merchant-specific uniqueness?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** race between two matching inserts.
  - **Verification scenario:** concurrent duplicate SKU regression.

- [ ] **Q0297 — How would you implement SKU existence query and database constraint using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** race between two matching inserts.
  - **Verification scenario:** concurrent duplicate SKU regression.

- [ ] **Q0298 — How would you connect SKU existence query and database constraint end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** race between two matching inserts.
  - **Verification scenario:** concurrent duplicate SKU regression.

- [ ] **Q0299 — How would you prevent or recover from race between two matching inserts when building SKU existence query and database constraint?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** race between two matching inserts.
  - **Verification scenario:** concurrent duplicate SKU regression.

- [ ] **Q0300 — How would you verify SKU existence query and database constraint with concurrent duplicate SKU regression, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** race between two matching inserts.
  - **Verification scenario:** concurrent duplicate SKU regression.


## backward compatible product URL access

- [ ] **Q0301 — How would you design backward compatible product URL access with explicit rules for ID lookup, friendly URL lookup and API evolution?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** legacy URL breaks after new route.
  - **Verification scenario:** old and new route contract tests.

- [ ] **Q0302 — How would you implement backward compatible product URL access using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** legacy URL breaks after new route.
  - **Verification scenario:** old and new route contract tests.

- [ ] **Q0303 — How would you connect backward compatible product URL access end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** legacy URL breaks after new route.
  - **Verification scenario:** old and new route contract tests.

- [ ] **Q0304 — How would you prevent or recover from legacy URL breaks after new route when building backward compatible product URL access?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** legacy URL breaks after new route.
  - **Verification scenario:** old and new route contract tests.
