def chunk_summary_prompt_constraint_list(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert systems analyst and project manager. Your task is to analyze the following document segment and extract all constraints and requirements.

Follow these instructions:
1.  Identify all distinct constraints, requirements, or features mentioned.
2.  Categorize each item into one of the following, based on the language used (e.g., "must," "essential" vs. "should," "ideally" vs. "could," "future"):
    *   **Must-have (non-negotiable)**
    *   **Should-have (important but flexible)**
    *   **Nice-to-have (optional, future scope)**
3.  Format the output as a Markdown list under the appropriate category headers.
4.  If no constraints or requirements are found in this segment, state "No constraints or requirements were identified in this segment."

**EXAMPLE FORMAT:**
### Must-have (non-negotiable)
*   Summarizer must handle PDF, TXT, and DOCX input.

### Should-have (important but flexible)
*   Support timeline and checklist output formats.

### Nice-to-have (optional, future scope)
*   Export summaries to LaTeX.

---
DOCUMENT SEGMENT TO ANALYZE:
{text}
---

Provide the extracted constraints and requirements for the segment above.
"""

def reduce_summaries_prompt_constraint_list(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are a senior project manager responsible for creating a final, comprehensive list of project constraints and requirements.
You have been given a series of requirement lists extracted from different segments of a larger document.
Your task is to synthesize these segments into a single, cohesive, and de-duplicated master list, organized by priority.

Follow these instructions:
1.  Combine all unique requirements from the provided segments under their respective categories: **Must-have**, **Should-have**, and **Nice-to-have**.
2.  Eliminate duplicate or redundant requirements. If two items describe the same requirement, merge them into the clearest and most concise version.
3.  The final output must be a clean, well-formatted Markdown list, organized with the category headers. Do not include any text before or after the list.

---
REQUIREMENT LISTS TO SYNTHESIZE:
{text}
---

Provide the single, synthesized Constraint / Requirement List below.
"""
