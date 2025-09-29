/**
 * Express.js integration example for TypeScript prompt templates.
 * Demonstrates how to build a web API that uses prompt templates for AI-powered features.
 */

// Mock Express imports (install with: npm install express @types/express cors helmet)
// import express, { Request, Response, NextFunction } from 'express';
// import cors from 'cors';
// import helmet from 'helmet';

// Mock implementations for demonstration
interface Request {
  body: any;
  params: any;
  query: any;
  headers: any;
}

interface Response {
  json(data: any): void;
  status(code: number): Response;
  send(data: any): void;
}

interface NextFunction {
  (error?: any): void;
}

// Import prompt templates (mock for demonstration)
function scaffolderPlanningPrompt(description: string, settings: any): string {
  return `Generate project plan for: ${description} with settings: ${JSON.stringify(settings)}`;
}

function stepByStepReasoningPrompt(problem: string): string {
  return `Analyze step by step: ${problem}`;
}

function chunkSummaryPromptReadme(text: string): string {
  return `Generate README for: ${text}`;
}

// AI Client interface
interface AIClient {
  complete(prompt: string): Promise<string>;
}

class MockAIClient implements AIClient {
  async complete(prompt: string): Promise<string> {
    // Simulate AI processing
    await new Promise(resolve => setTimeout(resolve, 500));
    
    if (prompt.includes('project plan')) {
      return JSON.stringify({
        project: { name: "GeneratedProject", language: "typescript" },
        tree: [{ path: "src/index.ts", purpose: "Entry point" }]
      });
    }
    
    return `AI response for: ${prompt.slice(0, 50)}...`;
  }
}

// Request/Response DTOs
interface ScaffoldRequest {
  description: string;
  language: string;
  template: string;
  packageManager?: string;
  license?: string;
}

interface AnalysisRequest {
  problem: string;
  analysisType: 'reasoning' | 'summary' | 'stakeholder';
}

interface DocumentRequest {
  content: string;
  outputFormat: 'readme' | 'summary' | 'analysis';
}

// Service layer for AI operations
class AIPromptService {
  constructor(private aiClient: AIClient) {}

  async generateProjectScaffold(request: ScaffoldRequest): Promise<any> {
    const settings = {
      language: request.language,
      template: request.template,
      packageManager: request.packageManager || 'npm',
      license: request.license || 'MIT'
    };

    const prompt = scaffolderPlanningPrompt(request.description, settings);
    const response = await this.aiClient.complete(prompt);
    
    try {
      return JSON.parse(response);
    } catch (error) {
      throw new Error('Failed to parse AI response as JSON');
    }
  }

  async performAnalysis(request: AnalysisRequest): Promise<string> {
    let prompt: string;
    
    switch (request.analysisType) {
      case 'reasoning':
        prompt = stepByStepReasoningPrompt(request.problem);
        break;
      case 'summary':
        prompt = `Summarize the following: ${request.problem}`;
        break;
      case 'stakeholder':
        prompt = `Identify stakeholders in: ${request.problem}`;
        break;
      default:
        throw new Error('Invalid analysis type');
    }

    return this.aiClient.complete(prompt);
  }

  async processDocument(request: DocumentRequest): Promise<string> {
    let prompt: string;
    
    switch (request.outputFormat) {
      case 'readme':
        prompt = chunkSummaryPromptReadme(request.content);
        break;
      case 'summary':
        prompt = `Create a summary of: ${request.content}`;
        break;
      case 'analysis':
        prompt = `Analyze the following document: ${request.content}`;
        break;
      default:
        throw new Error('Invalid output format');
    }

    return this.aiClient.complete(prompt);
  }
}

// Controller layer
class AIPromptController {
  constructor(private promptService: AIPromptService) {}

