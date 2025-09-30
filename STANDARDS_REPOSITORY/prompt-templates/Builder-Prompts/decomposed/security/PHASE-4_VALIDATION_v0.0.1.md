**Subject: Phase 4: Security Track — Security Validation & Compliance Assurance for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Conduct formal security validation to confirm requirements, controls, and remediation actions are satisfied. Produce evidence for architecture certification and regulatory audits.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Apply standards `SEC-VAL`, `PEN-TEST`, `PRIVACY-AUDIT`, `COMP-REPORT`, and `SEC-OPS`.
* Use production-equivalent environments and finalized configurations.
* Track findings with severity levels and remediation owners.

**3. Mandatory Quality & Finalization Rules**
Store validation artifacts in `security/outputs/phase-4/`, including penetration test reports, compliance checklists, privacy assessments, and residual risk statements.

**4. Directive Section: Security Phase 4 Tasks**
* **Input Context:**
    * Threat model, integration findings, risk register, validation plans from testing/architecture.

* **Execution Tasks (sequential):**
    - [ ] **Task 4.1: Validation Plan Confirmation** *(Planning)*
        - [ ] Align on test scope, tools, and success criteria with stakeholders.
        - [ ] Document plan in `security_validation_plan.md`.
    - [ ] **Task 4.2: Penetration & Vulnerability Testing** *(Testing)*
        - [ ] Execute penetration tests (internal/external) and advanced vulnerability scans.
        - [ ] Document findings with reproduction steps and severity ratings.
    - [ ] **Task 4.3: Compliance & Privacy Review** *(Compliance)*
        - [ ] Verify adherence to regulatory standards (e.g., GDPR, HIPAA) and corporate policies.
        - [ ] Confirm data retention, consent management, and audit logging meet requirements.
    - [ ] **Task 4.4: Risk Closure** *(Risk Management)*
        - [ ] Update risk register, mark mitigated/accepted items, and document residual risks.
        - [ ] Prepare waiver requests for any deferred fixes.
    - [ ] **Task 4.5: Evidence Package Assembly** *(Documentation)*
        - [ ] Compile `security_validation_report.md` summarizing activities, findings, remediation status, and sign-offs.

* **Internal Success Criteria:** Validation completed, evidence recorded, critical findings closed or waived with approvals.
* **Internal Verification Method:** Ensure every requirement/control has validation evidence; confirm documentation stored correctly.

**5. Test Reporting Protocol (Internal)**
Update `docs/Test_Result_Analysis.md` with validation results tagged `SEC-PH4`.

**6. Final Instruction for this Phase**
Provide security validation report to architecture and compliance stakeholders for release certification.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
