### Overview

This document defines a generic serverless system template focusing on architectural strategies:
- function-as-a-service (FaaS), cloud-native, and event-driven serverless computing with managed cloud services integration.
- Every project must be designed first conceptually from the Function-out. Then ask:
      - "Given this business capability, what functions are needed, what events trigger them, how should they scale, and what managed services should handle infrastructure concerns?"
- Function-out: Define business functions first, identify triggers and events, design stateless execution models.
- Cloud-native: Leverage managed cloud services for data, messaging, authentication, and infrastructure.
- Ensure extended future scalability, cost efficiency + auto-scaling, rapid deployment via serverless execution, event-driven triggers.

### EXAMPLE ONLY Project Map of a serverless architecture project following FaaS and cloud-native patterns

```go
serverless-application/
├─ serverless.yml                    # Serverless Framework configuration
├─ terraform/                        # Infrastructure as Code
│  ├─ main.tf
│  ├─ variables.tf
│  └─ outputs.tf
├─ functions/
│  ├─ user-management/
│  │  ├─ create-user/
│  │  │  ├─ handler.py
│  │  │  ├─ requirements.txt
│  │  │  ├─ schema.json
│  │  │  └─ tests/
│  │  │     ├─ test_handler.py
│  │  │     └─ fixtures/
│  │  ├─ get-user/
│  │  │  ├─ handler.py
│  │  │  ├─ requirements.txt
│  │  │  └─ tests/
│  │  ├─ update-user/
│  │  │  ├─ handler.py
│  │  │  ├─ requirements.txt
│  │  │  └─ tests/
│  │  └─ delete-user/
│  │     ├─ handler.py
│  │     ├─ requirements.txt
│  │     └─ tests/
│  ├─ order-processing/
│  │  ├─ create-order/
│  │  │  ├─ index.js
│  │  │  ├─ package.json
│  │  │  ├─ validation.js
│  │  │  └─ tests/
│  │  ├─ process-payment/
│  │  │  ├─ index.js
│  │  │  ├─ package.json
│  │  │  ├─ stripe-client.js
│  │  │  └─ tests/
│  │  ├─ fulfill-order/
│  │  │  ├─ index.js
│  │  │  ├─ package.json
│  │  │  └─ tests/
│  │  └─ order-status/
│  │     ├─ index.js
│  │     ├─ package.json
│  │     └─ tests/
│  ├─ notifications/
│  │  ├─ email-notification/
│  │  │  ├─ main.go
│  │  │  ├─ go.mod
│  │  │  ├─ templates/
│  │  │  │  ├─ welcome.html
│  │  │  │  └─ order-confirmation.html
│  │  │  └─ tests/
│  │  ├─ sms-notification/
│  │  │  ├─ main.go
│  │  │  ├─ go.mod
│  │  │  └─ tests/
│  │  └─ push-notification/
│  │     ├─ main.go
│  │     ├─ go.mod
│  │     └─ tests/
│  ├─ analytics/
│  │  ├─ event-processor/
│  │  │  ├─ src/
│  │  │  │  ├─ main.rs
│  │  │  │  ├─ processors/
│  │  │  │  │  ├─ user_events.rs
│  │  │  │  │  └─ order_events.rs
│  │  │  │  └─ models/
│  │  │  ├─ Cargo.toml
│  │  │  └─ tests/
│  │  ├─ metrics-aggregator/
│  │  │  ├─ src/
│  │  │  │  ├─ main.rs
│  │  │  │  ├─ aggregators/
│  │  │  │  └─ storage/
│  │  │  ├─ Cargo.toml
│  │  │  └─ tests/
│  │  └─ report-generator/
│  │     ├─ src/
│  │     │  ├─ main.rs
│  │     │  ├─ generators/
│  │     │  └─ formatters/
│  │     ├─ Cargo.toml
│  │     └─ tests/
│  └─ utilities/
│     ├─ image-processor/
│     │  ├─ handler.py
│     │  ├─ requirements.txt
│     │  ├─ image_utils.py
│     │  └─ tests/
│     ├─ file-converter/
│     │  ├─ handler.py
│     │  ├─ requirements.txt
│     │  └─ tests/
│     └─ data-validator/
│        ├─ handler.py
│        ├─ requirements.txt
│        ├─ validators.py
│        └─ tests/
├─ layers/                           # Shared code layers
│  ├─ common-utils/
│  │  ├─ python/
│  │  │  ├─ common/
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ logger.py
│  │  │  │  ├─ auth.py
│  │  │  │  ├─ database.py
│  │  │  │  └─ validators.py
│  │  │  └─ requirements.txt
│  │  ├─ nodejs/
│  │  │  ├─ common/
│  │  │  │  ├─ logger.js
│  │  │  │  ├─ auth.js
│  │  │  │  ├─ database.js
│  │  │  │  └─ validators.js
│  │  │  └─ package.json
│  │  └─ golang/
│  │     ├─ common/
│  │     │  ├─ logger.go
│  │     │  ├─ auth.go
│  │     │  ├─ database.go
│  │     │  └─ validators.go
│  │     └─ go.mod
│  └─ external-apis/
│     ├─ stripe-client/
│     ├─ sendgrid-client/
│     └─ twilio-client/
├─ api-gateway/
│  ├─ openapi.yml                   # API Gateway configuration
│  ├─ authorizers/
│  │  ├─ jwt-authorizer/
│  │  │  ├─ handler.py
│  │  │  └─ tests/
│  │  └─ api-key-authorizer/
│  │     ├─ handler.py
│  │     └─ tests/
│  └─ validators/
│     ├─ request-validator.json
│     └─ response-validator.json
├─ events/
│  ├─ schemas/
│  │  ├─ user-events.json
│  │  ├─ order-events.json
│  │  └─ system-events.json
│  ├─ rules/
│  │  ├─ user-lifecycle.json
│  │  ├─ order-processing.json
│  │  └─ notifications.json
│  └─ patterns/
│     ├─ event-patterns.json
│     └─ dead-letter-handling.json
├─ workflows/
│  ├─ order-fulfillment/
│  │  ├─ definition.json           # Step Functions definition
│  │  ├─ states/
│  │  │  ├─ validate-order.py
│  │  │  ├─ process-payment.py
│  │  │  ├─ update-inventory.py
│  │  │  └─ send-notification.py
│  │  └─ tests/
│  ├─ user-onboarding/
│  │  ├─ definition.json
│  │  ├─ states/
│  │  └─ tests/
│  └─ data-pipeline/
│     ├─ definition.json
│     ├─ states/
│     └─ tests/
├─ storage/
│  ├─ dynamodb/
│  │  ├─ tables/
│  │  │  ├─ users.json
│  │  │  ├─ orders.json
│  │  │  └─ analytics.json
│  │  └─ indexes/
│  ├─ s3/
│  │  ├─ buckets/
│  │  │  ├─ user-uploads.json
│  │  │  ├─ processed-files.json
│  │  │  └─ backups.json
│  │  └─ lifecycle-policies/
│  └─ rds/
│     ├─ aurora-serverless/
│     └─ connection-config/
├─ monitoring/
│  ├─ dashboards/
│  │  ├─ function-metrics.json
│  │  ├─ api-gateway-metrics.json
│  │  └─ cost-analysis.json
│  ├─ alarms/
│  │  ├─ error-rates.json
│  │  ├─ duration-limits.json
│  │  └─ cost-thresholds.json
│  └─ logs/
│     ├─ log-groups.json
│     └─ retention-policies.json
├─ testing/
│  ├─ unit/
│  │  ├─ functions/
│  │  └─ layers/
│  ├─ integration/
│  │  ├─ api-tests/
│  │  ├─ workflow-tests/
│  │  └─ event-tests/
│  ├─ load/
│  │  ├─ artillery/
│  │  └─ k6/
│  └─ e2e/
│     ├─ user-journeys/
│     └─ business-scenarios/
├─ deployment/
│  ├─ environments/
│  │  ├─ dev.yml
│  │  ├─ staging.yml
│  │  └─ prod.yml
│  ├─ ci-cd/
│  │  ├─ github-actions/
│  │  ├─ codepipeline/
│  │  └─ jenkins/
│  └─ scripts/
│     ├─ deploy.sh
│     ├─ rollback.sh
│     └─ cleanup.sh
└─ docs/
   ├─ architecture/
   │  ├─ function-design.md
   │  ├─ event-flows.md
   │  ├─ cost-optimization.md
   │  └─ security-model.md
   ├─ api/
   │  ├─ function-apis.md
   │  └─ event-schemas.md
   └─ operations/
      ├─ deployment-guide.md
      ├─ monitoring-guide.md
      └─ troubleshooting.md
```

