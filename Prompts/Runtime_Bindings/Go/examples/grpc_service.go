package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"strings"
	"sync"
	"time"

	// Mock gRPC imports (install with: go get google.golang.org/grpc)
	// "google.golang.org/grpc"
	// "google.golang.org/grpc/codes"
	// "google.golang.org/grpc/status"
)

// Mock gRPC types for demonstration
type UnaryServerInterceptor func(ctx context.Context, req interface{}, info *UnaryServerInfo, handler UnaryHandler) (interface{}, error)
type UnaryServerInfo struct {
	FullMethod string
}
type UnaryHandler func(ctx context.Context, req interface{}) (interface{}, error)

// Mock prompt templates (would import from your actual modules)
func scaffolderPlanningPrompt(description string, settings map[string]string) string {
	return fmt.Sprintf("Generate project plan for: %s with settings: %v", description, settings)
}

func stepByStepReasoningPrompt(problem string) string {
	return fmt.Sprintf("Analyze step by step: %s", problem)
}

func chunkSummaryPromptReadme(text string) string {
	return fmt.Sprintf("Generate README for: %s", text)
}

// AI Client interface
type AIClient interface {
	Complete(ctx context.Context, prompt string) (string, error)
}

type MockAIClient struct {
	requestCount int
	mu           sync.Mutex
}

func (m *MockAIClient) Complete(ctx context.Context, prompt string) (string, error) {
	m.mu.Lock()
	defer m.mu.Unlock()
	m.requestCount++

	// Simulate processing time
	select {
	case <-time.After(200 * time.Millisecond):
	case <-ctx.Done():
		return "", ctx.Err()
	}

	if strings.Contains(prompt, "project plan") {
		return m.mockProjectPlan(), nil
	} else if strings.Contains(prompt, "step-by-step") {
		return m.mockReasoningResponse(), nil
	}

	return fmt.Sprintf("Mock AI response %d for: %s", m.requestCount, prompt[:50]), nil
}

func (m *MockAIClient) mockProjectPlan() string {
	plan := map[string]interface{}{
		"project": map[string]interface{}{
			"name":            "gRPCGeneratedProject",
			"language":        "go",
			"template":        "grpc",
			"package_manager": "go mod",
			"license":         "MIT",
		},
		"layers": []string{"presentation", "application", "domain", "infrastructure"},
		"tree": []map[string]interface{}{
			{
				"path":    "internal/grpc/server.go",
				"layer":   "presentation",
				"purpose": "gRPC server implementation",
			},
			{
				"path":    "internal/service/business_service.go",
				"layer":   "application",
				"purpose": "Business logic service",
			},
		},
	}

	jsonData, _ := json.Marshal(plan)
	return string(jsonData)
}

func (m *MockAIClient) mockReasoningResponse() string {
	return `**Step 1: Problem Analysis**
Understand the core requirements and constraints.

**Step 2: Solution Design**
Design a scalable and maintainable approach.

**Step 3: Implementation Strategy**
Define the technical approach and tools.

**Step 4: Quality Assurance**
Establish testing and validation criteria.`
}

// gRPC Service Request/Response types
type ScaffoldRequest struct {
	Description    string            `json:"description"`
	Language       string            `json:"language"`
	Template       string            `json:"template"`
	PackageManager string            `json:"package_manager,omitempty"`
	License        string            `json:"license,omitempty"`
}

type ScaffoldResponse struct {
	Success   bool        `json:"success"`
	Plan      interface{} `json:"plan,omitempty"`
	Error     string      `json:"error,omitempty"`
	Timestamp time.Time   `json:"timestamp"`
}

type AnalysisRequest struct {
	Problem      string `json:"problem"`
	AnalysisType string `json:"analysis_type"`
}

type AnalysisResponse struct {
	Success   bool      `json:"success"`
	Result    string    `json:"result,omitempty"`
	Error     string    `json:"error,omitempty"`
	Timestamp time.Time `json:"timestamp"`
}

type DocumentRequest struct {
	Content      string `json:"content"`
	OutputFormat string `json:"output_format"`
}

type DocumentResponse struct {
	Success      bool      `json:"success"`
	ProcessedContent string `json:"processed_content,omitempty"`
	Error        string    `json:"error,omitempty"`
	Timestamp    time.Time `json:"timestamp"`
}

