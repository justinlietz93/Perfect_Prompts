**Subject: Phase 1: Security Track — Threat Modeling & Control Strategy for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Security Phase 1 establishes the threat model, security requirements, and control roadmap that guide all other tracks. Work focuses strictly on security governance and planning, not on building application features.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Reference architecture compendium, risk register, and guardrails from architecture track.
* Apply standards `SEC-REQ`, `SEC-THREAT`, `SEC-CONTROL`, `PRIVACY`, and `COMPLIANCE`.
* Ensure alignment with regulatory frameworks relevant to the project.

**3. Mandatory Quality & Finalization Rules**
Store outputs in `security/outputs/phase-1/`. Deliverables include threat model, control matrix, security requirements traceability, and cross-track briefs.

**4. Directive Section: Security Phase 1 Tasks**
* **Input Context:**
    * Architecture outputs, NFRs, compliance mandates.
    * Existing corporate security policies.

* **Execution Tasks (sequential):**
    - [ ] **Task 1.1: Context Review** *(Analysis)*
        - [ ] Summarize assets, data classifications, and trust boundaries from architecture documents.
        - [ ] Identify stakeholders and escalation paths.
    - [ ] **Task 1.2: Threat Modeling** *(Design)*
        - [ ] Build STRIDE (or equivalent) threat model covering each component and interaction.
        - [ ] Rate risks and map mitigations to standards.
    - [ ] **Task 1.3: Security Requirement Definition** *(Planning)*
        - [ ] Document security requirements per component, mapped to requirement IDs and controls.
        - [ ] Specify authentication, authorization, encryption, auditing, and privacy needs.
    - [ ] **Task 1.4: Control Strategy & Roadmap** *(Enablement)*
        - [ ] Create control matrix linking threats to preventive/detective controls and owning tracks.
        - [ ] Sequence security deliverables across phases and note dependencies on other tracks.
    - [ ] **Task 1.5: Communication Package** *(Communication)*
        - [ ] Produce briefs for frontend, backend, networking, testing, and UX tracks describing required security integrations.
        - [ ] Establish verification checklists for later phases and store as `security_quality_checklist.md`.

* **Internal Success Criteria:** Threat model, requirements, control matrix, and briefs completed with traceability to standards.
* **Internal Verification Method:** Validate coverage across components, confirm deliverables stored, ensure no non-security tasks included.

**5. Test Reporting Protocol (Internal)**
Log planning readiness and key risks in `docs/Test_Result_Analysis.md` tagged `SEC-PH1`.

**6. Final Instruction for this Phase**
Share security strategy with architecture and implementation leads before proceeding to control implementation.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
