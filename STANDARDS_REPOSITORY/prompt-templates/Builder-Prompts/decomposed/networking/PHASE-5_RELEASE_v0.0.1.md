**Subject: Phase 5: Networking Track — Release Readiness & Operations Handoff for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Finalize networking deliverables for production launch, ensuring operations teams have runbooks, monitoring, and escalation paths. The worker agent confines work to networking assets.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Follow `REL-NET`, `OPS-NET`, `DOC-RUNBOOK`, `SEC-OPS`, and `DR-OPS` standards.
* Leverage validation evidence and architecture governance playbook.
* Maintain IaC as the source of truth; manual changes require documented justifications.

**3. Mandatory Quality & Finalization Rules**
Outputs stored in `networking/outputs/phase-5/`. Provide release notes, change windows, rollback plans, and contact matrix for network operations.

**4. Directive Section: Networking Phase 5 Tasks**
* **Input Context:**
    * Networking validation report, architecture governance playbook, release schedule.
    * Operations requirements for monitoring, alerting, and capacity planning.

* **Execution Tasks (sequential):**
    - [ ] **Task 5.1: Deployment Package Finalization** *(Packaging)*
        - [ ] Tag IaC modules for release and export change manifests.
        - [ ] Provide configuration snapshots for audit and rollback.
    - [ ] **Task 5.2: Runbook Completion** *(Enablement)*
        - [ ] Update `networking_runbook.md` with deployment steps, incident response, and maintenance tasks.
        - [ ] Include diagrams referencing failover paths and escalation procedures.
    - [ ] **Task 5.3: Monitoring & Alerting Setup** *(Operations)*
        - [ ] Verify monitoring dashboards, alerts, and log pipelines align with SLOs.
        - [ ] Document alert routing and on-call expectations.
    - [ ] **Task 5.4: Handoff & Training** *(Communication)*
        - [ ] Conduct knowledge transfer session with operations/security teams; capture minutes and open actions.
        - [ ] Distribute release notes detailing network changes and dependencies on other tracks.
    - [ ] **Task 5.5: Final Approvals & Archiving** *(Governance)*
        - [ ] Obtain sign-offs from architecture, security, and operations leads.
        - [ ] Archive IaC state files, diagrams, and runbooks with version metadata.

* **Internal Success Criteria:** IaC tagged, runbooks complete, monitoring verified, approvals recorded.
* **Internal Verification Method:** Cross-check deliverables against governance checklist; ensure artifacts accessible to operations.

**5. Test Reporting Protocol (Internal)**
Log release readiness confirmation in `docs/Test_Result_Analysis.md` tagged `NET-PH5`.

**6. Final Instruction for this Phase**
Transfer ownership to network operations and support go-live decision making.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
