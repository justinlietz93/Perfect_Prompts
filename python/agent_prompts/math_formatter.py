def chunk_math_format_prompt_template(text: str, format_type: str) -> str:
    """Generate a prompt template for formatting mathematical expressions in text."""
    return f"""
You are an expert in MathJax formatting.
Your task is to reformat the following Markdown/text segment to ensure all mathematical notations are correctly formatted for MathJax rendering on GitHub.

**RULES:**
1.  **Do not change any content, text, or code.** Your only job is to fix the formatting of the math.
2.  Wrap all **inline** mathematical expressions and single variables in single dollar signs. Example: `The equation is $E = mc^2$.`.
3.  Wrap all **display** or **block** mathematical expressions (equations on their own lines) in double dollar signs. Example: `$$\\sum_{{i=1}}^n i = \\frac{{n(n+1)}}{{2}}$$`.
4.  Ensure there is an empty newline before and after any `$$` block, with no blank lines inside the block.
5.  If the math is already correctly formatted with `$` or `$$`, do not change it.
6.  Preserve all original text, markdown formatting (like headers, lists, code blocks), and line breaks exactly as they are.

**Original Text Segment:**
---
{text}
---

**Begin reformatting the text segment:**
"""