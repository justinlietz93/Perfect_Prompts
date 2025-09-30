**Subject: Phase 3: Architecture Track — Multi-Discipline Integration Oversight for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Architecture Phase 3 ensures every implementation track integrates according to the blueprint. The worker agent coordinates cross-track integration checkpoints, validates that in-flight deliverables adhere to architectural guardrails, and updates architectural assets when controlled changes are required.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Architecture remains the single source of truth. Any deviation must be recorded via Architecture Decision Records (ADRs).
* Integration oversight focuses on contracts, data flow, and dependency order—not on authoring feature code.
* Highlight blockers early; downstream tracks must not proceed if architectural prerequisites fail verification.
* Align all actions with `ARCH-INT`, `ARCH-CHANGE`, `QUAL-REV`, and `TEST-SYS` standards.

**3. Mandatory Quality & Finalization Rules**
Maintain the change log for every architectural asset touched. Ensure integration checkpoints include traceability to requirements and risk register updates. Provide red/amber/green status for each track in the integration dashboard.

**4. Directive Section: Architecture Phase 3 Tasks**
* **Input Context:**
    * Phase 1 & 2 outputs.
    * Track-specific Phase 2 build plans (read-only) for frontend, backend, networking, security, testing, UX/UI polish.
    * Standards guide `[relative_path_to_standards]`.

* **Execution Tasks (sequential):**
    - [ ] **Task 3.1: Integration Control Board Kickoff** *(Coordination)*
        - [ ] Schedule integration checkpoints aligned with milestone plan.
        - [ ] Create `integration_dashboard.md` capturing track status, dependencies, and upcoming gates.
    - [ ] **Task 3.2: Contract Verification** *(Compliance)*
        - [ ] Review implementations against interface catalog, flagging mismatches in `integration_findings.md`.
        - [ ] Ensure shared schemas and DTOs remain synchronized across repositories.
    - [ ] **Task 3.3: Dependency Flow Audit** *(Analysis)*
        - [ ] Validate build order adherence; document any out-of-order work and required remediations.
    - [ ] **Task 3.4: Change Management** *(Governance)*
        - [ ] For each requested architectural change, author an ADR with rationale, impact, and approvals.
        - [ ] Update guardrail documents if changes are accepted.
    - [ ] **Task 3.5: Risk & Issue Tracking** *(Risk Management)*
        - [ ] Update risk register with integration-related items and mitigation dates.
    - [ ] **Task 3.6: Broadcast & Alignment** *(Communication)*
        - [ ] Share checkpoint outcomes, action items, and updated deadlines with track leads.
        - [ ] Confirm receipt and agreement from each track lead.

* **Internal Success Criteria:** Integration dashboard reflects real status; contracts verified; ADRs exist for any change; all tracks acknowledge action items.
* **Internal Verification Method:** Conduct a retrospective checklist verifying each track’s compliance status, risk coverage, and acceptance of updates.

**5. Test Reporting Protocol (Internal)**
Record checkpoint results and contract verification findings in `docs/Test_Result_Analysis.md` with references to impacted artifacts.

**6. Final Instruction for this Phase**
Confirm that every track is aligned on integration outcomes and that architecture assets reflect the current state. If major blockers persist, escalate before Phase 4 validation begins.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
