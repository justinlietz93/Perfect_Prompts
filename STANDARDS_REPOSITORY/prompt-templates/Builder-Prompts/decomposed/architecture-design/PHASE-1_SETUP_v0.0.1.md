**Subject: Phase 1: Enterprise Architecture Discovery and System Blueprint Planning for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
Initiate **Phase 1: Architecture Discovery & Blueprint Planning** for **[Project Name]**. The architecting agent must:
    a. Internalize Apex Standards and Hybrid-Clean Architecture mandates for the entire solution stack.
    b. Analyze business capabilities, value streams, and constraints to frame architectural drivers.
    c. Define target architecture vision (logical, physical, deployment views) and trace to requirements.
    d. Plan strategic increments, dependencies, and governance checkpoints for downstream phases.

**2. Core Execution Principles & Global Rules**
* Enforce Apex Standards Guide (`[Specify relative path]`) referencing `[(Rule #X: CODE)](...)`.
* Respect Hybrid-Clean Architecture layering and dependency rule across all proposed structures.
* Ensure no file >500 LOC; plan modularization accordingly.
* Execute tasks sequentially and verify outputs before marking complete.
* Log significant decisions per Section 5.

**3. Mandatory Quality & Finalization Rules**
Apply relevant standards continuously:
* Architecture Standards (`ARCH-*`, `QUAL-ARCH`).
* Security & Compliance (`SEC-*`).
* Data Governance (`DATA-*`).
* Documentation (`DOC-*`, architecture decision records, diagrams).
* Planning & Governance (`PLAN-*`, `FINAL-*`).

**4. Directive Section: Phase 1 - Architecture Blueprint Planning**

* **Input Context:**
    * Business goals, strategic outcomes, KPIs.
    * Functional requirements, domain models, capability maps.
    * Non-functional requirements (performance, scalability, availability, compliance, sustainability).
    * Technology constraints (approved stacks, cloud providers, licensing, AMD hardware compatibility).

* **Execution Tasks:**
    -   [ ] **Task 1.1: Standards & Context Confirmation**
        -   [ ] * **Step 1.1.1 [(Rule #? : INIT-CONF)](...):** Confirm understanding of standards, dependency rule, repository mandate, DI strategy.
        -   [ ] * **Step 1.1.2 [(Rule #? : INPUT-VAL)](...):** Validate access to inputs (requirements, domain maps, policies).

    -   [ ] **Task 1.2: Driver & Constraint Analysis**
        -   [ ] * **Step 1.2.1:** Identify business drivers, stakeholder priorities, regulatory constraints.
        -   [ ] * **Step 1.2.2:** Analyze NFR implications on architecture choices.
        -   [ ] * **Step 1.2.3:** Evaluate technology constraints/opportunities (cloud, data platforms, integration patterns).
        -   [ ] * **Step 1.2.4 [(Rule #? : ARCH-DRIVE)](...):** Prioritize top drivers guiding architectural decisions.

    -   [ ] **Task 1.3: Target Architecture Definition**
        -   [ ] * **Step 1.3.1 [(Rule #? : ARCH-PAT)](...):** Assess macro patterns (modular monolith, event-driven, data mesh) and select primary approach.
        -   [ ] * **Step 1.3.2:** Produce logical component model (layers, modules, boundaries) aligned to dependency rule.
        -   [ ] * **Step 1.3.3 [(Rule #? : ARCH-INT)](...):** Map integrations, contracts, and data flows (sequence/context diagrams).
        -   [ ] * **Step 1.3.4 [(Rule #? : ARCH-DEP)](...):** Document dependency matrix and enforce interface boundaries.
        -   [ ] * **Step 1.3.5:** Outline deployment topology (environments, zones, scaling strategies).

    -   [ ] **Task 1.4: Governance & Roadmap Planning**
        -   [ ] * **Step 1.4.1 [(Rule #? : PLAN-SEQ)](...):** Define phased roadmap aligning to dependencies and value delivery.
        -   [ ] * **Step 1.4.2 [(Rule #? : PLAN-JUST)](...):** Justify sequencing with driver alignment and risk mitigation.
        -   [ ] * **Step 1.4.3 [(Rule #? : PLAN-GOV)](...):** Establish governance checkpoints, decision forums, compliance checks.
        -   [ ] * **Step 1.4.4 [(Rule #? : DOC-ADR)](...):** Plan architecture decision record cadence and repository structure.

    -   [ ] **Task 1.5: Risk & Mitigation Strategy**
        -   [ ] * **Step 1.5.1 [(Rule #? : RISK-ID)](...):** Identify architectural risks, technical debt, external dependencies.
        -   [ ] * **Step 1.5.2 [(Rule #? : RISK-MIT)](...):** Define mitigation strategies, experiment spikes, and contingency plans.
        -   [ ] * **Step 1.5.3:** Align monitoring/feedback loops to track risk indicators.

    -   [ ] **Task 1.6: Consolidation & Verification**
        -   [ ] * **Step 1.6.1:** Compile architecture blueprint (diagrams, matrices, roadmap) into single deliverable.
        -   [ ] * **Step 1.6.2 [(Rule #? : PLAN-VER)](...):** Verify outputs against drivers, standards, and dependency rule.

* **Internal Success Criteria:** Tasks 1.1-1.6 complete; drivers traced to decisions; roadmap and governance plan established; blueprint validated.
* **Internal Verification Method:** Execute Step 1.6.2, cross-check decisions vs standards, confirm diagrams reflect dependency rule.

**5. Test Reporting Protocol**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Scope (Architecture decision/diagram), Validation Activity, Status, Notes.
* **Update Frequency:** After major analysis milestones or decision validations.

**6. Final Instruction**
Produce the architecture blueprint and roadmap, submit for review before moving to downstream component build phases.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
