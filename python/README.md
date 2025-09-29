# Python Prompt Templates

This directory contains Python implementations of prompt templates designed for agentic AI systems. These templates provide structured, reusable prompts for various AI-assisted development and analysis tasks.

## Overview

The Python prompt templates are organized into two main categories:

### 🤖 Agent Prompts (`agent_prompts/`)
Specialized prompts for AI agents that perform specific development and analysis tasks:

- **`project_scaffolder.py`** - Generate project structures using Hybrid-Clean architecture
- **`agent_designer.py`** - Design single-agent and multi-agent AI systems  
- **`mermaid_designer.py`** - Create and fix Mermaid.js diagrams from specifications
- **`prompt_enhancer.py`** - Improve and optimize existing prompts
- **`reasoner.py`** - Perform step-by-step logical reasoning
- **`rewriter.py`** - Rewrite content with specific styles and requirements
- **`citations.py`** - Generate proper citations and references
- **`math_formatter.py`** - Format mathematical expressions and equations
- **`style_extractor.py`** - Extract and analyze writing styles
- **`highlight_extraction.py`** - Extract key highlights from content
- **`next_steps.py`** - Generate actionable next steps from analysis
- **`request_splitter.py`** - Break down complex requests into manageable tasks

### 📊 Summary Prompts (`summary_prompts/`)
Templates for analyzing, summarizing, and structuring content:

- **`readme.py`** - Generate comprehensive README documentation
- **`summarize.py`** - Create concise summaries of complex content
- **`checklist.py`** - Convert content into actionable checklists
- **`timeline.py`** - Extract and organize temporal information
- **`process_flow.py`** - Document step-by-step processes
- **`stakeholder_map.py`** - Identify and map project stakeholders
- **`risk_register.py`** - Identify and assess project risks
- **`decision_matrix.py`** - Structure decision-making processes
- **`swot_analysis.py`** - Perform SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis
- **`entity_relationship_digest.py`** - Extract entity relationships from content
- **`system_walkthrough.py`** - Generate system documentation and walkthroughs

## Usage in Agentic Projects

### Basic Usage Pattern

```python
from python.agent_prompts.project_scaffolder import scaffolder_planning_prompt
from python.summary_prompts.readme import chunk_summary_prompt_readme

# Generate a project scaffolding prompt
project_description = "Build a REST API for task management"
settings = {"language": "python", "template": "fastapi", "packageManager": "pip"}
scaffold_prompt = scaffolder_planning_prompt(project_description, settings)

# Use with your AI client
response = ai_client.complete(scaffold_prompt)
```

### Integration with AI Frameworks

#### LangChain Integration
```python
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from python.agent_prompts.reasoner import step_by_step_reasoning_prompt

# Create LangChain prompt template
reasoning_template = PromptTemplate(
    input_variables=["problem"],
    template=step_by_step_reasoning_prompt("{problem}")
)

# Use with LangChain chain
llm = OpenAI()
chain = reasoning_template | llm
result = chain.invoke({"problem": "Design a scalable microservices architecture"})
```

#### CrewAI Integration
```python
from crewai import Agent, Task, Crew
from python.agent_prompts.agent_designer import agent_designer_prompt_template

# Create specialized agent
architect_agent = Agent(
    role="Software Architect",
    goal="Design robust system architectures",
    backstory="Expert in system design and architecture patterns",
    tools=[web_search_tool, file_tool]
)

# Create task using prompt template
design_task = Task(
    description=agent_designer_prompt_template({
        "systemType": "multiAgent",
        "goal": "Design a document processing system"
    }),
    agent=architect_agent
)
```

### Workflow Examples

#### Document Analysis Pipeline
```python
from python.summary_prompts.readme import chunk_summary_prompt_readme, reduce_summaries_prompt_readme
from python.summary_prompts.stakeholder_map import stakeholder_mapping_prompt

def analyze_project_document(document_text):
    # Step 1: Chunk and summarize
    chunks = split_document(document_text)
    summaries = []
    
    for chunk in chunks:
        summary_prompt = chunk_summary_prompt_readme(chunk)
        summary = ai_client.complete(summary_prompt)
        summaries.append(summary)
    
    # Step 2: Reduce summaries
    combined_summaries = "\n\n".join(summaries)
    final_readme_prompt = reduce_summaries_prompt_readme(combined_summaries)
    final_readme = ai_client.complete(final_readme_prompt)
    
    # Step 3: Extract stakeholders
    stakeholder_prompt = stakeholder_mapping_prompt(document_text)
    stakeholders = ai_client.complete(stakeholder_prompt)
    
    return {
        "readme": final_readme,
        "stakeholders": stakeholders
    }
```

#### Project Scaffolding Workflow
```python
from python.agent_prompts.project_scaffolder import (
    scaffolder_planning_prompt,
    scaffolder_file_prompt_generation
)

def scaffold_project(description, settings):
    # Step 1: Generate project plan
    planning_prompt = scaffolder_planning_prompt(description, settings)
    project_plan = ai_client.complete(planning_prompt)
    plan_json = json.loads(project_plan)
    
    # Step 2: Generate file prompts
    file_prompts = {}
    for file_item in plan_json["tree"]:
        file_prompt = scaffolder_file_prompt_generation(
            json.dumps(plan_json["project"]), 
            json.dumps(file_item)
        )
        file_prompts[file_item["path"]] = file_prompt
    
    return {
        "plan": plan_json,
        "file_prompts": file_prompts
    }
```

## Best Practices

### 1. **Prompt Composition**
Combine multiple prompts for complex workflows:
```python
# Chain prompts for comprehensive analysis
analysis = reasoner_prompt(data) → summary_prompt(analysis) → next_steps_prompt(summary)
```

### 2. **Error Handling**
Always validate AI responses, especially for structured outputs:
```python
try:
    result = json.loads(ai_response)
    validate_schema(result)
except (json.JSONDecodeError, ValidationError) as e:
    # Retry with corrected prompt or fallback logic
    pass
```

### 3. **Template Customization**
Extend base templates for specific use cases:
```python
def custom_scaffolder_prompt(description, settings, custom_constraints):
    base_prompt = scaffolder_planning_prompt(description, settings)
    return f"{base_prompt}\n\nAdditional Constraints:\n{custom_constraints}"
```

### 4. **Async Processing**
Use async patterns for better performance:
```python
import asyncio

async def process_multiple_prompts(prompts):
    tasks = [ai_client.complete_async(prompt) for prompt in prompts]
    return await asyncio.gather(*tasks)
```

## Integration Examples

See the `examples/` directory for complete, runnable examples demonstrating:
- LangChain integration patterns
- CrewAI agent workflows  
- FastAPI web service integration
- Jupyter notebook analysis workflows
- Async processing patterns

## Dependencies

Most prompt templates are dependency-free, but integration examples may require:
- `langchain` - For LangChain integration
- `crewai` - For CrewAI workflows
- `openai` - For OpenAI API integration
- `anthropic` - For Anthropic Claude integration
- `fastapi` - For web service examples

## Contributing

When adding new prompt templates:
1. Follow the existing function signature patterns
2. Include comprehensive docstrings
3. Add usage examples in the `examples/` directory
4. Ensure prompts are language-agnostic where possible
5. Test with multiple AI providers for compatibility

## Related Resources

- [Architecture Standards](../STANDARDS_REPOSITORY/) - Comprehensive architectural guidelines
- [General Guidelines](../general_guidelines/) - Cross-language development practices
- [Main Repository README](../README.md) - Overall project documentation