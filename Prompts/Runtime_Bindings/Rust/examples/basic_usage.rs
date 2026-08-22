use std::collections::HashMap;
use std::sync::Arc;
use std::time::Duration;
use tokio::time::sleep;
use serde_json::{json, Value};

// Mock AI Client for demonstration
#[async_trait::async_trait]
pub trait AIClient: Send + Sync {
    async fn complete(&self, prompt: &str) -> Result<String, Box<dyn std::error::Error + Send + Sync>>;
    async fn complete_with_timeout(
        &self,
        prompt: &str,
        timeout: Duration,
    ) -> Result<String, Box<dyn std::error::Error + Send + Sync>>;
}

pub struct MockAIClient {
    call_count: std::sync::atomic::AtomicUsize,
}

impl MockAIClient {
    pub fn new() -> Self {
        Self {
            call_count: std::sync::atomic::AtomicUsize::new(0),
        }
    }

    fn mock_project_plan(&self) -> String {
        let plan = json!({
            "project": {
                "name": "TaskManagerAPI",
                "language": "rust",
                "template": "axum",
                "package_manager": "cargo",
                "license": "MIT"
            },
            "layers": ["presentation", "application", "domain", "infrastructure", "shared", "tests"],
            "tree": [
                {
                    "path": "src/presentation/handlers/task_handler.rs",
                    "layer": "presentation",
                    "purpose": "HTTP handlers for task management",
                    "prompt": ""
                },
                {
                    "path": "src/application/services/task_service.rs",
                    "layer": "application", 
                    "purpose": "Business logic for task operations",
                    "prompt": ""
                }
            ]
        });

        plan.to_string()
    }

    fn mock_reasoning_response(&self) -> String {
        r#"**Step 1: Problem Analysis**
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
4. Add monitoring and observability"#.to_string()
    }

    fn mock_stakeholder_response(&self) -> String {
        r#"## Project Stakeholders

### Primary Stakeholders
- **Product Owner**: Defines requirements and priorities
- **Development Team**: Implements the solution
- **End Users**: Will use the task management system

### Secondary Stakeholders
- **DevOps Team**: Manages deployment and infrastructure
- **QA Team**: Ensures quality and testing
- **Security Team**: Reviews security requirements"#.to_string()
    }
}

#[async_trait::async_trait]
impl AIClient for MockAIClient {
    async fn complete(&self, prompt: &str) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
        // Simulate API delay
        sleep(Duration::from_millis(100)).await;

        let count = self.call_count.fetch_add(1, std::sync::atomic::Ordering::SeqCst);

        // Mock responses based on prompt content
        if prompt.to_lowercase().contains("project plan") {
            Ok(self.mock_project_plan())
        } else if prompt.to_lowercase().contains("step-by-step") {
            Ok(self.mock_reasoning_response())
        } else if prompt.to_lowercase().contains("stakeholder") {
            Ok(self.mock_stakeholder_response())
        } else {
            Ok(format!("Mock response {} for prompt: {}...", count + 1, &prompt[..prompt.len().min(50)]))
        }
    }

    async fn complete_with_timeout(
        &self,
        prompt: &str,
        timeout: Duration,
    ) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
        tokio::time::timeout(timeout, self.complete(prompt))
            .await
            .map_err(|e| Box::new(e) as Box<dyn std::error::Error + Send + Sync>)?
    }
}

// Mock prompt functions (replace with actual imports from your crate)
fn scaffolder_planning_prompt(description: &str, settings: &HashMap<&str, &str>) -> String {
    format!(
        r#"You are an expert AI software architect specializing in the Hybrid-Clean architecture.
Your task is to take a user's project description and generate a detailed project plan as a single JSON object.

Project Description: {}
Settings: {:?}

Generate a comprehensive project plan..."#,
        description, settings
    )
}

fn step_by_step_reasoning_prompt(problem: &str) -> String {
    format!(
        r#"You are an expert problem solver. Break down the following problem into clear, logical steps:

Problem: {}

Provide a step-by-step analysis and solution..."#,
        problem
    )
}