// Stream response for real-time processing
type StreamResponse struct {
	RequestId string `json:"request_id"`
	Type      string `json:"type"` // "start", "chunk", "complete", "error"
	Data      string `json:"data,omitempty"`
	Error     string `json:"error,omitempty"`
}

// gRPC Service implementation
type PromptService struct {
	aiClient AIClient
	logger   *log.Logger
}

func NewPromptService(aiClient AIClient) *PromptService {
	return &PromptService{
		aiClient: aiClient,
		logger:   log.New(log.Writer(), "[PromptService] ", log.LstdFlags),
	}
}

func (s *PromptService) ScaffoldProject(ctx context.Context, req *ScaffoldRequest) (*ScaffoldResponse, error) {
	s.logger.Printf("ScaffoldProject called: %s", req.Description)

	// Validate request
	if req.Description == "" || req.Language == "" || req.Template == "" {
		return &ScaffoldResponse{
			Success:   false,
			Error:     "Missing required fields: description, language, template",
			Timestamp: time.Now(),
		}, nil
	}

	// Prepare settings
	settings := map[string]string{
		"language":       req.Language,
		"template":       req.Template,
		"packageManager": req.PackageManager,
		"license":        req.License,
	}

	if settings["packageManager"] == "" {
		settings["packageManager"] = "go mod"
	}
	if settings["license"] == "" {
		settings["license"] = "MIT"
	}

	// Generate project plan
	prompt := scaffolderPlanningPrompt(req.Description, settings)
	response, err := s.aiClient.Complete(ctx, prompt)
	if err != nil {
		s.logger.Printf("AI client error: %v", err)
		return &ScaffoldResponse{
			Success:   false,
			Error:     fmt.Sprintf("AI processing failed: %v", err),
			Timestamp: time.Now(),
		}, nil
	}

	// Parse JSON response
	var plan interface{}
	if err := json.Unmarshal([]byte(response), &plan); err != nil {
		s.logger.Printf("JSON parse error: %v", err)
		return &ScaffoldResponse{
			Success:   false,
			Error:     "Failed to parse AI response",
			Timestamp: time.Now(),
		}, nil
	}

	return &ScaffoldResponse{
		Success:   true,
		Plan:      plan,
		Timestamp: time.Now(),
	}, nil
}

func (s *PromptService) AnalyzeProblem(ctx context.Context, req *AnalysisRequest) (*AnalysisResponse, error) {
	s.logger.Printf("AnalyzeProblem called: %s (type: %s)", req.Problem[:min(50, len(req.Problem))], req.AnalysisType)

	if req.Problem == "" {
		return &AnalysisResponse{
			Success:   false,
			Error:     "Problem field is required",
			Timestamp: time.Now(),
		}, nil
	}

	var prompt string
	switch req.AnalysisType {
	case "reasoning", "":
		prompt = stepByStepReasoningPrompt(req.Problem)
	case "summary":
		prompt = fmt.Sprintf("Summarize the following: %s", req.Problem)
	case "stakeholder":
		prompt = fmt.Sprintf("Identify stakeholders in: %s", req.Problem)
	default:
		return &AnalysisResponse{
			Success:   false,
			Error:     fmt.Sprintf("Unknown analysis type: %s", req.AnalysisType),
			Timestamp: time.Now(),
		}, nil
	}

	result, err := s.aiClient.Complete(ctx, prompt)
	if err != nil {
		s.logger.Printf("AI client error: %v", err)
		return &AnalysisResponse{
			Success:   false,
			Error:     fmt.Sprintf("AI processing failed: %v", err),
			Timestamp: time.Now(),
		}, nil
	}

	return &AnalysisResponse{
		Success:   true,
		Result:    result,
		Timestamp: time.Now(),
	}, nil
}

