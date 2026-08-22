use axum::{
    extract::{Path, Query, State},
    http::{HeaderMap, StatusCode},
    response::Json,
    routing::{get, post},
    Router,
};
use serde::{Deserialize, Serialize};
use std::{
    collections::HashMap,
    sync::Arc,
    time::{Duration, SystemTime, UNIX_EPOCH},
};
use tokio::{sync::RwLock, time::sleep};
use tower::ServiceBuilder;
use tower_http::{cors::CorsLayer, trace::TraceLayer};
use tracing::{info, warn, error};
use uuid::Uuid;

// Mock AI Client (same as basic_usage.rs)
#[async_trait::async_trait]
pub trait AIClient: Send + Sync {
    async fn complete(&self, prompt: &str) -> Result<String, Box<dyn std::error::Error + Send + Sync>>;
}

pub struct MockAIClient {
    delay: Duration,
}

impl MockAIClient {
    pub fn new(delay: Duration) -> Self {
        Self { delay }
    }
}

#[async_trait::async_trait]
impl AIClient for MockAIClient {
    async fn complete(&self, prompt: &str) -> Result<String, Box<dyn std::error::Error + Send + Sync>> {
        sleep(self.delay).await;
        
        if prompt.to_lowercase().contains("project plan") {
            Ok(serde_json::json!({
                "project": {
                    "name": "AxumGeneratedProject",
                    "language": "rust",
                    "template": "axum",
                    "package_manager": "cargo"
                },
                "tree": [
                    {
                        "path": "src/main.rs",
                        "purpose": "Application entry point"
                    },
                    {
                        "path": "src/handlers.rs", 
                        "purpose": "HTTP request handlers"
                    }
                ]
            }).to_string())
        } else if prompt.to_lowercase().contains("step-by-step") {
            Ok("**Step 1: Analysis**\nBreak down the problem\n**Step 2: Design**\nCreate solution architecture\n**Step 3: Implementation**\nBuild the solution".to_string())
        } else {
            Ok(format!("AI response for: {}", &prompt[..prompt.len().min(50)]))
        }
    }
}

// Mock prompt functions
fn scaffolder_planning_prompt(description: &str, settings: &ScaffolderSettings) -> String {
    format!(
        "Generate project plan for: {} with language: {} and template: {}",
        description, settings.language, settings.template
    )
}

fn step_by_step_reasoning_prompt(problem: &str) -> String {
    format!("Provide step-by-step analysis for: {}", problem)
}

fn chunk_summary_prompt_readme(text: &str) -> String {
    format!("Generate README summary for: {}", text)
}

// Request/Response DTOs
#[derive(Debug, Deserialize, Serialize)]
pub struct ScaffolderSettings {
    pub language: String,
    pub template: String,
    pub package_manager: Option<String>,
    pub license: Option<String>,
}

#[derive(Debug, Deserialize)]
pub struct ScaffoldRequest {
    pub description: String,
    #[serde(flatten)]
    pub settings: ScaffolderSettings,
}

#[derive(Debug, Deserialize)]
pub struct AnalysisRequest {
    pub problem: String,
    pub analysis_type: Option<String>,
}

#[derive(Debug, Deserialize)]
pub struct DocumentRequest {
    pub content: String,
    pub output_format: Option<String>,
}

#[derive(Debug, Serialize)]
pub struct ApiResponse<T> {
    pub success: bool,
    pub data: Option<T>,
    pub error: Option<String>,
    pub timestamp: u64,
    pub request_id: String,
}

impl<T> ApiResponse<T> {
    pub fn success(data: T) -> Self {
        Self {
            success: true,
            data: Some(data),
            error: None,
            timestamp: SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs(),
            request_id: Uuid::new_v4().to_string(),
        }
    }

    pub fn error(message: String) -> Self {
        Self {
            success: false,
            data: None,
            error: Some(message),
            timestamp: SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs(),
            request_id: Uuid::new_v4().to_string(),
        }
    }
}

// Application state
#[derive(Clone)]
pub struct AppState {
    pub ai_client: Arc<dyn AIClient>,
    pub request_stats: Arc<RwLock<RequestStats>>,
}

#[derive(Debug, Default)]
pub struct RequestStats {
    pub total_requests: usize,
    pub successful_requests: usize,
    pub failed_requests: usize,
    pub average_response_time_ms: f64,
}

// Rate limiting
#[derive(Debug)]
pub struct RateLimiter {
    requests: Arc<RwLock<HashMap<String, Vec<SystemTime>>>>,
    max_requests: usize,
    window_duration: Duration,
}

