### Overview

This document defines a generic full-stack app template focusing on hexagonal architectural strategies:
- ports and adapters pattern with domain-centric design isolating business logic from external concerns (databases, web frameworks, external services).
- Every project must be designed first conceptually from the Inside-out. Then ask:
      - "Given this core business domain, what ports (interfaces) and adapters (implementations) will be required to connect the domain to the external world?"
- Inside-out: Define core domain logic first, identify required ports, then implement adapters.
- Outside-in: Start with external requirements and work inward to the domain.
- Ensure extended future scalability, stability + flexibility, maintainability via hexagonal isolation, testable ports.

### EXAMPLE ONLY Project Map of a hexagonal architecture project following the Ports and Adapters pattern in Python

```go
hexagonal-app/
├─ pyproject.toml
├─ README.md
├─ src/
│  ├─ domain/                     # core business logic (center of hexagon)
│  │  ├─ models/
│  │  │  ├─ user.py
│  │  │  ├─ order.py
│  │  │  └─ product.py
│  │  ├─ services/
│  │  │  ├─ user_service.py
│  │  │  ├─ order_service.py
│  │  │  └─ inventory_service.py
│  │  ├─ exceptions/
│  │  │  ├─ domain_exceptions.py
│  │  │  └─ validation_errors.py
│  │  └─ value_objects/
│  │     ├─ email.py
│  │     ├─ money.py
│  │     └─ order_status.py
│  ├─ ports/                      # interfaces/contracts (hexagon edges)
│  │  ├─ driving/                 # primary ports (use cases)
│  │  │  ├─ user_management_port.py
│  │  │  ├─ order_processing_port.py
│  │  │  └─ inventory_port.py
│  │  └─ driven/                  # secondary ports (infrastructure)
│  │     ├─ user_repository_port.py
│  │     ├─ order_repository_port.py
│  │     ├─ email_service_port.py
│  │     ├─ payment_service_port.py
│  │     └─ notification_port.py
│  ├─ adapters/                   # implementations (outside hexagon)
│  │  ├─ driving/                 # primary adapters (controllers/interfaces)
│  │  │  ├─ web/
│  │  │  │  ├─ fastapi_adapter.py
│  │  │  │  ├─ flask_adapter.py
│  │  │  │  └─ dto/
│  │  │  │     ├─ user_dto.py
│  │  │  │     └─ order_dto.py
│  │  │  ├─ cli/
│  │  │  │  └─ command_adapter.py
│  │  │  └─ graphql/
│  │  │     └─ graphql_adapter.py
│  │  └─ driven/                  # secondary adapters (infrastructure)
│  │     ├─ persistence/
│  │     │  ├─ sqlalchemy_user_repository.py
│  │     │  ├─ mongodb_order_repository.py
│  │     │  └─ redis_cache_adapter.py
│  │     ├─ external_services/
│  │     │  ├─ stripe_payment_adapter.py
│  │     │  ├─ sendgrid_email_adapter.py
│  │     │  └─ twilio_sms_adapter.py
│  │     └─ messaging/
│  │        ├─ rabbitmq_adapter.py
│  │        └─ kafka_adapter.py
│  ├─ application/                # use case orchestration
│  │  ├─ use_cases/
│  │  │  ├─ create_user_use_case.py
│  │  │  ├─ process_order_use_case.py
│  │  │  └─ update_inventory_use_case.py
│  │  └─ handlers/
│  │     ├─ command_handlers.py
│  │     └─ query_handlers.py
│  ├─ shared/
│  │  ├─ logging/
│  │  ├─ security/
│  │  ├─ configuration/
│  │  └─ utilities/
│  ├─ config/
│  │  ├─ settings.py
│  │  ├─ dependency_injection.py
│  │  └─ env/
│  └─ tests/
│     ├─ unit/
│     │  ├─ domain/
│     │  ├─ ports/
│     │  └─ use_cases/
│     ├─ integration/
│     │  ├─ adapters/
│     │  └─ repositories/
│     └─ e2e/
│        ├─ web/
│        └─ cli/
└─ docs/
   ├─ ADRs/
   ├─ ports_and_adapters_diagram.md
   └─ hexagonal_design_decisions.md
```

