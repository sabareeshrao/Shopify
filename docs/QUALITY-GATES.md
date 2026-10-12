# Implementation and MCQ quality gates

## A task is VERIFIED only if

1. The complete question and dependencies are visible in the canonical bank.
2. Java implementation is shown **incrementally** in IntelliJ IDEA with all required file paths, imports, configs and commands—no hidden manual typing.
3. For Java examples, include `// Voice:` instructions immediately before new code, and the exact console output when the example prints output.
4. Meaningful tests run with recorded commands, expected outputs and actual results. No passing-test assertions without execution evidence.
5. For HTTP features, document method, URL, request, success status, error response, authorization and idempotency if applicable.
6. For database features, include schema migration, constraints, rollback behavior, representative rows and database-backed tests.
7. Security, invalid input, concurrency and failure recovery are considered appropriate to the task.
8. The code compiles, application boots when applicable, and GitHub commit is linked in tracking/PROGRESS.csv.
9. A concise five-year Java developer interview answer explains why the design was chosen.
10. Progress is updated only after the user confirms the completed task and the artifacts are actually verified.

## MCQ lesson standard

Ask truly diverse questions: core Java, internal mechanics, Spring, SQL, API semantics, what the code prints, debugging, threat modeling, transaction behavior and design alternatives. Provide correct answers and explanations, not copied interview misinformation. Do not repeat semantically identical questions for volume. For complex tasks 15–35 MCQs may be appropriate; short tasks may need fewer.

## Scope boundaries

- Shopizer's five backend Maven modules are *not* independent microservices.
- Original public repos are a reference, **not** proof of current dependency safety.
- Java 21 and a compatible modern Spring Boot line are the new implementation baseline.
- Test payment providers in sandbox; never store raw payment card details.
- Production-readiness is a verification objective, not an automatic status granted by reaching a question ID.
