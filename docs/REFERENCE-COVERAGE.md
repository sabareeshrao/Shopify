# Shopizer reference coverage map (initial, editable)

Pinned snapshot identifiers are in the repository README. This is a **feature-area mapping**, not a statement that each Shopizer class is copied, reimplemented, or already understood. Use it to discover missing functionality while coding; file-specific mappings and gap evidence should be added as the investigation deepens.

| Phases | Reference repository area | Intended coverage |
|---|---|---|
| 00–04 | `pom.xml`, `sm-core-model`, `sm-core`, `sm-shop-model`, `sm-shop` | Modules, entities, services, APIs |
| 05 | `sm-core-model/.../reference`, `sm-shop/.../references` | Countries, zones, currency, languages |
| 06 | `sm-core-model/.../merchant`, `sm-shop/.../store` | Stores, merchants and configuration |
| 07 | `sm-shop/.../security`, `sm-shop/.../api/v1/security` | Authentication and authorization |
| 08 | `sm-core-model/.../catalog/category`, `sm-shop/.../api/v1/category` | Catalog tree and category routes |
| 09–10 | `sm-core-model/.../catalog/product`, `sm-shop/.../api/v1/product`, `sm-shop/.../api/v2/product` | Products, variants, price options |
| 11 | `sm-core/.../modules/cms`, `sm-shop/.../api/v1/content` | Product images and content |
| 12–14 | `sm-core/.../services/catalog`, `sm-shop/.../api/v1/search` | Pricing, inventory, search |
| 15 | `sm-core-model/.../customer`, `sm-shop/.../api/v1/customer` | Customers and reviews |
| 16–21 | `sm-core-model/.../shoppingcart`, `.../shipping`, `.../tax`, `.../payments`, `.../order` | Cart, fulfillment and purchase lifecycle |
| 22–23 | `sm-core/.../modules/email`, `.../integration` | Email, providers and data processing extensions |
| 24 | `shopizer-shop-reactjs/src/components`, `src/pages`, `src/redux` | Customer React storefront |
| 25 | `shopizer-admin/src/app/pages` | Admin Angular dashboard |
| 26–27 | Backend `src/test`, `.circleci`, Docker files | Testing, operations and modernization |

## Coverage review protocol

For each baseline phase, build a source-derived checklist of entities, APIs, workflows, external integrations and boundary cases. Mark items **COVERED**, **DEFERRED**, **NOT_APPLICABLE**, or **GAP**; for a GAP, file a change request and add a numbered question. Never assert full parity simply because the planned count has been reached.

## Explicit extensions vs literal reference parity

The curriculum includes modernization and training additions such as Java 21, newer Spring Boot/Jakarta APIs, transactional outbox patterns, Testcontainers and richer failure tests. These may be improvements beyond the selected Shopizer snapshot. Record these as extensions rather than misattributing them to the original code.
