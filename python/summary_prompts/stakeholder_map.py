def chunk_summary_prompt_stakeholder_map(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert project and business analyst AI. Your task is to analyze the following document segment and extract all stakeholders and their related information.

A stakeholder is any individual, role, or group with an interest in the project.

Follow these instructions:
1.  Identify any stakeholders mentioned.
2.  For each stakeholder, extract the following information if available:
    *   **Interest / Goals:** What the stakeholder cares about or wants to achieve.
    *   **Influence / Power:** Their degree of authority (e.g., High, Medium, Low).
    *   **Alignment:** Their stance (e.g., Supportive, Neutral, Opposed).
    *   **Engagement Strategy:** How they should be managed or communicated with.
3.  Format the extracted information as a clear Markdown list for each stakeholder.
4.  If no stakeholders are identified in this segment, state "No stakeholders were identified in this segment."

**EXAMPLE FORMAT:**
*   **Stakeholder:** Product Manager
*   **Interest / Goals:** Delivery on time, within scope
*   **Influence:** High
*   **Alignment:** Supportive
*   **Engagement Strategy:** Regular syncs, progress demos

---
DOCUMENT SEGMENT TO ANALYZE:
{text}
---

Provide the extracted stakeholder information for the segment above.
"""

def reduce_summaries_prompt_stakeholder_map(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are a senior project manager responsible for creating a final, comprehensive Stakeholder Map.
You have been given a series of notes extracted from a larger document, each detailing various stakeholders and their attributes.
Your task is to synthesize all these notes into a single, comprehensive Stakeholder Map table in Markdown format.

Follow these instructions:
1.  Identify all unique **Stakeholders** from the notes. Consolidate information for the same stakeholder from different notes into a single, comprehensive row.
2.  Construct a Markdown table with the following columns: \`Stakeholder\`, \`Interest / Goals\`, \`Influence\`, \`Alignment\`, and \`Engagement Strategy\`.
3.  Fill in the cells of the table with the corresponding values for each stakeholder.
4.  If a value for a specific cell is not mentioned in the notes (e.g., 'Alignment' is missing), use "N/A" or a reasonable default like "Neutral".
5.  The final output must be a clean, well-formatted, and easy-to-read Markdown table. Do not include any text before or after the table.

---
NOTES TO SYNTHESIZE:
{text}
---

Provide the single, synthesized Stakeholder Map Markdown table below.
"""
