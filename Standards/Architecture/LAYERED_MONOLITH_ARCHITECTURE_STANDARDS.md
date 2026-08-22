### Overview

This document defines a generic Layered Monolith Architecture template focusing on architectural strategies:
- Simple layered structure with clear dependencies flowing downward through layers.
- Every project must be designed first conceptually from the Layer-by-Layer approach. Then ask:
      - "What responsibilities belong in each layer, and how do layers interact with clear boundaries?"
- Top-Down: Start from user-facing layer, work down through business logic to data layer.
- Bottom-Up: Build foundation data layer first, add business logic, then user interface.
- Ensure extended future scalability, stability + flexibility, maintainability via strict layer dependencies and minimal coupling.

### EXAMPLE ONLY Project Map of a Layered Monolith application following the layered architecture pattern in Python

```go
layered-monolith-app/
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ presentation/              # Layer 1: Presentation/UI Layer
│  │  ├─ web/
│  │  │  ├─ app.py
│  │  │  ├─ routes/
│  │  │  │  ├─ user_routes.py
│  │  │  │  ├─ product_routes.py
│  │  │  │  └─ order_routes.py
│  │  │  ├─ controllers/
│  │  │  │  ├─ user_controller.py
│  │  │  │  ├─ product_controller.py
│  │  │  │  └─ order_controller.py
│  │  │  ├─ templates/
│  │  │  │  ├─ layout.html
│  │  │  │  ├─ home.html
│  │  │  │  └─ users/
│  │  │  └─ static/
│  │  │     ├─ css/
│  │  │     ├─ js/
│  │  │     └─ images/
│  │  ├─ api/
│  │  │  ├─ rest_api.py
│  │  │  ├─ endpoints/
│  │  │  │  ├─ user_endpoints.py
│  │  │  │  ├─ product_endpoints.py
│  │  │  │  └─ order_endpoints.py
│  │  │  └─ schemas/
│  │  │     ├─ user_schema.py
│  │  │     └─ order_schema.py
│  │  └─ cli/
│  │     ├─ commands.py
│  │     └─ admin_commands.py
│  ├─ application/               # Layer 2: Application/Business Logic Layer
│  │  ├─ services/
│  │  │  ├─ user_service.py
│  │  │  ├─ product_service.py
│  │  │  ├─ order_service.py
│  │  │  ├─ inventory_service.py
│  │  │  └─ payment_service.py
│  │  ├─ use_cases/
│  │  │  ├─ create_order.py
│  │  │  ├─ process_payment.py
│  │  │  ├─ update_inventory.py
│  │  │  └─ fulfill_order.py
│  │  ├─ workflows/
│  │  │  ├─ checkout_workflow.py
│  │  │  └─ return_workflow.py
│  │  ├─ validators/
│  │  │  ├─ business_validators.py
│  │  │  ├─ order_validator.py
│  │  │  └─ payment_validator.py
│  │  └─ dto/
│  │     ├─ user_dto.py
│  │     ├─ order_dto.py
│  │     └─ product_dto.py
│  ├─ domain/                    # Layer 3: Domain/Model Layer
│  │  ├─ entities/
│  │  │  ├─ user.py
│  │  │  ├─ product.py
│  │  │  ├─ order.py
│  │  │  ├─ order_item.py
│  │  │  └─ inventory.py
│  │  ├─ value_objects/
│  │  │  ├─ address.py
│  │  │  ├─ money.py
│  │  │  ├─ email.py
│  │  │  └─ phone.py
│  │  ├─ enums/
│  │  │  ├─ order_status.py
│  │  │  ├─ payment_status.py
│  │  │  └─ user_role.py
│  │  └─ specifications/
│  │     ├─ order_specifications.py
│  │     └─ product_specifications.py
│  ├─ infrastructure/            # Layer 4: Infrastructure/Data Layer
│  │  ├─ persistence/
│  │  │  ├─ database/
│  │  │  │  ├─ connection.py
│  │  │  │  ├─ session.py
│  │  │  │  └─ unit_of_work.py
│  │  │  ├─ models/
│  │  │  │  ├─ user_model.py
│  │  │  │  ├─ product_model.py
│  │  │  │  └─ order_model.py
│  │  │  ├─ repositories/
│  │  │  │  ├─ user_repository.py
│  │  │  │  ├─ product_repository.py
│  │  │  │  ├─ order_repository.py
│  │  │  │  └─ base_repository.py
│  │  │  └─ migrations/
│  │  │     ├─ 001_create_users.sql
│  │  │     ├─ 002_create_products.sql
│  │  │     └─ 003_create_orders.sql
│  │  ├─ caching/
│  │  │  ├─ cache_manager.py
│  │  │  ├─ redis_cache.py
│  │  │  └─ memory_cache.py
│  │  ├─ messaging/
│  │  │  ├─ message_bus.py
│  │  │  ├─ event_publisher.py
│  │  │  └─ event_handlers/
│  │  ├─ external/
│  │  │  ├─ payment_gateway.py
│  │  │  ├─ email_service.py
│  │  │  ├─ sms_service.py
│  │  │  └─ shipping_api.py
│  │  └─ file_storage/
│  │     ├─ local_storage.py
│  │     └─ cloud_storage.py
│  ├─ shared/                    # Cross-cutting concerns
│  │  ├─ logging/
│  │  │  ├─ logger.py
│  │  │  └─ log_config.py
│  │  ├─ security/
│  │  │  ├─ authentication.py
│  │  │  ├─ authorization.py
│  │  │  ├─ encryption.py
│  │  │  └─ password_hasher.py
│  │  ├─ exceptions/
│  │  │  ├─ base_exception.py
│  │  │  ├─ business_exception.py
│  │  │  ├─ data_exception.py
│  │  │  └─ validation_exception.py
│  │  ├─ utilities/
│  │  │  ├─ date_utils.py
│  │  │  ├─ string_utils.py
│  │  │  └─ validation_utils.py
│  │  └─ constants/
│  │     ├─ error_codes.py
│  │     └─ system_constants.py
│  └─ config/
│     ├─ settings.py
│     ├─ database_config.py
│     ├─ cache_config.py
│     └─ env/
│        ├─ development.py
│        ├─ production.py
│        └─ testing.py
├─ tests/
│  ├─ unit/
│  │  ├─ application/
│  │  ├─ domain/
│  │  └─ infrastructure/
│  ├─ integration/
│  │  ├─ repositories/
│  │  ├─ services/
│  │  └─ external/
│  └─ e2e/
│     ├─ api_tests/
│     └─ web_tests/
├─ scripts/
│  ├─ migrate.py
│  ├─ seed_data.py
│  └─ deploy.sh
└─ docs/
   ├─ architecture.md
   ├─ layer_diagram.md
   ├─ api_docs.md
   └─ setup_guide.md
```

