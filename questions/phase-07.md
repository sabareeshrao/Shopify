# Phase 07 — Users, authentication, JWT and permissions

**Task count:** 43 · **IDs:** Q0176–Q0218 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop

Every checklist item is one original development question. Each must be taught with MCQs, implemented incrementally and verified before completion. Tests and evidence belong with the eventual implementation.


## user and role entity mapping

- [ ] **Q0176 — How would you design user and role entity mapping with explicit rules for admin, merchant, staff and customer principals?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** username duplicates and role escalation.
  - **Verification scenario:** user-role persistence and uniqueness.

- [ ] **Q0177 — How would you implement user and role entity mapping using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** username duplicates and role escalation.
  - **Verification scenario:** user-role persistence and uniqueness.

- [ ] **Q0178 — How would you connect user and role entity mapping end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** username duplicates and role escalation.
  - **Verification scenario:** user-role persistence and uniqueness.

- [ ] **Q0179 — How would you prevent or recover from username duplicates and role escalation when building user and role entity mapping?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** username duplicates and role escalation.
  - **Verification scenario:** user-role persistence and uniqueness.

- [ ] **Q0180 — How would you verify user and role entity mapping with user-role persistence and uniqueness, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** username duplicates and role escalation.
  - **Verification scenario:** user-role persistence and uniqueness.

- [ ] **Q0181 — How would you profile, secure or refactor user and role entity mapping after it works, while preserving its public contract?**
  - **Acceptance:** Document a measured or justified improvement with regression protection.
  - **Critical failure:** username duplicates and role escalation.
  - **Verification scenario:** user-role persistence and uniqueness.


## password hashing and credential policy

- [ ] **Q0182 — How would you design password hashing and credential policy with explicit rules for PasswordEncoder, reset tokens and brute-force mitigation?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** plaintext passwords or timing leaks.
  - **Verification scenario:** hash matches and invalid login.

- [ ] **Q0183 — How would you implement password hashing and credential policy using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** plaintext passwords or timing leaks.
  - **Verification scenario:** hash matches and invalid login.

- [ ] **Q0184 — How would you connect password hashing and credential policy end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** plaintext passwords or timing leaks.
  - **Verification scenario:** hash matches and invalid login.

- [ ] **Q0185 — How would you prevent or recover from plaintext passwords or timing leaks when building password hashing and credential policy?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** plaintext passwords or timing leaks.
  - **Verification scenario:** hash matches and invalid login.

- [ ] **Q0186 — How would you verify password hashing and credential policy with hash matches and invalid login, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** plaintext passwords or timing leaks.
  - **Verification scenario:** hash matches and invalid login.

- [ ] **Q0187 — How would you profile, secure or refactor password hashing and credential policy after it works, while preserving its public contract?**
  - **Acceptance:** Document a measured or justified improvement with regression protection.
  - **Critical failure:** plaintext passwords or timing leaks.
  - **Verification scenario:** hash matches and invalid login.


## Spring Security filter chain

- [ ] **Q0188 — How would you design Spring Security filter chain with explicit rules for permit-list, secured routes and CORS configuration?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** public admin endpoint or cross-origin error.
  - **Verification scenario:** 401 vs 403 and preflight tests.

- [ ] **Q0189 — How would you implement Spring Security filter chain using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** public admin endpoint or cross-origin error.
  - **Verification scenario:** 401 vs 403 and preflight tests.

- [ ] **Q0190 — How would you connect Spring Security filter chain end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** public admin endpoint or cross-origin error.
  - **Verification scenario:** 401 vs 403 and preflight tests.

- [ ] **Q0191 — How would you prevent or recover from public admin endpoint or cross-origin error when building Spring Security filter chain?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** public admin endpoint or cross-origin error.
  - **Verification scenario:** 401 vs 403 and preflight tests.

- [ ] **Q0192 — How would you verify Spring Security filter chain with 401 vs 403 and preflight tests, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** public admin endpoint or cross-origin error.
  - **Verification scenario:** 401 vs 403 and preflight tests.

- [ ] **Q0193 — How would you profile, secure or refactor Spring Security filter chain after it works, while preserving its public contract?**
  - **Acceptance:** Document a measured or justified improvement with regression protection.
  - **Critical failure:** public admin endpoint or cross-origin error.
  - **Verification scenario:** 401 vs 403 and preflight tests.


## JWT issuance and verification

- [ ] **Q0194 — How would you design JWT issuance and verification with explicit rules for signature, issuer, audience, expiration and signing keys?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** expired, altered or wrong-audience JWT.
  - **Verification scenario:** positive and tampered token tests.

- [ ] **Q0195 — How would you implement JWT issuance and verification using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** expired, altered or wrong-audience JWT.
  - **Verification scenario:** positive and tampered token tests.

- [ ] **Q0196 — How would you connect JWT issuance and verification end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** expired, altered or wrong-audience JWT.
  - **Verification scenario:** positive and tampered token tests.

