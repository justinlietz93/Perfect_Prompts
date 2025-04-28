# Meta-Structure Definition for Autonomous LLM Codebase Analysis Prompts v1.0.0

**Date:** [YYYY-MM-DD]  
**Time:** [HH:MM UTC+/-Offset]

---

## 1. Overall Purpose

This document defines a standardized template structure for prompts intended to guide a Large Language Model (LLM) agent in executing comprehensive, in-depth codebase analysis projects autonomously. The structure emphasizes absolute explicitness, sequential task execution, integrated quality checks referencing the Code Analysis Quality & Standards Guide, systematic code exploration, and minimizes ambiguity to ensure reliable analysis, synthesis, and reporting according to predefined rules and requirements.

---

## 2. Core Execution Principles & Global Rules

The agent executing a prompt based on this template **MUST** adhere to the following core principles:

- **Code Analysis Standards Adherence:**  
  Compliance with the Code Analysis Quality & Standards Guide (located at `CODEBASE_STANDARDS_REPOSITORY/CODE_ANALYSIS_STANDARDS.md` relative to the project root where the plan file resides) is **MANDATORY** for all steps and deliverables. Specific rules referenced as `[(Rule #CX: DOMAIN)](<relative_path_to_standards>#rule-CX)` **MUST** link to the corresponding rule anchor in the standards document using the correct relative path. The Standards Guide takes precedence over potentially conflicting prompt details unless a deviation is explicitly stated and justified within the prompt itself.  
  *(Note: This assumes a hypothetical Code Analysis Standards Guide exists, analogous to a Coding Standards or Security Checklist).*

- **Strict Sequential Execution:**  
  The prompt defines work hierarchically: **Phase -> Task -> Step**. Each item **MUST** begin with an unchecked Markdown checkbox (`- [ ]`).  
  Execution **MUST** proceed sequentially: complete all Steps within a Task before the next Task; complete all Tasks within a Phase before the next Phase. Codebase Analysis Phases might include: Scoping & Setup, Code Parsing & Static Analysis, Dependency Mapping, Logic & Flow Analysis, Quality & Security Assessment, Synthesis & Reporting.
  
  Do **NOT** proceed to the next item until the current item is fully completed, its Internal Success Criteria are met (verified via Internal Verification Method), and its checkbox is marked complete (`- [x]`).

- **Internal Success Criteria & Verification:**  
  Each Task defines Internal Success Criteria and an Internal Verification Method.  
  The agent **MUST** perform the internal verification upon completing the steps for a Task/Phase. Verification **MUST** include confirming compliance with all `(Rule #CX: DOMAIN)` references within the completed Task/Steps (e.g., checking adherence to naming conventions, confirming dependency analysis accuracy, validating security finding locations).

- **Recursive Error Handling / Retry Logic:**  
  If Internal Verification fails (criteria unmet, standards violated, analysis tools fail, code paths unresolvable), the agent **MUST NOT** proceed.  
  It **MUST** re-execute the failed Step(s)/Task(s), identify and implement corrections (e.g., adjust parsing parameters, use alternative analysis techniques, refine logic tracing), and re-run the Internal Verification Method (including rule compliance checks).  
  This cycle repeats until verification succeeds.

- **Autonomous Operation & Reporting:**  
  Execution is fully autonomous unless specified otherwise (e.g., needing clarification on ambiguous code or configuration).  
  Intermediate reporting is **DISABLED** unless explicitly required (e.g., for generating partial dependency graphs or requesting human input on complex logic).  
  Analysis progress, files examined, functions mapped, issues identified, and verification results are logged internally per the Analysis Progress Log Protocol. Checkbox state visually tracks progress.  
  External reporting (e.g., the final analysis report, vulnerability list, or architectural summary) occurs **ONLY** upon completion of the entire sequence.

---

## 3. Mandatory Quality & Finalization Rules  
*(Reference: `./CODEBASE_STANDARDS_REPOSITORY/CODE_ANALYSIS_STANDARDS.md`)*

Regardless of specific Step instructions, the agent **MUST** continuously enforce and finally verify adherence to all applicable rules within the Code Analysis Quality & Standards Guide (`./CODEBASE_STANDARDS_REPOSITORY/CODE_ANALYSIS_STANDARDS.md`), particularly including but not limited to:

- **Code Structure & Readability:**  
  *(e.g., STRUCT-* rules) - Naming conventions, formatting, commenting clarity, modularity, file organization.

- **Logic & Complexity:**  
  *(e.g., LOGIC-* rules) - Cyclomatic complexity thresholds, algorithm clarity, proper error handling patterns, avoidance of anti-patterns.

