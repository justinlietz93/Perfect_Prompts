# Meta-Structure Definition for Autonomous LLM Execution Prompts v1.2.1 (Unified - Initial Sweep)

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM UTC+/-Offset]

## 1. Overall Purpose
This document defines a standardized template structure for prompts intended to guide an Large Language Model (LLM) agent (e.g., SE-Apex) in executing complex, multi-step projects autonomously. The structure emphasizes absolute explicitness, sequential task execution including a **mandatory initial codebase exploration**, integrated quality checks referencing the **Apex Software Compliance Standards Guide**, scripting of initial project setup, and minimizes ambiguity to ensure reliable completion according to predefined rules and requirements.

## 2. Core Execution Principles & Global Rules
The agent executing a prompt based on this template MUST adhere to the following core principles:

* **Mandatory Initial Sweep:** The **VERY FIRST ACTION** before any other task execution MUST be the `Phase 0: Initial Codebase Exploration` defined below. This involves a deep, meticulous sweep executing `ls` (or equivalent recursive directory listing) in every directory of the project root to understand the existing state.
* **Apex Standards Adherence:** Compliance with the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` relative to the project root where the plan file resides) is **MANDATORY** for all steps and deliverables. Specific rules referenced as `[(Rule #X: CODE)](<relative_path_to_standards>#rule-X)` MUST link to the corresponding rule anchor in the standards document using the correct relative path. The Standards Guide takes precedence over potentially conflicting prompt details unless a deviation is explicitly stated and justified within the prompt itself.
* **Strict Sequential Execution:**
    * The prompt defines work hierarchically: **Phase -> Task -> Step**. Each item MUST begin with an unchecked Markdown checkbox (`- [ ]`).
    * Execution MUST proceed sequentially: start with `Phase 0`, then complete all Steps within a Task before the next Task; complete all Tasks within a Phase before the next Phase.
    * Do NOT proceed to the next item until the current item is fully completed, its `Internal Success Criteria` are met (verified via `Internal Verification Method`), and its checkbox is marked complete (`- [x]`).
* **Internal Success Criteria & Verification:**
    * Each Task defines `Internal Success Criteria` and `Internal Verification Method`.
    * The agent MUST perform the internal verification upon completing the steps for a Task/Phase. Verification MUST include confirming compliance with all `(Rule #X: CODE)` references within the completed Task/Steps.
* **Recursive Error Handling / Retry Logic:**
    * If `Internal Verification` fails (criteria unmet, tests fail, rule violations detected), the agent MUST NOT proceed.
    * It MUST re-execute the failed Step(s)/Task(s), identify and implement corrections, and re-run the `Internal Verification Method` (including rule compliance checks).
    * This cycle repeats until verification succeeds.
* **Autonomous Operation & Reporting:**
    * Execution is fully autonomous unless specified otherwise.
    * Intermediate reporting is DISABLED unless explicitly required.
    * Progress/test results are logged internally per `Test Reporting Protocol`. Checkbox state visually tracks progress.
    * External reporting occurs ONLY upon completion of the entire sequence.

## 3. Mandatory Quality & Finalization Rules (Reference `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`)
Regardless of specific Step instructions, the agent MUST continuously enforce and finally verify adherence to **all** applicable rules within the **Apex Software Compliance Standards Guide** (`./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`), particularly including but not limited to:
* **Code Quality & Structure:** See Section 8 (`QUAL-*` rules).
* **Line Limit & Modularization:** Adhere to the 500-line limit per file, refactoring as needed (See Section 8, specifically Rule #16: `QUAL-SIZE`).
* **Configuration Management:** See Section 12 (`CONF-*` rules).
* **Security:** See Section 13 (`SEC-*` rules).
* **Testing & Verification:** See Section 14 (`TEST-*` rules).
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
    * Establishes context, execution mode, **explicit instruction for the mandatory `Phase 0` initial sweep**, sequential rule, **explicit reference to mandatory adherence to `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`**, reporting constraints, internal logging instructions.

* **D. Test Reporting Protocol (Internal):**
    * Defines standard for internal test log (e.g., `docs/Test_Result_Analysis.md`).
    * Specifies location, data points (Date, Scope, Pass %, Coverage %, Findings), update frequency.

* **E. Hierarchical Execution Blocks:**
    * Core of the prompt, sequential. Uses Markdown headings/lists. Separated by `---`.
    * **Every Phase, Task, Step MUST start with `- [ ]`.**

    * **E.0. MANDATORY FIRST PHASE: Initial Exploration**
        -   [ ] **Phase 0: Initial Codebase Exploration**
            * **Objective:** To perform a comprehensive, deep, and meticulous sweep of the *entire existing project directory structure* before any other tasks are initiated. This establishes a baseline understanding of the current state.
            -   [ ] **Task 0.1: Full Directory Listing Sweep**
                * **Task Objective:** Execute a recursive directory listing (`ls -R` or equivalent command appropriate for the environment) starting from the project root directory to capture the structure and contents of *every* subdirectory.
                -   [ ] * **Step 0.1.1 [(Rule #63: DIAG-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-63):** **Execute Recursive Listing:** Run the command to list all files and directories recursively within the project root. Ensure the output captures the full path for each item.
                -   [ ] * **Step 0.1.2 [(Rule #63: DIAG-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-63):** **Log Output:** Save the complete, raw output of the recursive listing command to a dedicated log file (e.g., `logs/initial_codebase_sweep.log`). This log serves as the baseline reference.
                * **Internal Success Criteria:**
                    * A recursive directory listing command was executed successfully starting from the project root.
                    * The complete output, showing all files and directories, is saved to `logs/initial_codebase_sweep.log`.
                    * Compliance with all referenced Apex Standards Rules.
                * **Internal Verification Method:**
                    * Confirm the successful execution of the listing command (e.g., exit code 0).
                    * Verify the existence and non-emptiness of the `logs/initial_codebase_sweep.log` file.
                    * Briefly review the log file content to ensure it appears to be a comprehensive directory listing.
                    * Verify compliance with referenced Apex Standards Rules for this Task and its Steps.
                * **Task Completion Testing (Internal):** N/A (Exploration Task). Update internal development log.

    ---
    * **E.1. Phase Block (`- [ ] **Phase 1: Name**`)** *(Renumber subsequent Phases and Tasks accordingly, starting from 1)*
        * Content: High-level `* **Objective:**`. Contains Task Blocks.

    * **E.2. Task Block (`- [ ] **Task 1.1: Name**`)** *(Renumber subsequent Tasks accordingly, starting from 1.1)*
        * Content: `* **Task Objective:**`, Step list items, `Internal Success Criteria`, `Internal Verification Method`, `Task Completion Testing (Internal)`.
        * *(Example incorporating the **enhanced conditional** setup task, now renumbered):*
        -   [ ] **Task 1.1: Generate/Update Project Structure via Script**
            * **Task Objective:** Define and execute a script to create the necessary project directory structure and essential blank files *based on the established plan AND informed by the initial sweep in Phase 0*. **If the project root already exists (confirmed during Phase 0), this script will only ensure the specific folders and files planned for the current execution phase exist, avoiding modification of pre-existing unrelated structures.** If the project root does not exist, it will create the initial full structure.
            -   [ ] * **Step 1.1.0 [(Rule #1: PLAN-CHK)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-1):** **Analyze Initial Sweep Log:** Review `logs/initial_codebase_sweep.log` to confirm if the project root and key directories already exist.
            -   [ ] * **Step 1.1.1 [(Rule #1: PLAN-CHK)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-1), [(Rule #26: CONF-EXT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-26):** **Generate Script Logic:** Create or update a shell script (`scripts/01_setup_project_structure.sh`) or appropriate format.
                * If the project **does not** exist (per Step 1.1.0 analysis), the script should contain commands to create **all** necessary top-level and nested directories (e.g., `src/`, `tests/`, `docs/`, `config/`, `scripts/`, `logs/`) as derived from the *overall* project plan/architecture.
                * If the project **does** exist (per Step 1.1.0 analysis), the script should contain commands to create **only** the specific directories required for the *current execution plan* that do not already exist (as determined by comparing the plan against the sweep log).
            -   [ ] * **Step 1.1.2 [(Rule #59: IMPL-PLACE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-59), [(Rule #56: DOC-INT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-56):** **Enhance Script for File Creation:** Modify the script:
                * If the project **does not** exist, it should also create **all** essential blank starter files (e.g., `src/main.js`, `README.md`, `docs/architecture.md`, `config/default.json`, `.gitignore`, `logs/.gitkeep`) within the appropriate directories.
                * If the project **does** exist, it should create **only** the specific blank files required for the *current execution plan* that do not already exist (as determined by comparing the plan against the sweep log).
                * For *newly created* files (in either case) that support comments (e.g., `.js`, `.py`, `.md`), inject relevant high-level plan comments (e.g., file purpose, related Phase/Task objective). Skip injection for non-commentable types or pre-existing files.
            -   [ ] * **Step 1.1.3 [(Rule #26: CONF-EXT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-26):** **Execute:** Run the generated/updated setup script (`scripts/01_setup_project_structure.sh`) to create the necessary directory structure and initial files. Capture any execution errors.
            * **Internal Success Criteria:**
                * The setup script (`scripts/01_setup_project_structure.sh`) is created/updated and contains correct conditional commands for directory and file generation based on project existence analysis from the sweep log [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * The script executes successfully without errors [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * The expected directory structure (either full initial or specific additions) exists in the workspace, consistent with the plan and initial state [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * Essential blank files (either full initial set or specific additions) are created in the correct locations, avoiding overwrites [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * Newly created commentable files contain injected plan-related comments [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * Compliance with all referenced Apex Standards Rules [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
            * **Internal Verification Method:**
                * Review the generated script content for correctness and conditional logic against the plan and the initial sweep log [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * Verify script execution completed successfully (exit code 0) and check for logged errors [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * List the directory structure *again* and verify it matches the script's intent based on the initial state and the plan [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * Check for the existence of the specified blank files (new or pre-existing) [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * Inspect the content of newly created files to verify comment injection (where applicable) [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
                * Verify compliance with referenced Apex Standards Rules for this Task and its Steps [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
            * **Task Completion Testing (Internal):** N/A (Setup Task). Update internal development log [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

    * **E.3. Step (`- [ ] * **Step X.Y.Z [[(Rule #N: CODE)](<relative_path_to_standards>#rule-N), ...]:** Action`)**
        * Content: Begins with explicit **action verb**. Describes single action. **MUST** reference all applicable rules from `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` using the linked format `[(Rule #N: CODE)](<relative_path_to_standards>#rule-N)`, where `<relative_path_to_standards>` is the correct relative path from the plan file to the standards file (e.g., `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` if the plan is in the root) [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
    * **E.3.1. Optional: Sub-Step (`- [ ] * **Sub-Step X.Y.Z.# [[(Rule #N: CODE)](<relative_path_to_standards>#rule-N), ...]:** Action`)**
        * Content: Begins with explicit **action verb**. Describes absolute atomic action. **MUST** reference all applicable rules from `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` using the linked format `[(Rule #N: CODE)](<relative_path_to_standards>#rule-N)`, where `<relative_path_to_standards>` is the correct relative path from the plan file to the standards file (e.g., `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` if the plan is in the root) [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

    * **E.4. Internal Success Criteria (within Task Block)**
        * Defines measurable conditions for Task completion. MUST implicitly include "Compliance with all referenced and linked Apex Standards Rules" [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

    * **E.5. Internal Verification Method (within Task Block)**
        * Defines agent actions to check Success Criteria. MUST include "Verify compliance with all referenced and linked Apex Standards Rules for this Task and its Steps" [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

    * **E.6. Task Completion Testing (Internal - within Task Block)**
        * Instructs agent to run relevant tests and update internal test log [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

    * **E.7. Phase Completion Testing (Internal - end of Phase Block)**
        * Instructs agent to run cumulative Phase tests, check metrics, update internal test log [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

* **F. Final Instruction:**
    * Explicitly commands start of execution, beginning with the **mandatory `Phase 0` sweep**, then proceeding sequentially through the subsequent phases/tasks, marking checkboxes, **adhering strictly to the linked `APEX_STANDARDS.md`**, and following the final reporting constraint [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].
    * Final explicit requirements to perform a last sweep over the tasks performed to look for gaps or missed areas [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

* **G. Contextual Footer:**
    * Metadata: Timestamp, location. `*(Instructions generated: [YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Location])*` [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

## 5. Summary
This enhanced template mandates an **initial, comprehensive codebase sweep (Phase 0)** before other work begins. It requires strict adherence to the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` relative to the plan file) by requiring explicit, linked rule references in steps and verification checks [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md]. It includes an early task (now Task 1.1) for scripting the project structure generation with conditional logic informed by the initial sweep. It enforces sequential, verifiable, and high-quality autonomous execution [cite: uploaded:STANDARDS_REPOSITORY.zip/prompt-templates/PROMPT_TEMPLATE_v1.2.0.md].

*(Meta-structure v1.2.1 explanation updated [Current Date YYYY-MM-DD])*