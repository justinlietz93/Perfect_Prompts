### Overview

This document defines a generic Three-Tier Architecture template focusing on architectural strategies:
- Clear separation of concerns between Presentation tier, Business Logic tier, and Data tier.
- Every project must be designed first conceptually from the Business-Layer-Out. Then ask:
      - "Given these business requirements, what data is needed, how should it be presented, and how do the tiers communicate?"
- Business-Out: Define business logic and requirements first, identify data needs, then design presentation.
- End-to-End: Consider full user journey from UI through business rules to data persistence.
- Ensure extended future scalability, stability + flexibility, maintainability via clear tier boundaries and well-defined interfaces.

### EXAMPLE ONLY Project Map of a Three-Tier application following the classic three-tier pattern in Python

```go
three-tier-app/
├─ pyproject.toml
├─ README.md
├─ presentation/                 # Presentation Tier
│  ├─ web/
│  │  ├─ app.py
│  │  ├─ templates/
│  │  │  ├─ base.html
│  │  │  ├─ home.html
│  │  │  ├─ users/
│  │  │  │  ├─ list.html
│  │  │  │  └─ detail.html
│  │  │  └─ products/
│  │  │     ├─ catalog.html
│  │  │     └─ detail.html
│  │  ├─ static/
│  │  │  ├─ css/
│  │  │  ├─ js/
│  │  │  └─ images/
│  │  ├─ forms/
│  │  │  ├─ user_form.py
│  │  │  └─ order_form.py
│  │  └─ blueprints/
│  │     ├─ user_blueprint.py
│  │     ├─ product_blueprint.py
│  │     └─ order_blueprint.py
│  ├─ api/
│  │  ├─ rest/
│  │  │  ├─ endpoints/
│  │  │  │  ├─ users.py
│  │  │  │  ├─ products.py
│  │  │  │  └─ orders.py
│  │  │  ├─ dto/
│  │  │  │  ├─ user_dto.py
│  │  │  │  ├─ product_dto.py
│  │  │  │  └─ order_dto.py
│  │  │  └─ validators/
│  │  │     ├─ request_validator.py
│  │  │     └─ response_validator.py
│  │  └─ graphql/
│  │     ├─ schema.py
│  │     └─ resolvers/
│  ├─ middleware/
│  │  ├─ auth_middleware.py
│  │  ├─ logging_middleware.py
│  │  └─ error_handler.py
│  └─ config/
│     ├─ routes.py
│     └─ settings.py
├─ business/                     # Business Logic Tier
│  ├─ services/
│  │  ├─ user_service.py
│  │  ├─ product_service.py
│  │  ├─ order_service.py
│  │  ├─ inventory_service.py
│  │  └─ payment_service.py
│  ├─ managers/
│  │  ├─ order_manager.py
│  │  ├─ cart_manager.py
│  │  └─ pricing_manager.py
│  ├─ workflows/
│  │  ├─ checkout_workflow.py
│  │  ├─ fulfillment_workflow.py
│  │  └─ return_workflow.py
│  ├─ rules/
│  │  ├─ pricing_rules.py
│  │  ├─ discount_rules.py
│  │  └─ validation_rules.py
│  ├─ interfaces/
│  │  ├─ service_interface.py
│  │  ├─ repository_interface.py
│  │  └─ external_service_interface.py
│  └─ dto/
│     ├─ business_dto.py
│     └─ internal_dto.py
├─ data/                         # Data Tier
│  ├─ models/
│  │  ├─ user.py
│  │  ├─ product.py
│  │  ├─ order.py
│  │  ├─ inventory.py
│  │  └─ base_model.py
│  ├─ repositories/
│  │  ├─ user_repository.py
│  │  ├─ product_repository.py
│  │  ├─ order_repository.py
│  │  └─ inventory_repository.py
│  ├─ database/
│  │  ├─ connection.py
│  │  ├─ session.py
│  │  ├─ migrations/
│  │  │  ├─ 001_init.sql
│  │  │  └─ 002_add_inventory.sql
│  │  └─ seed_data.py
│  ├─ cache/
│  │  ├─ redis_cache.py
│  │  └─ cache_manager.py
│  └─ external/
│     ├─ payment_gateway.py
│     ├─ shipping_api.py
│     └─ email_service.py
├─ shared/                       # Shared utilities
│  ├─ logging/
│  │  ├─ logger.py
│  │  └─ formatters.py
│  ├─ security/
│  │  ├─ encryption.py
│  │  ├─ authentication.py
│  │  └─ authorization.py
│  ├─ validation/
│  │  ├─ validators.py
│  │  └─ sanitizers.py
│  └─ exceptions/
│     ├─ business_exceptions.py
│     ├─ data_exceptions.py
│     └─ presentation_exceptions.py
├─ config/
│  ├─ app_config.py
│  ├─ database_config.py
│  └─ env/
│     ├─ development.py
│     ├─ production.py
│     └─ testing.py
├─ tests/
│  ├─ unit/
│  │  ├─ business/
│  │  ├─ data/
│  │  └─ presentation/
│  ├─ integration/
│  │  ├─ tier_integration/
│  │  └─ external_services/
│  └─ e2e/
│     ├─ user_scenarios/
│     └─ business_flows/
└─ docs/
   ├─ architecture_diagram.md
   ├─ api_documentation.md
   ├─ database_schema.md
   └─ deployment_guide.md
```