  async scaffoldProject(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const request: ScaffoldRequest = req.body;
      
      // Validation
      if (!request.description || !request.language || !request.template) {
        res.status(400).json({
          error: 'Missing required fields: description, language, template'
        });
        return;
      }

      const result = await this.promptService.generateProjectScaffold(request);
      
      res.json({
        success: true,
        data: result,
        metadata: {
          generatedAt: new Date().toISOString(),
          language: request.language,
          template: request.template
        }
      });
    } catch (error) {
      next(error);
    }
  }

  async analyzeContent(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const request: AnalysisRequest = req.body;
      
      if (!request.problem || !request.analysisType) {
        res.status(400).json({
          error: 'Missing required fields: problem, analysisType'
        });
        return;
      }

      const result = await this.promptService.performAnalysis(request);
      
      res.json({
        success: true,
        data: {
          analysis: result,
          analysisType: request.analysisType
        },
        metadata: {
          analyzedAt: new Date().toISOString(),
          inputLength: request.problem.length
        }
      });
    } catch (error) {
      next(error);
    }
  }

  async processDocument(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const request: DocumentRequest = req.body;
      
      if (!request.content || !request.outputFormat) {
        res.status(400).json({
          error: 'Missing required fields: content, outputFormat'
        });
        return;
      }

      // Handle large documents by chunking
      if (request.content.length > 10000) {
        const result = await this.processLargeDocument(request);
        res.json(result);
        return;
      }

      const result = await this.promptService.processDocument(request);
      
      res.json({
        success: true,
        data: {
          processedContent: result,
          outputFormat: request.outputFormat
        },
        metadata: {
          processedAt: new Date().toISOString(),
          inputLength: request.content.length,
          outputLength: result.length
        }
      });
    } catch (error) {
      next(error);
    }
  }

  private async processLargeDocument(request: DocumentRequest): Promise<any> {
    // Split large document into chunks
    const chunkSize = 5000;
    const chunks = [];
    
    for (let i = 0; i < request.content.length; i += chunkSize) {
      chunks.push(request.content.slice(i, i + chunkSize));
    }

    // Process chunks concurrently
    const chunkPromises = chunks.map(async (chunk, index) => {
      const chunkRequest = { ...request, content: chunk };
      const result = await this.promptService.processDocument(chunkRequest);
      return { index, result };
    });

    const chunkResults = await Promise.all(chunkPromises);
    
    // Sort results by index and combine
    const sortedResults = chunkResults
      .sort((a, b) => a.index - b.index)
      .map(cr => cr.result);

    return {
      success: true,
      data: {
        processedContent: sortedResults.join('\n\n'),
        outputFormat: request.outputFormat,
        chunked: true,
        totalChunks: chunks.length
      },
      metadata: {
        processedAt: new Date().toISOString(),
        inputLength: request.content.length,
        outputLength: sortedResults.join('\n\n').length
      }
    };
  }

  // Batch processing endpoint
  async batchProcess(req: Request, res: Response, next: NextFunction): Promise<void> {
    try {
      const requests: DocumentRequest[] = req.body.requests;
      
      if (!Array.isArray(requests) || requests.length === 0) {
        res.status(400).json({
          error: 'requests must be a non-empty array'
        });
        return;
      }

      if (requests.length > 10) {
        res.status(400).json({
          error: 'Maximum 10 requests allowed per batch'
        });
        return;
      }

      // Process all requests concurrently
      const batchPromises = requests.map(async (request, index) => {
        try {
          const result = await this.promptService.processDocument(request);
          return {
            index,
            success: true,
            data: result,
            error: null
          };
        } catch (error) {
          return {
            index,
            success: false,
            data: null,
            error: error instanceof Error ? error.message : 'Unknown error'
          };
        }
      });

      const batchResults = await Promise.all(batchPromises);
      
      const successCount = batchResults.filter(r => r.success).length;
      const failureCount = batchResults.length - successCount;

      res.json({
        success: true,
        data: {
          results: batchResults.sort((a, b) => a.index - b.index),
          summary: {
            total: requests.length,
            successful: successCount,
            failed: failureCount
          }
        },
        metadata: {
          processedAt: new Date().toISOString(),
          batchSize: requests.length
        }
      });
    } catch (error) {
      next(error);
    }
  }
}

// Middleware for rate limiting (mock implementation)
class RateLimiter {
  private requests = new Map<string, number[]>();
  
  constructor(private maxRequests: number, private windowMs: number) {}

  middleware() {
    return (req: Request, res: Response, next: NextFunction) => {
      const clientId = req.headers['x-client-id'] as string || 'anonymous';
      const now = Date.now();
      
      if (!this.requests.has(clientId)) {
        this.requests.set(clientId, []);
      }
      
      const clientRequests = this.requests.get(clientId)!;
      
      // Remove old requests outside the window
      const validRequests = clientRequests.filter(time => now - time < this.windowMs);
      
      if (validRequests.length >= this.maxRequests) {
        res.status(429).json({
          error: 'Rate limit exceeded',
          retryAfter: Math.ceil(this.windowMs / 1000)
        });
        return;
      }
      
      validRequests.push(now);
      this.requests.set(clientId, validRequests);
      
      next();
    };
  }
}

// Error handling middleware
function errorHandler(error: any, req: Request, res: Response, next: NextFunction): void {
  console.error('API Error:', error);

  if (error.name === 'ValidationError') {
    res.status(400).json({
      error: 'Validation failed',
      details: error.message
    });
    return;
  }

  if (error.message?.includes('rate limit')) {
    res.status(429).json({
      error: 'Rate limit exceeded',
      message: error.message
    });
    return;
  }

  res.status(500).json({
    error: 'Internal server error',
    message: process.env.NODE_ENV === 'development' ? error.message : 'Something went wrong'
  });
}

// Mock Express app setup
function createApp(): any {
  // This would be the actual Express app setup
  const mockApp = {
    use: (middleware: any) => console.log('Added middleware'),
    post: (path: string, handler: any) => console.log(`Added POST route: ${path}`),
    get: (path: string, handler: any) => console.log(`Added GET route: ${path}`),
    listen: (port: number, callback: () => void) => {
      console.log(`Mock server would start on port ${port}`);
      callback();
    }
  };

  return mockApp;
}

