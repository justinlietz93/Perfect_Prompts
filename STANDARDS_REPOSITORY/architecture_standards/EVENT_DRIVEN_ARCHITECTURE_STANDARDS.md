### Overview

This document defines a generic event-driven system template focusing on architectural strategies:
- event sourcing, CQRS, and reactive programming patterns with asynchronous communication through events and messages.
- Every project must be designed first conceptually from the Event-out. Then ask:
      - "Given this business process, what events occur, what state changes trigger events, what reactions are needed, and how should event flow be orchestrated?"
- Event-out: Define business events first, identify event producers and consumers, design event schemas and flows.
- Stream-processing: Design data and command flows as streams of events with transformation and aggregation.
- Ensure extended future scalability, eventual consistency + resilience, real-time responsiveness via event-driven reactions, loose coupling.

### EXAMPLE ONLY Project Map of an event-driven architecture project following reactive and event sourcing patterns

```go
event-driven-system/
├─ docker-compose.yml
├─ event-streaming/
│  ├─ kafka/
│  │  ├─ topics.yml
│  │  └─ schemas/
│  ├─ pulsar/
│  └─ nats/
├─ services/
│  ├─ command-service/
│  │  ├─ Dockerfile
│  │  ├─ pyproject.toml
│  │  ├─ src/
│  │  │  ├─ api/
│  │  │  │  ├─ controllers/
│  │  │  │  │  ├─ command_controller.py
│  │  │  │  │  └─ health_controller.py
│  │  │  │  └─ dto/
│  │  │  │     ├─ command_dto.py
│  │  │  │     └─ response_dto.py
│  │  │  ├─ domain/
│  │  │  │  ├─ aggregates/
│  │  │  │  │  ├─ user_aggregate.py
│  │  │  │  │  └─ order_aggregate.py
│  │  │  │  ├─ commands/
│  │  │  │  │  ├─ create_user_command.py
│  │  │  │  │  └─ place_order_command.py
│  │  │  │  ├─ events/
│  │  │  │  │  ├─ user_created_event.py
│  │  │  │  │  └─ order_placed_event.py
│  │  │  │  └─ value_objects/
│  │  │  ├─ application/
│  │  │  │  ├─ command_handlers/
│  │  │  │  │  ├─ user_command_handler.py
│  │  │  │  │  └─ order_command_handler.py
│  │  │  │  └─ services/
│  │  │  │     └─ command_bus.py
│  │  │  ├─ infrastructure/
│  │  │  │  ├─ event_store/
│  │  │  │  │  ├─ event_store_repository.py
│  │  │  │  │  └─ event_serializer.py
│  │  │  │  ├─ messaging/
│  │  │  │  │  ├─ kafka_event_publisher.py
│  │  │  │  │  └─ event_dispatcher.py
│  │  │  │  └─ persistence/
│  │  │  │     └─ aggregate_repository.py
│  │  │  └─ config/
│  │  └─ tests/
│  ├─ query-service/
│  │  ├─ Dockerfile
│  │  ├─ package.json
│  │  ├─ src/
│  │  │  ├─ api/
│  │  │  │  ├─ controllers/
│  │  │  │  │  ├─ query-controller.js
│  │  │  │  │  └─ projection-controller.js
│  │  │  │  └─ middleware/
│  │  │  ├─ projections/
│  │  │  │  ├─ user-projection.js
│  │  │  │  ├─ order-projection.js
│  │  │  │  └─ analytics-projection.js
│  │  │  ├─ event-handlers/
│  │  │  │  ├─ user-event-handler.js
│  │  │  │  └─ order-event-handler.js
│  │  │  ├─ repositories/
│  │  │  │  ├─ read-model-repository.js
│  │  │  │  └─ projection-repository.js
│  │  │  ├─ infrastructure/
│  │  │  │  ├─ messaging/
│  │  │  │  │  ├─ kafka-consumer.js
│  │  │  │  │  └─ event-processor.js
│  │  │  │  └─ database/
│  │  │  │     ├─ mongodb-connection.js
│  │  │  │     └─ elasticsearch-client.js
│  │  │  └─ config/
│  │  └─ tests/
│  ├─ notification-service/
│  │  ├─ Dockerfile
│  │  ├─ go.mod
│  │  ├─ cmd/
│  │  │  └─ main.go
│  │  ├─ internal/
│  │  │  ├─ handlers/
│  │  │  │  ├─ event-handler.go
│  │  │  │  └─ notification-handler.go
│  │  │  ├─ services/
│  │  │  │  ├─ email-service.go
│  │  │  │  ├─ sms-service.go
│  │  │  │  └─ push-service.go
│  │  │  ├─ models/
│  │  │  │  ├─ notification.go
│  │  │  │  └─ template.go
│  │  │  ├─ messaging/
│  │  │  │  ├─ kafka-consumer.go
│  │  │  │  └─ event-processor.go
│  │  │  └─ config/
│  │  └─ tests/
│  └─ analytics-service/
│     ├─ Dockerfile
│     ├─ Cargo.toml
│     ├─ src/
│     │  ├─ main.rs
│     │  ├─ handlers/
│     │  │  ├─ event_handler.rs
│     │  │  └─ analytics_handler.rs
│     │  ├─ processors/
│     │  │  ├─ stream_processor.rs
│     │  │  ├─ aggregator.rs
│     │  │  └─ window_functions.rs
│     │  ├─ models/
│     │  │  ├─ metrics.rs
│     │  │  └─ aggregates.rs
│     │  ├─ infrastructure/
│     │  │  ├─ messaging/
│     │  │  │  └─ kafka_streams.rs
│     │  │  └─ storage/
│     │  │     ├─ timeseries_db.rs
│     │  │     └─ cache.rs
│     │  └─ config/
│     └─ tests/
├─ event-schemas/
│  ├─ avro/
│  │  ├─ user-events.avsc
│  │  ├─ order-events.avsc
│  │  └─ payment-events.avsc
│  ├─ protobuf/
│  │  ├─ user_events.proto
│  │  └─ order_events.proto
│  └─ json-schema/
│     ├─ user-events.json
│     └─ order-events.json
├─ stream-processing/
│  ├─ kafka-streams/
│  │  ├─ user-stream-processor/
│  │  ├─ order-stream-processor/
│  │  └─ analytics-aggregator/
│  ├─ flink/
│  │  ├─ real-time-analytics/
│  │  └─ fraud-detection/
│  └─ storm/
│     └─ event-enrichment/
├─ event-store/
│  ├─ eventstoredb/
│  ├─ postgresql-events/
│  └─ cassandra-events/
├─ monitoring/
│  ├─ grafana/
│  │  ├─ dashboards/
│  │  │  ├─ event-metrics.json
│  │  │  ├─ stream-processing.json
│  │  │  └─ system-health.json
│  │  └─ alerts/
│  ├─ prometheus/
│  │  ├─ rules/
│  │  └─ targets/
│  └─ jaeger/
│     └─ config/
└─ docs/
   ├─ event-catalog/
   │  ├─ events/
   │  │  ├─ user-created.md
   │  │  └─ order-placed.md
   │  ├─ services/
   │  └─ flows/
   ├─ architecture/
   │  ├─ event-flows.md
   │  ├─ cqrs-design.md
   │  └─ streaming-topology.md
   └─ runbooks/
      ├─ event-replay.md
      ├─ stream-recovery.md
      └─ monitoring.md
```

