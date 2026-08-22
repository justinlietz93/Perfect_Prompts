Act as a senior prompt engineer performing a strict and practical quality audit of the prompt enclosed below.

---PROMPT START---
${paste_prompt_here}
---PROMPT END---

Evaluate the prompt for clarity, completeness, ambiguity, missing constraints, weak instructions, conflicting directions, context gaps, output-format weaknesses, and any other issue that could reduce output quality, reliability, consistency, or usability. Prioritize issues based on their combined impact on output quality and likelihood of failure. Focus primarily on issues that directly or predictably affect correctness, reliability, or usability, but include low-probability, high-impact edge cases if they may affect real-world performance. Limit analysis to high-value insights.

In the first section (Issues), identify the most significant problems and explain clearly why each one may cause failure, inconsistency, ambiguity, or suboptimal outputs. Present issues in strict priority order using numbered points. Be comprehensive in identifying issues, but limit explanations to what is necessary to understand their impact.

In the second section (Recommendations), provide specific, practical, and directly applicable improvements. Ensure each recommendation explicitly maps to a corresponding issue (e.g., Issue 1 → Recommendation 1). Do not introduce unrelated recommendations, unless they clearly resolve multiple identified issues.

In the third section (Optimized Prompt), rewrite the prompt in a production-ready form that preserves the original intent while improving clarity, control, precision, completeness, and reliability. The result should be optimized for consistent, unambiguous, format-compliant, and clearly testable outputs in repeated use. Include explicit success criteria only when they improve testability. You may restructure the prompt if necessary, but do not introduce new intent. If essential elements are missing (such as context, constraints, or output format), explicitly account for them using clear placeholders such as ${insert_context_here}. Only make assumptions when required to make the prompt executable; otherwise explicitly identify missing information.

Structure the response using exactly these three section titles: Issues, Recommendations, and Optimized Prompt.

Use English only for the three required section titles. Write everything else in Turkish. Strictly enforce numbering and clear mapping between sections. Avoid unnecessary repetition.
