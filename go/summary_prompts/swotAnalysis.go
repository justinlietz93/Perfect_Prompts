package summary_prompts

import "fmt"

// ChunkSummaryPromptSwotAnalysis generates a prompt template
func ChunkSummaryPromptSwotAnalysis(text string) string {
	return fmt.Sprintf(`
You are an expert strategic analyst. Your task is to analyze the following document segment and extract information to build a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats).

- **Strengths:** Internal advantages or assets that support success.
- **Weaknesses:** Internal limitations or risks that could hinder success.
- **Opportunities:** External trends or openings that could be exploited.
- **Threats:** External risks or challenges that could cause harm.

Extract bullet points for each category based ONLY on the provided text. If no information is found for a category, state "Not mentioned in this segment."

**### Strengths ###**
- (List points here)

**### Weaknesses ###**
- (List points here)

**### Opportunities ###**
- (List points here)

**### Threats ###**
- (List points here)

---
DOCUMENT SEGMENT TO ANALYZE:
%s
---

Provide the extracted SWOT elements for the segment above.
`, text)
}

// ReduceSummariesPromptSwotAnalysis generates a prompt template
func ReduceSummariesPromptSwotAnalysis(text string) string {
	return fmt.Sprintf(`
You are a senior business strategist creating a final SWOT analysis report.
You have been given a series of notes extracted from a larger document, categorized into Strengths, Weaknesses, Opportunities, and Threats.
Your task is to synthesize all these notes into a single, comprehensive SWOT Matrix table in Markdown format.

**Instructions:**
1.  Consolidate all points for each of the four categories, removing duplicates and merging similar ideas.
2.  Format the final output as a 2x2 Markdown table.
3.  The content of each cell should be a bulleted list. Use \`<br>\` for line breaks within a cell to ensure proper rendering.

**Table Structure:**
| Strengths (Internal) | Weaknesses (Internal) |
| :--- | :--- |
| - Point 1 <br> - Point 2 | - Point 1 <br> - Point 2 |
| **Opportunities (External)** | **Threats (External)** |
| - Point 1 <br> - Point 2 | - Point 1 <br> - Point 2 |

---
NOTES TO SYNTHESIZE:
%s
---

Provide the single, synthesized SWOT Matrix Markdown table below.
`, text)
}
