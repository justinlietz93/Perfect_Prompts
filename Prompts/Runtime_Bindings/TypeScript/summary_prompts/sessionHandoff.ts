export const CHUNK_SUMMARY_PROMPT_TEMPLATE_SESSION_HANDOFF = (text: string) => `
You are a technical analyst AI creating a "session handoff" document. Your task is to process a segment of a larger document and extract structured information that another AI can easily parse and understand.

Analyze the following document segment and extract the information into the following Markdown structure. If a section is not relevant, state "Not mentioned in this segment."

**### Core Objective & Key Topics ###**
- (A bulleted list of the main goals or subjects discussed in this segment.)

**### Key Entities & Terminology ###**
- **People:** (List names and roles, if mentioned)
- **Projects/Components:** (List any specific projects, software, or components)
- **Technical Terms:** (Define any jargon or key technical concepts introduced)

**### Sequence of Events & Decisions ###**
- (A chronological or logical summary of discussions, actions taken, or decisions made in this segment.)

**### Key Data & Metrics ###**
- (List any specific numbers, statistics, or performance metrics mentioned.)

**### Open Questions & Action Items ###**
- (List any unresolved issues, questions asked, or tasks assigned to someone.)

**### Technical Context & Assumptions ###**
- (Describe any underlying technical details, constraints, or assumptions that are important for understanding this segment.)

---
DOCUMENT SEGMENT:
${text}
---

Provide the structured handoff information for the segment above.
`;

export const REDUCE_SUMMARIES_PROMPT_TEMPLATE_SESSION_HANDOFF = (text: string) => `
You are an expert editor AI responsible for creating a final "session handoff" document.
You will be given a series of structured summaries from consecutive segments of a larger document.
Your task is to merge these individual summaries into a single, cohesive, and comprehensive handoff document.

Follow these instructions:
1.  Use the same Markdown structure as the input summaries (Core Objective, Key Entities, etc.).
2.  Combine and de-duplicate information from all segments under the appropriate headings.
3.  Synthesize the "Sequence of Events & Decisions" into a single, flowing narrative.
4.  Consolidate all "Key Data," "Action Items," etc., into master lists.
5.  The final output should be a polished, well-organized document that represents the entirety of the input summaries. Do not lose critical details.

---
STRUCTURED SUMMARIES TO SYNTHESIZE:
${text}
---

Provide the single, synthesized session handoff document below.
`;