### Three-Tier Architecture Implementation

This section documents the Three-Tier Architecture approach, emphasizing clear separation between Presentation, Business Logic, and Data tiers.
This serves as a generic template for implementing enterprise applications with well-defined boundaries and scalable structure.

#### Core Principles

- **Tier Separation**: Each tier has distinct responsibilities - Presentation (UI/API), Business (logic/rules), Data (persistence).
- **Physical Separation**: Tiers can be deployed on separate servers/containers for scalability.
- **Interface-Based Communication**: Tiers communicate through well-defined interfaces, not direct dependencies.
- **Technology Independence**: Each tier can use different technologies appropriate to its purpose.
- **File Size Limit**: No source code file shall exceed 500 lines of code (LOC) to maintain readability.
- **Scope Boundaries**: Clear boundaries between tiers prevent coupling and enable independent evolution.
- **Scalability**: Each tier can scale independently based on its specific load characteristics.

#### Layer Structure

1. **Presentation Tier** (User Interface)
   - **Components**: Web UI, REST APIs, GraphQL endpoints, mobile apps, desktop clients
   - **Responsibilities**: User interaction, input validation, output formatting, session management
   - **Dependencies**: Only on Business tier interfaces via service contracts
   - **Rules**:
     - No direct database access or business logic
     - Thin layer that delegates to business tier
     - Handles HTTP/transport concerns (routing, authentication, content negotiation)
     - Transforms business objects to DTOs for external consumption
     - Client-side validation for UX, server-side validation for security

2. **Business Logic Tier** (Application Logic)
   - **Components**: Services, managers, workflows, business rules, domain logic
   - **Responsibilities**: Business rules enforcement, transaction coordination, workflow orchestration
   - **Dependencies**: On Data tier via repository interfaces, external service abstractions
   - **Rules**:
     - Framework-agnostic pure business logic
     - Coordinates operations across multiple data entities
     - Enforces business rules and constraints
     - Manages transactions and ensures data consistency
     - Stateless service design for scalability
     - Returns domain objects or result types, not HTTP responses

3. **Data Tier** (Data Access)
   - **Components**: Repositories, database connections, ORM models, external service adapters
   - **Responsibilities**: Data persistence, retrieval, caching, external system integration
   - **Dependencies**: Database drivers, external APIs, cache systems
   - **Rules**:
     - Implements repository interfaces from business tier
     - Handles all database operations (CRUD, queries, transactions)
     - Manages connections and connection pooling
     - Caching strategy for performance
     - External service integrations (payment, email, shipping)
     - Data validation at database level (constraints, triggers)

4. **Service Interfaces**
   - **Location**: Defined in business tier, implemented across tiers
   - **Purpose**: Enable loose coupling and testability
   - **Types**: 
     - Business Service Interface (business tier implements, presentation tier consumes)
     - Repository Interface (business tier defines, data tier implements)
     - External Service Interface (business tier defines, data tier implements adapters)

5. **Data Transfer Objects (DTOs)**
   - **Purpose**: Define contracts between tiers
   - **Types**:
     - API DTOs (presentation tier external contracts)
     - Business DTOs (internal business tier communication)
     - Data DTOs (data tier internal use)
   - **Rules**: Each tier's DTOs tailored to that tier's needs

