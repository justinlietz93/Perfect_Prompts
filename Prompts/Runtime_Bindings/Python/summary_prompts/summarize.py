def chunk_summary_prompt_default(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert technical analyst. Your task is to provide a comprehensive, detailed summary of the following segment of a technical document or transcript.
Focus on extracting the key concepts, technical details, decisions made, and any action items mentioned.
Do not make up information. The summary should be dense with information but still highly readable.
Organize the summary logically, using paragraphs to separate different topics.
The output should be a clean summary, without any introductory or concluding remarks like "Here is the summary".

Here is the document segment:
---
{text}
---

Provide your comprehensive summary below:
"

If any external links, references, or citations are included, they MUST be listed at the end of the entire response in a dedicated "References" section, formatted using a professional citation style (e.g., APA, MLA). Do not invent citations. Only list them if present in the source text."
"""

def reduce_summaries_prompt_default(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert editor and synthesizer of information.
You will be given a series of summaries from consecutive segments of a larger document.
Your task is to synthesize these summaries into a single, cohesive, and comprehensive summary that flows naturally.
Eliminate redundancy, resolve contradictions, and connect related concepts across the different segments.
The final output should be a polished, detailed summary of the combined information. Do not lose any key details from the input summaries.
The output should be a clean summary, without any introductory or concluding remarks.

Here are the summaries to synthesize:
---
{text}
---

Provide the single, synthesized summary below:
"

If any external links, references, or citations are included, they MUST be listed at the end of the entire response in a dedicated "References" section, formatted using a professional citation style (e.g., APA, MLA). Do not invent citations. Only list them if present in the source text."
"""
