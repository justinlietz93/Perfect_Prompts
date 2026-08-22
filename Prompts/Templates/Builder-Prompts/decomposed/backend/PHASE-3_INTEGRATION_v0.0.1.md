**Subject: Phase 3: Backend Track — Cross-Component Integration & Contract Verification for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Phase 3 integrates backend services with external systems (frontend, networking, security, data stores) and validates adherence to defined contracts. The worker agent ensures APIs, messaging, and persistence interactions behave as designed without implementing non-backend features.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Follow architecture integration dashboard scheduling and ADR decisions.
* Use `TEST-CONTRACT`, `TEST-E2E-BACK`, `SEC-API`, and `DATA-CONSIST` standards.
* Changes limited to backend modules; escalate issues owned by other tracks.

**3. Mandatory Quality & Finalization Rules**
Capture integration artifacts in `backend/outputs/phase-3/`, including test logs, schema validation results, and issue registers. Ensure data migration scripts are versioned and reversible.

**4. Directive Section: Backend Phase 3 Tasks**
* **Input Context:**
    * Frontend contract tests, networking deployment topology, security auth flows.
    * Integration dashboard and risk register.

* **Execution Tasks (sequential):**
    - [ ] **Task 3.1: Environment Alignment** *(Setup)*
        - [ ] Verify configuration for databases, message brokers, and external services matches architecture assumptions.
        - [ ] Document environment variables/secrets required (without storing values) in `backend_env_requirements.md`.
    - [ ] **Task 3.2: API Contract Verification** *(Testing)*
        - [ ] Run automated contract tests against each endpoint, validating schemas, status codes, and error handling.
        - [ ] Log discrepancies and collaborate with consuming tracks on remediation.
    - [ ] **Task 3.3: Data Integration Testing** *(Data)*
        - [ ] Execute integration tests covering persistence operations, migrations, and transactional integrity.
        - [ ] Validate data seeding scripts and rollback procedures.
    - [ ] **Task 3.4: Cross-Service Orchestration** *(Verification)*
        - [ ] Test orchestrated workflows across backend modules (e.g., saga flows, event-driven pipelines).
        - [ ] Monitor logs/metrics ensuring observability instrumentation meets expectations.
    - [ ] **Task 3.5: Issue Tracking & Reporting** *(Communication)*
        - [ ] Maintain `backend_integration_report.md` summarizing status, defects, and dependencies.
        - [ ] Provide updates to architecture, networking, and security leads.

* **Internal Success Criteria:** Integration tests passing, critical defects resolved or assigned, environment requirements documented.
* **Internal Verification Method:** Review report, confirm evidence stored, ensure no scope creep beyond backend.

**5. Test Reporting Protocol (Internal)**
Update `docs/Test_Result_Analysis.md` with integration test results tagged `BACK-PH3`.

**6. Final Instruction for this Phase**
Signal readiness for validation testing and coordinate any outstanding cross-track fixes.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