### Layered Monolith Architecture Implementation

This section documents the Layered Monolith Architecture approach, emphasizing simple layered structure with unidirectional dependencies.
This serves as a generic template for implementing straightforward, maintainable applications with clear layer boundaries.

#### Core Principles

- **Unidirectional Dependencies**: Dependencies flow downward only. Upper layers depend on lower layers, never the reverse.
- **Layer Separation**: Each layer has distinct responsibility and communicates only with adjacent layers.
- **Single Deployment**: All layers deployed together as one unit (monolith) for simplicity.
- **Clear Boundaries**: Layers separated by clear interfaces, enabling future extraction to services if needed.
- **File Size Limit**: No source code file shall exceed 500 lines of code (LOC) to maintain readability.
- **Progressive Complexity**: Simple projects use fewer layers, complex projects use all layers.
- **Testability**: Each layer testable in isolation by mocking dependencies from layer below.

#### Layer Structure

1. **Presentation Layer** (Top - Layer 1)
   - **Components**: Web UI, REST API, CLI, GraphQL endpoints
   - **Responsibilities**: User interaction, request handling, response formatting, input validation
   - **Dependencies**: Depends on Application layer only
   - **Rules**:
     - Handles all HTTP/transport concerns (routing, status codes, headers)
     - Converts between external DTOs and internal objects
     - No business logic - delegates to application layer
     - No database access - never skips to infrastructure layer
     - Thin controllers that orchestrate calls to application services

2. **Application Layer** (Layer 2)
   - **Components**: Services, use cases, workflows, application DTOs, validators
   - **Responsibilities**: Business logic orchestration, transaction coordination, business rules
   - **Dependencies**: Depends on Domain layer and Infrastructure interfaces
   - **Rules**:
     - Contains all business logic and business rules
     - Orchestrates domain entities and workflows
     - Manages transactions across repositories
     - Framework-agnostic (no web or database framework references)
     - Defines interfaces for infrastructure needs (repository interfaces)
     - Stateless services for scalability

