**Subject: Phase 3: Frontend Integration, Cross-Surface Assembly, and Shared Experience Alignment for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt governs **Phase 3: Frontend Integration** for **[Project Name]**. The executing agent must assemble completed frontend components into cohesive experiences, activate shared infrastructure (routing, state, localization), and verify UI-to-backend contracts. Objectives include:
    a. Cataloging implemented frontend components, routes, states, and shared libraries ready for integration.
    b. Orchestrating assembly of shells, navigation, layout frameworks, and interaction flows across view modules.
    c. Ensuring dependency rule compliance (Presentation → Business Logic interfaces) and verifying API adapter contracts.
    d. Activating shared infrastructure (routing, design system tokens, observability instrumentation).
    e. Conducting integration-level tests (end-to-end, visual regression, accessibility sweeps) to confirm cohesive UX.
    f. Logging integration evidence and remediation actions while maintaining standards compliance.

**2. Core Execution Principles & Global Rules (MANDATORY ADHERENCE)**
* Continue enforcing Apex Standards Guide requirements (`[Path to Standards Guide]`).
* Maintain Hybrid-Clean Architecture boundaries; Presentation layer must only depend on BL interfaces, not infrastructure implementations.
* Preserve sequential execution of integration plan tasks (`Phase -> Task -> Step`).
* Perform internal verification for each integration activity, referencing applicable rules (`[(Rule #X: CODE)](...)`).
* Apply iterative remediation for integration failures; document root causes and fixes.
* Update internal logs per `Test Reporting Protocol` (Section 5).

**3. Mandatory Quality & Finalization Rules**
Reaffirm continuous enforcement of:
* Code Structure & Size (`QUAL-*`, `QUAL-SIZE`).
* Security & Privacy for client interactions (`SEC-*`, CSP, token handling).
* Accessibility (`QUAL-A11Y`, WCAG AA) across integrated flows.
* Performance Budgets (`QUAL-PERF`, `TEST-PERF`) for combined bundles/routes.
* Testing (`TEST-*`, particularly `TEST-E2E`, `TEST-VISUAL`, `TEST-A11Y`).
* Documentation (`DOC-*`, update navigation maps, component catalogs).
* Change Management (`CONF-*`, feature flags for rollout).

**4. Directive Section: Phase 3 - Frontend Integration Execution**

* **Inputs Required:**
    * `[Path to Phase 2 Outputs]`: Component deliverables and execution plans.
    * `[Path to Standards Guide]`: Apex Standards location.
    * `[Project Repo Access]`: Access instructions for codebase.
    * `[Integration Targets]`: List of components/routes/features confirmed complete.

* **Integration Plan Requirements:**
    1.  **Assemble Integration Context:**
        * Inventory completed components and confirm readiness via Phase 2 checklists.
        * Map dependencies: shared state slices, service facades, routing entries, global styles.
        * Identify pending shared infrastructure tasks (e.g., theming provider, analytics bootstrap).
    2.  **Generate Integration Plan (`- [ ]`):**
        * Define tasks for enabling routing/navigation, layout composition, cross-component communication, and data prefetch strategies.
        * Include tasks for integrating with backend APIs via BL interfaces, ensuring no direct infrastructure coupling.
        * Specify accessibility, performance, and responsiveness validations for integrated flows.
        * Plan documentation updates (navigation maps, integration diagrams).
        * Define `Internal Success Criteria`/`Internal Verification Method` per task referencing standards.
    3.  **Execute Integration Plan:**
        * Implement routing updates, layout scaffolds, and state orchestration per plan.
        * Wire telemetry, logging, and feature flags consistently across surfaces.
        * Run integration tests: E2E flows, contract tests (UI ↔ BL), visual regression, accessibility sweeps.
        * Resolve defects, iterating until all success criteria satisfied.
        * Update documentation and logs.
    4.  **Compliance Verification:**
        * Confirm adherence to dependency rule, performance budgets, and a11y requirements.
        * Validate integrated bundles respect size thresholds.
        * Ensure test results are captured in logs and summarized.

* **Internal Success Criteria:** Integration plan fully executed; navigation/routes functional; shared state/services working; tests passing; documentation/logs updated; standards compliance confirmed.
* **Internal Verification Method:** Execute final review referencing plan items, rerun targeted tests if any metrics borderline, confirm no direct Presentation → Infrastructure dependencies exist.

**5. Test Reporting Protocol (Integration Focus)**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Scope (Integration feature/route), Test Suite (E2E, visual, accessibility, performance), Metrics (LCP, FID, CLS, axe violations), Status, Findings.
* **Update Frequency:** After each integration test cycle and remediation iteration.

**6. Final Instruction**
Assemble the integrated frontend experience per the generated plan, meeting all standards, performance, and accessibility requirements. Provide summary of integrated components, test outcomes, remediation actions, and updated documentation references upon completion.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