impl RateLimiter {
    pub fn new(max_requests: usize, window_duration: Duration) -> Self {
        Self {
            requests: Arc::new(RwLock::new(HashMap::new())),
            max_requests,
            window_duration,
        }
    }

    pub async fn check_rate_limit(&self, client_id: &str) -> bool {
        let mut requests = self.requests.write().await;
        let now = SystemTime::now();
        
        let client_requests = requests.entry(client_id.to_string()).or_insert_with(Vec::new);
        
        // Remove old requests outside the window
        client_requests.retain(|&time| {
            now.duration_since(time).unwrap_or(Duration::ZERO) < self.window_duration
        });
        
        if client_requests.len() >= self.max_requests {
            return false;
        }
        
        client_requests.push(now);
        true
    }
}

// Handler functions
pub async fn scaffold_project(
    State(state): State<AppState>,
    headers: HeaderMap,
    Json(request): Json<ScaffoldRequest>,
) -> Result<Json<ApiResponse<serde_json::Value>>, StatusCode> {
    let start_time = std::time::Instant::now();
    info!("Scaffold project request: {}", request.description);

    // Validate request
    if request.description.is_empty() {
        return Ok(Json(ApiResponse::error(
            "Description field is required".to_string(),
        )));
    }

    // Generate prompt and call AI service
    let prompt = scaffolder_planning_prompt(&request.description, &request.settings);
    
    match state.ai_client.complete(&prompt).await {
        Ok(response) => {
            // Try to parse as JSON, fallback to string response
            let parsed_response = serde_json::from_str::<serde_json::Value>(&response)
                .unwrap_or_else(|_| serde_json::Value::String(response));

            // Update stats
            let elapsed = start_time.elapsed();
            update_request_stats(&state.request_stats, true, elapsed.as_millis() as f64).await;

            info!("Scaffold project completed in {:?}", elapsed);
            Ok(Json(ApiResponse::success(parsed_response)))
        }
        Err(e) => {
            let elapsed = start_time.elapsed();
            update_request_stats(&state.request_stats, false, elapsed.as_millis() as f64).await;
            
            error!("Scaffold project failed: {}", e);
            Ok(Json(ApiResponse::error(format!("AI processing failed: {}", e))))
        }
    }
}

pub async fn analyze_problem(
    State(state): State<AppState>,
    Json(request): Json<AnalysisRequest>,
) -> Result<Json<ApiResponse<String>>, StatusCode> {
    let start_time = std::time::Instant::now();
    info!("Analysis request: {}", &request.problem[..request.problem.len().min(50)]);

    if request.problem.is_empty() {
        return Ok(Json(ApiResponse::error(
            "Problem field is required".to_string(),
        )));
    }

    let prompt = match request.analysis_type.as_deref() {
        Some("reasoning") | None => step_by_step_reasoning_prompt(&request.problem),
        Some("summary") => format!("Summarize: {}", request.problem),
        Some("stakeholder") => format!("Identify stakeholders in: {}", request.problem),
        Some(unknown) => {
            return Ok(Json(ApiResponse::error(format!(
                "Unknown analysis type: {}",
                unknown
            ))));
        }
    };

    match state.ai_client.complete(&prompt).await {
        Ok(response) => {
            let elapsed = start_time.elapsed();
            update_request_stats(&state.request_stats, true, elapsed.as_millis() as f64).await;
            
            info!("Analysis completed in {:?}", elapsed);
            Ok(Json(ApiResponse::success(response)))
        }
        Err(e) => {
            let elapsed = start_time.elapsed();
            update_request_stats(&state.request_stats, false, elapsed.as_millis() as f64).await;
            
            error!("Analysis failed: {}", e);
            Ok(Json(ApiResponse::error(format!("AI processing failed: {}", e))))
        }
    }
}

