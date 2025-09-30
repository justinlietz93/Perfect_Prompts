**Subject: Phase 1: Architecture Track — Establish System Blueprint & Cross-Discipline Briefing for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Phase 1 for the architecture track creates the canonical system vision that every other implementation lane (frontend, backend, networking, security, testing, UX/UI polish) must consume. The worker agent must:
    a. Reconcile business goals, functional requirements, and non-functional drivers into explicit architectural objectives.
    b. Select and justify structural patterns compatible with the Hybrid-Clean Architecture system card.
    c. Produce a standards-linked blueprint plus hand-off packets that downstream tracks will reference verbatim.
    d. Publish the authoritative dependency graph, interface contract catalog, and sequencing notes consumed by later phases.

**2. Core Execution Principles & Global Rules (MANDATORY)**
The worker must honour all corporate standards, with emphasis on:
* **Architecture Rule of Precedence:** `[(Rule #01: ARCH-PRIME)](<path_to_standards>#arch-prime)` — architecture outputs drive the other tracks.
* **Hybrid-Clean Architecture Compliance:** Preserve layer boundaries and dependency inversion in all diagrams and narratives.
* **Traceability:** Every design decision must trace back to a requirement identifier.
* **Sequenced Deliverables:** Downstream prompts rely on clearly enumerated artifacts. Missing artifacts block subsequent phases.
* **Autonomous Validation:** Before finishing, re-read outputs to ensure completeness and alignment with the Apex Standards Guide at `[relative_path_to_standards]`.

**3. Mandatory Quality & Finalization Rules**
Enforce all quality gates defined in the standards guide, including `QUAL-*`, `ARCH-*`, `SEC-*`, `DATA-*`, `DOC-*`, and `PLAN-*`. If the system card introduces tighter constraints, explicitly cite them. No artifact can remain in draft state; each deliverable must carry version v0.0.1 and a change log stub.

**4. Directive Section: Architecture Phase 1 Tasks**
* **Input Context:**
    * Project goal, requirements, constraints, and stakeholder roster supplied by the user.
    * Standards location: `[relative_path_to_standards]`.
    * Deliverable directory: `architecture-design/outputs/phase-1/`.

* **Execution Tasks (sequential):**
    - [ ] **Task 1.1: Requirements Normalization** *(Setup/Meta)*
        - [ ] Aggregate all functional & non-functional inputs into the `01_requirements_matrix.md` template.
        - [ ] Flag ambiguities, conflicts, or missing data and request clarification channels.
    - [ ] **Task 1.2: Architectural Driver Synthesis** *(Analysis)*
        - [ ] Rank top architectural drivers (max 7) and justify each with requirement IDs and NFR metrics.
        - [ ] Map each driver to the Hybrid-Clean layer(s) it influences.
    - [ ] **Task 1.3: System Topology Definition** *(Design)*
        - [ ] Evaluate at least two macro-architecture patterns (e.g., modular monolith vs. service-segmented monolith) against the drivers.
        - [ ] Select the winning pattern, document rationale, and illustrate the layered topology using Mermaid.
    - [ ] **Task 1.4: Component & Interface Ledger** *(Design)*
        - [ ] Enumerate all core components per layer, specifying responsibilities, inbound/outbound ports, and owning teams.
        - [ ] Produce the `interfaces_catalog.csv` capturing interface IDs, protocol, payload schema refs, and dependency direction.
    - [ ] **Task 1.5: Cross-Track Enablement Packet** *(Enablement)*
        - [ ] Draft targeted briefs for each track summarizing expectations, dependencies, and mandatory inputs they must read before Phase 1 in their lane. Store in `cross-track-briefs/`.
        - [ ] Define configuration baseline, shared terminology, and artifact naming conventions.
    - [ ] **Task 1.6: Build Sequencing & Milestones** *(Planning)*
        - [ ] Create the architecture-first milestone plan identifying readiness gates for downstream tracks.
        - [ ] Document gating criteria for hand-offs (e.g., frontend cannot start Phase 2 until UI contract doc `UX-FRONT-001` is signed-off).
    - [ ] **Task 1.7: Consolidation & Verification** *(QA)*
        - [ ] Compile the `phase-1_architecture_compendium.md` summarizing all outputs with hyperlinks.
        - [ ] Run standards compliance checklist, confirm deliverables exist, and log verification in `docs/Test_Result_Analysis.md`.

* **Internal Success Criteria:** All artifacts listed in Tasks 1.1–1.7 exist, are cross-referenced, and carry explicit standard citations.
* **Internal Verification Method:** Perform a final walkthrough referencing the standards checklist, driver alignment table, and dependency graph. Any unresolved gap blocks completion.

**5. Test Reporting Protocol (Internal)**
* Log location: `docs/Test_Result_Analysis.md` (project root).
* Entry format: Date/Time, Architecture Phase Step, Artifact Name, Compliance Result, Outstanding Risks.
* Update cadence: After Task 1.7 completion.

**6. Final Instruction for this Phase**
Deliver the consolidated architecture package and notify downstream track leads that Phase 1 outputs are ready. Await acknowledgement before triggering other track prompts.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
