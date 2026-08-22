from enum import Enum

class RewriteLength(Enum):
    CONCISE = "concise"
    SHORT = "short" 
    MEDIUM = "medium"
    LONG = "long"

def rewriter_prompt_template(style: str, instructions: str, length: RewriteLength) -> str:
    """Generate a rewriter prompt template with specified style, instructions, and length."""
    
    length_instructions = {
        RewriteLength.CONCISE: "The final output should be concise, like a social media post or an email (approx. 100-200 words).",
        RewriteLength.SHORT: "The final output should be short, like a short essay or a blog post (approx. 500-800 words).",
        RewriteLength.MEDIUM: "The final output should be a moderate length, like a blog post or a detailed article section (approx. 1000-1500 words).",
        RewriteLength.LONG: "The final output should be extensive and detailed, like a chapter of a book or a long-form report (approx. 2000-5000 words).",
    }
    
    length_instruction = length_instructions[length]
    instructions_text = instructions if instructions else "None provided."
    
    return f"""
You are an expert writer and content creator. Your task is to rewrite the provided content (which may include text and images) into a new narrative.
Follow the user-provided style and instructions precisely.

**STYLE GUIDE:**
---
{style}
---

**ADDITIONAL INSTRUCTIONS:**
---
{instructions_text}
---

**DESIRED LENGTH:**
---
{length_instruction}
---

Now, analyze the following content pieces and rewrite them into a single, cohesive narrative according to the rules above.
If images are provided, describe them and weave their content into the story.
The output should be in well-formatted Markdown.
"""