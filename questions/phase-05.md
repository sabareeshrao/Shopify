# Phase 05 — Countries, currencies, languages and reference data

**Task count:** 25 · **IDs:** Q0116–Q0140 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model

Every checklist item is one original development question. Each must be taught with MCQs, implemented incrementally and verified before completion. Tests and evidence belong with the eventual implementation.


## country and region reference entities

- [ ] **Q0116 — How would you design country and region reference entities with explicit rules for ISO codes, subdivisions and address fields?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** an unsupported or malformed region.
  - **Verification scenario:** country/zone lookups and unique-code enforcement.

- [ ] **Q0117 — How would you implement country and region reference entities using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** an unsupported or malformed region.
  - **Verification scenario:** country/zone lookups and unique-code enforcement.

- [ ] **Q0118 — How would you connect country and region reference entities end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** an unsupported or malformed region.
  - **Verification scenario:** country/zone lookups and unique-code enforcement.

- [ ] **Q0119 — How would you prevent or recover from an unsupported or malformed region when building country and region reference entities?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** an unsupported or malformed region.
  - **Verification scenario:** country/zone lookups and unique-code enforcement.

- [ ] **Q0120 — How would you verify country and region reference entities with country/zone lookups and unique-code enforcement, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** an unsupported or malformed region.
  - **Verification scenario:** country/zone lookups and unique-code enforcement.


## currency reference model and BigDecimal formatting

- [ ] **Q0121 — How would you design currency reference model and BigDecimal formatting with explicit rules for ISO currency codes, minor units and monetary precision?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** float rounding or unknown currency.
  - **Verification scenario:** different currency scale and precision cases.

- [ ] **Q0122 — How would you implement currency reference model and BigDecimal formatting using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** float rounding or unknown currency.
  - **Verification scenario:** different currency scale and precision cases.

- [ ] **Q0123 — How would you connect currency reference model and BigDecimal formatting end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** float rounding or unknown currency.
  - **Verification scenario:** different currency scale and precision cases.

- [ ] **Q0124 — How would you prevent or recover from float rounding or unknown currency when building currency reference model and BigDecimal formatting?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** float rounding or unknown currency.
  - **Verification scenario:** different currency scale and precision cases.

- [ ] **Q0125 — How would you verify currency reference model and BigDecimal formatting with different currency scale and precision cases, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** float rounding or unknown currency.
  - **Verification scenario:** different currency scale and precision cases.


## localized descriptions and language preferences

- [ ] **Q0126 — How would you design localized descriptions and language preferences with explicit rules for locale fallback, translation keys and UTF-8 strings?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** missing translation or invalid locale.
  - **Verification scenario:** English and second-language fallback.

- [ ] **Q0127 — How would you implement localized descriptions and language preferences using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** missing translation or invalid locale.
  - **Verification scenario:** English and second-language fallback.

- [ ] **Q0128 — How would you connect localized descriptions and language preferences end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** missing translation or invalid locale.
  - **Verification scenario:** English and second-language fallback.

- [ ] **Q0129 — How would you prevent or recover from missing translation or invalid locale when building localized descriptions and language preferences?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** missing translation or invalid locale.
  - **Verification scenario:** English and second-language fallback.

- [ ] **Q0130 — How would you verify localized descriptions and language preferences with English and second-language fallback, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** missing translation or invalid locale.
  - **Verification scenario:** English and second-language fallback.


## bootstrap reference-data migrations

- [ ] **Q0131 — How would you design bootstrap reference-data migrations with explicit rules for idempotent country, currency and zone seeding?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** rerunning seed creates duplicate records.
  - **Verification scenario:** empty database and repeated startup.

- [ ] **Q0132 — How would you implement bootstrap reference-data migrations using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** rerunning seed creates duplicate records.
  - **Verification scenario:** empty database and repeated startup.

- [ ] **Q0133 — How would you connect bootstrap reference-data migrations end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** rerunning seed creates duplicate records.
  - **Verification scenario:** empty database and repeated startup.

- [ ] **Q0134 — How would you prevent or recover from rerunning seed creates duplicate records when building bootstrap reference-data migrations?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** rerunning seed creates duplicate records.
  - **Verification scenario:** empty database and repeated startup.

- [ ] **Q0135 — How would you verify bootstrap reference-data migrations with empty database and repeated startup, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** rerunning seed creates duplicate records.
  - **Verification scenario:** empty database and repeated startup.


## reference data REST endpoints

- [ ] **Q0136 — How would you design reference data REST endpoints with explicit rules for read-only public lists, caching and pagination?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** misconfigured public access or stale cache.
  - **Verification scenario:** OpenAPI and HTTP tests for country, zone and currency.

- [ ] **Q0137 — How would you implement reference data REST endpoints using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** misconfigured public access or stale cache.
  - **Verification scenario:** OpenAPI and HTTP tests for country, zone and currency.

- [ ] **Q0138 — How would you connect reference data REST endpoints end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** misconfigured public access or stale cache.
  - **Verification scenario:** OpenAPI and HTTP tests for country, zone and currency.

- [ ] **Q0139 — How would you prevent or recover from misconfigured public access or stale cache when building reference data REST endpoints?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** misconfigured public access or stale cache.
  - **Verification scenario:** OpenAPI and HTTP tests for country, zone and currency.

- [ ] **Q0140 — How would you verify reference data REST endpoints with OpenAPI and HTTP tests for country, zone and currency, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** misconfigured public access or stale cache.
  - **Verification scenario:** OpenAPI and HTTP tests for country, zone and currency.