### Hexagonal Architecture Implementation

This section documents the Hexagonal Architecture approach, also known as Ports and Adapters pattern. 
This serves as a generic template for implementing domain-centric, highly testable applications that isolate business logic from external concerns.

#### Core Principles

- **Domain-Centric Design**: Business logic resides in the center of the hexagon, completely isolated from external concerns.
- **Ports and Adapters**: Define contracts (ports) between the domain and external world, implement concrete adapters for specific technologies.
- **Dependency Inversion**: Domain depends only on abstractions (ports), never on concrete implementations (adapters).
- **Testability**: Domain logic can be tested in isolation using test doubles for ports.
- **Technology Agnostic**: Domain layer is completely independent of frameworks, databases, or external services.
- **Symmetric Architecture**: No distinction between "left side" (UI) and "right side" (data) - all external concerns are treated equally.

#### Layer Structure

1. **Domain Layer** (Center of Hexagon)
   - **Projects**: Core business models, domain services, value objects
   - **Responsibilities**: Pure business logic, domain rules, entities, value objects
   - **Dependencies**: None (completely isolated)
   - **Rules**:
     - No dependencies on external frameworks or libraries
     - Contains all business rules and invariants
     - Uses domain-specific language and concepts
     - Raises domain events for cross-boundary communication

2. **Ports Layer** (Hexagon Edges)
   - **Projects**: Interface definitions for all external interactions
   - **Responsibilities**: Define contracts between domain and external world
   - **Dependencies**: Only on domain types and shared abstractions
   - **Rules**:
     - Primary ports (driving): Use cases that external actors trigger
     - Secondary ports (driven): Dependencies that domain needs from external world
     - All ports are interfaces/abstract base classes
     - Port methods should be domain-focused, not technology-focused

3. **Application Layer** (Use Case Orchestration)
   - **Projects**: Use case implementations, command/query handlers
   - **Responsibilities**: Orchestrate domain objects to fulfill use cases
   - **Dependencies**: Domain layer and port interfaces
   - **Rules**:
     - Implements primary ports using domain services
     - Coordinates multiple domain objects for complex use cases
     - Handles transaction boundaries and cross-cutting concerns
     - No direct dependencies on adapters

4. **Adapters Layer** (Outside Hexagon)
   - **Projects**: Concrete implementations of ports for specific technologies
   - **Responsibilities**: Bridge between ports and external systems/frameworks
   - **Dependencies**: Port interfaces and external libraries/frameworks
   - **Rules**:
     - Primary adapters (driving): Controllers, CLI commands, message consumers
     - Secondary adapters (driven): Repository implementations, external service clients
     - Handle technology-specific concerns (serialization, protocols, etc.)
     - Translate between domain concepts and external system formats

5. **Configuration Layer** (Dependency Injection)
   - **Projects**: Wiring of ports to adapters, application startup
   - **Responsibilities**: Dependency injection, application bootstrapping
   - **Dependencies**: All layers for wiring purposes
   - **Rules**:
     - Only place where concrete adapter types are referenced
     - Configuration based on environment (dev, test, prod)
     - Handles adapter lifecycle and resource management

#### Interfaces, Contracts, and API Requirements

- **Port Design Principles**
  - All external interactions MUST go through well-defined ports (interfaces).
  - Ports MUST be designed from the domain perspective, not the technology perspective.
  - Primary ports represent use cases that external actors want to trigger.
  - Secondary ports represent capabilities that the domain needs from the external world.

- **Dependency Direction (strictly enforced)**
  - Domain → Nothing (completely isolated)
  - Application → Domain + Port interfaces
  - Adapters → Port interfaces + External libraries
  - Configuration → Everything (for wiring only)

- **Port Taxonomy (essential ports)**
  - **Use Case Ports**: Command and query interfaces for business operations
  - **Repository Ports**: Data persistence and retrieval interfaces
  - **Service Ports**: External service integration interfaces (payment, email, etc.)
  - **Event Ports**: Domain event publishing and subscription interfaces
  - **Notification Ports**: User notification interfaces (email, SMS, push)