### Serverless Architecture Implementation

This section documents the Serverless Architecture approach, emphasizing Function-as-a-Service (FaaS), cloud-native managed services, and event-driven serverless computing.
This serves as a generic template for implementing cost-effective, auto-scaling, and rapidly deployable serverless applications.

#### Core Principles

- **Function-Centric Design**: Applications composed of small, focused functions that do one thing well.
- **Event-Driven Execution**: Functions triggered by events from various sources (HTTP, databases, queues, schedules).
- **Stateless Functions**: Functions are stateless and ephemeral, with state managed by external services.
- **Managed Services**: Leverage cloud provider managed services for infrastructure, databases, messaging, and authentication.
- **Auto-Scaling**: Functions automatically scale based on demand with pay-per-execution pricing.
- **Rapid Deployment**: Fast deployment cycles with infrastructure as code and automated CI/CD.
- **Cost Optimization**: Pay-per-use model optimizes costs for variable and unpredictable workloads.

#### Architecture Structure

1. **Function Layer** (Business Logic)
   - **Components**: Lambda functions, Azure Functions, Google Cloud Functions
   - **Responsibilities**: Stateless business logic execution, event processing
   - **Dependencies**: Managed cloud services, external APIs
   - **Rules**:
     - Functions should be small and focused on single responsibility
     - Stateless design with external state management
     - Timeout and memory optimization for cost efficiency
     - Cold start optimization for performance

