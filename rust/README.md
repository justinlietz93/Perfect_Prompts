# Rust Prompt Templates

This directory contains Rust implementations of prompt templates designed for agentic AI systems. These templates provide structured, reusable prompts with Rust's memory safety, performance, and type system advantages for AI-assisted development and analysis tasks.

## Overview

The Rust prompt templates are organized into two main categories:

### 🤖 Agent Prompts (`agent_prompts/`)
Specialized prompts for AI agents that perform specific development and analysis tasks:

- **`projectScaffolder.rs`** - Generate project structures using Hybrid-Clean architecture
- **`agentDesigner.rs`** - Design single-agent and multi-agent AI systems
- **`mermaidDesigner.rs`** - Create and validate Mermaid.js diagrams from specifications
- **`promptEnhancer.rs`** - Improve and optimize existing prompts with advanced techniques
- **`reasoner.rs`** - Perform step-by-step logical reasoning and problem-solving
- **`rewriter.rs`** - Rewrite content with specific styles, tones, and requirements
- **`citations.rs`** - Generate proper academic and professional citations
- **`mathFormatter.rs`** - Format mathematical expressions and equations
- **`styleExtractor.rs`** - Extract and analyze writing styles and patterns
- **`highlightExtraction.rs`** - Extract key highlights and insights from content
- **`nextSteps.rs`** - Generate actionable next steps from analysis results
- **`requestSplitter.rs`** - Break down complex requests into manageable sub-tasks

### 📊 Summary Prompts (`summary_prompts/`)
Templates for analyzing, summarizing, and structuring content:

- **`readme.rs`** - Generate comprehensive README documentation
- **`summarize.rs`** - Create concise summaries of complex content
- **`checklist.rs`** - Convert content into actionable checklists
- **`timeline.rs`** - Extract and organize temporal information
- **`processFlow.rs`** - Document step-by-step processes and workflows
- **`stakeholderMap.rs`** - Identify and map project stakeholders
- **`riskRegister.rs`** - Identify and assess project risks
- **`decisionMatrix.rs`** - Structure decision-making processes
- **`swotAnalysis.rs`** - Perform SWOT analysis
- **`entityRelationshipDigest.rs`** - Extract entity relationships from content
- **`systemWalkthrough.rs`** - Generate system documentation and walkthroughs
- **`reverseEngineering.rs`** - Analyze and document existing systems

## Usage in Agentic Projects

### Basic Usage Pattern

```rust
use crate::agent_prompts::project_scaffolder::{scaffolder_planning_prompt, ScaffolderSettings};
use crate::summary_prompts::readme::chunk_summary_prompt_readme;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Generate a project scaffolding prompt
    let project_description = "Build a REST API for task management";
    let settings = ScaffolderSettings {
        language: "rust".to_string(),
        template: "axum".to_string(),
        package_manager: "cargo".to_string(),
        license: "MIT".to_string(),
    };

    let scaffold_prompt = scaffolder_planning_prompt(project_description, &settings);

    // Use with your AI client
    let response = ai_client.complete(&scaffold_prompt).await?;
    println!("{}", response);
    
    Ok(())
}
```

### Type-Safe Configuration with Serde

Rust's type system and serde provide compile-time safety and easy serialization:

```rust
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct AgentDesignerSettings {
    pub system_type: String,
    pub goal: String,
    pub trigger: String,
    pub provider: String,
    pub capabilities: std::collections::HashMap<String, bool>,
}

impl Default for AgentDesignerSettings {
    fn default() -> Self {
        Self {
            system_type: "multiAgent".to_string(),
            goal: String::new(),
            trigger: String::new(),
            provider: "openai".to_string(),
            capabilities: std::collections::HashMap::new(),
        }
    }
}

// Usage
let settings = AgentDesignerSettings {
    system_type: "multiAgent".to_string(),
    goal: "Design a document processing system".to_string(),
    trigger: "file_upload".to_string(),
    provider: "openai".to_string(),
    capabilities: [
        ("web_search".to_string(), true),
        ("file_io".to_string(), true),
        ("email".to_string(), false),
    ].into_iter().collect(),
};

let prompt = agent_designer_prompt_template(&settings);
```

### Integration with Rust AI Libraries

#### Async AI Client Integration
```rust
use tokio;
use reqwest;
use serde_json;

#[derive(Clone)]
pub struct AIClient {
    client: reqwest::Client,
    api_key: String,
    base_url: String,
}

impl AIClient {
    pub fn new(api_key: String) -> Self {
        Self {
            client: reqwest::Client::new(),
            api_key,
            base_url: "https://api.openai.com/v1".to_string(),
        }
    }

    pub async fn complete(&self, prompt: &str) -> Result<String, Box<dyn std::error::Error>> {
        let request_body = serde_json::json!({
            "model": "gpt-4",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7
        });

        let response = self.client
            .post(&format!("{}/chat/completions", self.base_url))
            .header("Authorization", format!("Bearer {}", self.api_key))
            .header("Content-Type", "application/json")
            .json(&request_body)
            .send()
            .await?;

        let response_json: serde_json::Value = response.json().await?;
        
        Ok(response_json["choices"][0]["message"]["content"]
            .as_str()
            .unwrap_or("")
            .to_string())
    }
}
```

