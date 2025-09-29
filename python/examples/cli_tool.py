#!/usr/bin/env python3
"""
CLI tool example using Python prompt templates.
Demonstrates how to build a command-line interface for AI-powered development tasks.

Usage:
    python cli_tool.py scaffold --description "Build a REST API" --language python
    python cli_tool.py analyze --problem "How to scale databases?" --type reasoning
    python cli_tool.py document --file input.txt --output readme
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging

# Add the parent directory to the path to import prompt modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from agent_prompts.project_scaffolder import scaffolder_planning_prompt, scaffolder_file_prompt_generation
from agent_prompts.reasoner import step_by_step_reasoning_prompt
from summary_prompts.readme import chunk_summary_prompt_readme, reduce_summaries_prompt_readme
from summary_prompts.stakeholder_map import stakeholder_mapping_prompt

# Mock AI client for demonstration
class MockAIClient:
    def __init__(self, delay: float = 0.5):
        self.delay = delay
        self.call_count = 0

    async def complete_async(self, prompt: str) -> str:
        """Async completion for better CLI responsiveness."""
        await asyncio.sleep(self.delay)
        self.call_count += 1
        
        if "project plan" in prompt.lower():
            return self._mock_project_plan()
        elif "step-by-step" in prompt.lower():
            return self._mock_reasoning_response()
        elif "stakeholder" in prompt.lower():
            return self._mock_stakeholder_response()
        elif "readme" in prompt.lower():
            return self._mock_readme_response()
        else:
            return f"Mock response {self.call_count} for prompt: {prompt[:50]}..."

    def complete(self, prompt: str) -> str:
        """Sync wrapper for async completion."""
        return asyncio.run(self.complete_async(prompt))

    def _mock_project_plan(self) -> str:
        return json.dumps({
            "project": {
                "name": "CLIGeneratedProject",
                "language": "python",
                "template": "fastapi",
                "package_manager": "pip",
                "license": "MIT"
            },
            "layers": ["presentation", "application", "domain", "infrastructure", "shared", "tests"],
            "tree": [
                {
                    "path": "src/presentation/api/main.py",
                    "layer": "presentation",
                    "purpose": "FastAPI application entry point",
                    "prompt": ""
                },
                {
                    "path": "src/application/services/user_service.py",
                    "layer": "application",
                    "purpose": "User business logic",
                    "prompt": ""
                }
            ]
        }, indent=2)

    def _mock_reasoning_response(self) -> str:
        return """**Step 1: Problem Analysis**
Identify the core challenge and constraints.

**Step 2: Solution Design**
Break down the problem into manageable components.

**Step 3: Implementation Strategy**
Define the approach and technology choices.

**Step 4: Validation Plan**
Establish criteria for success and testing."""

    def _mock_stakeholder_response(self) -> str:
        return """## Stakeholder Analysis

### Primary Stakeholders
- **Development Team**: Responsible for implementation
- **Product Owner**: Defines requirements and priorities
- **End Users**: Will interact with the final product

### Secondary Stakeholders
- **QA Team**: Ensures quality standards
- **DevOps Team**: Manages deployment and infrastructure
- **Security Team**: Reviews security requirements"""

    def _mock_readme_response(self) -> str:
        return """# Generated Project

## Overview
This project was generated using AI-powered scaffolding tools.

## Features
- Modern architecture patterns
- Comprehensive testing
- Documentation generation
- CI/CD integration

