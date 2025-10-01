generate_tasks_prompt = """You are a hierarchical planning assistant. Given a high-level goal, the current phase, and context, decompose the phase into a sequence of logical tasks.

**Goal:**
{goal}

**Current Phase:**
Name: {phase_name}
Description: {phase_description}

**Context:**
{context}

**Instructions:**
1. Analyze the goal, current phase, and context.
2. Define a sequence of {max_tasks} or fewer specific tasks required to complete the current phase.
3. For each task, provide a concise name and a brief description.
4. Output the result as a JSON object containing a single key \"tasks\", which is a list of task objects (e.g., `[{{"name": "Task 1 Name", "description": "Task 1 Description"}}, ...]`).

**Output JSON:**
```json
{{
  "tasks": [
    {{"name": "...", "description": "..."}},
    {{"name": "...", "description": "..."}}
  ]
}}
```"""