- **Adapter Categories**
  - **Web Adapters**: REST API, GraphQL, WebSocket implementations
  - **CLI Adapters**: Command-line interface implementations
  - **Persistence Adapters**: Database, file system, cache implementations
  - **Messaging Adapters**: Message queue, event bus implementations
  - **External Service Adapters**: Third-party API client implementations

- **Error Handling Strategy**
  - Domain exceptions for business rule violations
  - Port-specific exceptions for adapter failures
  - Adapter responsibility to translate external errors to port exceptions
  - Application layer handles transaction rollback and error recovery

- **Testing Strategy**
  - Domain: Pure unit tests with no external dependencies
  - Ports: Contract tests that any adapter must satisfy
  - Adapters: Integration tests with real external systems
  - Application: Use case tests with mock adapters
  - End-to-end: Full system tests through primary adapters

#### Dependency Flow

```
[Primary Adapters] → [Application] → [Domain] ← [Secondary Adapters via Ports]
       ↓                ↓              ↓
[Web/CLI/GUI]     [Use Cases]    [Business Logic]    [DB/API/Message Queue]
```

- Arrows indicate allowed dependencies
- Domain is completely isolated in the center
- All external interactions go through ports
- Configuration layer wires adapters to ports at runtime

#### External Service Integration Points

- All external dependencies represented as secondary ports
- Adapters implement ports for specific technologies
- Easy to swap implementations without changing domain logic
- Mock implementations for testing and development
- Circuit breaker and retry logic in adapters, not domain

#### Rules for AI Agents

1. **Domain Isolation**: Keep domain layer completely free of external dependencies, frameworks, or libraries
2. **Port-First Design**: Define ports before implementing adapters
3. **Symmetric Treatment**: Treat all external concerns (UI, database, services) symmetrically through ports
4. **Adapter Responsibility**: Adapters handle all technology-specific concerns and translations
5. **Configuration Separation**: Only configuration/DI layer knows about concrete adapter types
6. **Test Independence**: Domain and application layers must be testable without any external systems
7. **Port Contracts**: All adapters for the same port must satisfy identical contract tests
8. **Error Translation**: Adapters must translate external errors to domain-appropriate exceptions

#### Example Implementation

- User registration use case: Web adapter receives HTTP request → calls application use case → orchestrates domain services → uses repository port → persistence adapter saves to database
- Domain service validates business rules using only domain objects
- Repository port defines domain-focused persistence interface
- Database adapter implements repository port for specific database technology
- Easy to switch from SQL to NoSQL by changing adapter configuration

This architecture ensures applications remain highly testable, technology-independent, and maintainable while clearly separating business logic from infrastructure concerns.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **Domain Purity**: Never add external dependencies to the domain layer. All external interactions must go through ports.

2. **Port-First Development**: Always define the port interface before implementing any adapter. Consider what the domain needs, not what the technology provides.

3. **Adapter Isolation**: Keep technology-specific code confined to adapters. Domain concepts should not leak into adapters, and technology concerns should not leak into domain.

4. **Symmetric Design**: Treat all external concerns equally - database, web framework, message queue, external API. No special treatment for any particular technology.

5. **Dependency Direction**: Domain depends on nothing. Application depends on domain and ports. Adapters depend on ports and external libraries. Configuration wires everything together.

6. **Contract Testing**: Every port must have contract tests that all implementations must pass. This ensures adapter substitutability.

7. **Error Boundaries**: Domain raises domain exceptions. Adapters catch external errors and translate to domain exceptions. Application layer handles cross-cutting error concerns.

8. **Test Strategy**: Domain tests need no external systems. Application tests use mock adapters. Integration tests verify adapter behavior with real external systems.

**Code Review Checklist for AI Agents:**

- [ ] Domain layer has zero external dependencies
- [ ] All external interactions go through defined ports
- [ ] Ports are designed from domain perspective, not technology perspective
- [ ] Adapters handle all technology-specific concerns
- [ ] Configuration layer is the only place that knows concrete adapter types
- [ ] Domain logic is testable in complete isolation
- [ ] Each port has contract tests that all adapters must satisfy
- [ ] Error handling follows domain → port → adapter translation pattern

