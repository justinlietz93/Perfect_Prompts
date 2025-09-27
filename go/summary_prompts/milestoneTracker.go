package summary_prompts

import "fmt"

// ChunkSummaryPromptMilestoneTracker generates a prompt template
func ChunkSummaryPromptMilestoneTracker(text string) string {
	return fmt.Sprintf(`
You are an expert project management AI. Your task is to analyze the following document segment and extract all project milestones.

Follow these instructions:
1.  Identify any distinct milestones, deliverables, or significant checkpoints.
2.  For each milestone, extract the following information if available:
    *   **Milestone ID / Name:** A short label for the deliverable.
    *   **Objective:** What the milestone represents.
    *   **Due Date:** The target completion date.
    *   **Owner:** The person or team accountable.
    *   **Status:** The current state (e.g., Not started, In progress, Completed, At risk). Use symbols if appropriate (✔ for Completed).
    *   **Dependencies:** Other milestones that must be completed first.
    *   **Notes:** Any extra context, risks, or links.
3.  Format the extracted information as a clear Markdown list for each milestone.
4.  If no milestones are identified in this segment, state "No milestones were identified in this segment."

**EXAMPLE FORMAT:**
*   **Milestone ID:** M1
*   **Objective:** Finalize feature set
*   **Due Date:** 2025-10-15
*   **Owner:** Product Mgr
*   **Status:** ✔ Completed
*   **Dependencies:** —

---
DOCUMENT SEGMENT TO ANALYZE:
%s
---

Provide the extracted milestone information for the segment above.
`, text)
}

// ReduceSummariesPromptMilestoneTracker generates a prompt template
func ReduceSummariesPromptMilestoneTracker(text string) string {
	return fmt.Sprintf(`
You are a senior program manager responsible for creating a final, comprehensive Milestone Tracker.
You have been given a series of notes extracted from a larger document, each detailing various project milestones.
Your task is to synthesize all these notes into a single, comprehensive Milestone Tracker table in Markdown format.

Follow these instructions:
1.  Identify all unique milestones from the notes. Consolidate information for the same milestone from different notes into a single row.
2.  Construct a Markdown table with the following columns: \`Milestone ID\`, \`Objective\`, \`Due Date\`, \`Owner\`, \`Status\`, and \`Dependencies\`. You may add a 'Notes' column if relevant information is present.
3.  Assign a unique Milestone ID (e.g., M1, M2, M3...) if one is not explicitly provided.
4.  For the 'Status' column, use clear labels (e.g., "Completed", "In progress", "At risk") or symbols (✔ for Completed).
5.  Fill in the cells of the table with the corresponding values for each milestone.
6.  If a value for a specific cell is not mentioned in the notes (e.g., 'Dependencies' is missing), use "—" for that cell.
7.  The final output must be a clean, well-formatted, and easy-to-read Markdown table. Do not include any text before or after the table.

---
NOTES TO SYNTHESIZE:
%s
---

Provide the single, synthesized Milestone Tracker Markdown table below.
`, text)
}