2. **API Gateway Layer** (HTTP Interface)
   - **Components**: AWS API Gateway, Azure API Management, Google Cloud Endpoints
   - **Responsibilities**: HTTP routing, authentication, rate limiting, request/response transformation
   - **Dependencies**: Backend functions, authentication services
   - **Rules**:
     - RESTful API design with proper HTTP methods and status codes
     - Request validation and response formatting
     - Authentication and authorization enforcement
     - CORS configuration for web clients

3. **Event Sources** (Triggers)
   - **Components**: HTTP requests, database changes, file uploads, queues, schedules, IoT events
   - **Responsibilities**: Function invocation triggers, event payload delivery
   - **Dependencies**: Event sources (S3, DynamoDB, SQS, EventBridge, etc.)
   - **Rules**:
     - Appropriate trigger selection based on use case requirements
     - Event filtering and routing configuration
     - Error handling and dead letter queue setup
     - Batch processing configuration for high-volume events

4. **Data Layer** (Managed Storage)
   - **Components**: DynamoDB, RDS Aurora Serverless, S3, CosmosDB, Cloud Storage
   - **Responsibilities**: Data persistence, caching, file storage
   - **Dependencies**: Functions access data through SDKs/APIs
   - **Rules**:
     - NoSQL for simple key-value and document storage
     - SQL for complex relational queries with serverless scaling
     - Object storage for files and static assets
     - Appropriate indexing and partitioning strategies

5. **Integration Layer** (Service Communication)
   - **Components**: SQS, SNS, EventBridge, Service Bus, Pub/Sub
   - **Responsibilities**: Asynchronous communication, event routing, message queuing
   - **Dependencies**: Functions publish and consume messages
   - **Rules**:
     - Asynchronous processing for loose coupling
     - Message ordering and deduplication where required
     - Dead letter queues for failed message processing
     - Event schema versioning and compatibility

6. **Observability Layer** (Monitoring)
   - **Components**: CloudWatch, Application Insights, Cloud Monitoring, X-Ray
   - **Responsibilities**: Logging, metrics, tracing, alerting
   - **Dependencies**: All functions participate in observability
   - **Rules**:
     - Structured logging with correlation IDs
     - Custom metrics for business KPIs
     - Distributed tracing for request flows
     - Cost monitoring and optimization alerts

#### Interfaces, Contracts, and API Requirements

- **Function Interface Standards**
  - All functions MUST have well-defined input/output schemas.
  - Functions MUST be idempotent where possible to handle retries safely.
  - Functions MUST handle errors gracefully and return appropriate status codes.
  - Functions MUST implement health checks and monitoring hooks.

- **Event Contracts**
  - **Event Structure**: Standard event envelope with metadata, timestamp, source, and payload
  - **Schema Validation**: Events validated against JSON schemas or protocol buffers
  - **Versioning**: Event schema versioning with backward compatibility
  - **Filtering**: Event filtering capabilities to reduce unnecessary function invocations