## Getting Started
1. Install dependencies
2. Configure environment
3. Run the application"""


class ProgressIndicator:
    """Simple progress indicator for CLI operations."""
    
    def __init__(self, message: str):
        self.message = message
        self.running = False
        
    async def __aenter__(self):
        self.running = True
        print(f"{self.message}...", end="", flush=True)
        asyncio.create_task(self._animate())
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.running = False
        if exc_type is None:
            print(" ✓")
        else:
            print(" ✗")
            
    async def _animate(self):
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        i = 0
        while self.running:
            print(f"\r{self.message}... {chars[i % len(chars)]}", end="", flush=True)
            i += 1
            await asyncio.sleep(0.1)


class CLITool:
    """Main CLI tool class."""
    
    def __init__(self, ai_client: MockAIClient):
        self.ai_client = ai_client
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """Setup logging for the CLI tool."""
        logger = logging.getLogger('cli_tool')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            
        return logger

    async def scaffold_project(self, args: argparse.Namespace) -> None:
        """Generate project scaffolding."""
        self.logger.info(f"Scaffolding project: {args.description}")
        
        settings = {
            "language": args.language,
            "template": args.template or "fastapi",
            "packageManager": args.package_manager or "pip", 
            "license": args.license or "MIT"
        }

        # Generate project plan
        async with ProgressIndicator("Generating project plan"):
            planning_prompt = scaffolder_planning_prompt(args.description, settings)
            plan_response = await self.ai_client.complete_async(planning_prompt)

        try:
            plan = json.loads(plan_response)
        except json.JSONDecodeError:
            print("❌ Failed to parse project plan")
            return

        print(f"\n📋 Project Plan Generated:")
        print(f"   Name: {plan['project']['name']}")
        print(f"   Language: {plan['project']['language']}")
        print(f"   Files: {len(plan['tree'])}")

        # Generate file prompts if requested
        if args.generate_files:
            async with ProgressIndicator("Generating file prompts"):
                file_prompts = {}
                for file_item in plan['tree']:
                    project_context = json.dumps(plan['project'])
                    file_context = json.dumps(file_item)
                    
                    file_prompt = scaffolder_file_prompt_generation(project_context, file_context)
                    file_prompts[file_item['path']] = file_prompt

            # Save to output directory
            output_dir = Path(args.output or "generated_project")
            output_dir.mkdir(exist_ok=True)
            
            # Save project plan
            with open(output_dir / "project_plan.json", "w") as f:
                json.dump(plan, f, indent=2)
                
            # Save file prompts
            prompts_dir = output_dir / "prompts"
            prompts_dir.mkdir(exist_ok=True)
            
            for file_path, prompt in file_prompts.items():
                prompt_file = prompts_dir / f"{file_path.replace('/', '_')}.txt"
                prompt_file.parent.mkdir(parents=True, exist_ok=True)
                with open(prompt_file, "w") as f:
                    f.write(prompt)

            print(f"📁 Generated files saved to: {output_dir}")
        
        if args.json:
            print("\n" + json.dumps(plan, indent=2))

    async def analyze_problem(self, args: argparse.Namespace) -> None:
        """Perform problem analysis."""
        self.logger.info(f"Analyzing problem: {args.problem[:50]}...")
        
        if args.type == "reasoning":
            async with ProgressIndicator("Performing step-by-step analysis"):
                prompt = step_by_step_reasoning_prompt(args.problem)
                result = await self.ai_client.complete_async(prompt)
        elif args.type == "stakeholder":
            async with ProgressIndicator("Identifying stakeholders"):
                prompt = stakeholder_mapping_prompt(args.problem)
                result = await self.ai_client.complete_async(prompt)
        else:
            print(f"❌ Unknown analysis type: {args.type}")
            return

        print("\n📊 Analysis Result:")
        print(result)
        
        # Save to file if requested
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(result)
            print(f"\n💾 Analysis saved to: {output_path}")

    async def process_document(self, args: argparse.Namespace) -> None:
        """Process document content."""
        if args.file:
            file_path = Path(args.file)
            if not file_path.exists():
                print(f"❌ File not found: {args.file}")
                return
            content = file_path.read_text()
            self.logger.info(f"Processing document: {args.file}")
        else:
            content = args.content
            self.logger.info("Processing provided content")

        if args.output_type == "readme":
            async with ProgressIndicator("Generating README"):
                prompt = chunk_summary_prompt_readme(content)
                result = await self.ai_client.complete_async(prompt)
        elif args.output_type == "summary":
            async with ProgressIndicator("Creating summary"):
                prompt = f"Summarize the following content:\n\n{content}"
                result = await self.ai_client.complete_async(prompt)
        else:
            print(f"❌ Unknown output type: {args.output_type}")
            return

        print("\n📄 Processed Document:")
        print(result)
        
        # Save to file if requested
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(result)
            print(f"\n💾 Document saved to: {output_path}")

    async def batch_process(self, args: argparse.Namespace) -> None:
        """Process multiple files in batch."""
        config_path = Path(args.config)
        if not config_path.exists():
            print(f"❌ Config file not found: {args.config}")
            return

        with open(config_path) as f:
            config = json.load(f)

        tasks = config.get("tasks", [])
        if not tasks:
            print("❌ No tasks found in config file")
            return

        self.logger.info(f"Processing {len(tasks)} tasks")
        
        results = []
        for i, task in enumerate(tasks):
            task_type = task.get("type")
            
            print(f"\n🔄 Processing task {i+1}/{len(tasks)}: {task_type}")
            
            if task_type == "scaffold":
                # Mock scaffolding task
                async with ProgressIndicator(f"Scaffolding {task.get('name', 'project')}"):
                    result = await self.ai_client.complete_async("scaffold project")
                    results.append({"task": i+1, "type": task_type, "result": result[:100]})
                    
            elif task_type == "analyze":
                async with ProgressIndicator(f"Analyzing {task.get('subject', 'content')}"):
                    result = await self.ai_client.complete_async("analyze problem")
                    results.append({"task": i+1, "type": task_type, "result": result[:100]})
                    
            elif task_type == "document":
                async with ProgressIndicator(f"Processing document"):
                    result = await self.ai_client.complete_async("process document")
                    results.append({"task": i+1, "type": task_type, "result": result[:100]})

        # Save batch results
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                json.dump(results, f, indent=2)
            print(f"\n💾 Batch results saved to: {output_path}")

        print(f"\n✅ Completed {len(results)} tasks")


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        description="AI-powered development CLI tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s scaffold --description "Build a REST API" --language python
  %(prog)s analyze --problem "How to scale databases?" --type reasoning  
  %(prog)s document --file README.md --output-type readme
  %(prog)s batch --config tasks.json --output results.json
        """
    )

    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Scaffold command
    scaffold_parser = subparsers.add_parser("scaffold", help="Generate project scaffolding")
    scaffold_parser.add_argument("--description", "-d", required=True, help="Project description")
    scaffold_parser.add_argument("--language", "-l", required=True, choices=["python", "go", "rust", "typescript"], help="Programming language")
    scaffold_parser.add_argument("--template", "-t", help="Project template")
    scaffold_parser.add_argument("--package-manager", help="Package manager")
    scaffold_parser.add_argument("--license", help="License type")
    scaffold_parser.add_argument("--generate-files", action="store_true", help="Generate file prompts")
    scaffold_parser.add_argument("--output", "-o", help="Output directory")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze problems and content")
    analyze_parser.add_argument("--problem", "-p", required=True, help="Problem to analyze")
    analyze_parser.add_argument("--type", "-t", choices=["reasoning", "stakeholder"], default="reasoning", help="Analysis type")
    analyze_parser.add_argument("--output", "-o", help="Output file path")

    # Document command
    document_parser = subparsers.add_parser("document", help="Process documents")
    document_group = document_parser.add_mutually_exclusive_group(required=True)
    document_group.add_argument("--file", "-f", help="Input file path")
    document_group.add_argument("--content", "-c", help="Direct content input")
    document_parser.add_argument("--output-type", choices=["readme", "summary"], default="readme", help="Output type")
    document_parser.add_argument("--output", "-o", help="Output file path")

    # Batch command
    batch_parser = subparsers.add_parser("batch", help="Process multiple operations")
    batch_parser.add_argument("--config", "-c", required=True, help="Batch configuration file")
    batch_parser.add_argument("--output", "-o", help="Output file for results")

    return parser


