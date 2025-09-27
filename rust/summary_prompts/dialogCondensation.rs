pub fn chunk_summary_prompt_dialog_condensation(text: &str) -> String {
    format!(r#"
You are an expert meeting summarizer. Your task is to analyze the following segment of a transcript and condense it into a dialog-style summary.

Follow these instructions:
1.  Identify each speaker. Use their name or role (e.g., "PM," "Engineer").
2.  For each speaker, extract only their most essential statements, decisions, or questions. Strip all filler words, tangents, and repetition.
3.  Maintain the chronological order of the conversation as it appears in the segment.
4.  Apply one of the following tags where appropriate to highlight key moments:
    - **[Decision]** for when a decision is made.
    - **[Action]** for when a task is assigned or a next step is defined.
    - **[Concern]** for when a risk, problem, or disagreement is raised.
5.  Format each line as: \`* **Speaker:** Key statement [Optional Tag]\`
6.  If no clear dialog or speakers are present in this segment, state "No dialog was identified in this segment."

---
TRANSCRIPT SEGMENT TO ANALYZE:
{}
---

Provide the condensed dialog for the segment above.
"#, text)
}

pub fn reduce_summaries_prompt_dialog_condensation(text: &str) -> String {
    format!(r#"
You are an expert editor responsible for creating a final, cohesive dialog-style summary of a meeting.
You have been given a series of condensed dialog segments from a larger transcript.
Your task is to merge these segments into a single, coherent conversation log.

Follow these instructions:
1.  Combine all dialog entries from the provided segments into a single, chronologically ordered list.
2.  Eliminate redundant or repeated statements. If two consecutive lines from the same speaker say similar things, merge them into one concise statement.
3.  Ensure the flow of conversation is logical and easy to follow.
4.  Maintain the original speaker attribution and any tags like [Decision], [Action], or [Concern].
5.  The final output must be a clean, well-formatted Markdown list representing the entire conversation's key points.

---
CONDENSED DIALOG SEGMENTS TO SYNTHESIZE:
{}
---

Provide the single, synthesized dialog-style summary below.
"#, text)
}
