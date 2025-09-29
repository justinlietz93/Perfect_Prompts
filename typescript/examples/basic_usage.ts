/**
 * Basic usage examples for TypeScript prompt templates.
 * Demonstrates fundamental patterns for integrating prompts with AI clients.
 */

import { performance } from 'perf_hooks';

// Mock AI Client interface for demonstration
interface AIClient {
  complete(prompt: string): Promise<string>;
  completeWithTimeout(prompt: string, timeoutMs: number): Promise<string>;
}

interface ClientStats {
  totalCalls: number;
  totalDuration: number;
}

class MockAIClient implements AIClient {
  private callCount = 0;

  async complete(prompt: string): Promise<string> {
    return this.completeWithTimeout(prompt, 30000);
  }

  async completeWithTimeout(prompt: string, timeoutMs: number): Promise<string> {
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 100));
    
    this.callCount++;

    const lowerPrompt = prompt.toLowerCase();
    
    if (lowerPrompt.includes('project plan')) {
      return this.mockProjectPlan();
    } else if (lowerPrompt.includes('step-by-step')) {
      return this.mockReasoningResponse();
    } else if (lowerPrompt.includes('stakeholder')) {
      return this.mockStakeholderResponse();
    }

    return `Mock response ${this.callCount} for prompt: ${prompt.slice(0, 50)}...`;
  }

  private mockProjectPlan(): string {
    const plan = {
      project: {
        name: "TaskManagerAPI",
        language: "typescript",
        template: "express",
        package_manager: "npm",
        license: "MIT"
      },
      layers: ["presentation", "application", "domain", "infrastructure", "shared", "tests"],
      tree: [
        {
          path: "src/presentation/controllers/TaskController.ts",
          layer: "presentation",
          purpose: "HTTP controllers for task management",
          prompt: ""
        },
        {
          path: "src/application/services/TaskService.ts",
          layer: "application",
          purpose: "Business logic for task operations",
          prompt: ""
        }
      ]
    };

    return JSON.stringify(plan, null, 2);
  }

  private mockReasoningResponse(): string {
    return `**Step 1: Problem Analysis**
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
4. Add monitoring and observability`;
  }

  private mockStakeholderResponse(): string {
    return `## Project Stakeholders

### Primary Stakeholders
- **Product Owner**: Defines requirements and priorities
- **Development Team**: Implements the solution
- **End Users**: Will use the task management system

### Secondary Stakeholders
- **DevOps Team**: Manages deployment and infrastructure
- **QA Team**: Ensures quality and testing
- **Security Team**: Reviews security requirements`;
  }
}

// Mock prompt functions (replace with actual imports)
function scaffolderPlanningPrompt(description: string, settings: Record<string, string>): string {
  return `You are an expert AI software architect specializing in the Hybrid-Clean architecture.
Your task is to take a user's project description and generate a detailed project plan as a single JSON object.

Project Description: ${description}
Settings: ${JSON.stringify(settings)}

Generate a comprehensive project plan...`;
}

function stepByStepReasoningPrompt(problem: string): string {
  return `You are an expert problem solver. Break down the following problem into clear, logical steps:

Problem: ${problem}

Provide a step-by-step analysis and solution...`;
}

function chunkSummaryPromptReadme(text: string): string {
  return `You are a technical writer AI tasked with creating a section of a project README.md file.
Your job is to analyze the following document segment and extract information relevant to a project's documentation.

Document to analyze:
${text}

Generate a README section...`;
}

// Project scaffolding example
async function demonstrateBasicScaffolding(client: AIClient): Promise<void> {
  console.log('=== Project Scaffolding Example ===');

  const description = "Build a REST API for task management with user authentication";
  const settings = {
    language: "typescript",
    template: "express",
    packageManager: "npm",
    license: "MIT"
  };

  // Step 1: Generate project plan
  const planningPrompt = scaffolderPlanningPrompt(description, settings);
  console.log(`Generated planning prompt (${planningPrompt.length} chars)`);

  try {
    const planResponse = await client.complete(planningPrompt);
    const plan = JSON.parse(planResponse);

    console.log(`Project: ${plan.project.name}`);
    console.log(`Files to generate: ${plan.tree.length}`);

    // Step 2: Generate file prompts would go here
    console.log("File prompt generation completed");
  } catch (error) {
    console.error("Error in scaffolding:", error);
  }
}