6. **Configuration and Cross-Cutting**
   - **Config**: Centralized configuration in config/ directory
   - **Logging**: Structured logging across all tiers
   - **Security**: Authentication, authorization, encryption
   - **Monitoring**: Health checks, metrics, distributed tracing
   - **Error Handling**: Consistent error handling across tiers

#### Interfaces, Contracts, and API Requirements

- Tier communication contracts
  - Presentation → Business: Call business services via interfaces with DTOs
  - Business → Data: Call repositories via interfaces with domain models
  - Business → External: Call external services via adapter interfaces
  - All inter-tier calls MUST use interfaces, never concrete implementations

- Business service contracts
  - Services MUST expose interfaces for all public methods
  - Services MUST be stateless (no instance state between calls)
  - Services MUST return result objects indicating success/failure
  - Services MUST handle all business exceptions and convert to result objects
  - Services SHOULD coordinate transactions but delegate data access to repositories

- Repository contracts
  - Repositories MUST implement interfaces defined by business tier
  - Repositories MUST return domain models, not database entities directly
  - Repositories MUST handle all database exceptions
  - Repositories SHOULD use unit of work pattern for transactions
  - Repositories MUST NOT contain business logic

- API contracts (Presentation tier)
  - REST APIs MUST follow RESTful conventions (resources, HTTP methods, status codes)
  - APIs MUST version endpoints (/api/v1/) for backward compatibility
  - APIs MUST validate input and return standardized error responses
  - APIs MUST use DTOs for requests/responses, never expose internal models
  - APIs SHOULD support content negotiation (JSON, XML, etc.)

#### Dependency Flow

```
[Presentation Tier]
    ↓ calls via interface
[Business Logic Tier]
    ↓ calls via interface
[Data Tier]
    ↓
[Database / External Services]

Response flow:
[Database] → [Data Models]
    ↑
[Repository] → [Domain Objects]
    ↑
[Business Service] → [Business Results]
    ↑
[Presentation] → [DTOs / Views]
    ↑
[User]
```

**Key principles:**
- Presentation depends on Business interfaces only
- Business depends on Data interfaces only
- Data tier is self-contained with external dependencies
- Each tier isolated behind interfaces
- Physical deployment can separate tiers onto different servers

#### Integration Points

- **Web UI**: Browser-based interface calling business services
- **REST API**: External applications calling business services via HTTP
- **Mobile Apps**: Native mobile apps calling REST API
- **Background Jobs**: Scheduled tasks calling business services directly
- **Message Queue**: Async processing via message handlers calling business services
- **External Systems**: Payment gateways, shipping APIs, email services integrated at data tier

#### Rules for AI Agents

1. **Maintain Tier Boundaries**: Never bypass tiers. Presentation calls Business, Business calls Data. No shortcuts.
2. **Interface-Based Communication**: All inter-tier communication via interfaces, never concrete classes.
3. **Service Layer Design**: Business tier services orchestrate, don't implement low-level operations.
4. **Repository Pattern**: All data access through repositories implementing interfaces.
5. **Enforce 500 LOC Limit**: Break large services into smaller focused services.
6. **Stateless Services**: Business services must be stateless for scalability.
7. **DTO Usage**: Transform objects between tiers using appropriate DTOs.
8. **Transaction Management**: Coordinate transactions at business tier level.

#### Example Implementation

- User makes request → Presentation tier endpoint
- Endpoint validates input → Creates business DTO
- Endpoint calls Business Service interface
- Business Service validates business rules
- Business Service calls Repository interface
- Repository executes database operation
- Repository returns domain model
- Business Service processes result
- Business Service returns result to Presentation
- Presentation converts to API DTO
- Presentation returns response to user

This architecture ensures applications remain scalable, maintainable, and allow independent tier evolution.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **File Size Enforcement**: Never create or modify files exceeding 500 lines of code. Break large services into focused components.

2. **Tier Isolation**: Maintain strict tier boundaries. Presentation → Business → Data. No tier bypassing.

3. **Interface Definitions**: Define interfaces before implementations. Business tier defines what it needs, data tier implements.

4. **Layer Responsibilities**:
   - Presentation: UI/API concerns only (routing, formatting, validation)
   - Business: Business rules, workflows, transaction coordination
   - Data: Persistence, caching, external integrations

5. **Service Design**: Business services should be stateless orchestrators coordinating operations.

