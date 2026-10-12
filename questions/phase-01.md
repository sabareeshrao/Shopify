# Phase 01 — Java 21, IntelliJ, Git and Maven environment

**Canonical IDs:** Q0013 onward · **Planned tasks:** 20 · **Status:** NOT STARTED

**Reference area:** https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/pom.xml

Questions are development tasks, not MCQ answers. Implementation generates separate MCQs later. A checked box must have code/artifact evidence and an updated tracker.


## Java 21 and IntelliJ IDEA SDK configuration

- [ ] **Q0013 — How would you examine and specify Java 21 and IntelliJ IDEA SDK configuration, documenting JDK vs JRE, language level, project and module SDKs before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** incorrect JAVA_HOME or Java 11 selected by Maven.
  - **Proof focus:** java -version, mvn -version and compiling a Java 21 record.

- [ ] **Q0014 — How would you create the minimal reproducible workspace or architecture artifact for Java 21 and IntelliJ IDEA SDK configuration without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating JDK vs JRE, language level, project and module SDKs.
  - **Edge/failure to consider:** incorrect JAVA_HOME or Java 11 selected by Maven.
  - **Proof focus:** java -version, mvn -version and compiling a Java 21 record.

- [ ] **Q0015 — How would you diagnose incorrect JAVA_HOME or Java 11 selected by Maven while establishing Java 21 and IntelliJ IDEA SDK configuration, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** incorrect JAVA_HOME or Java 11 selected by Maven.
  - **Proof focus:** java -version, mvn -version and compiling a Java 21 record.

- [ ] **Q0016 — How would you verify Java 21 and IntelliJ IDEA SDK configuration from a clean checkout, specifically using java -version, mvn -version and compiling a Java 21 record?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** incorrect JAVA_HOME or Java 11 selected by Maven.
  - **Proof focus:** java -version, mvn -version and compiling a Java 21 record.

- [ ] **Q0017 — How would you explain the architectural trade-offs and alternatives for Java 21 and IntelliJ IDEA SDK configuration in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** incorrect JAVA_HOME or Java 11 selected by Maven.
  - **Proof focus:** java -version, mvn -version and compiling a Java 21 record.


## Maven wrapper and reproducible dependency resolution

- [ ] **Q0018 — How would you examine and specify Maven wrapper and reproducible dependency resolution, documenting mvnw, Maven Central and offline versus online behavior before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** dependency conflicts, plugin mismatches and failed downloads.
  - **Proof focus:** clean package from the wrapper on a second machine.

- [ ] **Q0019 — How would you create the minimal reproducible workspace or architecture artifact for Maven wrapper and reproducible dependency resolution without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating mvnw, Maven Central and offline versus online behavior.
  - **Edge/failure to consider:** dependency conflicts, plugin mismatches and failed downloads.
  - **Proof focus:** clean package from the wrapper on a second machine.

- [ ] **Q0020 — How would you diagnose dependency conflicts, plugin mismatches and failed downloads while establishing Maven wrapper and reproducible dependency resolution, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** dependency conflicts, plugin mismatches and failed downloads.
  - **Proof focus:** clean package from the wrapper on a second machine.

- [ ] **Q0021 — How would you verify Maven wrapper and reproducible dependency resolution from a clean checkout, specifically using clean package from the wrapper on a second machine?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** dependency conflicts, plugin mismatches and failed downloads.
  - **Proof focus:** clean package from the wrapper on a second machine.

- [ ] **Q0022 — How would you explain the architectural trade-offs and alternatives for Maven wrapper and reproducible dependency resolution in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** dependency conflicts, plugin mismatches and failed downloads.
  - **Proof focus:** clean package from the wrapper on a second machine.


## Git repository and branch workflow

- [ ] **Q0023 — How would you examine and specify Git repository and branch workflow, documenting status, staging, commits, ignore rules and remote tracking before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** accidental secrets or generated binaries being committed.
  - **Proof focus:** tracked tree cleanliness and verified remote commit.

- [ ] **Q0024 — How would you create the minimal reproducible workspace or architecture artifact for Git repository and branch workflow without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating status, staging, commits, ignore rules and remote tracking.
  - **Edge/failure to consider:** accidental secrets or generated binaries being committed.
  - **Proof focus:** tracked tree cleanliness and verified remote commit.

- [ ] **Q0025 — How would you diagnose accidental secrets or generated binaries being committed while establishing Git repository and branch workflow, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** accidental secrets or generated binaries being committed.
  - **Proof focus:** tracked tree cleanliness and verified remote commit.

- [ ] **Q0026 — How would you verify Git repository and branch workflow from a clean checkout, specifically using tracked tree cleanliness and verified remote commit?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** accidental secrets or generated binaries being committed.
  - **Proof focus:** tracked tree cleanliness and verified remote commit.

- [ ] **Q0027 — How would you explain the architectural trade-offs and alternatives for Git repository and branch workflow in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** accidental secrets or generated binaries being committed.
  - **Proof focus:** tracked tree cleanliness and verified remote commit.


## local tools for HTTP and relational persistence

- [ ] **Q0028 — How would you examine and specify local tools for HTTP and relational persistence, documenting MySQL, Postman, Docker Compose and terminal configuration before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** database port collisions, bad credentials and lost connections.
  - **Proof focus:** an authenticated MySQL connection and saved HTTP request.

- [ ] **Q0029 — How would you create the minimal reproducible workspace or architecture artifact for local tools for HTTP and relational persistence without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating MySQL, Postman, Docker Compose and terminal configuration.
  - **Edge/failure to consider:** database port collisions, bad credentials and lost connections.
  - **Proof focus:** an authenticated MySQL connection and saved HTTP request.

- [ ] **Q0030 — How would you diagnose database port collisions, bad credentials and lost connections while establishing local tools for HTTP and relational persistence, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** database port collisions, bad credentials and lost connections.
  - **Proof focus:** an authenticated MySQL connection and saved HTTP request.

- [ ] **Q0031 — How would you verify local tools for HTTP and relational persistence from a clean checkout, specifically using an authenticated MySQL connection and saved HTTP request?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** database port collisions, bad credentials and lost connections.
  - **Proof focus:** an authenticated MySQL connection and saved HTTP request.

- [ ] **Q0032 — How would you explain the architectural trade-offs and alternatives for local tools for HTTP and relational persistence in a five-year Java interview?**
  - **Acceptance:** A defensible design decision and at least one rejected alternative.
  - **Edge/failure to consider:** database port collisions, bad credentials and lost connections.
  - **Proof focus:** an authenticated MySQL connection and saved HTTP request.
