#!/usr/bin/env python3
"""
LangChain integration examples for Python prompt templates.
Demonstrates how to use prompts with LangChain chains and agents.
"""

import os
import sys
from typing import Dict, List

# Add the parent directory to the path to import prompt modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Note: This example shows how to integrate with LangChain
# Install with: pip install langchain langchain-openai

try:
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain, SequentialChain
    from langchain.schema import BaseOutputParser
    from langchain_openai import ChatOpenAI
    LANGCHAIN_AVAILABLE = True
except ImportError:
    print("LangChain not installed. This is a demonstration of integration patterns.")
    LANGCHAIN_AVAILABLE = False

from agent_prompts.project_scaffolder import scaffolder_planning_prompt
from agent_prompts.reasoner import step_by_step_reasoning_prompt
from summary_prompts.readme import chunk_summary_prompt_readme


class MockChatOpenAI:
    """Mock LangChain LLM for demonstration purposes."""
    
    def __call__(self, text: str) -> str:
        if "project plan" in text.lower():
            return '{"project": {"name": "MockProject"}, "tree": []}'
        elif "step-by-step" in text.lower():
            return "Step 1: Analyze\nStep 2: Design\nStep 3: Implement"
        else:
            return f"Mock response for: {text[:50]}..."


class JSONOutputParser:
    """Simple JSON output parser for demo."""
    
    def parse(self, text: str) -> Dict:
        import json
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON", "raw": text}


def demonstrate_prompt_template_integration():
    """Show how to integrate custom prompts with LangChain PromptTemplate."""
    print("=== LangChain PromptTemplate Integration ===")
    
    if not LANGCHAIN_AVAILABLE:
        # Show the pattern without actual LangChain
        print("Pattern: Wrapping custom prompts in LangChain PromptTemplate")
        
        # Custom prompt function
        def create_scaffolder_template(description: str, settings: Dict) -> str:
            return scaffolder_planning_prompt(description, settings)
        
        # Simulate usage
        description = "Build a web API"
        settings = {"language": "python", "template": "fastapi"}
        prompt_text = create_scaffolder_template(description, settings)
        
        print(f"Generated prompt length: {len(prompt_text)} characters")
        return
    
    # Actual LangChain integration
    llm = ChatOpenAI(temperature=0.7, model="gpt-4")
    
    # Create a custom prompt template that uses our scaffolder prompt
    scaffolder_template = PromptTemplate(
        input_variables=["description", "language", "template"],
        template=lambda description, language, template: scaffolder_planning_prompt(
            description, 
            {"language": language, "template": template, "packageManager": "pip", "license": "MIT"}
        )
    )
    
    # Create a chain
    scaffolder_chain = LLMChain(
        llm=llm,
        prompt=scaffolder_template,
        output_parser=JSONOutputParser()
    )
    
    # Use the chain
    result = scaffolder_chain.run(
        description="Build a REST API for user management",
        language="python",
        template="fastapi"
    )
    
    print(f"Scaffolding result: {result}")


def demonstrate_sequential_chain():
    """Show how to chain multiple prompts together."""
    print("\n=== Sequential Chain Example ===")
    
    if not LANGCHAIN_AVAILABLE:
        # Mock sequential processing
        llm = MockChatOpenAI()
        
        # Step 1: Planning
        planning_prompt = scaffolder_planning_prompt(
            "Build a task management API",
            {"language": "python", "template": "fastapi"}
        )
        plan_result = llm(planning_prompt)
        print(f"Planning result: {plan_result[:100]}...")
        
        # Step 2: Reasoning
        reasoning_prompt = step_by_step_reasoning_prompt(
            f"How to implement this plan: {plan_result}"
        )
        reasoning_result = llm(reasoning_prompt)
        print(f"Reasoning result: {reasoning_result[:100]}...")
        
        return
    
    llm = ChatOpenAI(temperature=0.7, model="gpt-4")
    
    # First chain: Project planning
    planning_template = PromptTemplate(
        input_variables=["description"],
        template=lambda description: scaffolder_planning_prompt(
            description,
            {"language": "python", "template": "fastapi", "packageManager": "pip"}
        )
    )
    
    planning_chain = LLMChain(
        llm=llm,
        prompt=planning_template,
        output_key="project_plan"
    )
    
    # Second chain: Implementation reasoning
    reasoning_template = PromptTemplate(
        input_variables=["project_plan"],
        template=lambda project_plan: step_by_step_reasoning_prompt(
            f"How to implement this project plan: {project_plan}"
        )
    )
    
    reasoning_chain = LLMChain(
        llm=llm,
        prompt=reasoning_template,
        output_key="implementation_steps"
    )
    
    # Combine into sequential chain
    overall_chain = SequentialChain(
        chains=[planning_chain, reasoning_chain],
        input_variables=["description"],
        output_variables=["project_plan", "implementation_steps"]
    )
    
    # Execute the chain
    result = overall_chain.run("Build a real-time chat application")
    print(f"Sequential chain result: {result}")


