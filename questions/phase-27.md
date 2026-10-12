# Phase 27 — Docker, CI/CD, monitoring and deployment

**Questions:** 38 · **IDs:** Q0988–Q1025 · **Status:** NOT STARTED

**Reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop

Each question is a real build/test task. A box is checked only after concrete code, an observed outcome, and a matching tracker commit.


## backend Docker image and runtime hardening

- [ ] **Q0988 — How would you specify backend Docker image and runtime hardening with explicit contracts for multi-stage build, JRE runtime, non-root and health check and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** broken start script or baked secret.
  - **Verification:** run image with least privileges.

- [ ] **Q0989 — How would you implement backend Docker image and runtime hardening with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** broken start script or baked secret.
  - **Verification:** run image with least privileges.

- [ ] **Q0990 — How would you integrate backend Docker image and runtime hardening into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** broken start script or baked secret.
  - **Verification:** run image with least privileges.

- [ ] **Q0991 — How would you detect and recover from broken start script or baked secret while implementing backend Docker image and runtime hardening?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** broken start script or baked secret.
  - **Verification:** run image with least privileges.

- [ ] **Q0992 — How would you demonstrate run image with least privileges with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** broken start script or baked secret.
  - **Verification:** run image with least privileges.


## local Docker Compose environment

- [ ] **Q0993 — How would you specify local Docker Compose environment with explicit contracts for API, MySQL, frontend and supporting services and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** startup ordering or bad volumes.
  - **Verification:** fresh environment boots with one command.

- [ ] **Q0994 — How would you implement local Docker Compose environment with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** startup ordering or bad volumes.
  - **Verification:** fresh environment boots with one command.

- [ ] **Q0995 — How would you integrate local Docker Compose environment into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** startup ordering or bad volumes.
  - **Verification:** fresh environment boots with one command.

- [ ] **Q0996 — How would you detect and recover from startup ordering or bad volumes while implementing local Docker Compose environment?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** startup ordering or bad volumes.
  - **Verification:** fresh environment boots with one command.

- [ ] **Q0997 — How would you demonstrate fresh environment boots with one command with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** startup ordering or bad volumes.
  - **Verification:** fresh environment boots with one command.


## GitHub Actions build/test pipeline

- [ ] **Q0998 — How would you specify GitHub Actions build/test pipeline with explicit contracts for Java 21 matrix, Maven cache, lint and artifact publication and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** broken tests merged or exposed credentials.
  - **Verification:** PR CI fail/pass scenarios.

- [ ] **Q0999 — How would you implement GitHub Actions build/test pipeline with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** broken tests merged or exposed credentials.
  - **Verification:** PR CI fail/pass scenarios.

- [ ] **Q1000 — How would you integrate GitHub Actions build/test pipeline into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** broken tests merged or exposed credentials.
  - **Verification:** PR CI fail/pass scenarios.

- [ ] **Q1001 — How would you detect and recover from broken tests merged or exposed credentials while implementing GitHub Actions build/test pipeline?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** broken tests merged or exposed credentials.
  - **Verification:** PR CI fail/pass scenarios.

- [ ] **Q1002 — How would you demonstrate PR CI fail/pass scenarios with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** broken tests merged or exposed credentials.
  - **Verification:** PR CI fail/pass scenarios.


## database migration at deployment

- [ ] **Q1003 — How would you specify database migration at deployment with explicit contracts for schema versioning, rollout and rollback planning and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** new code deployed before schema.
  - **Verification:** fresh and upgrade release tests.

- [ ] **Q1004 — How would you implement database migration at deployment with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** new code deployed before schema.
  - **Verification:** fresh and upgrade release tests.

- [ ] **Q1005 — How would you integrate database migration at deployment into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** new code deployed before schema.
  - **Verification:** fresh and upgrade release tests.

- [ ] **Q1006 — How would you detect and recover from new code deployed before schema while implementing database migration at deployment?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** new code deployed before schema.
  - **Verification:** fresh and upgrade release tests.

- [ ] **Q1007 — How would you demonstrate fresh and upgrade release tests with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** new code deployed before schema.
  - **Verification:** fresh and upgrade release tests.


