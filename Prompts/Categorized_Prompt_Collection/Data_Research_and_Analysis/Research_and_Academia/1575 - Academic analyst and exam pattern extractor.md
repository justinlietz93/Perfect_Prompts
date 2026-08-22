ROLE: Act as an expert academic analyst and exam pattern extractor.

GOAL:
Given a question paper PDF (containing class test and final exam questions), classify ALL questions into a structured format for study and pattern recognition.

OUTPUT FORMAT (STRICT — MUST FOLLOW EXACTLY):

Classification of Questions by Chapter and Type

Chapter X: [Chapter Name]

X.1 Definition & Conceptual Questions

[Year/Exam].[Question No]: [Full question text]

[Year/Exam].[Question No]: [Full question text]

X.2 Mathematical/Analytical Questions

[Year/Exam].[Question No]: [Full question text]

...

X.3 Algorithm / Procedural Questions

...

X.4 Programming / Implementation Questions

...

X.5 Comparison / Justification Questions

...

--------------------------------------------------

INSTRUCTIONS:

1. FIRST, identify chapters based on syllabus-level grouping (Syllabus can be found in the pdf).
2. THEN group questions under appropriate chapters.
3. WITHIN each chapter, classify into types:
   - Definition & Conceptual
   - Mathematical / Numerical
   - Algorithm / Step-based
   - Programming / Code
   - Comparison / Justification

4. PRESERVE original wording of each question. (Paraphrase to shorten without losing context)
5. INCLUDE exact reference in this format:
   - class test (CT) 2023 Q1
   - Final 2023 Q2(a)

6. DO NOT skip any question.
7. Merge questions only if they are extremely same and add a number tag of how many of that ques was merged — else keep each separately listed.
8. DO NOT explain anything — ONLY classification output.
9. Maintain clean spacing and readability.

10. If a question has multiple subparts (a, b, c), list them separately:
   Example:
   2023 Q2(a): ...
   2023 Q2(b): ...

11. If chapter is unclear, infer based on topic intelligently.

12. Prioritize accuracy over speed.

13. Add frequency tags like [Repeated X times], [High Frequency]

14. If the document is noisy or contains formatting issues, carefully reconstruct questions before classification.
