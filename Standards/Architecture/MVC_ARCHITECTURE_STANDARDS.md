### Overview

This document defines a generic MVC (Model-View-Controller) architecture template focusing on architectural strategies:
- Clear separation of concerns between data (Model), presentation (View), and business logic (Controller).
- Every project must be designed first conceptually from the User-Interface-Down. Then ask:
      - "Given this user interaction, what data is needed, how should it be presented, and what controller logic orchestrates the flow?"
- UI-Down: Define user interactions and views first, identify required models, then implement controllers.
- Data-Up: Start with data models, build views to display them, connect with controllers.
- Ensure extended future scalability, stability + flexibility, maintainability via clear MVC separation and minimal coupling.

### EXAMPLE ONLY Project Map of an MVC application following the classic MVC pattern in Python

```go
mvc-app/
├─ pyproject.toml
├─ README.md
├─ src/
│  ├─ models/                    # data layer (Model)
│  │  ├─ user.py
│  │  ├─ product.py
│  │  ├─ order.py
│  │  ├─ base_model.py
│  │  └─ validators/
│  │     ├─ user_validator.py
│  │     └─ order_validator.py
│  ├─ views/                     # presentation layer (View)
│  │  ├─ templates/
│  │  │  ├─ layout.html
│  │  │  ├─ home.html
│  │  │  ├─ users/
│  │  │  │  ├─ list.html
│  │  │  │  ├─ detail.html
│  │  │  │  └─ form.html
│  │  │  ├─ products/
│  │  │  │  ├─ list.html
│  │  │  │  └─ detail.html
│  │  │  └─ orders/
│  │  │     ├─ list.html
│  │  │     └─ checkout.html
│  │  ├─ static/
│  │  │  ├─ css/
│  │  │  │  ├─ main.css
│  │  │  │  └─ components.css
│  │  │  ├─ js/
│  │  │  │  ├─ app.js
│  │  │  │  └─ validation.js
│  │  │  └─ images/
│  │  └─ helpers/
│  │     ├─ form_helpers.py
│  │     └─ template_filters.py
│  ├─ controllers/               # control layer (Controller)
│  │  ├─ base_controller.py
│  │  ├─ home_controller.py
│  │  ├─ user_controller.py
│  │  ├─ product_controller.py
│  │  ├─ order_controller.py
│  │  └─ auth_controller.py
│  ├─ services/                  # business logic services
│  │  ├─ user_service.py
│  │  ├─ product_service.py
│  │  ├─ order_service.py
│  │  └─ payment_service.py
│  ├─ database/                  # data access layer
│  │  ├─ connection.py
│  │  ├─ repositories/
│  │  │  ├─ user_repository.py
│  │  │  ├─ product_repository.py
│  │  │  └─ order_repository.py
│  │  ├─ migrations/
│  │  │  ├─ 001_initial.sql
│  │  │  └─ 002_add_orders.sql
│  │  └─ seed_data.py
│  ├─ middleware/
│  │  ├─ auth_middleware.py
│  │  ├─ logging_middleware.py
│  │  └─ error_middleware.py
│  ├─ utils/
│  │  ├─ logger.py
│  │  ├─ security.py
│  │  ├─ validation.py
│  │  └─ helpers.py
│  ├─ config/
│  │  ├─ settings.py
│  │  ├─ routes.py
│  │  └─ env/
│  │     ├─ development.py
│  │     ├─ production.py
│  │     └─ testing.py
│  └─ tests/
│     ├─ unit/
│     │  ├─ models/
│     │  ├─ controllers/
│     │  └─ services/
│     ├─ integration/
│     │  ├─ database/
│     │  └─ api/
│     └─ e2e/
│        ├─ user_flows/
│        └─ checkout_flow/
└─ docs/
   ├─ api_documentation.md
   ├─ model_schemas.md
   └─ deployment_guide.md
```

### MVC Architecture Implementation

This section documents the MVC (Model-View-Controller) Architecture approach, emphasizing clear separation between data models, user interface, and control logic.
This serves as a generic template for implementing web applications with clean separation of concerns and straightforward maintenance.

