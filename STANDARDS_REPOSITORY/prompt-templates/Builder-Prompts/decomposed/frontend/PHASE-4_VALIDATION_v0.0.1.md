**Subject: Phase 4: Frontend Track — User-Facing Validation & Accessibility Certification for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Phase 4 validates the frontend experience against UX, accessibility, performance, and security acceptance criteria. The worker agent performs comprehensive testing and assembles the evidence package required by the architecture and testing tracks.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Follow `UI-VAL`, `ACC-WCAG`, `PERF-UI`, `SEC-UI`, and `DOC-VAL` standards.
* Validation must use release-candidate builds and production-like configuration.
* Any defect outside frontend scope must be reported to the owning track instead of fixed here.

**3. Mandatory Quality & Finalization Rules**
Results stored in `frontend/outputs/phase-4/`. Evidence includes screenshots, performance reports, accessibility audits, and test logs. Annotate each with requirement IDs and standards references.

**4. Directive Section: Frontend Phase 4 Tasks**
* **Input Context:**
    * Integration report, architecture certification checklist, UX acceptance criteria.
    * Testing track validation plan.

* **Execution Tasks (sequential):**
    - [ ] **Task 4.1: Validation Plan Finalization** *(Planning)*
        - [ ] Align with testing track on scope, environments, and success thresholds.
        - [ ] Document plan in `frontend_validation_plan.md`.
    - [ ] **Task 4.2: Functional Acceptance Testing** *(Testing)*
        - [ ] Execute scripted end-user scenarios covering all critical paths.
        - [ ] Capture pass/fail status with evidence for each scenario.
    - [ ] **Task 4.3: Accessibility Compliance** *(Accessibility)*
        - [ ] Run WCAG AA audits (automated + manual assistive tech checks) and record compliance status.
        - [ ] Document remediation or waivers for any outstanding issues.
    - [ ] **Task 4.4: Performance & Resilience Testing** *(Performance)*
        - [ ] Measure core web vitals, page weight, and responsiveness under load.
        - [ ] Validate offline/poor network behaviour if applicable.
    - [ ] **Task 4.5: Security & Privacy Checks** *(Security)*
        - [ ] Verify frontend handles tokens/session data per security track rules.
        - [ ] Confirm no sensitive data exposure in logs or browser storage.
    - [ ] **Task 4.6: Evidence Pack Assembly** *(Documentation)*
        - [ ] Compile all findings into `frontend_validation_report.md` with sign-off fields for UX, testing, and architecture leads.

* **Internal Success Criteria:** Validation plan executed, evidence recorded, sign-off ready with no unresolved critical issues.
* **Internal Verification Method:** Cross-check report against validation plan to ensure every item has evidence and responsible owner.

**5. Test Reporting Protocol (Internal)**
Update `docs/Test_Result_Analysis.md` with validation outcomes tagged `FRONT-PH4`.

**6. Final Instruction for this Phase**
Submit evidence to architecture and testing tracks for certification approval.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
