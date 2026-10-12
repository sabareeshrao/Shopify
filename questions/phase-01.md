# Phase 01 — Java 21, IntelliJ IDEA, Maven and Git

**Canonical range:** Q0013–Q0032 · **20 original tasks** · **Status:** NOT STARTED

**Objective:** Build the development environment from zero using IntelliJ IDEA, with reproducible commands and no hidden setup. The full Shopizer application is **not** copied into this project.

**Reference:** https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/pom.xml

## Q0013

- [ ] **Q0013 — How would you install and verify Microsoft OpenJDK 21 and distinguish the JDK, JVM and JRE on the target machine?**
  - **Acceptance:** Run java -version and javac -version, record the actual installation path.
  - **Failure to practice:** A Java 17/11 runtime is selected unexpectedly.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0014

- [ ] **Q0014 — How would you configure JAVA_HOME and PATH so the terminal and IntelliJ use the same Java 21 installation?**
  - **Acceptance:** Record shell-specific environment variables and confirm both tools agree.
  - **Failure to practice:** Maven runs with a different Java version.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0015

- [ ] **Q0015 — How would you create the initial empty Java project in IntelliJ IDEA using Maven and Java 21 without copying Shopizer source?**
  - **Acceptance:** Show all wizard choices and the generated project root.
  - **Failure to practice:** The IDE creates a nested or wrong project directory.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0016

- [ ] **Q0016 — How would you explain and verify the Maven project directory conventions for src/main/java, src/test/java and pom.xml?**
  - **Acceptance:** Create a tiny class and matching test source folder.
  - **Failure to practice:** Java files exist outside source roots.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0017

- [ ] **Q0017 — How would you generate or adopt a version-controlled Maven wrapper and verify a clean compile?**
  - **Acceptance:** Run mvnw compile with explicit JDK and record outputs.
  - **Failure to practice:** Global Maven version mismatch.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0018

- [ ] **Q0018 — How would you initialize clean Git tracking and safe ignore rules for target/, .idea/, logs, DB files and secrets?**
  - **Acceptance:** Commit only intended source files and prove ignored files remain untracked.
  - **Failure to practice:** Accidentally checking in credentials or generated .class files.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0019

- [ ] **Q0019 — How would you connect IntelliJ Git to the existing Shopify repository and verify push/pull permissions?**
  - **Acceptance:** Document branch, remote origin and the precise starting commit.
  - **Failure to practice:** Pushing over someone else's changes or to the wrong remote.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0020

- [ ] **Q0020 — How would you set up a feature-branch and commit-message convention tied to stable question IDs?**
  - **Acceptance:** Create a harmless test branch and return cleanly to main.
  - **Failure to practice:** Task evidence becomes impossible to trace to a commit.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0021

- [ ] **Q0021 — How would you write a reproducible development-environment README that another Java learner can follow from a fresh checkout?**
  - **Acceptance:** Document SDK, Maven wrapper, MySQL, commands and troubleshooting.
  - **Failure to practice:** Hidden local configuration needed to build.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0022

- [ ] **Q0022 — How would you create a Java 21 Hello World class and run it in IntelliJ and through Maven?**
  - **Acceptance:** Capture the exact console output of both runs.
  - **Failure to practice:** Class or main method not found.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0023

- [ ] **Q0023 — How would you implement a minimal immutable Java record and test its generated equals/hashCode behavior?**
  - **Acceptance:** Show a passing JUnit assertion on two equivalent records.
  - **Failure to practice:** Comparing record references instead of logical equality.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0024

- [ ] **Q0024 — How would you add JUnit 5 dependencies and execute one meaningful passing and one deliberately failing test?**
  - **Acceptance:** Record surefire output and then restore a green suite.
  - **Failure to practice:** Tests are silently skipped.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0025

- [ ] **Q0025 — How would you demonstrate the Maven validate, compile, test, package and verify lifecycle stages?**
  - **Acceptance:** Capture which plugins and output artifacts run at each stage.
  - **Failure to practice:** Confusing the Maven phase with a Java method.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0026

- [ ] **Q0026 — How would you diagnose and resolve a deliberately incompatible or conflicting Maven dependency?**
  - **Acceptance:** Use dependency:tree and record root cause and corrected graph.
  - **Failure to practice:** Uncontrolled transitive dependency mismatch.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0027

- [ ] **Q0027 — How would you configure IntelliJ debugging with a breakpoint, step into, step over, watches and variable inspection?**
  - **Acceptance:** Provide a reproducible breakpoint demonstration for the record test.
  - **Failure to practice:** Debugger points to stale compiled code.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0028

- [ ] **Q0028 — How would you install or configure the MySQL server or reproducible local container for development?**
  - **Acceptance:** Show the running service, listening port and connection credentials handling.
  - **Failure to practice:** Port conflict or passwords committed to Git.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0029

- [ ] **Q0029 — How would you create an isolated local MySQL user/database with suitable minimum privileges for app development?**
  - **Acceptance:** Verify the user can connect but cannot access unrelated databases.
  - **Failure to practice:** Developing permanently as MySQL root.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0030

- [ ] **Q0030 — How would you set up Postman collections/environments without storing real bearer tokens in committed files?**
  - **Acceptance:** Save a sample request with environment variable placeholders.
  - **Failure to practice:** Leaking credentials through exported collections.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0031

- [ ] **Q0031 — How would you record and troubleshoot a simulated unavailable MySQL endpoint or incorrect database password?**
  - **Acceptance:** Show the error, root cause, and successful retry after restoring the connection.
  - **Failure to practice:** Unclear error masking connection failure.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

## Q0032

- [ ] **Q0032 — How would you verify the entire environment from clean checkout: Java, Maven, unit tests, MySQL reachability and a clean Git state?**
  - **Acceptance:** Produce the phase completion checklist with exact commands and outputs.
  - **Failure to practice:** Claiming environment is ready without a reproducible build.
  - **Evidence:** Screenshot or exact command, actual output and any changed files. Do not mark VERIFIED without a test/commit record.