- **Dependency Management:**  
  *(e.g., DEP-* rules) - Identifying coupling issues, detecting circular dependencies, verifying library usage against approved lists.

- **Security Vulnerability Checks:**  
  *(e.g., SEC-* rules) - Input validation, output encoding, authentication/authorization flaws, insecure configurations, secrets management.

- **Performance Considerations:**  
  *(e.g., PERF-* rules) - Identifying inefficient loops or algorithms, potential resource leaks, database query issues (N+1).

- **Testability & Coverage Analysis:**  
  *(e.g., TEST-* rules) - Assessing ease of unit testing, identifying untested code paths (requires integration with coverage tools if available).

- **Documentation Accuracy & Consistency:**  
  *(e.g., DOC-* rules) - Ensuring comments and external documentation align with code functionality.

- **Adherence to Project Standards:**  
  *(e.g., PROJ-* rules) - Compliance with project-specific style guides, framework usage patterns, or architectural principles.

- **Final Validation & Review:**  
  *(e.g., FINAL-* rules), especially a FINAL-CODE-ANALYSIS-SWEEP for overall quality, accuracy of findings, and completeness of the analysis against objectives.

---

## 4. Prompt Template Structure (Section by Section)

### A. Overall Formatting

- Enclose the entire prompt in markdown.
- All Phase, Task, Step items **MUST** begin with `- [ ]`.

### B. Subject Line

- Format: `Subject: Codebase Analysis Request - [SPECIFIC CODEBASE/MODULE/FEATURE]`

### C. Directive Section

- Establishes context (codebase analysis), execution mode (autonomous, sequential), explicit reference to mandatory adherence to `./CODEBASE_STANDARDS_REPOSITORY/CODE_ANALYSIS_STANDARDS.md`, reporting constraints, internal logging instructions.  
- Define the overall analysis objective (e.g., "Identify security vulnerabilities related to user input handling," "Map component dependencies for the billing service," "Assess technical debt in the legacy_ui module").

### D. Analysis Progress Log Protocol (Internal)

- Defines standard for internal analysis log (e.g., `analysis_artifacts/Analysis_Log.md`).
- Specifies location, data points (Date, Phase/Task, Files/Modules Analyzed, Functions/Classes Mapped, Dependencies Identified, Issues Found (Type, Severity, Location), Verification Checks Performed, Identified Ambiguities/Gaps, Compliance Notes), update frequency (e.g., after each Task verification).

### E. Hierarchical Execution Blocks

- Core of the prompt, sequential. Uses Markdown headings/lists. Separated by `---`.

- **Every Phase, Task, Step MUST start with `- [ ]`.**

#### E.1. Phase Block

- Example: `- [ ] **Phase X: Name**` *(e.g., Phase 1: Setup and Code Inventory)*  
- **Content:**  
  - High-level **Objective:**.  
  - Contains Task Blocks.

#### E.2. Task Block

- Example:  
- **Content:**  
- **Task Objective:**  
- Step list items  
- Internal Success Criteria  
- Internal Verification Method  
- Task Completion Review (Internal)

**Example Code Analysis Task:**

