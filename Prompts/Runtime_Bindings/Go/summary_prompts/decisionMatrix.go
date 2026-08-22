package summary_prompts

import "fmt"

// ChunkSummaryPromptDecisionMatrix generates a prompt template
func ChunkSummaryPromptDecisionMatrix(text string) string {
	return fmt.Sprintf(`
You are a business and technical analyst AI. Your task is to analyze the following document segment and extract any information related to a decision-making process where multiple options are being compared against various criteria.

Follow these instructions:
1.  Identify the **Options** being considered (e.g., Tool A, Strategy X, Vendor Z).
2.  Identify the **Criteria** used for evaluation (e.g., Cost, Performance, Ease of Use, Security).
3.  For each option, extract its **Score/Evaluation** against each criterion (e.g., $50k, 4/5, "High Risk", "Good").
4.  Format the extracted information clearly in Markdown, listing each option and its evaluated criteria.
5.  If no comparison or decision-making process is found in this segment, state "No decision matrix elements were identified in this segment."

---
DOCUMENT SEGMENT TO ANALYZE:
%s
---

Provide the extracted decision-making information for the segment above.
`, text)
}

// ReduceSummariesPromptDecisionMatrix generates a prompt template
func ReduceSummariesPromptDecisionMatrix(text string) string {
	return fmt.Sprintf(`
You are an expert data synthesizer and technical writer. You have been given a series of notes extracted from a larger document, each detailing parts of a comparison between different options.
Your task is to synthesize all these notes into a single, comprehensive Decision Matrix table in Markdown format.

Follow these instructions:
1.  Identify all unique **Options** and **Criteria** from the notes. The Options should be the rows and the Criteria should be the columns of your table.
2.  Construct a Markdown table with the identified Options and Criteria.
3.  Fill in the cells of the table with the corresponding evaluation or score for each option against each criterion.
4.  If a score or evaluation for a specific cell is not mentioned in the notes, use "N/A" for that cell.
5.  Ensure the final output is a clean, well-formatted, and easy-to-read Markdown table. Do not include any text before or after the table.

---
NOTES TO SYNTHESIZE:
%s
---

Provide the single, synthesized Decision Matrix Markdown table below.
`, text)
}