pub async fn process_document(
    State(state): State<AppState>,
    Json(request): Json<DocumentRequest>,
) -> Result<Json<ApiResponse<String>>, StatusCode> {
    let start_time = std::time::Instant::now();
    info!("Document processing request: {} chars", request.content.len());

    if request.content.is_empty() {
        return Ok(Json(ApiResponse::error(
            "Content field is required".to_string(),
        )));
    }

    let prompt = match request.output_format.as_deref() {
        Some("readme") | None => chunk_summary_prompt_readme(&request.content),
        Some("summary") => format!("Create summary of: {}", request.content),
        Some("analysis") => format!("Analyze document: {}", request.content),
        Some(unknown) => {
            return Ok(Json(ApiResponse::error(format!(
                "Unknown output format: {}",
                unknown
            ))));
        }
    };

    // Handle large documents by chunking
    if request.content.len() > 10000 {
        return handle_large_document(&state, &request.content, &request.output_format).await;
    }

    match state.ai_client.complete(&prompt).await {
        Ok(response) => {
            let elapsed = start_time.elapsed();
            update_request_stats(&state.request_stats, true, elapsed.as_millis() as f64).await;
            
            info!("Document processing completed in {:?}", elapsed);
            Ok(Json(ApiResponse::success(response)))
        }
        Err(e) => {
            let elapsed = start_time.elapsed();
            update_request_stats(&state.request_stats, false, elapsed.as_millis() as f64).await;
            
            error!("Document processing failed: {}", e);
            Ok(Json(ApiResponse::error(format!("AI processing failed: {}", e))))
        }
    }
}

async fn handle_large_document(
    state: &AppState,
    content: &str,
    output_format: &Option<String>,
) -> Result<Json<ApiResponse<String>>, StatusCode> {
    info!("Processing large document with chunking");
    
    let chunk_size = 5000;
    let chunks: Vec<&str> = content
        .chars()
        .collect::<Vec<char>>()
        .chunks(chunk_size)
        .map(|chunk| chunk.iter().collect::<String>())
        .collect::<Vec<String>>()
        .iter()
        .map(|s| s.as_str())
        .collect();

    let mut results = Vec::new();
    
    for (i, chunk) in chunks.iter().enumerate() {
        let prompt = match output_format.as_deref() {
            Some("readme") | None => chunk_summary_prompt_readme(chunk),
            Some("summary") => format!("Create summary of: {}", chunk),
            Some("analysis") => format!("Analyze document: {}", chunk),
            _ => continue,
        };

        match state.ai_client.complete(&prompt).await {
            Ok(response) => {
                results.push(format!("Chunk {}: {}", i + 1, response));
            }
            Err(e) => {
                warn!("Failed to process chunk {}: {}", i + 1, e);
                results.push(format!("Chunk {}: Processing failed", i + 1));
            }
        }
    }

    let combined_result = results.join("\n\n");
    Ok(Json(ApiResponse::success(combined_result)))
}

// Batch processing endpoint
#[derive(Debug, Deserialize)]
pub struct BatchRequest {
    pub requests: Vec<BatchItem>,
}

#[derive(Debug, Deserialize)]
pub struct BatchItem {
    pub id: String,
    pub request_type: String,
    pub data: serde_json::Value,
}

pub async fn batch_process(
    State(state): State<AppState>,
    Json(request): Json<BatchRequest>,
) -> Result<Json<ApiResponse<Vec<serde_json::Value>>>, StatusCode> {
    info!("Batch processing request: {} items", request.requests.len());

    if request.requests.len() > 10 {
        return Ok(Json(ApiResponse::error(
            "Maximum 10 requests allowed per batch".to_string(),
        )));
    }

    let mut results = Vec::new();
    
    // Process requests concurrently
    let tasks: Vec<_> = request.requests
        .into_iter()
        .enumerate()
        .map(|(index, item)| {
            let state = state.clone();
            tokio::spawn(async move {
                let result = match item.request_type.as_str() {
                    "scaffold" => {
                        if let Ok(req) = serde_json::from_value::<ScaffoldRequest>(item.data) {
                            let prompt = scaffolder_planning_prompt(&req.description, &req.settings);
                            state.ai_client.complete(&prompt).await
                        } else {
                            Err("Invalid scaffold request".into())
                        }
                    }
                    "analysis" => {
                        if let Ok(req) = serde_json::from_value::<AnalysisRequest>(item.data) {
                            let prompt = step_by_step_reasoning_prompt(&req.problem);
                            state.ai_client.complete(&prompt).await
                        } else {
                            Err("Invalid analysis request".into())
                        }
                    }
                    _ => Err("Unknown request type".into()),
                };

                (index, item.id, result)
            })
        })
        .collect();

    let task_results = futures::future::join_all(tasks).await;
    
    for task_result in task_results {
        match task_result {
            Ok((index, id, result)) => {
                let response = match result {
                    Ok(data) => serde_json::json!({
                        "id": id,
                        "success": true,
                        "data": data,
                        "error": null
                    }),
                    Err(e) => serde_json::json!({
                        "id": id,
                        "success": false,
                        "data": null,
                        "error": e.to_string()
                    }),
                };
                results.push((index, response));
            }
            Err(e) => {
                results.push((
                    usize::MAX,
                    serde_json::json!({
                        "id": "unknown",
                        "success": false,
                        "data": null,
                        "error": format!("Task execution failed: {}", e)
                    }),
                ));
            }
        }
    }

    // Sort results by original index
    results.sort_by_key(|(index, _)| *index);
    let sorted_results: Vec<serde_json::Value> = results.into_iter().map(|(_, result)| result).collect();

    Ok(Json(ApiResponse::success(sorted_results)))
}

