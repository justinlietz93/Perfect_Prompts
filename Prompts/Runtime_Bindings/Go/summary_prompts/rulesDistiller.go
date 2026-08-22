package summary_prompts

import "fmt"

// ChunkSummaryPromptRulesDistiller generates a prompt template
func ChunkSummaryPromptRulesDistiller(text string) string {
	return fmt.Sprintf(`
You are an expert technical analyst and rule distiller. Your task is to analyze the following document segment and extract every hard technical rule, syntax requirement, or constraint.

Follow these instructions:
1.  Identify all enforceable directives, such as "must," "shall," "always," "never," or syntax definitions.
2.  Convert each rule into a concise, imperative statement (e.g., "Use...", "Do not...", "Ensure...").
3.  Format the output as a Markdown bulleted list.
4.  If possible, group rules under relevant categories (e.g., **Syntax**, **Security**, **Architecture**).
5.  If no rules or constraints are found in this segment, state "No rules were identified in this segment."

---
DOCUMENT SEGMENT TO ANALYZE:
%s
---

Provide the distilled rules for the segment above.
`, text)
}

// ReduceSummariesPromptRulesDistiller generates a prompt template
func ReduceSummariesPromptRulesDistiller(text string) string {
	return fmt.Sprintf(`
You are a senior technical editor responsible for creating a final, comprehensive list of technical rules.
You have been given a series of distilled rule lists from different segments of a larger document.
Your task is to synthesize these segments into a single, cohesive, and de-duplicated master list of rules.

Follow these instructions:
1.  Combine all unique rules from the provided segments.
2.  Eliminate duplicate or redundant rules. If two rules describe the same constraint, merge them into the clearest and most concise version.
3.  Organize the final list under logical categories (e.g., **Syntax**, **Architecture**, **Security**, **Process**). Consolidate rules from different segments into the same category.
4.  Infer a title for the ruleset, such as "Rules Distilled from [Document Context]".
5.  The final output must be a clean, well-formatted Markdown list of commandments.

---
RULE LISTS TO SYNTHESIZE:
%s
---

Provide the single, synthesized master list of rules below.
`, text)
}
