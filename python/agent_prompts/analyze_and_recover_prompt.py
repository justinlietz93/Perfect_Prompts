analyze_and_recover_prompt = """# Placeholder for Analyze and Recover Prompt

**Context:**
The agent encountered an error or unexpected situation during autonomous operation.

**Input:**
- Current Task Goal: {{ task_goal }}
- Agent State (relevant parts): {{ agent_state }}
- Error/Situation Details: {{ error_details }}
- Recent Action History: {{ action_history }}
- Current Plan State (if available): {{ plan_state }}

**Objective:**
Analyze the situation, identify the root cause, and propose concrete recovery steps or a revised plan to achieve the original task goal. The recovery steps should be actionable by the agent (e.g., retry a tool with different parameters, revise the last instruction, ask the user for clarification if truly stuck).

**Output Format:**
Provide the analysis and recovery plan in a structured format (e.g., JSON or YAML) that the agent can parse.

Example Output Structure (JSON):
```json
{
  "analysis": "Brief analysis of the root cause.",
  "recovery_strategy": "Description of the overall recovery approach.",
  "next_actions": [
    {
      "type": "tool_use | instruction | clarification_request",
      "details": {
        // Specific parameters for the action
      }
    }
    // ... potentially more actions
  ],
  "confidence_score": 0.8 // Optional: Confidence in the recovery plan
}
```

**Instructions:**
1.  Thoroughly analyze the provided context and error details.
2.  Determine the most likely root cause.
3.  Formulate a recovery plan focused on achieving the `task_goal`.
4.  Prioritize actions that the agent can perform autonomously.
5.  If recovery seems impossible or requires external intervention, suggest requesting user clarification as the next action.
6.  Output the result in the specified structured format."""
