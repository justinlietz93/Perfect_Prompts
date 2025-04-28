# Meta-Structure Definition for Autonomous LLM Deep Research Prompts v1.0.0

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM UTC+/-Offset]

## 1. Overall Purpose
This document defines a standardized template structure for prompts intended to guide a Large Language Model (LLM) agent in executing **comprehensive, in-depth research projects** autonomously. The structure emphasizes absolute explicitness, sequential task execution, integrated quality checks referencing the **Research Quality & Integrity Standards Guide**, systematic source exploration, and minimizes ambiguity to ensure reliable synthesis and reporting according to predefined rules and requirements.

## 2. Core Execution Principles & Global Rules
The agent executing a prompt based on this template MUST adhere to the following core principles:

* **Research Standards Adherence:** Compliance with the **Research Quality & Integrity Standards Guide** (located at `RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md` relative to the project root where the plan file resides) is **MANDATORY** for all steps and deliverables. Specific rules referenced as `[(Rule #RX: DOMAIN)](<relative_path_to_standards>#rule-RX)` MUST link to the corresponding rule anchor in the standards document using the correct relative path. The Standards Guide takes precedence over potentially conflicting prompt details unless a deviation is explicitly stated and justified within the prompt itself. *(Note: This assumes a hypothetical Research Standards Guide exists, analogous to the Apex Standards Guide)*.
* **Strict Sequential Execution:**
    * The prompt defines work hierarchically: **Phase -> Task -> Step**. Each item MUST begin with an unchecked Markdown checkbox (`- [ ]`).
    * Execution MUST proceed sequentially: complete all Steps within a Task before the next Task; complete all Tasks within a Phase before the next Phase. Research Phases might include: Scoping & Planning, Source Identification & Gathering, Information Extraction & Analysis, Synthesis & Gap Identification, Reporting & Verification.
    * Do NOT proceed to the next item until the current item is fully completed, its `Internal Success Criteria` are met (verified via `Internal Verification Method`), and its checkbox is marked complete (`- [x]`).
* **Internal Success Criteria & Verification:**
    * Each Task defines `Internal Success Criteria` and `Internal Verification Method`.
    * The agent MUST perform the internal verification upon completing the steps for a Task/Phase. Verification MUST include confirming compliance with all `(Rule #RX: DOMAIN)` references within the completed Task/Steps (e.g., source credibility checks, citation formatting, synthesis depth).
* **Recursive Error Handling / Retry Logic:**
    * If `Internal Verification` fails (criteria unmet, standards violated, sources found unreliable), the agent MUST NOT proceed.
    * It MUST re-execute the failed Step(s)/Task(s), identify and implement corrections (e.g., find alternative sources, refine analysis, correct citations), and re-run the `Internal Verification Method` (including rule compliance checks).
    * This cycle repeats until verification succeeds.
* **Autonomous Operation & Reporting:**
    * Execution is fully autonomous unless specified otherwise.
    * Intermediate reporting is DISABLED unless explicitly required (e.g., for generating interim summaries or requesting clarification on ambiguous findings).
    * Research progress, sources evaluated, key findings, and verification results are logged internally per `Research Progress Log Protocol`. Checkbox state visually tracks progress.
    * External reporting (e.g., the final research report) occurs ONLY upon completion of the entire sequence.

## 3. Mandatory Quality & Finalization Rules (Reference `./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md`)
Regardless of specific Step instructions, the agent MUST continuously enforce and finally verify adherence to **all** applicable rules within the **Research Quality & Integrity Standards Guide** (`./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md`), particularly including but not limited to:
* **Source Credibility & Vetting:** (e.g., `SOURCE-*` rules) - Evaluating author expertise, publication reputation, bias, timeliness.
* **Information Accuracy & Cross-Verification:** (e.g., `ACC-*` rules) - Confirming facts across multiple reliable sources.
* **Depth of Analysis & Synthesis:** (e.g., `SYN-*` rules) - Moving beyond summarizing to comparing, contrasting, identifying themes, and drawing conclusions.
* **Citation & Attribution:** (e.g., `CITE-*` rules) - Correctly attributing all information, data, and ideas using the specified format.
* **Objectivity & Bias Mitigation:** (e.g., `BIAS-*` rules) - Acknowledging and minimizing potential biases in sources and the agent's own analysis.
* **Completeness & Gap Identification:** (e.g., `GAP-*` rules) - Assessing the scope of information gathered and explicitly identifying unanswered questions or areas needing further research.
* **Logical Coherence & Structure:** (e.g., `STRUCT-*` rules) - Ensuring the final output is well-organized, logically sound, and easy to follow.
* **Final Validation & Review:** (e.g., `FINAL-*` rules), especially a `FINAL-RESEARCH-SWEEP` for overall quality and adherence to standards.

