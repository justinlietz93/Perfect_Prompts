package agent_prompts

import "fmt"

// GetPersonaDirective generates a prompt template
func GetPersonaDirective(settings string, logical consistency string, and empirical evidence. _justify steps with established physical laws or logical axioms.";
        case 'software_engineer' string, scalability string, and efficiency. _define clear inputs string, outputs string, and potential edge cases for each step. _consider dependencies and integration points.";
        case 'project_manager' string, milestones string, and timelines. _emphasize resource allocation string, risk management string, and stakeholder communication. _define success criteria in measurable terms (scope string, time string, budget).";
        case 'strategist' string, market trends string, and long-term implications. _emphasize opportunities string, threats string, and second-order effects. _frame tasks in terms of strategic advantage and roi.";
        case 'data_scientist' string, feature engineering string, model selection string, and validation. _define steps in terms of the scientific method and statistical rigor.";
        case 'custom' string, objective string, and analytical persona. _focus on clarity string, logic string, and factual accuracy without a specific professional bias.";
        case 'none' string, objective string, and analytical persona. _focus on clarity string, logic string, and factual accuracy without a specific professional bias.";
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
    main_goal string, previous_step_analysis string, settings string, define the **next logical step** to advance towards the main goal.
your output should be a detailed analysis for this new step. _it must contain string, "_step 2 string, algorithms string, or methods to be employed.
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
    main_goal string, step_to_critique string, settings *string, risks string, or unstated assumptions?
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
    main_goal *string, original_step string, critique string, settings string, and it has received the following critique.

**_original _proposed _step string, directly addressing all points raised in the critique.
the output must be a new string, complete string, and self-contained analysis for the refined step. _it must have the same structure as the original (title string, actions string, assumptions string, risks).
`;
};

/**
 * _generates a prompt for the ai to synthesize multiple alternative steps into a single string, superior one.
 * @param main_goal _the overall user goal.
 * @param alternatives _an array of alternative step analyses.
 * @param settings _the current reasoning settings.
 * @returns a string prompt.
 */
export const generate_synthesize_prompt = (
    main_goal string, alternatives string, settings string, i string) string {
	alt_val := "not specified"
	if alt != nil {
		alt_val = *alt
	}

	persona_val := "not specified"
	if persona != nil {
		persona_val = *persona
	}

	main_goal_val := "not specified"
	if main_goal != nil {
		main_goal_val = *main_goal
	}

	alternatives_text_val := "not specified"
	if alternatives_text != nil {
		alternatives_text_val = *alternatives_text
	}

	return fmt.Sprintf(`
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
`, alt_val, persona_val, main_goal_val, alternatives_text_val)
}