### Event-Driven Architecture Implementation

This section documents the Event-Driven Architecture approach, emphasizing asynchronous communication, event sourcing, CQRS, and reactive programming patterns.
This serves as a generic template for implementing scalable, responsive, and resilient event-driven applications.

#### Core Principles

- **Event-First Design**: Business processes modeled as sequences of events with clear causality chains.
- **Eventual Consistency**: Accept that different parts of the system will reach consistency asynchronously.
- **Reactive Programming**: Systems react to events as they occur, enabling real-time responsiveness.
- **Immutable Events**: Events are immutable facts that represent something that happened in the past.
- **Event Sourcing**: Store events as the primary source of truth, derive current state from event history.
- **CQRS**: Separate command (write) and query (read) models for optimal performance and scalability.
- **Loose Coupling**: Components communicate through events without direct dependencies.

#### Architecture Structure

1. **Event Store** (Source of Truth)
   - **Components**: Event persistence, event streams, snapshots, event replay
   - **Responsibilities**: Durable event storage, ordering guarantees, event history
   - **Dependencies**: Persistence layer (database, distributed log)
   - **Rules**:
     - Events are append-only and immutable
     - Strong consistency within aggregate boundaries
     - Event ordering preserved within streams
     - Support for event replay and time-travel debugging

2. **Command Side** (Write Operations)
   - **Components**: Command handlers, aggregates, domain services, event publishers
   - **Responsibilities**: Process commands, enforce business rules, generate events
   - **Dependencies**: Event store, domain models
   - **Rules**:
     - Commands may succeed or fail (not idempotent)
     - Aggregate consistency boundaries
     - Business logic validation before event generation
     - Optimistic concurrency control for aggregates

