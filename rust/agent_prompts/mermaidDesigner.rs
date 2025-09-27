pub fn generate_mermaid_from_digest_prompt(digest: &str) -> String {
    format!(r#"
You are a Mermaid.js expert. Based on the following entity-relationship digest, create a comprehensive Mermaid.js graph diagram (\`graph TD\`).

**Instructions:**
1.  Analyze all the entities and their relationships in the provided text.
2.  Create a single \`graph TD\` that visualizes all these connections.
3.  De-duplicate relationships.
4.  The final output MUST be ONLY the Mermaid code inside a Markdown code fence (\`\`\`mermaid ... \`\`\`).
5.  Do not add any explanations, titles, or any other text before or after the code fence.
6.  **CRITICAL SYNTAX FOR LINKS:** To add a label to a link, you MUST use the format: \`NodeA -- Link Label --> NodeB\`. Do NOT use quotes around the link label.
    *   **Correct:** \`User -- writes --> Document\`
    *   **Incorrect:** \`User -- "writes" --> Document\`

**Entity-Relationship Digest:**
---
{}
---

**Mermaid Diagram:**
"#, digest)
}

pub fn generate_simplified_mermaid_prompt(digest: &str) -> String {
    format!(r#"
You are a Mermaid.js expert specializing in data visualization for documentation.
Based on the following detailed entity-relationship digest, create a **simplified**, high-level Mermaid.js graph diagram (\`graph TD\`).

**Your Goal:** Create a diagram that is easy to read and understand at a glance inside a static Markdown document. It must be visually clean and avoid being too cluttered.

**Instructions:**
1.  **Analyze the full digest:** Understand all entities and their relationships.
2.  **Simplify:**
    *   Focus on the **most important entities** and their primary relationships.
    *   You MAY omit less important entities or group related minor entities into a single representative node.
    *   You SHOULD omit most or all attributes to reduce clutter.
    *   The goal is to show the high-level structure, not every single detail.
3.  **Create a \`graph TD\` diagram:** The final output MUST be ONLY the Mermaid code inside a Markdown code fence (\`\`\`mermaid ... \`\`\`).
4.  **Do not add any explanations or other text** before or after the code fence.
5.  **Adhere to Mermaid.js syntax rules:** Pay close attention to link labeling.

**CRITICAL SYNTAX FOR LINKS:** To add a label to a link, you MUST use the format: \`NodeA -- Link Label --> NodeB\`. Do NOT use quotes around the link label.
    *   **Correct:** \`User -- writes --> Document\`
    *   **Incorrect:** \`User -- "writes" --> Document\`

---
**DETAILED ENTITY-RELATIONSHIP DIGEST:**
{}
---

**Simplified Mermaid Diagram:**
"#, digest)
}

pub fn correct_mermaid_syntax_prompt(invalid_code: &str, error_message: &str, relevant_docs: &str) -> String {
    format!(r#"
You are a Mermaid.js syntax correction expert.
You previously generated a Mermaid diagram, but it contained a syntax error.
Your task is to fix the error and provide the corrected code.

**Original (Incorrect) Code:**
\`\`\`mermaid
{}
\`\`\`

**Error Message from Validator:**
\`\`\`
{}
\`\`\`

**Relevant Documentation / Rules:**
---
{}
---

**Instructions:**
1. Analyze the error message and the incorrect code.
2. Use the provided documentation to understand the correct syntax.
3. Rewrite the Mermaid code to fix the error.
4. The final output MUST be ONLY the corrected Mermaid code inside a Markdown code fence (\`\`\`mermaid ... \`\`\`).
5. Do not add any explanations, apologies, or any other text before or after the code fence.

**Corrected Mermaid Diagram:**
"#, invalid_code, error_message, relevant_docs)
}

pub fn generate_reverse_engineering_mermaid_prompt(report: &str) -> String {
    format!(r#"
You are a Mermaid.js expert specializing in visualizing software architecture.
Based on the following reverse-engineering report, create a Mermaid.js \`graph TD\` that illustrates the system's architecture.

**Instructions:**
1.  Identify the **Core Components**, **Entry Points**, and **External/Proprietary Services** from the report.
2.  Represent each as a distinct node in the graph. Use different shapes for different types of components if it enhances clarity (e.g., databases, external APIs).
3.  Draw arrows to represent the **data and control flow** between components. Label the arrows to describe the interaction (e.g., "API Call", "Reads from", "Sends data to").
4.  Group related components into subgraphs to represent layers or services.
5.  The final output MUST be ONLY the Mermaid code inside a Markdown code fence (\`\`\`mermaid ... \`\`\`). Do not add any explanations or other text.
6.  **CRITICAL SYNTAX FOR LINKS:** Use the format \`NodeA -- Link Label --> NodeB\`. Do NOT use quotes around the link label.

**Reverse-Engineering Report:**
---
{}
---

**Architecture Flow Diagram:**
"#, report)
}
