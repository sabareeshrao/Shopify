# Code Company Explorer — Progress

This folder contains the incremental company explorer, separate from Shopify's existing 1,025-question curriculum.

## Original code

- Repository: https://github.com/shopizer-ecommerce/shopizer
- Fixed reference commit: 6a4a0a65a3408ee8f62597b51d1b3aac24b77dee
- The reference is read-only.

## Completed companies

| Company ID | Plain-English name | Actual method | File | Lines | Subsidiaries | Status |
|---|---|---|---|---|---|---|
| 1 | Start the shop | ShopApplication.main(String[] args) | sm-shop/src/main/java/com/salesmanager/shop/application/ShopApplication.java | 11–13 | 0 mapped | Verified |

Source blob SHA: dd91c2f7c8d2d04b9ecbb318b450af7359d04493.

### Company 1 connections

- Started by: Java runtime (external; no Shopizer callsite).
- Uses: SpringApplication.run(ShopApplication.class, args) (line 12; external Spring Boot library).
- Subsidiaries: none assigned yet. External libraries are not Shopizer subsidiaries.

## Incremental-build rules

1. Add only one new company or verified subsidiary per prompt.
2. Before assigning an ID, inspect the actual Java source at the pinned commit.
3. Keep company numbers stable. Use dotted subsidiary numbers only for confirmed code relationships.
4. Record exact file path, method, line range, evidence, and caller/supplier distinctions.
5. Never substitute demonstration code or guessed relationships for source-derived facts.
6. Update companies.json, index.html, and this tracker together.
7. Preserve the existing questions/, tracking/, changes/, and curriculum documentation.

## GitHub Pages

Set Settings → Pages → Build and deployment → Deploy from a branch; Branch = main, Folder = /docs.

The homepage docs/index.html opens the explorer at docs/code-company-explorer/index.html.

After Pages finishes building, the expected URL is: https://sabareeshrao.github.io/Shopify/

This static site displays source code; GitHub Pages does not execute the Spring Boot application.
