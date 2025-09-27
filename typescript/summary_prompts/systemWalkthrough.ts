export const CHUNK_SUMMARY_PROMPT_TEMPLATE_SYSTEM_WALKTHROUGH = (text: string) => `
You are an expert software architect tasked with analyzing a segment of a system's documentation or codebase. Your goal is to extract key information to build a comprehensive explanation of how it works.

Follow these instructions:
1.  Analyze the provided segment and extract architectural details.
2.  Format your output in Markdown with the specified headings.
3.  If no information is found for a section, state "Not identified in this segment."

### Identified Components
- (List any components, classes, functions, or modules and their immediate purpose.)

### Observed Interactions & Data Flow
- (Describe how the identified components interact, what data is passed between them, and the sequence of calls.)

### Inferred Design Rationale
- (Based on the code structure, comments, or text, infer *why* it was designed this way. E.g., "This appears to use a Singleton pattern to ensure a single database connection.")

### Operational Snippets
- (Extract any small, self-contained examples of the system in action, like a function call or a log entry showing a process.)

---
SYSTEM SEGMENT TO ANALYZE:
${text}
---

Provide the structured analysis for the segment above.
`;

export const REDUCE_SUMMARIES_PROMPT_TEMPLATE_SYSTEM_WALKTHROUGH = (text: string) => `
You are a senior principal engineer tasked with writing a clear, comprehensive document explaining how a complex system works.
You have been given a series of detailed analyses from different segments of the system's codebase and documentation.
Your task is to synthesize these analyses into a single, cohesive, and easy-to-understand "System Walkthrough" document in Markdown format.

Follow these instructions:
1.  Synthesize all the provided information, eliminating redundancy and creating a holistic view.
2.  Structure the final report into the following sections:
    *   **High-Level Overview:** A plain-language summary of the system's purpose and primary function.
    *   **Core Components & Responsibilities:** A consolidated list and description of all major components.
    *   **Key Design Patterns & Rationale:** A narrative explaining the architectural choices and the inferred "why" behind the design.
    *   **Example Operational Loop:** A step-by-step narrative walkthrough of a common use case from start to finish, explaining what happens in each component and how data flows through the system.
3.  The report must be clear, detailed, and provide a practical understanding for a new engineer joining the team.

---
ANALYSES TO SYNTHESIZE:
${text}
---

Provide the single, synthesized System Walkthrough document below.
`;