#### Core Principles

- **Separation of Concerns**: Models handle data, Views handle presentation, Controllers handle user input and orchestration.
- **Single Responsibility**: Each component has one clear purpose - Models for data integrity, Views for display, Controllers for flow.
- **Thin Controllers**: Controllers should orchestrate, not implement business logic (delegate to services).
- **Reusable Models**: Models represent data structures independent of presentation or control logic.
- **File Size Limit**: No source code file shall exceed 500 lines of code (LOC) to maintain readability and facilitate refactoring.
- **Directory Structure**: Organize by component type (models/, views/, controllers/) with subfolders for related functionality.
- **Naming Conventions**: Descriptive names that indicate purpose (UserController, ProductModel, OrderView).

#### Layer Structure

1. **Model Layer** (Data)
   - **Components**: Data models, validators, data access objects
   - **Responsibilities**: Data structure definition, validation rules, database interaction
   - **Dependencies**: Only on database libraries and validation utilities
   - **Rules**:
     - Models represent domain entities and their relationships
     - Validation logic belongs in model validators
     - No UI concerns or control flow logic
     - Use ORM or data access patterns for persistence
     - Models should be plain data classes with minimal behavior

2. **View Layer** (Presentation)
   - **Components**: Templates, static assets (CSS/JS), view helpers
   - **Responsibilities**: User interface rendering, data display formatting, user input collection
   - **Dependencies**: Only on view helpers and template engines
   - **Rules**:
     - Views should not contain business logic
     - Keep views simple with minimal conditional logic
     - Use template inheritance for consistency
     - Separate concerns with partial views/components
     - Static assets organized by type (css/, js/, images/)

3. **Controller Layer** (Control)
   - **Components**: Controllers, request handlers, routing configuration
   - **Responsibilities**: Request handling, user input processing, service orchestration, response building
   - **Dependencies**: Models, Services, and View selection
   - **Rules**:
     - Controllers are thin - delegate business logic to services
     - One controller per resource or feature area
     - Handle HTTP concerns (status codes, headers, redirects)
     - Input validation and error handling
     - Return appropriate views with necessary data

4. **Service Layer** (Business Logic)
   - **Components**: Business services, domain logic processors
   - **Responsibilities**: Complex business rules, transaction management, multi-model operations
   - **Dependencies**: Models and repositories
   - **Rules**:
     - Services encapsulate reusable business logic
     - Coordinate operations across multiple models
     - Handle transactions and ensure data consistency
     - Services are independent of HTTP/request context

5. **Data Access Layer**
   - **Components**: Repositories, database connection management, migrations
   - **Responsibilities**: CRUD operations, query execution, schema management
   - **Dependencies**: Models and database drivers
   - **Rules**:
     - Repositories abstract database operations
     - Use connection pooling for performance
     - Migrations for version-controlled schema changes
     - Repository pattern separates data access from business logic

6. **Configuration and Routing**
   - **Config**: All configurations must be in a centralized config/ folder at the root of the project.
   - **Routes**: Route definitions map URLs to controller actions, organized in routes.py or similar.
   - **Parameters**: Any static or default parameters kept in config directory.
   - **Environment**: Use environment-specific configs (development.py, production.py, testing.py).

7. **Middleware and Cross-Cutting Concerns**
   - **Middleware**: Authentication, logging, error handling, request/response modification.
   - **Utilities**: Shared helpers, security functions, logging infrastructure.
   - **Documentation**: Every method, function, class must have clear documentation.

#### Interfaces, Contracts, and API Requirements

- Request/Response flow
  - User request → Controller receives and validates input
  - Controller → Service processes business logic
  - Service → Model/Repository for data operations
  - Model → Database for persistence
  - Controller → View with processed data
  - View → Rendered response to user

- Controller contracts
  - Controllers MUST handle all HTTP concerns (status codes, headers, content negotiation)
  - Controllers MUST validate input before passing to services
  - Controllers MUST NOT contain business logic beyond basic validation and flow control
  - Controllers MUST handle errors gracefully and return appropriate responses

