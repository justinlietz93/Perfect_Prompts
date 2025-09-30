**Subject: Phase 1: Frontend Track — Context Intake & UI Architecture Planning for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
This phase prepares the frontend track to begin implementation by internalizing the architecture outputs, defining UI scope, and producing the roadmap for presentation layer delivery. The worker agent must focus exclusively on frontend responsibilities and avoid backend, infrastructure, or security implementation.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Architecture-design outputs are authoritative; reference `architecture-design/outputs/phase-1/phase-1_architecture_compendium.md` and `cross-track-briefs/frontend.md`.
* Align all plans with Hybrid-Clean Architecture by keeping frontend in the presentation layer and interacting only through approved ports.
* Use standards `UI-QUAL`, `UX-GUIDE`, `ACC-STD`, `DOC-UI`, and `TEST-UI` in the Apex guide.
* Scope guard: produce plans, design assets, and dependencies solely for the frontend.

**3. Mandatory Quality & Finalization Rules**
Create artifacts under `frontend/outputs/phase-1/`. Each must cite relevant standards, list dependencies on backend/security/networking deliverables, and include acceptance criteria.

**4. Directive Section: Frontend Phase 1 Tasks**
* **Input Context:**
    * Architecture compendium and guardrails.
    * UX research, brand guidelines, and accessibility mandates (if provided).
    * Standards guide `[relative_path_to_standards]`.

* **Execution Tasks (sequential):**
    - [ ] **Task 1.1: Context Assimilation** *(Setup)*
        - [ ] Summarize user roles, UI flows, and interface contracts relevant to the frontend.
        - [ ] Record dependencies on backend APIs and security requirements.
    - [ ] **Task 1.2: Presentation Layer Blueprint** *(Design)*
        - [ ] Define the frontend application structure (routing map, state management strategy, component hierarchy) within `frontend_architecture.md`.
        - [ ] Confirm alignment with architecture guardrails (no direct infrastructure access).
    - [ ] **Task 1.3: Experience Planning** *(UX Coordination)*
        - [ ] Map prioritized user journeys into storyboard or wireframe references.
        - [ ] Capture accessibility and localization requirements per journey.
    - [ ] **Task 1.4: Delivery Plan & Dependencies** *(Planning)*
        - [ ] Create a Phase -> Task -> Step execution plan enumerating UI modules, shared component libraries, and integration points.
        - [ ] Note prerequisites from backend/networking/security that must exist before each UI module starts.
    - [ ] **Task 1.5: Verification Checklist** *(Quality)*
        - [ ] Build a checklist covering coding standards, linting, testing, accessibility, and performance budgets to be enforced during Phase 2.
        - [ ] Store as `frontend_delivery_checklist.md`.

* **Internal Success Criteria:** Frontend blueprint, execution plan, and quality checklist completed with dependencies identified.
* **Internal Verification Method:** Review architecture alignment, ensure no backend tasks included, verify deliverables stored correctly.

**5. Test Reporting Protocol (Internal)**
Log Phase 1 readiness confirmation in `docs/Test_Result_Analysis.md` noting outstanding dependencies.

**6. Final Instruction for this Phase**
Present the frontend plan to architecture and UX leads for confirmation before commencing Phase 2 build work.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
