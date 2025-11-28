# SESSION STATE PERSISTENCE & HANDOFF — PROMPT TEMPLATE

**Mission**
Act as a **Cognitive State Preservation Engine**. Exhaustively analyze the current session's discourse, code, and latent intent to produce a **high-fidelity Handoff Artifact**. The goal is **Zero-Loss Context Switching**: a future agent must be able to resume work immediately without re-reading the full history. You will capture not just the *explicit* data, but the *liminal* state—the "why," the rejected paths, and the intuitive leaps.

---
<!-- Mini “Fill Sheet” (copy this block below for fast reuse) -->
### 0) Inputs (fill these)

* **Current Session Scope:** `<Ideation | Debugging | Refactoring | Architecture | Creative Writing>`
* **Primary Domain:** `<Software Eng | Physics | Philosophy | General>`
* **Session Duration/Depth:** `<Short | Deep Dive | Multi-day>`
* **Critical Entities:** `<Project Name, Module X, Algorithm Y>`
* **Urgency Level:** `<Low | Medium | Critical>`
* **Next Action Owner:** `<User | AI | Specific Role>`

---

### 1) Output Package (exact files to produce)

The output must be a structured set of artifacts (virtual files), not a single text block.

```
handoff/
  00_executive_narrative.md         # The "Story of the Session" (chronological & logical flow)
  01_state_snapshot.json            # Machine-readable context (Schema §2)
  02_active_context.md              # Current focus, hot paths, immediate blockers
  03_concept_map.mmd                # Mermaid Mindmap of ideas/entities explored
  04_decision_log.md                # What was decided, what was rejected, and why
  05_liminal_space.md               # Abstract connections, intuition, tone, and "the unsaid"
  06_next_actions.md                # Prioritized tasks with estimated difficulty
  07_environment_spec.md            # Variables, constants, library versions, or axioms assumed
  assets/                           # Rendered diagrams
```

---

### 2) Machine-Readable State — `state_snapshot.json` (JSON Schema)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Session State Object",
  "type": "object",
  "required": ["timestamp", "domain", "status", "focus"],
  "properties": {
    "timestamp": { "type": "string" },
    "domain": { "type": "string" },
    "status": { "type": "string", "enum": ["stable", "volatile", "blocked", "complete"] },
    "focus": {
      "type": "object",
      "properties": {
        "primary_topic": { "type": "string" },
        "active_files": { "type": "array", "items": { "type": "string" } },
        "cursor_position": { "type": "string", "description": "Conceptual location in the problem space" }
      }
    },
    "entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "type"],
        "properties": {
          "name": { "type": "string" },
          "type": { "type": "string" },
          "state": { "type": "string" },
          "definition": { "type": "string" }
        }
      }
    },
    "knowledge_graph": {
      "type": "object",
      "description": "Adjacency list of related concepts detected in session"
    },
    "sentiment": {
      "type": "object",
      "properties": {
        "tone": { "type": "string" },
        "frustration_level": { "type": "number", "minimum": 0, "maximum": 1 }
      }
    }
  }
}
```

---

### 3) Process & Method (Execution Protocol)

**3.1 Domain & Signal Extraction**
*   **Identify the Domain:** Adapt parsing logic.
    *   *Coding:* Prioritize stack traces, UUIDs, function signatures, and diffs.
    *   *Physics/Math:* Preserve LaTeX ($$), constants, and derivation steps.
    *   *Philosophy/Creative:* Track dialectic shifts, tonal changes, and metaphors.
*   **Filter Noise:** Remove conversational filler ("Thank you," "Can you check?") but retain the *intent* behind the query.

**3.2 Liminal Analysis (The "Between" Spaces)**
*   **Detect Rejected Paths:** Identify ideas that were discussed and discarded. Record *why* they were rejected to prevent regression.
*   **Capture Intuition:** Note leaps in logic that weren't fully proven but assumed true. Label these as `[Assumption]`.
*   **Tonal Mapping:** Was the session exploratory and loose, or rigid and debugging-focused? This dictates the tone of the next agent.

**3.3 Narrative Synthesis (`00_executive_narrative.md`)**
*   Convert the raw log into a **causal chain**. "User asked X -> We tried Y -> Error Z occurred -> We pivoted to A."
*   Do not use bullet points for the narrative; use cohesive paragraphs.

**3.4 Visual Mapping**
*   Generate a **Mermaid.js Mindmap** (`03_concept_map.mmd`) showing the relationship between Key Entities identified in the session.

**3.5 Actionable Consolidation**
*   Merge "Open Questions" and "Next Steps" into a rigorous **Action Matrix**.
*   Assign a **Confidence Score** (0-100%) to any partial solutions.

---

### 4) Constraints & Style

*   **Rigor:** Technical details (versions, error codes, formulas) must be verbatim.
*   **No Redundancy:** Deduplicate information across the generated artifacts.
*   **Navigability:** Use clear headers and links between the virtual files.
*   **Objective Tone:** Clinical, precise, and professional.

---

### 5) Quality Gates (Self-Correction)

Before outputting, rate the handoff (0-5) on:
1.  **Resumability:** Can a new model start work in <10 seconds?
2.  **Ambiguity Reduction:** Are all pronouns ("it", "that") resolved to specific entities?
3.  **Context Density:** Is the ratio of information to words maximized?
4.  **Liminal Capture:** Did we save the *intent*, not just the text?

**Top Risk:** Identify one critical piece of context that is missing or ambiguous in the current session.

---

### 6) Acceptance Criteria (Must Pass)

1.  Output contains all files listed in **§1**.
2.  JSON in `01_state_snapshot.json` is valid and parseable.
3.  `03_concept_map.mmd` renders a valid Mermaid diagram.
4.  Narrative in `00_executive_narrative.md` explains the *evolution* of the session, not just the final state.
5.  All code snippets in the handoff are wrapped in correct language blocks.
6.  The "Liminal Space" artifact captures at least one implicit assumption or rejected idea.