// Health check endpoint
pub async fn health_check(
    State(state): State<AppState>,
) -> Json<serde_json::Value> {
    let stats = state.request_stats.read().await;
    
    // Test AI client with a simple prompt
    let ai_status = match state.ai_client.complete("health check").await {
        Ok(_) => "healthy",
        Err(_) => "unhealthy",
    };

    Json(serde_json::json!({
        "status": "healthy",
        "timestamp": SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs(),
        "services": {
            "ai_client": ai_status
        },
        "stats": {
            "total_requests": stats.total_requests,
            "successful_requests": stats.successful_requests,
            "failed_requests": stats.failed_requests,
            "average_response_time_ms": stats.average_response_time_ms
        }
    }))
}

// Statistics endpoint
pub async fn get_stats(
    State(state): State<AppState>,
) -> Json<serde_json::Value> {
    let stats = state.request_stats.read().await;
    
    Json(serde_json::json!({
        "total_requests": stats.total_requests,
        "successful_requests": stats.successful_requests,
        "failed_requests": stats.failed_requests,
        "success_rate": if stats.total_requests > 0 {
            stats.successful_requests as f64 / stats.total_requests as f64 * 100.0
        } else {
            0.0
        },
        "average_response_time_ms": stats.average_response_time_ms
    }))
}

async fn update_request_stats(
    request_stats: &Arc<RwLock<RequestStats>>,
    success: bool,
    response_time_ms: f64,
) {
    let mut stats = request_stats.write().await;
    stats.total_requests += 1;
    
    if success {
        stats.successful_requests += 1;
    } else {
        stats.failed_requests += 1;
    }
    
    // Update rolling average
    let total_time = stats.average_response_time_ms * (stats.total_requests - 1) as f64;
    stats.average_response_time_ms = (total_time + response_time_ms) / stats.total_requests as f64;
}

// Application setup
pub fn create_app(ai_client: Arc<dyn AIClient>) -> Router {
    let state = AppState {
        ai_client,
        request_stats: Arc::new(RwLock::new(RequestStats::default())),
    };

    Router::new()
        .route("/api/scaffold", post(scaffold_project))
        .route("/api/analyze", post(analyze_problem))
        .route("/api/document", post(process_document))
        .route("/api/batch", post(batch_process))
        .route("/health", get(health_check))
        .route("/stats", get(get_stats))
        .with_state(state)
        .layer(
            ServiceBuilder::new()
                .layer(TraceLayer::new_for_http())
                .layer(CorsLayer::very_permissive())
        )
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize tracing
    tracing_subscriber::fmt()
        .with_env_filter("info,axum_service=debug")
        .init();

    info!("Starting Axum Prompt Service");

    // Initialize AI client
    let ai_client: Arc<dyn AIClient> = Arc::new(MockAIClient::new(Duration::from_millis(200)));

    // Create application
    let app = create_app(ai_client);

    // Start server
    let addr = "0.0.0.0:3000";
    info!("Server listening on {}", addr);
    
    let listener = tokio::net::TcpListener::bind(addr).await?;
    axum::serve(listener, app).await?;

    Ok(())
}

/*
To run this example:

1. Add to Cargo.toml:
[dependencies]
axum = "0.7"
tokio = { version = "1.0", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
async-trait = "0.1"
futures = "0.3"
tower = "0.4"
tower-http = { version = "0.5", features = ["cors", "trace"] }
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
uuid = { version = "1.0", features = ["v4"] }

2. Run with:
cargo run --bin axum_service --features web-service

3. Test endpoints:
curl -X POST http://localhost:3000/api/scaffold \
  -H "Content-Type: application/json" \
  -d '{"description": "Build a REST API", "language": "rust", "template": "axum"}'

curl -X POST http://localhost:3000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"problem": "How to scale microservices?", "analysis_type": "reasoning"}'

curl http://localhost:3000/health
curl http://localhost:3000/stats
*/