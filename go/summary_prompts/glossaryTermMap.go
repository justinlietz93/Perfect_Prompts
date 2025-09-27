package summary_prompts

import "fmt"

// ChunkSummaryPromptGlossaryTermMap generates a prompt template
func ChunkSummaryPromptGlossaryTermMap(text string) string {
	return fmt.Sprintf(`
You are an expert technical writer and lexicographer. Your task is to analyze the following document segment and extract all key terms, acronyms, and concepts to build a glossary.

Follow these instructions:
1.  Identify all important terms that require a definition for clear understanding.
2.  For each term, extract the following information if available:
    *   **Definition:** A short, clear explanation.
    *   **Category:** Thematic grouping (e.g., Technical, Process, Business).
    *   **Synonyms / Related Terms:** Cross-links to other potential glossary items.
3.  Format the extracted information as a clear Markdown list for each term.
4.  If no glossary terms are found in this segment, state "No glossary terms were identified in this segment."

**EXAMPLE FORMAT:**
*   **Term:** Embedding
    *   **Definition:** A numerical vector representation of text for ML models.
    *   **Category:** Technical
    *   **Related Terms:** Vector, Encoding
*   **Term:** KPI
    *   **Definition:** Key Performance Indicator; a measurable value for performance.
    *   **Category:** Business
    *   **Related Terms:** Metrics, Dashboard

---
DOCUMENT SEGMENT TO ANALYZE:
%s
---

Provide the extracted glossary terms for the segment above.
`, text)
}

// ReduceSummariesPromptGlossaryTermMap generates a prompt template
func ReduceSummariesPromptGlossaryTermMap(text string) string {
	return fmt.Sprintf(`
You are an expert editor creating a final, comprehensive Glossary / Term Map.
You have been given a series of notes extracted from a larger document, each detailing various terms and their definitions.
Your task is to synthesize all these notes into a single, comprehensive Glossary table in Markdown format.

Follow these instructions:
1.  Identify all unique **Terms** from the notes. Consolidate information for the same term from different notes into a single row, synthesizing the best definition.
2.  Construct a Markdown table with the following columns: \`Term\`, \`Definition\`, \`Category\`, and \`Related Terms\`.
3.  Alphabetize the final list of terms.
4.  Fill in the cells of the table with the corresponding values for each term.
5.  If a value for a specific cell is not mentioned in the notes (e.g., 'Category' is missing), use "N/A" for that cell.
6.  The final output must be a clean, well-formatted, and easy-to-read Markdown table. Do not include any text before or after the table.

---
NOTES TO SYNTHESIZE:
%s
---

Provide the single, synthesized Glossary / Term Map Markdown table below.
`, text)
}
