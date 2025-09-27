
export const CHUNK_SUMMARY_PROMPT_TEMPLATE_PRIORITY_RANKING = (text: string) => `
You are an expert project manager and strategist. Your task is to analyze the following document segment and extract all prioritized or ranked items.

Follow these instructions:
1.  Identify any tasks, features, decisions, or items that are ranked or prioritized.
2.  For each item, extract the following information if available:
    *   **Item / Task:** The feature, deliverable, or decision being ranked.
    *   **Rank:** The numeric order or priority level (e.g., 1, "High").
    *   **Criteria:** The basis for the ranking (e.g., impact, urgency, ROI).
    *   **Owner:** The person or role responsible.
    *   **Status:** The current state (e.g., Not started, In progress, Done).
3.  Format the extracted information as a clear Markdown list for each item.
4.  If no ranked items are identified in this segment, state "No ranked items were identified in this segment."

**EXAMPLE FORMAT:**
*   **Item:** Add timeline summary output
*   **Rank:** 1
*   **Criteria:** High impact, high demand
*   **Owner:** Eng Lead
*   **Status:** In progress

---
DOCUMENT SEGMENT TO ANALYZE:
${text}
---

Provide the extracted ranked items for the segment above.
`;

export const REDUCE_SUMMARIES_PROMPT_TEMPLATE_PRIORITY_RANKING = (text: string) => `
You are a senior program manager responsible for creating a final, comprehensive Priority Ranking list.
You have been given a series of notes extracted from a larger document, each detailing various prioritized items.
Your task is to synthesize all these notes into a single, comprehensive Priority Ranking table in Markdown format.

Follow these instructions:
1.  Identify all unique items from the notes. Consolidate information for the same item from different notes into a single row.
2.  Construct a Markdown table with the following columns: \`Rank\`, \`Item\`, \`Criteria\`, \`Owner\`, and \`Status\`.
3.  Sort the table by the 'Rank' column in ascending order (1, 2, 3, ...). If ranks are non-numeric (e.g., High, Medium, Low), order them logically.
4.  Fill in the cells of the table with the corresponding values for each item.
5.  If a value for a specific cell is not mentioned in the notes (e.g., 'Owner' is missing), use "N/A" for that cell.
6.  The final output must be a clean, well-formatted, and easy-to-read Markdown table. Do not include any text before or after the table.

---
NOTES TO SYNTHESIZE:
${text}
---

Provide the single, synthesized Priority Ranking Markdown table below.
`;
