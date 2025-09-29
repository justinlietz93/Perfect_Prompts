#!/usr/bin/env python3
"""
CrewAI integration example for Python prompt templates.
Demonstrates how to use prompts with CrewAI agents and crews for multi-agent workflows.
"""

import os
import sys
from typing import Dict, List, Optional

# Add the parent directory to the path to import prompt modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Note: This example shows how to integrate with CrewAI
# Install with: pip install crewai crewai-tools

try:
    from crewai import Agent, Task, Crew, Process
    from crewai.tools import BaseTool
    CREWAI_AVAILABLE = True
except ImportError:
    print("CrewAI not installed. This is a demonstration of integration patterns.")
    CREWAI_AVAILABLE = False

from agent_prompts.project_scaffolder import scaffolder_planning_prompt, scaffolder_file_prompt_generation
from agent_prompts.agent_designer import agent_designer_prompt_template
from agent_prompts.reasoner import step_by_step_reasoning_prompt
from summary_prompts.readme import chunk_summary_prompt_readme
from summary_prompts.stakeholder_map import stakeholder_mapping_prompt


class MockAgent:
    """Mock CrewAI Agent for demonstration purposes."""
    
    def __init__(self, role: str, goal: str, backstory: str, tools: List = None):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools or []

    def execute(self, task_description: str) -> str:
        return f"Mock execution by {self.role}: {task_description[:50]}..."


class MockTask:
    """Mock CrewAI Task for demonstration purposes."""
    
    def __init__(self, description: str, agent, expected_output: str = ""):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output

    def execute(self) -> str:
        return self.agent.execute(self.description)


class MockCrew:
    """Mock CrewAI Crew for demonstration purposes."""
    
    def __init__(self, agents: List, tasks: List, process=None):
        self.agents = agents
        self.tasks = tasks
        self.process = process

    def kickoff(self) -> Dict:
        results = []
        for task in self.tasks:
            result = task.execute()
            results.append(result)
        
        return {
            "final_output": "\n".join(results),
            "tasks_outputs": results
        }


# Custom tools using our prompt templates
class ProjectScaffolderTool:
    """Custom tool for project scaffolding using our prompt templates."""
    
    def __init__(self):
        self.name = "project_scaffolder"
        self.description = "Generate project scaffolding plans and file structures"

    def run(self, description: str, language: str = "python", template: str = "fastapi") -> str:
        """Execute project scaffolding."""
        settings = {
            "language": language,
            "template": template,
            "packageManager": "pip" if language == "python" else "npm",
            "license": "MIT"
        }
        
        # Generate the scaffolding prompt
        prompt = scaffolder_planning_prompt(description, settings)
        
        # In a real implementation, you'd call your AI client here
        # For demo, return the prompt structure
        return f"Generated scaffolding plan for: {description}\nLanguage: {language}\nTemplate: {template}"


class ReasoningTool:
    """Custom tool for step-by-step reasoning using our prompt templates."""
    
    def __init__(self):
        self.name = "reasoning_engine"
        self.description = "Perform step-by-step logical reasoning on complex problems"

    def run(self, problem: str) -> str:
        """Execute reasoning analysis."""
        prompt = step_by_step_reasoning_prompt(problem)
        
        # Mock reasoning response
        return f"""**Step 1: Problem Analysis**
Analyzing: {problem[:50]}...

**Step 2: Key Components**
- Identify core requirements
- Map dependencies and constraints
- Define success criteria

**Step 3: Solution Strategy**
- Break down into manageable tasks
- Prioritize by impact and complexity
- Plan implementation approach

**Step 4: Risk Assessment**
- Identify potential challenges
- Plan mitigation strategies
- Define fallback options"""


class DocumentAnalysisTool:
    """Custom tool for document analysis using our prompt templates."""
    
    def __init__(self):
        self.name = "document_analyzer"
        self.description = "Analyze documents and generate summaries, stakeholder maps, and insights"

    def run(self, document_content: str, analysis_type: str = "readme") -> str:
        """Execute document analysis."""
        if analysis_type == "readme":
            prompt = chunk_summary_prompt_readme(document_content)
            return f"Generated README analysis for {len(document_content)} characters of content"
        elif analysis_type == "stakeholders":
            prompt = stakeholder_mapping_prompt(document_content)
            return f"Identified stakeholders in document: Product Owner, Development Team, End Users, QA Team"
        else:
            return f"Unknown analysis type: {analysis_type}"