func (s *PromptService) ProcessDocument(ctx context.Context, req *DocumentRequest) (*DocumentResponse, error) {
	s.logger.Printf("ProcessDocument called: %d chars (format: %s)", len(req.Content), req.OutputFormat)

	if req.Content == "" {
		return &DocumentResponse{
			Success:   false,
			Error:     "Content field is required",
			Timestamp: time.Now(),
		}, nil
	}

	var prompt string
	switch req.OutputFormat {
	case "readme", "":
		prompt = chunkSummaryPromptReadme(req.Content)
	case "summary":
		prompt = fmt.Sprintf("Create a summary of: %s", req.Content)
	case "analysis":
		prompt = fmt.Sprintf("Analyze the following document: %s", req.Content)
	default:
		return &DocumentResponse{
			Success:   false,
			Error:     fmt.Sprintf("Unknown output format: %s", req.OutputFormat),
			Timestamp: time.Now(),
		}, nil
	}

	result, err := s.aiClient.Complete(ctx, prompt)
	if err != nil {
		s.logger.Printf("AI client error: %v", err)
		return &DocumentResponse{
			Success:   false,
			Error:     fmt.Sprintf("AI processing failed: %v", err),
			Timestamp: time.Now(),
		}, nil
	}

	return &DocumentResponse{
		Success:          true,
		ProcessedContent: result,
		Timestamp:        time.Now(),
	}, nil
}

// Streaming service for real-time processing
func (s *PromptService) StreamAnalysis(req *AnalysisRequest, stream interface{}) error {
	s.logger.Printf("StreamAnalysis called: %s", req.Problem[:min(50, len(req.Problem))])

	requestId := fmt.Sprintf("req_%d", time.Now().UnixNano())

	// Send start signal
	startResponse := &StreamResponse{
		RequestId: requestId,
		Type:      "start",
		Data:      "Starting analysis...",
	}
	s.sendStreamResponse(stream, startResponse)

	// Generate prompt
	prompt := stepByStepReasoningPrompt(req.Problem)

	// Simulate streaming by getting full response and chunking it
	ctx := context.Background()
	result, err := s.aiClient.Complete(ctx, prompt)
	if err != nil {
		errorResponse := &StreamResponse{
			RequestId: requestId,
			Type:      "error",
			Error:     err.Error(),
		}
		s.sendStreamResponse(stream, errorResponse)
		return err
	}

	// Stream response in chunks
	chunks := s.chunkResponse(result, 100) // 100 chars per chunk
	for i, chunk := range chunks {
		chunkResponse := &StreamResponse{
			RequestId: requestId,
			Type:      "chunk",
			Data:      chunk,
		}
		s.sendStreamResponse(stream, chunkResponse)

		// Simulate processing time
		time.Sleep(100 * time.Millisecond)

		// Check if client disconnected (in real gRPC)
		if i%5 == 0 { // Check every 5 chunks
			select {
			case <-ctx.Done():
				return ctx.Err()
			default:
			}
		}
	}

	// Send completion signal
	completeResponse := &StreamResponse{
		RequestId: requestId,
		Type:      "complete",
		Data:      "Analysis completed",
	}
	s.sendStreamResponse(stream, completeResponse)

	return nil
}

func (s *PromptService) sendStreamResponse(stream interface{}, response *StreamResponse) {
	// In real gRPC, this would be: stream.Send(response)
	jsonData, _ := json.Marshal(response)
	s.logger.Printf("Stream: %s", string(jsonData))
}

func (s *PromptService) chunkResponse(text string, chunkSize int) []string {
	var chunks []string
	for i := 0; i < len(text); i += chunkSize {
		end := i + chunkSize
		if end > len(text) {
			end = len(text)
		}
		chunks = append(chunks, text[i:end])
	}
	return chunks
}

// Middleware for logging and monitoring
func LoggingInterceptor(logger *log.Logger) UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *UnaryServerInfo, handler UnaryHandler) (interface{}, error) {
		start := time.Now()
		
		logger.Printf("Starting %s", info.FullMethod)
		
		resp, err := handler(ctx, req)
		
		duration := time.Since(start)
		if err != nil {
			logger.Printf("Completed %s with error in %v: %v", info.FullMethod, duration, err)
		} else {
			logger.Printf("Completed %s successfully in %v", info.FullMethod, duration)
		}
		
		return resp, err
	}
}

// Rate limiting middleware
type RateLimiter struct {
	requests map[string][]time.Time
	mu       sync.RWMutex
	limit    int
	window   time.Duration
}

func NewRateLimiter(limit int, window time.Duration) *RateLimiter {
	return &RateLimiter{
		requests: make(map[string][]time.Time),
		limit:    limit,
		window:   window,
	}
}

