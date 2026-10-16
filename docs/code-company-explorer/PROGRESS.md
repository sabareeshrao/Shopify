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
| 7 | Handle images and binary downloads | `ShopApplicationConfiguration.byteArrayHttpMessageConverter()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 100–108 | 0 mapped | Verified |
| 8 | Create the language-change interceptor | `ShopApplicationConfiguration.localeChangeInterceptor()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 110–113 | 0 mapped | Verified |
| 9 | Create the CORS interceptor | `ShopApplicationConfiguration.corsFilter()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 119–122 | 0 mapped | Verified |
| 10 | Choose the default language | `ShopApplicationConfiguration.localeResolver()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 125–130 | 0 mapped | Verified |
| 11 | Load translated messages | `ShopApplicationConfiguration.messageSource()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 132–144 | 0 mapped | Verified |
| 12 | Provide message helper tools | `ShopApplicationConfiguration.messages()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopApplicationConfiguration.java` | 146–149 | 0 mapped | Verified |
| 13 | Load shop settings from a file | `ShopizerPropertiesConfig.mapper()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopizerPropertiesConfig.java` | 12–17 | 0 mapped | Verified |
| 14 | Run work in the background | `AsyncConfig.getAsyncExecutor()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/AsyncConfig.java` | 19–22 | 0 mapped | Verified |
| 15 | Handle uncaught background errors | `AsyncConfig.getAsyncUncaughtExceptionHandler()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/AsyncConfig.java` | 24–27 | 0 mapped | Verified |
| 16 | Read shop and language details from requests | `WebConfig.addArgumentResolvers()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/WebConfig.java` | 22–26 | 0 mapped | Verified |
| 17 | Identify merchant-store arguments | `supportsParameter()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MerchantStoreArgumentResolver.java` | 37–40 | 0 mapped | Verified |
| 18 | Find and authorize the selected store | `resolveArgument()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MerchantStoreArgumentResolver.java` | 42–61 | 0 mapped | Verified |
| 19 | Identify language arguments | `supportsParameter()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/LanguageArgumentResolver.java` | 23–26 | 0 mapped | Verified |
| 20 | Find the current request language | `resolveArgument()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/LanguageArgumentResolver.java` | 28–35 | 0 mapped | Verified |
| 21 | Log servlet startup information | `contextInitialized()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopServletContextListener.java` | 14–24 | 0 mapped | Verified |
| 22 | Stop the cache at shutdown | `contextDestroyed()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/ShopServletContextListener.java` | 26–31 | 0 mapped | Verified |
| 23 | Build Swagger API documentation | `api()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/DocumentationConfiguration.java` | 51–85 | 0 mapped | Verified |
| 24 | Choose documented API packages | `requestHandlers()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/DocumentationConfiguration.java` | 87–95 | 0 mapped | Verified |
| 25 | Describe REST API metadata | `apiInfo()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/DocumentationConfiguration.java` | 97–104 | 0 mapped | Verified |
| 26 | Choose cloud or local image paths | `img()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/LocationImageConfig.java` | 25–44 | 0 mapped | Verified |
| 27 | Provide the token authentication filter | `authenticationTokenFilter()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 45–48 | 0 mapped | Verified |
| 28 | Provide credential service | `credentialsService()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 50–53 | 0 mapped | Verified |
| 29 | Create the BCrypt password encoder | `passwordEncoder()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 55–58 | 0 mapped | Verified |
| 30 | Handle successful user authentication | `userAuthenticationSuccessHandler()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 60–63 | 0 mapped | Verified |
| 31 | Handle successful service authentication | `servicesAuthenticationSuccessHandler()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 65–68 | 0 mapped | Verified |
| 32 | Provide a customer facade | `customerFacade()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 70–73 | 0 mapped | Verified |
| 33 | Expose customer authentication manager | `authenticationManagerBean()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 87–91 | 0 mapped | Verified |
| 34 | Exclude selected routes from security filters | `configure(WebSecurity web)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 100–107 | 0 mapped | Verified |
| 35 | Register customer identity lookup | `configure(AuthenticationManagerBuilder auth)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 110–113 | 0 mapped | Verified |
| 36 | Define shop authorization and logout rules | `configure(HttpSecurity http)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 115–144 | 0 mapped | Verified |
| 37 | Provide the shop Basic-auth realm | `shopAuthenticationEntryPoint()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 146–151 | 0 mapped | Verified |
| 38 | Register legacy service user details | `configure(AuthenticationManagerBuilder auth)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 176–179 | 0 mapped | Verified |
| 39 | Secure legacy service endpoints | `configure(HttpSecurity http)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 181–194 | 0 mapped | Verified |
| 40 | Set the service Basic-auth realm | `servicesAuthenticationEntryPoint()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 196–201 | 0 mapped | Verified |
| 41 | Expose the JWT admin authentication manager | `authenticationManagerBean()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 295–300 | 0 mapped | Verified |
| 42 | Register JWT admin provider | `configure(AuthenticationManagerBuilder auth)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 308–313 | 0 mapped | Verified |
| 43 | Exclude Swagger UI from web security | `configure(WebSecurity web)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 315–318 | 0 mapped | Verified |
| 44 | Protect private JWT admin routes | `configure(HttpSecurity http)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 324–340 | 0 mapped | Verified |
| 45 | Build JWT admin authentication provider | `authenticationProvider()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 342–347 | 0 mapped | Verified |
| 46 | Set admin API Basic realm | `apiAdminAuthenticationEntryPoint()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 349–354 | 0 mapped | Verified |
| 47 | Expose customer JWT authentication manager | `authenticationManagerBean()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 380–384 | 0 mapped | Verified |
| 48 | Register JWT customer user details | `configure(AuthenticationManagerBuilder auth)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 386–389 | 0 mapped | Verified |
| 49 | Secure customer auth API endpoints | `configure(HttpSecurity http)` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 391–408 | 0 mapped | Verified |
| 50 | Build JWT customer authentication provider | `authenticationProvider()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 410–415 | 0 mapped | Verified |
| 51 | Set customer API Basic realm | `apiCustomerAuthenticationEntryPoint()` | `sm-shop/src/main/java/com/salesmanager/shop/application/config/MultipleEntryPointsSecurityConfig.java` | 417–422 | 0 mapped | Verified |
| 52 | Process request authentication tokens | `doFilterInternal()` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/AuthenticationTokenFilter.java` | 49–126 | 0 mapped | Verified |
| 53 | Clean per-request user context | `postFilter()` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/AuthenticationTokenFilter.java` | 129–142 | 0 mapped | Verified |
| 54 | Authenticate JWT admin credentials | `authenticate(Authentication authentication)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java` | 35–59 | 0 mapped | Verified |
| 55 | Audit admin password comparison | `passwordMatch(String rawPassword, String user)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java` | 62–64 | 0 mapped | Verified |
| 56 | Audit supported authentication types | `supports(Class<?> authentication)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java` | 66–69 | 0 mapped | Verified |
| 57 | Authenticate customer credentials | `authenticate(Authentication authentication)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java` | 28–52 | 0 mapped | Verified |
| 58 | Compare customer password | `passwordMatch(String rawPassword, String user)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java` | 55–57 | 0 mapped | Verified |
| 59 | Declare supported authentication tokens | `supports(Class<?> authentication)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java` | 59–62 | 0 mapped | Verified |
| 60 | Expose customer identity lookup dependency | `getJwtCustomerDetailsService()` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java` | 65–67 | 0 mapped | Verified |
| 61 | Assign customer identity lookup dependency | `setJwtCustomerDetailsService(UserDetailsService jwtCustomerDetailsService)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java` | 70–72 | 0 mapped | Verified |
| 62 | Read JWT username | `getUsernameFromToken(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 56–58 | 0 mapped | Verified |
| 63 | Read JWT issuance time | `getIssuedAtDateFromToken(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 60–62 | 0 mapped | Verified |
| 64 | Read JWT expiry timestamp | `getExpirationDateFromToken(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 64–66 | 0 mapped | Verified |
| 65 | Read intended JWT audience | `getAudienceFromToken(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 68–70 | 0 mapped | Verified |
| 66 | Resolve any supported JWT claim | `getClaimFromToken(String token, Function<Claims, T> claimsResolver)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 72–75 | 0 mapped | Verified |
| 67 | Parse and verify signed JWT | `getAllClaimsFromToken(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 77–82 | 0 mapped | Verified |
| 68 | Check strict JWT expiration | `isTokenExpired(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 84–87 | 0 mapped | Verified |
| 69 | Check expiration with 200-second allowance | `isTokenExpiredWithGrace(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 89–93 | 0 mapped | Verified |
| 70 | Invalidate tokens preceding password reset | `isCreatedBeforeLastPasswordReset(Date created, Date lastPasswordReset)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 95–97 | 0 mapped | Verified |
| 71 | Adjust reset cutoff by 200 seconds | `isCreatedBeforeLastPasswordResetWithGrace(Date created, Date lastPasswordReset)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 99–101 | 0 mapped | Verified |
| 72 | Add seconds to a Date | `addSeconds(Date date, Integer seconds)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 103–108 | 0 mapped | Verified |
| 73 | Choose API token audience | `generateAudience()` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 110–112 | 0 mapped | Verified |
| 74 | Recognize mobile/tablet expiry exception | `ignoreTokenExpiration(String token)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 114–117 | 0 mapped | Verified |
| 75 | Generate user JWT | `generateToken(UserDetails userDetails)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 119–122 | 0 mapped | Verified |
| 76 | Sign JWT with HS512 | `doGenerateToken(Map<String, Object> claims, String subject, String audience)` | `sm-shop/src/main/java/com/salesmanager/shop/store/security/JWTTokenUtil.java` | 124–138 | 0 mapped | Verified |

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
| 7 | Add binary and image media types after JSON response conversion. | IQ-7: `ByteArrayHttpMessageConverter` vs JSON, supported media types and negotiation |
| 8 | Open the actual locale-change interceptor created for Company 6. | IQ-8: `LocaleChangeInterceptor` with `LocaleResolver` |
| 9 | Open the actual Shopizer `CorsFilter` method called by Company 6. | IQ-9: Why Shopizer's `corsFilter()` is registered with `addInterceptor()` |
| 10 | Configure session-based language resolution to support locale changes. | IQ-10: `SessionLocaleResolver` vs `AcceptHeaderLocaleResolver` |
| 11 | Finish internationalization with UTF-8 resource bundles for translated messages. | IQ-11: Resource-bundle resolution and reloadable message sources |
| 12 | Complete message infrastructure by creating the LabelUtils bean. | IQ-12: Spring @Bean names and utility beans |
| 13 | Move from language resources to general configuration properties. | IQ-13: PropertiesFactoryBean and classpath resource loading |
| 14 | Introduce asynchronous work after web configuration. | IQ-14: Fixed thread-pool capacity, queuing, and lifecycle |
| 15 | Add background failure handling after executor setup. | IQ-15: Exception handling for void versus future-returning @Async methods |
| 16 | Connect MVC requests to shop/language argument resolvers. | IQ-16: Custom argument resolver selection and precedence |

Each company has the complete unique question and a plain-English sequence reason in `companies.json`, displayed within the HTML explorer. This numbering is an **instructional discovery path**, not a claim that Spring calls the methods in company number order.

### Companies 12–16: verified source

- **12:** `ShopApplicationConfiguration.messages()` (lines 146–149) returns a `LabelUtils` Spring bean; sequence follows the message source.
- **13:** `ShopizerPropertiesConfig.mapper()` (lines 12–17) registers `shopizer-properties`, backed by `shopizer-properties.properties`.
- **14:** `AsyncConfig.getAsyncExecutor()` (lines 19–22) creates a fixed pool of five worker threads.
- **15:** `AsyncConfig.getAsyncUncaughtExceptionHandler()` (lines 24–27) returns `SimpleAsyncUncaughtExceptionHandler`.
- **16:** `WebConfig.addArgumentResolvers()` (lines 22–26) registers Shopizer's merchant-store and language argument resolvers.
- All five have distinct sequence explanations and questions IQ-12 through IQ-16 in `companies.json`.
- The original Shopizer reference is pinned to `6a4a0a65a3408ee8f62597b51d1b3aac24b77dee`.

### Verified Company 6 rendering failure — corrected

- Root cause: the connection UI mixed **internal company links** and **outside-service links** in one list and used the combined list position to index only the outside-service array.
- Company 6 contains two internal links (Companies 8 and 9) before one outside-service link; the UI attempted to read a non-existent outside-service entry and threw `Cannot read properties of undefined (reading 'code_line')` while rendering.
- Fix: `edgeCard()` now derives the external source index from the stable `outside-in-N`/`outside-out-N` relation ID, not from the combined-card index. A missing entry safely produces no card.
- Separate robustness changes: numeric search result click is handled directly; company pages write `#company-N` permalinks and are restored on refresh; navigation scrolls to the top.
- A simulated browser test loaded all 16 companies, rendered their interview questions, opened Company 6 through a numeric search click, verified `#company-6`, and moved 6 → 7 → 6 using next/previous.
- This test validates application behavior in a DOM simulation; live GitHub Pages rendering still requires deployment confirmation.
### Search and navigation repair

- Company 6 exists as `addInterceptors()` in `ShopApplicationConfiguration.java` lines 77–98; it is not missing from the source registry.
- Numeric search results now have a dedicated click handler instead of relying only on the general document click listener.
- Opening a company updates the address fragment to `#company-6` (or the appropriate company number), enabling direct links and preserving selection on refresh.
- A `hashchange` listener responds to manually changed links; the search still handles Enter and keyboard arrows.
- Navigating to a company scrolls to the top rather than leaving the user at the prior company’s scroll position.
### Companies 7–11: verified source and connections

- **7** `byteArrayHttpMessageConverter()` lines 100–108 — supported response types: JPEG, GIF, PNG, and octet-stream; creates `ByteArrayHttpMessageConverter`.
- **8** `localeChangeInterceptor()` lines 110–113 — Spring bean producing `LocaleChangeInterceptor`; Company 6 calls it at line 80.
- **9** `corsFilter()` lines 119–122 — Spring bean producing Shopizer `CorsFilter`; Company 6 calls it at line 92. The commented `storeFilter()` method on lines 115–117 is not active.
- **10** `localeResolver()` lines 125–130 — provides `SessionLocaleResolver` with default `Locale.getDefault()`.
- **11** `messageSource()` lines 132–144 — supplies shopizer, messages, shipping, payment resource-bundle basenames and UTF-8 encoding.
- Company 6 has real, direct code connections to Company 8 at source line 80 and Company 9 at source line 92. Those now appear as clickable clients/suppliers in the HTML rather than unnumbered external dependencies.
- All five are separate top-level companies in learning order; they have no subsidiary numbers assigned yet.
- Source commit: `6a4a0a65a3408ee8f62597b51d1b3aac24b77dee`; blob SHA: `41f81a6604d64ad9a60829a606f247dd547182c4`.
- Complete sequence reasons and unique questions IQ-7 through IQ-11 are stored in `companies.json` and shown on each company page.
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

### Company 1–11 verified source

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

1. Add the number of verified companies requested by the user, ordinarily one at a time unless they explicitly request a batch.
2. Before assigning an ID, inspect the actual Java source at the pinned commit.
3. Keep company numbers stable. Use dotted subsidiary numbers only for confirmed code relationships.
4. Record exact file path, method, line range, evidence, and caller/supplier distinctions.
5. Never substitute demonstration code or guessed relationships for source-derived facts.
6. Update companies.json, index.html, and this tracker together; include a unique IQ-N question and a clear rationale for the company's place in the learning sequence.
7. Preserve the existing questions/, tracking/, changes/, and curriculum documentation.

## Modular UI and highlighting upgrade (16 companies)

- **Approved visual design preserved.** Original CSS moved to `assets/styles.css`, with additional persistent tap-selection rules using existing black, blue, orange, green and white palette.
- `index.html` is now a small static shell; JavaScript is split into nine ordered deferred scripts: `icons`, `data`, `tree`, `views`, `connections`, `highlight`, `navigation`, `events`, `app` under `assets/js/`.
- Deliberately uses ordinary deferred JavaScript files sharing existing top-level state; no framework, npm build step, or GitHub Pages configuration change is necessary.
- Removed earlier duplicate implementations of `getRelations()` and `edgeCard()`.
- Connection-box selection, highlighted code row, and detail explanation now all update through `selectLine()` / `selectExternalCard()` using a single `activeRelationKey` and `activeLine`.
- Outside-service boxes carry a stable relation key (`uses:outside-out-N` / `usedby:outside-in-N`), rather than treating mixed internal/external card positions as source indices.
- Tapping a new box clears the old border and line; tapping a code line clears the box selection; opening another company resets stale selection.
- `findLineInfo()` now considers mapped company calls, external suppliers, and external clients rather than accidentally carrying unrelated text forward.
- Clicking internal company cards navigates to the target company; a related callsite outside its method range is described rather than pretending it belongs to the new method.
- Numeric search, permanent `#company-N` URLs, previous/next, and mobile sidebar remain in place.

### Verification

- Simulated DOM integration audit (current pinned data): 16 of 16 companies render, all 41 external cards highlight the corresponding source line, update their explanation, and become the only selected card.
- Verified no selected card or code-line highlight persists after switching companies; Company 7 switches from line 102 to line 105 with matching card details.
- Company 6 retains valid internal navigations to Companies 8 and 9; numeric search and previous/next mapping remain available.
- Independent browser test runner at `tests/index.html` opens the explorer in a responsive same-origin iframe and can rerun the full 16-company + external-card audit, including touch/click behavior in an actual browser.
- **Limit:** The assistant verified GitHub commits and simulated DOM interactions; actual deployment/browser behavior must be checked using the browser test runner after GitHub Pages publishes the updated files.

### Rules for future additions

- Add new records only in `companies.json`, storing original source ranges, sequence reasons, and unique IQ interview questions.
- Add snapshots under `sources/` as needed; the page loads all declared sources. Plan lazy source loading and paginated folder browsing as the repository scales to hundreds/thousands of files.
- For each change run both source-range validation and the `tests/` browser interaction audit; never conflate learning order with runtime call order.

## Companies 17–36: source-verified learning batch

- Pinned Shopizer commit: `6a4a0a65a3408ee8f62597b51d1b3aac24b77dee`; six new complete Java source snapshots in `sources/`.
- Company 16 registers the two argument-resolver classes. Its links to Companies 17 and 19 represent **registration**, not direct invocation.
- Company 23 invokes Company 24 at source line 69; the Company 25 `apiInfo()` helper is present but not called by `api()` in the pinned file.
- Companies 33–36 belong to the nested `CustomerConfigurationAdapter` inside `MultipleEntryPointsSecurityConfig.java`.
- Security review: Company 36 has a broad `/shop/**` `permitAll()` matcher before the more specific customer role matcher. The interview question explicitly tests this potential access-control ordering issue.
- Every company retains a unique permanent `IQ-N` and a specific source-based learning rationale.
- Pre-commit QA: 20 pinned method-range checks; 36 UI render checks; numeric search 36; navigation 35↔36; verified 16→17 and 23→24 links. Changes prepared only after passing checks.

## GitHub Pages

Set Settings → Pages → Build and deployment → Deploy from a branch; Branch = main, Folder = /docs.

The homepage docs/index.html opens the explorer at docs/code-company-explorer/index.html.

After Pages finishes building, the expected URL is: https://sabareeshrao.github.io/Shopify/

This static site displays source code; GitHub Pages does not execute the Spring Boot application.

## Companies 37–56 — security configuration and authentication filters

- **Company 37 / IQ-37:** Provide the shop Basic-auth realm. Company 36 directly calls this factory; inspect the Basic authentication challenge before other security chains. Interview: What does BasicAuthenticationEntryPoint do on an unauthenticated request, and how does shop-realm affect the challenge?
- **Company 38 / IQ-38:** Register legacy service user details. After the shop Basic realm, enter the active @Order(2) services adapter and find how its user identities are loaded. Interview: How does a chain-specific AuthenticationManagerBuilder.userDetailsService() affect authentication of service requests?
- **Company 39 / IQ-39:** Secure legacy service endpoints. After binding service identities, examine public versus private service route rules and authentication entry points. Interview: Why might disabling CSRF be dangerous when an HttpSecurity chain also enables formLogin(), and how do the service URL matchers interact?
- **Company 40 / IQ-40:** Set the service Basic-auth realm. Company 39 directly calls this entry-point factory, so examine the challenge response after its security rules. Interview: Does the Basic-auth realm name restrict which users authenticate, or only describe the HTTP challenge?
- **Company 41 / IQ-41:** Expose the JWT admin authentication manager. The source's AdminConfigurationAdapter is commented out; skip it and start the active @Order(5) JWT admin adapter with its named manager. Interview: How do named AuthenticationManager beans avoid ambiguity when Spring Security has multiple filter chains?
- **Company 42 / IQ-42:** Register JWT admin provider. Once the JWT admin manager exists, inspect its user-details source and provider factory before its route rules. Interview: How does AuthenticationManagerBuilder select from a configured UserDetailsService and AuthenticationProvider?
- **Company 43 / IQ-43:** Exclude Swagger UI from web security. Before private admin API rules, identify the path intentionally excluded from security filtering. Interview: Why does web.ignoring('/swagger-ui.html') differ from permitAll() for filters, security headers and audit logging?
- **Company 44 / IQ-44:** Protect private JWT admin routes. After configuring admin credentials and Swagger exclusions, study the protected endpoints and shared token-filter placement. Interview: Why are login, refresh and OPTIONS routes public here, and how does addFilterAfter(authenticationTokenFilter, BasicAuthenticationFilter.class) affect token authentication?
- **Company 45 / IQ-45:** Build JWT admin authentication provider. Company 42 invokes this provider factory; follow its instantiated class to the authentication behavior mapped as Company 54. Interview: What must a custom AuthenticationProvider receive to safely validate admin credentials?
- **Company 46 / IQ-46:** Set admin API Basic realm. Company 44 directly calls this method when configuring HTTP Basic authentication failures. Interview: How does a Spring Security AuthenticationEntryPoint distinguish a 401 challenge from an authorization-denied response?
- **Company 47 / IQ-47:** Expose customer JWT authentication manager. After completing admin API security, enter active @Order(6) customer API configuration at its named manager. Interview: Why keep a customer AuthenticationManager separate from an admin manager, and how do bean names affect wiring?
- **Company 48 / IQ-48:** Register JWT customer user details. After exposing the customer manager, inspect which customer identity source it uses. Interview: How would you test that the JWT customer chain does not authenticate users through the admin UserDetailsService?
- **Company 49 / IQ-49:** Secure customer auth API endpoints. With customer identity resolution in place, inspect authorization rules and token-filter order for /api/v*/auth/**. Interview: Why must public auth paths precede the AUTH_CUSTOMER matcher, and which preflight and token-security tests belong in this chain?
- **Company 50 / IQ-50:** Build JWT customer authentication provider. After configuring customer endpoints, examine the provider factory that supplies customer-specific authentication logic. Interview: What changes when JWTCustomerAuthenticationProvider is wired with customer rather than admin UserDetailsService?
- **Company 51 / IQ-51:** Set customer API Basic realm. Company 49 directly references this factory for its HTTP Basic authentication entry point. Interview: What HTTP response and WWW-Authenticate challenge should this entry point send for an unauthenticated customer API call?
- **Company 52 / IQ-52:** Process request authentication tokens. Now inspect the actual OncePerRequestFilter instance registered in earlier security chains and created by Company 27. Interview: Why is reflecting an arbitrary request Origin together with Access-Control-Allow-Credentials:true unsafe, and what should a secure CORS policy validate?
- **Company 53 / IQ-53:** Clean per-request user context. Company 52 directly calls this helper; inspect cleanup ordering and error paths immediately after the filter body. Interview: Why should UserContext cleanup be in a finally block around chain.doFilter(), instead of running only after it returns normally?
- **Company 54 / IQ-54:** Authenticate JWT admin credentials. Company 45 instantiates this provider class; inspect its authenticate() behavior after token-filter processing. Interview: What is wrong with comparing the supplied password to a username rather than an encoded stored password, and how would you test this bug?
- **Company 55 / IQ-55:** Audit admin password comparison. Company 54 directly calls this helper, exposing a source-level password-verification bug. Interview: Why does passwordEncoder.matches(rawPassword, username) fail to verify the stored password hash, and what should be passed instead?
- **Company 56 / IQ-56:** Audit supported authentication types. Conclude the provider review by examining the supports(Class<?>) selection contract and its unconditional return value. Interview: What issues arise when AuthenticationProvider.supports() unconditionally returns true, and how should it restrict acceptable token classes?

Before this batch, verified Companies 1–36 against the pinned source: 36/36 valid ranges; zero missing company references; unique IDs; simulated UI audit 36/36 company pages, 83/83 external cards, 82 correct in-range highlights, 36/36 stale selections cleared. New active security source methods checked on the pinned reference; commented AdminConfigurationAdapter lines 211–277 intentionally excluded. IQ-55 and IQ-56 highlight potential security bugs in the source without modifying Shopizer.

### Previous-company review correction after Batch 37–56

Company 24 previously duplicated its verified Company 23 caller as an external card pointing to source line 69, outside Company 24's method (87–95). The inbound record is now classified as an internal company link to Company 23, and the graph derives that caller from Company 23's verified outbound edge. No source line or permanent company ID changed. The browser regression runner now distinguishes outside-method callsites from highlightable in-method lines.

## Mandatory pre-batch audit (standing rule)

Before **every future batch**, inspect every previously registered company and block the new batch if any audit fails:

1. Check permanent company IDs and interview IDs for uniqueness and gaps.
2. Match each existing company's Java file, pinned blob SHA, method and line range to its source snapshot.
3. Validate internal client/supplier links; distinguish direct method calls, Spring bean wiring, and framework callbacks. Do not misrepresent a registration as a method invocation.
4. Run the existing batch's company-page, numeric search, previous/next, detail-panel, and connection-card highlighting regression tests. Check stale-selection resets.
5. Correct and document any previous-company defect **before** publishing new company IDs.
6. After adding the requested batch, rerun all audits against the full updated registry; commit source snapshots, registry, progress and test updates atomically.

This audit gate was explicitly requested after Companies 1–36 and applies to Company 57 onward.

## Companies 57–76 — JWT provider and token utility

Previous-company gate: 56 verified company sources and interview IDs, 151 relationships; 56 rendered pages, 131 external selected cards, 131 correct code-line highlights, and 56 stale-selection resets—all passed before starting this batch.

- **57 (IQ-57) — Authenticate customer credentials:** Company 50 constructs this customer authentication provider; start with its actual authentication method. Interview: Why does passing a username rather than an encoded password to passwordMatch make the customer authentication flow incorrect?
- **58 (IQ-58) — Compare customer password:** Immediately inspect the helper directly invoked by Company 57 to reveal the incorrect comparison. Interview: What must the second argument to BCrypt PasswordEncoder.matches be, and why is username unsuitable?
- **59 (IQ-59) — Declare supported authentication tokens:** Review the AuthenticationProvider selection contract after the credential check. Interview: Why might supports() always returning true disrupt a chain of multiple Spring Security providers?
- **60 (IQ-60) — Expose customer identity lookup dependency:** Inspect the provider's accessor after its authentication and selection behavior. Interview: What are the tradeoffs of exposing a mutable UserDetailsService dependency through a getter?
- **61 (IQ-61) — Assign customer identity lookup dependency:** Complete the provider's setter/getter pair before moving to JWT utility methods. Interview: Why might constructor injection be safer than a mutable setter in a singleton AuthenticationProvider?
- **62 (IQ-62) — Read JWT username:** Begin JWTTokenUtil with user identity encoded in the signed token. Interview: Why must a JWT subject be signature-verified before it is trusted as the user identity?
- **63 (IQ-63) — Read JWT issuance time:** After subject identity, read issue time needed for password-reset checks. Interview: What does the iat claim prove, and can it replace signature or expiration verification?
- **64 (IQ-64) — Read JWT expiry timestamp:** Learn exp extraction before assessing strict and grace-based expiry. Interview: How should JWT signature and expiration verification behave for expired tokens and clock skew?
- **65 (IQ-65) — Read intended JWT audience:** Learn audience before special mobile/tablet expiration behavior. Interview: Why should a JWT consumer validate aud against its own intended audience?
- **66 (IQ-66) — Resolve any supported JWT claim:** Companies 62–65 share this helper; now inspect its generic extraction mechanism. Interview: How does Function<Claims,T> support type-safe reuse when reading different JWT claims?
- **67 (IQ-67) — Parse and verify signed JWT:** Continue from the generic claim helper into the actual signed-token parser. Interview: What errors should parseClaimsJws raise for forged, malformed or expired JWTs?
- **68 (IQ-68) — Check strict JWT expiration:** After parsing the exp claim, learn strict expiration enforcement. Interview: How would you test exact expiration boundaries without depending on the system clock?
- **69 (IQ-69) — Check expiration with 200-second allowance:** Contrast strict expiration with the source's 200-second grace variant. Interview: What security risk results from adding 200 seconds to a token's expiry before checking it?
- **70 (IQ-70) — Invalidate tokens preceding password reset:** After expiry, address revocation due to password changes. Interview: Why should JWTs issued before a password reset become invalid even if their exp is still valid?
- **71 (IQ-71) — Adjust reset cutoff by 200 seconds:** Compare with Company 70 and examine how shifting the cutoff changes the result. Interview: Why might adding grace seconds to the reset date reject MORE tokens despite the method's name?
- **72 (IQ-72) — Add seconds to a Date:** The grace checks use this common date helper; inspect its exact arithmetic next. Interview: When is Instant.plusSeconds more predictable and testable than Calendar.add for security timestamps?
- **73 (IQ-73) — Choose API token audience:** Transition from claims and validation helpers into JWT generation. Interview: What are the limits of always issuing tokens with a single 'api' audience?
- **74 (IQ-74) — Recognize mobile/tablet expiry exception:** After audience generation, examine special-case expiration handling. Interview: Why is using a mobile/tablet audience as a reason to bypass expiration risky?
- **75 (IQ-75) — Generate user JWT:** Inspect the public entry point for JWT creation after learning its audience helper. Interview: What claims should be placed in a new JWT, and why should subject, expiry and audience be verified by recipients?
- **76 (IQ-76) — Sign JWT with HS512:** Conclude with the signed-token builder that Company 75 directly invokes. Interview: What is the correct way to handle signing-key storage, rotation and expiration for HS512 JWTs?

Security issues evidenced in the original source: customer-provider password comparison against username (57–58), supports() always true (59), grace-window behavior (69 and 71), audience-based expiration exception (74), and symmetric HS512 key management (76). These are discussed, not silently changed.

## UX and code-line audit — Companies 1–76

- Reverified all 76 method signatures and exact line spans in 15 pinned Java snapshots before changing the UI. No source-line drift was found.
- Fixed false internal supplier highlighting: the actual caller line belongs to the previous company, while the destination highlights its method declaration; inbound caller links highlight their genuine callsite.
- Full-file Java code now lets users click or keyboard-activate mapped source lines to open the corresponding company at the same original line. Unmapped lines are read-only.
- Added an in-page Back button and synchronized URL fragments when entering/exiting companies, files, folders and history.
- Made source line numbers sticky during horizontal code scrolling and emphasized the corresponding connection cable on selection.
- Aligned SVG wire breakpoint to the stacked layout at 1100px and reduced dependency cards to one column on narrow phones.
- Corrected stale browser tab title and versioned static assets to avoid old cached scripts.
- Extended the browser regression to check Company 6→8 declaration highlighting, caller context, Back, file→Company 7 line 105, sticky gutter and mobile cables.
- Source/DOM unit checks are performed in model-side tooling; a full real-browser deployment check remains separate.