#### Error Handling with Custom Error Types
```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum PromptError {
    #[error("AI client error: {0}")]
    AIClientError(#[from] reqwest::Error),
    
    #[error("JSON parsing error: {0}")]
    JsonError(#[from] serde_json::Error),
    
    #[error("Invalid prompt configuration: {message}")]
    InvalidConfig { message: String },
    
    #[error("Prompt generation failed: {0}")]
    GenerationFailed(String),
}

pub type PromptResult<T> = Result<T, PromptError>;
```

### Workflow Examples

#### Concurrent Document Processing with Tokio
```rust
use tokio::task;
use futures::future::join_all;

pub struct DocumentProcessor {
    ai_client: AIClient,
}

impl DocumentProcessor {
    pub async fn process_documents_concurrently(
        &self,
        documents: Vec<String>,
    ) -> PromptResult<Vec<DocumentAnalysis>> {
        let tasks: Vec<_> = documents
            .into_iter()
            .map(|doc| {
                let client = self.ai_client.clone();
                task::spawn(async move {
                    let analysis_prompt = crate::summary_prompts::system_walkthrough::prompt(&doc);
                    let result = client.complete(&analysis_prompt).await?;
                    
                    Ok::<DocumentAnalysis, PromptError>(DocumentAnalysis {
                        document: doc,
                        analysis: result,
                        processed_at: chrono::Utc::now(),
                    })
                })
            })
            .collect();

        let results = join_all(tasks).await;
        
        let mut analyses = Vec::new();
        for result in results {
            analyses.push(result??);
        }
        
        Ok(analyses)
    }
}

#[derive(Debug)]
pub struct DocumentAnalysis {
    pub document: String,
    pub analysis: String,
    pub processed_at: chrono::DateTime<chrono::Utc>,
}
```

#### Project Scaffolding Pipeline with Error Recovery
```rust
use serde_json;

pub struct ProjectScaffolder {
    ai_client: AIClient,
}

impl ProjectScaffolder {
    pub async fn scaffold_project(
        &self,
        description: &str,
        settings: &ScaffolderSettings,
    ) -> PromptResult<ProjectPlan> {
        // Step 1: Generate project plan with retry logic
        let planning_prompt = scaffolder_planning_prompt(description, settings);
        let plan_response = self.complete_with_retry(&planning_prompt, 3).await?;
        
        let plan: ProjectPlan = serde_json::from_str(&plan_response)
            .map_err(|e| PromptError::InvalidConfig {
                message: format!("Invalid project plan JSON: {}", e),
            })?;
        
        // Step 2: Generate file prompts concurrently
        let file_prompt_tasks: Vec<_> = plan.tree
            .iter()
            .map(|file_item| {
                let client = self.ai_client.clone();
                let project_data = serde_json::to_string(&plan.project).unwrap();
                let file_data = serde_json::to_string(file_item).unwrap();
                let path = file_item.path.clone();
                
                task::spawn(async move {
                    let file_prompt = scaffolder_file_prompt_generation(&project_data, &file_data);
                    Ok::<(String, String), PromptError>((path, file_prompt))
                })
            })
            .collect();
        
        let file_prompt_results = join_all(file_prompt_tasks).await;
        let mut file_prompts = std::collections::HashMap::new();
        
        for result in file_prompt_results {
            let (path, prompt) = result??;
            file_prompts.insert(path, prompt);
        }
        
        Ok(ProjectPlan {
            project: plan.project,
            layers: plan.layers,
            tree: plan.tree,
            file_prompts: Some(file_prompts),
        })
    }
    
    async fn complete_with_retry(&self, prompt: &str, max_retries: usize) -> PromptResult<String> {
        let mut last_error = None;
        
        for attempt in 0..=max_retries {
            match self.ai_client.complete(prompt).await {
                Ok(response) => return Ok(response),
                Err(e) => {
                    last_error = Some(e);
                    if attempt < max_retries {
                        tokio::time::sleep(tokio::time::Duration::from_millis(
                            1000 * (attempt + 1) as u64
                        )).await;
                    }
                }
            }
        }
        
        Err(PromptError::GenerationFailed(
            format!("Failed after {} attempts: {:?}", max_retries, last_error)
        ))
    }
}

#[derive(Debug, Deserialize)]
pub struct ProjectPlan {
    pub project: ProjectInfo,
    pub layers: Vec<String>,
    pub tree: Vec<FileItem>,
    pub file_prompts: Option<std::collections::HashMap<String, String>>,
}
```

## Best Practices

