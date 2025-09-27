pub enum RewriteLength {
    Concise,
    Short,
    Medium,
    Long,
}

pub fn rewriter_prompt_template(style: &str, instructions: &str, length: RewriteLength) -> String {
    let length_instruction = match length {
        RewriteLength::Concise => "The final output should be concise, like a social media post or an email (approx. 100-200 words).",
        RewriteLength::Short => "The final output should be short, like a short essay or a blog post (approx. 500-800 words).",
        RewriteLength::Medium => "The final output should be a moderate length, like a blog post or a detailed article section (approx. 1000-1500 words).",
        RewriteLength::Long => "The final output should be extensive and detailed, like a chapter of a book or a long-form report (approx. 2000-5000 words).",
    };

    let instructions_text = if instructions.is_empty() {
        "None provided."
    } else {
        instructions
    };

    format!(r#"
You are an expert writer and content creator. Your task is to rewrite the provided content (which may include text and images) into a new narrative.
Follow the user-provided style and instructions precisely.

**STYLE GUIDE:**
---
{}
---

**ADDITIONAL INSTRUCTIONS:**
---
{}
---

**DESIRED LENGTH:**
---
{}
---

Now, analyze the following content pieces and rewrite them into a single, cohesive narrative according to the rules above.
If images are provided, describe them and weave their content into the story.
The output should be in well-formatted Markdown.
"#, style, instructions_text, length_instruction)
}