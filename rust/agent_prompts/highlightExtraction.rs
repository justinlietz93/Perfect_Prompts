pub fn highlight_extraction_prompt(text: &str) -> String {
    format!(r#"
You are an AI assistant specializing in information extraction.
From the following summary text, identify and extract the 5 to 10 most important, impactful, or actionable highlights.
Each highlight should be a concise, self-contained sentence or two.
Return the highlights as a JSON array of objects, where each object has a "text" field.
Example format:
[
  {{"text": "This is the first important highlight."}},
  {{"text": "This is another key takeaway."}}
]
Do not include any text outside of the JSON array. The response must be only the JSON.

Here is the summary text to analyze:
---
{}
---

Extract the JSON array of highlights below:
"#, text)
}
