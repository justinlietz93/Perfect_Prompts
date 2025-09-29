# TypeScript Prompt Templates

This directory contains TypeScript implementations of prompt templates designed for agentic AI systems. These templates provide structured, reusable prompts with TypeScript's type safety, modern JavaScript features, and excellent tooling support for AI-assisted development and analysis tasks.

## Overview

The TypeScript prompt templates are organized into two main categories:

### 🤖 Agent Prompts (`agent_prompts/`)
Specialized prompts for AI agents that perform specific development and analysis tasks:

- **`projectScaffolder.ts`** - Generate project structures using Hybrid-Clean architecture
- **`agentDesigner.ts`** - Design single-agent and multi-agent AI systems with comprehensive settings
- **`mermaidDesigner.ts`** - Create and validate Mermaid.js diagrams from specifications
- **`promptEnhancer.ts`** - Improve and optimize existing prompts with advanced techniques
- **`reasoner.ts`** - Perform step-by-step logical reasoning and problem-solving
- **`rewriter.ts`** - Rewrite content with specific styles, tones, and requirements
- **`citations.ts`** - Generate proper academic and professional citations
- **`mathFormatter.ts`** - Format mathematical expressions and equations
- **`styleExtractor.ts`** - Extract and analyze writing styles and patterns
- **`highlightExtraction.ts`** - Extract key highlights and insights from content
- **`nextSteps.ts`** - Generate actionable next steps from analysis results
- **`requestSplitter.ts`** - Break down complex requests into manageable sub-tasks

### 📊 Summary Prompts (`summary_prompts/`)
Templates for analyzing, summarizing, and structuring content:

- **`readme.ts`** - Generate comprehensive README documentation
- **`summarize.ts`** - Create concise summaries of complex content
- **`checklist.ts`** - Convert content into actionable checklists
- **`timeline.ts`** - Extract and organize temporal information
- **`processFlow.ts`** - Document step-by-step processes and workflows
- **`stakeholderMap.ts`** - Identify and map project stakeholders
- **`riskRegister.ts`** - Identify and assess project risks
- **`decisionMatrix.ts`** - Structure decision-making processes
- **`swotAnalysis.ts`** - Perform SWOT analysis
- **`entityRelationshipDigest.ts`** - Extract entity relationships from content
- **`systemWalkthrough.ts`** - Generate system documentation and walkthroughs
- **`reverseEngineering.ts`** - Analyze and document existing systems

## Usage in Agentic Projects

### Basic Usage Pattern

```typescript
import { 
  SCAFFOLDER_PLANNING_PROMPT_TEMPLATE,
  type ScaffolderSettings 
} from './agent_prompts/projectScaffolder';
import { CHUNK_SUMMARY_PROMPT_TEMPLATE_README } from './summary_prompts/readme';

async function main() {
  // Generate a project scaffolding prompt
  const projectDescription = "Build a REST API for task management";
  const settings: ScaffolderSettings = {
    language: "typescript",
    template: "express",
    packageManager: "npm",
    license: "MIT"
  };

  const scaffoldPrompt = SCAFFOLDER_PLANNING_PROMPT_TEMPLATE(projectDescription, settings);

  // Use with your AI client
  const response = await aiClient.complete(scaffoldPrompt);
  console.log(response);
}
```

### Type-Safe Configuration with Zod

TypeScript's type system combined with runtime validation provides excellent developer experience:

```typescript
import { z } from 'zod';

const AgentDesignerSettingsSchema = z.object({
  systemType: z.enum(['singleAgent', 'multiAgent']),
  goal: z.string().min(1, 'Goal cannot be empty'),
  trigger: z.string().optional(),  
  provider: z.enum(['openai', 'anthropic', 'azure']).default('openai'),
  capabilities: z.record(z.boolean()).default({}),
  temperature: z.number().min(0).max(2).default(0.7),
  maxTokens: z.number().int().positive().max(4096).default(2048)
});

export type AgentDesignerSettings = z.infer<typeof AgentDesignerSettingsSchema>;

// Usage with validation
function createAgentDesignerPrompt(settings: unknown): string {
  const validatedSettings = AgentDesignerSettingsSchema.parse(settings);
  return AGENT_DESIGNER_PROMPT_TEMPLATE(validatedSettings);
}
```

