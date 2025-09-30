**Subject: Phase 3: Security Track — Cross-Track Security Integration & Verification for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Ensure security controls integrate correctly across frontend, backend, networking, and testing activities. The worker agent validates enforcement points, telemetry, and incident response workflows while remaining within the security domain.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Follow integration dashboard, threat model updates, and risk register.
* Apply standards `SEC-TEST`, `SEC-MON`, `SEC-OPS`, and `PRIVACY-VAL`.
* Collaborate with other tracks but avoid implementing their features.

**3. Mandatory Quality & Finalization Rules**
Store evidence in `security/outputs/phase-3/` including integration test results, audit logs, and remediation plans. Update security checklist and risk register.

**4. Directive Section: Security Phase 3 Tasks**
* **Input Context:**
    * Backend/frontend integration artifacts, networking policies, logging infrastructure.
    * Security tooling dashboards and alerting systems.

* **Execution Tasks (sequential):**
    - [ ] **Task 3.1: Access Control Verification** *(Testing)*
        - [ ] Execute authentication and authorization test suites across user roles.
        - [ ] Validate token issuance, revocation, and session management behaviours.
    - [ ] **Task 3.2: Data Protection Checks** *(Security)*
        - [ ] Confirm encryption-in-transit and at-rest configurations across environments.
        - [ ] Inspect sensitive data handling in logs and storage systems.
    - [ ] **Task 3.3: Telemetry & Alert Validation** *(Observability)*
        - [ ] Ensure security events are emitted, aggregated, and alert thresholds trigger appropriately.
        - [ ] Verify incident response workflows and escalation paths.
    - [ ] **Task 3.4: Vulnerability Management** *(Risk Management)*
        - [ ] Review SAST/DAST/dependency scanning results, track remediation with owning teams.
        - [ ] Update risk register entries with mitigation status.
    - [ ] **Task 3.5: Integration Reporting** *(Communication)*
        - [ ] Produce `security_integration_report.md` summarizing findings, open issues, and required actions for other tracks.
        - [ ] Communicate results to architecture and operations leads.

* **Internal Success Criteria:** Security controls verified across components, critical findings assigned, telemetry functioning.
* **Internal Verification Method:** Review evidence, ensure traceability to threats/controls, confirm no scope creep beyond security tasks.

**5. Test Reporting Protocol (Internal)**
Log integration results in `docs/Test_Result_Analysis.md` tagged `SEC-PH3`.

**6. Final Instruction for this Phase**
Coordinate remediation with owning teams and confirm readiness for validation audits.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
