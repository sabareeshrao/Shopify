# Phase 00 — Reference investigation and system design

**Canonical IDs:** Q0001 onward · **Planned tasks:** 12 · **Status:** NOT STARTED

**Reference area:** https://github.com/shopizer-ecommerce/shopizer

Questions are development tasks, not MCQ answers. Implementation generates separate MCQs later. A checked box must have code/artifact evidence and an updated tracker.


## Shopizer three-repository inventory

- [ ] **Q0001 — How would you examine and specify Shopizer three-repository inventory, documenting backend, Angular admin and React storefront boundaries before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** confusing a Maven module with a deployed microservice.
  - **Proof focus:** a diagram naming the real repositories and entrypoints.

- [ ] **Q0002 — How would you create the minimal reproducible workspace or architecture artifact for Shopizer three-repository inventory without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating backend, Angular admin and React storefront boundaries.
  - **Edge/failure to consider:** confusing a Maven module with a deployed microservice.
  - **Proof focus:** a diagram naming the real repositories and entrypoints.

- [ ] **Q0003 — How would you diagnose confusing a Maven module with a deployed microservice while establishing Shopizer three-repository inventory, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** confusing a Maven module with a deployed microservice.
  - **Proof focus:** a diagram naming the real repositories and entrypoints.

- [ ] **Q0004 — How would you verify Shopizer three-repository inventory from a clean checkout, specifically using a diagram naming the real repositories and entrypoints?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** confusing a Maven module with a deployed microservice.
  - **Proof focus:** a diagram naming the real repositories and entrypoints.


## five-module Maven dependency investigation

- [ ] **Q0005 — How would you examine and specify five-module Maven dependency investigation, documenting parent POM, core-model, core-modules, core, shop-model and shop relationships before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** cyclic module dependencies or inconsistent versions.
  - **Proof focus:** a reproducible module build and dependency map.

- [ ] **Q0006 — How would you create the minimal reproducible workspace or architecture artifact for five-module Maven dependency investigation without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating parent POM, core-model, core-modules, core, shop-model and shop relationships.
  - **Edge/failure to consider:** cyclic module dependencies or inconsistent versions.
  - **Proof focus:** a reproducible module build and dependency map.

- [ ] **Q0007 — How would you diagnose cyclic module dependencies or inconsistent versions while establishing five-module Maven dependency investigation, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** cyclic module dependencies or inconsistent versions.
  - **Proof focus:** a reproducible module build and dependency map.

- [ ] **Q0008 — How would you verify five-module Maven dependency investigation from a clean checkout, specifically using a reproducible module build and dependency map?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** cyclic module dependencies or inconsistent versions.
  - **Proof focus:** a reproducible module build and dependency map.


## commerce domain and user journey inventory

- [ ] **Q0009 — How would you examine and specify commerce domain and user journey inventory, documenting browse, cart, pay, place order, fulfill and administer before changing any code?**
  - **Acceptance:** Written scope with concrete examples, decisions and a traceable source reference.
  - **Edge/failure to consider:** missing a state transition or authorization boundary.
  - **Proof focus:** one fully traced browse-to-order sequence.

- [ ] **Q0010 — How would you create the minimal reproducible workspace or architecture artifact for commerce domain and user journey inventory without silently skipping setup?**
  - **Acceptance:** A committed artifact or command transcript demonstrating browse, cart, pay, place order, fulfill and administer.
  - **Edge/failure to consider:** missing a state transition or authorization boundary.
  - **Proof focus:** one fully traced browse-to-order sequence.

- [ ] **Q0011 — How would you diagnose missing a state transition or authorization boundary while establishing commerce domain and user journey inventory, including its root cause and fix?**
  - **Acceptance:** A documented failing example and confirmed recovery procedure.
  - **Edge/failure to consider:** missing a state transition or authorization boundary.
  - **Proof focus:** one fully traced browse-to-order sequence.

- [ ] **Q0012 — How would you verify commerce domain and user journey inventory from a clean checkout, specifically using one fully traced browse-to-order sequence?**
  - **Acceptance:** A reproducible command, observed result and evidence log.
  - **Edge/failure to consider:** missing a state transition or authorization boundary.
  - **Proof focus:** one fully traced browse-to-order sequence.
