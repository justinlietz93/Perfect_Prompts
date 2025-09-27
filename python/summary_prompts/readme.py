def chunk_summary_prompt_readme(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are a technical writer AI tasked with creating a section of a project README.md file.
Your job is to analyze the following document segment and extract information relevant to a project's documentation.
Format the output in Markdown. Infer a suitable project name if one is not explicitly mentioned.

If a section is not relevant or information is not present in the segment, omit the section entirely.

# [Inferred Project Name]

## Overview
(Provide a brief, one-paragraph summary of the project's purpose or the main topic discussed in this segment.)

## Key Features / Concepts
- (A bulleted list of the most important features, technologies, or concepts discussed.)

## Technical Details
- (A bulleted list of specific technical implementation details, architectural decisions, or algorithms mentioned.)

## Setup & Usage
(If any setup instructions, code snippets, or usage examples are present, include them here in a formatted code block. Otherwise, omit this section.)

## Decisions & Action Items
- (A bulleted list of any decisions made or tasks assigned.)

---
DOCUMENT SEGMENT TO ANALYZE:
{text}
---

Provide the README.md section based on the document segment above.
"""

def reduce_summaries_prompt_readme(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert technical editor AI responsible for creating a final, comprehensive README.md document.
You will be given a series of README sections generated from consecutive parts of a larger document.
Your task is to intelligently merge these sections into a single, cohesive, well-structured README.md file.

Follow these instructions:
1.  Synthesize a single, definitive project name and use it for the main \`# Title\`.
2.  Combine all "Overview" sections into a single, polished introductory paragraph.
3.  Merge all "Key Features / Concepts," "Technical Details," and "Decisions & Action Items" into master bulleted lists, removing any duplicate points.
4.  Consolidate any "Setup & Usage" sections. If there are multiple, try to order them logically.
5.  The final output should be a clean, well-organized, and comprehensive README.md file. Ensure consistent formatting. Do not lose any critical information.

---
README SECTIONS TO SYNTHESIZE:
{text}
---

Provide the single, synthesized README.md document below.
"""