### Integration with Modern AI Libraries

#### OpenAI SDK Integration
```typescript
import OpenAI from 'openai';
import { STEP_BY_STEP_REASONING_PROMPT } from './agent_prompts/reasoner';

class AIPromptProcessor {
  private openai: OpenAI;

  constructor(apiKey: string) {
    this.openai = new OpenAI({ apiKey });
  }

  async processReasoningTask(problem: string): Promise<string> {
    const prompt = STEP_BY_STEP_REASONING_PROMPT(problem);
    
    const completion = await this.openai.chat.completions.create({
      messages: [{ role: 'user', content: prompt }],
      model: 'gpt-4',
      temperature: 0.7,
    });

    return completion.choices[0]?.message?.content ?? '';
  }

  async streamProcessing(prompt: string): Promise<AsyncIterable<string>> {
    const stream = await this.openai.chat.completions.create({
      messages: [{ role: 'user', content: prompt }],
      model: 'gpt-4',
      stream: true,
    });

    return this.extractContentFromStream(stream);
  }

  private async* extractContentFromStream(
    stream: AsyncIterable<OpenAI.Chat.Completions.ChatCompletionChunk>
  ): AsyncIterable<string> {
    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        yield content;
      }
    }
  }
}
```

#### LangChain Integration
```typescript
import { ChatOpenAI } from "@langchain/openai";
import { PromptTemplate } from "@langchain/core/prompts";
import { RunnableSequence } from "@langchain/core/runnables";
import { StringOutputParser } from "@langchain/core/output_parsers";

export class LangChainPromptProcessor {
  private model: ChatOpenAI;

  constructor(openAIApiKey: string) {
    this.model = new ChatOpenAI({
      openAIApiKey,
      modelName: "gpt-4",
      temperature: 0.7,
    });
  }

  async createAnalysisChain(documentText: string) {
    // Create prompt templates
    const summaryTemplate = PromptTemplate.fromTemplate(
      CHUNK_SUMMARY_PROMPT_TEMPLATE_README(documentText)
    );

    const stakeholderTemplate = PromptTemplate.fromTemplate(
      STAKEHOLDER_MAPPING_PROMPT(documentText)
    );

    // Create processing chain
    const analysisChain = RunnableSequence.from([
      {
        summary: summaryTemplate.pipe(this.model).pipe(new StringOutputParser()),
        stakeholders: stakeholderTemplate.pipe(this.model).pipe(new StringOutputParser()),
      },
    ]);

    return analysisChain;
  }
}
```

### Workflow Examples

#### Async Document Processing with Promise.all
```typescript
interface DocumentAnalysis {
  document: string;
  analysis: string;
  processedAt: Date;
}

export class DocumentProcessor {
  constructor(private aiClient: AIPromptProcessor) {}

  async processDocumentsConcurrently(documents: string[]): Promise<DocumentAnalysis[]> {
    const analysisPromises = documents.map(async (doc): Promise<DocumentAnalysis> => {
      try {
        const analysisPrompt = SYSTEM_WALKTHROUGH_PROMPT(doc);
        const analysis = await this.aiClient.complete(analysisPrompt);
        
        return {
          document: doc,
          analysis,
          processedAt: new Date(),
        };
      } catch (error) {
        throw new Error(`Failed to process document: ${error instanceof Error ? error.message : 'Unknown error'}`);
      }
    });

    return Promise.all(analysisPromises);
  }

  async processDocumentsWithErrorHandling(documents: string[]): Promise<{
    successful: DocumentAnalysis[];
    failed: Array<{ document: string; error: string }>;
  }> {
    const results = await Promise.allSettled(
      documents.map(doc => this.processDocument(doc))
    );

    const successful: DocumentAnalysis[] = [];
    const failed: Array<{ document: string; error: string }> = [];

    results.forEach((result, index) => {
      if (result.status === 'fulfilled') {
        successful.push(result.value);
      } else {
        failed.push({
          document: documents[index],
          error: result.reason.message,
        });
      }
    });

    return { successful, failed };
  }

  private async processDocument(document: string): Promise<DocumentAnalysis> {
    const analysisPrompt = SYSTEM_WALKTHROUGH_PROMPT(document);
    const analysis = await this.aiClient.complete(analysisPrompt);
    
    return {
      document,
      analysis,
      processedAt: new Date(),
    };
  }
}
```

