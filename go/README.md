# Go Prompt Templates

This directory contains Go implementations of prompt templates designed for agentic AI systems. These templates provide structured, reusable prompts for various AI-assisted development and analysis tasks, following Go's idiomatic patterns and type safety principles.

## Overview

The Go prompt templates are organized into two main categories:

### 🤖 Agent Prompts (`agent_prompts/`)
Specialized prompts for AI agents that perform specific development and analysis tasks:

- **`agentDesigner.go`** - Design single-agent and multi-agent AI systems with comprehensive settings
- **`projectScaffolder.go`** - Generate project structures using Hybrid-Clean architecture
- **`mermaidDesigner.go`** - Create and validate Mermaid.js diagrams from specifications
- **`promptEnhancer.go`** - Improve and optimize existing prompts with advanced techniques
- **`reasoner.go`** - Perform step-by-step logical reasoning and problem-solving
- **`rewriter.go`** - Rewrite content with specific styles, tones, and requirements
- **`citations.go`** - Generate proper academic and professional citations
- **`mathFormatter.go`** - Format mathematical expressions and equations
- **`styleExtractor.go`** - Extract and analyze writing styles and patterns
- **`highlightExtraction.go`** - Extract key highlights and insights from content
- **`nextSteps.go`** - Generate actionable next steps from analysis results
- **`requestSplitter.go`** - Break down complex requests into manageable sub-tasks

### 📊 Summary Prompts (`summary_prompts/`)
Templates for analyzing, summarizing, and structuring content:

- **`readme.go`** - Generate comprehensive README documentation
- **`summarize.go`** - Create concise summaries of complex content
- **`checklist.go`** - Convert content into actionable checklists
- **`timeline.go`** - Extract and organize temporal information
- **`processFlow.go`** - Document step-by-step processes and workflows
- **`stakeholderMap.go`** - Identify and map project stakeholders
- **`riskRegister.go`** - Identify and assess project risks
- **`decisionMatrix.go`** - Structure decision-making processes
- **`swotAnalysis.go`** - Perform SWOT analysis
- **`entityRelationshipDigest.go`** - Extract entity relationships from content
- **`systemWalkthrough.go`** - Generate system documentation and walkthroughs
- **`reverseEngineering.go`** - Analyze and document existing systems

## Usage in Agentic Projects

### Basic Usage Pattern

```go
package main

import (
    "fmt"
    "github.com/yourorg/project/go/agent_prompts"
    "github.com/yourorg/project/go/summary_prompts"
)

func main() {
    // Generate a project scaffolding prompt
    projectDescription := "Build a REST API for task management"
    settings := agent_prompts.ScaffolderSettings{
        Language:       "go",
        Template:       "gin",
        PackageManager: "go mod",
        License:        "MIT",
    }
    
    scaffoldPrompt := agent_prompts.ScaffolderPlanningPrompt(projectDescription, settings)
    
    // Use with your AI client
    response, err := aiClient.Complete(scaffoldPrompt)
    if err != nil {
        log.Fatal(err)
    }
    
    fmt.Println(response)
}
```

### Type-Safe Configuration

Go's type system ensures compile-time safety for prompt configurations:

```go
// Agent Designer with strongly typed settings
type AgentDesignerSettings struct {
    SystemType   string                 `json:"systemType"`
    Goal         string                 `json:"goal"`
    Trigger      string                 `json:"trigger"`
    Provider     string                 `json:"provider"`
    Capabilities map[string]interface{} `json:"capabilities"`
}

settings := agent_prompts.AgentDesignerSettings{
    SystemType: "multiAgent",
    Goal:       "Design a document processing system",
    Trigger:    "file_upload",
    Provider:   "openai",
    Capabilities: map[string]interface{}{
        "web_search": true,
        "file_io":    true,
        "email":      false,
    },
}

prompt := agent_prompts.AgentDesignerPromptTemplate(settings)
```

### Integration with Go AI Libraries

#### OpenAI Go Client Integration
```go
package main

import (
    "context"
    "fmt"
    "github.com/sashabaranov/go-openai"
    "github.com/yourorg/project/go/agent_prompts"
)

func main() {
    client := openai.NewClient("your-api-key")
    
    // Generate reasoning prompt
    problem := "Design a scalable microservices architecture"
    reasoningPrompt := agent_prompts.StepByStepReasoningPrompt(problem)
    
    resp, err := client.CreateChatCompletion(
        context.Background(),
        openai.ChatCompletionRequest{
            Model: openai.GPT4,
            Messages: []openai.ChatCompletionMessage{
                {
                    Role:    openai.ChatMessageRoleUser,
                    Content: reasoningPrompt,
                },
            },
        },
    )
    
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    
    fmt.Println(resp.Choices[0].Message.Content)
}
```

#### Custom AI Client Interface
```go
type AIClient interface {
    Complete(prompt string) (string, error)
    CompleteWithSettings(prompt string, settings CompletionSettings) (string, error)
}

type PromptProcessor struct {
    client AIClient
}

func (p *PromptProcessor) ProcessDocumentAnalysis(document string) (*AnalysisResult, error) {
    // Step 1: Generate summary
    summaryPrompt := summary_prompts.ChunkSummaryPromptReadme(document)
    summary, err := p.client.Complete(summaryPrompt)
    if err != nil {
        return nil, fmt.Errorf("summary generation failed: %w", err)
    }
    
    // Step 2: Extract stakeholders
    stakeholderPrompt := summary_prompts.StakeholderMappingPrompt(document)
    stakeholders, err := p.client.Complete(stakeholderPrompt)
    if err != nil {
        return nil, fmt.Errorf("stakeholder extraction failed: %w", err)
    }
    
    return &AnalysisResult{
        Summary:      summary,
        Stakeholders: stakeholders,
    }, nil
}
```