fn chunk_summary_prompt_readme(text: &str) -> String {
    format!(
        r#"You are a technical writer AI tasked with creating a section of a project README.md file.
Your job is to analyze the following document segment and extract information relevant to a project's documentation.

Document to analyze:
{}

Generate a README section..."#,
        text
    )
}

// Project scaffolding example
async fn demonstrate_basic_scaffolding(client: Arc<dyn AIClient>) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("=== Project Scaffolding Example ===");

    let description = "Build a REST API for task management with user authentication";
    let mut settings = HashMap::new();
    settings.insert("language", "rust");
    settings.insert("template", "axum");
    settings.insert("packageManager", "cargo");
    settings.insert("license", "MIT");

    // Step 1: Generate project plan
    let planning_prompt = scaffolder_planning_prompt(description, &settings);
    println!("Generated planning prompt ({} chars)", planning_prompt.len());

    let plan_response = client.complete(&planning_prompt).await?;
    let plan: Value = serde_json::from_str(&plan_response)?;

    let project = &plan["project"];
    let tree = plan["tree"].as_array().unwrap();

    println!("Project: {}", project["name"]);
    println!("Files to generate: {}", tree.len());

    // Step 2: Generate file prompts would go here
    println!("File prompt generation completed");
    Ok(())
}

// Reasoning workflow example
async fn demonstrate_reasoning_workflow(client: Arc<dyn AIClient>) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("\n=== Reasoning Workflow Example ===");

    let problem = "How can we design a scalable microservices architecture for a high-traffic e-commerce platform?";

    let reasoning_prompt = step_by_step_reasoning_prompt(problem);
    println!("Generated reasoning prompt ({} chars)", reasoning_prompt.len());

    let reasoning_result = client.complete(&reasoning_prompt).await?;

    println!("Reasoning Result:");
    println!("{}", reasoning_result);
    Ok(())
}

// Concurrent processing example
async fn demonstrate_concurrent_processing(client: Arc<dyn AIClient>) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("\n=== Concurrent Processing Example ===");

    let problems = vec![
        "Design a caching strategy for high-load systems",
        "Implement fault tolerance in distributed systems",
        "Optimize database queries for performance",
    ];

    let mut tasks = Vec::new();
    
    for (i, problem) in problems.iter().enumerate() {
        let client_clone = client.clone();
        let problem_clone = problem.to_string();
        
        let task = tokio::spawn(async move {
            let prompt = step_by_step_reasoning_prompt(&problem_clone);
            let result = client_clone.complete(&prompt).await;
            (i, problem_clone, result)
        });
        
        tasks.push(task);
    }

    let results = futures::future::join_all(tasks).await;

    for task_result in results {
        match task_result {
            Ok((index, problem, result)) => {
                match result {
                    Ok(response) => {
                        println!("Problem {}: {}", index + 1, problem);
                        println!("Result: {}...\n", &response[..response.len().min(100)]);
                    }
                    Err(e) => {
                        println!("Problem {} failed: {}", index + 1, e);
                    }
                }
            }
            Err(e) => {
                println!("Task failed: {}", e);
            }
        }
    }
    
    Ok(())
}

// Timeout and error handling example
async fn demonstrate_timeout_handling(client: Arc<dyn AIClient>) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("\n=== Timeout Handling Example ===");

    let problem = "Explain the principles of clean architecture";
    let prompt = step_by_step_reasoning_prompt(problem);

    match client.complete_with_timeout(&prompt, Duration::from_secs(5)).await {
        Ok(result) => {
            println!("Result: {}...", &result[..result.len().min(150)]);
        }
        Err(e) => {
            if e.to_string().contains("timeout") {
                println!("Request timed out");
            } else {
                println!("Request failed: {}", e);
            }
        }
    }
    
    Ok(())
}