- **API Contracts**
  - **OpenAPI Specification**: All HTTP APIs documented with OpenAPI/Swagger
  - **Request/Response Format**: Consistent JSON API format with error handling
  - **Authentication**: JWT, API keys, or OAuth2 for secure access
  - **Rate Limiting**: Appropriate rate limits to prevent abuse and control costs

- **Integration Patterns**
  - **Request-Response**: Synchronous HTTP-based function invocation
  - **Fire-and-Forget**: Asynchronous event-driven function invocation
  - **Workflow Orchestration**: Step Functions or Logic Apps for complex business processes
  - **Fan-out/Fan-in**: Parallel processing with result aggregation

#### Dependency Flow

```
[Event Sources] → [Functions] → [Managed Services]
       ↓              ↓              ↓
[API Gateway]    [Business Logic]  [Data Storage]
[Queues/Topics]  [Integrations]   [External APIs]
[Schedules]      [Workflows]      [Authentication]
```

- Event sources trigger function execution
- Functions execute business logic using managed services
- Results stored in appropriate data services or sent to other systems
- Observability captures all interactions for monitoring and debugging

#### Service Integration Points

- **External API Integration**: Functions integrate with third-party APIs using HTTP clients
- **Database Integration**: Functions access databases through managed service SDKs
- **Message Queue Integration**: Functions publish and consume messages from queues/topics
- **File Storage Integration**: Functions process files from object storage services
- **Workflow Integration**: Functions participate in complex workflows and state machines

#### Rules for AI Agents

1. **Single Responsibility**: Each function should have one clear, focused responsibility
2. **Stateless Design**: Functions must be stateless with external state management
3. **Error Handling**: Implement comprehensive error handling with appropriate retry policies
4. **Performance Optimization**: Optimize for cold start time and execution duration
5. **Cost Awareness**: Monitor and optimize function costs through resource allocation
6. **Security**: Implement least privilege access and secure secrets management
7. **Observability**: Include logging, metrics, and tracing in every function
8. **Testing**: Comprehensive testing including unit, integration, and load testing

#### Example Implementation

- E-commerce order processing: API Gateway receives order → CreateOrder function validates and stores order → triggers ProcessPayment function → on success triggers FulfillOrder function → sends confirmation via NotificationFunction
- Each function handles one step in the process
- Functions communicate through events and managed services
- System scales automatically based on order volume
- Pay only for actual function execution time

This architecture ensures applications remain cost-effective, automatically scalable, and rapidly deployable while leveraging managed cloud services for operational simplicity.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **Function Scope**: Keep functions small and focused on single business operations to optimize performance and maintainability.

2. **Stateless Design**: Design functions to be completely stateless with all state managed by external services.

3. **Cold Start Optimization**: Minimize cold start latency through proper language choice, dependency management, and initialization patterns.

4. **Error Resilience**: Implement comprehensive error handling, retry logic, and dead letter queues for failed executions.

5. **Cost Optimization**: Monitor function duration, memory usage, and invocation patterns to optimize costs.

6. **Security by Default**: Implement least privilege IAM policies, secure environment variables, and input validation.

7. **Observability Integration**: Include structured logging, custom metrics, and distributed tracing from function inception.

8. **Event-Driven Design**: Design functions to be triggered by appropriate events rather than polling or scheduled execution where possible.

**Code Review Checklist for AI Agents:**

- [ ] Function has single, well-defined responsibility
- [ ] Function is stateless with external state management
- [ ] Error handling includes retry logic and dead letter queues
- [ ] Function timeout and memory settings optimized for use case
- [ ] IAM permissions follow least privilege principle
- [ ] Logging includes correlation IDs and structured format
- [ ] Input validation and output formatting implemented
- [ ] Function can handle concurrent executions safely

### Architectural Concepts

- **Function-as-a-Service (FaaS)**: Serverless compute model where functions execute in response to events.
- **Event-Driven Architecture**: Functions triggered by various event sources (HTTP, database, file, schedule).
- **Managed Services**: Cloud provider services that handle infrastructure management automatically.
- **Auto-Scaling**: Automatic scaling based on demand with no capacity planning required.
- **Pay-per-Execution**: Cost model where you pay only for actual function execution time and resources used.
- **Infrastructure as Code**: Declarative infrastructure definition using tools like Serverless Framework or SAM.

### UI/UX Strategies

- **JAMstack Architecture**: Static sites with dynamic functionality powered by serverless functions.
- **Progressive Web Apps**: Client-side applications that use serverless APIs for backend functionality.
- **Real-time Features**: WebSocket APIs powered by serverless functions for live updates.
- **Edge Computing**: Functions deployed to edge locations for reduced latency.
- **Mobile Backend**: Serverless APIs optimized for mobile applications with offline support.

