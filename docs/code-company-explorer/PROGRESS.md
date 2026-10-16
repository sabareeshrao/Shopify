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
| 2 | Check that the shop has started | `ShopApplicationConfiguration.applicationReadyCode()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 48–52 | 0 mapped | Verified |
| 3 | Set up request filtering | `ShopApplicationConfiguration.croseSiteFilter()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 54–65 | 0 mapped | Verified |
| 4 | Prepare JSON responses | `ShopApplicationConfiguration.configureMessageConverters()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 67–70 | 0 mapped | Verified |
| 5 | Set up the shop homepage | `ShopApplicationConfiguration.addViewControllers()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 72–75 | 0 mapped | Verified |
| 6 | Add request interceptors | `ShopApplicationConfiguration.addInterceptors()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 77–98 | 0 mapped | Verified |

Source blob SHA: dd91c2f7c8d2d04b9ecbb318b450af7359d04493.

## Why this sequence? (Learning order, not execution order)

| Company | Why here? | Unique interview question |
|---|---|---|
| 1 | Start with the actual Java application entry point. | IQ-1: What happens when `SpringApplication.run()` starts Spring Boot? |
| 2 | Observe the readiness callback, while acknowledging it fires **after** startup configuration at runtime. | IQ-2: How does `ApplicationReadyEvent` differ from `@PostConstruct`? |
| 3 | Inspect registering the servlet XSS filter for incoming shop, API and customer requests. | IQ-3: How are servlet filter URL patterns registered, and why isn't a filter sufficient for XSS prevention? |
| 4 | Understand JSON conversion of MVC requests and responses. | IQ-4: What does overriding `configureMessageConverters()` do to defaults versus `extendMessageConverters()`? |
| 5 | Connect `/` to a view without a dedicated controller method. | IQ-5: When use `addViewController()` instead of `@Controller`, and how is the view resolved? |
| 6 | Add MVC interceptors for locale and CORS after basic routing concepts. | IQ-6: How does an MVC `HandlerInterceptor` differ from a servlet `Filter`? |

Each company has the complete unique question and a plain-English sequence reason in `companies.json`, displayed within the HTML explorer. This numbering is an **instructional discovery path**, not a claim that Spring calls the methods in company number order.

### Company 4 connections

- Source: `ShopApplicationConfiguration.java:67–70`
- Spring MVC calls the WebMvcConfigurer override during configuration.
- Adds `MappingJackson2HttpMessageConverter` to the converter list at line 69.

### Company 5 connections

- Source: `ShopApplicationConfiguration.java:72–75`
- Registers `/` with view name `shop` at line 74.

### Company 6 connections

- Source: `ShopApplicationConfiguration.java:77–98`
- Adds `localeChangeInterceptor()` on line 80.
- Adds `corsFilter()` at line 92 for `/services/**` (line 94) and `/api/**` (line 96).
- Lines 82–89 are a commented-out `storeFilter()` block and must not be treated as active configuration.

### Company 1–6 verified source

- All new companies use existing pinned Shopizer commit `6a4a0a65a3408ee8f62597b51d1b3aac24b77dee`.
- Companies 2–6 share source file blob SHA `41f81a6604d64ad9a60829a606f247dd547182c4`.

### Company 3 connections

- Spring invokes the `@Bean` method in `ShopApplicationConfiguration.java` (line 54) when configuring the application.
- `croseSiteFilter()` builds a Spring `FilterRegistrationBean<XssFilter>` (lines 55–57).
- It instantiates Shopizer's real `XssFilter` (line 59) and adds URL patterns `/shop/**`, `/api/**`, `/customer/**` (lines 60–62).
- The actual `XssFilter` implementation is **not yet mapped as a numbered company**; external APIs are not subsidiaries.
- It is a **separate top-level company** from 1 and 2. Numeric learning sequence does not imply Spring's runtime call order.
- Source blob SHA: `41f81a6604d64ad9a60829a606f247dd547182c4` (same file as Company 2).

## Navigation behavior

- Search by exact number (e.g. `3`, `21`, `21.1`, or `Company 21`) and press Enter or select a result.
- If a number isn't mapped yet, the explorer says it hasn't been created instead of jumping to another company.
- `←` and `→` move backward and forward through the current numerical company level, with visible Previous / Next buttons for phones.
- Top-level company 21 advances to top-level company 22 when available, without forcing a detour through subsidiary 21.1.
- Subsidiaries such as 21.1 and 21.2 navigate among their siblings at the same depth.
- Arrow shortcuts do not intercept typing inside search fields or other text inputs.
- Company IDs stay permanent; the UI derives navigation from `companies.json` automatically.

### Company 2 connections

- Triggered by: Spring Boot `ApplicationReadyEvent` at line 48. It is not directly called by Company 1.
- Uses: `System.getProperty("user.dir")` on line 50; `logger.info(...)` on line 51.
- Subsidiaries: None assigned yet. Company 2 remains independent from Company 1.
- Source blob SHA: `41f81a6604d64ad9a60829a606f247dd547182c4`.

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
6. Update companies.json, index.html, and this tracker together; include a unique IQ-N question and a clear rationale for the company's place in the learning sequence.
7. Preserve the existing questions/, tracking/, changes/, and curriculum documentation.

## GitHub Pages

Set Settings → Pages → Build and deployment → Deploy from a branch; Branch = main, Folder = /docs.

The homepage docs/index.html opens the explorer at docs/code-company-explorer/index.html.

After Pages finishes building, the expected URL is: https://sabareeshrao.github.io/Shopify/

This static site displays source code; GitHub Pages does not execute the Spring Boot application.
