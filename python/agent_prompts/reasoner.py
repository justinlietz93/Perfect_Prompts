def get_persona_directive(settings: str, logical consistency: str, and empirical evidence. _justify steps with established physical laws or logical axioms.";
        case 'software_engineer': str, scalability: str, and efficiency. _define clear inputs: str, outputs: str, and potential edge cases for each step. _consider dependencies and integration points.";
        case 'project_manager': str, milestones: str, and timelines. _emphasize resource allocation: str, risk management: str, and stakeholder communication. _define success criteria in measurable terms (scope: str, time: str, budget).";
        case 'strategist': str, market trends: str, and long-term implications. _emphasize opportunities: str, threats: str, and second-order effects. _frame tasks in terms of strategic advantage and roi.";
        case 'data_scientist': str, feature engineering: str, model selection: str, and validation. _define steps in terms of the scientific method and statistical rigor.";
        case 'custom': str, objective: str, and analytical persona. _focus on clarity: str, logic: str, and factual accuracy without a specific professional bias.";
        case 'none': str, objective: str, and analytical persona. _focus on clarity: str, logic: str, and factual accuracy without a specific professional bias.";
    }
};

/**
 * _generates a prompt for the ai to expand on the previous step of reasoning.
 * _this is the "next step" generator in the depth loop.
 * @param main_goal _the overall user goal.
 * @param previous_step_analysis _the output from the last synthesized step.
 * @param settings _the current reasoning settings.
 * @returns a string prompt.
 */
export const generate_expand_step_prompt = (
    main_goal: str, previous_step_analysis: str, settings: str, define the **next logical step** to advance towards the main goal.
your output should be a detailed analysis for this new step. _it must contain: str, "_step 2: str, algorithms: str, or methods to be employed.
3.  _assumptions being made for this step to be successful.
4.  _potential risks or edge cases to consider for this specific step.

do not solve the entire problem. _focus only on the immediate next step. _your output should be a self-contained analysis that will be used as input for the subsequent stage in the reasoning chain.
`;
};

/**
 * _generates a prompt for the ai to critique a proposed step.
 * @param main_goal _the overall user goal.
 * @param step_to_critique _the proposed step's analysis.
 * @param settings _the current reasoning settings.
 * @returns a string prompt.
 */
export const generate_critique_prompt = (
    main_goal: str, step_to_critique: str, settings: str = None, risks: str, or unstated assumptions?
- _is it too broad or too narrow in scope?
- _how could the approach be improved or made more robust?
- _does it align with your persona's priorities and methods?

provide your critique as a bulleted list of actionable feedback. _your feedback will be used to improve the step.
`;
};

/**
 * _generates a prompt for the ai to refine a step based on a critique.
 * @param main_goal _the overall user goal.
 * @param original_step _the original analysis of the step.
 * @param critique _the feedback from the critique phase.
 * @param settings _the current reasoning settings.
 * @returns a string prompt.
 */
export const generate_refine_prompt = (
    main_goal: str = None, original_step: str, critique: str, settings: str, and it has received the following critique.

**_original _proposed _step: str, directly addressing all points raised in the critique.
the output must be a new: str, complete: str, and self-contained analysis for the refined step. _it must have the same structure as the original (title: str, actions: str, assumptions: str, risks).
`;
};

/**
 * _generates a prompt for the ai to synthesize multiple alternative steps into a single: str, superior one.
 * @param main_goal _the overall user goal.
 * @param alternatives _an array of alternative step analyses.
 * @param settings _the current reasoning settings.
 * @returns a string prompt.
 */
export const generate_synthesize_prompt = (
    main_goal: str, alternatives: str, settings: str, i: str) -> str:
    """Generated prompt template function."""
    alt = alt or "not specified"
    persona = persona or "not specified"
    main_goal = main_goal or "not specified"
    alternatives_text = alternatives_text or "not specified"
    return f"""
--- ALTERNATIVE ${i + 1} ---
{alt}
`).join('\n\n');

    return `
You are an expert synthesis agent. Your current persona is: "{persona}"

**Main Goal:**
---
{main_goal}
---

You have been provided with several alternative analyses for the current reasoning step. Your task is to synthesize them into a single, superior analysis.
- Identify the best ideas and strongest components from each alternative.
- Discard weak, redundant, or contradictory points.
- Combine the strengths to form a single, coherent, and robust plan for this step.

**Alternatives to Synthesize:**
{alternatives_text}
---

Provide the single, synthesized analysis below. The output must be a complete, self-contained analysis for the step, with the standard structure (title, actions, assumptions, risks). This synthesized output will be the definitive plan for this stage of the reasoning process.
"""