func (rl *RateLimiter) Allow(clientID string) bool {
	rl.mu.Lock()
	defer rl.mu.Unlock()

	now := time.Now()
	requests := rl.requests[clientID]

	// Remove old requests outside the window
	var validRequests []time.Time
	for _, reqTime := range requests {
		if now.Sub(reqTime) < rl.window {
			validRequests = append(validRequests, reqTime)
		}
	}

	if len(validRequests) >= rl.limit {
		return false
	}

	validRequests = append(validRequests, now)
	rl.requests[clientID] = validRequests
	return true
}

func (rl *RateLimiter) Interceptor() UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *UnaryServerInfo, handler UnaryHandler) (interface{}, error) {
		// In real implementation, extract client ID from context/metadata
		clientID := "default_client"
		
		if !rl.Allow(clientID) {
			return nil, fmt.Errorf("rate limit exceeded")
		}
		
		return handler(ctx, req)
	}
}

// Health check service
type HealthService struct {
	promptService *PromptService
}

func (h *HealthService) Check(ctx context.Context) (map[string]interface{}, error) {
	// Test AI client connectivity
	testPrompt := "Health check test"
	_, err := h.promptService.aiClient.Complete(ctx, testPrompt)
	
	status := map[string]interface{}{
		"status":    "healthy",
		"timestamp": time.Now(),
		"services": map[string]string{
			"ai_client": "healthy",
		},
	}
	
	if err != nil {
		status["status"] = "unhealthy"
		status["services"].(map[string]string)["ai_client"] = "unhealthy: " + err.Error()
	}
	
	return status, nil
}

// Server setup and configuration
type ServerConfig struct {
	Port         int
	EnableTLS    bool
	CertFile     string
	KeyFile      string
	RateLimit    int
	RateWindow   time.Duration
	ReadTimeout  time.Duration
	WriteTimeout time.Duration
}

func DefaultServerConfig() *ServerConfig {
	return &ServerConfig{
		Port:         8080,
		EnableTLS:    false,
		RateLimit:    100,
		RateWindow:   time.Minute,
		ReadTimeout:  30 * time.Second,
		WriteTimeout: 30 * time.Second,
	}
}

func SetupServer(config *ServerConfig) error {
	// Initialize services
	aiClient := &MockAIClient{}
	promptService := NewPromptService(aiClient)
	healthService := &HealthService{promptService: promptService}
	
	// Setup middleware
	logger := log.New(log.Writer(), "[gRPC] ", log.LstdFlags)
	rateLimiter := NewRateLimiter(config.RateLimit, config.RateWindow)
	
	// Mock gRPC server setup (in real implementation)
	// interceptors := []grpc.UnaryServerInterceptor{
	//     LoggingInterceptor(logger),
	//     rateLimiter.Interceptor(),
	// }
	// 
	// server := grpc.NewServer(
	//     grpc.ChainUnaryInterceptor(interceptors...),
	// )

	// Register services
	// pb.RegisterPromptServiceServer(server, promptService)
	// grpc_health_v1.RegisterHealthServer(server, healthService)

	// Start server
	address := fmt.Sprintf(":%d", config.Port)
	logger.Printf("Mock gRPC server would start on %s", address)
	
	// lis, err := net.Listen("tcp", address)
	// if err != nil {
	//     return fmt.Errorf("failed to listen: %v", err)
	// }
	
	// logger.Printf("gRPC server listening on %s", address)
	// return server.Serve(lis)
	
	return nil
}

// Client example
func demonstrateGRPCClient() {
	fmt.Println("\n=== gRPC Client Example ===")
	
	// Mock client setup (in real implementation)
	// conn, err := grpc.Dial("localhost:8080", grpc.WithInsecure())
	// if err != nil {
	//     log.Fatalf("Failed to connect: %v", err)
	// }
	// defer conn.Close()
	// 
	// client := pb.NewPromptServiceClient(conn)
	
	// Mock requests
	fmt.Println("Mock gRPC client requests:")
	
	// Scaffold request
	scaffoldReq := &ScaffoldRequest{
		Description: "Build a microservices API gateway",
		Language:    "go",
		Template:    "grpc",
	}
	fmt.Printf("1. ScaffoldProject: %+v\n", scaffoldReq)
	
	// Analysis request
	analysisReq := &AnalysisRequest{
		Problem:      "How to implement distributed caching?",
		AnalysisType: "reasoning",
	}
	fmt.Printf("2. AnalyzeProblem: %+v\n", analysisReq)
	
	// Document request
	docReq := &DocumentRequest{
		Content:      "This is a sample technical specification document...",
		OutputFormat: "readme",
	}
	fmt.Printf("3. ProcessDocument: %+v\n", docReq)
	
	fmt.Println("gRPC client demonstration completed")
}