3. **Query Side** (Read Operations)
   - **Components**: Event handlers, projections, read models, query handlers
   - **Responsibilities**: Build read-optimized views from events, handle queries
   - **Dependencies**: Event streams, read databases
   - **Rules**:
     - Eventually consistent with command side
     - Multiple projections for different query needs
     - Denormalized data for query performance
     - Idempotent event processing

4. **Event Streaming Platform** (Event Transportation)
   - **Components**: Message brokers, event routing, stream processing, dead letter queues
   - **Responsibilities**: Event distribution, ordering, durability, scalability
   - **Dependencies**: Messaging infrastructure (Kafka, Pulsar, EventStore)
   - **Rules**:
     - At-least-once delivery guarantees
     - Event partitioning for parallelism
     - Schema evolution and compatibility
     - Poison message handling

5. **Stream Processing** (Real-time Analytics)
   - **Components**: Stream processors, aggregators, windowing functions, complex event processing
   - **Responsibilities**: Real-time event analysis, pattern detection, aggregations
   - **Dependencies**: Event streams, state stores
   - **Rules**:
     - Stateful and stateless processing
     - Time-based and count-based windows
     - Exactly-once processing semantics where required
     - Fault tolerance and state recovery

6. **Saga Orchestration** (Distributed Transactions)
   - **Components**: Saga managers, compensation handlers, state machines
   - **Responsibilities**: Coordinate long-running business processes across boundaries
   - **Dependencies**: Event streams, saga state store
   - **Rules**:
     - Choreography or orchestration patterns
     - Compensation actions for rollback scenarios
     - Timeout handling and retry policies
     - Idempotent saga steps

#### Interfaces, Contracts, and API Requirements

- **Event Schema Management**
  - All events MUST have well-defined schemas with versioning support.
  - Schema evolution MUST maintain backward and forward compatibility.
  - Event schemas MUST be registered in a schema registry.
  - Breaking changes require new event versions with migration strategies.

- **Event Contracts**
  - **Event Structure**: Event ID, timestamp, event type, version, payload, metadata
  - **Ordering Guarantees**: Events within an aggregate stream maintain order
  - **Delivery Semantics**: At-least-once delivery with idempotent processing
  - **Retention Policies**: Event retention based on business and compliance requirements

- **Command Contracts**
  - Commands represent intent to change system state
  - Commands are not durable and may be rejected
  - Command validation occurs before event generation
  - Command results communicated through events or responses

- **Query Contracts**
  - Read models optimized for specific query patterns
  - Eventually consistent with event store
  - Multiple projections for different use cases
  - Query responses include freshness indicators

- **Integration Patterns**
  - **Event Notification**: Lightweight events for loose coupling
  - **Event-Carried State Transfer**: Events contain full state changes
  - **Event Sourcing**: Events as primary source of truth
  - **CQRS**: Separate command and query responsibilities

#### Dependency Flow

```
[Commands] → [Aggregates] → [Events] → [Event Store]
                              ↓
[Event Streams] → [Event Handlers] → [Projections] → [Read Models]
                              ↓
[Stream Processing] → [Real-time Analytics] → [Metrics/Alerts]
                              ↓
[Saga Orchestration] → [Compensation] → [Long-running Processes]
```

