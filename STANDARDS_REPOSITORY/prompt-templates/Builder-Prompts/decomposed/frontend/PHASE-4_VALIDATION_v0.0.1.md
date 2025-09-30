**Subject: Phase 4: Frontend Experience Validation, Hardening, and Pre-Release Readiness for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt activates **Phase 4: Frontend Validation**. The agent must execute comprehensive quality assurance across the assembled UI to ensure reliability, accessibility, performance, and security prior to release. Objectives include:
    a. Planning and executing exhaustive validation across routes, states, and device/browser matrices.
    b. Running automated and manual accessibility audits, performance profiling, and resilience testing.
    c. Verifying security posture (CSP, XSS protections, token handling) and dependency rule adherence.
    d. Capturing evidence, defects, and remediation actions while iterating until success criteria met.
    e. Updating documentation and logs to reflect validation status and outstanding risks.

**2. Core Execution Principles & Global Rules**
* Maintain compliance with Apex Standards Guide and Hybrid-Clean Architecture boundaries.
* Execute validation plan sequentially, marking `- [x]` only when success criteria satisfied.
* Enforce rigorous internal verification referencing `[(Rule #X: CODE)](...)` for each validation task.
* Apply iterative remediation cycles for failed tests or metrics.
* Log all validation activities, results, and defects per Section 5.

**3. Mandatory Quality & Finalization Rules**
Focus on enforcing:
* Testing Standards (`TEST-*`: unit, integration, e2e, performance, accessibility, cross-browser).
* Security Standards (`SEC-*`: CSP, clickjacking protection, input sanitization).
* Performance Standards (`QUAL-PERF`: bundle size, render metrics, memory usage).
* Accessibility Standards (`QUAL-A11Y`: WCAG 2.1 AA, keyboard navigation, screen reader support).
* Documentation Standards (`DOC-*`: validation reports, known issues catalog).
* Release Readiness (`FINAL-*`: `FINAL-SWEEP`, `FINAL-RISK`).

**4. Directive Section: Phase 4 - Frontend Validation Execution**

* **Inputs Required:**
    * `[Validation Matrix]`: Target browsers/devices/locales/accessibility assistive tech.
    * `[Performance Budgets]`: Baseline thresholds for Core Web Vitals, bundle sizes.
    * `[Security Checklist]`: Client-side security requirements and threat model.
    * `[Path to Integration Output]`: Integrated frontend from Phase 3.

* **Validation Plan Requirements:**
    1.  **Plan Validation Campaign:**
        * Inventory test suites (unit, integration, e2e, visual, accessibility, performance) and ensure coverage of critical journeys.
        * Define manual exploratory testing scenarios, edge cases, and regression targets.
        * Establish acceptance gates per metric/standard.
    2.  **Execute Automated Suites:**
        * Run unit/integration/e2e suites with cross-browser automation.
        * Run visual regression, accessibility (axe, pa11y), and performance (Lighthouse/WebPageTest) suites.
        * Capture raw outputs, compare against thresholds, log deviations.
    3.  **Perform Manual/Exploratory Validation:**
        * Execute manual cross-device checks, screen reader validation, keyboard navigation, offline/resume flows.
        * Validate localization, theming, and responsive breakpoints.
    4.  **Security & Resilience Verification:**
        * Validate CSP headers, token storage, input sanitization, anti-CSRF flows.
        * Test error boundaries, fallback UI, and resilience under degraded network conditions.
    5.  **Defect Management & Remediation:**
        * Log defects with severity, root cause, remediation owner.
        * Prioritize fixes, execute remediation sprints, and retest until all blockers resolved.
    6.  **Evidence & Documentation:**
        * Update validation dashboard/report summarizing results, metrics, and residual risks.
        * Document known issues, mitigations, and recommendations for release gate.

* **Internal Success Criteria:** All planned validations executed; metrics within thresholds or approved exceptions documented; no open critical defects; documentation/logs updated; standards compliance confirmed.
* **Internal Verification Method:** Conduct final audit referencing validation plan, verify evidence attachments, re-run spot checks on high-risk journeys, confirm compliance with dependency rule (no presentation direct infrastructure dependencies introduced during fixes).

**5. Test Reporting Protocol (Validation Focus)**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Scope (Route/Feature), Test Suite, Metrics (LCP, CLS, accessibility score, CSP status), Pass/Fail, Defects, Remediation.
* **Update Frequency:** After each automated suite run and manual validation cycle.

**6. Final Instruction**
Complete the validation campaign, document results and remediation, and provide a readiness assessment summarizing metrics, outstanding risks, and go/no-go recommendation for Phase 5.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
