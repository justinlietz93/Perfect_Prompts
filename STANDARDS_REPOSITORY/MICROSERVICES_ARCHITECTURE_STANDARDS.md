### Overview

This document defines a generic distributed microservices template focusing on architectural strategies:
- distributed system design with autonomous services communicating through well-defined APIs and event-driven messaging.
- Every project must be designed first conceptually from the Service-out. Then ask:
      - "Given this business capability, what autonomous services, data boundaries, communication patterns, and resilience mechanisms will be required to build this as a distributed system?"
- Service-out: Define business capabilities as autonomous services, identify service boundaries, then design inter-service communication.
- Domain-driven: Use domain-driven design to identify service boundaries based on business contexts.
- Ensure extended future scalability, fault tolerance + resilience, independent deployability via service autonomy, loose coupling.

### EXAMPLE ONLY Project Map of a microservices architecture project following distributed system patterns

```go
microservices-ecosystem/
├─ docker-compose.yml
├─ kubernetes/
│  ├─ namespaces/
│  ├─ services/
│  └─ ingress/
├─ services/
│  ├─ user-service/
│  │  ├─ Dockerfile
│  │  ├─ pyproject.toml
│  │  ├─ src/
│  │  │  ├─ api/
│  │  │  │  ├─ controllers/
│  │  │  │  ├─ middleware/
│  │  │  │  └─ dto/
│  │  │  ├─ domain/
│  │  │  │  ├─ models/
│  │  │  │  ├─ services/
│  │  │  │  └─ events/
│  │  │  ├─ infrastructure/
│  │  │  │  ├─ database/
│  │  │  │  ├─ messaging/
│  │  │  │  └─ external_services/
│  │  │  ├─ config/
│  │  │  └─ health/
│  │  └─ tests/
│  ├─ order-service/
│  │  ├─ Dockerfile
│  │  ├─ package.json
│  │  ├─ src/
│  │  │  ├─ controllers/
│  │  │  ├─ services/
│  │  │  ├─ models/
│  │  │  ├─ events/
│  │  │  ├─ database/
│  │  │  ├─ messaging/
│  │  │  └─ config/
│  │  └─ tests/
│  ├─ payment-service/
│  │  ├─ Dockerfile
│  │  ├─ Cargo.toml
│  │  ├─ src/
│  │  │  ├─ handlers/
│  │  │  ├─ domain/
│  │  │  ├─ repositories/
│  │  │  ├─ events/
│  │  │  ├─ external/
│  │  │  └─ config/
│  │  └─ tests/
│  ├─ notification-service/
│  │  ├─ Dockerfile
│  │  ├─ go.mod
│  │  ├─ cmd/
│  │  ├─ internal/
│  │  │  ├─ handlers/
│  │  │  ├─ services/
│  │  │  ├─ models/
│  │  │  ├─ messaging/
│  │  │  └─ config/
│  │  └─ tests/
│  └─ inventory-service/
│     ├─ Dockerfile
│     ├─ pom.xml
│     ├─ src/main/java/
│     │  ├─ controllers/
│     │  ├─ services/
│     │  ├─ entities/
│     │  ├─ repositories/
│     │  ├─ events/
│     │  └─ config/
│     └─ src/test/java/
├─ shared/
│  ├─ event-schemas/
│  │  ├─ user-events.avro
│  │  ├─ order-events.avro
│  │  └─ payment-events.avro
│  ├─ api-contracts/
│  │  ├─ openapi/
│  │  └─ protobuf/
│  └─ libraries/
│     ├─ common-logging/
│     ├─ common-metrics/
│     └─ common-security/
├─ infrastructure/
│  ├─ api-gateway/
│  │  ├─ nginx.conf
│  │  ├─ kong/
│  │  └─ traefik/
│  ├─ service-mesh/
│  │  ├─ istio/
│  │  └─ linkerd/
│  ├─ messaging/
│  │  ├─ kafka/
│  │  ├─ rabbitmq/
│  │  └─ nats/
│  ├─ databases/
│  │  ├─ postgresql/
│  │  ├─ mongodb/
│  │  └─ redis/
│  ├─ monitoring/
│  │  ├─ prometheus/
│  │  ├─ grafana/
│  │  ├─ jaeger/
│  │  └─ elk-stack/
│  └─ security/
│     ├─ oauth2/
│     ├─ jwt/
│     └─ tls-certs/
├─ deployment/
│  ├─ terraform/
│  ├─ helm-charts/
│  └─ ci-cd/
│     ├─ github-actions/
│     ├─ jenkins/
│     └─ gitlab-ci/
└─ docs/
   ├─ architecture/
   │  ├─ service-map.md
   │  ├─ data-flow.md
   │  └─ deployment-strategy.md
   ├─ api-docs/
   └─ runbooks/
```