#### Project Scaffolding Pipeline with Error Recovery
```typescript
interface ProjectPlan {
  project: ProjectInfo;
  layers: string[];
  tree: FileItem[];
  filePrompts?: Record<string, string>;
}

interface FileItem {
  path: string;
  layer: string;
  purpose: string;
}

export class ProjectScaffolder {
  constructor(private aiClient: AIPromptProcessor) {}

  async scaffoldProject(
    description: string,
    settings: ScaffolderSettings
  ): Promise<ProjectPlan> {
    // Step 1: Generate project plan with retry logic
    const planningPrompt = SCAFFOLDER_PLANNING_PROMPT_TEMPLATE(description, settings);
    const planResponse = await this.completeWithRetry(planningPrompt, 3);
    
    let plan: ProjectPlan;
    try {
      plan = JSON.parse(planResponse) as ProjectPlan;
    } catch (error) {
      throw new Error(`Invalid project plan JSON: ${error instanceof Error ? error.message : 'Parse error'}`);
    }

    // Step 2: Generate file prompts concurrently
    const filePromptPromises = plan.tree.map(async (fileItem): Promise<[string, string]> => {
      const projectData = JSON.stringify(plan.project);
      const fileData = JSON.stringify(fileItem);
      const filePrompt = SCAFFOLDER_FILE_PROMPT_GENERATION_TEMPLATE(
        JSON.parse(projectData),
        fileItem
      );
      return [fileItem.path, filePrompt];
    });

    const filePromptResults = await Promise.all(filePromptPromises);
    const filePrompts = Object.fromEntries(filePromptResults);

    return {
      ...plan,
      filePrompts,
    };
  }

  private async completeWithRetry(
    prompt: string,
    maxRetries: number,
    delay: number = 1000
  ): Promise<string> {
    let lastError: Error | null = null;

    for (let attempt = 0; attempt <= maxRetries; attempt++) {
      try {
        return await this.aiClient.complete(prompt);
      } catch (error) {
        lastError = error instanceof Error ? error : new Error('Unknown error');
        
        if (attempt < maxRetries) {
          await this.sleep(delay * (attempt + 1)); // Exponential backoff
        }
      }
    }

    throw new Error(`Failed after ${maxRetries} attempts: ${lastError?.message}`);
  }

  private sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

## Best Practices

### 1. **Type Safety with Strict TypeScript**
Configure strict TypeScript settings:
```json
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

### 2. **Error Handling with Custom Error Classes**
```typescript
export class PromptError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly details?: unknown
  ) {
    super(message);
    this.name = 'PromptError';
  }
}

export class AIClientError extends PromptError {
  constructor(message: string, details?: unknown) {
    super(message, 'AI_CLIENT_ERROR', details);
  }
}

export class ValidationError extends PromptError {
  constructor(message: string, details?: unknown) {
    super(message, 'VALIDATION_ERROR', details);
  }
}
```

### 3. **Async/Await with Proper Error Boundaries**
```typescript
export async function safePromptExecution<T>(
  operation: () => Promise<T>,
  context: string
): Promise<T> {
  try {
    return await operation();
  } catch (error) {
    if (error instanceof PromptError) {
      throw error;
    }
    
    throw new PromptError(
      `Operation failed in ${context}`,
      'EXECUTION_ERROR',
      error
    );
  }
}
```

