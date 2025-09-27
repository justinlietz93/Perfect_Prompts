pub fn chunk_summary_prompt_pitch_generator(text: &str) -> String {
    format!(r#"
You are a strategic analyst AI. Your task is to analyze the following document segment and extract raw information that could be used to build a pitch.
Do not invent information. Extract only what is present in the text.

Structure your output clearly. For each category, list relevant points as bullets. If no information is found for a category, state "Not mentioned in this segment."

**### Problems / Pain Points ###**
- (List any problems, challenges, or user pain points described.)

**### Solutions / Features ###**
- (List any proposed solutions, product features, or capabilities.)

**### Benefits / Outcomes ###**
- (List the positive results, benefits, or value propositions mentioned.)

**### Differentiators / Unique Selling Points ###**
- (List what makes the solution unique or better than alternatives.)

**### Target Audience / Users ###**
- (Identify who the product or solution is for.)

**### Market Context / "Why Now" ###**
- (Extract any information about market trends, timing, or the competitive landscape.)

**### Data / Proof Points ###**
- (List any metrics, statistics, or evidence of success.)

**### Call to Action ###**
- (Identify any next steps, requests, or calls to action.)

---
DOCUMENT SEGMENT TO ANALYZE:
{}
---

Provide the extracted pitch elements for the segment above.
"#, text)
}

pub fn reduce_summaries_prompt_pitch_generator(text: &str) -> String {
    format!(r#"
You are an expert pitch deck writer and business strategist. You have been given a collection of raw notes extracted from a larger document.
Your task is to synthesize these notes into a cohesive and compelling multi-audience pitch.

**INSTRUCTIONS:**
1.  Analyze all the provided notes to understand the core narrative.
2.  Structure the output in Markdown with the following sections: **Problem**, **Solution**, **Why Now**, **Benefits**, **Differentiation**, **Proof**, and **Call to Action**.
3.  For EACH section, you MUST create tailored messaging for the following four audiences: **Technical**, **Non-Technical**, **Investors**, and **Users**.
4.  Frame the messaging for each audience based on their likely priorities:
    *   **Technical:** Focus on architecture, performance, scalability, integration.
    *   **Non-Technical:** Focus on ease of use, time savings, impact.
    *   **Investors:** Focus on market size, business model, competitive advantage, traction.
    *   **Users:** Focus on pain-point relief, workflow improvements, usability.
5.  If there is insufficient information for a specific audience in a specific section, it's acceptable to state "Key points are similar to the Non-Technical perspective." or provide a brief, logical inference based on the available data.
6.  The final output should be a well-organized, scannable document that tells the same core story from four different perspectives.

**EXAMPLE STRUCTURE FOR A SECTION:**
### Problem
*   **Technical:** (Your synthesized point for a technical audience here)
*   **Non-Technical:** (Your synthesized point for a non-technical audience here)
*   **Investors:** (Your synthesized point for an investor audience here)
*   **Users:** (Your synthesized point for a user audience here)

---
RAW NOTES TO SYNTHESIZE:
{}
---

Provide the complete, multi-audience pitch document below.
"#, text)
}
