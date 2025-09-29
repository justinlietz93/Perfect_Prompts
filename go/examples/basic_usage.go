package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"strings"
	"sync"
	"time"

	// Import your prompt packages - adjust path as needed
	// "github.com/yourorg/perfect-prompts/go/agent_prompts"
	// "github.com/yourorg/perfect-prompts/go/summary_prompts"
)

// Mock AI Client for demonstration
type AIClient interface {
	Complete(prompt string) (string, error)
	CompleteWithContext(ctx context.Context, prompt string) (string, error)
}

type MockAIClient struct {
	callCount int
	mu        sync.Mutex
}

func (m *MockAIClient) Complete(prompt string) (string, error) {
	return m.CompleteWithContext(context.Background(), prompt)
}

func (m *MockAIClient) CompleteWithContext(ctx context.Context, prompt string) (string, error) {
	m.mu.Lock()
	defer m.mu.Unlock()
	m.callCount++

	// Simulate API delay
	select {
	case <-time.After(100 * time.Millisecond):
	case <-ctx.Done():
		return "", ctx.Err()
	}

	// Mock responses based on prompt content
	if contains(prompt, "project plan") {
		return m.mockProjectPlan(), nil
	} else if contains(prompt, "step-by-step") {
		return m.mockReasoningResponse(), nil
	} else if contains(prompt, "stakeholder") {
		return m.mockStakeholderResponse(), nil
	}

	return fmt.Sprintf("Mock response %d for prompt: %.50s...", m.callCount, prompt), nil
}

func (m *MockAIClient) mockProjectPlan() string {
	plan := map[string]interface{}{
		"project": map[string]interface{}{
			"name":            "TaskManagerAPI",
			"language":        "go",
			"template":        "gin",
			"package_manager": "go mod",
			"license":         "MIT",
		},
		"layers": []string{"presentation", "application", "domain", "infrastructure", "shared", "tests"},
		"tree": []map[string]interface{}{
			{
				"path":    "internal/presentation/handlers/task_handler.go",
				"layer":   "presentation",
				"purpose": "HTTP handlers for task management",
				"prompt":  "",
			},
			{
				"path":    "internal/application/services/task_service.go",
				"layer":   "application",
				"purpose": "Business logic for task operations",
				"prompt":  "",
			},
		},
	}

	jsonData, _ := json.Marshal(plan)
	return string(jsonData)
}

