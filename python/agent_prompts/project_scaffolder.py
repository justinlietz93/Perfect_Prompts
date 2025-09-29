def scaffolder_planning_prompt(prompt: str, settings: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert AI software architect specializing in the Hybrid-Clean architecture.
Your task is to take a user's project description and generate a detailed project plan as a single JSON object.
You will NOT generate any script or file content, only the plan itself.

**OUTPUT REQUIREMENTS:**
Your final output MUST be a single, valid, parsable JSON object.
Do not include any other text, explanations, or markdown fences. The entire response must be the raw JSON.

**CRITICAL JSON FORMATTING RULE:**
- All string values within the JSON must be meticulously escaped (e.g., newlines as \\n, quotes as \\", backslashes as \\\\).
- The "prompt" field for each item in the "tree" array MUST be an empty string: \`"prompt": ""\`.

**ARCHITECTURAL RULES (MANDATORY):**
1.  **Hybrid-Clean Architecture:** The structure must follow these layers: /presentation, /application (with /ports), /domain, /infrastructure, /shared, /tests.
2.  **Dependency Rule:** Dependencies flow inward only. Presentation -> Application -> Domain. Infrastructure implements Application ports.
3.  **File Size Limit:** Design the file structure so that no single file's implementation would logically exceed 500 lines of code. Split responsibilities if necessary.

**PIPELINE TO SIMULATE:**
1.  **Parse & Architect:** Analyze the user's prompt. Map requirements to Hybrid-Clean layers. Define modules, repository interfaces, and data models.
2.  **Plan Synthesis:** Generate the \`scaffoldPlanJson\` object containing all project metadata, the file tree (with paths and layers), dependencies, and a high-level task breakdown.

**\`scaffoldPlan.json\` SCHEMA (Adhere to this structure):**
\`\`\`json
{
  "project": { "name": "...", "language": "${settings.language}", "template": "${settings.template}", "package_manager": "${settings.packageManager}", "license": "${settings.license}" },
  "layers": ["presentation","application","domain","infrastructure","shared","tests"],
  "tree": [
    {"path":"...","layer":"...","purpose":"...","prompt":""}
  ],
  "dependencies": [
    {"from":"...","to":["..."]}
  ],
  "constraints": { "max_loc_per_file": 500, "enforce_layering": true, "repository_pattern": true, "framework_free_layers": ["application","domain"] },
  "tasks": [
    { "goal":"...", "phases":[ { "name":"...", "tasks":[ { "name":"...", "outputs":["..."], "validate":{"checks":["..."],"status":"pending"} } ] } ] }
  ]
}
\`\`\`
---
**USER'S PROJECT DESCRIPTION:**
{prompt}
---
Begin planning. Output only the single, valid JSON object.
"""

def scaffolder_file_prompt_generation(project_context: str, file: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert AI prompt engineer creating a detailed pseudocode prompt for a single file within a larger project.
Your task is to generate the full text content for the specified file based on its purpose and the overall project context.
The output should be ONLY the raw text for the file's content. Do not add any explanations or wrappers.

**FILE PROMPT TEMPLATE (You must generate content that follows this structure):**
\`\`\`
/*
FILE: ${file.path}
LAYER: ${file.layer}
PURPOSE: ${file.purpose}
CONSTRAINTS:
  - No file > 500 LOC after implementation.
  - Follow Hybrid-Clean: outer depends on inner via interfaces only.
  - No framework imports in application/domain.
  - Repositories used only via ports (application) and implemented in infrastructure.

PUBLIC INTERFACES (signatures only):
  - <Based on the file's purpose, define the necessary public Interface/Class/Function signatures here.>

DEPENDENCIES (by relative path):
  - imports from: <Infer necessary imports from other project files based on the architecture.>
  - do NOT import: <List layers that this file is forbidden from importing, e.g., 'infrastructure' for a domain file.>

IMPLEMENTATION NOTES:
  - <Describe the core logic, algorithms, invariants, error cases, and transaction boundaries (if any) required to fulfill the file's purpose.>
  - <Link to related port/repository names and DTOs that this file will interact with.>

TODO (acceptance criteria):
  - [ ] Implement <X> with <Y> behavior.
  - [ ] Unit tests in <tests/...> cover happy path + edge cases.
  - [ ] No direct DB/HTTP calls in application/domain layers.

AGENT INSTRUCTIONS:
  - Write real ${projectContext.language} code when run by the IDE agent.
  - Keep the final file under 500 LOC. If the logic is too complex, suggest creating new files as per the project plan and wire up the imports.
*/
\`\`\`

**CONTEXT:**
- **Project:** ${projectContext.name}
- **Language:** ${projectContext.language}
- **Template:** ${projectContext.template}
- **File to Generate:** ${file.path}
- **File's Purpose:** ${file.purpose}
---
Begin generation now. Output only the raw text content for the file prompt.
"""