### Architectural Concepts

- **Hexagonal Structure**: Business logic at center, surrounded by ports (interfaces), with adapters on the outside connecting to external systems.
- **Ports**: Primary ports (driving) for use cases, Secondary ports (driven) for infrastructure dependencies.
- **Adapters**: Primary adapters (controllers, CLI) initiate use cases, Secondary adapters (repositories, services) fulfill infrastructure needs.
- **Domain Isolation**: Core business logic completely independent of frameworks, databases, and external services.
- **Testability**: Each layer can be tested in isolation with appropriate test doubles.

### UI/UX Strategies

- **Adapter-Based UI**: Web, mobile, and desktop UIs are all primary adapters implementing the same use case ports.
- **Technology Independence**: UI frameworks can be swapped without changing business logic.
- **Consistent Experience**: Same use cases accessible through multiple UI adapters ensure consistent user experience.
- **API-First Design**: UI adapters consume the same APIs as external integrations, ensuring consistency.

### Performance Strategies (Speed & Power)

- **Caching Adapters**: Implement caching as secondary adapters for repository and service ports.
- **Async Adapters**: Use asynchronous implementations for I/O-bound operations in adapters.
- **Connection Pooling**: Handle connection management within adapter implementations.
- **Load Balancing**: Implement load balancing logic in adapter layer, transparent to domain.

### Memory Optimization & Safety

- **Resource Management**: Adapters responsible for managing external resource connections and cleanup.
- **Object Lifecycle**: Domain objects have clear lifecycle boundaries defined by use cases.
- **Memory Leaks**: Prevent leaks by proper resource disposal in adapter implementations.

```python
# Example: Repository adapter with proper resource management
class SqlUserRepository(UserRepositoryPort):
    def __init__(self, connection_factory):
        self._connection_factory = connection_factory
    
    def save(self, user: User) -> None:
        with self._connection_factory() as conn:
            # Database operations
            pass  # Connection automatically closed
```

### Logging Strategies

- **Adapter-Level Logging**: Log technology-specific operations (database queries, API calls) in adapters.
- **Use Case Logging**: Log business operations and decisions in application layer.
- **Domain Events**: Use domain events for business-significant logging rather than direct logging calls.
- **Correlation IDs**: Pass correlation IDs through port interfaces for distributed tracing.

### Security Strategies

- **Authentication Adapters**: Handle authentication mechanisms as primary adapters.
- **Authorization in Domain**: Business-level authorization rules belong in domain layer.
- **Security Ports**: Define security-related ports for encryption, token validation, etc.
- **Audit Logging**: Implement audit logging as a secondary adapter listening to domain events.

### Networking / API Strategies

- **Protocol Independence**: Same use cases accessible through REST, GraphQL, gRPC via different primary adapters.
- **API Versioning**: Handle versioning in adapter layer without changing domain logic.
- **Content Negotiation**: Adapters handle different content types and serialization formats.
- **Rate Limiting**: Implement rate limiting in primary adapters before reaching use cases.

### Controller / Backend Logic Strategies

- **Thin Controllers**: Controllers (primary adapters) should only handle HTTP concerns and delegate to use cases.
- **Use Case Orchestration**: Complex business flows orchestrated in application layer, not controllers.
- **DTO Mapping**: Controllers handle mapping between external DTOs and domain objects.
- **Error Handling**: Controllers catch domain exceptions and translate to appropriate HTTP responses.