def demonstrate_single_agent_workflow():
    """Demonstrate a single agent using our prompt templates."""
    print("=== Single Agent Workflow Example ===")
    
    # Create custom tools using our prompts
    scaffolder_tool = ProjectScaffolderTool()
    reasoning_tool = ReasoningTool()
    
    if not CREWAI_AVAILABLE:
        # Mock implementation
        architect = MockAgent(
            role="Software Architect",
            goal="Design and plan software projects using best practices",
            backstory="""You are an expert software architect with 15+ years of experience.
            You specialize in clean architecture, microservices, and scalable system design.
            You use AI-powered tools to generate comprehensive project plans and analyze complex problems.""",
            tools=[scaffolder_tool, reasoning_tool]
        )
        
        task = MockTask(
            description="""Plan a new microservices-based e-commerce platform.
            Use the scaffolding tool to generate the project structure and the reasoning tool
            to analyze the architectural decisions.""",
            agent=architect,
            expected_output="A comprehensive project plan with architectural analysis"
        )
        
        result = task.execute()
        print(f"Single agent result: {result}")
        return
    
    # Real CrewAI implementation
    architect = Agent(
        role="Software Architect",
        goal="Design and plan software projects using best practices",
        backstory="""You are an expert software architect with 15+ years of experience.
        You specialize in clean architecture, microservices, and scalable system design.
        You use AI-powered tools to generate comprehensive project plans and analyze complex problems.""",
        tools=[scaffolder_tool, reasoning_tool],
        verbose=True
    )
    
    task = Task(
        description="""Plan a new microservices-based e-commerce platform.
        Use the scaffolding tool to generate the project structure and the reasoning tool
        to analyze the architectural decisions.""",
        agent=architect,
        expected_output="A comprehensive project plan with architectural analysis"
    )
    
    crew = Crew(
        agents=[architect],
        tasks=[task],
        process=Process.sequential
    )
    
    result = crew.kickoff()
    print(f"Single agent result: {result['final_output']}")


