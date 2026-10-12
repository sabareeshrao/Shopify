# Phase 08 — Catalogs and hierarchical categories

**Task count:** 37 · **IDs:** Q0219–Q0255 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Every checklist item is one original development question. Each must be taught with MCQs, implemented incrementally and verified before completion. Tests and evidence belong with the eventual implementation.


## catalog and category database entities

- [ ] **Q0219 — How would you design catalog and category database entities with explicit rules for parent-child mappings and store ownership?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** orphaned categories or cycles.
  - **Verification scenario:** hierarchy persistence across restart.

- [ ] **Q0220 — How would you implement catalog and category database entities using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** orphaned categories or cycles.
  - **Verification scenario:** hierarchy persistence across restart.

- [ ] **Q0221 — How would you connect catalog and category database entities end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** orphaned categories or cycles.
  - **Verification scenario:** hierarchy persistence across restart.

- [ ] **Q0222 — How would you prevent or recover from orphaned categories or cycles when building catalog and category database entities?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** orphaned categories or cycles.
  - **Verification scenario:** hierarchy persistence across restart.

- [ ] **Q0223 — How would you verify catalog and category database entities with hierarchy persistence across restart, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** orphaned categories or cycles.
  - **Verification scenario:** hierarchy persistence across restart.

- [ ] **Q0224 — How would you profile, secure or refactor catalog and category database entities after it works, while preserving its public contract?**
  - **Acceptance:** Document a measured or justified improvement with regression protection.
  - **Critical failure:** orphaned categories or cycles.
  - **Verification scenario:** hierarchy persistence across restart.


## category tree traversal

- [ ] **Q0225 — How would you design category tree traversal with explicit rules for ancestor-descendant queries and recursive traversal?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** cyclic hierarchy and excessive recursion.
  - **Verification scenario:** deep tree and cycle prevention tests.

- [ ] **Q0226 — How would you implement category tree traversal using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** cyclic hierarchy and excessive recursion.
  - **Verification scenario:** deep tree and cycle prevention tests.

- [ ] **Q0227 — How would you connect category tree traversal end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** cyclic hierarchy and excessive recursion.
  - **Verification scenario:** deep tree and cycle prevention tests.

- [ ] **Q0228 — How would you prevent or recover from cyclic hierarchy and excessive recursion when building category tree traversal?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** cyclic hierarchy and excessive recursion.
  - **Verification scenario:** deep tree and cycle prevention tests.

- [ ] **Q0229 — How would you verify category tree traversal with deep tree and cycle prevention tests, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** cyclic hierarchy and excessive recursion.
  - **Verification scenario:** deep tree and cycle prevention tests.

- [ ] **Q0230 — How would you profile, secure or refactor category tree traversal after it works, while preserving its public contract?**
  - **Acceptance:** Document a measured or justified improvement with regression protection.
  - **Critical failure:** cyclic hierarchy and excessive recursion.
  - **Verification scenario:** deep tree and cycle prevention tests.


## category CRUD application services

- [ ] **Q0231 — How would you design category CRUD application services with explicit rules for ownership checks, slug uniqueness and hierarchy changes?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** delete category with child products.
  - **Verification scenario:** create, move and delete rules.

- [ ] **Q0232 — How would you implement category CRUD application services using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** delete category with child products.
  - **Verification scenario:** create, move and delete rules.

- [ ] **Q0233 — How would you connect category CRUD application services end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** delete category with child products.
  - **Verification scenario:** create, move and delete rules.

- [ ] **Q0234 — How would you prevent or recover from delete category with child products when building category CRUD application services?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** delete category with child products.
  - **Verification scenario:** create, move and delete rules.

- [ ] **Q0235 — How would you verify category CRUD application services with create, move and delete rules, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** delete category with child products.
  - **Verification scenario:** create, move and delete rules.


## category description localization

- [ ] **Q0236 — How would you design category description localization with explicit rules for language-specific names and friendly URLs?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** two categories with same slug in same store.
  - **Verification scenario:** locale fallback and slug uniqueness.

- [ ] **Q0237 — How would you implement category description localization using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** two categories with same slug in same store.
  - **Verification scenario:** locale fallback and slug uniqueness.

- [ ] **Q0238 — How would you connect category description localization end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** two categories with same slug in same store.
  - **Verification scenario:** locale fallback and slug uniqueness.

- [ ] **Q0239 — How would you prevent or recover from two categories with same slug in same store when building category description localization?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** two categories with same slug in same store.
  - **Verification scenario:** locale fallback and slug uniqueness.

- [ ] **Q0240 — How would you verify category description localization with locale fallback and slug uniqueness, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** two categories with same slug in same store.
  - **Verification scenario:** locale fallback and slug uniqueness.


## catalog-category and product-category links

- [ ] **Q0241 — How would you design catalog-category and product-category links with explicit rules for many-to-many membership and presentation order?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** duplicate membership and N+1 loading.
  - **Verification scenario:** multi-category product retrieval.

- [ ] **Q0242 — How would you implement catalog-category and product-category links using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** duplicate membership and N+1 loading.
  - **Verification scenario:** multi-category product retrieval.

- [ ] **Q0243 — How would you connect catalog-category and product-category links end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** duplicate membership and N+1 loading.
  - **Verification scenario:** multi-category product retrieval.

- [ ] **Q0244 — How would you prevent or recover from duplicate membership and N+1 loading when building catalog-category and product-category links?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** duplicate membership and N+1 loading.
  - **Verification scenario:** multi-category product retrieval.

- [ ] **Q0245 — How would you verify catalog-category and product-category links with multi-category product retrieval, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** duplicate membership and N+1 loading.
  - **Verification scenario:** multi-category product retrieval.


## category REST endpoints

- [ ] **Q0246 — How would you design category REST endpoints with explicit rules for list, tree, CRUD, pagination and permission policy?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** unsupported category path and bad request data.
  - **Verification scenario:** HTTP status and store-scope tests.

- [ ] **Q0247 — How would you implement category REST endpoints using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** unsupported category path and bad request data.
  - **Verification scenario:** HTTP status and store-scope tests.

- [ ] **Q0248 — How would you connect category REST endpoints end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** unsupported category path and bad request data.
  - **Verification scenario:** HTTP status and store-scope tests.

- [ ] **Q0249 — How would you prevent or recover from unsupported category path and bad request data when building category REST endpoints?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** unsupported category path and bad request data.
  - **Verification scenario:** HTTP status and store-scope tests.

- [ ] **Q0250 — How would you verify category REST endpoints with HTTP status and store-scope tests, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** unsupported category path and bad request data.
  - **Verification scenario:** HTTP status and store-scope tests.


## category caching and index invalidation

- [ ] **Q0251 — How would you design category caching and index invalidation with explicit rules for tree read optimization and invalidation on edits?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** stale category after a move.
  - **Verification scenario:** cache coherence after update.

- [ ] **Q0252 — How would you implement category caching and index invalidation using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** stale category after a move.
  - **Verification scenario:** cache coherence after update.

- [ ] **Q0253 — How would you connect category caching and index invalidation end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** stale category after a move.
  - **Verification scenario:** cache coherence after update.

- [ ] **Q0254 — How would you prevent or recover from stale category after a move when building category caching and index invalidation?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** stale category after a move.
  - **Verification scenario:** cache coherence after update.

- [ ] **Q0255 — How would you verify category caching and index invalidation with cache coherence after update, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** stale category after a move.
  - **Verification scenario:** cache coherence after update.
