# Master question index

**Initial baseline: 1,025 original build tasks, 28 phases.** This index lists *initial allocations*: approved change requests may revise wording, split questions or move execution order while IDs remain permanent.

| Phase | Initial ID range | Initial tasks |
|---|---|---:|
| [00 — Reference investigation and design](./phase-00.md) | Q0001–Q0012 | 12 |
| [01 — IntelliJ, Java 21, Maven, Git](./phase-01.md) | Q0013–Q0032 | 20 |
| [02 — Spring Boot modular skeleton](./phase-02.md) | Q0033–Q0058 | 26 |
| [03 — MySQL and JPA](./phase-03.md) | Q0059–Q0090 | 32 |
| [04 — Shared DTOs and REST](./phase-04.md) | Q0091–Q0115 | 25 |
| [05 — Reference data](./phase-05.md) | Q0116–Q0140 | 25 |
| [06 — Merchants and stores](./phase-06.md) | Q0141–Q0175 | 35 |
| [07 — Security and users](./phase-07.md) | Q0176–Q0218 | 43 |
| [08 — Catalogs and categories](./phase-08.md) | Q0219–Q0255 | 37 |
| [09 — Products and SKUs](./phase-09.md) | Q0256–Q0304 | 49 |
| [10 — Attributes and variants](./phase-10.md) | Q0305–Q0349 | 45 |
| [11 — Images, storage and CMS](./phase-11.md) | Q0350–Q0381 | 32 |
| [12 — Pricing and promotions](./phase-12.md) | Q0382–Q0423 | 42 |
| [13 — Inventory](./phase-13.md) | Q0424–Q0457 | 34 |
| [14 — Search](./phase-14.md) | Q0458–Q0493 | 36 |
| [15 — Customers and reviews](./phase-15.md) | Q0494–Q0533 | 40 |
| [16 — Cart](./phase-16.md) | Q0534–Q0567 | 34 |
| [17 — Shipping](./phase-17.md) | Q0568–Q0599 | 32 |
| [18 — Tax and totals](./phase-18.md) | Q0600–Q0629 | 30 |
| [19 — Payments](./phase-19.md) | Q0630–Q0671 | 42 |
| [20 — Checkout](./phase-20.md) | Q0672–Q0719 | 48 |
| [21 — Orders and refunds](./phase-21.md) | Q0720–Q0761 | 42 |
| [22 — Email and integration adapters](./phase-22.md) | Q0762–Q0788 | 27 |
| [23 — Bulk import/export](./phase-23.md) | Q0789–Q0812 | 24 |
| [24 — React storefront](./phase-24.md) | Q0813–Q0877 | 65 |
| [25 — Angular admin](./phase-25.md) | Q0878–Q0942 | 65 |
| [26 — Hardening and tests](./phase-26.md) | Q0943–Q0987 | 45 |
| [27 — Docker and deployment](./phase-27.md) | Q0988–Q1025 | 38 |
| **Total** | **Q0001–Q1025** | **1,025** |

## Start learning

1. Open [Phase 00](./phase-00.md) and paste the full text of **Q0001** into ChatGPT.
2. Request diverse multiple-choice training for that question, with runnable Java code, voice-typing comments and actual expected output where relevant.
3. Implement it in IntelliJ IDEA in short explained increments and validate it.
4. After verification and your confirmation, commit implementation, lesson and tracker evidence; then proceed to the next task specified by [editable execution order](../tracking/EXECUTION_ORDER.md).

## We can change this roadmap

- Add newly discovered questions in [extensions](./extensions/README.md), beginning at **Q1026**.
- Review changes in [the change log](../changes/CHANGELOG.md).
- Submit a scoped revision with [the change request template](../changes/CHANGE-REQUEST-TEMPLATE.md).
- Current status is recorded in [PROGRESS.csv](../tracking/PROGRESS.csv), rather than inferring it from question IDs.
- [Quality gates](../docs/QUALITY-GATES.md) prevent false completion or untested feature claims.

## Scope integrity

The full Shopizer-class backend, React storefront and Angular admin are included in the **planned** curriculum. Source-to-feature parity will be reviewed during development. Do not equate completing the initial 1,025 tasks automatically with matching every current or historical Shopizer feature.