// Reasoning workflow example
async function demonstrateReasoningWorkflow(client: AIClient): Promise<void> {
  console.log('\n=== Reasoning Workflow Example ===');

  const problem = "How can we design a scalable microservices architecture for a high-traffic e-commerce platform?";

  const reasoningPrompt = stepByStepReasoningPrompt(problem);
  console.log(`Generated reasoning prompt (${reasoningPrompt.length} chars)`);

  try {
    const reasoningResult = await client.complete(reasoningPrompt);
    console.log("Reasoning Result:");
    console.log(reasoningResult);
  } catch (error) {
    console.error("Error in reasoning:", error);
  }
}

// Concurrent processing example
async function demonstrateConcurrentProcessing(client: AIClient): Promise<void> {
  console.log('\n=== Concurrent Processing Example ===');

  const problems = [
    "Design a caching strategy for high-load systems",
    "Implement fault tolerance in distributed systems",
    "Optimize database queries for performance"
  ];

  const processingTasks = problems.map(async (problem, index) => {
    try {
      const prompt = stepByStepReasoningPrompt(problem);
      const result = await client.complete(prompt);
      return { index: index + 1, problem, result, success: true };
    } catch (error) {
      return { 
        index: index + 1, 
        problem, 
        error: error instanceof Error ? error.message : 'Unknown error', 
        success: false 
      };
    }
  });

  const results = await Promise.all(processingTasks);

  results.forEach(result => {
    if (result.success) {
      console.log(`Problem ${result.index}: ${result.problem}`);
      console.log(`Result: ${(result as any).result.slice(0, 100)}...\n`);
    } else {
      console.log(`Problem ${result.index} failed: ${(result as any).error}`);
    }
  });
}

// Promise.allSettled example for error handling
async function demonstrateErrorHandling(client: AIClient): Promise<void> {
  console.log('\n=== Error Handling with Promise.allSettled ===');

  class FailingClient implements AIClient {
    async complete(_prompt: string): Promise<string> {
      throw new Error("API rate limit exceeded");
    }

    async completeWithTimeout(_prompt: string, _timeoutMs: number): Promise<string> {
      throw new Error("API rate limit exceeded");
    }
  }

  const failingClient = new FailingClient();

  // Retry function with exponential backoff
  async function retryWithBackoff(
    client: AIClient,
    prompt: string,
    maxRetries: number = 3
  ): Promise<string> {
    let lastError: Error | null = null;

    for (let attempt = 0; attempt < maxRetries; attempt++) {
      try {
        return await client.complete(prompt);
      } catch (error) {
        lastError = error instanceof Error ? error : new Error('Unknown error');
        console.log(`Attempt ${attempt + 1} failed: ${lastError.message}`);

        if (attempt < maxRetries - 1) {
          const delay = Math.pow(2, attempt) * 1000; // Exponential backoff
          await new Promise(resolve => setTimeout(resolve, delay));
        }
      }
    }

    throw new Error(`All ${maxRetries} attempts failed. Last error: ${lastError?.message}`);
  }

  const prompt = stepByStepReasoningPrompt("Test problem");
  
  try {
    const result = await retryWithBackoff(failingClient, prompt);
    console.log(`Final result: ${result}`);
  } catch (error) {
    console.log(`Final result: Failed - ${error instanceof Error ? error.message : 'Unknown error'}`);
  }
}

// Performance monitoring example
class InstrumentedClient implements AIClient {
  private stats: ClientStats = { totalCalls: 0, totalDuration: 0 };

  constructor(private client: AIClient) {}

  async complete(prompt: string): Promise<string> {
    const start = performance.now();
    try {
      const result = await this.client.complete(prompt);
      return result;
    } finally {
      const duration = performance.now() - start;
      this.stats.totalCalls++;
      this.stats.totalDuration += duration;
    }
  }

  async completeWithTimeout(prompt: string, timeoutMs: number): Promise<string> {
    const start = performance.now();
    try {
      const result = await this.client.completeWithTimeout(prompt, timeoutMs);
      return result;
    } finally {
      const duration = performance.now() - start;
      this.stats.totalCalls++;
      this.stats.totalDuration += duration;
    }
  }

  getStats(): ClientStats {
    return { ...this.stats };
  }
}

