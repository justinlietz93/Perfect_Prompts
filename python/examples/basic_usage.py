#!/usr/bin/env python3
"""
Basic usage examples for Python prompt templates.
Demonstrates fundamental patterns for integrating prompts with AI clients.
"""

import json
import asyncio
from typing import Dict, List, Optional
import sys
import os

# Add the parent directory to the path to import prompt modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from agent_prompts.project_scaffolder import scaffolder_planning_prompt, scaffolder_file_prompt_generation
from agent_prompts.reasoner import step_by_step_reasoning_prompt
from summary_prompts.readme import chunk_summary_prompt_readme, reduce_summaries_prompt_readme
from summary_prompts.stakeholder_map import stakeholder_mapping_prompt


class MockAIClient:
    """Mock AI client for demonstration purposes."""
    
    def __init__(self):
        self.call_count = 0
    
    def complete(self, prompt: str) -> str:
        """Simulate AI completion with mock responses."""
        self.call_count += 1
        
        if "project plan" in prompt.lower():
            return self._mock_project_plan()
        elif "step-by-step" in prompt.lower():
            return self._mock_reasoning_response()
        elif "stakeholder" in prompt.lower():
            return self._mock_stakeholder_response()
        else:
            return f"Mock response {self.call_count} for prompt: {prompt[:50]}..."
    
    def _mock_project_plan(self) -> str:
        return json.dumps({
            "project": {
                "name": "TaskManagerAPI",
                "language": "python",
                "template": "fastapi",
                "package_manager": "pip",
                "license": "MIT"
            },
            "layers": ["presentation", "application", "domain", "infrastructure", "shared", "tests"],
            "tree": [
                {
                    "path": "src/presentation/api/task_controller.py",
                    "layer": "presentation",
                    "purpose": "REST API endpoints for task management",
                    "prompt": ""
                },
                {
                    "path": "src/application/services/task_service.py",
                    "layer": "application",
                    "purpose": "Business logic for task operations",
                    "prompt": ""
                }
            ]
        })
    
    def _mock_reasoning_response(self) -> str:
        return """
**Step 1: Problem Analysis**
The challenge is to design a scalable microservices architecture.

**Step 2: Key Requirements**
- Service independence
- Data consistency
- Communication patterns
- Fault tolerance

**Step 3: Solution Approach**
Use event-driven architecture with:
- API Gateway for routing
- Service mesh for communication
- Event sourcing for data consistency
- Circuit breakers for resilience

**Step 4: Implementation Strategy**
1. Start with domain decomposition
2. Define service boundaries
3. Implement async messaging
4. Add monitoring and observability
"""
    
    def _mock_stakeholder_response(self) -> str:
        return """
## Project Stakeholders

### Primary Stakeholders
- **Product Owner**: Defines requirements and priorities
- **Development Team**: Implements the solution
- **End Users**: Will use the task management system

### Secondary Stakeholders  
- **DevOps Team**: Manages deployment and infrastructure
- **QA Team**: Ensures quality and testing
- **Security Team**: Reviews security requirements

### External Stakeholders
- **Customers**: Provide feedback and requirements
- **Compliance Team**: Ensures regulatory compliance
"""


def demonstrate_basic_scaffolding():
    """Demonstrate basic project scaffolding workflow."""
    print("=== Project Scaffolding Example ===")
    
    ai_client = MockAIClient()
    
    # Step 1: Generate project plan
    description = "Build a REST API for task management with user authentication"
    settings = {
        "language": "python",
        "template": "fastapi", 
        "packageManager": "pip",
        "license": "MIT"
    }
    
    planning_prompt = scaffolder_planning_prompt(description, settings)
    print(f"Generated planning prompt ({len(planning_prompt)} chars)")
    
    # Get project plan from AI
    plan_response = ai_client.complete(planning_prompt)
    plan = json.loads(plan_response)
    
    print(f"Project: {plan['project']['name']}")
    print(f"Files to generate: {len(plan['tree'])}")
    
    # Step 2: Generate file prompts
    file_prompts = {}
    for file_item in plan['tree']:
        project_context = json.dumps(plan['project'])
        file_context = json.dumps(file_item)
        
        file_prompt = scaffolder_file_prompt_generation(project_context, file_context)
        file_prompts[file_item['path']] = file_prompt
        print(f"  Generated prompt for: {file_item['path']}")
    
    print(f"Total prompts generated: {len(file_prompts)}")


