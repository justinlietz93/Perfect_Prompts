# Meta-Structure Definition for Autonomous LLM Execution Prompts v1.1.2

**Date:** 2025-04-11
**Time:** 14:52 UTC-5 (CDT)

## 1. Overall Purpose
This document defines a standardized template structure for prompts intended to guide an Large Language Model (LLM) agent (e.g., SE-Apex) in executing complex, multi-step projects autonomously. The structure emphasizes absolute explicitness, sequential task execution, integrated quality checks referencing the **Apex Software Compliance Standards Guide**, scripting of initial project setup, and minimizes ambiguity to ensure reliable completion according to predefined rules and requirements.

## 2. Core Execution Principles & Global Rules
The agent executing a prompt based on this template MUST adhere to the following core principles:

* **Apex Standards Adherence:** Compliance with the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` relative to the project root where the plan file resides) is **MANDATORY** for all steps and deliverables. Specific rules referenced as `[(Rule #X: CODE)](<relative_path_to_standards>#rule-X)` MUST link to the corresponding rule anchor in the standards document using the correct relative path. The Standards Guide takes precedence over potentially conflicting prompt details unless a deviation is explicitly stated and justified within the prompt itself.
* **Strict Sequential Execution:**
    * The prompt defines work hierarchically: **Phase -> Task -> Step**. Each item MUST begin with an unchecked Markdown checkbox (`- [ ]`).
    * Execution MUST proceed sequentially: complete all Steps within a Task before the next Task; complete all Tasks within a Phase before the next Phase.
    * Do NOT proceed to the next item until the current item is fully completed, its `Internal Success Criteria` are met (verified via `Internal Verification Method`), and its checkbox is marked complete (`- [x]`).
* **Test-Driven Development (TDD) Mindset:** **For tasks involving new feature implementation or modification, development MUST follow a TDD approach where feasible: first, create automated test cases that define the desired functionality and initially fail; second, write or modify the minimum amount of production code necessary to make the test cases pass; third, refactor the code while ensuring tests continue to pass. Steps within Task blocks should reflect this order (e.g., a 'Create Test' step preceding a 'Implement Feature' step). Adherence to [(Rule #32: TEST-PLAN-PROC)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-32) and [(Rule #33: TEST-REQ-COVERAGE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-33) is essential.**
* **Internal Success Criteria & Verification:**
    * Each Task defines `Internal Success Criteria` and `Internal Verification Method`.
    * The agent MUST perform the internal verification upon completing the steps for a Task/Phase. Verification MUST include confirming compliance with all `(Rule #X: CODE)` references within the completed Task/Steps.
* **Recursive Error Handling / Retry Logic:**
    * If `Internal Verification` fails (criteria unmet, tests fail, rule violations detected), the agent MUST NOT proceed.
    * It MUST re-execute the failed Step(s)/Task(s), identify and implement corrections, and re-run the `Internal Verification Method` (including rule compliance checks and relevant tests).
    * This cycle repeats until verification succeeds.
* **Autonomous Operation & Reporting:**
    * Execution is fully autonomous unless specified otherwise.
    * Intermediate reporting is DISABLED unless explicitly required.
    * Progress/test results are logged internally per `Test Reporting Protocol`. Checkbox state visually tracks progress.
    * External reporting occurs ONLY upon completion of the entire sequence.

## 3. Mandatory Quality & Finalization Rules (Reference `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`)
Regardless of specific Step instructions, the agent MUST continuously enforce and finally verify adherence to **all** applicable rules within the **Apex Software Compliance Standards Guide** (`./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`), particularly including but not limited to:
* **Code Quality & Structure:** See Section 8 (`QUAL-*` rules).
* **Data Handling & Robustness:** **Rigorous use of development-time assertions per Section 11 (esp. [(Rule #24: DATA-ASSERT-DEV)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-24)).**
* **Configuration Management:** See Section 12 (`CONF-*` rules).
* **Security:** See Section 13 (`SEC-*` rules).
* **Testing & Verification:** See Section 14 (`TEST-*` rules, reinforcing TDD where applicable).
* **Documentation:** See Section 18 (`DOC-*` rules).
* **Implementation Correctness:** See Section 19 (`IMPL-*` rules).
* **Final Validation:** See Section 21 (`FINAL-*` rules), especially `FINAL-SWEEP`.

## 4. Prompt Template Structure (Section by Section)

* **A. Overall Formatting:**
    * Enclose entire prompt in ```markdown ... ```.
    * All Phase, Task, Step items MUST begin with `- [ ]`.

* **B. Subject Line:**
    * Format: `Subject: [CONCISE, ACTION-ORIENTED TITLE]`

* **C. Directive Section:**
    * Establishes context, execution mode, sequential rule, **explicit reference to mandatory adherence to `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`**, TDD mindset reinforcement, reporting constraints, internal logging instructions.

* **D. Test Reporting Protocol (Internal):**
    * Defines standard for internal test log (e.g., `docs/Test_Result_Analysis.md`).
    * Specifies location, data points (Date, Scope, Pass %, Coverage %, Findings), update frequency.

* **E. Hierarchical Execution Blocks:**
    * Core of the prompt, sequential. Uses Markdown headings/lists. Separated by `---`.
    * **Every Phase, Task, Step MUST start with `- [ ]`.**

    * **E.1. Phase Block (`- [ ] **Phase X: Name**`)**
        * Content: High-level `* **Objective:**`. Contains Task Blocks.

    * **E.2. Task Block (`- [ ] **Task X.Y: Name**`)**
        * Content: `* **Task Objective:**`, Step list items (reflecting TDD order where applicable), `Internal Success Criteria`, `Internal Verification Method`, `Task Completion Testing (Internal)`.
        * *(Example incorporating the new setup task, adjust X.Y as needed, typically early in the first Phase):*
        * [ ] **Task 1.1: Generate Project Structure via Script**
            * **Task Objective:** Define and execute a script to create the initial project directory structure and essential blank files based on the established plan.
            * [ ] * **Step 1.1.1 [(Rule #1: PLAN-CHK)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-1), [(Rule #26: CONF-EXT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-26):** **Generate:** Create a shell script (`scripts/01_setup_project_structure.sh`) or appropriate scripting format for the target OS. This script should contain commands to create all necessary top-level and nested directories (e.g., `src/`, `tests/`, `docs/`, `config/`, `scripts/`) as derived from the overall project plan/architecture defined earlier.
            * [ ] * **Step 1.1.2 [(Rule #59: IMPL-PLACE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-59), [(Rule #56: DOC-INT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-56):** **Enhance Script:** Modify the script generated in Step 1.1.1 to also create essential blank starter files within the appropriate directories (e.g., `src/main.js`, `tests/test_main.js`, `README.md`, `docs/architecture.md`, `config/default.json`). For file types that support comments (e.g., `.js`, `.py`, `.md`), the script should inject relevant high-level plan comments (e.g., file purpose, related Phase/Task objective) into the newly created blank files. Skip comment injection for non-commentable file types (e.g., `.json`).
            * [ ] * **Step 1.1.3 [(Rule #26: CONF-EXT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-26):** **Execute:** Run the generated setup script (`scripts/01_setup_project_structure.sh`) to create the directory structure and initial files. Capture any execution errors.
            * **Internal Success Criteria:**
                * The setup script (`scripts/01_setup_project_structure.sh`) is created and contains correct commands for directory and file generation.
                * The script executes successfully without errors.
                * The expected directory structure exists in the workspace.
                * Essential blank files are created in the correct locations (including test files if applicable per TDD).
                * Commentable files contain injected plan-related comments.
                * Compliance with all referenced Apex Standards Rules.
            * **Internal Verification Method:**
                * Review the generated script content for correctness and completeness against the plan.
                * Verify script execution completed successfully (exit code 0) and check for logged errors.
                * List the directory structure and verify it matches the script's intent.
                * Check for the existence of the specified blank files.
                * Inspect the content of several created files to verify comment injection (where applicable).
                * Verify compliance with referenced Apex Standards Rules for this Task and its Steps.
            * **Task Completion Testing (Internal):** N/A (Setup Task). Update internal development log.

    * **E.3. Step (`- [ ] * **Step X.Y.Z [[(Rule #N: CODE)](<relative_path_to_standards>#rule-N), ...]:** Action`)**
        * Content: Begins with explicit **action verb**. Describes single action. **For implementation tasks, steps should ideally follow a TDD sequence (e.g., test creation before implementation).** **MUST** reference all applicable rules from `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` using the linked format `[(Rule #N: CODE)](<relative_path_to_standards>#rule-N)`, where `<relative_path_to_standards>` is the correct relative path from the plan file to the standards file (e.g., `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` if the plan is in the root).
    * **E.3.1. Optional: Sub-Step (`- [ ] * **Sub-Step X.Y.Z.# [[(Rule #N: CODE)](<relative_path_to_standards>#rule-N), ...]:** Action`)**
        * Content: Begins with explicit **action verb**. Describes absolute atomic action. **MUST** reference all applicable rules from `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` using the linked format `[(Rule #N: CODE)](<relative_path_to_standards>#rule-N)`, where `<relative_path_to_standards>` is the correct relative path from the plan file to the standards file (e.g., `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` if the plan is in the root).

    * **E.4. Internal Success Criteria (within Task Block)**
        * Defines measurable conditions for Task completion. MUST implicitly include "Compliance with all referenced and linked Apex Standards Rules".

    * **E.5. Internal Verification Method (within Task Block)**
        * Defines agent actions to check Success Criteria. MUST include "Verify compliance with all referenced and linked Apex Standards Rules for this Task and its Steps".

    * **E.6. Task Completion Testing (Internal - within Task Block)**
        * Instructs agent to run relevant tests (which should exist first per TDD) and update internal test log.

    * **E.7. Phase Completion Testing (Internal - end of Phase Block)**
        * Instructs agent to run cumulative Phase tests, check metrics, update internal test log.

* **F. Final Instruction:**
    * Explicitly commands start of execution, emphasizing sequential processing, checkbox marking, **adherence to the linked `APEX_STANDARDS.md` including TDD mindset and assertion usage**, and final reporting constraint.
    * Final explicit requirements to perform a last sweep over the tasks performed to look for gaps or missed areas.

* **G. Contextual Footer:**
    * Metadata: Timestamp, location. `*(Instructions generated: [YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: Menasha, Wisconsin, United States)*`

## 5. Summary
This enhanced template mandates strict adherence to the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` relative to the plan file) by requiring explicit, linked rule references in steps and verification checks. It emphasizes a **Test-Driven Development (TDD) mindset** and **rigorous use of development-time assertions** as core execution principles. It includes an early task for scripting the project structure generation. It enforces sequential, verifiable, and high-quality autonomous execution.

*(Meta-structure v1.1.2 explanation updated 2025-04-11)*
