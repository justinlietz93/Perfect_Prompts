# Go Examples Makefile
# Provides convenient commands to build and run the Go prompt template examples

.PHONY: help build run-basic run-grpc clean deps test fmt vet lint

# Default target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Build all examples
build: ## Build all example binaries
	@echo "Building Go examples..."
	go build -o bin/basic_usage basic_usage.go
	go build -o bin/grpc_service grpc_service.go
	@echo "Build complete. Binaries in ./bin/"

# Run examples
run-basic: build ## Run the basic usage example
	@echo "Running basic usage example..."
	./bin/basic_usage

run-grpc: build ## Run the gRPC service example
	@echo "Running gRPC service example..."
	./bin/grpc_service

# Development targets
deps: ## Download and install dependencies
	@echo "Downloading dependencies..."
	go mod download
	go mod tidy

test: ## Run tests
	@echo "Running tests..."
	go test -v ./...

benchmark: ## Run benchmarks
	@echo "Running benchmarks..."
	go test -bench=. -benchmem ./...

# Code quality
fmt: ## Format Go code
	@echo "Formatting code..."
	go fmt ./...

vet: ## Run go vet
	@echo "Running go vet..."
	go vet ./...

lint: deps ## Run golangci-lint (requires golangci-lint to be installed)
	@echo "Running golangci-lint..."
	@which golangci-lint > /dev/null || (echo "golangci-lint not found. Install with: go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest" && exit 1)
	golangci-lint run

# Cleanup
clean: ## Clean build artifacts
	@echo "Cleaning up..."
	rm -rf bin/
	go clean

# Docker targets (for containerized deployment)
docker-build: ## Build Docker image
	@echo "Building Docker image..."
	docker build -t go-prompt-examples .

docker-run: docker-build ## Run in Docker container
	@echo "Running in Docker..."
	docker run --rm -p 8080:8080 go-prompt-examples

# Development server with auto-reload (requires air)
dev: ## Start development server with auto-reload
	@echo "Starting development server..."
	@which air > /dev/null || (echo "air not found. Install with: go install github.com/cosmtrek/air@latest" && exit 1)
	air

# Initialize go module (for new projects)
init: ## Initialize a new Go module
	@read -p "Enter module name (e.g., github.com/user/project): " module; \
	go mod init $$module

# Generate documentation
docs: ## Generate documentation
	@echo "Generating documentation..."
	go doc -all > DOCS.md

# Security scan
security: ## Run security scan with gosec
	@echo "Running security scan..."
	@which gosec > /dev/null || (echo "gosec not found. Install with: go install github.com/securecodewarrior/gosec/v2/cmd/gosec@latest" && exit 1)
	gosec ./...

# Performance profiling
profile: build ## Run with CPU profiling
	@echo "Running with CPU profiling..."
	./bin/basic_usage -cpuprofile=cpu.prof
	@echo "Profile saved to cpu.prof. Analyze with: go tool pprof cpu.prof"

# Cross-compilation targets
build-all: ## Build for multiple platforms
	@echo "Building for multiple platforms..."
	GOOS=linux GOARCH=amd64 go build -o bin/basic_usage-linux-amd64 basic_usage.go
	GOOS=darwin GOARCH=amd64 go build -o bin/basic_usage-darwin-amd64 basic_usage.go  
	GOOS=windows GOARCH=amd64 go build -o bin/basic_usage-windows-amd64.exe basic_usage.go
	GOOS=linux GOARCH=arm64 go build -o bin/basic_usage-linux-arm64 basic_usage.go
	@echo "Cross-compilation complete. Binaries in ./bin/"

# Release build
release: clean ## Build optimized release binaries
	@echo "Building release binaries..."
	go build -ldflags="-w -s" -o bin/basic_usage basic_usage.go
	go build -ldflags="-w -s" -o bin/grpc_service grpc_service.go
	@echo "Release build complete."

# Install tools
install-tools: ## Install development tools
	@echo "Installing development tools..."
	go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
	go install github.com/cosmtrek/air@latest
	go install github.com/securecodewarrior/gosec/v2/cmd/gosec@latest
	@echo "Tools installed."

# Usage examples
examples: ## Show usage examples
	@echo "Usage examples:"
	@echo ""
	@echo "1. Basic development workflow:"
	@echo "   make deps && make fmt && make vet && make test && make build"
	@echo ""
	@echo "2. Run basic example:"
	@echo "   make run-basic"
	@echo ""
	@echo "3. Development with auto-reload:"
	@echo "   make dev"
	@echo ""
	@echo "4. Full quality check:"
	@echo "   make fmt vet lint test"
	@echo ""
	@echo "5. Cross-platform build:"
	@echo "   make build-all"

# Check if required tools are installed
check-tools: ## Check if required development tools are installed
	@echo "Checking development tools..."
	@go version || (echo "Go is not installed" && exit 1)
	@which git > /dev/null || (echo "Git is not installed" && exit 1)
	@which make > /dev/null || (echo "Make is not installed" && exit 1)
	@echo "✓ All required tools are available"
	@echo ""
	@echo "Optional tools:"
	@which golangci-lint > /dev/null && echo "✓ golangci-lint available" || echo "✗ golangci-lint not found (make install-tools)"
	@which air > /dev/null && echo "✓ air available" || echo "✗ air not found (make install-tools)"
	@which gosec > /dev/null && echo "✓ gosec available" || echo "✗ gosec not found (make install-tools)"

# Variables for customization
BIN_DIR := bin
GO_FILES := $(wildcard *.go)
MODULE := $(shell go list -m)

# Default Go build flags
LDFLAGS := -ldflags="-w -s"
BUILD_FLAGS := -trimpath

.DEFAULT_GOAL := help