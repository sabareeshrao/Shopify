# Phase 02 — Spring Boot and modular application skeleton

**Canonical IDs:** Q0033 onward · **Planned tasks:** 26 · **Status:** NOT STARTED

**Reference area:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop

Questions are development tasks, not MCQ answers. Implementation generates separate MCQs later. A checked box must have code/artifact evidence and an updated tracker.


## Java 21 compatible parent POM and module layout

- [ ] **Q0033 — How would you examine and specify Java 21 compatible parent POM and module layout, documenting domain, integrations, core services, API model and executable API modules before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** mixing incompatible Spring/Jakarta dependencies.
  - **Proof focus:** mvn clean verify across all modules.

- [ ] **Q0034 — How would you create the minimal reproducible workspace or architecture artifact for Java 21 compatible parent POM and module layout without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating domain, integrations, core services, API model and executable API modules.
  - **Edge/failure to consider:** mixing incompatible Spring/Jakarta dependencies.
  - **Proof focus:** mvn clean verify across all modules.

- [ ] **Q0035 — How would you diagnose mixing incompatible Spring/Jakarta dependencies while establishing Java 21 compatible parent POM and module layout, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** mixing incompatible Spring/Jakarta dependencies.
  - **Proof focus:** mvn clean verify across all modules.

- [ ] **Q0036 — How would you verify Java 21 compatible parent POM and module layout from a clean checkout, specifically using mvn clean verify across all modules?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** mixing incompatible Spring/Jakarta dependencies.
  - **Proof focus:** mvn clean verify across all modules.

- [ ] **Q0037 — How would you explain the architectural trade-offs and alternatives for Java 21 compatible parent POM and module layout in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** mixing incompatible Spring/Jakarta dependencies.
  - **Proof focus:** mvn clean verify across all modules.

- [ ] **Q0038 — How would you review Java 21 compatible parent POM and module layout for security, reproducibility and future maintenance before accepting it?**
  - **Acceptance:** Peer-review checklist with identified risks and mitigations.
  - **Edge/failure to consider:** mixing incompatible Spring/Jakarta dependencies.
  - **Proof focus:** mvn clean verify across all modules.


## Spring Boot bootstrap and dependency injection

- [ ] **Q0039 — How would you examine and specify Spring Boot bootstrap and dependency injection, documenting main application, bean scopes, constructor injection and component scanning before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** missing bean or ambiguous dependency at startup.
  - **Proof focus:** context startup test and injected service response.

- [ ] **Q0040 — How would you create the minimal reproducible workspace or architecture artifact for Spring Boot bootstrap and dependency injection without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating main application, bean scopes, constructor injection and component scanning.
  - **Edge/failure to consider:** missing bean or ambiguous dependency at startup.
  - **Proof focus:** context startup test and injected service response.

- [ ] **Q0041 — How would you diagnose missing bean or ambiguous dependency at startup while establishing Spring Boot bootstrap and dependency injection, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** missing bean or ambiguous dependency at startup.
  - **Proof focus:** context startup test and injected service response.

- [ ] **Q0042 — How would you verify Spring Boot bootstrap and dependency injection from a clean checkout, specifically using context startup test and injected service response?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** missing bean or ambiguous dependency at startup.
  - **Proof focus:** context startup test and injected service response.

- [ ] **Q0043 — How would you explain the architectural trade-offs and alternatives for Spring Boot bootstrap and dependency injection in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** missing bean or ambiguous dependency at startup.
  - **Proof focus:** context startup test and injected service response.


## configuration profiles and typed properties

- [ ] **Q0044 — How would you examine and specify configuration profiles and typed properties, documenting local, test and production settings with safe environment overrides before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** committing credentials and configuration binding errors.
  - **Proof focus:** separate profile startup with verified properties.

- [ ] **Q0045 — How would you create the minimal reproducible workspace or architecture artifact for configuration profiles and typed properties without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating local, test and production settings with safe environment overrides.
  - **Edge/failure to consider:** committing credentials and configuration binding errors.
  - **Proof focus:** separate profile startup with verified properties.

- [ ] **Q0046 — How would you diagnose committing credentials and configuration binding errors while establishing configuration profiles and typed properties, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** committing credentials and configuration binding errors.
  - **Proof focus:** separate profile startup with verified properties.

- [ ] **Q0047 — How would you verify configuration profiles and typed properties from a clean checkout, specifically using separate profile startup with verified properties?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** committing credentials and configuration binding errors.
  - **Proof focus:** separate profile startup with verified properties.

- [ ] **Q0048 — How would you explain the architectural trade-offs and alternatives for configuration profiles and typed properties in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** committing credentials and configuration binding errors.
  - **Proof focus:** separate profile startup with verified properties.


## logging, health checks and exception boundaries

- [ ] **Q0049 — How would you examine and specify logging, health checks and exception boundaries, documenting structured logs, Actuator, controller advice and correlation IDs before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** leaking secrets or stack traces in API responses.
  - **Proof focus:** healthy startup and structured failure responses.

- [ ] **Q0050 — How would you create the minimal reproducible workspace or architecture artifact for logging, health checks and exception boundaries without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating structured logs, Actuator, controller advice and correlation IDs.
  - **Edge/failure to consider:** leaking secrets or stack traces in API responses.
  - **Proof focus:** healthy startup and structured failure responses.

- [ ] **Q0051 — How would you diagnose leaking secrets or stack traces in API responses while establishing logging, health checks and exception boundaries, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** leaking secrets or stack traces in API responses.
  - **Proof focus:** healthy startup and structured failure responses.

- [ ] **Q0052 — How would you verify logging, health checks and exception boundaries from a clean checkout, specifically using healthy startup and structured failure responses?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** leaking secrets or stack traces in API responses.
  - **Proof focus:** healthy startup and structured failure responses.

- [ ] **Q0053 — How would you explain the architectural trade-offs and alternatives for logging, health checks and exception boundaries in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** leaking secrets or stack traces in API responses.
  - **Proof focus:** healthy startup and structured failure responses.


## first vertical REST feature with module dependencies

- [ ] **Q0054 — How would you examine and specify first vertical REST feature with module dependencies, documenting controller to application service to domain model response before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** putting business rules directly in controller or cyclic imports.
  - **Proof focus:** GET endpoint verified in Postman and MockMvc.

- [ ] **Q0055 — How would you create the minimal reproducible workspace or architecture artifact for first vertical REST feature with module dependencies without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating controller to application service to domain model response.
  - **Edge/failure to consider:** putting business rules directly in controller or cyclic imports.
  - **Proof focus:** GET endpoint verified in Postman and MockMvc.

- [ ] **Q0056 — How would you diagnose putting business rules directly in controller or cyclic imports while establishing first vertical REST feature with module dependencies, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** putting business rules directly in controller or cyclic imports.
  - **Proof focus:** GET endpoint verified in Postman and MockMvc.

- [ ] **Q0057 — How would you verify first vertical REST feature with module dependencies from a clean checkout, specifically using GET endpoint verified in Postman and MockMvc?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** putting business rules directly in controller or cyclic imports.
  - **Proof focus:** GET endpoint verified in Postman and MockMvc.

- [ ] **Q0058 — How would you explain the architectural trade-offs and alternatives for first vertical REST feature with module dependencies in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** putting business rules directly in controller or cyclic imports.
  - **Proof focus:** GET endpoint verified in Postman and MockMvc.
