export const CHUNK_SUMMARY_PROMPT_TEMPLATE_RACI_SNAPSHOT = (text: string) => `
You are an expert AI systems architect. Your task is to analyze the following document segment and extract tasks and their ownership into a RACI matrix format. The roles should be for AI Agents or automated systems, not humans.

A RACI matrix clarifies ownership:
- **R = Responsible:** The AI agent that performs the work.
- **A = Accountable:** The AI agent with final ownership and decision-making authority.
- **C = Consulted:** An AI agent that provides input or expertise.
- **I = Informed:** An AI agent that is kept updated on progress or decisions.

Follow these instructions:
1.  Identify all discrete tasks, activities, or deliverables.
2.  Identify the AI Agent roles involved (e.g., Data Processing Agent, User Interface Agent, Orchestrator Agent). Infer logical agent roles if not explicitly stated.
3.  For each task, assign the appropriate RACI marker (R, A, C, I) to each relevant AI agent role.
4.  Format the output as a clear Markdown list.
5.  If no tasks or roles are identified in this segment, state "No RACI elements were identified in this segment."

**EXAMPLE FORMAT:**
*   **Task:** Ingest raw user data
    *   Data Processing Agent: R
    *   Orchestrator Agent: A
    *   Security Agent: C
*   **Task:** Generate user summary
    *   Natural Language Agent: R
    *   Orchestrator Agent: A
    *   Data Processing Agent: I

---
DOCUMENT SEGMENT TO ANALYZE:
${text}
---

Provide the extracted RACI assignments for the segment above.
`;

export const REDUCE_SUMMARIES_PROMPT_TEMPLATE_RACI_SNAPSHOT = (text: string) => `
You are an expert AI project manager responsible for creating a final, comprehensive RACI (Responsible, Accountable, Consulted, Informed) matrix.
You have been given a series of notes extracted from a larger document, each detailing various tasks and their ownership by different AI Agents.
Your task is to synthesize all these notes into a single, comprehensive RACI matrix table in Markdown format.

Follow these instructions:
1.  Identify all unique **Tasks** from the notes. Each unique task should be a row in your table.
2.  Identify all unique **AI Agent Roles** from the notes. Each unique role should be a column in your table.
3.  Construct a Markdown table with the Tasks as rows and Roles as columns.
4.  Fill in the cells of the table with the corresponding RACI marker (R, A, C, I).
5.  If a role has multiple assignments for the same task from different notes, consolidate them into the single most appropriate marker. There should only be one marker per cell.
6.  If a cell has no assignment, leave it blank.
7.  The final output must be a clean, well-formatted, and easy-to-read Markdown table. Do not include any text before or after the table.

---
NOTES TO SYNTHESIZE:
${text}
---

Provide the single, synthesized RACI Matrix Markdown table below.
`;
