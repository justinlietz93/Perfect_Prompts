pub fn chunk_summary_prompt_risk_register(text: &str) -> String {
    format!(r#"
You are an expert risk analyst AI. Your task is to analyze the following document segment and extract all potential risks.

Follow these instructions:
1.  Identify any potential risks, uncertainties, or threats mentioned.
2.  For each risk, extract the following information if available:
    *   **Description:** A short, clear description of the risk.
    *   **Category:** The type of risk (e.g., Technical, Operational, Financial, Compliance).
    *   **Probability:** Likelihood (e.g., High, Medium, Low).
    *   **Impact:** Severity (e.g., High, Medium, Low).
    *   **Mitigation:** Planned actions to reduce or control the risk.
    *   **Owner:** The person or role responsible for the risk.
    *   **Status:** The current state of the risk (e.g., Open, Monitoring, Mitigated, Closed).
3.  Format the extracted information as a clear Markdown list.
4.  If no risks are identified in this segment, state "No risks were identified in this segment."

**EXAMPLE FORMAT:**
*   **Description:** API refactor delay
*   **Category:** Technical
*   **Probability:** High
*   **Impact:** High
*   **Mitigation:** Add extra devs, limit scope
*   **Owner:** Eng Manager
*   **Status:** Open

---
DOCUMENT SEGMENT TO ANALYZE:
{}
---

Provide the extracted risk information for the segment above.
"#, text)
}

pub fn reduce_summaries_prompt_risk_register(text: &str) -> String {
    format!(r#"
You are a senior project manager responsible for creating a final, comprehensive Risk Register.
You have been given a series of notes extracted from a larger document, each detailing various risks.
Your task is to synthesize all these notes into a single, comprehensive Risk Register table in Markdown format.

Follow these instructions:
1.  Identify all unique risks from the notes. Consolidate information for the same risk from different notes into a single row.
2.  Construct a Markdown table with the following columns: \`Risk ID\`, \`Description\`, \`Category\`, \`Probability\`, \`Impact\`, \`Score\`, \`Mitigation\`, \`Owner\`, and \`Status\`.
3.  Assign a unique Risk ID to each risk (e.g., R1, R2, R3...).
4.  Calculate a numeric \`Score\` if possible (e.g., High=3, Medium=2, Low=1; Score = Probability * Impact). If not possible, use "N/A".
5.  Fill in the cells of the table with the corresponding values for each risk.
6.  If a value for a specific cell is not mentioned in the notes (e.g., 'Owner' is missing), use "N/A" for that cell.
7.  The final output must be a clean, well-formatted, and easy-to-read Markdown table. Do not include any text before or after the table.

---
NOTES TO SYNTHESIZE:
{}
---

Provide the single, synthesized Risk Register Markdown table below.
"#, text)
}