### Workflow Examples

#### Concurrent Document Processing
```go
func ProcessDocumentsConcurrently(documents []string, client AIClient) ([]*DocumentAnalysis, error) {
    results := make([]*DocumentAnalysis, len(documents))
    errors := make([]error, len(documents))
    
    var wg sync.WaitGroup
    
    for i, doc := range documents {
        wg.Add(1)
        go func(index int, document string) {
            defer wg.Done()
            
            // Generate analysis prompt
            analysisPrompt := summary_prompts.SystemWalkthroughPrompt(document)
            result, err := client.Complete(analysisPrompt)
            
            if err != nil {
                errors[index] = err
                return
            }
            
            results[index] = &DocumentAnalysis{
                Document: document,
                Analysis: result,
                ProcessedAt: time.Now(),
            }
        }(i, doc)
    }
    
    wg.Wait()
    
    // Check for errors
    for _, err := range errors {
        if err != nil {
            return nil, fmt.Errorf("processing failed: %w", err)
        }
    }
    
    return results, nil
}
```

#### Project Scaffolding Pipeline
```go
type ProjectScaffolder struct {
    client AIClient
}

func (ps *ProjectScaffolder) ScaffoldProject(description string, settings ScaffolderSettings) (*ProjectPlan, error) {
    // Step 1: Generate project plan
    planningPrompt := agent_prompts.ScaffolderPlanningPrompt(description, settings)
    planResponse, err := ps.client.Complete(planningPrompt)
    if err != nil {
        return nil, fmt.Errorf("planning failed: %w", err)
    }
    
    var plan ProjectPlan
    if err := json.Unmarshal([]byte(planResponse), &plan); err != nil {
        return nil, fmt.Errorf("invalid plan format: %w", err)
    }
    
    // Step 2: Generate file prompts
    filePrompts := make(map[string]string)
    for _, fileItem := range plan.Tree {
        fileData, _ := json.Marshal(fileItem)
        projectData, _ := json.Marshal(plan.Project)
        
        filePrompt := agent_prompts.ScaffolderFilePromptGeneration(
            string(projectData),
            string(fileData),
        )
        filePrompts[fileItem.Path] = filePrompt
    }
    
    plan.FilePrompts = filePrompts
    return &plan, nil
}
```

## Best Practices

### 1. **Error Handling**
Always handle errors gracefully and provide meaningful error messages:
```go
if err != nil {
    return fmt.Errorf("failed to generate prompt for %s: %w", operation, err)
}
```

### 2. **Context Management**
Use Go's context package for cancellation and timeouts:
```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()

response, err := client.CompleteWithContext(ctx, prompt)
```

### 3. **Structured Logging**
Use structured logging for better observability:
```go
import "log/slog"

slog.Info("Generating prompt",
    "type", "scaffolder",
    "project", settings.Template,
    "language", settings.Language)
```

### 4. **Configuration Management**
Use environment variables and configuration structs:
```go
type Config struct {
    OpenAIKey    string `env:"OPENAI_API_KEY"`
    Model        string `env:"AI_MODEL" envDefault:"gpt-4"`
    Temperature  float32 `env:"AI_TEMPERATURE" envDefault:"0.7"`
    MaxTokens    int    `env:"AI_MAX_TOKENS" envDefault:"2048"`
}
```

### 5. **Testing**
Write comprehensive tests with table-driven patterns:
```go
func TestAgentDesignerPrompt(t *testing.T) {
    tests := []struct {
        name        string
        settings    AgentDesignerSettings
        expectError bool
        contains    []string
    }{
        {
            name: "single agent system",
            settings: AgentDesignerSettings{
                SystemType: "singleAgent",
                Goal:       "Test goal",
            },
            contains: []string{"single agent", "fine-tuning"},
        },
        // More test cases...
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := AgentDesignerPromptTemplate(tt.settings)
            
            for _, expectedText := range tt.contains {
                if !strings.Contains(result, expectedText) {
                    t.Errorf("Expected prompt to contain %q", expectedText)
                }
            }
        })
    }
}
```

## Integration Examples

See the `examples/` directory for complete, runnable examples demonstrating:
- OpenAI Go client integration
- Concurrent prompt processing
- HTTP service integration with Gin
- gRPC service examples
- CLI tool implementations
- Testing patterns and mocks

## Dependencies

Core prompt templates have no external dependencies. Integration examples may require:

```go
// go.mod
module github.com/yourorg/project

go 1.21

require (
    github.com/sashabaranov/go-openai v1.17.9
    github.com/gin-gonic/gin v1.9.1
    github.com/spf13/cobra v1.8.0
    github.com/spf13/viper v1.17.0
)
```

## Performance Considerations

- Use goroutines for concurrent prompt processing
- Implement connection pooling for AI API clients
- Cache frequently used prompts
- Use streaming responses for long-running operations
- Implement circuit breakers for external API calls

## Contributing

When adding new prompt templates:
1. Follow Go naming conventions and idiomatic patterns
2. Include comprehensive documentation and examples
3. Add type-safe configuration structs where applicable
4. Write table-driven tests with good coverage
5. Use structured logging for observability
6. Ensure thread-safety for concurrent usage

## Related Resources

- [Architecture Standards](../STANDARDS_REPOSITORY/) - Comprehensive architectural guidelines
- [General Guidelines](../general_guidelines/) - Cross-language development practices
- [Main Repository README](../README.md) - Overall project documentation
- [Go Best Practices](https://golang.org/doc/effective_go) - Official Go guidelines