6. **Repository Pattern**: All database operations through repositories. Business tier never touches database directly.

7. **DTO Usage**: Each tier has its own DTOs. Transform between tiers appropriately.

8. **Physical Separation**: Design for tiers to be deployable separately (different servers/containers).

**Code Review Checklist for AI Agents:**

- [ ] File size ≤ 500 LOC
- [ ] No tier boundary violations
- [ ] All inter-tier calls use interfaces
- [ ] Business services are stateless
- [ ] No business logic in presentation or data tiers
- [ ] Repository pattern used consistently
- [ ] DTOs used for tier communication
- [ ] Transactions managed at business tier

### Architectural Concepts

- **Three-Tier Pattern**: Logical separation of Presentation, Business Logic, and Data tiers. Each tier handles specific concerns.
- **Physical vs Logical**: Tiers can be logically separated in same deployment or physically separated on different servers.
- **Scalability**: Scale each tier independently. Add more presentation servers for traffic, more business servers for processing, or scale data tier for storage.
- **Technology Independence**: Each tier can use different technology stack (e.g., React frontend, Java business tier, PostgreSQL data tier).
- **Deployment Flexibility**: Deploy as monolith or distribute across multiple servers/containers.

### UI/UX Strategies

- **Multiple Interfaces**: Support web UI, REST API, mobile apps all calling same business tier.
- **Responsive Design**: Presentation tier adapts to device (desktop, tablet, mobile).
- **API-First**: Design REST API first, then build UI on top of it.
- **Progressive Enhancement**: Core functionality works with basic HTML, JavaScript enhances experience.
- **Consistent Experience**: All presentation interfaces use same business tier ensuring consistent behavior.

### Performance Strategies (Speed & Power)

- **Tier Scalability**: Scale bottleneck tier independently (typically presentation or business tier).
- **Caching Strategy**: 
  - Presentation: Cache rendered pages, API responses
  - Business: Cache frequently used business objects
  - Data: Cache database query results
- **Connection Pooling**: Reuse database connections across requests.
- **Async Operations**: Long-running business operations executed asynchronously.
- **Load Balancing**: Distribute requests across multiple tier instances.
- **CDN**: Serve static assets from CDN for presentation tier.

### Memory Optimization & Safety

- **Stateless Services**: Business services stateless to prevent memory leaks from long-lived objects.
- **Connection Management**: Proper database connection pooling and cleanup.
- **Object Lifecycle**: Clear object lifecycle in each tier with appropriate cleanup.
- **Resource Limits**: Set memory limits per tier to prevent resource exhaustion.

### Logging Strategies

- **Tier-Specific Logging**: Each tier logs at appropriate level with tier context.
- **Request Tracing**: Correlation IDs track requests across all tiers.
- **Structured Logging**: JSON logs with tier, service, operation, and result.
- **Centralized Logs**: Aggregate logs from all tiers for analysis.
- **Performance Logging**: Log slow operations in each tier for optimization.

### Security Strategies

- **Authentication**: Handle at presentation tier, validate in business tier.
- **Authorization**: Enforce at business tier based on business rules.
- **Input Validation**: Validate at presentation tier, re-validate at business tier.
- **SQL Injection**: Use parameterized queries/ORM in data tier exclusively.
- **Encryption**: Encrypt sensitive data at rest (data tier) and in transit (between tiers).
- **Security Headers**: Set at presentation tier for web security.
- **Least Privilege**: Each tier has minimal permissions needed.

### Networking / API Strategies

- **RESTful Design**: Presentation tier exposes RESTful APIs for external consumption.
- **Service Communication**: Tiers communicate via HTTP/REST or RPC (gRPC) depending on deployment.
- **API Gateway**: Optional API gateway in front of presentation tier for routing, rate limiting.
- **Service Discovery**: In distributed deployment, use service discovery for tier location.
- **Circuit Breakers**: Protect against cascading failures between tiers.
- **Timeouts**: Set appropriate timeouts for inter-tier calls.

### Controller / Backend Logic Strategies

- **Thin Presentation**: Presentation tier handlers are thin, delegating to business tier.
- **Rich Business Tier**: Business tier contains all business logic, rules, workflows.
- **Service Orchestration**: Business services orchestrate multiple operations and repositories.
- **Transaction Boundaries**: Business tier defines transaction boundaries.
- **Error Transformation**: Convert data tier exceptions to business exceptions, then to presentation errors.