### Microservices Architecture Implementation

This section documents the Microservices Architecture approach for building distributed systems as a collection of loosely coupled, independently deployable services.
This serves as a generic template for implementing scalable, resilient distributed applications.

#### Core Principles

- **Service Autonomy**: Each service owns its data, logic, and deployment lifecycle independently.
- **Business Capability Alignment**: Services organized around business capabilities, not technical layers.
- **Decentralized Governance**: Teams have autonomy over technology choices, data management, and deployment decisions.
- **Failure Isolation**: Failures in one service should not cascade to other services.
- **Evolutionary Design**: Services can evolve independently without coordinated releases.
- **Smart Endpoints, Dumb Pipes**: Business logic in services, simple communication mechanisms between them.

#### Service Structure

1. **Individual Microservice** (Autonomous Unit)
   - **Components**: API layer, business logic, data persistence, messaging
   - **Responsibilities**: Single business capability, data ownership, API contracts
   - **Dependencies**: Minimal dependencies on other services
   - **Rules**:
     - Own database per service (database per service pattern)
     - Expose well-defined APIs (REST, GraphQL, gRPC)
     - Handle own failures and degradation
     - Implement health checks and metrics

2. **API Gateway Layer** (External Interface)
   - **Components**: Request routing, authentication, rate limiting, response aggregation
   - **Responsibilities**: Single entry point, cross-cutting concerns, protocol translation
   - **Dependencies**: Routes to appropriate microservices
   - **Rules**:
     - Authentication and authorization enforcement
     - Request/response transformation
     - Circuit breaker and retry logic
     - API versioning and documentation

3. **Service Mesh** (Communication Infrastructure)
   - **Components**: Service discovery, load balancing, encryption, observability
   - **Responsibilities**: Inter-service communication, security, monitoring
   - **Dependencies**: All microservices participate in mesh
   - **Rules**:
     - Transparent service-to-service communication
     - Automatic load balancing and failover
     - Mutual TLS for security
     - Distributed tracing and metrics collection

4. **Event Messaging System** (Asynchronous Communication)
   - **Components**: Message brokers, event streaming, pub/sub patterns
   - **Responsibilities**: Asynchronous service communication, event sourcing, decoupling
   - **Dependencies**: Services publish and subscribe to events
   - **Rules**:
     - At-least-once or exactly-once delivery guarantees
     - Event schema evolution and versioning
     - Dead letter queues for failed processing
     - Event replay capabilities for recovery

5. **Data Storage** (Distributed Data Management)
   - **Components**: Database per service, distributed transactions, data synchronization
   - **Responsibilities**: Data persistence, consistency, backup and recovery
   - **Dependencies**: Each service owns its data store
   - **Rules**:
     - No direct database access between services
     - Eventual consistency for cross-service data
     - Saga pattern for distributed transactions
     - Data replication and sharding strategies

6. **Observability Stack** (Monitoring and Debugging)
   - **Components**: Metrics, logging, distributed tracing, alerting
   - **Responsibilities**: System health monitoring, performance analysis, troubleshooting
   - **Dependencies**: All services participate in observability
   - **Rules**:
     - Centralized log aggregation
     - Distributed tracing for request flows
     - Service-level metrics and SLAs
     - Automated alerting and escalation

#### Interfaces, Contracts, and API Requirements

- **API Design Standards**
  - All inter-service communication MUST occur through well-defined APIs (REST, GraphQL, gRPC).
  - API contracts MUST be versioned and backward compatible within major versions.
  - Services MUST NOT share databases or make direct database connections to other services' data.
  - API documentation MUST be automatically generated and kept up-to-date.

- **Communication Patterns**
  - **Synchronous**: REST APIs, GraphQL, gRPC for real-time operations
  - **Asynchronous**: Event-driven messaging for eventual consistency and decoupling
  - **Request-Reply**: For operations requiring immediate response
  - **Publish-Subscribe**: For broadcasting events to multiple interested services
  - **Event Sourcing**: For maintaining audit trails and enabling replay capabilities