3. **Domain Layer** (Layer 3)
   - **Components**: Entities, value objects, enums, domain events, specifications
   - **Responsibilities**: Core business concepts, domain models, domain logic
   - **Dependencies**: No dependencies on other layers (pure domain)
   - **Rules**:
     - Pure domain models without framework dependencies
     - Contains domain invariants and business rules intrinsic to entities
     - Value objects for immutable domain concepts
     - Domain events for important state changes
     - No persistence concerns (no database annotations)
     - Entities can have behavior (not anemic models)

4. **Infrastructure Layer** (Bottom - Layer 4)
   - **Components**: Repositories, database, caching, external services, file storage
   - **Responsibilities**: Data persistence, external integrations, technical implementations
   - **Dependencies**: Depends on Domain layer models, implements Application layer interfaces
   - **Rules**:
     - Implements repository interfaces defined in application layer
     - Handles all database operations (CRUD, queries, migrations)
     - Integrates with external services (payment, email, etc.)
     - Manages caching strategies
     - Connection pooling and resource management
     - Converts between domain models and persistence models

5. **Cross-Cutting Concerns** (Shared)
   - **Components**: Logging, security, exceptions, utilities, constants
   - **Purpose**: Functionality used by all layers
   - **Rules**:
     - No business logic - only technical utilities
     - Logging, encryption, validation helpers
     - Custom exceptions for different layer concerns
     - Configuration management

6. **Configuration**
   - **Location**: Centralized config/ directory
   - **Contents**: Application settings, database config, environment-specific configs
   - **Rules**: Environment variables for deployment-specific settings

#### Interfaces, Contracts, and API Requirements

- Layer communication rules
  - Presentation → Application: Calls application services, passes DTOs
  - Application → Domain: Works with domain entities and value objects
  - Application → Infrastructure: Calls through repository interfaces
  - Infrastructure → Domain: Returns domain entities from repositories
  - No layer skipping: Presentation cannot call Infrastructure directly
  - No upward dependencies: Infrastructure cannot depend on Application

- Application service contracts
  - Services expose clear interfaces for presentation layer
  - Services accept and return DTOs or domain objects
  - Services coordinate transactions
  - Services handle exceptions and convert to application-level errors

- Repository contracts
  - Repositories implement interfaces defined in application layer
  - Repositories accept and return domain entities
  - Repositories handle all database operations
  - Repositories convert between domain models and database models

- Presentation contracts
  - REST APIs follow RESTful conventions
  - Input validation at presentation layer
  - Error responses with appropriate HTTP status codes
  - API versioning for backward compatibility

#### Dependency Flow

```
┌─────────────────────────────────┐
│   Presentation Layer (Layer 1)  │ ← User Interface, API, CLI
│   - Controllers                  │
│   - Routes                       │
│   - API Endpoints                │
└────────────┬────────────────────┘
             │ depends on
             ↓
┌─────────────────────────────────┐
│   Application Layer (Layer 2)   │ ← Business Logic
│   - Services                     │
│   - Use Cases                    │
│   - Workflows                    │
└────────────┬────────────────────┘
             │ depends on
             ↓
┌─────────────────────────────────┐
│   Domain Layer (Layer 3)        │ ← Core Domain
│   - Entities                     │
│   - Value Objects                │
│   - Domain Events                │
└────────────┬────────────────────┘
             │ used by
             ↓
┌─────────────────────────────────┐
│   Infrastructure Layer (Layer 4)│ ← Technical Implementation
│   - Repositories (implements     │
│     interfaces from App layer)   │
│   - Database                     │
│   - External Services            │
└─────────────────────────────────┘
```

**Key principles:**
- Dependencies flow downward only
- Each layer depends only on layer immediately below
- Domain layer has no dependencies (pure)
- Infrastructure implements interfaces from application
- All layers can use shared utilities

#### Communication Patterns

- **Request Flow**: User Request → Presentation → Application Service → Repository → Database
- **Response Flow**: Database → Repository (domain entity) → Application Service (DTO) → Presentation (JSON/HTML) → User
- **Transaction Scope**: Managed at application layer, spans repository calls
- **Error Handling**: Each layer handles its errors, converts to appropriate type for layer above

#### Rules for AI Agents

