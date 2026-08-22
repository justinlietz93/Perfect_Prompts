pub fn chunk_summary_prompt_process_flow(text: &str) -> String {
    format!(r#"
You are an expert process analyst. Your task is to analyze the following document segment and extract any process flows, sequences of actions, or step-by-step instructions.

Follow these instructions:
1.  Identify all concrete steps, actions, or states in the process described.
2.  Note any decision points (e.g., if/else conditions) and their outcomes.
3.  Identify any loops or repetitions.
4.  Format the output as a clear, ordered list (numbered or bulleted) in Markdown. Use indentation to show sub-steps or conditional branches.
5.  If no process flow is identified in this segment, state "No process flow was identified in this segment."

**EXAMPLE FORMAT:**
1.  Detect anomaly
2.  Verify alert
    *   If false positive → End
    *   If valid → Continue
3.  Classify severity

---
DOCUMENT SEGMENT TO ANALYZE:
{}
---

Provide the extracted process flow for the segment above.
"#, text)
}

pub fn reduce_summaries_prompt_process_flow(text: &str) -> String {
    format!(r#"
You are a senior process engineer responsible for creating a final, comprehensive process map.
You have been given a series of process flow segments extracted from a larger document.
Your task is to synthesize these segments into a single, cohesive, start-to-finish process flow.

Follow these instructions:
1.  Analyze all the provided steps and understand the overall workflow.
2.  Merge and consolidate the steps into one logical, ordered sequence.
3.  Eliminate redundant steps and combine related actions.
4.  Ensure all decision points and branches are correctly integrated into the main flow.
5.  Organize the final output as a clean, easy-to-follow numbered list in Markdown, using indentation for sub-steps and branches.
6.  The final output must be a single, polished process map.

---
PROCESS FLOW SEGMENTS TO SYNTHESIZE:
{}
---

Provide the single, synthesized process flow map below.
"#, text)
}
