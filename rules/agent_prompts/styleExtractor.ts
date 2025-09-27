import { CITATION_INSTRUCTION } from '../shared/citation';

export const SINGLE_TEXT_STYLE_EXTRACTION_PROMPT_TEMPLATE = (text: string, styleTarget?: string) => `
You are an expert literary analyst. Your task is to analyze the following text and create a detailed "style model" or "style description".
This style model should be a comprehensive guide that another AI or human could use to replicate the writing style.

Consider the following aspects in your analysis:
1.  **Tone & Mood:** (e.g., formal, informal, witty, somber, academic, sarcastic, etc.)
2.  **Diction & Vocabulary:** (e.g., simple, complex, technical jargon, slang, descriptive, concise, etc.)
3.  **Sentence Structure:** (e.g., short and punchy, long and complex, varied, simple, compound, etc.)
4.  **Pacing & Rhythm:** (e.g., fast-paced, deliberate, meandering, etc.)
5.  **Use of Literary Devices:** (e.g., metaphors, similes, irony, humor, rhetorical questions, etc.)
6.  **Overall Voice:** (e.g., authoritative, personal, objective, narrative, etc.)

${styleTarget && styleTarget.trim().toLowerCase() !== 'all' && styleTarget.trim() !== '' ? `Focus specifically on the writing style of the character or person named "${styleTarget}". If this person's dialogue or narration isn't present, analyze the overall style and note that the target was not found.` : `Analyze the overall writing style of the entire text.`}

The output should be a well-structured description of the style, not a summary of the content.

Here is the text to analyze:
---
${text}
---

Provide your detailed style model below:
${CITATION_INSTRUCTION}
`;

export const CHUNK_STYLE_ANALYSIS_PROMPT_TEMPLATE = (text: string, styleTarget?: string) => `
You are an expert literary analyst. Your task is to analyze the following SEGMENT of a larger text and create a detailed "style model" or "style description" for this specific segment.
This style model should be a comprehensive guide that another AI or human could use to replicate the writing style found in this part of the text.

Consider the following aspects in your analysis:
1.  **Tone & Mood:** (e.g., formal, informal, witty, somber, academic, sarcastic, etc.)
2.  **Diction & Vocabulary:** (e.g., simple, complex, technical jargon, slang, descriptive, concise, etc.)
3.  **Sentence Structure:** (e.g., short and punchy, long and complex, varied, simple, compound, etc.)
4.  **Pacing & Rhythm:** (e.g., fast-paced, deliberate, meandering, etc.)
5.  **Use of Literary Devices:** (e.g., metaphors, similes, irony, humor, rhetorical questions, etc.)
6.  **Overall Voice:** (e.g., authoritative, personal, objective, narrative, etc.)

${styleTarget && styleTarget.trim().toLowerCase() !== 'all' && styleTarget.trim() !== '' ? `Focus specifically on the writing style of the character or person named "${styleTarget}". If this person's dialogue or narration isn't present, analyze the overall style and note that the target was not found.` : `Analyze the overall writing style of the entire text segment.`}

The output should be a well-structured description of the style, not a summary of the content.

Here is the text segment to analyze:
---
${text}
---

Provide your detailed style model for this segment below:
${CITATION_INSTRUCTION}
`;

export const REDUCE_STYLE_ANALYSES_PROMPT_TEMPLATE = (text: string, styleTarget?: string) => `
You are an expert editor and literary synthesizer.
You will be given a series of style analyses from consecutive segments of a larger document.
Your task is to synthesize these individual analyses into a single, cohesive, and comprehensive style model.
Identify the core, consistent stylistic elements and patterns. Note any variations or evolution of style if present.
Eliminate redundancy and create a unified, polished style description that represents the entire document.
${styleTarget && styleTarget.trim().toLowerCase() !== 'all' && styleTarget.trim() !== '' ? `The final model should focus on the style of "${styleTarget}".` : `The final model should represent the overall style.`}
The output should be a clean, well-structured style model.

Here are the style analyses to synthesize:
---
${text}
---

Provide the single, synthesized style model below:
${CITATION_INSTRUCTION}
`;