1. **Maintain Downward Dependencies**: Upper layers depend on lower layers only. Never reverse dependencies.
2. **No Layer Skipping**: Presentation must call Application, cannot skip directly to Infrastructure.
3. **Interface-Based**: Application defines repository interfaces, Infrastructure implements them.
4. **Pure Domain**: Domain layer has no framework dependencies, no database annotations.
5. **Enforce 500 LOC Limit**: Break large files into smaller focused files.
6. **Service Orchestration**: Application services orchestrate, don't implement low-level operations.
7. **Repository Pattern**: All data access through repositories implementing interfaces.
8. **Thin Presentation**: Controllers are thin adapters, delegate to application services.

#### Example Implementation

- User submits order via API
- Presentation controller validates input, creates DTO
- Controller calls Application OrderService
- OrderService validates business rules using Domain entities
- OrderService calls Repository to save order
- Repository converts Domain entity to database model
- Repository persists to database
- Repository returns Domain entity to OrderService
- OrderService returns result DTO to Controller
- Controller returns JSON response to user

This architecture ensures applications remain simple, maintainable, and evolvable with clear responsibilities per layer.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **File Size Enforcement**: Never create or modify files exceeding 500 lines of code. Break into focused components.

2. **Dependency Direction**: Always maintain downward dependencies. Presentation → Application → Domain ← Infrastructure.

3. **Layer Isolation**: Each layer has specific responsibilities. Don't mix presentation logic in services or business logic in repositories.

4. **Interface Definitions**: Application layer defines repository interfaces. Infrastructure implements them.

5. **Pure Domain**: Domain entities have no database annotations, no framework dependencies.

6. **Service Design**: Application services coordinate operations across domain and infrastructure.

7. **No Layer Skipping**: Presentation calls Application, Application calls Infrastructure. No shortcuts.

8. **Monolith Deployment**: All layers deployed together, but maintain clear boundaries for future service extraction.

**Code Review Checklist for AI Agents:**

- [ ] File size ≤ 500 LOC
- [ ] Dependencies flow downward only
- [ ] No layer skipping (presentation to infrastructure)
- [ ] Domain layer has no external dependencies
- [ ] Application services are stateless
- [ ] Infrastructure implements application interfaces
- [ ] Clear separation of concerns per layer
- [ ] Proper error handling at each layer

### Architectural Concepts

- **Layered Architecture**: Horizontal layers with specific responsibilities. Dependencies flow downward.
- **Monolithic Deployment**: Single deployable unit containing all layers. Simpler deployment than microservices.
- **Clear Boundaries**: Well-defined layer boundaries enable future extraction to microservices if needed.
- **Progressive Complexity**: Start simple with basic layers, add complexity as needed.
- **Technology Stack**: Typically single technology stack (e.g., all Python or all Java) simplifies development.

### UI/UX Strategies

- **Multiple Frontends**: Web UI, REST API, CLI all at presentation layer calling same application services.
- **Consistent Behavior**: All interfaces use same application layer ensuring consistent business logic.
- **Template-Based**: Web UI uses server-side templates for rendering.
- **API-First Option**: Build REST API first, add web UI later using the API.
- **Responsive Design**: Frontend adapts to different devices.

### Performance Strategies (Speed & Power)

- **Caching**: Application-level caching for frequently accessed data. Infrastructure-level caching for database queries.
- **Connection Pooling**: Database connection pooling at infrastructure layer.
- **Lazy Loading**: Load related entities only when needed.
- **Eager Loading**: For known access patterns, load related data upfront to avoid N+1 queries.
- **Async Operations**: Background jobs for long-running tasks outside request cycle.
- **Query Optimization**: Optimize database queries at infrastructure layer.

### Memory Optimization & Safety

- **Stateless Services**: Application services stateless to avoid memory leaks.
- **Connection Management**: Proper connection lifecycle management in infrastructure.
- **Resource Cleanup**: Use context managers (Python) or try-finally for resource cleanup.
- **Bounded Collections**: Pagination for large result sets to limit memory usage.

### Logging Strategies

- **Layer-Specific Logging**: Each layer logs at appropriate detail level.
- **Structured Logging**: JSON logs with layer, operation, result.
- **Request Correlation**: Correlation ID tracks request through all layers.
- **Error Logging**: Full stack traces for errors with context.
- **Performance Logging**: Log slow operations for optimization.

### Security Strategies

