def chunk_summary_prompt_qa_pairs(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert analyst. Your task is to analyze the following document segment and extract all questions and their corresponding answers.

Follow these instructions:
1.  Identify all distinct questions, whether explicitly asked or implied.
2.  For each question, find the most direct and concise answer in the text.
3.  Format each pair as a Markdown bulleted list.
4.  Start each question with "**Q:**" and each answer on a new line with "**A:**".
5.  Apply one of the following tags to the answer where appropriate:
    - **[Decision]** for when an answer reflects an agreed-upon choice.
    - **[Action]** if the answer implies a next step or task.
    - **[Concern]** for when a risk or problem is identified.
    - **[Info]** for general background details or facts.
6.  If no clear questions and answers are present in this segment, state "No Q&A pairs were identified in this segment."

**EXAMPLE FORMAT:**
*   **Q:** What is the release target?
    **A:** End of Q3 2025. [Decision]
*   **Q:** What is the biggest risk?
    **A:** API refactor may slip. [Concern]

---
DOCUMENT SEGMENT TO ANALYZE:
{text}
---

Provide the extracted Q&A pairs for the segment above.
"""

def reduce_summaries_prompt_qa_pairs(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert editor responsible for creating a final, comprehensive Q&A document.
You have been given a series of Q&A pairs extracted from different segments of a larger document.
Your task is to synthesize these segments into a single, cohesive, and de-duplicated Q&A list.

Follow these instructions:
1.  Combine all unique Q&A pairs from the provided segments.
2.  Eliminate duplicate or redundant pairs. If two pairs ask the same question, merge them into the single best-worded question with the most complete and concise answer.
3.  Group the final list by theme if logical themes emerge (e.g., "Product," "Process," "Risks"). Use Markdown headers (e.g., "### Product") for grouping. If no clear themes emerge, present a single flat list.
4.  Ensure the final output is a clean, well-formatted Markdown list using the "**Q:**" and "**A:**" format.

---
Q&A PAIRS TO SYNTHESIZE:
{text}
---

Provide the single, synthesized Q&A list below.
"""