- **Service Contracts**
  - **API Contracts**: OpenAPI specifications, GraphQL schemas, Protocol Buffer definitions
  - **Event Contracts**: Event schema definitions with versioning support
  - **SLA Contracts**: Service level agreements for availability, latency, and throughput
  - **Data Contracts**: Agreed-upon data formats and semantics between services

- **Dependency Management**
  - Services MUST minimize dependencies on other services
  - Hard dependencies should be avoided; use eventual consistency patterns
  - Circuit breaker pattern for handling service failures
  - Bulkhead pattern for isolating critical resources

- **Security Contracts**
  - **Authentication**: OAuth2, JWT tokens, service-to-service authentication
  - **Authorization**: RBAC, attribute-based access control
  - **Encryption**: TLS for data in transit, encryption at rest for sensitive data
  - **Security Scanning**: Regular vulnerability assessments and dependency checks

#### Dependency Flow

```
[Client] → [API Gateway] → [Service Mesh] → [Microservices]
   ↓             ↓              ↓              ↓
[Auth]    [Load Balancing]  [Discovery]   [Business Logic]
   ↓             ↓              ↓              ↓
[Monitoring] [Rate Limiting] [Encryption]  [Data Store]
```

- Event-driven communication flows asynchronously through message brokers
- Service mesh handles service-to-service communication concerns
- API gateway provides single point of entry for external clients
- Each service maintains its own data store and business logic

#### Service Integration Points

- **API Gateway Integration**: Single entry point for all external requests
- **Message Broker Integration**: Asynchronous communication and event publishing
- **Service Discovery**: Dynamic service registration and discovery
- **Configuration Management**: Centralized configuration with service-specific overrides
- **Monitoring Integration**: Metrics, logs, and traces flowing to observability stack

#### Rules for AI Agents

1. **Service Boundaries**: Define clear business capability boundaries for each service
2. **Data Ownership**: Each service must own its data and never share databases
3. **API-First Design**: Design APIs before implementing service logic
4. **Failure Handling**: Implement circuit breakers, retries, and graceful degradation
5. **Monitoring**: Include comprehensive logging, metrics, and health checks
6. **Security**: Implement authentication, authorization, and encryption at service level
7. **Testing**: Include unit, integration, contract, and end-to-end testing strategies
8. **Documentation**: Maintain up-to-date API documentation and service descriptions

#### Example Implementation

- Customer places order: Client → API Gateway → Order Service → publishes OrderCreated event → Payment Service processes payment → publishes PaymentProcessed event → Inventory Service updates stock → Notification Service sends confirmation
- Each service handles its part independently and communicates through events
- Failures in one service don't prevent others from continuing
- Services can be deployed, scaled, and updated independently

This architecture ensures applications remain scalable, resilient, and maintainable while supporting complex distributed business processes.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **Service Isolation**: Each service must be completely autonomous with its own data, logic, and deployment pipeline.

2. **API-First Development**: Define service APIs and contracts before implementing internal logic.

3. **Event-Driven Communication**: Use asynchronous messaging for service coordination to reduce coupling.

4. **Failure Resilience**: Implement circuit breakers, retries, timeouts, and graceful degradation in every service.

5. **Data Consistency**: Accept eventual consistency and implement saga patterns for distributed transactions.

6. **Independent Deployment**: Each service must be deployable independently without coordinating with other services.

7. **Monitoring and Observability**: Implement comprehensive logging, metrics, and distributed tracing from day one.

8. **Security by Design**: Implement authentication, authorization, and encryption at every service boundary.

**Code Review Checklist for AI Agents:**

- [ ] Service has single well-defined business responsibility
- [ ] Service owns its data store and doesn't access other services' databases
- [ ] All inter-service communication goes through APIs or events
- [ ] Circuit breakers and timeout handling implemented
- [ ] Health checks and metrics endpoints exposed
- [ ] API documentation is current and comprehensive
- [ ] Security measures implemented (auth, encryption, input validation)
- [ ] Service can be deployed and scaled independently

### Architectural Concepts

