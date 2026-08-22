

import type { ReasoningSettings } from '../../types';

/**
 * Retrieves the detailed directive for a given persona setting.
 * This is exported to be used by both the prompt generation and the service layer.
 * @param settings The current reasoning settings.
 * @returns A string containing the detailed persona directive.
 */
export const getPersonaDirective = (settings: ReasoningSettings): string => {
    switch (settings.persona) {
        case 'physicist': return "Adopt the persona of a first-principles physicist. Decompose problems into their fundamental components. Emphasize causality, logical consistency, and empirical evidence. Justify steps with established physical laws or logical axioms.";
        case 'software_engineer': return "Adopt the persona of a senior software engineer. Decompose problems into modular components with clear interfaces. Emphasize robustness, scalability, and efficiency. Define clear inputs, outputs, and potential edge cases for each step. Consider dependencies and integration points.";
        case 'project_manager': return "Adopt the persona of a project manager. Decompose goals into clear deliverables, milestones, and timelines. Emphasize resource allocation, risk management, and stakeholder communication. Define success criteria in measurable terms (scope, time, budget).";
        case 'strategist': return "Adopt the persona of a business strategist. Decompose problems by analyzing the competitive landscape, market trends, and long-term implications. Emphasize opportunities, threats, and second-order effects. Frame tasks in terms of strategic advantage and ROI.";
        case 'data_scientist': return "Adopt the persona of a data scientist. Decompose problems into hypotheses that can be tested with data. Emphasize data collection, feature engineering, model selection, and validation. Define steps in terms of the scientific method and statistical rigor.";
        case 'custom': return settings.customPersonaDirective || "Adopt a neutral, objective, and analytical persona. Focus on clarity, logic, and factual accuracy without a specific professional bias.";
        case 'none':
        default: return "Adopt a neutral, objective, and analytical persona. Focus on clarity, logic, and factual accuracy without a specific professional bias.";
    }
};

/**
 * Generates a prompt for the AI to expand on the previous step of reasoning.
 * This is the "next step" generator in the depth loop.
 * @param mainGoal The overall user goal.
 * @param previousStepAnalysis The output from the last synthesized step.
 * @param settings The current reasoning settings.
 * @returns A string prompt.
 */
export const generateExpandStepPrompt = (
    mainGoal: string,
    previousStepAnalysis: string,
    settings: ReasoningSettings
): string => {
    const persona = getPersonaDirective(settings);
    return `
You are an expert reasoning agent. Your current persona is: "${persona}"

**Main Goal:**
---
${mainGoal}
---

**Analysis of Previous Step / Current Context:**
---
${previousStepAnalysis}
---

Based on the previous step's analysis, define the **next logical step** to advance towards the main goal.
Your output should be a detailed analysis for this new step. It must contain:
1.  A clear title for this step (e.g., "Step 2: Data Collection and Preprocessing").
2.  The specific actions, algorithms, or methods to be employed.
3.  Assumptions being made for this step to be successful.
4.  Potential risks or edge cases to consider for this specific step.

Do not solve the entire problem. Focus ONLY on the immediate next step. Your output should be a self-contained analysis that will be used as input for the subsequent stage in the reasoning chain.
`;
};

/**
 * Generates a prompt for the AI to critique a proposed step.
 * @param mainGoal The overall user goal.
 * @param stepToCritique The proposed step's analysis.
 * @param settings The current reasoning settings.
 * @returns A string prompt.
 */
export const generateCritiquePrompt = (
    mainGoal: string,
    stepToCritique: string,
    settings: ReasoningSettings
): string => {
    const persona = getPersonaDirective(settings);
    return `
You are an expert critic agent. Your current persona is: "${persona}"

**Main Goal:**
---
${mainGoal}
---

**Proposed Step Analysis to Critique:**
---
${stepToCritique}
---

Your task is to critically evaluate the proposed step. Be harsh but fair.
- Does it logically follow from the main goal and previous context?
- Does it overlook any obvious flaws, risks, or unstated assumptions?
- Is it too broad or too narrow in scope?
- How could the approach be improved or made more robust?
- Does it align with your persona's priorities and methods?

Provide your critique as a bulleted list of actionable feedback. Your feedback will be used to improve the step.
`;
};

/**
 * Generates a prompt for the AI to refine a step based on a critique.
 * @param mainGoal The overall user goal.
 * @param originalStep The original analysis of the step.
 * @param critique The feedback from the critique phase.
 * @param settings The current reasoning settings.
 * @returns A string prompt.
 */
export const generateRefinePrompt = (
    mainGoal: string,
    originalStep: string,
    critique: string,
    settings: ReasoningSettings
): string => {
    const persona = getPersonaDirective(settings);
    return `
You are an expert reasoning agent. Your current persona is: "${persona}"

**Main Goal:**
---
${mainGoal}
---

You previously proposed a step, and it has received the following critique.

**Original Proposed Step:**
---
${originalStep}
---

**Critique to Address:**
---
${critique}
---

Your task is to rewrite and improve the original proposed step, directly addressing all points raised in the critique.
The output must be a new, complete, and self-contained analysis for the refined step. It must have the same structure as the original (title, actions, assumptions, risks).
`;
};

/**
 * Generates a prompt for the AI to synthesize multiple alternative steps into a single, superior one.
 * @param mainGoal The overall user goal.
 * @param alternatives An array of alternative step analyses.
 * @param settings The current reasoning settings.
 * @returns A string prompt.
 */
export const generateSynthesizePrompt = (
    mainGoal: string,
    alternatives: string[],
    settings: ReasoningSettings
): string => {
    const persona = getPersonaDirective(settings);
    const alternativesText = alternatives.map((alt, i) => `
--- ALTERNATIVE ${i + 1} ---
${alt}
`).join('\n\n');

    return `
You are an expert synthesis agent. Your current persona is: "${persona}"

**Main Goal:**
---
${mainGoal}
---

You have been provided with several alternative analyses for the current reasoning step. Your task is to synthesize them into a single, superior analysis.
- Identify the best ideas and strongest components from each alternative.
- Discard weak, redundant, or contradictory points.
- Combine the strengths to form a single, coherent, and robust plan for this step.

**Alternatives to Synthesize:**
${alternativesText}
---

Provide the single, synthesized analysis below. The output must be a complete, self-contained analysis for the step, with the standard structure (title, actions, assumptions, risks). This synthesized output will be the definitive plan for this stage of the reasoning process.
`;
};

/**
 * Generates a prompt for the AI to write the final report based on the complete reasoning trace.
 * @param mainGoal The original user goal.
 * @param fullReasoningTrace A string containing the content of all nodes in the reasoning tree.
 * @param settings The current reasoning settings.
 * @returns A string prompt.
 */
export const generateFinalReportPrompt = (
    mainGoal: string,
    fullReasoningTrace: string,
    settings: ReasoningSettings
): string => {
    const persona = getPersonaDirective(settings);
    return `
You are an expert technical writer. Your current persona is: "${persona}"

**Original User Goal:**
---
${mainGoal}
---

**Full Reasoning Trace (Internal Steps):**
---
${fullReasoningTrace}
---

Your task is to write a final, polished, comprehensive report in Markdown format.
This report should directly address the user's original goal.
Use the information from the reasoning trace to structure your answer, provide justifications for your conclusions, and explain the final plan or solution.
The report should be well-organized, easy to read, and suitable for the target audience implied by your persona. Do not simply regurgitate the trace; synthesize it into a final answer.
`;
};