### 4. **Configuration Management with Environment Variables**
```typescript
import { z } from 'zod';

const ConfigSchema = z.object({
  OPENAI_API_KEY: z.string().min(1, 'OpenAI API key is required'),
  AI_MODEL: z.string().default('gpt-4'),
  AI_TEMPERATURE: z.coerce.number().min(0).max(2).default(0.7),
  AI_MAX_TOKENS: z.coerce.number().int().positive().max(4096).default(2048),
  LOG_LEVEL: z.enum(['debug', 'info', 'warn', 'error']).default('info'),
});

export type Config = z.infer<typeof ConfigSchema>;

export function loadConfig(): Config {
  return ConfigSchema.parse(process.env);
}
```

### 5. **Testing with Jest and MSW**
```typescript
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import { AIPromptProcessor } from '../src/AIPromptProcessor';

const server = setupServer(
  rest.post('https://api.openai.com/v1/chat/completions', (req, res, ctx) => {
    return res(
      ctx.json({
        choices: [
          {
            message: {
              content: 'Mock AI response',
            },
          },
        ],
      })
    );
  })
);

describe('AIPromptProcessor', () => {
  beforeAll(() => server.listen());
  afterEach(() => server.resetHandlers());
  afterAll(() => server.close());

  it('should process reasoning task successfully', async () => {
    const processor = new AIPromptProcessor('test-api-key');
    const result = await processor.processReasoningTask('Test problem');
    
    expect(result).toBe('Mock AI response');
  });

  it('should handle API errors gracefully', async () => {
    server.use(
      rest.post('https://api.openai.com/v1/chat/completions', (req, res, ctx) => {
        return res(ctx.status(500), ctx.json({ error: 'Server error' }));
      })
    );

    const processor = new AIPromptProcessor('test-api-key');
    
    await expect(processor.processReasoningTask('Test problem'))
      .rejects
      .toThrow('Server error');
  });
});
```

## Integration Examples

See the `examples/` directory for complete, runnable examples demonstrating:
- Express.js REST API integration
- Next.js web application integration
- Node.js CLI applications
- React hooks for AI interactions
- WebSocket streaming implementations
- Electron desktop app integration
- Testing patterns with Jest and MSW
- Docker containerization

## Dependencies

Core prompt templates have no dependencies. Integration examples may require:

```json
{
  "dependencies": {
    "openai": "^4.20.0",
    "@langchain/openai": "^0.0.14",
    "@langchain/core": "^0.1.17",
    "zod": "^3.22.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "@types/node": "^20.10.0",
    "@types/jest": "^29.5.0",
    "typescript": "^5.3.0",
    "ts-node": "^10.9.0",
    "jest": "^29.7.0",
    "ts-jest": "^29.1.0",
    "msw": "^2.0.0",
    "eslint": "^8.56.0",
    "@typescript-eslint/parser": "^6.15.0",
    "@typescript-eslint/eslint-plugin": "^6.15.0"
  }
}
```

## Performance Considerations

- Use `Promise.all()` for concurrent operations
- Implement streaming for long-running AI operations
- Use connection pooling for HTTP clients
- Cache frequently used prompts with Redis or memory
- Implement request deduplication
- Use compression for large prompt payloads
- Monitor memory usage with Node.js profiling tools

## Modern JavaScript Features

Leverage modern ECMAScript features:
- **Optional chaining**: `response?.choices?.[0]?.message?.content`
- **Nullish coalescing**: `content ?? 'default content'`
- **Template literals**: For dynamic prompt generation
- **Async iterators**: For streaming responses
- **WeakMap/WeakSet**: For memory-efficient caching

## Contributing

When adding new prompt templates:
1. Use TypeScript strict mode and proper type annotations
2. Follow ESLint and Prettier configuration
3. Add comprehensive JSDoc comments
4. Write unit and integration tests with Jest
5. Use Zod for runtime validation where appropriate
6. Add examples in the `examples/` directory
7. Ensure Node.js compatibility (LTS versions)
8. Use semantic versioning for releases

## Related Resources

- [Architecture Standards](../STANDARDS_REPOSITORY/) - Comprehensive architectural guidelines
- [General Guidelines](../general_guidelines/) - Cross-language development practices
- [Main Repository README](../README.md) - Overall project documentation
- [TypeScript Handbook](https://www.typescriptlang.org/docs/) - Official TypeScript documentation
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices) - Node.js guidelines