- **Authentication**: Handle at presentation layer with middleware.
- **Authorization**: Enforce at application layer based on business rules.
- **Input Validation**: Multi-level - presentation for format, application for business rules.
- **SQL Injection**: Use ORM or parameterized queries exclusively at infrastructure layer.
- **Encryption**: Encrypt sensitive data at infrastructure layer before persistence.
- **Security Headers**: Set at presentation layer for web requests.

### Networking / API Strategies

- **RESTful APIs**: Standard REST conventions at presentation layer.
- **API Versioning**: Version endpoints for backward compatibility.
- **Content Negotiation**: Support JSON, XML based on Accept header.
- **Rate Limiting**: Implement at presentation layer to protect application.
- **CORS**: Configure for cross-origin requests at presentation layer.

### Controller / Backend Logic Strategies

- **Thin Controllers**: Presentation controllers are thin, delegate to application services.
- **Service Orchestration**: Application services orchestrate domain operations.
- **Transaction Management**: Application layer manages transaction boundaries.
- **Error Handling**: Convert exceptions to appropriate responses at presentation layer.

### Data Activities & ACID Strategies

- **Transactions**: Application layer defines transaction scope, infrastructure executes.
- **Unit of Work**: Implement unit of work pattern at infrastructure for transaction management.
- **Consistency**: Enforce at application layer before persisting via infrastructure.
- **Optimistic Locking**: Version fields on entities for concurrent update handling.

### Database Design & Optimizations

- **Normalized Schema**: Standard normalization (3NF) with selective denormalization.
- **Indexes**: Index foreign keys and frequently queried columns.
- **Migrations**: Version-controlled schema migrations in infrastructure layer.
- **Connection Pooling**: Efficient connection management at infrastructure layer.
- **Query Optimization**: Use EXPLAIN to optimize slow queries.

### Source Control Strategies

- **Single Repository**: Monolith in single repository with layer directories.
- **Feature Branches**: Branch per feature spanning multiple layers.
- **Clear Structure**: Directory structure reflects layer architecture.
- **Code Reviews**: Review changes across layers for boundary violations.

### CI/CD Strategies

- **Single Pipeline**: Build and deploy entire monolith as one unit.
- **Automated Tests**: Run tests for all layers in pipeline.
- **Database Migrations**: Run migrations automatically during deployment.
- **Blue-Green Deployment**: Deploy new version alongside old, switch after validation.
- **Rollback**: Easy rollback to previous version if issues arise.

### Engineering Approach: Layer-by-Layer & Vertical Slices

- **Layer-by-Layer**: Build complete layer before moving to next. Foundation up (infrastructure → domain → application → presentation).
- **Vertical Slices**: Build complete feature through all layers before next feature. Proves architecture early.
- **Iteration**: Start with walking skeleton (minimal feature through all layers), iterate adding features.

### Testing Strategies

Comprehensive testing at each layer plus integration across layers. Coverage goal: 80%+.

- **Unit Testing**:
  - Domain: Test entities and value objects in isolation
  - Application: Test services with mocked repositories
  - Infrastructure: Test repositories with test database
  - Presentation: Test controllers with mocked services
- **Integration Testing**:
  - Application-Infrastructure: Test services with real repositories and test database
  - Presentation-Application: Test API endpoints with real services
  - End-to-End: Test complete flows through all layers
- **Performance Testing**: Load test to identify bottlenecks
- **Security Testing**: Test authentication, authorization, input validation

Testing best practices:
- Test each layer in isolation with mocked dependencies
- Integration tests verify layer interaction
- Use test database for infrastructure tests
- Test transactions and error handling
- Clear test names describing scenario

### Validation Domains & Best Combination

Multi-layer validation provides defense in depth. Each layer validates from its perspective.

| Domain          | Description & Strategies                          | Best Practices & Integration |
|-----------------|---------------------------------------------------|------------------------------|
| Presentation Validation | Format validation, required fields, basic type checking | Client-side for UX, server-side authoritative. Return field-level errors. |
| Application Validation | Business rule validation, cross-field validation, authorization | Core validation layer. Enforce business invariants. |
| Domain Validation | Entity invariants, value object validation | Validate on construction. Throw domain exceptions. |
| Infrastructure Validation | Data integrity, constraints, referential integrity | Database constraints as last defense. |
| Security Validation | Authentication, authorization, sanitization | Multiple layers: auth at presentation, authz at application. |

Overall Strategy: Validate at presentation for UX, application for business rules, domain for invariants, infrastructure for integrity. Each layer assumes inputs are potentially invalid.
