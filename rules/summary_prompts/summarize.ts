import { CITATION_INSTRUCTION } from '../shared/citation';

export const CHUNK_SUMMARY_PROMPT_TEMPLATE_DEFAULT = (text: string) => `
You are an expert technical analyst. Your task is to provide a comprehensive, detailed summary of the following segment of a technical document or transcript.
Focus on extracting the key concepts, technical details, decisions made, and any action items mentioned.
Do not make up information. The summary should be dense with information but still highly readable.
Organize the summary logically, using paragraphs to separate different topics.
The output should be a clean summary, without any introductory or concluding remarks like "Here is the summary".

Here is the document segment:
---
${text}
---

Provide your comprehensive summary below:
${CITATION_INSTRUCTION}
`;

export const REDUCE_SUMMARIES_PROMPT_TEMPLATE_DEFAULT = (text: string) => `
You are an expert editor and synthesizer of information.
You will be given a series of summaries from consecutive segments of a larger document.
Your task is to synthesize these summaries into a single, cohesive, and comprehensive summary that flows naturally.
Eliminate redundancy, resolve contradictions, and connect related concepts across the different segments.
The final output should be a polished, detailed summary of the combined information. Do not lose any key details from the input summaries.
The output should be a clean summary, without any introductory or concluding remarks.

Here are the summaries to synthesize:
---
${text}
---

Provide the single, synthesized summary below:
${CITATION_INSTRUCTION}
`;
