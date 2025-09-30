**Subject: Phase 4: Architecture Track — System Validation & Compliance Certification for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Phase 4 confirms that the implemented solution aligns with the sanctioned architecture. The worker agent executes architecture-focused validation, cross-checking implemented artifacts, test evidence, and documentation. The outcome is a certification package gating release readiness.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Validate against requirements, interface contracts, and guardrails established in Phases 1–3.
* Utilize `ARCH-VAL`, `QUAL-AUD`, `TEST-SYS`, and `SEC-ARCH` standards for inspection depth.
* Record objective evidence only; subjective assessments must be backed by traceable data (tests, metrics, screenshots).

**3. Mandatory Quality & Finalization Rules**
Maintain audit trails for every validation checklist. Any non-conformance must include remediation ownership and due dates. Certification cannot proceed until high-severity issues are resolved or formally waived by stakeholders.

**4. Directive Section: Architecture Phase 4 Tasks**
* **Input Context:**
    * Implementation artifacts from all tracks.
    * Integration dashboard and risk register from Phase 3.
    * Standards guide `[relative_path_to_standards]` and guardrail documents.

* **Execution Tasks (sequential):**
    - [ ] **Task 4.1: Validation Plan Setup** *(Planning)*
        - [ ] Assemble validation scope matrix linking requirements to implemented components and test suites.
        - [ ] Confirm availability of evidence repositories (CI logs, test reports, documentation).
    - [ ] **Task 4.2: Architecture Conformance Audit** *(Inspection)*
        - [ ] Review implementation snapshots, ensuring layering rules and dependency inversions remain intact.
        - [ ] Document findings in `validation_reports/architecture_conformance.md` with pass/fail per component.
    - [ ] **Task 4.3: Cross-Track Evidence Review** *(Verification)*
        - [ ] Validate that each track provides evidence fulfilling Definition of Done/Ready criteria authored in Phase 2.
        - [ ] Capture gaps, assign owners, and schedule remediation windows.
    - [ ] **Task 4.4: Risk Closure & Waivers** *(Governance)*
        - [ ] Reconcile risk register entries; mark mitigated, accepted, or residual.
        - [ ] Draft waiver requests for unresolved risks requiring executive approval.
    - [ ] **Task 4.5: Certification Packet Assembly** *(Output)*
        - [ ] Compile the `architecture_validation_certificate_v0.0.1.md` summarizing compliance status, open issues, and waiver list.
        - [ ] Obtain sign-off from architecture lead and key track owners.

* **Internal Success Criteria:** Validation packet complete, all high severity issues resolved or waived, and certification signed.
* **Internal Verification Method:** Run final audit checklist ensuring each requirement, interface, and guardrail has validation evidence.

**5. Test Reporting Protocol (Internal)**
Log validation outcomes and evidence references in `docs/Test_Result_Analysis.md`, tagging each entry with `ARCH-PH4`.

**6. Final Instruction for this Phase**
Publish the certification packet and distribute remediation assignments for remaining medium/low issues. Block release until sign-offs recorded.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