def demonstrate_custom_chain_class():
    """Show how to create a custom chain class using our prompts."""
    print("\n=== Custom Chain Class ===")
    
    class DocumentAnalysisChain:
        """Custom chain for document analysis using our prompts."""
        
        def __init__(self, llm):
            self.llm = llm
        
        def analyze_document(self, document_text: str) -> Dict[str, str]:
            # Step 1: Generate README
            readme_prompt = chunk_summary_prompt_readme(document_text)
            readme_result = self.llm(readme_prompt)
            
            # Step 2: Extract stakeholders (mock for this example)
            stakeholder_prompt = f"Identify stakeholders in: {document_text[:200]}..."
            stakeholder_result = self.llm(stakeholder_prompt)
            
            return {
                "readme": readme_result,
                "stakeholders": stakeholder_result
            }
    
    # Use the custom chain
    llm = MockChatOpenAI()
    analysis_chain = DocumentAnalysisChain(llm)
    
    document = """
    ProjectX is a machine learning platform for predictive analytics.
    It serves data scientists, business analysts, and executive stakeholders.
    The system requires high availability and regulatory compliance.
    """
    
    result = analysis_chain.analyze_document(document)
    print(f"README: {result['readme'][:100]}...")
    print(f"Stakeholders: {result['stakeholders'][:100]}...")


def demonstrate_memory_integration():
    """Show how to use prompts with LangChain memory."""
    print("\n=== Memory Integration Example ===")
    
    if not LANGCHAIN_AVAILABLE:
        # Mock memory pattern
        class MockMemory:
            def __init__(self):
                self.chat_history = []
            
            def add_message(self, message: str):
                self.chat_history.append(message)
            
            def get_context(self) -> str:
                return "\n".join(self.chat_history[-3:])  # Last 3 messages
        
        memory = MockMemory()
        llm = MockChatOpenAI()
        
        # Simulate conversation with context
        questions = [
            "Explain microservices architecture",
            "How do microservices communicate?",
            "What are the benefits of this approach?"
        ]
        
        for question in questions:
            context = memory.get_context()
            reasoning_prompt = step_by_step_reasoning_prompt(
                f"Context: {context}\nQuestion: {question}"
            )
            
            response = llm(reasoning_prompt)
            memory.add_message(f"Q: {question}")
            memory.add_message(f"A: {response}")
            
            print(f"Q: {question}")
            print(f"A: {response[:100]}...")
            print()
        
        return
    
    from langchain.memory import ConversationBufferMemory
    
    # Set up memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    llm = ChatOpenAI(temperature=0.7)
    
    # Create a chain that uses reasoning prompts with memory
    reasoning_template = PromptTemplate(
        input_variables=["chat_history", "question"],
        template="""
        Previous conversation:
        {chat_history}
        
        New question: {question}
        
        Provide a step-by-step reasoning response considering the conversation context.
        """
    )
    
    conversation_chain = LLMChain(
        llm=llm,
        prompt=reasoning_template,
        memory=memory
    )
    
    # Have a conversation
    questions = [
        "Explain the benefits of clean architecture",
        "How does this relate to microservices?",
        "What testing strategies work best?"
    ]
    
    for question in questions:
        response = conversation_chain.run(question=question)
        print(f"Q: {question}")
        print(f"A: {response[:100]}...")
        print()


def main():
    """Run all LangChain integration examples."""
    print("Python Prompt Templates - LangChain Integration Examples")
    print("=" * 60)
    
    if not LANGCHAIN_AVAILABLE:
        print("Note: LangChain not installed. Showing integration patterns with mocks.")
        print("Install with: pip install langchain langchain-openai")
        print()
    
    demonstrate_prompt_template_integration()
    demonstrate_sequential_chain()
    demonstrate_custom_chain_class()
    demonstrate_memory_integration()
    
    print("=" * 60)
    print("LangChain integration examples completed!")


if __name__ == "__main__":
    main()