- Service contracts
  - Services MUST be framework-agnostic (no HTTP/request dependencies)
  - Services MUST return domain objects or result types, not HTTP responses
  - Services MUST handle transactions appropriately
  - Services SHOULD be reusable across different controllers or interfaces

- Model contracts
  - Models MUST define data structure and validation rules
  - Models MUST NOT depend on views or controllers
  - Models SHOULD be serializable for API responses
  - Model validation MUST occur before persistence

- View requirements
  - Views MUST receive all necessary data from controllers
  - Views MUST NOT query databases or call services directly
  - Views SHOULD use template inheritance for consistency
  - Views MUST properly escape user-generated content (XSS prevention)

#### Dependency Flow

```
User Request
    ↓
[Controller] ← handles HTTP, validates input
    ↓
[Service] ← executes business logic
    ↓
[Repository] ← data access abstraction
    ↓
[Model] ← data structure and validation
    ↓
[Database] ← persistence
    ↑
[Model] ← populated with data
    ↑
[Repository] ← returns domain objects
    ↑
[Service] ← processes results
    ↑
[Controller] ← prepares response
    ↓
[View] ← renders presentation
    ↓
Response to User
```

**Key principles:**
- Controllers depend on Services and Views
- Services depend on Repositories and Models
- Repositories depend on Models and Database
- Views depend only on data passed from Controllers
- Models have no dependencies on other layers

#### User Interaction Integration Points

- Controller actions map to user interactions (GET for display, POST for submissions)
- Forms in views collect user input
- Controllers validate and process form submissions
- Middleware handles cross-cutting concerns (authentication, logging)
- Error handlers provide user-friendly error pages
- Flash messages communicate operation results to users

#### Rules for AI Agents

1. **Maintain MVC Separation**: Models contain data and validation, Views contain presentation, Controllers orchestrate flow. Never mix concerns.
2. **Thin Controllers**: Controllers should be lightweight orchestrators, delegating business logic to services.
3. **Service Layer Usage**: Complex business logic belongs in services, not controllers or models.
4. **Enforce 500 LOC Limit**: Break large files into smaller, focused classes.
5. **Repository Pattern**: All database operations through repositories, never direct SQL in controllers.
6. **View Simplicity**: Keep views simple with minimal logic, use helpers for complex formatting.
7. **Input Validation**: Validate at controller level before passing to services.
8. **Error Handling**: Centralized error handling with user-friendly error pages.

#### Example Implementation

- User submits form → Controller validates input
- Controller → Service processes business logic
- Service → Repository to persist data
- Repository → Model with validation
- Model → Database via ORM
- Success → Controller redirects to success view
- Error → Controller returns form with error messages

This architecture ensures applications remain simple to understand, easy to maintain, and natural for web application development.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **File Size Enforcement**: Never create or modify files exceeding 500 lines of code. Break large controllers into multiple resource-specific controllers.

2. **MVC Separation**: Strictly maintain Model-View-Controller boundaries. Controllers orchestrate, Views render, Models manage data.

3. **Service Layer**: Extract complex business logic into services. Controllers should be thin adapters between HTTP and business logic.

4. **Layer Isolation**:
   - Controllers: HTTP handling, validation, orchestration only
   - Services: Business logic, transaction management
   - Models: Data structure, validation rules
   - Views: Presentation, templating only

5. **Repository Pattern**: All data access through repositories, never direct database calls from controllers or services.

6. **View Simplicity**: Keep templates simple with minimal logic. Use view helpers for complex formatting needs.

7. **Configuration Management**: All settings in config/ directory with environment-specific overrides.

8. **Naming Conventions**: UserController, ProductModel, order_list.html - clear, consistent naming.

**Code Review Checklist for AI Agents:**

