**Subject: Phase 2: Frontend Track — Implement Presentation Layer Modules for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Execute the frontend build plan produced in Phase 1 by delivering UI components, routing, state management, and accessibility scaffolding. All work must stay within the presentation layer and respect backend interface boundaries defined by architecture.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Work only on frontend code within `<src_root>/presentation/...` as defined by the architecture documents.
* Consume API contracts via typed clients or service interfaces generated per the backend guardrails; never invoke backend implementations directly.
* Enforce `QUAL-FRONTEND`, `UI-STYLE`, `ACC-WCAG`, `TEST-UNIT`, and `TEST-VISUAL` rules.
* Each module must include component documentation, storybook/demo entry (if applicable), and tests meeting coverage targets.

**3. Mandatory Quality & Finalization Rules**
* Place outputs under `frontend/src/` and `frontend/tests/` following architecture naming conventions.
* Update `frontend_delivery_checklist.md` as tasks complete, keeping verification evidence.
* Maintain changelog in `frontend/CHANGELOG.md` for each component release candidate.

**4. Directive Section: Frontend Phase 2 Tasks**
* **Input Context:**
    * Phase 1 frontend plan and architecture guardrails.
    * Mock API responses or schema definitions from backend track.
    * Design assets or UX sign-offs.

* **Execution Tasks (sequential):**
    - [ ] **Task 2.1: Environment Preparation** *(Setup)*
        - [ ] Confirm tooling (package manager, bundler, linting, formatting) matches standards.
        - [ ] Scaffold base app shell aligned with routing/state strategy.
    - [ ] **Task 2.2: Component Implementation** *(Development)*
        - [ ] Implement prioritized UI modules following the plan’s sequence, ensuring atomic commits per module.
        - [ ] Include storybook stories or equivalent previews for each component group.
    - [ ] **Task 2.3: API Integration Layer** *(Integration)*
        - [ ] Generate API clients or hooks using backend interface definitions; include contract tests or mocks verifying schema compliance.
        - [ ] Document fallback behaviour for API latency/failure states.
    - [ ] **Task 2.4: Accessibility & Performance Hardening** *(Quality)*
        - [ ] Run accessibility audits (automated + manual checklists) and record results.
        - [ ] Establish performance budgets (bundle size, render timings) and validate against tooling.
    - [ ] **Task 2.5: Testing & Verification** *(Testing)*
        - [ ] Author unit/component tests hitting coverage thresholds.
        - [ ] Configure visual regression or snapshot suite for critical screens.
    - [ ] **Task 2.6: Documentation Update** *(Documentation)*
        - [ ] Update developer guides for component usage, theming, and integration boundaries.
        - [ ] Note outstanding dependencies or blockers for integration phase.

* **Internal Success Criteria:** All planned modules implemented with tests, documentation updated, checklists satisfied, and no scope bleed beyond frontend.
* **Internal Verification Method:** Review commits and artifacts ensuring only frontend directories touched; cross-check with quality checklist.

**5. Test Reporting Protocol (Internal)**
Capture unit, component, and accessibility test outcomes in `docs/Test_Result_Analysis.md` tagged `FRONT-PH2`.

**6. Final Instruction for this Phase**
Prepare the integration demo package (component library, app shell) and notify backend and UX leads that the frontend is ready for API integration tests.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