### Performance Strategies (Speed & Power)

- **Cold Start Optimization**: Language choice (Go, Node.js), dependency reduction, connection pooling.
- **Memory vs Duration Trade-offs**: Higher memory allocation for CPU-intensive tasks to reduce duration.
- **Connection Reuse**: Persistent connections to databases and external services across invocations.
- **Caching Strategies**: In-memory caching, external cache services, and CDN integration.
- **Async Processing**: Asynchronous processing for I/O-bound operations to improve throughput.

### Memory Optimization & Safety

- **Right-Sizing Functions**: Allocate appropriate memory based on actual function requirements.
- **Memory Leak Prevention**: Proper cleanup of resources and connections in function handlers.
- **Garbage Collection Tuning**: Language-specific GC optimization for serverless environments.
- **Resource Monitoring**: Monitor memory usage patterns and optimize allocation accordingly.

```python
# Example: Optimized Lambda function with connection reuse
import json
import boto3
from functools import lru_cache

# Initialize clients outside handler for connection reuse
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

@lru_cache(maxsize=100)
def get_user_from_cache(user_id):
    """Cache frequently accessed users in memory"""
    response = table.get_item(Key={'user_id': user_id})
    return response.get('Item')

def lambda_handler(event, context):
    user_id = event['pathParameters']['user_id']
    
    try:
        user = get_user_from_cache(user_id)
        if not user:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
        
        return {
            'statusCode': 200,
            'body': json.dumps(user)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

### Logging Strategies

- **Structured Logging**: JSON-formatted logs with consistent fields across all functions.
- **Correlation Tracking**: Request correlation IDs to track execution across function calls.
- **Log Aggregation**: Centralized logging using cloud-native log aggregation services.
- **Cost-Aware Logging**: Balance logging detail with storage and analysis costs.
- **Security Logging**: Audit logs for security events and compliance requirements.

### Security Strategies

- **Least Privilege IAM**: Functions granted minimal permissions required for their operations.
- **Secrets Management**: Secure storage and retrieval of sensitive configuration and credentials.
- **Input Validation**: Comprehensive validation of all function inputs and event payloads.
- **Network Security**: VPC configuration for functions requiring private network access.
- **Runtime Security**: Regular updates of function runtimes and dependencies.
- **API Security**: Authentication, authorization, and rate limiting at API Gateway level.

### Networking / API Strategies

- **API Gateway Patterns**: RESTful APIs, GraphQL endpoints, WebSocket APIs for different use cases.
- **Custom Domains**: Branded API endpoints with SSL/TLS certificates.
- **CORS Configuration**: Proper cross-origin resource sharing for web applications.
- **API Versioning**: Strategies for API evolution without breaking existing clients.
- **Response Caching**: API Gateway and CDN caching for improved performance and cost reduction.

### Function Communication Strategies

- **Synchronous Invocation**: Direct function-to-function calls for immediate response requirements.
- **Asynchronous Messaging**: Queue-based communication for loose coupling and reliability.
- **Event-Driven Workflows**: Step Functions or Logic Apps for complex business process orchestration.
- **Publish-Subscribe**: Event-driven communication patterns for decoupled system integration.

```javascript
// Example: Event-driven function communication
exports.handler = async (event) => {
    const AWS = require('aws-sdk');
    const eventbridge = new AWS.EventBridge();
    
    // Process the order
    const order = await processOrder(event.order);
    
    // Publish event for other functions to consume
    await eventbridge.putEvents({
        Entries: [{
            Source: 'ecommerce.orders',
            DetailType: 'Order Processed',
            Detail: JSON.stringify({
                orderId: order.id,
                customerId: order.customerId,
                amount: order.total,
                timestamp: new Date().toISOString()
            })
        }]
    }).promise();
    
    return {
        statusCode: 200,
        body: JSON.stringify({ orderId: order.id })
    };
};
```

### Data Activities & Consistency Strategies

- **Eventually Consistent**: Accept eventual consistency for cross-function data operations.
- **Idempotent Operations**: Design functions to handle duplicate invocations safely.
- **Transaction Boundaries**: Use managed transaction services for multi-step operations.
- **Event Sourcing**: Store events for auditability and state reconstruction.
- **Data Validation**: Validate data at function boundaries to ensure data quality.

### Database Design & Optimizations

- **Database Selection**: Choose appropriate database services based on access patterns and scalability needs.
- **Connection Management**: Optimize database connections for serverless execution patterns.
- **Query Optimization**: Design queries and indexes for serverless function access patterns.
- **Data Partitioning**: Partition data appropriately for parallel serverless processing.

| Database Type | Serverless Service | Use Case | Optimization Strategy |
|--------------|-------------------|----------|----------------------|
| NoSQL | DynamoDB, CosmosDB | Key-value, document | Partition key design, on-demand billing |
| SQL | Aurora Serverless, SQL Database | Relational queries | Connection pooling, query optimization |
| Cache | ElastiCache Serverless | Session, temporary data | TTL policies, memory sizing |
| Search | OpenSearch Serverless | Full-text search | Index optimization, query tuning |
| Time-series | Timestream | Metrics, IoT data | Data retention, aggregation strategies |

### Source Control Strategies

- **Monorepo vs Multi-repo**: Consider deployment dependencies and team structure.
- **Function Versioning**: Semantic versioning for function deployments with alias management.
- **Infrastructure as Code**: Version control for infrastructure definitions and configurations.
- **Environment Configuration**: Environment-specific configurations and secrets management.
- **Deployment Automation**: Automated testing and deployment pipelines for functions.

### CI/CD Strategies

- **Automated Testing**: Unit tests, integration tests, and performance tests in CI pipeline.
- **Multi-Environment Deployment**: Separate environments for development, staging, and production.
- **Blue-Green Deployment**: Zero-downtime deployments using function aliases and weighted routing.
- **Canary Releases**: Gradual rollout of function updates with automatic rollback on errors.
- **Infrastructure Deployment**: Automated infrastructure provisioning and updates.

### Engineering Approach: Function-First & Event-Driven

- **Function Decomposition**: Break down business capabilities into focused, single-purpose functions.
- **Event Modeling**: Design system interactions around business events and triggers.
- **API-First Design**: Define function APIs and contracts before implementation.
- **Cost-Driven Architecture**: Consider cost implications in architectural decisions.
- **Serverless-Native**: Design specifically for serverless constraints and benefits.

### Testing Strategies

Comprehensive testing strategy for serverless applications with distributed function execution:

- **Unit Testing**: Test individual function logic in isolation with mocked dependencies.
- **Integration Testing**: Test function interactions with managed services and external APIs.
- **Contract Testing**: Verify API contracts and event schemas between functions.
- **Load Testing**: Test function performance under various load conditions and concurrency levels.
- **Chaos Testing**: Test system resilience under function failures and service degradation.
- **Cost Testing**: Monitor and test cost implications of different usage patterns.
- **Security Testing**: Penetration testing and vulnerability assessment of function endpoints.

Test organization for serverless applications:
```
tests/
├─ unit/
│  ├─ functions/        # Individual function logic
│  ├─ layers/          # Shared layer testing
│  └─ utilities/       # Helper function testing
├─ integration/
│  ├─ api/            # API Gateway integration
│  ├─ events/         # Event source integration
│  ├─ workflows/      # Step function workflows
│  └─ databases/      # Database integration
├─ load/
│  ├─ concurrency/    # Concurrent execution testing
│  ├─ throughput/     # High-volume event processing
│  └─ cost-analysis/  # Cost impact of load patterns
└─ e2e/
   ├─ user-journeys/  # Complete user scenarios
   └─ business-flows/ # End-to-end business processes
```

### Validation Domains & Best Combination

Validation strategy for serverless architecture with distributed function execution:

| Validation Domain | Implementation Location | Strategy |
|------------------|------------------------|----------|
| Input Validation | Function Entry Points | Validate all function inputs and event payloads |
| Business Logic | Function Implementation | Validate business rules within function context |
| API Contracts | API Gateway | Schema validation and request/response formatting |
| Event Schemas | Event Sources | Validate event structure and required fields |
| Data Integrity | Database Layer | Use managed service validation features |
| Security | Multiple Layers | Authentication at gateway, authorization per function |

**Best Practices:**
- Validate inputs at function boundaries to fail fast and reduce execution costs
- Use API Gateway request validation to prevent invalid requests from reaching functions
- Implement idempotent functions to handle duplicate events and retries safely
- Monitor validation failures and implement cost-aware error handling
- Use managed service validation features to reduce custom validation code
- Implement circuit breaker patterns for external service validation failures