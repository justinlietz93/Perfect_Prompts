**Subject: Phase 3: UX/UI Polish Focus - Cross-Component Integration, End-to-End Assembly, and Shared Infrastructure Enablement for [Project Name]**

**Date:** [Customizer: Enter Current Date]
**Time:** [Customizer: Enter Current Time with UTC Offset]

**1. Overall Purpose**
This prompt initiates **Phase 3: System Integration & Assembly** for the **[Project Name]** initiative. The autonomous agent executing this prompt must:
    a. Consolidate outputs from previously completed component builds (Phase 2 iterations) and confirm readiness for integration.
    b. Design and implement the cross-component wiring, shared infrastructure services, and interface contracts exactly as specified in the Phase 1 Architectural Blueprint and updated Phase 2 deliverables.
    c. Execute comprehensive integration validation (functional, data, workflow) ensuring components operate cohesively within the target environment.
    d. Update shared documentation, diagrams, and configuration artifacts to reflect the assembled system state.

**2. Core Execution Principles & Global Rules (MANDATORY - REITERATE WITH INTEGRATION FOCUS)**
*(Customizer Note: Maintain verbatim structure; adjust bracketed content only.)*

* **Apex Standards Adherence:** Continuous compliance with the **Apex Software Compliance Standards Guide** (located at `[User Input: Path to Standards Guide]`) is non-negotiable. Every integration artifact (code, scripts, infra definitions, tests, docs) must reference applicable `[(Rule #X: CODE)](...)` links.
* **Strict Sequential Execution:** Follow the generated Phase 3 plan in strict `Phase -> Task -> Step` order (`- [ ]`). Do not advance until current items meet `Internal Success Criteria` validated through `Internal Verification Method`.
* **Internal Verification & Standards Compliance:** Each integration task requires explicit verification against functional expectations and all linked standards.
* **Recursive Error Handling / Retry Logic:** Halt on any integration defect, analyze the root cause, remediate, and re-run verifications until success.
* **Autonomous Operation & Internal Logging:** Operate autonomously. Record integration outcomes and test metrics in the internal log as dictated by Section 5.

**3. Mandatory Quality & Finalization Rules (Integration Emphasis)**
*(Customizer Note: Keep structure; inject additional rules if Phase 1 blueprint mandates them.)*

Enforce all relevant rules from the **Apex Software Compliance Standards Guide** (`[User Input: Path to Standards Guide]`) with heightened attention to:
* Code Quality & Structure (Section 8: `QUAL-*`, including `QUAL-SIZE` for shared modules)
* Configuration Management (Section 12: `CONF-*`)
* Security & Access Controls across components (Section 13: `SEC-*`)
* Data Integrity & Migration (Reference applicable `DATA-*` rules if defined)
* Testing & Verification (Section 14: `TEST-*`, focus on integration and regression coverage)
* Deployment & Infrastructure (Section 17: `DEP-*` if applicable)
* Documentation & Knowledge Transfer (Section 18: `DOC-*`)
* Final Validation (Section 21: `FINAL-*`)

**4. Directive Section: Phase 3 - System Integration & Assembly**

* **Context Provided by User (Customizer Checklist):**
    * `[User Input: Project Name]`
    * `[User Input: List of Components Completed in Phase 2]`
    * `[User Input: Phase 1 Blueprint Path]`
    * `[User Input: Phase 2 Deliverables Path(s)]`
    * `[User Input: Path to Standards Guide]`
    * `[User Input: Current Environment/Repository State Reference]`

* **Instructions for Worker LLM:**

    1.  **Confirm Integration Scope:**
        * Identify all components slated for integration in this phase using `[List of Components Completed in Phase 2]` and cross-reference dependencies from the Phase 1 blueprint.
        * Enumerate integration interfaces, shared contracts, data exchange formats, and infrastructure services required.
        * Validate availability of prerequisite artifacts (code modules, schemas, configs) from prior phases.

    2.  **Generate Detailed Integration Execution Plan:**
        * Produce a `Phase -> Task -> Step` plan (`- [ ]`) covering:
            * Environment preparation and dependency synchronization.
            * Interface binding, adapter creation, or API gateway configuration.
            * Data migration/synchronization scripts if needed.
            * Integration test suite development & execution.
            * Observability, logging correlation, and resilience hardening.
            * Documentation updates (architecture diagrams, runbooks).
        * Ensure each step includes precise `[(Rule #? : CODE)](...)` references.

    3.  **Execute Integration Plan Sequentially:**
        * Perform all plan items in order, modifying only files relevant to integration scope.
        * Run all integration tests and regression checks defined.
        * Capture logs/metrics per Section 5 and attach results to verification notes.
        * Update shared docs/configs to reflect new system state.

    4.  **Self-Verify & Summarize:**
        * Confirm the integrated system meets functional & NFR expectations defined in the Phase 1 blueprint.
        * Validate all success criteria & verification methods have been satisfied.
        * Prepare a concise integration summary (components involved, interfaces activated, tests executed, outstanding risks).

* **Internal Success Criteria (Worker LLM Self-Check):** All components listed for integration are wired together per blueprint, integration tests pass, shared configs/docs updated, and logs captured.
* **Internal Verification Method:** Review execution trace, confirm test results, ensure documentation alignment, verify standards compliance for all touched items.

**5. Test Reporting Protocol (Internal)**
*(Customizer Note: Keep consistent across phases.)*
* **Log File Location:** `docs/Test_Result_Analysis.md`
* **Data Points per Entry:** Date/Time, Scope (Integration Phase), Components, Test Suites, Pass/Fail, Key Metrics (latency, throughput, error rates), Summary Findings.
* **Update Frequency:** After each major integration test suite or milestone.

**6. Final Instruction**
Execute all directives in Section 4 sequentially. Upon completion:
    * Report integration status for **[Project Name]**.
    * Provide references to modified files/configs.
    * Supply test evidence and highlight any residual issues.
    * Deliver the finalized integration execution plan with all checkboxes marked `- [x]`.

**7. Contextual Footer**
*(Instructions generated: [Customizer: Timestamp]. Location context: [Customizer: Location])* 