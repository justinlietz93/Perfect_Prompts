generate_phases_prompt = """You are a hierarchical planning assistant. Given a high-level goal and context, decompose the goal into a sequence of logical phases.

**Goal:**
{goal}

**Context:**
{context}

**Instructions:**
1. Analyze the goal and context.
2. Define a sequence of {max_phases} or fewer high-level phases required to achieve the goal.
3. For each phase, provide a concise name and a brief description.
4. Output the result as a JSON object containing a single key \"phases\", which is a list of phase objects (e.g., `[{{"name": "Phase 1 Name", "description": "Phase 1 Description"}}, ...]`).

**Output JSON:**
```json
{{
  "phases": [
    {{"name": "...", "description": "..."}},
    {{"name": "...", "description": "..."}}
  ]
}}
```"""
