pub fn next_steps_technical_summary_prompt_template(summary: &str) -> String {
    format!(r#"
You are a helpful strategic assistant. Based on the provided technical summary, suggest 3-5 insightful and actionable next steps or areas for further investigation.
These suggestions should be practical and relevant to the content of the summary.
Format your response as a JSON array of strings.
Example: ["Investigate the performance impact of the new algorithm.", "Schedule a follow-up meeting to discuss the deployment timeline."]
Do not include any text outside of the JSON array.

Technical Summary:
---
{}
---

Provide the JSON array of suggestions below:
"#, summary)
}

pub fn next_steps_style_model_prompt_template(style_description: &str, style_target: Option<&str>) -> String {
    let target = style_target.unwrap_or("not specified");
    format!(r#"
You are a creative writing consultant. Based on the following extracted writing style model, provide 3-5 creative suggestions on how this style could be used or applied.
Think about different formats, audiences, or content types where this style would be effective.
If a specific person/character was targeted for the style analysis ({}), tailor the suggestions accordingly.
Format your response as a JSON array of strings.
Example: ["Use this witty and informal style to write a series of engaging blog posts.", "Apply this descriptive style to create a vivid short story."]
Do not include any text outside of the JSON array.

Extracted Writing Style Model:
---
{}
---

Provide the JSON array of suggestions below:
"#, target, style_description)
}