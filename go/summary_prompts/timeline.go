package summary_prompts

import "fmt"

// ChunkSummaryPromptTimeline generates a prompt template
func ChunkSummaryPromptTimeline(text string) string {
	return fmt.Sprintf(`
You are an expert historical analyst. Your task is to analyze the following document segment and extract key events, dates, and their outcomes in chronological order.

Follow these instructions:
1.  Format the output as a Markdown bulleted list. Each item should represent a single event or a closely related group of events.
2.  If a specific date or time is mentioned (e.g., "Q3 2023", "last Tuesday", "2024-01-15"), start the line with it in bold markdown (e.g., **Q3 2023:**).
3.  If no specific date is present, describe the event in its logical sequence relative to other events in this segment without a date prefix.
4.  Focus on actions, decisions, and outcomes.
5.  If no chronological events are found in this segment, state "No chronological events were identified in this segment."

---
DOCUMENT SEGMENT TO ANALYZE:
%s
---

Provide the chronological list of events for the segment above.
`, text)
}

// ReduceSummariesPromptTimeline generates a prompt template
func ReduceSummariesPromptTimeline(text string) string {
	return fmt.Sprintf(`
You are an expert editor specializing in creating comprehensive timelines.
You will be given a series of chronologically ordered event lists from consecutive segments of a larger document.
Your task is to merge these lists into a single, cohesive timeline.

Follow these instructions:
1.  Combine all events from the input lists into a single master list.
2.  Sort the master list chronologically. If specific dates/times are present, use them for sorting. If dates are relative or absent, use the document's sequential flow to determine the order.
3.  Remove duplicate events and merge related information into a single, more comprehensive bullet point where appropriate.
4.  Ensure the final output is a clean, well-formatted Markdown bulleted list representing the complete timeline.

---
EVENT LISTS TO SYNTHESIZE:
%s
---

Provide the single, synthesized timeline below.
`, text)
}