- Events flow from command processing through various consumption patterns
- Each consumer processes events independently and asynchronously
- Stream processing enables real-time analytics and complex event processing
- Saga patterns coordinate distributed business processes

#### Event Integration Points

- **Event Publishing**: Domain aggregates publish events to event store/streams
- **Event Subscription**: Services subscribe to relevant event types/streams
- **Stream Processing**: Real-time processing and transformation of event streams
- **External Integration**: Events bridge internal and external systems
- **Event Replay**: Ability to replay events for recovery or new projections

#### Rules for AI Agents

1. **Event Immutability**: Never modify events after they are stored; create new events for corrections
2. **Aggregate Boundaries**: Keep event consistency within aggregate boundaries only
3. **Idempotent Processing**: Design event handlers to be idempotent and handle duplicates
4. **Event Versioning**: Plan for event schema evolution from the beginning
5. **Error Handling**: Implement dead letter queues and compensation patterns
6. **Monitoring**: Track event processing latency, throughput, and failure rates
7. **Schema Registry**: Use centralized schema management for event definitions
8. **Testing**: Test event flows, projections, and eventual consistency scenarios

#### Example Implementation

- User registration flow: RegisterUser command → User aggregate validates → UserCreated event → stored in event store → multiple projections updated (user profile, authentication, analytics) → notification service sends welcome email
- Each component processes events asynchronously and independently
- System remains responsive even if individual components fail
- New projections can be built by replaying historical events

This architecture ensures applications remain scalable, responsive, and resilient while supporting complex event-driven business processes.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **Event Immutability**: Treat events as immutable historical facts; never change events after creation.

2. **Idempotent Processing**: Design all event handlers to be idempotent and safely handle duplicate events.

3. **Schema Evolution**: Plan for event schema changes from day one with backward/forward compatibility.

4. **Aggregate Consistency**: Maintain strong consistency only within aggregate boundaries, accept eventual consistency across aggregates.

5. **Error Recovery**: Implement robust error handling with dead letter queues, retry policies, and compensation actions.

6. **Event Ordering**: Preserve ordering within event streams while allowing parallel processing across streams.

7. **Monitoring and Observability**: Track event processing metrics, lag, and system health continuously.

8. **Testing Strategy**: Test event flows, projection rebuilding, and system behavior under failure conditions.

**Code Review Checklist for AI Agents:**

- [ ] Events are immutable and contain all necessary context
- [ ] Event handlers are idempotent and handle duplicates gracefully
- [ ] Event schemas are versioned and registered in schema registry
- [ ] Aggregate boundaries respect consistency requirements
- [ ] Dead letter queues configured for poison message handling
- [ ] Event ordering preserved where business requires it
- [ ] Monitoring and alerting configured for event processing
- [ ] Error scenarios tested including network partitions and service failures

### Architectural Concepts

- **Event Sourcing**: Store events as the primary source of truth, derive current state through event replay.
- **CQRS**: Command Query Responsibility Segregation - separate write and read models for optimal performance.
- **Event Streaming**: Continuous flow of events through the system enabling real-time processing.
- **Saga Pattern**: Long-running business processes coordinated through events with compensation actions.
- **Event Store**: Specialized database optimized for storing and querying event streams.
- **Projections**: Read-optimized views built by processing event streams.

### UI/UX Strategies

- **Real-time Updates**: WebSocket connections or Server-Sent Events for live UI updates based on events.
- **Optimistic UI**: Update UI immediately on command, handle eventual consistency gracefully.
- **Event-driven Notifications**: Push notifications triggered by domain events for user engagement.
- **Progressive Enhancement**: Degrade gracefully when event processing is delayed or unavailable.
- **Temporal UI**: Show event timelines and audit trails for transparency and debugging.

### Performance Strategies (Speed & Power)

