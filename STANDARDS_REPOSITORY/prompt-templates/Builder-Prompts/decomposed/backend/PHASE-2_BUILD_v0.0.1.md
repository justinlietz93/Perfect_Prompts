**Subject: Phase 2: Build Backend Component: [Component Name] (STRICT SERVICE SCOPE)**

**Date:** [Customizer: Current Date]
**Time:** [Customizer: Current Time UTC+/-Offset]

**1. Overall Purpose**
This prompt governs **Phase 2: Backend Component Build** for **[Component Name]** within **[Project Name]**. The executing agent must:
    a. Retrieve specifications for **[Component Name]** (application service, domain service, repository, adapter) from the Phase 1 blueprint.
    b. Generate a standards-compliant execution plan (`Phase -> Task -> Step`, `- [ ]`) covering implementation, tests, documentation, and infrastructure bindings strictly for **[Component Name]**.
    c. Execute the plan, producing verified, tested backend code that adheres to dependency inversion, repository pattern, and DI rules without leaking scope.

**2. Core Execution Principles & Global Rules (REITERATED)**
* **Apex Standards Adherence:** Follow the Apex Standards Guide (`[User Input: Path to Standards Guide]`) referencing `[(Rule #X: CODE)](...)`.
* **Dependency Discipline:** Presentation layer must depend on BL interfaces only; infrastructure implements those interfaces. **[Component Name]** must respect these edges.
* **Strict Sequential Execution:** Execute generated plan sequentially, marking completion only when success criteria satisfied.
* **Internal Verification & Compliance:** Validate outputs against standards, repository pattern, transactionality, security requirements.
* **Recursive Remediation:** Halt on failure, remediate, retest.
* **Autonomous Logging:** Log progress to `docs/Test_Result_Analysis.md` per Section 5.

**3. Mandatory Quality & Finalization Rules**
Continuously enforce:
* Code Quality (`QUAL-*`, `QUAL-SIZE`, cyclomatic complexity caps).
* Security (`SEC-*`: auth, secrets, encryption, secure coding).
* Data Integrity (`DATA-*`: migrations, consistency checks).
* Testing (`TEST-*`: unit, integration, contract, load for service-level components).
* Documentation (`DOC-*`: ADR updates, API specs, README snippets).
* Implementation Correctness (`IMPL-*`).

**4. Directive Section: Phase 2 - Backend Component Execution**

* **Context Provided by User:**
    * `[Project Name]`
    * `[Component Name]`
    * `[Path to Phase 1 Output]`
    * `[Path to Standards Guide]`
    * `[Current Project State Reference]`

* **Instructions for Worker LLM:**

    **Scope Enforcement:** Limit all actions to **[Component Name]** and its explicitly documented interfaces/dependencies.

    1.  **Load Context:**
        * Extract functional requirements, NFR impacts, interface contracts, and dependencies for **[Component Name]** from the Phase 1 blueprint.
        * Identify required abstractions, DTOs, domain models, repository interfaces, and infrastructure touchpoints.
        * Confirm awareness of relevant rules (`QUAL-DI`, `DATA-TRANS`, `SEC-AUTH`, `TEST-UNIT`, `TEST-INTEG`).

    2.  **Generate Execution Plan:**
        * Detail implementation steps for application/domain logic abiding by dependency inversion (no framework code inside business logic).
        * Include repository interface definitions, adapter scaffolding, DI registration updates (if in scope), and transactional boundaries.
        * Plan tests: unit tests for business logic, integration/contract tests for adapters, seed data validations.
        * Include documentation tasks (API spec updates, ADR note) and configuration updates limited to **[Component Name]**.
        * Provide `Internal Success Criteria` and `Internal Verification Method` referencing standards for each task.

    3.  **Execute Plan:**
        * Implement code per plan; ensure application/domain code remains framework-agnostic.
        * Implement infrastructure adapters abiding by repository pattern and interface contracts.
        * Wire DI container using constructor injection only.
        * Run planned tests; ensure they pass and meet coverage/performance goals.
        * Update documentation and configuration artifacts.
        * Log progress and results.

* **Internal Success Criteria Check:** Confirm only **[Component Name]** files changed, all tests executed/passed, documentation updated, DI boundaries respected.
* **Internal Verification Method:** Review plan vs. execution, confirm layering compliance, inspect dependencies, re-run targeted tests if necessary.

**5. Test Reporting Protocol**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Component (**[Component Name]**), Task/Step ID, Test Type (unit/integration/contract), Metrics (latency, coverage), Status, Notes.
* **Update Frequency:** After each test suite or major verification step.

**6. Final Instruction**
Complete planning and implementation for **[Component Name]**, deliver summary of outputs (files, tests, docs), provide execution plan with `- [x]` status, and reference relevant commits.

**7. Contextual Footer**
*(Instructions generated: [Timestamp]. Location context: [Location])* 
