# Rules for Clean Code

**Generated on:** December 5, 2025 at 11:14 AM CST

---

## **1. Naming Conventions**
*   **Reveal Intent:** Names must answer why an entity exists, what it does, and how it is used.
*   **Use Concept-Specific Word Classes:**
    *   **Classes:** Use nouns or noun phrases. Avoid verbs.
    *   **Methods:** Use verbs or verb phrases. Use `get`, `set`, and `is` for accessors/predicates.
*   **One Word Per Concept:** Pick one term (e.g., `fetch`, `retrieve`, or `get`) per abstract concept and use it consistently across the system.
*   **Match Scope to Length:** Use short names for small scopes and longer, descriptive names for large scopes. Names must be searchable.
*   **Avoid Encodings:** Do not use Hungarian notation, type encoding, or member prefixes (e.g., `m_`, `f`).
*   **Avoid Disinformation:** Do not use names that map to specific programming concepts (like `List`) unless the container is actually that type.
*   **Use Domain Names:** Prefer solution domain terms (CS patterns, algorithms) or problem domain terms. Rename implementation details to reflect the domain (e.g., `DayDate` instead of `SerialDate`).
*   **Pronounceability:** Ensure names can be easily spoken for team discussion.

## **2. Functions & Methods**
*   **Do One Thing:** Functions should do one thing, do it well, and do it only.
*   **Size:** Keep functions small (ideally < 20 lines).
*   **Abstraction Levels:** All statements within a function must be at the same level of abstraction.
*   **Stepdown Rule:** Code must read from top to bottom, descending one level of abstraction at a time.
*   **Arguments:**
    *   Prefer zero arguments (niladic).
    *   One (monadic) or two (dyadic) are acceptable.
    *   Avoid three or more (triadic+); justify strictly if used.
    *   **No Flag Arguments:** Do not pass booleans to select behavior; split the function instead.
    *   **No Output Arguments:** Modify the owning object state or return a value instead.
*   **Command Query Separation:** Functions should either do something (command) or answer something (query), never both.
*   **Side Effects:** Functions must have no hidden side effects.
*   **Conditionals:** Encapsulate conditional logic; avoid negative conditionals (express logic positively).

## **3. Comments & Documentation**
*   **Code > Comments:** Do not use comments to compensate for bad code; rewrite the code to be expressive.
*   **Allowed Comments:** Use only for explanation of intent, clarification of obscure arguments, warnings of consequences, or TODOs.
*   **Prohibited Comments:**
    *   No commented-out code (delete it; rely on version control).
    *   No attribution, changelogs, or bylines (rely on version control).
    *   No closing brace comments.
    *   No redundant/noise comments.
*   **Javadocs:** Reserve formal Javadocs for public APIs only.

## **4. Formatting & Layout**
*   **Vertical Formatting:**
    *   **Openness:** Separate packages, imports, and functions with blank lines.
    *   **Density:** Keep closely related lines of code vertically dense.
    *   **Ordering:** Dependent functions should be vertically close, with the caller immediately above the callee.
*   **Horizontal Formatting:** Limit line length (typically 100–120 characters).
*   **Variable Placement:**
    *   **Instance Variables:** Declare at the top of the class.
    *   **Local Variables:** Declare just above their first usage.
*   **Team Consensus:** The team must agree on a single formatting ruleset and adhere to it strictly.

## **5. Objects & Data Structures**
*   **Data Abstraction:** Expose abstract interfaces, not concrete data implementation.
*   **Law of Demeter:** A method should only call methods of its own class, objects it creates, or objects passed as arguments. Avoid "train wrecks" (chains of method calls like `a.getB().getC()`).
*   **Structure Choice:**
    *   Use **Objects** to expose behavior and hide data (allows new data types via subclassing).
    *   Use **Data Structures** (DTOs) to expose data and have no behavior (allows new functions).
    *   **Avoid Hybrids:** Do not mix the two.
*   **Base Classes:** Base classes should not depend on or know about their derivatives.

## **6. Error Handling**
*   **Exceptions over Return Codes:** Use exceptions for error handling.
*   **Unchecked Exceptions:** Prefer unchecked exceptions to preserve the Open-Closed Principle.
*   **Context:** Provide informative error messages.
*   **Structure:** Write the `try-catch-finally` block first.
*   **Null Safety:**
    *   Do not return `null`.
    *   Do not pass `null` into methods.
    *   Use the **Special Case Pattern** or empty collections instead.
*   **Boundary Wrapping:** Wrap third-party APIs to define exception classes in terms of your application's domain.

