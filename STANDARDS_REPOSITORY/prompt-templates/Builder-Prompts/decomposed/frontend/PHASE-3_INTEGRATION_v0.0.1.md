**Subject: Phase 3: Frontend Track — Cross-Track Integration & UX Verification for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Phase 3 integrates the frontend modules with backend APIs, security controls, and networking layers defined by other tracks. The worker agent verifies contract adherence, resolves UI-side integration defects, and collaborates on end-to-end flow validation while remaining within the frontend scope.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Respect architecture integration checkpoints documented in `integration_dashboard.md`.
* Frontend adjustments must occur within presentation layer boundaries; backend fixes are escalated rather than implemented here.
* Apply `TEST-E2E`, `ACC-UX`, `SEC-UI`, and `QUAL-INTEG` standards.
* Maintain synchronized mocks and fixtures with backend definitions.

**3. Mandatory Quality & Finalization Rules**
All integration evidence lives in `frontend/outputs/phase-3/`. Capture test runs, screenshots, and issue logs. Any deviations require tickets referencing architecture ADRs.

**4. Directive Section: Frontend Phase 3 Tasks**
* **Input Context:**
    * Backend API endpoints, security flows, networking configs.
    * Architecture integration dashboard and ADRs.
    * Test plans from testing track.

* **Execution Tasks (sequential):**
    - [ ] **Task 3.1: Integration Environment Sync** *(Setup)*
        - [ ] Confirm environment variables, API gateways, and auth providers match expected configuration.
        - [ ] Update frontend `.env` templates documenting required secrets (without storing values).
    - [ ] **Task 3.2: Contract Validation** *(Testing)*
        - [ ] Run contract and schema validation suites ensuring frontend clients respect backend contracts.
        - [ ] Record mismatches and collaborate with backend/security teams for fixes.
    - [ ] **Task 3.3: End-to-End Flow Exercise** *(Verification)*
        - [ ] Execute prioritized user journeys end-to-end, capturing screenshots/videos for UX confirmation.
        - [ ] Document performance observations (initial load, navigation) and compare to budgets.
    - [ ] **Task 3.4: Defect Management** *(Quality)*
        - [ ] Log integration defects in shared tracker, categorize by severity, and track resolution.
        - [ ] Retest resolved issues to confirm closure.
    - [ ] **Task 3.5: Integration Readout** *(Communication)*
        - [ ] Summarize integration status, outstanding issues, and dependency needs in `frontend_integration_report.md`.
        - [ ] Share with architecture, backend, security, and UX leads.

* **Internal Success Criteria:** All critical flows validated, no open blocking defects owned by frontend, documentation and environment instructions updated.
* **Internal Verification Method:** Review integration report, ensure evidence exists, confirm only frontend-side changes performed.

**5. Test Reporting Protocol (Internal)**
Log integration test outcomes and defect stats in `docs/Test_Result_Analysis.md` tagged `FRONT-PH3`.

**6. Final Instruction for this Phase**
Notify stakeholders of integration readiness for formal validation testing. Provide guidance on any conditional workarounds required.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