async function demonstratePerformanceMonitoring(): Promise<void> {
  console.log('\n=== Performance Monitoring Example ===');

  const baseClient = new MockAIClient();
  const instrumentedClient = new InstrumentedClient(baseClient);

  // Make several calls
  const promises = Array.from({ length: 5 }, (_, i) => {
    const prompt = stepByStepReasoningPrompt(`Problem ${i + 1}`);
    return instrumentedClient.complete(prompt).catch(error => {
      console.error(`Call ${i + 1} failed:`, error);
      return null;
    });
  });

  await Promise.all(promises);

  const stats = instrumentedClient.getStats();
  const avgDuration = stats.totalDuration / stats.totalCalls;

  console.log('Performance Stats:');
  console.log(`  Total calls: ${stats.totalCalls}`);
  console.log(`  Total duration: ${stats.totalDuration.toFixed(2)}ms`);
  console.log(`  Average duration: ${avgDuration.toFixed(2)}ms`);
}

// Timeout handling example
async function demonstrateTimeoutHandling(client: AIClient): Promise<void> {
  console.log('\n=== Timeout Handling Example ===');

  const problem = "Explain the principles of clean architecture";
  const prompt = stepByStepReasoningPrompt(problem);

  try {
    const result = await client.completeWithTimeout(prompt, 5000); // 5 second timeout
    console.log(`Result: ${result.slice(0, 150)}...`);
  } catch (error) {
    if (error instanceof Error && error.message.includes('timeout')) {
      console.log('Request timed out');
    } else {
      console.log(`Request failed: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  }
}

// Document analysis pipeline example
async function demonstrateDocumentAnalysisPipeline(client: AIClient): Promise<void> {
  console.log('\n=== Document Analysis Pipeline ===');

  const documentContent = `
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
  `;

  try {
    // Process document sections concurrently
    const [readmeSection, stakeholderAnalysis] = await Promise.all([
      client.complete(chunkSummaryPromptReadme(documentContent)),
      client.complete(`Identify and categorize stakeholders in: ${documentContent}`)
    ]);

    console.log('Generated README Section:');
    console.log(readmeSection.slice(0, 200) + '...\n');
    
    console.log('Stakeholder Analysis:');
    console.log(stakeholderAnalysis.slice(0, 200) + '...');
  } catch (error) {
    console.error('Document analysis failed:', error);
  }
}

// Streaming simulation example
async function demonstrateStreamingSimulation(client: AIClient): Promise<void> {
  console.log('\n=== Streaming Simulation Example ===');

  // Simulate streaming by breaking response into chunks
  async function* simulateStreaming(text: string): AsyncGenerator<string, void, unknown> {
    const words = text.split(' ');
    for (let i = 0; i < words.length; i += 3) {
      const chunk = words.slice(i, i + 3).join(' ') + ' ';
      yield chunk;
      await new Promise(resolve => setTimeout(resolve, 50)); // Simulate delay
    }
  }

  const prompt = stepByStepReasoningPrompt("Explain event-driven architecture");
  
  try {
    const fullResponse = await client.complete(prompt);
    console.log('Streaming response:');
    
    for await (const chunk of simulateStreaming(fullResponse)) {
      process.stdout.write(chunk);
    }
    console.log('\n\nStreaming completed');
  } catch (error) {
    console.error('Streaming failed:', error);
  }
}

// Main execution function
async function main(): Promise<void> {
  console.log('TypeScript Prompt Templates - Basic Usage Examples');
  console.log('='.repeat(60));

  const client = new MockAIClient();

  try {
    await demonstrateBasicScaffolding(client);
    await demonstrateReasoningWorkflow(client);
    await demonstrateConcurrentProcessing(client);
    await demonstrateErrorHandling(client);
    await demonstratePerformanceMonitoring();
    await demonstrateTimeoutHandling(client);
    await demonstrateDocumentAnalysisPipeline(client);
    await demonstrateStreamingSimulation(client);

    console.log('\n' + '='.repeat(60));
    console.log('All examples completed successfully!');
  } catch (error) {
    console.error('An error occurred during execution:', error);
    process.exit(1);
  }
}

// Error handling for unhandled promises
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
  process.exit(1);
});

// Run the examples
if (require.main === module) {
  main().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
  });
}

export {
  AIClient,
  MockAIClient,
  InstrumentedClient,
  scaffolderPlanningPrompt,
  stepByStepReasoningPrompt,
  chunkSummaryPromptReadme
};

/*
// Package.json dependencies for this example:
{
  "dependencies": {
    "@types/node": "^20.0.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "ts-node": "^10.9.0"
  }
}

// To run: npx ts-node basic_usage.ts
*/