// Application setup function
function setupApplication(): any {
  const app = createApp();
  
  // Initialize services
  const aiClient = new MockAIClient();
  const promptService = new AIPromptService(aiClient);
  const controller = new AIPromptController(promptService);
  const rateLimiter = new RateLimiter(100, 60000); // 100 requests per minute

  // Middleware
  // app.use(helmet());
  // app.use(cors());
  // app.use(express.json({ limit: '10mb' }));
  // app.use(rateLimiter.middleware());

  // Routes
  // app.post('/api/scaffold', controller.scaffoldProject.bind(controller));
  // app.post('/api/analyze', controller.analyzeContent.bind(controller));
  // app.post('/api/document/process', controller.processDocument.bind(controller));
  // app.post('/api/document/batch', controller.batchProcess.bind(controller));

  // Health check
  // app.get('/health', (req: Request, res: Response) => {
  //   res.json({ status: 'healthy', timestamp: new Date().toISOString() });
  // });

  // Error handling
  // app.use(errorHandler);

  console.log('Application setup completed (mock)');
  return app;
}

// Demo function
async function demonstrateExpressIntegration(): Promise<void> {
  console.log('=== Express.js Integration Demo ===');
  
  const app = setupApplication();
  
  // Mock some API requests
  const mockRequests = [
    {
      endpoint: '/api/scaffold',
      body: {
        description: "Build a REST API for user management",
        language: "typescript",
        template: "express"
      }
    },
    {
      endpoint: '/api/analyze',
      body: {
        problem: "How to implement authentication?",
        analysisType: "reasoning"
      }
    },
    {
      endpoint: '/api/document/process',
      body: {
        content: "This is a sample document for processing...",
        outputFormat: "readme"
      }
    }
  ];

  console.log('\nMock API requests:');
  mockRequests.forEach((req, index) => {
    console.log(`${index + 1}. POST ${req.endpoint}`);
    console.log(`   Body: ${JSON.stringify(req.body, null, 2)}`);
  });

  // Simulate server startup
  // app.listen(3000, () => {
  //   console.log('Server running on http://localhost:3000');
  // });
  
  console.log('\nExpress integration demo completed');
}

// WebSocket integration example (mock)
class WebSocketPromptService {
  private connections = new Set<any>();

  handleConnection(ws: any): void {
    this.connections.add(ws);
    
    ws.on('message', async (message: string) => {
      try {
        const request = JSON.parse(message);
        await this.handlePromptRequest(ws, request);
      } catch (error) {
        ws.send(JSON.stringify({
          type: 'error',
          error: 'Invalid message format'
        }));
      }
    });

    ws.on('close', () => {
      this.connections.delete(ws);
    });
  }

  private async handlePromptRequest(ws: any, request: any): Promise<void> {
    const { type, prompt, requestId } = request;
    
    try {
      // Simulate streaming response
      ws.send(JSON.stringify({
        type: 'start',
        requestId
      }));

      const aiClient = new MockAIClient();
      const response = await aiClient.complete(prompt);
      
      // Simulate chunked streaming
      const chunks = response.match(/.{1,50}/g) || [];
      
      for (const chunk of chunks) {
        ws.send(JSON.stringify({
          type: 'chunk',
          requestId,
          data: chunk
        }));
        
        await new Promise(resolve => setTimeout(resolve, 100));
      }

      ws.send(JSON.stringify({
        type: 'complete',
        requestId
      }));
    } catch (error) {
      ws.send(JSON.stringify({
        type: 'error',
        requestId,
        error: error instanceof Error ? error.message : 'Unknown error'
      }));
    }
  }
}

function demonstrateWebSocketIntegration(): void {
  console.log('\n=== WebSocket Integration Demo ===');
  
  const wsService = new WebSocketPromptService();
  
  console.log('WebSocket service would handle:');
  console.log('- Real-time prompt processing');
  console.log('- Streaming AI responses');
  console.log('- Multiple concurrent connections');
  console.log('- Request/response correlation');
  
  console.log('\nWebSocket integration demo completed');
}

// Main execution
async function main(): Promise<void> {
  console.log('TypeScript Express Integration Examples');
  console.log('='.repeat(50));

  await demonstrateExpressIntegration();
  demonstrateWebSocketIntegration();

  console.log('\n' + '='.repeat(50));
  console.log('All integration examples completed!');
}

if (require.main === module) {
  main().catch(console.error);
}

export {
  AIPromptService,
  AIPromptController,
  RateLimiter,
  WebSocketPromptService,
  setupApplication
};

/*
// Package.json dependencies for full implementation:
{
  "dependencies": {
    "express": "^4.18.0",
    "@types/express": "^4.17.0",
    "cors": "^2.8.5",
    "@types/cors": "^2.8.0",
    "helmet": "^7.0.0",
    "ws": "^8.14.0",
    "@types/ws": "^8.5.0",
    "express-rate-limit": "^7.1.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "ts-node": "^10.9.0",
    "@types/node": "^20.0.0",
    "nodemon": "^3.0.0"
  }
}
*/