## cloud configuration and deployment boundaries

- [ ] **Q1008 — How would you specify cloud configuration and deployment boundaries with explicit contracts for environment secrets, staging and deployment isolation and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** production secrets committed or mixed environments.
  - **Verification:** isolated stage deployment.

- [ ] **Q1009 — How would you implement cloud configuration and deployment boundaries with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** production secrets committed or mixed environments.
  - **Verification:** isolated stage deployment.

- [ ] **Q1010 — How would you integrate cloud configuration and deployment boundaries into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** production secrets committed or mixed environments.
  - **Verification:** isolated stage deployment.

- [ ] **Q1011 — How would you detect and recover from production secrets committed or mixed environments while implementing cloud configuration and deployment boundaries?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** production secrets committed or mixed environments.
  - **Verification:** isolated stage deployment.

- [ ] **Q1012 — How would you demonstrate isolated stage deployment with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** production secrets committed or mixed environments.
  - **Verification:** isolated stage deployment.


## structured logging and tracing

- [ ] **Q1013 — How would you specify structured logging and tracing with explicit contracts for request IDs, spans, correlation and PII masking and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** missing logs during checkout failure.
  - **Verification:** follow one order across logs.

- [ ] **Q1014 — How would you implement structured logging and tracing with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** missing logs during checkout failure.
  - **Verification:** follow one order across logs.

- [ ] **Q1015 — How would you integrate structured logging and tracing into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** missing logs during checkout failure.
  - **Verification:** follow one order across logs.

- [ ] **Q1016 — How would you detect and recover from missing logs during checkout failure while implementing structured logging and tracing?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** missing logs during checkout failure.
  - **Verification:** follow one order across logs.

- [ ] **Q1017 — How would you demonstrate follow one order across logs with automated regression checks and captured expected output?**
  - **Acceptance:** Test suite and verification commands passing.
  - **Failure case:** missing logs during checkout failure.
  - **Verification:** follow one order across logs.


## metrics, alerting and runbooks

- [ ] **Q1018 — How would you specify metrics, alerting and runbooks with explicit contracts for health, latency, errors, JVM and database saturation and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** alert storm or silent checkout outage.
  - **Verification:** documented alert and recovery drills.

- [ ] **Q1019 — How would you implement metrics, alerting and runbooks with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** alert storm or silent checkout outage.
  - **Verification:** documented alert and recovery drills.

- [ ] **Q1020 — How would you integrate metrics, alerting and runbooks into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** alert storm or silent checkout outage.
  - **Verification:** documented alert and recovery drills.

- [ ] **Q1021 — How would you detect and recover from alert storm or silent checkout outage while implementing metrics, alerting and runbooks?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** alert storm or silent checkout outage.
  - **Verification:** documented alert and recovery drills.


## release acceptance and handover

- [ ] **Q1022 — How would you specify release acceptance and handover with explicit contracts for repeatable setup, sample data, architecture and documentation and measurable completion criteria?**
  - **Acceptance:** Documented inputs, expected behavior, ownership boundaries and risks.
  - **Failure case:** new developer cannot reproduce deploy.
  - **Verification:** clone-to-checkout demonstration.

- [ ] **Q1023 — How would you implement release acceptance and handover with reproducible configuration, executable code and documented commands?**
  - **Acceptance:** Runnable source/configuration committed in the correct directory.
  - **Failure case:** new developer cannot reproduce deploy.
  - **Verification:** clone-to-checkout demonstration.

- [ ] **Q1024 — How would you integrate release acceptance and handover into the complete commerce application without introducing hidden manual setup?**
  - **Acceptance:** Working integrated end-to-end application behavior.
  - **Failure case:** new developer cannot reproduce deploy.
  - **Verification:** clone-to-checkout demonstration.

- [ ] **Q1025 — How would you detect and recover from new developer cannot reproduce deploy while implementing release acceptance and handover?**
  - **Acceptance:** Failure reproduced and safely handled, with explicit result.
  - **Failure case:** new developer cannot reproduce deploy.
  - **Verification:** clone-to-checkout demonstration.