- [ ] File size ≤ 500 LOC
- [ ] Controllers delegate to services for business logic
- [ ] Models contain only data and validation
- [ ] Views have no business logic or database calls
- [ ] Services are framework-agnostic
- [ ] Repository pattern used for data access
- [ ] Proper error handling and user feedback
- [ ] Input validation at controller level

### Architectural Concepts

- **MVC Pattern**: Separation of Model (data), View (presentation), Controller (logic flow). Each has distinct responsibility.
- **Request Flow**: HTTP Request → Router → Controller → Service → Repository → Model → Database. Response flows back through View.
- **Routing**: URL patterns map to controller actions. RESTful conventions (GET /users → index, POST /users → create).
- **Data Binding**: Automatic mapping of form data to models with validation.
- **Template Engines**: Server-side rendering with template inheritance and partials.

### UI/UX Strategies

- **Template Inheritance**: Base layouts with blocks for content sections. Consistent look across pages.
- **Form Helpers**: Reusable form components with built-in validation display.
- **Flash Messages**: Temporary messages for user feedback (success, errors, warnings).
- **Responsive Design**: Mobile-first approach with responsive CSS frameworks.
- **Accessibility**: Semantic HTML, ARIA labels, keyboard navigation.
- **Progressive Enhancement**: Core functionality works without JavaScript, enhancements layer on top.

### Performance Strategies (Speed & Power)

- **Database Optimization**: Query optimization, indexing, connection pooling. N+1 query prevention.
- **Caching**: Page caching, fragment caching, query result caching. Use Redis or Memcached.
- **Asset Pipeline**: CSS/JS minification and bundling. CDN for static assets.
- **Lazy Loading**: Load data only when needed. Pagination for large datasets.
- **Async Operations**: Background jobs for long-running tasks (email, reports).

### Memory Optimization & Safety

- **Connection Management**: Proper database connection pooling and cleanup.
- **Session Storage**: Use server-side sessions with appropriate expiration.
- **File Uploads**: Stream large files instead of loading into memory.
- **Resource Cleanup**: Ensure file handles, connections closed in finally blocks.

### Logging Strategies

- **Request Logging**: Log all incoming requests with timestamp, method, path, status.
- **Error Logging**: Detailed error logs with stack traces, separate from access logs.
- **Audit Logging**: Track data changes (who, what, when) for compliance.
- **Performance Logging**: Log slow queries and requests for optimization.
- **Structured Logging**: Use JSON format for easy parsing and analysis.

### Security Strategies

- **Authentication**: Session-based or token-based authentication with secure password storage.
- **Authorization**: Role-based access control (RBAC) at controller level.
- **Input Validation**: Validate and sanitize all user input to prevent injection attacks.
- **CSRF Protection**: Anti-CSRF tokens for all form submissions.
- **XSS Prevention**: Automatic output escaping in templates.
- **SQL Injection**: Use parameterized queries or ORM exclusively.
- **Security Headers**: Content-Security-Policy, X-Frame-Options, etc.

### Networking / API Strategies

- **RESTful Design**: Standard HTTP methods (GET, POST, PUT, DELETE) with appropriate status codes.
- **Content Negotiation**: Support multiple formats (HTML, JSON, XML) based on Accept header.
- **API Versioning**: Version APIs in URL path (/api/v1/) for backward compatibility.
- **Rate Limiting**: Protect against abuse with request throttling.
- **CORS**: Configure Cross-Origin Resource Sharing for API endpoints.

### Controller / Backend Logic Strategies

- **Thin Controllers**: Controllers orchestrate, services implement. Keep controllers under 150 LOC.
- **RESTful Actions**: Standard CRUD actions (index, show, create, update, delete).
- **Action Filters**: Before/after filters for common operations (authentication, logging).
- **Error Handling**: Centralized error handler with user-friendly error pages.
- **Response Building**: Consistent response format with status codes and messages.

### Data Activities & ACID Strategies

- **Transactions**: Wrap multi-step operations in database transactions.
- **Data Validation**: Multi-level validation (client-side, controller, model, database).
- **Referential Integrity**: Foreign key constraints at database level.
- **Optimistic Locking**: Version fields to handle concurrent updates.
- **Audit Trails**: Track data modifications with timestamps and user info.