def demonstrate_multi_agent_collaboration():
    """Demonstrate multiple agents collaborating using our prompt templates."""
    print("\n=== Multi-Agent Collaboration Example ===")
    
    # Create specialized tools
    scaffolder_tool = ProjectScaffolderTool()
    reasoning_tool = ReasoningTool()
    analysis_tool = DocumentAnalysisTool()
    
    if not CREWAI_AVAILABLE:
        # Mock multi-agent setup
        architect = MockAgent(
            role="Solution Architect",
            goal="Design overall system architecture",
            backstory="Expert in system design and architecture patterns",
            tools=[scaffolder_tool, reasoning_tool]
        )
        
        analyst = MockAgent(
            role="Business Analyst",
            goal="Analyze requirements and identify stakeholders",
            backstory="Expert in business analysis and stakeholder management",
            tools=[analysis_tool]
        )
        
        technical_writer = MockAgent(
            role="Technical Writer",
            goal="Create comprehensive documentation",
            backstory="Expert in technical writing and documentation",
            tools=[analysis_tool]
        )
        
        # Mock tasks
        planning_task = MockTask(
            description="Design the architecture for a real-time chat application",
            agent=architect
        )
        
        analysis_task = MockTask(
            description="Analyze stakeholders and create business requirements document",
            agent=analyst
        )
        
        documentation_task = MockTask(
            description="Create README and technical documentation",
            agent=technical_writer
        )
        
        # Mock crew execution
        crew = MockCrew(
            agents=[architect, analyst, technical_writer],
            tasks=[planning_task, analysis_task, documentation_task]
        )
        
        result = crew.kickoff()
        print(f"Multi-agent collaboration result:\n{result['final_output']}")
        return
    
    # Real CrewAI multi-agent setup
    architect = Agent(
        role="Solution Architect", 
        goal="Design overall system architecture using clean architecture principles",
        backstory="""You are a senior solution architect with expertise in:
        - Clean Architecture and Domain-Driven Design
        - Microservices and distributed systems
        - Real-time communication systems
        - Scalable cloud architectures""",
        tools=[scaffolder_tool, reasoning_tool],
        verbose=True
    )
    
    analyst = Agent(
        role="Business Analyst",
        goal="Analyze business requirements and identify all stakeholders",
        backstory="""You are an experienced business analyst who excels at:
        - Stakeholder identification and mapping
        - Requirements gathering and analysis
        - Business process modeling
        - Risk assessment""",
        tools=[analysis_tool],
        verbose=True
    )
    
    technical_writer = Agent(
        role="Technical Writer",
        goal="Create comprehensive and user-friendly documentation",
        backstory="""You are a technical writing expert specializing in:
        - API documentation
        - Developer guides and tutorials
        - Architecture documentation
        - User manuals and README files""",
        tools=[analysis_tool],
        verbose=True
    )
    
    # Define collaborative tasks
    planning_task = Task(
        description="""Design the architecture for a real-time chat application that supports:
        - 10,000+ concurrent users
        - Message persistence and search
        - File sharing capabilities
        - Mobile and web clients
        
        Use the scaffolding tool to generate the project structure and reasoning tool
        to analyze architectural decisions.""",
        agent=architect,
        expected_output="Detailed architecture plan with project structure"
    )
    
    analysis_task = Task(
        description="""Based on the architecture plan, analyze the business requirements and:
        - Identify all stakeholders (internal and external)
        - Map their roles and responsibilities
        - Document key business requirements
        - Assess potential risks
        
        Use the document analysis tool to create stakeholder mapping.""",
        agent=analyst,
        expected_output="Comprehensive stakeholder analysis and business requirements"
    )
    
    documentation_task = Task(
        description="""Create comprehensive documentation including:
        - Project README with setup instructions
        - API documentation structure
        - Developer onboarding guide
        - Architecture overview
        
        Use the analysis from previous tasks and the document analysis tool.""",
        agent=technical_writer,
        expected_output="Complete documentation package"
    )
    
    # Create crew with sequential process
    crew = Crew(
        agents=[architect, analyst, technical_writer],
        tasks=[planning_task, analysis_task, documentation_task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    print(f"Multi-agent collaboration result:\n{result['final_output']}")


def demonstrate_hierarchical_workflow():
    """Demonstrate hierarchical workflow with manager and worker agents."""
    print("\n=== Hierarchical Workflow Example ===")
    
    if not CREWAI_AVAILABLE:
        # Mock hierarchical setup
        manager = MockAgent(
            role="Project Manager",
            goal="Coordinate development workflow and ensure quality",
            backstory="Experienced project manager with technical background"
        )
        
        senior_dev = MockAgent(
            role="Senior Developer",
            goal="Lead technical implementation",
            backstory="Senior developer with full-stack expertise"
        )
        
        junior_dev = MockAgent(
            role="Junior Developer", 
            goal="Implement features under guidance",
            backstory="Junior developer eager to learn and contribute"
        )
        
        tasks = [
            MockTask("Plan development phases", manager),
            MockTask("Design core architecture", senior_dev),
            MockTask("Implement basic features", junior_dev)
        ]
        
        crew = MockCrew(
            agents=[manager, senior_dev, junior_dev],
            tasks=tasks
        )
        
        result = crew.kickoff()
        print(f"Hierarchical workflow result:\n{result['final_output']}")
        return
    
    # Real hierarchical workflow (would require CrewAI Pro for hierarchical process)
    print("Hierarchical workflow would require CrewAI Pro - showing sequential alternative")
    
    manager = Agent(
        role="Engineering Manager",
        goal="Coordinate the development team and ensure project success",
        backstory="""You are an experienced engineering manager who:
        - Coordinates cross-functional teams
        - Ensures code quality and best practices
        - Manages project timelines and deliverables
        - Mentors junior developers""",
        verbose=True
    )
    
    # This would be set up as a hierarchical process in CrewAI Pro
    coordination_task = Task(
        description="""Coordinate the development of a new feature:
        1. Break down the requirements into tasks
        2. Assign appropriate team members
        3. Set milestones and deadlines
        4. Define quality criteria
        
        Use reasoning to plan the optimal workflow.""",
        agent=manager,
        expected_output="Detailed project coordination plan"
    )
    
    crew = Crew(
        agents=[manager],
        tasks=[coordination_task],
        process=Process.sequential
    )
    
    result = crew.kickoff()
    print(f"Coordination result: {result['final_output']}")


def demonstrate_custom_agent_design():
    """Demonstrate using our agent designer prompt to create new agents."""
    print("\n=== Custom Agent Design Example ===")
    
    # Use our agent designer prompt template
    settings = {
        "systemType": "multiAgent",
        "goal": "Build a comprehensive software development workflow",
        "trigger": "new_project_request",
        "provider": "openai",
        "capabilities": {
            "web_search": True,
            "file_io": True,
            "code_execution": True,
            "email": False
        }
    }
    
    design_prompt = agent_designer_prompt_template(settings)
    
    print("Generated agent design prompt:")
    print(f"Prompt length: {len(design_prompt)} characters")
    print(f"System type: {settings['systemType']}")
    print(f"Goal: {settings['goal']}")
    print(f"Capabilities: {list(settings['capabilities'].keys())}")
    
    # In a real scenario, you would:
    # 1. Send this prompt to your AI provider
    # 2. Get back a comprehensive agent design
    # 3. Use that design to configure your CrewAI agents
    
    print("\nThis prompt would generate:")
    print("- Detailed agent role definitions")
    print("- Tool specifications")
    print("- Workflow diagrams")
    print("- Communication patterns")


def main():
    """Run all CrewAI integration examples."""
    print("Python Prompt Templates - CrewAI Integration Examples")
    print("=" * 60)
    
    if not CREWAI_AVAILABLE:
        print("Note: CrewAI not installed. Showing integration patterns with mocks.")
        print("Install with: pip install crewai crewai-tools")
        print()
    
    demonstrate_single_agent_workflow()
    demonstrate_multi_agent_collaboration()
    demonstrate_hierarchical_workflow()
    demonstrate_custom_agent_design()
    
    print("=" * 60)
    print("CrewAI integration examples completed!")
    
    if not CREWAI_AVAILABLE:
        print("\nTo run with real CrewAI:")
        print("1. pip install crewai crewai-tools")
        print("2. Set OPENAI_API_KEY environment variable")
        print("3. Run this script again")


if __name__ == "__main__":
    main()