- [ ] Task 2.1: Static Analysis of Module [ModuleName]  
Task Objective: Perform static analysis on all relevant source files within [ModuleName] to identify potential code quality issues, complexity hotspots, and adherence to defined coding standards.  
- [ ] *Step 2.1.1 (Rule #C1: FILE_ID):* Identify all source code files (e.g., `.py`, `.java`, `.js`, `.ts`, `.cs`) within the target module path: `[path/to/module/ModuleName]`. Apply include/exclude patterns as defined: `[patterns]`.
- [ ] *Step 2.1.2 (Rule #C2: LINT_TOOL), (Rule #C3: STYLE_GUIDE):* Execute the configured linter/static analyzer (e.g., ESLint, Pylint, Checkstyle, SonarLint) using the project-specific configuration (`[path/to/config]`) against the identified files. Capture all reported issues.
- [ ] *Step 2.1.3 (Rule #C4: COMPLEX_TOOL):* If available, run code complexity analysis (e.g., Radon, built-in IDE tools, dedicated complexity checker) to calculate metrics like Cyclomatic Complexity and Cognitive Complexity for functions/methods. Identify units exceeding thresholds defined in (Rule #C4).
- [ ] *Step 2.1.4 (Rule #C5: ISSUE_AGGREGATE):* Aggregate findings from Steps 2.1.2 and 2.1.3. Normalize issue format (File, Line, Rule ID, Severity, Description). Categorize issues based on type (e.g., Style, Bug Risk, Complexity, Security, Performance).
- [ ] *Step 2.1.5 (Rule #C6: FALSE_POS_REVIEW):* Perform an initial automated review or apply heuristics to flag potential false positives based on common patterns or `# noqa` / suppression comments. Document flagged items.

**Internal Success Criteria:**

- A documented list of source files targeted for analysis exists.
- Linter/static analyzer execution completed successfully; raw output is stored.
- Complexity metrics (if applicable) are calculated and stored for relevant code units.
- A consolidated, categorized list of static analysis findings is generated in a structured format (e.g., CSV, JSON).
- Potential false positives are flagged with rationale.
- Compliance with all referenced Code Analysis Standards Rules.

**Internal Verification Method:**

- Verify the analyzed file list correctly reflects the target module and include/exclude patterns.
- Check static analyzer logs for execution errors or configuration issues.
- Spot-check a sample of reported issues against the source code to confirm location and validity.
- Verify complexity scores for high-complexity units seem plausible relative to code structure.
- Review the format and completeness of the aggregated findings list.
- Check that flagged false positives have supporting evidence or rationale.
- Verify compliance with referenced Code Analysis Standards Rules for this Task and its Steps.

**Task Completion Review (Internal):**  
Update internal Analysis Log with files analyzed, tools run, summary of findings counts by category/severity, and verification status.

#### E.3. Step Format

- **Step Format:**  
`- [ ] * **Step X.Y.Z [[(Rule #CN: DOMAIN)](<relative_path_to_standards>#rule-CN), ...]:** Action`

**Content:**  
- Begins with an explicit action verb relevant to code analysis (e.g., Parse, Analyze, Trace, Identify, Verify, Document, Report, Scan, Calculate, Map).  
- Describes a single analysis action.  
- **MUST** reference all applicable rules from `CODEBASE_STANDARDS_REPOSITORY/CODE_ANALYSIS_STANDARDS.md` using the linked format `[(Rule #CN: DOMAIN)](<relative_path_to_standards>#rule-CN)`.

##### E.3.1. Optional: Sub-Step

- **Sub-Step Format:**  
`- [ ] * **Sub-Step X.Y.Z.# [[(Rule #CN: DOMAIN)](<relative_path_to_standards>#rule-CN), ...]:** Action`

**Content:**  
- Describes an absolute atomic analysis action, referencing applicable standards.

#### E.4. Internal Success Criteria (within Task Block)

- Defines measurable conditions for Task completion (e.g., "Call graph generated for function F," "List of external API calls identified and documented," "Security scan results parsed and high-severity vulnerabilities listed").  
- **MUST** implicitly include "Compliance with all referenced and linked Code Analysis Standards Rules".

#### E.5. Internal Verification Method (within Task Block)

- Defines agent actions to check Success Criteria (e.g., "Cross-reference nodes in call graph with actual function calls in code," "Verify identified API endpoints against project documentation or configuration," "Confirm reported vulnerability locations match code patterns described in (Rule #SC1)").
- **MUST** include "Verify compliance with all referenced and linked Code Analysis Standards Rules for this Task and its Steps".

#### E.6. Task Completion Review (Internal - within Task Block)

- Instructs the agent to update the internal analysis log with findings, metrics, compliance checks, and any identified ambiguities or areas needing deeper investigation.

#### E.7. Phase Completion Review (Internal - end of Phase Block)

- Instructs the agent to review the cumulative findings for the Phase, assess overall progress against Phase objectives, check for correlations between different types of findings (e.g., high complexity correlating with bugs), and update the internal analysis log.

---

### F. Final Instruction

- Explicitly commands the start of execution, emphasizing sequential processing, checkbox marking, strict adherence to the linked `CODE_ANALYSIS_STANDARDS.md`, thoroughness, analytical rigor, and the final reporting constraint.
- **Final explicit requirement:**  
Perform a last sweep (*FINAL-CODE-ANALYSIS-SWEEP*) over the entire analysis process and output to ensure quality, accuracy, completeness, proper issue reporting, and identification of analysis limitations.

---

### G. Contextual Footer

- **Metadata:** Timestamp, location.  
*Instructions generated: [YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Location]*

---

## 5. Summary

This template adapts the rigorous execution structure for codebase analysis tasks. It mandates strict adherence to a defined Code Analysis Quality & Standards Guide (located at `./CODEBASE_STANDARDS_REPOSITORY/CODE_ANALYSIS_STANDARDS.md` relative to the plan file) by requiring explicit, linked rule references in steps and verification checks. It enforces a sequential, verifiable, and high-quality autonomous analysis process, focusing on code structure, logic flow, dependency mapping, quality metrics, security vulnerabilities, and accurate reporting.

*(Codebase analysis meta-structure v1.0.0 explanation created 2025-04-13)*