### 1. **Error Handling with Result Types**
Use Rust's Result type for comprehensive error handling:
```rust
pub fn generate_prompt(config: &Config) -> PromptResult<String> {
    config.validate()
        .map_err(|e| PromptError::InvalidConfig { message: e })?;
    
    Ok(format_prompt(config))
}
```

### 2. **Memory Efficiency with String Slices**
Use string slices when possible to avoid unnecessary allocations:
```rust
pub fn chunk_summary_prompt_readme(text: &str) -> String {
    format!(r#"
You are a technical writer AI...
---
DOCUMENT SEGMENT TO ANALYZE:
{}
---
"#, text)
}
```

### 3. **Async/Await for Non-Blocking Operations**
Use async patterns for AI API calls:
```rust
pub async fn process_prompt_batch(
    prompts: Vec<String>,
    client: &AIClient,
) -> Vec<PromptResult<String>> {
    let futures = prompts.iter().map(|prompt| client.complete(prompt));
    futures::future::join_all(futures).await
        .into_iter()
        .map(|result| result.map_err(PromptError::from))
        .collect()
}
```

### 4. **Configuration with Serde and Validation**
Implement configuration validation:
```rust
#[derive(Debug, Deserialize, Validate)]
pub struct PromptConfig {
    #[validate(length(min = 1, message = "Template name cannot be empty"))]
    pub template: String,
    
    #[validate(range(min = 0.0, max = 2.0, message = "Temperature must be between 0.0 and 2.0"))]
    pub temperature: f32,
    
    #[validate(range(min = 1, max = 4096, message = "Max tokens must be between 1 and 4096"))]
    pub max_tokens: u32,
}

impl PromptConfig {
    pub fn validate(&self) -> Result<(), validator::ValidationErrors> {
        validator::Validate::validate(self)
    }
}
```

### 5. **Testing with Property-Based Testing**
Use proptest for comprehensive testing:
```rust
#[cfg(test)]
mod tests {
    use super::*;
    use proptest::prelude::*;

    proptest! {
        #[test]
        fn test_prompt_generation_never_panics(
            goal in "\\PC{1,100}",
            system_type in prop::sample::select(vec!["singleAgent", "multiAgent"])
        ) {
            let settings = AgentDesignerSettings {
                system_type,
                goal,
                ..Default::default()
            };
            
            // Should never panic
            let _ = agent_designer_prompt_template(&settings);
        }
    }

    #[tokio::test]
    async fn test_concurrent_processing() {
        let client = AIClient::new("test-key".to_string());
        let processor = DocumentProcessor { ai_client: client };
        
        let documents = vec![
            "Test document 1".to_string(),
            "Test document 2".to_string(),
        ];
        
        // This test would use a mock client in real scenarios
        // let results = processor.process_documents_concurrently(documents).await;
        // assert!(results.is_ok());
    }
}
```

## Integration Examples

See the `examples/` directory for complete, runnable examples demonstrating:
- Async HTTP client integration with reqwest
- Concurrent prompt processing with Tokio
- Web service integration with Axum
- CLI applications with clap
- Configuration management
- Error handling patterns
- Testing strategies with mocks

## Dependencies

Core prompt templates have minimal dependencies. Integration examples may require:

```toml
# Cargo.toml
[dependencies]
tokio = { version = "1.0", features = ["full"] }
reqwest = { version = "0.11", features = ["json"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
thiserror = "1.0"
anyhow = "1.0"
chrono = { version = "0.4", features = ["serde"] }
uuid = { version = "1.0", features = ["v4"] }
clap = { version = "4.0", features = ["derive"] }
axum = "0.7"
validator = { version = "0.16", features = ["derive"] }

[dev-dependencies]
proptest = "1.0"
tokio-test = "0.4"
mockall = "0.11"
```

## Performance Considerations

- Use `String` for owned data, `&str` for borrowed data
- Leverage Rust's zero-cost abstractions
- Use `async`/`await` for I/O-bound operations
- Consider using `Arc` and `Mutex` for shared state
- Profile with `cargo flamegraph` for optimization
- Use `serde_json::from_slice` for faster JSON parsing

## Memory Safety and Concurrency

Rust's ownership system ensures:
- No data races in concurrent prompt processing
- Memory safety without garbage collection
- Thread-safe sharing with `Arc` and `Mutex`
- Efficient async processing with Tokio

## Contributing

When adding new prompt templates:
1. Follow Rust naming conventions (snake_case for functions)
2. Use comprehensive error handling with custom error types
3. Add documentation with `///` comments
4. Write unit and integration tests
5. Use `clippy` for code quality checks
6. Ensure thread safety for concurrent usage
7. Add examples in the `examples/` directory

## Related Resources

- [Architecture Standards](../STANDARDS_REPOSITORY/) - Comprehensive architectural guidelines
- [General Guidelines](../general_guidelines/) - Cross-language development practices
- [Main Repository README](../README.md) - Overall project documentation
- [The Rust Book](https://doc.rust-lang.org/book/) - Official Rust documentation
- [Rust Async Programming](https://rust-lang.github.io/async-book/) - Async Rust guide