// Load testing helper
func demonstrateLoadTesting() {
	fmt.Println("\n=== Load Testing Example ===")
	
	aiClient := &MockAIClient{}
	service := NewPromptService(aiClient)
	
	// Concurrent requests simulation
	concurrency := 10
	requestsPerWorker := 5
	
	var wg sync.WaitGroup
	start := time.Now()
	
	for i := 0; i < concurrency; i++ {
		wg.Add(1)
		go func(workerID int) {
			defer wg.Done()
			
			for j := 0; j < requestsPerWorker; j++ {
				ctx := context.Background()
				req := &AnalysisRequest{
					Problem:      fmt.Sprintf("Worker %d request %d", workerID, j),
					AnalysisType: "reasoning",
				}
				
				_, err := service.AnalyzeProblem(ctx, req)
				if err != nil {
					log.Printf("Worker %d request %d failed: %v", workerID, j, err)
				}
			}
		}(i)
	}
	
	wg.Wait()
	
	duration := time.Since(start)
	totalRequests := concurrency * requestsPerWorker
	rps := float64(totalRequests) / duration.Seconds()
	
	fmt.Printf("Load test completed:")
	fmt.Printf("  Total requests: %d\n", totalRequests)
	fmt.Printf("  Duration: %v\n", duration)
	fmt.Printf("  Requests/second: %.2f\n", rps)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Println("Go gRPC Service Integration Example")
	fmt.Println(strings.Repeat("=", 50))
	
	// Setup server configuration
	config := DefaultServerConfig()
	config.Port = 8080
	
	fmt.Printf("Server configuration:\n")
	fmt.Printf("  Port: %d\n", config.Port)
	fmt.Printf("  Rate limit: %d requests per %v\n", config.RateLimit, config.RateWindow)
	fmt.Printf("  TLS enabled: %v\n", config.EnableTLS)
	
	// Demonstrate server setup
	if err := SetupServer(config); err != nil {
		log.Fatalf("Failed to setup server: %v", err)
	}
	
	// Demonstrate client usage
	demonstrateGRPCClient()
	
	// Demonstrate load testing
	demonstrateLoadTesting()
	
	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("gRPC service integration example completed!")
	
	fmt.Println("\nTo implement with real gRPC:")
	fmt.Println("1. go get google.golang.org/grpc")
	fmt.Println("2. Define .proto files")
	fmt.Println("3. Generate Go code with protoc")
	fmt.Println("4. Implement the service interfaces")
	fmt.Println("5. Add TLS and authentication")
}

/*
// Go dependencies for full implementation:
// go.mod
module grpc-prompt-service

go 1.21

require (
    google.golang.org/grpc v1.59.0
    google.golang.org/protobuf v1.31.0
    github.com/grpc-ecosystem/grpc-gateway/v2 v2.18.0
)

// Example .proto file:
syntax = "proto3";

package promptservice;

option go_package = "github.com/yourorg/prompt-service/pb";

service PromptService {
  rpc ScaffoldProject(ScaffoldRequest) returns (ScaffoldResponse);
  rpc AnalyzeProblem(AnalysisRequest) returns (AnalysisResponse);
  rpc ProcessDocument(DocumentRequest) returns (DocumentResponse);
  rpc StreamAnalysis(AnalysisRequest) returns (stream StreamResponse);
}

message ScaffoldRequest {
  string description = 1;
  string language = 2;
  string template = 3;
  string package_manager = 4;
  string license = 5;
}

message ScaffoldResponse {
  bool success = 1;
  string plan = 2;
  string error = 3;
  int64 timestamp = 4;
}

// Additional messages would be defined here...
*/