- **Event Partitioning**: Distribute events across partitions for parallel processing and scalability.
- **Stream Processing**: Real-time event processing with low-latency stream processing frameworks.
- **Projection Optimization**: Multiple specialized projections optimized for different query patterns.
- **Caching**: Cache frequently accessed projections and aggregates for improved read performance.
- **Batch Processing**: Batch event processing for high-throughput scenarios where latency is acceptable.

### Memory Optimization & Safety

- **Event Snapshots**: Periodic snapshots of aggregate state to avoid replaying entire event history.
- **Event Compaction**: Remove obsolete events while preserving business-critical audit trail.
- **Streaming Buffers**: Appropriate buffer sizes for stream processing to balance memory usage and throughput.
- **Resource Monitoring**: Monitor memory usage patterns in stream processors and event handlers.

```python
# Example: Aggregate with snapshotting
class UserAggregate:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.version = 0
        self.events = []
    
    @classmethod
    def from_snapshot(cls, snapshot: dict, events_since_snapshot: List[Event]):
        # Restore from snapshot and apply subsequent events
        aggregate = cls(snapshot['user_id'])
        aggregate.version = snapshot['version']
        # Apply remaining events
        for event in events_since_snapshot:
            aggregate.apply_event(event)
        return aggregate
    
    def create_snapshot(self) -> dict:
        return {
            'user_id': self.user_id,
            'version': self.version,
            'state': self.get_current_state()
        }
```

### Logging Strategies

- **Event Audit Trail**: Complete audit trail naturally provided by event store.
- **Correlation Tracking**: Track events and commands through system with correlation IDs.
- **Processing Metrics**: Log event processing times, throughput, and error rates.
- **Business Event Logging**: Log significant business events for analytics and monitoring.
- **Debug Event Logging**: Detailed logging for event processing debugging and troubleshooting.

### Security Strategies

- **Event Encryption**: Encrypt sensitive event data at rest and in transit.
- **Access Control**: Fine-grained access control for event streams and projections.
- **Event Signing**: Digital signatures for event integrity and non-repudiation.
- **Privacy Compliance**: GDPR compliance through event anonymization and right to be forgotten.
- **Audit Security**: Immutable audit trail for compliance and security investigations.

### Networking / Event Distribution Strategies

- **Message Brokers**: Reliable event distribution through Kafka, RabbitMQ, or cloud messaging services.
- **Event Routing**: Intelligent routing of events to interested consumers based on event types and filters.
- **Cross-Region Replication**: Event replication across geographic regions for disaster recovery.
- **API Gateway Integration**: REST APIs that trigger commands and expose projections.
- **WebSocket Streaming**: Real-time event streaming to web clients for live updates.

### Stream Processing Strategies

- **Stateless Processing**: Simple event transformations and filtering without maintaining state.
- **Stateful Processing**: Complex event processing with windowing, aggregations, and joins.
- **Exactly-Once Processing**: Ensure critical business operations are processed exactly once.
- **Windowed Aggregations**: Time-based and count-based windows for real-time analytics.
- **Complex Event Processing**: Pattern matching and correlation across multiple event streams.

```rust
// Example: Stream processing with windowed aggregations
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let mut stream_processor = StreamProcessor::new();
    
    stream_processor
        .from_topic("user-events")
        .filter(|event| event.event_type == "UserAction")
        .window(Duration::from_minutes(5))
        .aggregate(|window| UserActivityMetrics {
            active_users: window.unique_users().count(),
            total_actions: window.len(),
            top_actions: window.top_actions(10),
        })
        .to_topic("user-activity-metrics")
        .start()
        .await?;
        
    Ok(())
}
```

### Data Activities & Consistency Strategies

- **Event Store Consistency**: Strong consistency within event store, eventual consistency across projections.
- **Saga Transactions**: Long-running distributed transactions using saga pattern with compensation.
- **Idempotency Keys**: Ensure operations can be safely retried without side effects.
- **Conflict Resolution**: Handle concurrent updates through optimistic concurrency control.
- **Data Versioning**: Version both events and projections for schema evolution.

### Database Design & Optimizations