### Database Design & Optimizations

- **Schema Design**: Normalized schema (3NF) with appropriate indexes.
- **Relationships**: One-to-many, many-to-many properly modeled with join tables.
- **Indexing**: Index foreign keys and frequently queried columns.
- **Migrations**: Version-controlled schema changes with rollback capability.
- **Query Optimization**: Use EXPLAIN to analyze and optimize slow queries.
- **Connection Pooling**: Reuse database connections for better performance.

### Source Control Strategies

- **Feature Branches**: Separate branch per feature or bug fix.
- **Commit Messages**: Clear, descriptive commit messages explaining why, not just what.
- **Code Reviews**: All changes reviewed before merging to main branch.
- **Semantic Versioning**: Version releases with major.minor.patch format.
- **Tag Releases**: Git tags for production releases.

### CI/CD Strategies

- **Automated Testing**: Run full test suite on every commit.
- **Build Pipeline**: Lint → Test → Build → Deploy stages.
- **Environment Parity**: Development, staging, production environments as similar as possible.
- **Database Migrations**: Automatic migration execution on deployment.
- **Rollback Plan**: Easy rollback to previous version if deployment fails.
- **Health Checks**: Automated health checks after deployment.

### Engineering Approach: UI-Down & Data-Up

- **UI-Down**: Start with user interface mockups and user stories. Identify data needs from UI requirements. Design models to support UI needs. Build controllers to connect UI and data.
- **Data-Up**: Start with data model design based on domain entities. Build repositories for data access. Create services for business logic. Design controllers to expose functionality. Build views to present data.
- **Iteration**: Prototype quickly, gather feedback, refine. Use scaffolding tools to generate boilerplate (models, controllers, views).

### Testing Strategies

Adopt comprehensive testing pyramid: Many unit tests (fast, isolated), moderate integration tests (component interaction), few end-to-end tests (full flow). Test coverage goal: 80%+.

- **Unit Testing**: Test models, services, and helper functions in isolation. Mock external dependencies.
- **Controller Testing**: Test controller actions with mocked services. Verify correct responses and status codes.
- **Integration Testing**: Test full request/response cycle including database. Use test database with fixtures.
- **View Testing**: Test template rendering with sample data. Verify correct HTML output.
- **End-to-End Testing**: Test complete user flows with browser automation (Selenium, Playwright).
- **Performance Testing**: Load testing to verify response times under load.
- **Security Testing**: Test authentication, authorization, input validation, XSS, CSRF.

Testing best practices:
- Use test fixtures for consistent test data
- Test happy paths and error cases
- Clear test names describing what is tested
- Arrange-Act-Assert pattern for clarity
- Run tests in isolation with proper setup/teardown

### Validation Domains & Best Combination

Validation at multiple layers provides defense in depth. Best combination: Client-side for immediate feedback, Controller for authoritative validation, Model for data integrity, Database for constraints.

| Domain          | Description & Strategies                          | Best Practices & Integration |
|-----------------|---------------------------------------------------|------------------------------|
| Client-side Validation | JavaScript validation for immediate user feedback. Basic checks (required, format, length). | Enhance UX but never rely solely on it. Combo with server validation. |
| Controller Validation | Authoritative validation of user input before processing. | Use validation libraries. Return errors to view with user-friendly messages. |
| Model Validation | Data integrity validation at model level. | Define validation rules on model attributes. Automatic validation before save. |
| Database Constraints | Database-level integrity (NOT NULL, UNIQUE, FK, CHECK). | Last line of defense. Catch logic errors in application. |
| Service Validation | Business rule validation in service layer. | Complex multi-model validation. Authorization checks. |
| Security Validation | Authentication, authorization, input sanitization. | CSRF tokens, XSS prevention, SQL injection prevention. |

Overall Strategy: Layer validation from UI to database. Fail fast at earliest appropriate layer. Provide clear, actionable error messages to users.
