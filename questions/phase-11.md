# Phase 11 — Product media, CMS and file storage

**Tasks:** 32 · **Range:** Q0350–Q0381 · **Status:** NOT STARTED

**Shopizer reference:** https://github.com/shopizer-ecommerce/shopizer/tree/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core

Each item is an original, independently verifiable build/interview task. MCQ lessons and implementation commits are added only when tackled.


## product asset metadata model

- [ ] **Q0350 — How would you design product asset metadata model with explicit contracts for product/image ownership, filename, type and sort order?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** orphaned asset when product deleted.
  - **Proof focus:** image entity and association tests.

- [ ] **Q0351 — How would you implement product asset metadata model from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** orphaned asset when product deleted.
  - **Proof focus:** image entity and association tests.

- [ ] **Q0352 — How would you connect product asset metadata model across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** orphaned asset when product deleted.
  - **Proof focus:** image entity and association tests.

- [ ] **Q0353 — How would you handle orphaned asset when product deleted in product asset metadata model without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** orphaned asset when product deleted.
  - **Proof focus:** image entity and association tests.

- [ ] **Q0354 — How would you prove product asset metadata model is correct with image entity and association tests and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** orphaned asset when product deleted.
  - **Proof focus:** image entity and association tests.


## secure multipart upload

- [ ] **Q0355 — How would you design secure multipart upload with explicit contracts for file size, MIME sniffing, extension allowlist and auth?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** oversized or malicious upload.
  - **Proof focus:** valid image accepted and script rejected.

- [ ] **Q0356 — How would you implement secure multipart upload from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** oversized or malicious upload.
  - **Proof focus:** valid image accepted and script rejected.

- [ ] **Q0357 — How would you connect secure multipart upload across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** oversized or malicious upload.
  - **Proof focus:** valid image accepted and script rejected.

- [ ] **Q0358 — How would you handle oversized or malicious upload in secure multipart upload without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** oversized or malicious upload.
  - **Proof focus:** valid image accepted and script rejected.

- [ ] **Q0359 — How would you prove secure multipart upload is correct with valid image accepted and script rejected and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** oversized or malicious upload.
  - **Proof focus:** valid image accepted and script rejected.


## local storage implementation

- [ ] **Q0360 — How would you design local storage implementation with explicit contracts for safe directory layout and path normalization?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** path traversal and filename collision.
  - **Proof focus:** round-trip write/read/delete.

- [ ] **Q0361 — How would you implement local storage implementation from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** path traversal and filename collision.
  - **Proof focus:** round-trip write/read/delete.

- [ ] **Q0362 — How would you connect local storage implementation across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** path traversal and filename collision.
  - **Proof focus:** round-trip write/read/delete.

- [ ] **Q0363 — How would you handle path traversal and filename collision in local storage implementation without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** path traversal and filename collision.
  - **Proof focus:** round-trip write/read/delete.

- [ ] **Q0364 — How would you prove local storage implementation is correct with round-trip write/read/delete and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** path traversal and filename collision.
  - **Proof focus:** round-trip write/read/delete.


## object storage adapter

- [ ] **Q0365 — How would you design object storage adapter with explicit contracts for S3/GCP interface, uploads, signed URLs and permissions?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** network timeouts and partially written objects.
  - **Proof focus:** test with stubbed storage adapter.

- [ ] **Q0366 — How would you implement object storage adapter from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** network timeouts and partially written objects.
  - **Proof focus:** test with stubbed storage adapter.

- [ ] **Q0367 — How would you connect object storage adapter across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** network timeouts and partially written objects.
  - **Proof focus:** test with stubbed storage adapter.

- [ ] **Q0368 — How would you handle network timeouts and partially written objects in object storage adapter without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** network timeouts and partially written objects.
  - **Proof focus:** test with stubbed storage adapter.

- [ ] **Q0369 — How would you prove object storage adapter is correct with test with stubbed storage adapter and automated positive/negative tests?**
  - **Acceptance:** Passing tests, expected output and a documented manual verification.
  - **Edge case:** network timeouts and partially written objects.
  - **Proof focus:** test with stubbed storage adapter.


## image gallery and thumbnails

- [ ] **Q0370 — How would you design image gallery and thumbnails with explicit contracts for product main image, ordering, dimensions and fallback?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** broken thumbnail or invalid image.
  - **Proof focus:** image retrieval and expected image metadata.

- [ ] **Q0371 — How would you implement image gallery and thumbnails from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** broken thumbnail or invalid image.
  - **Proof focus:** image retrieval and expected image metadata.

- [ ] **Q0372 — How would you connect image gallery and thumbnails across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** broken thumbnail or invalid image.
  - **Proof focus:** image retrieval and expected image metadata.

- [ ] **Q0373 — How would you handle broken thumbnail or invalid image in image gallery and thumbnails without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** broken thumbnail or invalid image.
  - **Proof focus:** image retrieval and expected image metadata.


## CMS pages and content blocks

- [ ] **Q0374 — How would you design CMS pages and content blocks with explicit contracts for merchant-scoped content, draft/publication and static pages?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** cross-tenant content edit or unsafe HTML.
  - **Proof focus:** published page by friendly URL.

- [ ] **Q0375 — How would you implement CMS pages and content blocks from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** cross-tenant content edit or unsafe HTML.
  - **Proof focus:** published page by friendly URL.

- [ ] **Q0376 — How would you connect CMS pages and content blocks across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** cross-tenant content edit or unsafe HTML.
  - **Proof focus:** published page by friendly URL.

- [ ] **Q0377 — How would you handle cross-tenant content edit or unsafe HTML in CMS pages and content blocks without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** cross-tenant content edit or unsafe HTML.
  - **Proof focus:** published page by friendly URL.


## asset cache invalidation and cleanup

- [ ] **Q0378 — How would you design asset cache invalidation and cleanup with explicit contracts for cache freshness, deletion and durable references?**
  - **Acceptance:** A documented design with constraints and testable examples.
  - **Edge case:** stale content and orphaned files.
  - **Proof focus:** replace/delete under simulated cache load.

- [ ] **Q0379 — How would you implement asset cache invalidation and cleanup from scratch with correct Java types, files and module boundaries?**
  - **Acceptance:** Compileable implementation with migrations or client state as applicable.
  - **Edge case:** stale content and orphaned files.
  - **Proof focus:** replace/delete under simulated cache load.

- [ ] **Q0380 — How would you connect asset cache invalidation and cleanup across persistence, business logic and REST or UI components to make it work end-to-end?**
  - **Acceptance:** Working integration using real request and data flow.
  - **Edge case:** stale content and orphaned files.
  - **Proof focus:** replace/delete under simulated cache load.

- [ ] **Q0381 — How would you handle stale content and orphaned files in asset cache invalidation and cleanup without breaking invariants or disclosing secrets?**
  - **Acceptance:** Reproducible failure, explicit error behavior and safe recovery.
  - **Edge case:** stale content and orphaned files.
  - **Proof focus:** replace/delete under simulated cache load.