## **7. Concurrency**
*   **Single Responsibility:** Separate thread management code from application logic.
*   **Data Scope:** Encapsulate shared data and severely limit access to it.
*   **Synchronized Sections:** Keep critical sections as small as possible.
*   **Thread Independence:** Threads should share as little data as possible (use copies).
*   **Libraries:**
    *   Use thread-safe collections (e.g., `ConcurrentHashMap`).
    *   Use the `Executor` framework.
    *   Use non-blocking solutions (`AtomicInteger`, `Compare and Swap`) where possible.
*   **Testing Threaded Code:**
    *   Run with more threads than processors.
    *   Instrument code (sleep/yield) to force failures.
    *   Treat spurious failures ("one-offs") as legitimate threading issues.
    *   Ensure non-threaded logic works first (POJOs).

## **8. Architecture & Class Design**
*   **Class Organization:** Order: Public static constants -> private static vars -> private instance vars -> public functions -> private utilities.
*   **Encapsulation:** Keep variables and utility functions private.
*   **SOLID Principles:**
    *   **SRP:** Classes should have one reason to change.
    *   **OCP:** Open for extension, closed for modification.
    *   **DIP:** Depend on abstractions, not concrete details.
*   **Separation of Construction:** Separate system startup (object construction) from runtime logic (use Factories or Dependency Injection).
*   **Switch Statements:** Bury `switch` statements in an Abstract Factory (Polymorphism) to create objects; do not let them proliferate in logic.
*   **Simple Design Priority:** 1. Runs all tests. 2. Eliminates duplication. 3. Expresses intent. 4. Minimizes elements.

## **9. Testing**
*   **TDD Laws:** Write failing tests before production code. Write only enough to fail. Write only enough code to pass.
*   **F.I.R.S.T.:** Tests must be **F**ast, **I**ndependent, **R**epeatable, **S**elf-Validating, and **T**imely.
*   **Cleanliness:** Test code must be as clean and maintained as production code.
*   **Asserts:** Minimize assertions; aim for one concept per test function.
*   **Boundaries:** Test boundary conditions and run tests on all target platforms.
*   **Learning Tests:** Write tests to verify third-party APIs / Boundaries.

## **10. Java Syntax & Language Specifics**
*   **Constants:** Use `enum` types instead of integer constants.
*   **Imports:**
    *   Use wildcard imports (`import package.*`) if using two or more classes from a package to reduce clutter.
    *   Use `static import` instead of inheriting from classes strictly to access constants.
*   **Modifiers:**
    *   Prefer non-static methods to static methods (unless polymorphism is impossible).
    *   Do not use `final` on arguments/locals (reduces clutter).
*   **Serialization:** Delete `serialVersionUID` to rely on automatic generation unless specific cross-version control is required.

## **11. Domain Logic Constraints (Date/Spreadsheet Context)**
*   **Date Ranges:** Support years 1900–9999 and serial ordinals 2–2,958,465.
*   **Validation:** Throw `IllegalArgumentException` for invalid years, invalid days of the month, or out-of-range serials.
*   **Excel Compatibility:** Treat 1-Jan-1900 as ordinal 2 to synchronize with Excel's leap year bug.
*   **Equality Contracts:**
    *   `equals()` must check instance type and compare ordinal days.
    *   `hashCode()` must return the ordinal day.
    *   `compareTo()` must delegate to a date-difference calculation.
*   **Inheritance Model:** Factories must extend abstract factories; models must extend abstract models.

## Key Highlights

* Names must explicitly reveal intent, answering why an entity exists, what it does, and how it is used.
* Functions should be small, do exactly one thing, and adhere to a single level of abstraction.
* Avoid passing boolean flag arguments to functions; split the function into separate methods instead.
* Do not use comments to compensate for bad code; rewrite the code to be expressive and self-explanatory.
* Adhere to the Law of Demeter by ensuring methods only communicate with immediate friends, avoiding chained calls.
* Distinguish clearly between Objects (which expose behavior and hide data) and Data Structures (which expose data and have no behavior).
* Handle errors using exceptions rather than return codes, and strictly avoid passing or returning null values.
* Separate system startup and object construction from runtime logic using factories or dependency injection.
* Apply SOLID principles to architecture, ensuring classes have a single responsibility and depend on abstractions rather than details.
* Follow TDD laws by writing failing tests before production code and ensuring tests are Fast, Independent, Repeatable, Self-Validating, and Timely.

## Examples

* Implement a dedicated boundary test suite to verify the Date/Spreadsheet logic strictly adheres to the Excel 1900 leap year compatibility bug and serial ordinal limits.
* Conduct a code audit to identify mixed object construction and logic, refactoring them into Abstract Factories or Dependency Injection patterns to satisfy the Separation of Construction principle.
* Configure static analysis tools to strictly enforce the 'no null' policy and flag functions exceeding the 20-line threshold to align with the defined size and error handling standards.
* Review the current concurrency implementation to ensure thread management is fully decoupled from application logic and utilizes `Executor` frameworks instead of manual thread creation.
