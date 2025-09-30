**Subject: Phase 2: Testing Track — Build Automated & Manual Test Assets for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Create test suites, frameworks, and supporting assets aligned with the Phase 1 strategy. Work focuses on testing deliverables only.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Adhere to test architecture, tooling selections, and quality checklist.
* Apply standards `TEST-AUTO`, `TEST-MAN`, `TEST-DATA`, `DOC-TEST`, and `CI-CD-TEST`.
* Collaborate with other tracks to integrate tests without modifying their feature code.

**3. Mandatory Quality & Finalization Rules**
Store assets under `testing/outputs/phase-2/` (framework code, scripts, data sets, documentation). Ensure maintainability, modularity, and traceability to requirements.

**4. Directive Section: Testing Phase 2 Tasks**
* **Input Context:**
    * Test strategy, environment plan, architecture guardrails, component specifications.

* **Execution Tasks (sequential):**
    - [ ] **Task 2.1: Framework Setup** *(Implementation)*
        - [ ] Configure base automation framework(s) for unit/integration/system tests.
        - [ ] Establish folder structure, coding standards, and reusable utilities.
    - [ ] **Task 2.2: Test Case Development** *(Development)*
        - [ ] Implement automated tests per priority features and NFRs.
        - [ ] Document manual exploratory test charters for complex scenarios.
    - [ ] **Task 2.3: Test Data Management** *(Data)*
        - [ ] Create synthetic data sets, anonymization processes, and refresh scripts.
        - [ ] Ensure data complies with privacy/security requirements.
    - [ ] **Task 2.4: CI/CD Integration** *(Automation)*
        - [ ] Integrate test suites into pipelines with pass/fail gating criteria.
        - [ ] Configure reporting dashboards and coverage metrics.
    - [ ] **Task 2.5: Documentation & Training** *(Documentation)*
        - [ ] Update `testing_runbook.md` with execution steps, maintenance guidelines, and troubleshooting tips.
        - [ ] Provide onboarding material for other tracks to run tests locally.

* **Internal Success Criteria:** Framework operational, priority tests implemented, data strategy in place, CI/CD integration completed.
* **Internal Verification Method:** Review coverage metrics, ensure traceability to requirements, confirm documentation up to date.

**5. Test Reporting Protocol (Internal)**
Log build outcomes and coverage metrics in `docs/Test_Result_Analysis.md` tagged `TEST-PH2`.

**6. Final Instruction for this Phase**
Communicate test suite availability to other tracks and prepare for integration testing in Phase 3.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
