**Subject: Phase 1: Backend Track — Domain & Service Planning for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
This phase equips the backend track with the architecture context, domain understanding, and implementation roadmap required to build server-side capabilities. All activities stay within backend scope (business logic, domain, infrastructure abstractions) and exclude frontend or networking implementation.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Use architecture outputs: `architecture-design/outputs/phase-1/phase-1_architecture_compendium.md`, `layer_specs/business-logic.md`, and backend guardrail briefs.
* Honour Hybrid-Clean Architecture: presentation layer never invoked directly; backend interacts via ports and adapters only.
* Standards focus: `ARCH-BL`, `DOMAIN-MODEL`, `REPO-PATTERN`, `TEST-BACK`, `SEC-API`.
* Document dependencies on database, security, and networking tracks.

**3. Mandatory Quality & Finalization Rules**
Store planning artifacts in `backend/outputs/phase-1/`. Include domain glossary, service catalog, and build plan referencing requirement IDs.

**4. Directive Section: Backend Phase 1 Tasks**
* **Input Context:**
    * Architecture compendium, module specs, interface catalog.
    * Business requirements and NFRs affecting backend (scalability, consistency, latency).

* **Execution Tasks (sequential):**
    - [ ] **Task 1.1: Domain Understanding** *(Analysis)*
        - [ ] Create domain glossary and context map aligning bounded contexts with architecture layers.
        - [ ] Identify aggregate roots, invariants, and transactional boundaries.
    - [ ] **Task 1.2: Service & API Planning** *(Design)*
        - [ ] Draft service catalog detailing responsibilities, exposed endpoints, and consumer tracks.
        - [ ] Outline API style (REST/gRPC/etc.) referencing architecture directives.
    - [ ] **Task 1.3: Data & Persistence Strategy** *(Design)*
        - [ ] Map entities to data stores, define repository abstractions, and note consistency requirements.
        - [ ] Capture data privacy/compliance constraints from security track.
    - [ ] **Task 1.4: Technical Plan** *(Planning)*
        - [ ] Produce Phase -> Task -> Step plan covering business logic, domain models, repository adapters, and test harnesses.
        - [ ] Record required inputs from networking (service mesh, DNS) and security (auth providers).
    - [ ] **Task 1.5: Quality Gates** *(Quality)*
        - [ ] Establish coding standards, lint/test tooling, and observability requirements for backend modules.
        - [ ] Store as `backend_quality_checklist.md`.

* **Internal Success Criteria:** Domain map, service catalog, data strategy, and execution plan complete with dependencies noted.
* **Internal Verification Method:** Ensure outputs align with architecture guardrails, cite standards, and remain backend-specific.

**5. Test Reporting Protocol (Internal)**
Record planning readiness and open dependencies in `docs/Test_Result_Analysis.md` tagged `BACK-PH1`.

**6. Final Instruction for this Phase**
Review plan with architecture and security leads, confirm readiness to commence backend implementation in Phase 2.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