- **Service Decomposition**: Breaking monolithic applications into focused microservices based on business capabilities.
- **Distributed Data Management**: Each service manages its own data with eventual consistency across services.
- **Communication Patterns**: Synchronous (REST/gRPC) for immediate responses, asynchronous (messaging) for loose coupling.
- **Service Discovery**: Dynamic registration and discovery of service endpoints.
- **Circuit Breaker**: Preventing cascade failures by failing fast when downstream services are unavailable.
- **API Gateway**: Single entry point providing authentication, routing, and cross-cutting concerns.

### UI/UX Strategies

- **Backend for Frontend (BFF)**: Dedicated API gateways tailored for specific client types (web, mobile, desktop).
- **Micro-frontends**: Frontend architecture mirroring microservices with independently deployable UI components.
- **Progressive Web Apps**: Resilient UIs that work offline and handle service unavailability gracefully.
- **API Composition**: Aggregating data from multiple services to provide rich user experiences.
- **Caching Strategies**: Client-side and gateway-level caching to improve performance and reduce service load.

### Performance Strategies (Speed & Power)

- **Horizontal Scaling**: Scale individual services based on demand rather than scaling entire application.
- **Caching Layers**: Distributed caching (Redis, Memcached) and CDNs for static content.
- **Database Optimization**: Service-specific database choices optimized for their use cases.
- **Asynchronous Processing**: Non-blocking operations and event-driven workflows.
- **Load Balancing**: Distribute traffic across service instances with health-aware routing.

### Memory Optimization & Safety

- **Container Resource Limits**: Set appropriate memory and CPU limits for each service container.
- **Connection Pooling**: Manage database and HTTP connection pools to prevent resource exhaustion.
- **Garbage Collection**: Tune garbage collection settings for each service's memory patterns.
- **Memory Leak Detection**: Monitor memory usage patterns and implement alerting for leaks.

```yaml
# Example: Kubernetes resource limits
resources:
  limits:
    memory: "512Mi"
    cpu: "500m"
  requests:
    memory: "256Mi"
    cpu: "250m"
```

### Logging Strategies

- **Centralized Logging**: Aggregate logs from all services using ELK stack, Fluentd, or similar.
- **Structured Logging**: Use JSON format with consistent fields across all services.
- **Correlation IDs**: Track requests across service boundaries with unique correlation identifiers.
- **Log Levels**: Consistent log levels (DEBUG, INFO, WARN, ERROR) across all services.
- **Retention Policies**: Appropriate log retention based on compliance and debugging needs.

### Security Strategies

- **Zero Trust Architecture**: No implicit trust between services; verify every request.
- **Service-to-Service Authentication**: Mutual TLS, JWT tokens, or service mesh security.
- **API Gateway Security**: Authentication, authorization, rate limiting, and DDoS protection.
- **Secret Management**: Centralized secret storage (Vault, K8s secrets) with rotation policies.
- **Security Scanning**: Regular vulnerability scans of containers and dependencies.
- **Network Segmentation**: Isolate services using network policies and firewalls.

### Networking / API Strategies

- **API Versioning**: Semantic versioning with backward compatibility and deprecation policies.
- **Protocol Choice**: REST for CRUD operations, GraphQL for flexible queries, gRPC for high-performance communication.
- **Rate Limiting**: Protect services from overload with appropriate throttling mechanisms.
- **Content Negotiation**: Support multiple content types and compression formats.
- **CORS Handling**: Proper cross-origin resource sharing configuration for web clients.

### Service Communication Strategies

- **Synchronous Communication**: REST APIs, GraphQL, gRPC for real-time operations requiring immediate responses.
- **Asynchronous Communication**: Message queues, event streaming for eventual consistency and loose coupling.
- **Request-Response**: For operations that need immediate feedback and confirmation.
- **Publish-Subscribe**: For broadcasting events to multiple interested services.
- **Event Sourcing**: For maintaining complete audit trails and enabling event replay.

```python
# Example: Event-driven communication
@app.post("/orders")
async def create_order(order_data: OrderData):
    order = await order_service.create_order(order_data)
    
    # Publish event for other services
    await event_publisher.publish(
        "order.created",
        OrderCreatedEvent(
            order_id=order.id,
            customer_id=order.customer_id,
            amount=order.total_amount,
            timestamp=datetime.utcnow()
        )
    )
    return order
```

### Data Activities & ACID Strategies