def demonstrate_reasoning_workflow():
    """Demonstrate step-by-step reasoning."""
    print("\n=== Reasoning Workflow Example ===")
    
    ai_client = MockAIClient()
    
    problem = "How can we design a scalable microservices architecture for a high-traffic e-commerce platform?"
    
    reasoning_prompt = step_by_step_reasoning_prompt(problem)
    print(f"Generated reasoning prompt ({len(reasoning_prompt)} chars)")
    
    reasoning_result = ai_client.complete(reasoning_prompt)
    print("Reasoning Result:")
    print(reasoning_result)


def demonstrate_document_analysis_pipeline():
    """Demonstrate document analysis and README generation."""
    print("\n=== Document Analysis Pipeline ===")
    
    ai_client = MockAIClient()
    
    # Sample document content
    document_content = """
    Project Vision: TaskFlow Pro
    
    TaskFlow Pro is a next-generation task management platform designed for distributed teams.
    The system will support real-time collaboration, advanced analytics, and seamless integration
    with popular development tools.
    
    Key Features:
    - Real-time task updates and notifications
    - Kanban and Gantt chart visualizations  
    - Integration with GitHub, Slack, and Jira
    - Advanced reporting and analytics
    - Mobile and desktop applications
    
    Technical Requirements:
    - Cloud-native architecture on AWS
    - Microservices with containerization
    - Real-time WebSocket connections
    - PostgreSQL for primary data storage
    - Redis for caching and session management
    """
    
    # Step 1: Generate README content
    readme_prompt = chunk_summary_prompt_readme(document_content)
    readme_section = ai_client.complete(readme_prompt)
    
    # Step 2: Perform stakeholder analysis
    stakeholder_prompt = stakeholder_mapping_prompt(document_content)
    stakeholder_analysis = ai_client.complete(stakeholder_prompt)
    
    print("Generated README Section:")
    print(readme_section[:200] + "...")
    print("\nStakeholder Analysis:")
    print(stakeholder_analysis[:200] + "...")


def demonstrate_error_handling():
    """Demonstrate proper error handling patterns."""
    print("\n=== Error Handling Example ===")
    
    class FailingAIClient:
        def complete(self, prompt: str) -> str:
            raise Exception("API rate limit exceeded")
    
    def safe_prompt_execution(client, prompt: str, max_retries: int = 3) -> Optional[str]:
        """Execute prompt with retry logic."""
        for attempt in range(max_retries):
            try:
                return client.complete(prompt)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    print("All attempts failed")
                    return None
        return None
    
    failing_client = FailingAIClient()
    prompt = step_by_step_reasoning_prompt("Test problem")
    
    result = safe_prompt_execution(failing_client, prompt)
    print(f"Result with error handling: {result}")


async def demonstrate_async_processing():
    """Demonstrate async processing of multiple prompts."""
    print("\n=== Async Processing Example ===")
    
    class AsyncMockClient:
        async def complete_async(self, prompt: str) -> str:
            # Simulate network delay
            await asyncio.sleep(0.1)
            return f"Async response for: {prompt[:30]}..."
    
    client = AsyncMockClient()
    
    # Multiple prompts to process concurrently
    prompts = [
        step_by_step_reasoning_prompt("Problem 1"),
        step_by_step_reasoning_prompt("Problem 2"), 
        step_by_step_reasoning_prompt("Problem 3"),
    ]
    
    # Process concurrently
    tasks = [client.complete_async(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result}")


def main():
    """Run all demonstration examples."""
    print("Python Prompt Templates - Basic Usage Examples")
    print("=" * 50)
    
    demonstrate_basic_scaffolding()
    demonstrate_reasoning_workflow()
    demonstrate_document_analysis_pipeline()
    demonstrate_error_handling()
    
    # Run async example
    asyncio.run(demonstrate_async_processing())
    
    print("\n" + "=" * 50)
    print("All examples completed successfully!")


if __name__ == "__main__":
    main()