```python
# Example: Web adapter (controller)
@app.post("/users")
async def create_user(user_dto: CreateUserDTO):
    try:
        command = CreateUserCommand(
            email=user_dto.email,
            name=user_dto.name
        )
        user_id = await user_service.create_user(command)
        return {"user_id": user_id}
    except DomainException as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### Data Activities & ACID Strategies

- **Transaction Boundaries**: Define transaction boundaries in application layer using Unit of Work pattern.
- **Repository Transactions**: Repository adapters implement transactional behavior specific to their storage technology.
- **Event Consistency**: Use domain events with outbox pattern for eventual consistency across boundaries.
- **Isolation Levels**: Configure appropriate isolation levels in repository adapter implementations.

### Database Design & Optimizations

- **Database Agnostic Domain**: Domain models independent of database schema design.
- **Adapter-Specific Optimization**: Database optimizations implemented in repository adapters.
- **Multiple Storage**: Different adapters can use different storage technologies for different aggregates.
- **Schema Evolution**: Database schema changes handled in adapter layer without affecting domain.

| Storage Type | Use Case | Adapter Implementation |
|-------------|----------|----------------------|
| Relational | Transactional data, complex queries | SQL repository adapter with ORM |
| Document | Flexible schema, nested data | NoSQL repository adapter |
| Key-Value | Caching, session storage | Redis/Memcached adapter |
| Event Store | Event sourcing, audit trail | Event store repository adapter |

### Source Control Strategies

- **Modular Structure**: Each hexagon layer in separate modules/packages for clear boundaries.
- **Port Versioning**: Semantic versioning for port interfaces to manage backward compatibility.
- **Adapter Independence**: Adapters can evolve independently as long as they implement port contracts.
- **Configuration Management**: Environment-specific adapter configurations in separate files.

### CI/CD Strategies

- **Layer Testing**: Separate test suites for domain, application, and adapter layers.
- **Contract Testing**: Automated verification that all adapters satisfy port contracts.
- **Integration Testing**: Test adapters against real external systems in staging environment.
- **Deployment Flexibility**: Deploy different adapter implementations to different environments.

### Engineering Approach: Inside-Out & Outside-In

- **Inside-Out**: Start with domain modeling, identify required ports, then implement adapters for specific technologies.
- **Outside-In**: Start with external requirements (API contracts, database schemas), define ports, then model domain.
- **Iterative Refinement**: Continuously refine port definitions based on domain needs and external constraints.
- **Technology Evaluation**: Easy to evaluate new technologies by implementing adapters without touching domain logic.

### Testing Strategies

Comprehensive testing strategy leveraging the natural testing boundaries of hexagonal architecture:

- **Domain Testing**: Pure unit tests for business logic with no external dependencies or mocks.
- **Port Contract Testing**: Automated tests that verify adapter implementations correctly fulfill port contracts.
- **Adapter Integration Testing**: Test adapters against real external systems to verify technology integration.
- **Use Case Testing**: Test application layer with mock adapters to verify use case orchestration.
- **End-to-End Testing**: Full system tests through primary adapters to verify complete workflows.
- **Property-Based Testing**: Use property-based testing for domain logic to verify business invariants.
- **Mutation Testing**: Verify test quality by ensuring domain logic changes break appropriate tests.

Test organization follows architecture layers:
```
tests/
├─ unit/domain/          # Pure domain logic tests
├─ contract/ports/       # Port contract verification tests
├─ integration/adapters/ # Adapter integration tests
├─ use_cases/           # Application layer orchestration tests
└─ e2e/                 # End-to-end system tests
```

### Validation Domains & Best Combination

Validation strategy aligned with hexagonal architecture boundaries:

| Validation Domain | Implementation Location | Strategy |
|------------------|------------------------|----------|
| Business Rules | Domain Layer | Domain services and entities enforce business invariants |
| Input Validation | Primary Adapters | Controllers validate and sanitize external input before use cases |
| Data Integrity | Secondary Adapters | Repository adapters ensure data consistency with storage systems |
| API Contracts | Port Interfaces | Contract tests verify adapters implement ports correctly |
| External Service | Adapter Implementations | Adapters validate external service responses and handle failures |
| Security | Cross-cutting through Ports | Authentication/authorization ports with adapter implementations |

**Best Practices:**
- Fail-fast validation at adapter boundaries before reaching domain
- Domain validation focuses on business rules, not data format
- Port contracts define validation expectations for all implementations
- Use types and interfaces to enforce compile-time validation where possible
- Separate validation concerns: format validation in adapters, business validation in domain