- **Database Per Service**: Each service owns its data store, preventing direct database coupling.
- **Eventual Consistency**: Accept that data consistency across services happens eventually, not immediately.
- **Saga Pattern**: Manage distributed transactions using compensating actions for rollbacks.
- **Event Sourcing**: Store events rather than current state for auditability and replay capabilities.
- **CQRS**: Separate read and write models for better performance and scalability.

### Database Design & Optimizations

- **Polyglot Persistence**: Use the right database for each service's specific needs.
- **Data Partitioning**: Shard data across multiple database instances for scalability.
- **Read Replicas**: Use read replicas to distribute query load and improve performance.
- **Connection Management**: Implement connection pooling and circuit breakers for database access.

| Service Type | Database Choice | Reasoning |
|-------------|----------------|-----------|
| User Management | PostgreSQL | ACID compliance, relational data |
| Product Catalog | MongoDB | Flexible schema, document structure |
| Shopping Cart | Redis | High-performance caching, session storage |
| Analytics | ClickHouse | Time-series data, analytical queries |
| Search | Elasticsearch | Full-text search, complex queries |

### Source Control Strategies

- **Mono-repo vs Multi-repo**: Consider team structure, deployment dependencies, and shared code.
- **Service Versioning**: Semantic versioning for services with clear API compatibility rules.
- **Shared Libraries**: Common libraries for cross-cutting concerns (logging, metrics, security).
- **Dependency Management**: Clear policies for service dependencies and version compatibility.
- **Branch Protection**: Automated testing and review requirements before merging changes.

### CI/CD Strategies

- **Independent Pipelines**: Each service has its own CI/CD pipeline for independent deployment.
- **Container-First**: Build, test, and deploy services as containers for consistency.
- **Blue-Green Deployment**: Zero-downtime deployments with traffic switching.
- **Canary Releases**: Gradual rollouts to validate changes with real traffic.
- **Infrastructure as Code**: Terraform, CloudFormation, or Pulumi for reproducible infrastructure.
- **Service Mesh Integration**: Automatic sidecar injection and policy enforcement.

### Engineering Approach: Domain-Driven & Service-Oriented

- **Domain-Driven Design**: Use DDD to identify service boundaries based on business contexts and capabilities.
- **Service-First Thinking**: Design services around business capabilities rather than technical layers.
- **API Design First**: Define service contracts and APIs before implementing internal logic.
- **Evolutionary Architecture**: Design for change with versioning, backward compatibility, and graceful degradation.
- **Team Topology**: Align team structure with service ownership (Conway's Law).

### Testing Strategies

Comprehensive testing strategy for distributed systems with multiple autonomous services:

- **Unit Testing**: Test individual service components in isolation with mocked dependencies.
- **Integration Testing**: Test service interactions with real dependencies (databases, message queues).
- **Contract Testing**: Verify API contracts between services using tools like Pact.
- **End-to-End Testing**: Test complete user journeys across multiple services.
- **Performance Testing**: Load testing individual services and the entire system under realistic conditions.
- **Chaos Engineering**: Deliberately introduce failures to test system resilience and recovery.
- **Security Testing**: Penetration testing, vulnerability scanning, and compliance verification.

Test organization for microservices:
```
tests/
├─ unit/                # Service-level unit tests
├─ integration/         # Database and messaging integration tests
├─ contract/           # API contract tests (consumer and provider)
├─ e2e/               # Cross-service end-to-end tests
├─ performance/       # Load and stress testing
├─ chaos/            # Chaos engineering experiments
└─ security/         # Security and compliance tests
```

### Validation Domains & Best Combination

Validation strategy distributed across microservices architecture:

| Validation Domain | Implementation Location | Strategy |
|------------------|------------------------|----------|
| Input Validation | API Gateway + Service Entry Points | Validate and sanitize all external input |
| Business Rules | Individual Services | Each service validates its own business logic |
| Data Integrity | Service Data Layer | Database constraints and application-level checks |
| API Contracts | Service Boundaries | Contract testing and API schema validation |
| Cross-Service Consistency | Event Handlers | Validate event processing and saga compensation |
| Security | Multiple Layers | Authentication at gateway, authorization per service |

**Best Practices:**
- Validate at service boundaries to prevent invalid data propagation
- Use schema validation for API contracts and event messages
- Implement idempotency for message processing to handle duplicates
- Use correlation IDs to track validation failures across service calls
- Implement graceful degradation when validation services are unavailable
- Monitor validation failures and implement alerting for anomalous patterns