- [ ] **Q0197 — How would you prevent or recover from expired, altered or wrong-audience JWT when building JWT issuance and verification?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** expired, altered or wrong-audience JWT.
  - **Verification scenario:** positive and tampered token tests.

- [ ] **Q0198 — How would you verify JWT issuance and verification with positive and tampered token tests, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** expired, altered or wrong-audience JWT.
  - **Verification scenario:** positive and tampered token tests.


## refresh and session revocation strategy

- [ ] **Q0199 — How would you design refresh and session revocation strategy with explicit rules for token rotation, expiry and revocation semantics?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** stolen refresh token replay.
  - **Verification scenario:** logout and reused refresh token rejection.

- [ ] **Q0200 — How would you implement refresh and session revocation strategy using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** stolen refresh token replay.
  - **Verification scenario:** logout and reused refresh token rejection.

- [ ] **Q0201 — How would you connect refresh and session revocation strategy end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** stolen refresh token replay.
  - **Verification scenario:** logout and reused refresh token rejection.

- [ ] **Q0202 — How would you prevent or recover from stolen refresh token replay when building refresh and session revocation strategy?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** stolen refresh token replay.
  - **Verification scenario:** logout and reused refresh token rejection.

- [ ] **Q0203 — How would you verify refresh and session revocation strategy with logout and reused refresh token rejection, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** stolen refresh token replay.
  - **Verification scenario:** logout and reused refresh token rejection.


## role and tenant authorization

- [ ] **Q0204 — How would you design role and tenant authorization with explicit rules for @PreAuthorize, method security and owner checks?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** horizontal privilege escalation between stores.
  - **Verification scenario:** merchant A blocked from merchant B.

- [ ] **Q0205 — How would you implement role and tenant authorization using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** horizontal privilege escalation between stores.
  - **Verification scenario:** merchant A blocked from merchant B.

- [ ] **Q0206 — How would you connect role and tenant authorization end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** horizontal privilege escalation between stores.
  - **Verification scenario:** merchant A blocked from merchant B.

- [ ] **Q0207 — How would you prevent or recover from horizontal privilege escalation between stores when building role and tenant authorization?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** horizontal privilege escalation between stores.
  - **Verification scenario:** merchant A blocked from merchant B.

- [ ] **Q0208 — How would you verify role and tenant authorization with merchant A blocked from merchant B, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** horizontal privilege escalation between stores.
  - **Verification scenario:** merchant A blocked from merchant B.


## customer login and account recovery

- [ ] **Q0209 — How would you design customer login and account recovery with explicit rules for registration, login, forgot password and reset token flows?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** email enumeration and token reuse.
  - **Verification scenario:** reset consumed once and password changes.

- [ ] **Q0210 — How would you implement customer login and account recovery using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** email enumeration and token reuse.
  - **Verification scenario:** reset consumed once and password changes.

- [ ] **Q0211 — How would you connect customer login and account recovery end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** email enumeration and token reuse.
  - **Verification scenario:** reset consumed once and password changes.

- [ ] **Q0212 — How would you prevent or recover from email enumeration and token reuse when building customer login and account recovery?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** email enumeration and token reuse.
  - **Verification scenario:** reset consumed once and password changes.

- [ ] **Q0213 — How would you verify customer login and account recovery with reset consumed once and password changes, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** email enumeration and token reuse.
  - **Verification scenario:** reset consumed once and password changes.


## security audit and rate limiting

- [ ] **Q0214 — How would you design security audit and rate limiting with explicit rules for login events, trace IDs, throttling and secret redaction?**
  - **Acceptance:** Write concrete domain contracts, state transitions and constraints.
  - **Critical failure:** credential stuffing and PII in logs.
  - **Verification scenario:** rate-limit and log redaction checks.

- [ ] **Q0215 — How would you implement security audit and rate limiting using Java 21 and the correct module or database model?**
  - **Acceptance:** Commit compilable code, schema changes or executable frontend state as appropriate.
  - **Critical failure:** credential stuffing and PII in logs.
  - **Verification scenario:** rate-limit and log redaction checks.

- [ ] **Q0216 — How would you connect security audit and rate limiting end-to-end through service/API layers and return a documented result?**
  - **Acceptance:** Run a working use case through real components, not hardcoded demo output.
  - **Critical failure:** credential stuffing and PII in logs.
  - **Verification scenario:** rate-limit and log redaction checks.

- [ ] **Q0217 — How would you prevent or recover from credential stuffing and PII in logs when building security audit and rate limiting?**
  - **Acceptance:** Show a reproducible failure and an explicit, safe handling strategy.
  - **Critical failure:** credential stuffing and PII in logs.
  - **Verification scenario:** rate-limit and log redaction checks.

- [ ] **Q0218 — How would you verify security audit and rate limiting with rate-limit and log redaction checks, including automated positive and negative tests?**
  - **Acceptance:** Record passing test commands, expected behavior and evidence.
  - **Critical failure:** credential stuffing and PII in logs.
  - **Verification scenario:** rate-limit and log redaction checks.