async def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if not args.command:
        parser.print_help()
        return

    # Initialize AI client
    ai_client = MockAIClient(delay=0.3)  # Faster for CLI
    cli_tool = CLITool(ai_client)

    try:
        if args.command == "scaffold":
            await cli_tool.scaffold_project(args)
        elif args.command == "analyze":
            await cli_tool.analyze_problem(args)
        elif args.command == "document":
            await cli_tool.process_document(args)
        elif args.command == "batch":
            await cli_tool.batch_process(args)
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


def create_sample_batch_config():
    """Create a sample batch configuration file."""
    config = {
        "tasks": [
            {
                "type": "scaffold",
                "name": "user-api",
                "description": "REST API for user management",
                "language": "python",
                "template": "fastapi"
            },
            {
                "type": "analyze",
                "subject": "Database scaling strategies",
                "problem": "How to handle millions of users?",
                "analysis_type": "reasoning"
            },
            {
                "type": "document",
                "input_file": "requirements.txt",
                "output_type": "readme"
            }
        ]
    }
    
    with open("sample_batch_config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print("Created sample_batch_config.json")


if __name__ == "__main__":
    # Create sample config if it doesn't exist
    if len(sys.argv) > 1 and sys.argv[1] == "create-sample-config":
        create_sample_batch_config()
    else:
        asyncio.run(main())

"""
Installation requirements:
pip install asyncio pathlib

Usage examples:
python cli_tool.py scaffold --description "Build a task management API" --language python --generate-files --output my_project

python cli_tool.py analyze --problem "How to implement microservices communication?" --type reasoning --output analysis.md

python cli_tool.py document --file project_spec.txt --output-type readme --output README.md

python cli_tool.py create-sample-config
python cli_tool.py batch --config sample_batch_config.json --output batch_results.json
"""