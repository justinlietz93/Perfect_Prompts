def chunk_summary_prompt_hierarchy_of_needs(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert systems analyst who thinks in terms of dependencies and priorities. Your task is to analyze the following document segment and extract any layered dependencies or priorities that can be structured as a hierarchy of needs or a pyramid.

Follow these instructions:
1.  Identify concepts, components, or needs that are foundational (base layers) and which ones depend on them (higher layers).
2.  For each level of the hierarchy, extract a short label and a one-line description.
3.  Order the levels from the most foundational (Level 1 - base) to the most advanced (top).
4.  Format the extracted information as a clear Markdown list for each level.
5.  If no hierarchical dependencies are identified in this segment, state "No hierarchical structure was identified in this segment."

**EXAMPLE FORMAT:**
*   **Level 1 - Infrastructure (base):** Stable hardware, compute, storage, networking.
*   **Level 2 - Data Foundations:** Clean, reliable, well-structured datasets.
*   **Level 3 - Core Models:** Working algorithms, training, evaluation pipelines.

---
DOCUMENT SEGMENT TO ANALYZE:
{text}
---

Provide the extracted hierarchy levels for the segment above.
"""

def reduce_summaries_prompt_hierarchy_of_needs(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are a senior strategist responsible for creating a final, comprehensive Hierarchy of Needs / Pyramid Summary.
You have been given a series of notes extracted from a larger document, each detailing various levels of a hierarchical structure.
Your task is to synthesize all these notes into a single, cohesive pyramid structure in Markdown format.

Follow these instructions:
1.  Identify all unique levels and their descriptions from the notes. Consolidate information for the same level from different notes into a single, refined description.
2.  Determine the correct order of the levels, from the most foundational (Level 1) at the bottom to the highest level at the top.
3.  Eliminate redundant or overlapping levels.
4.  The final output must be a clean, well-formatted, and easy-to-understand Markdown list representing the complete hierarchy. Start with a suitable title for the pyramid.

**EXAMPLE OUTPUT:**
### AI System Development Pyramid

*   **Level 1 - Infrastructure (base):** Stable hardware, compute, storage, networking.
*   **Level 2 - Data Foundations:** Clean, reliable, well-structured datasets.
*   **Level 3 - Core Models:** Working algorithms, training, evaluation pipelines.
*   **Level 4 - Integration & APIs:** Model services accessible to apps and users.
*   **Level 5 - User Value (top):** Features, insights, or automation that deliver outcomes.

---
NOTES TO SYNTHESIZE:
{text}
---

Provide the single, synthesized Hierarchy of Needs / Pyramid Summary below.
"""
