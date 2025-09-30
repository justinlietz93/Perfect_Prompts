**Subject: Phase 2: Build Frontend Component: [Component Name] (STRICT UX SCOPE)**

**Date:** [Customizer: Current Date]
**Time:** [Customizer: Current Time UTC+/-Offset]

**1. Overall Purpose**
This prompt initiates **Phase 2: Frontend Component Build** for the UI element identified below: **[Component Name]** within the **[Project Name]** experience. The agent executing this prompt must:
    a. Retrieve the detailed frontend specifications for **[Component Name]** from the approved Phase 1 blueprint and design system documentation.
    b. Generate a standards-compliant execution plan (`Phase -> Task -> Step`, `- [ ]`) covering implementation, accessibility, state integration, testing, and documentation strictly for **[Component Name]**.
    c. Execute the plan rigorously, producing verified, accessible, performant UI output that integrates correctly with established frontend contracts and backend interfaces while remaining inside scope.

**2. Core Execution Principles & Global Rules (MANDATORY ADHERENCE - REITERATED)**
*(This section is invariant; include verbatim in the final prompt)*
* **Apex Standards Adherence:** Compliance with the **Apex Software Compliance Standards Guide** (located at `[User Input: Path to Standards Guide]`) is non-negotiable. All generated plans, code, styles, and tests for **[Component Name]** MUST comply, including references to `[(Rule #X: CODE)](...)`.
* **Strict Sequential Execution:** Execute the generated component plan sequentially. Mark completion only when `Internal Success Criteria` are satisfied via the `Internal Verification Method`.
* **Internal Verification & Standards Compliance:** Perform rigorous verification against all referenced rules, WCAG success criteria, performance budgets, and security mandates before marking tasks complete.
* **Recursive Error Handling / Retry Logic:** Halt on failures, analyze causes, remediate, and re-verify.
* **Autonomous Operation & Internal Logging:** Operate autonomously. Log results in `docs/Test_Result_Analysis.md` per Section 5.

**3. Mandatory Quality & Finalization Rules (Reference Standards Guide - Continuous Enforcement)**
*(Invariant; include verbatim. Ensure path accuracy.)*
Enforce relevant sections of the **Apex Software Compliance Standards Guide** (`[User Input: Path to Standards Guide]`) with frontend emphasis:
* Code Quality & Structure (Section 8: `QUAL-*`, `QUAL-SIZE`, modular component structure).
* Accessibility (Section 13: `SEC-*`, `QUAL-A11Y`).
* Security (Section 13: `SEC-*` for client sanitization, CSP compliance).
* Testing (Section 14: `TEST-*`, component/unit/interaction/visual tests).
* Performance (Section 14: `TEST-PERF`, `QUAL-PERF`).
* Documentation (Section 18: `DOC-*`, component usage docs, Storybook notes).
* Implementation Correctness (Section 19: `IMPL-*`).
* *(Add specific standards from Phase 1 blueprint: e.g., Design Token Governance Rule #?: `QUAL-DS`.)*

**4. Directive Section: Phase 2 - Frontend Component Planning and Execution**

* **Context Provided by User:**
    * `[Project Name]`: Name of the overall initiative.
    * `[Component Name]`: Specific frontend component/surface to build. **ONLY THIS COMPONENT IS IN SCOPE.**
    * `[Path to Phase 1 Output]`: Location of the frontend architecture blueprint and design system references.
    * `[Path to Standards Guide]`: Location of Apex Standards.
    * `[Current Project State Reference]`: Instructions for accessing existing codebase/design tokens.

* **Instructions for Worker LLM:**

    **STRICT SCOPE CONSTRAINT:** Work exclusively on **[Component Name]**. Do not modify unrelated components, global theming, or backend contracts beyond the explicit dependencies defined in Phase 1.

    1.  **Load Context (for [Component Name] ONLY):**
        * Parse Phase 1 blueprint and design references to extract functional requirements, UX acceptance criteria, accessibility notes, state interfaces, and API contracts for **[Component Name]**.
        * Confirm awareness of performance budgets (First Input Delay, LCP, bundle size) applicable to **[Component Name]**.
        * Ensure `[(Rule #? : QUAL-A11Y)](...)`, `[(Rule #? : QUAL-PERF)](...)`, and other relevant rules are at hand.
        * Validate access to design tokens, shared libraries, and project repository.

    2.  **Generate Detailed Component Execution Plan:**
        * Produce a sequential plan covering:
            * Component scaffolding and dependency injection alignment with Hybrid-Clean Architecture (Presentation layer depending only on BL interfaces).
            * Styling/theming integration using approved tokens.
            * State management wiring (selectors, dispatchers, service facades) in compliance with dependency inversion.
            * Accessibility instrumentation (semantic markup, keyboard focus, ARIA, contrast).
            * Testing strategy: unit, interaction, visual regression, accessibility automation.
            * Documentation updates (Storybook MDX, usage notes).
        * Reference applicable Apex rules inline.
        * Define `Internal Success Criteria` and `Internal Verification Methods` per Task.

    3.  **Execute Generated Plan:**
        * Implement **[Component Name]** per plan, respecting layering rules (Presentation -> BL interfaces only).
        * Ensure code organization prevents direct dependency on Infrastructure implementations.
        * Run all defined tests, lighthouse/aXe audits as applicable, and record outcomes.
        * Update documentation and visual catalogs.
        * Log actions and results to `docs/Test_Result_Analysis.md`.

* **Internal Success Criteria Check:** Confirm that only **[Component Name]** artifacts were modified, all tests/audits passed, documentation updated, and logs recorded.
* **Internal Verification Method:** Review execution trace, confirm compliance with Apex rules, inspect component layering, rerun accessibility/performance checks if thresholds unmet.

**5. Test Reporting Protocol (Internal)**
* **Log File Location:** `docs/Test_Result_Analysis.md`
* **Data Points per Entry:** Date/Time, Scope (Component: **[Component Name]**), Task/Step ID, Test Suite, Pass/Fail, Key Metrics (a11y score, bundle size, render latency), Summary Findings/Errors.
* **Update Frequency:** After each significant test batch or verification step for **[Component Name]**.

**6. Final Instruction (for Worker LLM)**
Execute context loading, planning, and implementation strictly for **[Component Name]**. Upon completion:
    * Provide success confirmation with references to updated files and commit hash.
    * Report test/audit outcomes and updated documentation assets.
    * Deliver the final execution plan with all items marked `- [x]`.

**7. Contextual Footer**
*(Instructions generated: [Timestamp]. Location context: [Location])* 