- **Event Store Design**: Optimized for append-only operations with efficient range queries.
- **Projection Stores**: Specialized databases for different query patterns (SQL, NoSQL, search, analytics).
- **Partitioning Strategy**: Partition events by aggregate ID or time for scalability.
- **Retention Policies**: Balance storage costs with audit requirements and replay needs.

| Storage Type | Use Case | Event Processing Pattern |
|-------------|----------|------------------------|
| Event Store | Source of truth | Append-only, ordered reads |
| RDBMS | Transactional projections | SQL queries, ACID consistency |
| Document DB | Flexible projections | Document queries, eventual consistency |
| Time-series DB | Metrics and analytics | Time-based queries, aggregations |
| Search Engine | Full-text search | Complex queries, faceted search |

### Source Control Strategies

- **Event Schema Versioning**: Version control for event schemas with migration strategies.
- **Service Independence**: Independent versioning for event producers and consumers.
- **Schema Registry**: Centralized schema management with backward compatibility checks.
- **Event Contracts**: API-first approach with event contracts defined before implementation.
- **Migration Scripts**: Automated migration of projections when event schemas change.

### CI/CD Strategies

- **Schema Validation**: Automated validation of event schema changes for compatibility.
- **Event Testing**: Test event production, consumption, and projection building.
- **Canary Deployments**: Gradual rollout of changes with event processing monitoring.
- **Blue-Green Processing**: Switch event processing between deployment versions.
- **Rollback Strategies**: Safe rollback procedures including projection rebuilding.

### Engineering Approach: Event-First & Stream-Oriented

- **Event Storming**: Collaborative modeling of business processes through events.
- **Domain Events**: Start with business events and work backward to commands and aggregates.
- **Stream Thinking**: Model data flows as continuous streams rather than batch operations.
- **Temporal Modeling**: Consider time as a first-class concept in system design.
- **Replay-First**: Design systems to handle event replay for recovery and new features.

### Testing Strategies

Comprehensive testing strategy for event-driven systems with eventual consistency:

- **Event Testing**: Test event schema, serialization, and business semantics.
- **Aggregate Testing**: Test command handling and event generation in aggregates.
- **Projection Testing**: Test event handler logic and projection consistency.
- **Integration Testing**: Test event flow through the entire system.
- **Eventual Consistency Testing**: Test system behavior under network partitions and delays.
- **Replay Testing**: Test event replay scenarios for recovery and new projections.
- **Performance Testing**: Load testing of event processing throughput and latency.

Test organization for event-driven systems:
```
tests/
├─ unit/
│  ├─ aggregates/       # Command handling and event generation
│  ├─ events/          # Event schema and serialization
│  └─ projections/     # Event handler logic
├─ integration/
│  ├─ event-flow/      # End-to-end event processing
│  ├─ projections/     # Projection consistency and updates
│  └─ sagas/          # Long-running process coordination
├─ performance/
│  ├─ throughput/      # Event processing throughput
│  ├─ latency/        # Event processing latency
│  └─ scalability/    # System behavior under load
└─ chaos/
   ├─ partitions/      # Network partition testing
   ├─ failures/       # Service failure scenarios
   └─ recovery/       # System recovery testing
```

### Validation Domains & Best Combination

Validation strategy for event-driven architecture with eventual consistency:

| Validation Domain | Implementation Location | Strategy |
|------------------|------------------------|----------|
| Command Validation | Command Handlers | Validate business rules before event generation |
| Event Schema Validation | Event Serialization | Validate event structure and required fields |
| Business Invariants | Aggregates | Enforce domain rules within aggregate boundaries |
| Projection Consistency | Event Handlers | Validate projection updates and handle conflicts |
| Stream Processing | Stream Processors | Validate event processing logic and transformations |
| Cross-System Consistency | Saga Coordinators | Validate distributed transaction completion |

**Best Practices:**
- Validate commands before generating events to prevent invalid state changes
- Use schema registry to validate event structure and evolution compatibility
- Implement idempotent event handlers to safely handle processing duplicates
- Monitor projection lag and implement alerting for consistency violations
- Test eventual consistency scenarios with chaos engineering approaches
- Use correlation IDs to track validation failures across event processing chains