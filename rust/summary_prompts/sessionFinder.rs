pub fn chunk_summary_prompt_solution_finder(text: &str) -> String {
    format!(r#"
You are an expert technical support engineer. Your task is to analyze the following document segment to find a solution to a problem.
Your goal is to create a clear, step-by-step instructional guide based ONLY on the information provided in the segment.

Follow these instructions carefully:
1.  Identify a problem, error, or question being addressed in the text.
2.  Extract the corresponding solution as a series of actionable steps.
3.  If any terminal commands, code snippets, or configuration changes are part of the solution, they MUST be included in Markdown code fences (\`\`\`) to be easily copyable.
4.  Format the output as a numbered list in Markdown.
5.  If no clear problem and solution are present in this segment, state "No specific solution was identified in this segment."

---
DOCUMENT SEGMENT TO ANALYZE:
{}
---

Provide the step-by-step solution guide based on the segment above.
"#, text)
}

pub fn reduce_summaries_prompt_solution_finder(text: &str) -> String {
    format!(r#"
You are a senior technical writer responsible for creating a final, comprehensive solution guide.
You have been given a series of step-by-step instructions extracted from different segments of a larger document.
Your task is to synthesize these segments into a single, cohesive, start-to-finish guide.

Follow these instructions:
1.  Analyze all the provided steps and understand the overall solution flow.
2.  Merge and consolidate the steps into one logical, numbered sequence.
3.  Eliminate redundant instructions and combine related steps.
4.  Ensure all terminal commands and code snippets are correctly formatted in Markdown code fences (\`\`\`) and placed within the correct step.
5.  Re-write the instructions for clarity and conciseness, making it easy for a user to follow.
6.  The final output must be a single, polished, step-by-step solution guide. Do not lose any critical commands or configuration details.

---
INSTRUCTIONAL SEGMENTS TO SYNTHESIZE:
{}
---

Provide the single, synthesized solution guide below.
"#, text)
}
