def chunk_summary_prompt_entity_relationship_digest(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are an expert data modeler and systems analyst. Your task is to analyze the following document segment and extract key entities, their attributes, and their relationships.

**Instructions:**
1.  Your output must ONLY be a textual digest. Do NOT create a Mermaid diagram.
2.  Format the digest as a nested Markdown bulleted list. An entity is a distinct object (e.g., User, Document), attributes are its properties (e.g., UserID), and relationships are how entities connect (e.g., User -> writes -> Document).
3.  If no entities or relationships are found, state "No entities or relationships were identified in this segment."

**EXAMPLE FORMAT:**
*   **Entity: [Entity Name]**
    *   **Attributes:** (Comma-separated list of attributes)
    *   **Relationships:**
        *   (e.g., \`writes -> Document\`)

---
DOCUMENT SEGMENT TO ANALYZE:
{text}
---

Provide the extracted entity-relationship digest for the segment above.
"""

def reduce_summaries_prompt_entity_relationship_digest(text: str) -> str:
    """Generated prompt template function."""
    return f"""
You are a senior data architect creating a final, consolidated data model digest.
You have been given a series of entity-relationship lists from consecutive segments of a larger document.
Your task is to merge these into a single, cohesive, and de-duplicated master digest.

**INSTRUCTIONS:**
1.  **Synthesize the Textual Digest ONLY.** Do NOT create a Mermaid diagram or any separators.
2.  Identify all unique entities across all provided segments.
3.  For each unique entity, consolidate all its attributes and relationships. Remove duplicates.
4.  The final output should be a single, well-organized list of entities and their complete profiles in Markdown.
5.  If no entities or relationships were found in any of the inputs, the output should just be a single line stating that.

---
ENTITY-RELATIONSHIP LISTS TO SYNTHESIZE:
{text}
---

Provide the single, synthesized master entity-relationship digest below.
"""
