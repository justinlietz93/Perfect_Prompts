def request_splitter_planning_prompt(spec: str, settings: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert system architect AI. Your first task is to create a high-level plan for decomposing a large request into a dependency graph of actionable tasks.
Analyze the user's specification and determine the sequence of implementation prompts and their prerequisites.

**PROCESS:**
1.  **Analyze Spec:** Thoroughly understand the user's entire specification.
2.  **Identify Invariants:** Extract global rules, constraints, and architectural principles that must apply to every step.
3.  **Define Dependency Graph:** Decompose the work into a series of tasks. For each task, identify its prerequisite tasks (dependencies). The graph should start with one or more foundational tasks with no dependencies.
4.  **Output JSON:** Format the entire output as a single, valid JSON object. Do not include any other text.

**CRITICAL JSON FORMATTING RULE:** You must produce a single, valid, parsable JSON object. All string values must be correctly escaped, especially newlines (\\n) and double quotes (\\").

**OUTPUT SCHEMA (A single JSON object):**
\`\`\`json
{
  "project": {
    "name": "...",
    "architecture": "...",
    "invariants": ["..."]
  },
  "plan": [
    { "id": 1, "title": "Foundation: Core Data Models and Services", "dependencies": [] },
    { "id": 2, "title": "Feature: Add User Authentication Endpoint", "dependencies": [1] },
    { "id": 3, "title": "Feature: Add Profile Management Endpoint", "dependencies": [1] },
    { "id": 4, "title": "Feature: Link Profiles to Auth", "dependencies": [2, 3] }
  ]
}
\`\`\`

---
**USER'S SPECIFICATION DOCUMENT:**
{spec}
---
Begin planning. Output only the single, valid JSON object containing the project context and the dependency graph plan.
"""

def request_splitter_generation_prompt(project_context: str, current_prompt_title: str, current_prompt_id: str, completed_prompt_titles: str, title: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert system architect AI. Your task is to generate the full content for a single, self-contained implementation prompt.
This prompt is part of a larger, sequential build plan. It must contain all necessary context for an agent to execute it, assuming the work from its prerequisite steps is complete.

**CRITICAL INSTRUCTION:** Generate only the text content for the prompt described below. You must fill in the content for the placeholders like <...>. Do not wrap the final output in JSON or Markdown fences.

**TEMPLATE TO USE FOR THE GENERATED PROMPT'S CONTENT:**
(You must fill this template out completely. Every part is mandatory.)
---
[#${currentPromptId.toString().padStart(2, '0')}] {current_prompt_title}

**PROJECT CONTEXT**
- **Application:** ${projectContext.name}
- **Architecture:** ${projectContext.architecture}
- **Invariants:**
${projectContext.invariants.map(inv => `  - {inv}`).join('\n')}

**PREREQUISITES**
- This step assumes the successful completion of the following previous steps:
${completedPromptTitles.length > 0 ? completedPromptTitles.map(p => `  - [#${p.id.toString().padStart(2, '0')}] ${p.title}`).join('\n') : '  - None. This is a foundational step.'}

**FEATURE REQUEST**
- **Modify the existing codebase** to implement exactly one new feature: **{current_prompt_title}**.
- This step builds upon the code generated in the prerequisite steps.

**DETAILS**
- **Input:** <Describe data/signals for this specific feature>
- **Output:** <Describe files/artifacts/sections to be created or modified>
- **Constraints:** <Describe limits, non-functional requirements etc.>
- **Non-goals:** <Describe excluded scope for this step>

**ACCEPTANCE CRITERIA**
- [ ] Feature is implemented and integrated correctly.
- [ ] Conforms to all project INVARIANTS.
- [ ] Unit tests for the new feature are included.

**AGENT INSTRUCTIONS**
- **Assume no prior context or memory about previous prompts.**
- Use the PROJECT CONTEXT, Invariants, and this FEATURE REQUEST only to guide your work.
- Do not reference other prompts by number except in the prerequisites section.
---

Begin generation. Output only the raw text for this single prompt.
"""