## 4. Prompt Template Structure (Section by Section)

* **A. Overall Formatting:**
    * Enclose entire prompt in ```markdown ... ```.
    * All Phase, Task, Step items MUST begin with `- [ ]`.

* **B. Subject Line:**
    * Format: `Subject: Deep Research Request - [SPECIFIC RESEARCH TOPIC]`

* **C. Directive Section:**
    * Establishes context (deep research), execution mode (autonomous, sequential), **explicit reference to mandatory adherence to `./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md`**, reporting constraints, internal logging instructions. Define the overall research question or objective.

* **D. Research Progress Log Protocol (Internal):**
    * Defines standard for internal research log (e.g., `research_artifacts/Research_Log.md`).
    * Specifies location, data points (Date, Phase/Task, Sources Consulted, Key Findings/Data Points, Verification Checks Performed, Identified Gaps/Issues, Compliance Notes), update frequency (e.g., after each Task verification).

* **E. Hierarchical Execution Blocks:**
    * Core of the prompt, sequential. Uses Markdown headings/lists. Separated by `---`.
    * **Every Phase, Task, Step MUST start with `- [ ]`.**

    * **E.1. Phase Block (`- [ ] **Phase X: Name**`)** (e.g., Phase 1: Scoping and Planning)
        * Content: High-level `* **Objective:**`. Contains Task Blocks.

    * **E.2. Task Block (`- [ ] **Task X.Y: Name**`)** (e.g., Task 2.1: Identify & Evaluate Primary Sources)
        * Content: `* **Task Objective:**`, Step list items, `Internal Success Criteria`, `Internal Verification Method`, `Task Completion Review (Internal)`.
        * *(Example Research Task):*
        -   [ ] **Task 2.1: Identify & Evaluate Primary Sources on [Sub-Topic]**
            * **Task Objective:** Identify a diverse set of potential primary sources (e.g., academic papers, official reports, reputable news archives, expert interviews if applicable) relevant to [Sub-Topic], evaluate their credibility, and select the most relevant and reliable ones for detailed analysis.
            -   [ ] * **Step 2.1.1 [(Rule #R1: KEYWORD_DEV)](./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md#rule-R1):** Develop a comprehensive set of search keywords and phrases related to [Sub-Topic].
            -   [ ] * **Step 2.1.2 [(Rule #R2: DB_SELECT)](./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md#rule-R2):** Identify appropriate databases, search engines, and archives (e.g., PubMed, JSTOR, Google Scholar, reputable institutional repositories) for executing the searches.
            -   [ ] * **Step 2.1.3 [(Rule #R4: SEARCH_EXEC)](./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md#rule-R4):** Execute searches using the developed keywords across selected platforms. Systematically log the search strings and number of results.
            -   [ ] * **Step 2.1.4 [(Rule #R3: SOURCE_VET)](./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md#rule-R3), [(Rule #R5: RELEVANCE_CHK)](./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md#rule-R5):** Review titles, abstracts, and summaries of search results. Apply initial credibility checks (author credentials, publication venue, date) and relevance assessment based on the core research question. Create a shortlist of potentially valuable sources.
            -   [ ] * **Step 2.1.5 [(Rule #R3: SOURCE_VET)](./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md#rule-R3), [(Rule #R6: DIVERSITY_CHK)](./RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md#rule-R6):** Perform a deeper credibility assessment on the shortlisted sources. Ensure a diversity of perspectives where appropriate and possible. Select the final set of primary sources for in-depth analysis in the next Task. Document rationale for inclusion/exclusion.
            * **Internal Success Criteria:**
                * A list of effective search keywords is documented.
                * A list of appropriate search platforms is documented.
                * Search execution logs are recorded.
                * A shortlist of potential sources with initial vetting notes is created.
                * A final list of selected primary sources with documented rationale for selection (including credibility and relevance assessment) exists.
                * Compliance with all referenced Research Standards Rules.
            * **Internal Verification Method:**
                * Review keyword list for comprehensiveness.
                * Verify suitability of selected search platforms.
                * Check search logs for completeness.
                * Audit the shortlisting process against relevance and initial credibility criteria.
                * Critically review the final source selection rationale against credibility (Rule #R3), relevance (Rule #R5), and diversity (Rule #R6) standards.
                * Verify compliance with referenced Research Standards Rules for this Task and its Steps.
            * **Task Completion Review (Internal):** Update internal Research Log with sources identified, vetting results, and final selections.

    * **E.3. Step (`- [ ] * **Step X.Y.Z [[(Rule #RN: DOMAIN)](<relative_path_to_standards>#rule-RN), ...]:** Action`)**
        * Content: Begins with explicit **action verb** relevant to research (e.g., Identify, Analyze, Compare, Synthesize, Verify, Cite, Document). Describes single research action. **MUST** reference all applicable rules from `RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md` using the linked format `[(Rule #RN: DOMAIN)](<relative_path_to_standards>#rule-RN)`.
    * **E.3.1. Optional: Sub-Step (`- [ ] * **Sub-Step X.Y.Z.# [[(Rule #RN: DOMAIN)](<relative_path_to_standards>#rule-RN), ...]:** Action`)**
        * Content: Describes absolute atomic research action, referencing applicable standards.

    * **E.4. Internal Success Criteria (within Task Block)**
        * Defines measurable conditions for Task completion (e.g., "Key findings from N sources extracted and documented," "Conflicting information between Source A and Source B identified and analyzed"). MUST implicitly include "Compliance with all referenced and linked Research Standards Rules".

    * **E.5. Internal Verification Method (within Task Block)**
        * Defines agent actions to check Success Criteria (e.g., "Cross-reference extracted data points against original sources," "Review synthesis points for logical flow and source support," "Check citations against specified format [Rule #RC1]"). MUST include "Verify compliance with all referenced and linked Research Standards Rules for this Task and its Steps".

    * **E.6. Task Completion Review (Internal - within Task Block)**
        * Instructs agent to update internal research log with findings, analyses, compliance checks, and any identified gaps or issues.

    * **E.7. Phase Completion Review (Internal - end of Phase Block)**
        * Instructs agent to review the cumulative findings for the Phase, assess overall progress against Phase objectives, check for thematic coherence, and update internal research log.

* **F. Final Instruction:**
    * Explicitly commands start of execution, emphasizing sequential processing, checkbox marking, **strict adherence to the linked `RESEARCH_STANDARDS.md`**, thoroughness, critical analysis, and the final reporting constraint.
    * Final explicit requirement to perform a last sweep (`FINAL-RESEARCH-SWEEP`) over the entire research process and output to ensure quality, accuracy, completeness, proper citation, and identification of limitations/gaps.

* **G. Contextual Footer:**
    * Metadata: Timestamp, location. `*(Instructions generated: [YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Location])*`

## 5. Summary
This template adapts the rigorous execution structure for **deep research tasks**. It mandates strict adherence to a defined **Research Quality & Integrity Standards Guide** (located at `RESEARCH_STANDARDS_REPOSITORY/RESEARCH_STANDARDS.md` relative to the plan file) by requiring explicit, linked rule references in steps and verification checks. It enforces a sequential, verifiable, and high-quality autonomous research process, focusing on source evaluation, critical analysis, synthesis, and accurate reporting.

*(Research meta-structure v1.0.0 explanation created 2025-04-11)*