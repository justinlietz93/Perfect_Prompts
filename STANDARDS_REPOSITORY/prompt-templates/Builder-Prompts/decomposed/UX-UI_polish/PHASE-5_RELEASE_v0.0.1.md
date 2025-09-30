**Subject: Phase 5: UX/UI Polish Focus - Release Readiness, Documentation Finalization, and Transition Planning for [Project Name]**

**Date:** [Customizer: Provide Current Date]
**Time:** [Customizer: Provide Current Time with UTC Offset]

**1. Overall Purpose**
This prompt orchestrates **Phase 5: Release & Transition** for **[Project Name]**. The executing agent must:
    a. Consolidate validated outputs into production-ready deliverables (code, infrastructure definitions, data artifacts).
    b. Finalize all documentation (architecture, operations, user-facing materials) ensuring alignment with the standards and preceding phases.
    c. Prepare deployment packages, release notes, and transition plans for operations/support teams.
    d. Conduct final compliance checks, sign-offs, and knowledge transfer steps to conclude the build initiative.

**2. Core Execution Principles & Global Rules (RELEASE FOCUS)**
*(Customizer Note: Retain structure; substitute bracketed inputs.)*

* **Apex Standards Adherence:** Rigorously enforce all applicable rules from the **Apex Software Compliance Standards Guide** at `[User Input: Path to Standards Guide]`. Every release artifact must include correct `[(Rule #X: CODE)](...)` references.
* **Sequential Closure:** Execute the Phase 5 plan strictly in order, marking `- [x]` only after satisfying `Internal Success Criteria` verified via `Internal Verification Method`.
* **Immutable Evidence:** Preserve immutable evidence of release readiness (reports, approvals, sign-offs) in version-controlled locations.
* **Transition Accountability:** Ensure all operational handoffs include explicit ownership, runbooks, and escalation paths.
* **Autonomous but Auditable:** Operate autonomously while maintaining detailed entries in the internal log per Section 5.

**3. Mandatory Quality & Finalization Rules (Release Emphasis)**
Enforce the **Apex Software Compliance Standards Guide** (`[User Input: Path to Standards Guide]`) with focus on:
* Final Validation & Sign-Off (Section 21: `FINAL-*`, especially `FINAL-SWEEP`, `FINAL-REL`)
* Documentation & Knowledge Transfer (Section 18: `DOC-*`)
* Deployment & Release Management (Section 17: `DEP-*`, `REL-*` if defined)
* Configuration & Secrets Management (Section 12: `CONF-*`, `SEC-SECRET`)
* Security & Compliance (Section 13: `SEC-*`)
* Implementation Correctness & Traceability (Section 19: `IMPL-*`)
* Testing Evidence Preservation (Section 14: `TEST-*`)

**4. Directive Section: Phase 5 - Release & Transition**

* **Context Provided by User (Customizer Inputs):**
    * `[User Input: Project Name]`
    * `[User Input: Phase 4 Validation Summary Path]`
    * `[User Input: Deployment Environment(s) & Access Details]`
    * `[User Input: Path to Standards Guide]`
    * `[User Input: Stakeholder/Operations Contacts]`

* **Instructions for Worker LLM:**

    1.  **Establish Release Scope & Criteria:**
        * Review Phase 4 validation outcomes to confirm readiness.
        * Enumerate release deliverables (code repositories, infrastructure templates, data seeds, documentation).
        * Confirm acceptance criteria, sign-off authorities, and regulatory/compliance obligations.

    2.  **Assemble Release Package:**
        * Produce or update deployment artifacts (manifests, scripts, pipelines) ensuring they match target environment specifications.
        * Generate migration scripts or data snapshots as required.
        * Verify versioning, tagging, and changelog accuracy.

    3.  **Finalize Documentation & Knowledge Transfer:**
        * Update architectural documentation, API references, operations runbooks, support playbooks, and user guides.
        * Document known limitations, feature toggles, and rollback strategies.
        * Prepare training materials or briefing notes for stakeholders.

    4.  **Conduct Release Readiness Review:**
        * Facilitate internal checklist covering tests passed, approvals received, security reviews completed, and rollback validated.
        * Capture sign-offs (digital approvals, recorded decisions) and store in repository.
        * Ensure `docs/Test_Result_Analysis.md` reflects final test status.

    5.  **Transition & Closure Activities:**
        * Outline deployment schedule, responsible parties, communication plan, and escalation paths.
        * Transfer monitoring dashboards, alerting configurations, and credentials per security policies.
        * Archive final artifacts and update backlog with post-release follow-ups.

    6.  **Self-Verification:**
        * Confirm all release deliverables are complete, standards-compliant, version-controlled, and communicated.
        * Validate documentation accuracy and accessibility.
        * Summarize release readiness including outstanding risks or deferred items.

* **Internal Success Criteria:** Release artifacts packaged, documentation finalized, approvals captured, transition plan published, and all standards references satisfied.
* **Internal Verification Method:** Review package contents, verify documentation links, confirm approvals, ensure logs updated, double-check standards compliance for each deliverable.

**5. Test Reporting Protocol (Internal)**
* **Log File Location:** `docs/Test_Result_Analysis.md`
* **Data Points per Entry:** Date/Time, Scope (Release Phase), Activity (e.g., Final Smoke Test, Deployment Dry Run), Result, Metrics/Notes, Approvals Recorded.
* **Update Frequency:** After each release readiness activity, dry run, or sign-off.

**6. Final Instruction**
Execute the release and transition directives sequentially. Upon completion:
    * Provide a comprehensive release package summary (artifacts, versions, locations).
    * Deliver final documentation index and access instructions.
    * Record approvals and transition plans.
    * Present the completed Phase 5 execution plan with all checkboxes marked `- [x]` and declare project handoff readiness.

**7. Contextual Footer**
*(Instructions generated: [Customizer Timestamp]. Location context: [Customizer Location])* 