### Data Activities & ACID Strategies

- **Transaction Management**: Business tier coordinates transactions spanning multiple repositories.
- **Unit of Work**: Implement unit of work pattern at data tier for transaction management.
- **Consistency**: Enforce consistency at business tier before persisting.
- **Isolation Levels**: Configure appropriate isolation levels in data tier.
- **Distributed Transactions**: Use saga pattern for transactions spanning external services.

### Database Design & Optimizations

- **Normalized Schema**: Proper normalization (3NF) with appropriate denormalization for performance.
- **Indexing Strategy**: Index foreign keys and frequently queried columns.
- **Connection Pooling**: Efficient connection reuse in data tier.
- **Query Optimization**: Use EXPLAIN plans to optimize slow queries.
- **Read Replicas**: Scale read operations with database replicas.
- **Caching**: Cache frequently accessed data at data tier level.

### Source Control Strategies

- **Monorepo vs Multirepo**: Single repo with tier directories or separate repos per tier.
- **Feature Branches**: Branch per feature spanning multiple tiers.
- **Trunk-Based**: Frequent integration to main branch with feature flags.
- **Code Ownership**: Clear ownership per tier with required reviewers.
- **Semantic Versioning**: Version APIs and services independently.

### CI/CD Strategies

- **Tier-Specific Pipelines**: Each tier can have its own build/deploy pipeline.
- **Independent Deployment**: Deploy tiers independently when physically separated.
- **Database Migrations**: Automated migration execution as part of data tier deployment.
- **Blue-Green Deployment**: Deploy new version alongside old, switch after validation.
- **Canary Releases**: Gradually roll out changes tier by tier.
- **Smoke Tests**: Automated tests verifying tier integration after deployment.

### Engineering Approach: Business-Out & End-to-End

- **Business-Out**: Start with business requirements and workflows. Design business tier services and interfaces. Determine data needs and design repositories. Finally design presentation interfaces exposing business capabilities.
- **End-to-End**: Consider complete user journey. Design vertical slice through all tiers for each feature. Ensures all tiers work together for user scenarios.
- **Iteration**: Build walking skeleton through all tiers first (simplest feature). Iterate adding features vertically through tiers.

### Testing Strategies

Comprehensive testing at each tier plus integration testing between tiers. Coverage goal: 80%+ overall.

- **Unit Testing**: 
  - Presentation: Test handlers with mocked business services
  - Business: Test services with mocked repositories
  - Data: Test repositories with test database
- **Integration Testing**:
  - Presentation-Business: Test API endpoints calling real business services with mocked data tier
  - Business-Data: Test business services calling real repositories with test database
  - End-to-End: Test complete flow through all tiers
- **Contract Testing**: Verify interfaces between tiers match expectations
- **Performance Testing**: Load test each tier independently and together
- **Security Testing**: Test authentication, authorization, input validation at each tier

Testing best practices:
- Test each tier in isolation with mocked dependencies
- Integration tests verify tier communication
- E2E tests verify complete user scenarios
- Use test database for data tier testing
- Mock external services at data tier boundary

### Validation Domains & Best Combination

Multi-level validation provides defense in depth. Each tier validates from its perspective.

| Domain          | Description & Strategies                          | Best Practices & Integration |
|-----------------|---------------------------------------------------|------------------------------|
| Presentation Validation | Input validation at API/UI level. Format, required fields, basic business rules. | Client-side for UX, server-side authoritative. Return clear error messages. |
| Business Validation | Business rule enforcement. Complex validations spanning multiple entities. | Core validation layer. Enforce invariants. Authorization checks. |
| Data Validation | Data integrity at database level. Constraints, foreign keys, check constraints. | Last line of defense. Catches bugs in business logic. |
| Service Contracts | Validate DTOs at tier boundaries. Ensure contracts honored. | Schema validation for APIs. Type checking between tiers. |
| Security Validation | Authentication, authorization, input sanitization. | Multi-tier: Auth at presentation, authz at business, sanitization everywhere. |
| Integration Validation | Validate external service responses. Handle failures gracefully. | Circuit breakers. Fallback strategies. Retry logic. |

Overall Strategy: Validate at presentation for UX, business tier for rules, data tier for integrity. Each tier validates its inputs even from trusted tiers (defense in depth).
