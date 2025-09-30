**Subject: Phase 1: Testing Track — Quality Strategy & Test Architecture Planning for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Testing Phase 1 defines the quality strategy, test architecture, and plans that will guide verification efforts across all tracks. Work is limited to testing governance and planning.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Consume architecture compendium, requirements matrix, and guardrails.
* Apply standards `TEST-STRAT`, `TEST-AUTO`, `TEST-ENV`, `QUAL-METRICS`, and `DOC-TEST`.
* Coordinate with frontend, backend, networking, security, and UX teams to capture dependencies.

**3. Mandatory Quality & Finalization Rules**
Store artifacts in `testing/outputs/phase-1/`, including test strategy document, environment plan, tooling selections, and traceability matrix.

**4. Directive Section: Testing Phase 1 Tasks**
* **Input Context:**
    * Architecture outputs, risk register, NFRs, compliance requirements.

* **Execution Tasks (sequential):**
    - [ ] **Task 1.1: Requirement & Risk Analysis** *(Analysis)*
        - [ ] Map functional and non-functional requirements to test coverage needs.
        - [ ] Prioritize risks influencing testing depth.
    - [ ] **Task 1.2: Test Architecture Definition** *(Design)*
        - [ ] Define test levels (unit, integration, system, performance, security, UX) and responsibilities per track.
        - [ ] Specify tooling frameworks and automation standards.
    - [ ] **Task 1.3: Environment & Data Strategy** *(Planning)*
        - [ ] Plan test environments, data management approach, and refresh cycles.
        - [ ] Document dependencies on networking and security configurations.
    - [ ] **Task 1.4: Traceability & Metrics** *(Quality)*
        - [ ] Build requirements-to-test traceability matrix and quality metric definitions.
        - [ ] Establish thresholds for coverage, defect leakage, and performance.
    - [ ] **Task 1.5: Communication Plan** *(Enablement)*
        - [ ] Produce cross-track testing brief highlighting responsibilities, entry/exit criteria, and reporting cadence.
        - [ ] Create `testing_quality_checklist.md` to enforce standards in future phases.

* **Internal Success Criteria:** Strategy, architecture, environment plan, traceability matrix, and communication plan completed.
* **Internal Verification Method:** Confirm alignment with architecture outputs and ensure artifacts stored correctly.

**5. Test Reporting Protocol (Internal)**
Log planning readiness in `docs/Test_Result_Analysis.md` tagged `TEST-PH1`.

**6. Final Instruction for this Phase**
Share strategy with all track leads, confirming readiness to begin building test assets in Phase 2.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