func (m *MockAIClient) mockReasoningResponse() string {
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
4. Add monitoring and observability`
}

func (m *MockAIClient) mockStakeholderResponse() string {
	return `## Project Stakeholders

### Primary Stakeholders
- **Product Owner**: Defines requirements and priorities
- **Development Team**: Implements the solution
- **End Users**: Will use the task management system

### Secondary Stakeholders
- **DevOps Team**: Manages deployment and infrastructure
- **QA Team**: Ensures quality and testing
- **Security Team**: Reviews security requirements`
}

// Helper function to check if string contains substring
func contains(s, substr string) bool {
	return len(s) >= len(substr) && 
		   (s == substr || (len(s) > len(substr) && 
			(s[:len(substr)] == substr || s[len(s)-len(substr):] == substr || 
			 containsSubstring(s, substr))))
}

func containsSubstring(s, substr string) bool {
	for i := 0; i <= len(s)-len(substr); i++ {
		if s[i:i+len(substr)] == substr {
			return true
		}
	}
	return false
}

// Mock prompt functions (replace with actual imports)
func scaffolderPlanningPrompt(description string, settings map[string]string) string {
	return fmt.Sprintf(`You are an expert AI software architect specializing in the Hybrid-Clean architecture.
Your task is to take a user's project description and generate a detailed project plan as a single JSON object.

Project Description: %s
Settings: %v

Generate a comprehensive project plan...`, description, settings)
}

func stepByStepReasoningPrompt(problem string) string {
	return fmt.Sprintf(`You are an expert problem solver. Break down the following problem into clear, logical steps:

Problem: %s

Provide a step-by-step analysis and solution...`, problem)
}

func chunkSummaryPromptReadme(text string) string {
	return fmt.Sprintf(`You are a technical writer AI tasked with creating a section of a project README.md file.
Your job is to analyze the following document segment and extract information relevant to a project's documentation.

Document to analyze:
%s

Generate a README section...`, text)
}

// Project scaffolding example
func demonstrateBasicScaffolding(client AIClient) {
	fmt.Println("=== Project Scaffolding Example ===")

	description := "Build a REST API for task management with user authentication"
	settings := map[string]string{
		"language":       "go",
		"template":       "gin",
		"packageManager": "go mod",
		"license":        "MIT",
	}

	// Step 1: Generate project plan
	planningPrompt := scaffolderPlanningPrompt(description, settings)
	fmt.Printf("Generated planning prompt (%d chars)\n", len(planningPrompt))

	planResponse, err := client.Complete(planningPrompt)
	if err != nil {
		log.Printf("Error generating plan: %v", err)
		return
	}

	var plan map[string]interface{}
	if err := json.Unmarshal([]byte(planResponse), &plan); err != nil {
		log.Printf("Error parsing plan JSON: %v", err)
		return
	}

	project := plan["project"].(map[string]interface{})
	tree := plan["tree"].([]interface{})

	fmt.Printf("Project: %s\n", project["name"])
	fmt.Printf("Files to generate: %d\n", len(tree))

	// Step 2: Generate file prompts would go here
	fmt.Println("File prompt generation completed")
}

// Reasoning workflow example
func demonstrateReasoningWorkflow(client AIClient) {
	fmt.Println("\n=== Reasoning Workflow Example ===")

	problem := "How can we design a scalable microservices architecture for a high-traffic e-commerce platform?"

	reasoningPrompt := stepByStepReasoningPrompt(problem)
	fmt.Printf("Generated reasoning prompt (%d chars)\n", len(reasoningPrompt))

	reasoningResult, err := client.Complete(reasoningPrompt)
	if err != nil {
		log.Printf("Error in reasoning: %v", err)
		return
	}

	fmt.Println("Reasoning Result:")
	fmt.Println(reasoningResult)
}

// Concurrent processing example
func demonstrateConcurrentProcessing(client AIClient) {
	fmt.Println("\n=== Concurrent Processing Example ===")

	problems := []string{
		"Design a caching strategy for high-load systems",
		"Implement fault tolerance in distributed systems", 
		"Optimize database queries for performance",
	}

	var wg sync.WaitGroup
	results := make([]string, len(problems))
	errors := make([]error, len(problems))

	for i, problem := range problems {
		wg.Add(1)
		go func(index int, prob string) {
			defer wg.Done()

			prompt := stepByStepReasoningPrompt(prob)
			result, err := client.Complete(prompt)

			results[index] = result
			errors[index] = err
		}(i, problem)
	}

	wg.Wait()

	for i, problem := range problems {
		if errors[i] != nil {
			fmt.Printf("Problem %d failed: %v\n", i+1, errors[i])
			continue
		}
		fmt.Printf("Problem %d: %s\n", i+1, problem)
		fmt.Printf("Result: %s\n\n", results[i][:100]+"...")
	}
}

// Context and timeout example
func demonstrateContextUsage(client AIClient) {
	fmt.Println("\n=== Context and Timeout Example ===")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	problem := "Explain the principles of clean architecture"
	prompt := stepByStepReasoningPrompt(problem)

	result, err := client.CompleteWithContext(ctx, prompt)
	if err != nil {
		if err == context.DeadlineExceeded {
			fmt.Println("Request timed out")
		} else {
			fmt.Printf("Request failed: %v\n", err)
		}
		return
	}

	fmt.Printf("Result: %s\n", result[:150]+"...")
}

// Error handling and retry example
func demonstrateErrorHandling(client AIClient) {
	fmt.Println("\n=== Error Handling and Retry Example ===")

	type FailingClient struct{}
	
	func (f *FailingClient) Complete(prompt string) (string, error) {
		return "", fmt.Errorf("API rate limit exceeded")
	}
	
	func (f *FailingClient) CompleteWithContext(ctx context.Context, prompt string) (string, error) {
		return "", fmt.Errorf("API rate limit exceeded")
	}

	failingClient := &FailingClient{}

	// Retry function
	retryWithBackoff := func(client AIClient, prompt string, maxRetries int) (string, error) {
		var lastErr error
		
		for attempt := 0; attempt < maxRetries; attempt++ {
			result, err := client.Complete(prompt)
			if err == nil {
				return result, nil
			}
			
			lastErr = err
			fmt.Printf("Attempt %d failed: %v\n", attempt+1, err)
			
			if attempt < maxRetries-1 {
				delay := time.Duration(attempt+1) * time.Second
				time.Sleep(delay)
			}
		}
		
		return "", fmt.Errorf("all %d attempts failed, last error: %w", maxRetries, lastErr)
	}

	prompt := stepByStepReasoningPrompt("Test problem")
	result, err := retryWithBackoff(failingClient, prompt, 3)
	
	if err != nil {
		fmt.Printf("Final result: Failed - %v\n", err)
	} else {
		fmt.Printf("Final result: %s\n", result)
	}
}

// Performance monitoring example
type InstrumentedClient struct {
	client AIClient
	stats  struct {
		totalCalls    int
		totalDuration time.Duration
		mu           sync.Mutex
	}
}

func NewInstrumentedClient(client AIClient) *InstrumentedClient {
	return &InstrumentedClient{client: client}
}

func (i *InstrumentedClient) Complete(prompt string) (string, error) {
	start := time.Now()
	defer func() {
		duration := time.Since(start)
		i.stats.mu.Lock()
		i.stats.totalCalls++
		i.stats.totalDuration += duration
		i.stats.mu.Unlock()
	}()

	return i.client.Complete(prompt)
}

func (i *InstrumentedClient) CompleteWithContext(ctx context.Context, prompt string) (string, error) {
	start := time.Now()
	defer func() {
		duration := time.Since(start)
		i.stats.mu.Lock()
		i.stats.totalCalls++
		i.stats.totalDuration += duration
		i.stats.mu.Unlock()
	}()

	return i.client.CompleteWithContext(ctx, prompt)
}

func (i *InstrumentedClient) Stats() (int, time.Duration) {
	i.stats.mu.Lock()
	defer i.stats.mu.Unlock()
	return i.stats.totalCalls, i.stats.totalDuration
}

func demonstratePerformanceMonitoring() {
	fmt.Println("\n=== Performance Monitoring Example ===")

	baseClient := &MockAIClient{}
	instrumentedClient := NewInstrumentedClient(baseClient)

	// Make several calls
	for i := 0; i < 5; i++ {
		prompt := stepByStepReasoningPrompt(fmt.Sprintf("Problem %d", i+1))
		_, err := instrumentedClient.Complete(prompt)
		if err != nil {
			log.Printf("Call %d failed: %v", i+1, err)
		}
	}

	totalCalls, totalDuration := instrumentedClient.Stats()
	avgDuration := totalDuration / time.Duration(totalCalls)

	fmt.Printf("Performance Stats:\n")
	fmt.Printf("  Total calls: %d\n", totalCalls)
	fmt.Printf("  Total duration: %v\n", totalDuration)
	fmt.Printf("  Average duration: %v\n", avgDuration)
}

func main() {
	fmt.Println("Go Prompt Templates - Basic Usage Examples")
	fmt.Println(strings.Repeat("=", 50))

	client := &MockAIClient{}

	demonstrateBasicScaffolding(client)
	demonstrateReasoningWorkflow(client)
	demonstrateConcurrentProcessing(client)
	demonstrateContextUsage(client)
	demonstrateErrorHandling(client)
	demonstratePerformanceMonitoring()

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("All examples completed successfully!")
}