// Error handling and retry example
async fn demonstrate_error_handling() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("\n=== Error Handling and Retry Example ===");

    struct FailingClient;

    #[async_trait::async_trait]
    impl AIClient for FailingClient {
        async fn complete(&self, _prompt: &str) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
            Err("API rate limit exceeded".into())
        }

        async fn complete_with_timeout(
            &self,
            prompt: &str,
            _timeout: Duration,
        ) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
            self.complete(prompt).await
        }
    }

    let failing_client: Arc<dyn AIClient> = Arc::new(FailingClient);

    // Retry function with exponential backoff
    async fn retry_with_backoff(
        client: Arc<dyn AIClient>,
        prompt: &str,
        max_retries: usize,
    ) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
        let mut last_error = None;

        for attempt in 0..max_retries {
            match client.complete(prompt).await {
                Ok(result) => return Ok(result),
                Err(e) => {
                    println!("Attempt {} failed: {}", attempt + 1, e);
                    last_error = Some(e);

                    if attempt < max_retries - 1 {
                        let delay = Duration::from_secs((attempt + 1) as u64);
                        sleep(delay).await;
                    }
                }
            }
        }

        Err(format!("All {} attempts failed, last error: {:?}", max_retries, last_error).into())
    }

    let prompt = step_by_step_reasoning_prompt("Test problem");
    match retry_with_backoff(failing_client, &prompt, 3).await {
        Ok(result) => println!("Final result: {}", result),
        Err(e) => println!("Final result: Failed - {}", e),
    }

    Ok(())
}

// Performance monitoring example
pub struct InstrumentedClient {
    client: Arc<dyn AIClient>,
    stats: std::sync::Arc<std::sync::Mutex<ClientStats>>,
}

#[derive(Default)]
struct ClientStats {
    total_calls: usize,
    total_duration: Duration,
}

impl InstrumentedClient {
    pub fn new(client: Arc<dyn AIClient>) -> Self {
        Self {
            client,
            stats: Arc::new(std::sync::Mutex::new(ClientStats::default())),
        }
    }

    pub fn get_stats(&self) -> (usize, Duration) {
        let stats = self.stats.lock().unwrap();
        (stats.total_calls, stats.total_duration)
    }
}

#[async_trait::async_trait]
impl AIClient for InstrumentedClient {
    async fn complete(&self, prompt: &str) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
        let start = std::time::Instant::now();
        let result = self.client.complete(prompt).await;
        let duration = start.elapsed();

        {
            let mut stats = self.stats.lock().unwrap();
            stats.total_calls += 1;
            stats.total_duration += duration;
        }

        result
    }

    async fn complete_with_timeout(
        &self,
        prompt: &str,
        timeout: Duration,
    ) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
        let start = std::time::Instant::now();
        let result = self.client.complete_with_timeout(prompt, timeout).await;
        let duration = start.elapsed();

        {
            let mut stats = self.stats.lock().unwrap();
            stats.total_calls += 1;
            stats.total_duration += duration;
        }

        result
    }
}

async fn demonstrate_performance_monitoring() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("\n=== Performance Monitoring Example ===");

    let base_client: Arc<dyn AIClient> = Arc::new(MockAIClient::new());
    let instrumented_client = Arc::new(InstrumentedClient::new(base_client));

    // Make several calls
    for i in 0..5 {
        let prompt = step_by_step_reasoning_prompt(&format!("Problem {}", i + 1));
        if let Err(e) = instrumented_client.complete(&prompt).await {
            eprintln!("Call {} failed: {}", i + 1, e);
        }
    }

    let (total_calls, total_duration) = instrumented_client.get_stats();
    let avg_duration = total_duration / total_calls as u32;

    println!("Performance Stats:");
    println!("  Total calls: {}", total_calls);
    println!("  Total duration: {:?}", total_duration);
    println!("  Average duration: {:?}", avg_duration);

    Ok(())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("Rust Prompt Templates - Basic Usage Examples");
    println!("{}", "=".repeat(50));

    let client: Arc<dyn AIClient> = Arc::new(MockAIClient::new());

    demonstrate_basic_scaffolding(client.clone()).await?;
    demonstrate_reasoning_workflow(client.clone()).await?;
    demonstrate_concurrent_processing(client.clone()).await?;
    demonstrate_timeout_handling(client.clone()).await?;
    demonstrate_error_handling().await?;
    demonstrate_performance_monitoring().await?;

    println!("\n{}", "=".repeat(50));
    println!("All examples completed successfully!");

    Ok(())
}

// Add this to Cargo.toml for dependencies:
/*
[dependencies]
tokio = { version = "1.0", features = ["full"] }
serde_json = "1.0"
async-trait = "0.1"
futures = "0.3"
*/