from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class AgentDesignerSettings:
    system_type: str
    goal: str
    trigger: str
    provider: str
    capabilities: Dict[str, bool]

def agent_designer_prompt_template(settings: AgentDesignerSettings) -> str:
    """Generate a comprehensive agent design prompt based on settings."""
    is_single_agent = settings.system_type == "singleAgent"
    
    persona = ("You are an expert AI Architect and Fine-Tuning Specialist. Your task is to design a robust, high-performing single agent system, including plans for fine-tuning and data curation."
               if is_single_agent else
               "You are an expert multi-agent systems architect. Your task is to design a robust and scalable agentic system based on a user's high-level goal and provided configuration.")

    design_principles = ("""
**DESIGN PRINCIPLES TO FOLLOW:**
1.  **Clarity of Purpose:** The agent's prompt must define a clear role, capabilities, and constraints.
2.  **Tooling:** Define specific, atomic tools the agent can use to accomplish its goal.
3.  **Fine-Tuning Strategy:** The fine-tuning plan must be actionable and tailored to the agent's goal.
4.  **Data Curation:** The data plan must be practical and lead to a high-quality dataset."""
                        if is_single_agent else
                        """
**DESIGN PRINCIPLES TO FOLLOW:**
1.  **Modularity:** Decompose the system into distinct agents with clear responsibilities (e.g., a Router Agent, a Research Agent, a Writing Agent).
2.  **Tooling:** Define specific, atomic tools that agents can use (e.g., `web_search`, `read_file`, `send_email`).
3.  **State Management:** Consider how the state of a task is maintained and passed between agents.
4.  **Control Flow:** Design a clear control flow, often orchestrated by a primary agent or router.
5.  **Error Handling:** Include concepts for handling failed tasks or tool executions.""")

    if is_single_agent:
        pipeline = f"""
**PIPELINE TO SIMULATE:**
1.  **Analyze Goal:** Deconstruct the user's goal: "{settings.goal}".
2.  **Define Core Agent:** Design the primary agent's prompt template and necessary tools based on user-selected capabilities.
3.  **Create Fine-Tuning Plan:** Detail the strategy for fine-tuning the base model to specialize it for the task. Include data requirements, size, and evaluation methods.
4.  **Create Data Curation Plan:** Describe how to source, clean, and format the data required for the fine-tuning dataset.
5.  **Map Process Flow:** Create a simple Mermaid diagram illustrating the agent's primary action loop (e.g., receive trigger, use tools, produce output).
6.  **Synthesize Artifacts:**
    *   **designMarkdown:** Write a comprehensive overview of the agent, its tools, and the detailed fine-tuning and data curation plans in the `<DESIGN_MD>` block.
    *   **designPlanJson:** Populate the detailed JSON structure in the `<DESIGN_PLAN_JSON>` block.
    *   **designFlowDiagram:** Create the Mermaid.js `graph TD` that visually represents the agent's process in the `<DESIGN_FLOW_DIAGRAM>` block."""
    else:
        caps = settings.capabilities
        pipeline = f"""
**PIPELINE TO SIMULATE:**
1.  **Analyze Goal:** Deconstruct the user's goal: "{settings.goal}".
2.  **Select Architecture:** Choose a suitable architecture (e.g., Router-Worker, Hierarchical, Broadcast) based on the goal.
3.  **Define Agents & Tools:**
    *   Define the necessary agents and their specific roles/prompts.
    *   Define the tools required to accomplish the goal, especially considering the user-selected capabilities: Web Search ({caps.get('webSearch', False)}), Email ({caps.get('emailAccess', False)}), File I/O ({caps.get('fileIO', False)}), Code Execution ({caps.get('codeExecution', False)}).
4.  **Map Process Flow:** Chart the sequence of operations, agent interactions, and tool usage from trigger to completion.
5.  **Synthesize Artifacts:**
    *   **designMarkdown:** Write a comprehensive overview of the system design in the `<DESIGN_MD>` block.
    *   **designPlanJson:** Populate the detailed JSON structure in the `<DESIGN_PLAN_JSON>` block.
    *   **designFlowDiagram:** Create a Mermaid.js `graph TD` that visually represents the process flow in the `<DESIGN_FLOW_DIAGRAM>` block."""

    return f"""
{persona}
You must generate a comprehensive design document consisting of three distinct blocks: a Markdown overview, a Mermaid.js process flow diagram, and a structured JSON plan.

**OUTPUT REQUIREMENTS:**
Your final output MUST contain three distinct, clearly separated blocks with the following XML-style tags:
1.  A `<DESIGN_MD>` block containing the full, raw, enhanced Markdown text for the design overview.
2.  A `<DESIGN_FLOW_DIAGRAM>` block containing only the raw Mermaid.js code for the diagram.
3.  A `<DESIGN_PLAN_JSON>` block containing a single, valid, parsable JSON object for the structured plan.

**CRITICAL JSON FORMATTING RULE:** The JSON block must be perfectly valid. All string values within the JSON must be correctly escaped (e.g., newlines as \\n, quotes as \\", backslashes as \\\\).

{design_principles}

{pipeline}

---
**USER CONFIGURATION:**
- **Goal:** {settings.goal}
- **System Type:** {settings.system_type}
- **Provider:** {settings.provider}
- **Trigger:** {settings.trigger}
---
**FINAL REMINDER:** Your entire response must be wrapped in the specified blocks in the correct order: `<DESIGN_MD>`, then `<DESIGN_FLOW_DIAGRAM>`, then `<DESIGN_PLAN_JSON>`. Do not add any other text, explanations, or apologies.
Begin generation now.
"""