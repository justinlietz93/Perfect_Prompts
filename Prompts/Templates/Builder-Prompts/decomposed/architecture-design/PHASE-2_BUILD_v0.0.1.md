**Subject: Phase 2: Architecture Track — Elaborate Layer Blueprints & Author Implementation Guardrails for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Architecture Phase 2 translates the Phase 1 blueprint into actionable guidance that each implementation lane will consume while starting their own Phase 1 setup. The worker agent must: (a) decompose each layer of the Hybrid-Clean stack into module-level specifications, (b) define interface contracts, quality bars, and acceptance gates, and (c) publish guardrail documents that keep downstream teams aligned with the architecture vision.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Use the canonical Phase 1 outputs as the only source of truth; do not revisit macro decisions unless blockers are discovered.
* Every module spec must reference the requirements matrix IDs and cite relevant standards `[(Rule #X: CODE)](...)`.
* Ensure portability: documentation must be technology-agnostic unless the stack decision is already locked.
* Guardrail documents must be versioned, stored under `architecture-design/outputs/phase-2/`, and flagged as blocking dependencies in the milestone plan.

**3. Mandatory Quality & Finalization Rules**
Apply `ARCH-MOD`, `ARCH-INT`, `QUAL-DOC`, `SEC-PLAN`, and `TEST-ARCH` rules from the standards guide. Provide interface definitions in both prose and structured tables. Every artifact must include a "Downstream Consumers" section listing the tracks and phases that require it.

**4. Directive Section: Architecture Phase 2 Tasks**
* **Input Context:**
    * Phase 1 compendium path: `architecture-design/outputs/phase-1/phase-1_architecture_compendium.md`.
    * Requirements matrix and interface catalog from Phase 1.
    * Standards guide path `[relative_path_to_standards]`.

* **Execution Tasks (sequential):**
    - [ ] **Task 2.1: Layer Module Breakdown** *(Design Detailing)*
        - [ ] For each clean architecture layer, enumerate modules/components and capture responsibilities in `layer_specs/<layer>.md`.
        - [ ] Define data ownership and collaboration boundaries per module.
    - [ ] **Task 2.2: Interface & Contract Authoring** *(Specification)*
        - [ ] Produce protocol-neutral interface definitions, including request/response schemas, error models, and latency expectations.
        - [ ] Link interfaces to the repository/port abstractions expected by backend and frontend tracks.
    - [ ] **Task 2.3: Cross-Layer Guardrails** *(Governance)*
        - [ ] Document anti-patterns to avoid (e.g., direct infrastructure calls from presentation) and enforcement strategy.
        - [ ] Issue dependency inversion guidance summarizing approved interaction pathways.
    - [ ] **Task 2.4: Acceptance Gates** *(Quality Control)*
        - [ ] Define Definition of Ready/Definition of Done checklists tailored to each track.
        - [ ] Establish verification hooks (e.g., architecture review checklists, ADR templates) and link them to tests or documentation deliverables.
    - [ ] **Task 2.5: Risk Register Update** *(Risk Management)*
        - [ ] Capture architectural risks introduced during detailing, mitigation plans, and monitoring triggers.
    - [ ] **Task 2.6: Consolidation & Broadcast** *(Communication)*
        - [ ] Update milestone plan with guardrail publication dates.
        - [ ] Publish summary broadcast in `cross-track-briefs/architecture_phase2_summary.md`.

* **Internal Success Criteria:** All layer specs, interface definitions, guardrail documents, and acceptance gates are published and linked.
* **Internal Verification Method:** Run through each downstream track’s checklist ensuring every dependency referenced in their upcoming Phase 1 prompt has a matching artifact.

**5. Test Reporting Protocol (Internal)**
Log coverage of modules and guardrail sign-offs into `docs/Test_Result_Analysis.md`, capturing tracked risks and mitigation status.

**6. Final Instruction for this Phase**
Announce completion to downstream leads, providing quick links to Phase 2 outputs and calling out any risks requiring their acknowledgement.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
