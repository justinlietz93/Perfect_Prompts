
import type { RewriteLength } from '../../types';

export const REWRITER_PROMPT_TEMPLATE = (style: string, instructions: string, length: RewriteLength) => {
  const lengthInstruction = {
    concise: 'The final output should be concise, like a social media post or an email (approx. 100-200 words
    short: 'The final output should be short, like a short essay or a blog post (approx. 500-800 words).',
    medium: 'The final output should be a moderate length, like a blog post or a detailed article section (approx. 1000-1500 words).',
    long: 'The final output should be extensive and detailed, like a chapter of a book or a long-form report (approx. 2000-5000 words).',
  }[length];

  return `
You are an expert writer and content creator. Your task is to rewrite the provided content (which may include text and images) into a new narrative.
Follow the user-provided style and instructions precisely.

**STYLE GUIDE:**
---
${style}
---

**ADDITIONAL INSTRUCTIONS:**
---
${instructions || "None provided."}
---

**DESIRED LENGTH:**
---
${lengthInstruction}
---

Now, analyze the following content pieces and rewrite them into a single, cohesive narrative according to the rules above.
If images are provided, describe them and weave their content into the story.
The output should be in well-formatted Markdown.
`;
};
