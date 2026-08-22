**Subject: Phase 2: Security Track — Implement Preventive & Detective Controls for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Deploy security controls identified in Phase 1, ensuring application teams can integrate authentication, authorization, encryption, and monitoring capabilities. Work is confined to security tooling, policies, and shared libraries; no application features are implemented here.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Follow threat model, control matrix, and quality checklist.
* Apply standards `SEC-AUTH`, `SEC-AUTHZ`, `SEC-CRYPTO`, `SEC-LOG`, `SEC-DEV`.
* Coordinate with backend/frontend/networking to ensure interfaces align with architecture.

**3. Mandatory Quality & Finalization Rules**
Place deliverables in `security/outputs/phase-2/`, including configuration templates, infrastructure policies, shared libraries, and documentation. All changes must be testable and version-controlled.

**4. Directive Section: Security Phase 2 Tasks**
* **Input Context:**
    * Control matrix, architecture guardrails, identity provider capabilities.
    * Compliance requirements for logging/auditing.

* **Execution Tasks (sequential):**
    - [ ] **Task 2.1: Identity & Access Foundations** *(Implementation)*
        - [ ] Configure identity provider/SSO integration, client registrations, and token lifetimes per requirements.
        - [ ] Publish configuration guides and secrets management expectations (no secrets in repo).
    - [ ] **Task 2.2: Authorization Framework** *(Implementation)*
        - [ ] Provide role/permission models, policy definitions, and middleware packages for backend/frontend consumption.
        - [ ] Document enforcement points and integration steps.
    - [ ] **Task 2.3: Data Protection Controls** *(Security)*
        - [ ] Define encryption standards (in transit, at rest) and deliver key management configurations.
        - [ ] Supply data classification handling guidelines for each component.
    - [ ] **Task 2.4: Security Logging & Monitoring** *(Observability)*
        - [ ] Implement centralized logging schemas, event taxonomy, and alerting rules for security events.
        - [ ] Provide integration instructions for other tracks to emit security telemetry.
    - [ ] **Task 2.5: Secure Development Tooling** *(Enablement)*
        - [ ] Configure SAST/DAST tools, dependency scanning, and secret scanning pipelines.
        - [ ] Document usage requirements and thresholds for build pipelines.
    - [ ] **Task 2.6: Documentation & Support** *(Documentation)*
        - [ ] Update `security_runbook.md` with setup steps, integration instructions, and support contacts.
        - [ ] Record outstanding dependencies for integration phase.

* **Internal Success Criteria:** Controls deployed/configured, documentation provided, integration points ready for other tracks.
* **Internal Verification Method:** Validate each control against threat model; ensure deliverables stored and versioned.

**5. Test Reporting Protocol (Internal)**
Log control deployment validation in `docs/Test_Result_Analysis.md` tagged `SEC-PH2`.

**6. Final Instruction for this Phase**
Notify other tracks that security controls are ready for integration, providing necessary credentials or onboarding steps.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
