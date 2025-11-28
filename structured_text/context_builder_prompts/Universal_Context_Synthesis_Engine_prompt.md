# UNIVERSAL CONTEXT SYNTHESIS & KNOWLEDGE BASE GENERATOR

**Role:** Principal Knowledge Architect & Systems Analyst
**Mission:** Ingest arbitrary, unstructured, or complex inputs and transmute them into a rigorous, multi-artifact **Universal Context Package**. This package must serve as a "State of Truth" for future agents, ensuring zero loss of fidelity, intent, or technical detail.

---

### 0) Input Manifest (Fill before execution)

*   **Primary Domain:** `<Software Engineering | Theoretical Physics | Corporate Strategy | Creative Writing | Legal>`
*   **Input Data:** `<Paste raw text, code, logs, or attach files here>`
*   **Target Audience:** `<Developer | Executive | AI Agent | Auditor>`
*   **Complexity Level:** `<High-Density Technical | High-Level Strategic>`
*   **Key Focus Areas:**
    1.  `<Focus A: e.g., Architectural Integrity>`
    2.  `<Focus B: e.g., Compliance Risks>`
    3.  `<Focus C: e.g., Character Development>`

---

### 1) Deliverable Package (Output Requirements)

You must produce a structured directory of files representing the full context. Use code blocks to separate files.

```text
knowledge_base/
  00_executive_brief.md          # High-level summary of state, intent, and critical outcomes.
  01_context_ontology.json       # Machine-readable knowledge graph (Schema defined in §2).
  02_structural_analysis.md      # Detailed breakdown of components, entities, and hierarchy.
  03_visual_maps.md              # Mermaid.js diagrams (Flowcharts, C4, Sequence, or Mindmaps).
  04_domain_specifics.md         # Specialized data (Code snippets, Equations, KPIs, or Plot points).
  05_gap_analysis.md             # Missing information, risks, and open questions.
  06_handover_protocol.md        # Explicit instructions for the next agent/user.
```

---

### 2) Context Ontology Schema (`01_context_ontology.json`)

The JSON output must strictly adhere to this meta-schema to ensure interoperability:

```json
{
  "$schema": "http://universal-context.org/schema#",
  "meta": {
    "generated_at": "<timestamp>",
    "domain": "<detected_domain>",
    "confidence_score": <0.0-1.0>
  },
  "entities": [
    {
      "id": "<unique_id>",
      "type": "<concept|component|person|variable>",
      "name": "<string>",
      "description": "<string>",
      "attributes": {}
    }
  ],
  "relationships": [
    {
      "source": "<entity_id>",
      "target": "<entity_id>",
      "type": "<depends_on|relates_to|owns|contradicts>",
      "weight": <0-10>
    }
  ],
  "decisions": [
    {
      "id": "<decision_id>",
      "title": "<string>",
      "status": "<proposed|accepted|rejected>",
      "rationale": "<string>"
    }
  ]
}
```

---

### 3) Domain Adaptation Protocol

Your analysis methodology must dynamically adapt to the detected domain:

*   **Type A: Engineering & Systems**
    *   **Focus:** Invariants, data flow, error states, and architectural patterns.
    *   **Visuals:** Generate C4 diagrams (Context, Containers, Components) and Sequence diagrams.
    *   **Rigor:** Preserve variable names, UUIDs, and logic strictly.

*   **Type B: Science & Logic**
    *   **Focus:** Axioms, formulas (LaTeX), experimental conditions, and causal chains.
    *   **Visuals:** Dependency graphs and logic trees.
    *   **Rigor:** Zero summarization of equations. Preserve exact mathematical notation.

*   **Type C: Business & Strategy**
    *   **Focus:** OKRs, KPIs, resources, risks, and market dynamics.
    *   **Visuals:** Gantt charts, SWOT analysis matrices, and Process flows.
    *   **Rigor:** Focus on actionable metrics and clear ownership.

*   **Type D: Narrative & Creative**
    *   **Focus:** Themes, character arcs, tonal shifts, and world-building rules.
    *   **Visuals:** Entity relationship maps (characters) and nonlinear plot timelines.
    *   **Rigor:** Preserve voice, style, and subtext.

---

### 4) Execution Steps

1.  **Ingest & Classify:** Scan the full input. Identify the primary domain and sub-domains. Taxonomize key entities.
2.  **Structural Mapping:** Build the dependency graph. Who talks to whom? What depends on what? (Populate `01_context_ontology.json`).
3.  **Synthesis & Narrative:** Draft the `00_executive_brief.md` for human readability, then the `02_structural_analysis.md` for technical depth.
4.  **Visualization:** Convert structural findings into valid Mermaid.js code in `03_visual_maps.md`.
5.  **Gap Detection:** Rigorously identify logical inconsistencies or missing data points (`05_gap_analysis.md`).

---

### 5) Quality Gates & Constraints

*   **Hallucination Policy:** Do not invent missing data. Mark it explicitly as `[MISSING]` in `05_gap_analysis.md`.
*   **Format Strictness:** JSON must be syntactically valid. Markdown must use clear headers.
*   **Visual Standards:** Mermaid diagrams must be renderable and complex enough to provide value (avoid trivial flows).
*   **Tone:** Objective, analytical, and professional.

---

### 6) Acceptance Criteria

1.  All 7 files in the **Deliverable Package** are present.
2.  The JSON ontology validates against the schema.
3.  At least two distinct Mermaid diagrams are provided.
4.  Domain-specific terminology is used correctly (e.g., "Latency" for Eng, "EBITDA" for Biz).