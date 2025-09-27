
export const CHUNK_SUMMARY_PROMPT_TEMPLATE_REVERSE_ENGINEERING = (text: string) => `
You are an expert software architect specializing in reverse engineering. Your task is to analyze the following codebase segment and extract its key architectural elements.

Follow these instructions:
1.  Identify all key components (e.g., classes, modules, functions, services).
2.  For each component, describe its apparent purpose and primary responsibilities.
3.  List all explicit dependencies (e.g., imports, library usage).
4.  Identify any potential external API calls or interactions with proprietary/opaque backend systems. For these, describe the *inferred contract* (what data goes in, what comes out) rather than guessing the implementation.
5.  Format the output as a structured Markdown document.
6.  If no meaningful code or architectural elements are found, state "No significant architectural elements were identified in this segment."

**EXAMPLE FORMAT:**
### Component: \`UserService\`
*   **Purpose:** Manages user authentication and profile data.
*   **Dependencies:** \`./api/client\`, \`jwt-decode\`
*   **External Interactions:**
    *   **Proprietary Service:** \`auth.proprietary.com\`
    *   **Inferred Contract:** Sends username/password, receives a JWT token.

---
CODEBASE SEGMENT TO ANALYZE:
${text}
---

Provide the architectural analysis for the segment above.
`;

export const REDUCE_SUMMARIES_PROMPT_TEMPLATE_REVERSE_ENGINEERING = (text: string) => `
You are a senior principal engineer creating a comprehensive reverse-engineering report and a plan to rebuild a codebase.
You have been given a series of architectural analyses from different segments of the codebase.
Your task is to synthesize these into a single, cohesive, and actionable report in Markdown format.

Follow these instructions:
1.  **Synthesize Findings:** Combine all unique components, dependencies, and external interactions. Eliminate duplicates and create a holistic view of the system.
2.  **Structure the Report:** Organize the final output into the following sections:
    *   **Project Overview:** A high-level summary of the codebase's purpose and functionality.
    *   **Inferred Architecture:** Describe the overall architectural pattern (e.g., MVC, Microservices, Layered, Monolith) and the primary programming languages/frameworks detected.
    *   **Core Components & Flow:** Detail the major components and how they interact. Describe the main data and control flow through the system.
    *   **Key Entry Points:** List the primary entry points for the application (e.g., main function, API endpoints).
    *   **Dependency Map:** Provide a summary of key internal libraries and major external dependencies (e.g., React, Express, AWS SDK).
    *   **Replication Plan for Proprietary Backends:** For each identified proprietary service, provide a high-level plan explaining what is required to replicate its functionality independently. Describe the necessary data models, API contracts, and business logic.
    *   **Suggested Build Plan:** Outline a high-level, step-by-step plan to rebuild this project from scratch, including setting up the environment, creating the file structure, and implementing components in a logical order.
3.  **Clarity and Actionability:** The report must be clear, detailed, and provide a practical roadmap for a development team.

---
ARCHITECTURAL ANALYSES TO SYNTHESIZE:
${text}
---

Provide the single, synthesized reverse-engineering report below.
`;
