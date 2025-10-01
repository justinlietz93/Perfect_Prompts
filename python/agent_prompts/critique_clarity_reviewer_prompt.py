critique_clarity_reviewer_prompt = """You are acting as a Clarity Reviewer. Your task is to review the provided checklist steps for clarity, precision, and actionability.

**Context:**
{context}

**Steps to Review:**
```json
{steps}
```

**Instructions:**
1. Analyze each step's wording.
2. Identify any ambiguous language, vague instructions, or steps that are not clearly actionable.
3. Ensure each step is concise and easy to understand.
4. Provide concise feedback listing the steps that lack clarity or actionability, briefly explaining why. If all steps are clear, state "Steps are clear and actionable."

**Critique:**"""
