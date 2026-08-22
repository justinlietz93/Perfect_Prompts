### Overview

This document defines a **project‑agnostic** event‑driven system template for a **LITE / single‑developer, single‑host tool**. The architecture preserves the original structure and intent while adapting components to a lightweight, in‑process design:
- Event sourcing, CQRS, and reactive programming patterns with **asynchronous communication through events and messages**.
- Every system is designed conceptually from the **Event‑out**. Then ask:
      - "Given this business process, what events occur, what state changes trigger events, what reactions are needed, and how should event flow be orchestrated?"
- Event‑out: Define business events first, identify event producers and consumers, design event schemas and flows.
- Stream‑processing: Design data and command flows as streams of events with transformation and aggregation.
- Ensure extended future scalability, **eventual consistency + resilience**, real‑time responsiveness via event‑driven reactions, **loose coupling**.

> LITE adaptation: replaces external brokers and multi‑service topology with an **in‑process event bus** and a **local append‑only event store (SQLite)**. All guidance remains project‑agnostic and compatible with scale‑out migration.

---

### EXAMPLE ONLY Project Map of an event-driven architecture project following reactive and event sourcing patterns

```go
event-driven-system-lite/
├─ README.md
├─ config/
│  └─ app.toml
├─ schema/
│  └─ events/
│     ├─ file-arrived.v1.json
│     ├─ job-created.v1.json
│     └─ …
├─ storage/
│  └─ sqlite/
│     ├─ events.db            # append-only event store (WAL mode)
│     └─ migrations/
├─ src/
│  ├─ presentation/
│  │  ├─ http/
│  │  │  └─ status_endpoints.[lang]
│  │  └─ cli/
│  ├─ application/
│  │  └─ jobs/
│  │     ├─ services/
│  │     │  ├─ file_arrival_handler.[lang]
│  │     │  └─ job_orchestrator.[lang]
│  │     └─ ports/
│  │        ├─ event_bus.[lang]
│  │        ├─ event_store.[lang]
│  │        ├─ job_repository.[lang]
│  │        ├─ job_runner.[lang]
│  │        └─ projection_store.[lang]
│  ├─ domain/
│  │  └─ jobs/
│  │     ├─ events.[lang]     # POJOs/structs only
│  │     └─ models.[lang]
│  └─ infrastructure/
│     ├─ runtime/
│     │  ├─ local_event_bus.[lang]
│     │  └─ process_job_runner.[lang]
│     ├─ storage/
│     │  ├─ sqlite_event_store.[lang]
│     │  ├─ sqlite_job_repository.[lang]
│     │  └─ sqlite_projection_store.[lang]
│     └─ linux/
│        └─ inotify_watcher.[lang]
├─ scripts/
│  ├─ migrate.[sh|ps1]
│  └─ replay.[sh|ps1]
├─ system/
│  └─ folder-jobs.service     # systemd unit (reference)
├─ tests/
│  ├─ unit/
│  ├─ contract/
│  ├─ e2e/
│  └─ property/
└─ docs/
   ├─ event-catalog/
   │  ├─ events/
   │  │  ├─ file-arrived.md
   │  │  └─ job-created.md
   │  └─ flows/
   ├─ architecture/
   │  ├─ event-flows.md
   │  ├─ cqrs-design.md
   │  └─ streaming-topology-lite.md
   └─ runbooks/
      ├─ event-replay.md
      └─ monitoring.md
```

> LITE adaptation: the original multi‑broker directories (`kafka/`, `pulsar/`, `nats/`) and multi‑service layout are consolidated into a **single codebase** with **ports/adapters**. External broker stubs are replaced by `runtime/local_event_bus` and `storage/sqlite_event_store`.

---

### Event-Driven Architecture Implementation

This section documents the Event‑Driven Architecture approach, emphasizing asynchronous communication, event sourcing, CQRS, and reactive programming patterns. It serves as a generic template for implementing responsive and resilient event‑driven applications.

#### Core Principles

- **Event‑First Design**: Business processes modeled as sequences of events with clear causality chains.
- **Eventual Consistency**: Different parts of the system reach consistency asynchronously.
- **Reactive Programming**: Components react to events as they occur, enabling near real‑time responsiveness.
- **Immutable Events**: Events are immutable facts representing what already happened.
- **Event Sourcing**: Store events as the primary source of truth; derive current state from event history.
- **CQRS**: Separate command (write) and query (read) models for clarity and performance.
- **Loose Coupling**: Components communicate through events without direct dependencies.

#### Architecture Structure

1. **Event Store (Source of Truth)**
   - **Components**: SQLite persistence, named streams, checkpoints, replay utilities.
   - **Responsibilities**: Durable append‑only storage, ordered reads per stream, history for audit/rebuild.
   - **Dependencies**: Local SQLite database in WAL mode.
   - **Rules**:
     - Events are append‑only and immutable.
     - Strong consistency within a stream/aggregate boundary.
     - Ordering preserved within streams (`stream`, `version`).
     - Support for replay and time‑travel debugging.

2. **Command Side (Write Operations)**
   - **Components**: Command handlers, domain aggregates/services, event emitters.
   - **Responsibilities**: Validate commands, enforce business rules, generate events.
   - **Dependencies**: Event store, domain models.
   - **Rules**:
     - Commands may succeed or fail; commands are not durable.
     - Aggregate consistency boundaries observed.
     - Business validation precedes event generation.
     - Optimistic concurrency via stream version checks.

3. **Query Side (Read Operations)**
   - **Components**: Event handlers, projections, read models, query handlers.
   - **Responsibilities**: Build read‑optimized views from events; answer queries.
   - **Dependencies**: Event streams, local read database (SQLite).
   - **Rules**:
     - Eventually consistent with command side.
     - Multiple projections are permitted for distinct query needs.
     - Denormalized data for query performance.
     - Idempotent event processing is mandatory.

4. **Event Streaming Platform (Event Transportation)**
   - **Components**: **Local in‑process event bus**, publication/subscription, dead‑letter handling.
   - **Responsibilities**: Event distribution, delivery guarantees, simple routing.
   - **Dependencies**: In‑process pub/sub; external brokers are out of scope for LITE.
   - **Rules**:
     - At‑least‑once delivery guarantees.
     - Ordering guaranteed per stream; parallelism via bounded worker pool.
     - Schema evolution and compatibility enforced at the edges.
     - Poison message handling via DLQ/quarantine.

5. **Stream Processing (Real‑time Analytics)**
   - **Components**: In‑process stream processors, aggregators, simple windows.
   - **Responsibilities**: Lightweight real‑time analysis, counters, rolling aggregates.
   - **Dependencies**: Local event bus and projection stores.
   - **Rules**:
     - Stateless and stateful handlers are permitted.
     - Time‑based windows are supported via timers/checkpoints.
     - Fault tolerance via idempotency + checkpointed progress.

6. **Saga Orchestration (Long‑running Processes)**
   - **Components**: In‑process saga coordinator, compensation handlers, timers.
   - **Responsibilities**: Coordinate long‑running processes inside one host.
   - **Dependencies**: Event streams, local saga state.
   - **Rules**:
     - Orchestration or choreography patterns are both acceptable.
     - Compensation actions for rollback scenarios.
     - Timeouts and retry policies are specified; steps remain idempotent.

#### Interfaces, Contracts, and API Requirements

- **Event Schema Management**
  - All events MUST have well‑defined schemas with versioning support.
  - Schema evolution MUST preserve backward compatibility within a major version.
  - Schemas are stored **in‑repo** under `schema/events` with code‑generated types OPTIONAL.
  - Breaking changes REQUIRE a new major version with migration strategy.

- **Event Contracts**
  - **Structure**: `event_id`, timestamp, `type`, `version`, `payload`, `meta`.
  - **Ordering**: Events within a stream maintain order.
  - **Delivery**: At‑least‑once with idempotent processing.
  - **Retention**: Based on business/compliance; archiving permitted.

- **Command Contracts**
  - Commands represent intent to change state.
  - Commands are not durable and may be rejected.
  - Validation occurs before event generation.
  - Results observable via subsequent events or synchronous acknowledgments.

- **Query Contracts**
  - Read models optimized for specific query patterns.
  - Eventually consistent with event store.
  - Multiple projections allowed.
  - Query responses SHOULD include freshness indicators when relevant.

- **Integration Patterns**
  - **Event Notification** (lightweight facts).
  - **Event‑Carried State Transfer** (where necessary).
  - **Event Sourcing** (primary source of truth).
  - **CQRS** (separate write and read responsibilities).

#### Dependency Flow

```
[Commands] → [Aggregates] → [Events] → [Event Store]
                              ↓
[Event Streams] → [Event Handlers] → [Projections] → [Read Models]
                              ↓
[Stream Processing] → [Real‑time Analytics] → [Metrics/Alerts]
                              ↓
[Saga Orchestration] → [Compensation] → [Long‑running Processes]
```

- Events flow from command processing to multiple consumption patterns.
- Each consumer processes events independently and asynchronously.
- Stream processing enables near real‑time analytics.
- Sagas coordinate long‑running business processes.

#### Event Integration Points

- **Event Publishing**: Aggregates publish events to the event store and local bus.
- **Event Subscription**: In‑process components subscribe to relevant event types/streams.
- **Stream Processing**: Real‑time transformation and enrichment of event streams.
- **External Integration**: Optional adapters bridge internal events to external systems (out‑of‑scope for LITE).
- **Event Replay**: Projections rebuilt from historical events as needed.

#### Rules for AI Agents

1. **Event Immutability**: Events are not modified after storage; corrections create new events.
2. **Aggregate Boundaries**: Consistency is maintained within aggregate boundaries only.
3. **Idempotent Processing**: All handlers are idempotent and duplicate‑safe.
4. **Event Versioning**: Schema evolution is planned from inception.
5. **Error Handling**: Dead‑letter handling and compensation patterns are defined.
6. **Monitoring**: Event processing latency, throughput, and failures are measured.
7. **Schema Location**: Schemas live in‑repo; compatibility checks are automated.
8. **Testing**: Event flows, projections, and eventual consistency are tested.

#### Example Implementation

- Registration flow: `RegisterUser` command → aggregate validation → `UserCreated` event → append to store → projections update (`user_profile`, `auth_view`, `analytics`) → notification module emits a local message.
- Components process events asynchronously and independently within one process.
- The system remains responsive under partial failures due to retries and DLQ.
- New projections are added by replaying historical events.

---

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **Event Immutability**: Treat events as immutable historical facts.
2. **Idempotent Processing**: Handlers are duplicate‑safe.
3. **Schema Evolution**: Backward/forward compatibility is enforced.
4. **Aggregate Consistency**: Strong consistency inside aggregates; eventual across aggregates.
5. **Error Recovery**: Robust error handling with DLQ and retries.
6. **Event Ordering**: Preserve per‑stream ordering.
7. **Monitoring and Observability**: Track lag, throughput, and failures.
8. **Testing Strategy**: Exercise replay, failure injection, and projection rebuilds.

**Code Review Checklist for AI Agents:**

- [ ] Events immutable with sufficient context.
- [ ] Handlers idempotent and duplicate‑safe.
- [ ] Schemas versioned under `schema/events` with checks.
- [ ] Aggregate boundaries respected.
- [ ] DLQ configured for poison messages.
- [ ] Ordering preserved where business requires.
- [ ] Monitoring/alerting configured for event processing.
- [ ] Failure scenarios covered, including crash recovery.

---

### Architectural Concepts

- **Event Sourcing**: Events are the source of truth; state derived by replay.
- **CQRS**: Separate command and query models.
- **Event Streaming**: Continuous flow of events through a local bus.
- **Saga Pattern**: Long‑running processes coordinated via events and compensations.
- **Event Store**: SQLite database optimized for append‑only operations and ordered reads.
- **Projections**: Read‑optimized views built from events.

### UI/UX Strategies

- **Real‑time Updates**: Server‑Sent Events or lightweight WebSocket for live status.
- **Optimistic UI**: Immediate UI updates on command; reconcile with eventual state.
- **Event‑driven Notifications**: Local notifications triggered by domain events.
- **Progressive Enhancement**: Graceful degradation when projection lag occurs.
- **Temporal UI**: Event timelines and audit trails for transparency.

### Performance Strategies (Speed & Power)

- **Per‑stream Parallelism**: Parallel workers with per‑stream ordering preserved.
- **In‑process Stream Processing**: Low‑latency handlers for transformations.
- **Projection Optimization**: Specialized read models for critical queries.
- **Caching**: Cache hot projections when beneficial.
- **Batching**: Batch projection updates to reduce write‑amplification.

### Memory Optimization & Safety

- **Snapshots**: Periodic snapshots of aggregates to reduce replay cost.
- **Compaction**: Optional compaction of obsolete events while preserving audit needs.
- **Streaming Buffers**: Bounded buffers sized by throughput targets.
- **Resource Monitoring**: Observe memory footprints of handlers and runners.

```python
# Example: Aggregate with snapshotting (language-agnostic pseudocode)
class UserAggregate:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.version = 0
        self.state = {}

    @classmethod
    def from_snapshot(cls, snapshot: dict, events_since: list):
        agg = cls(snapshot['user_id'])
        agg.version = snapshot['version']
        agg.state = snapshot['state']
        for evt in events_since:
            agg.apply(evt)
        return agg

    def snapshot(self) -> dict:
        return { 'user_id': self.user_id, 'version': self.version, 'state': self.state }
```

### Logging Strategies

- **Event Audit Trail**: Naturally provided by the event store.
- **Correlation Tracking**: Correlation/causation IDs across commands and events.
- **Processing Metrics**: Latency, throughput, error rates.
- **Business Event Logging**: Key domain events for analytics and monitoring.
- **Debug Logging**: Verbose traces gated by configuration.

### Security Strategies

- **Sensitive Data Handling**: Encrypt at rest where applicable; minimize payload PII.
- **Access Control**: Least privilege for event store and projections.
- **Event Signing**: Optional signatures for integrity and non‑repudiation.
- **Privacy Compliance**: Redaction/anonymization policies documented.
- **Immutable Audit**: Event log treated as append‑only with controlled access.

### Networking / Event Distribution Strategies

- **LITE Scope**: In‑process distribution only.
- **Scale‑out Path (Optional)**: When external distribution is required, replace the local bus with a broker adapter (Kafka/NATS/etc.) while preserving port contracts.
- **API Gateway Integration**: Optional REST endpoints trigger commands and expose read models.

### Stream Processing Strategies

- **Stateless Processing**: Transformations and filters.
- **Stateful Processing**: Windowed counters and joins via local state.
- **Exactly‑Once (Pragmatic)**: Achieved effectively via idempotent handlers + transactional append‑then‑publish.
- **Windowed Aggregations**: Time‑based windows with checkpointed progress.

```rust
// Example: Windowed metric in a local processor (pseudocode)
fn run() {
    let mut proc = Processor::new();
    proc.from_local_bus("user-events")
        .filter(|e| e.kind == "UserAction")
        .window(minutes(5))
        .aggregate(|w| metrics_from(w))
        .publish("user-activity-metrics");
}
```

### Data Activities & Consistency Strategies

- **Event Store Consistency**: Strong within streams; eventual across projections.
- **Saga Transactions**: Compensation‑based recovery for long‑running flows.
- **Idempotency Keys**: Stable tokens for safe retries.
- **Conflict Resolution**: Optimistic concurrency with version checks.
- **Data Versioning**: Version events and projections.

### Database Design & Optimizations

- **Event Store Design**: SQLite in WAL mode; append‑only; indexed by `(stream, version)` and `(type, ts)`.
- **Projection Stores**: SQLite tables optimized for read patterns.
- **Partitioning Strategy**: Logical partitioning by stream ID; execution parallelism at worker layer.
- **Retention Policies**: Archive old segments; keep projections rebuildable.

| Storage Type | Use Case | Event Processing Pattern |
|-------------|----------|--------------------------|
| Event Store | Source of truth | Append‑only, ordered reads |
| RDBMS (SQLite) | Transactional projections | SQL queries, ACID consistency |
| Document DB | Flexible projections (optional) | Document queries, eventual consistency |
| Time‑series DB | Metrics/analytics (optional) | Time‑based queries, aggregations |
| Search Engine | Full‑text search (optional) | Complex queries, faceted search |

### Source Control Strategies

- **Event Schema Versioning**: Version control for event schemas under `schema/events`.
- **Producer/Consumer Independence**: Contracts enforced via tests; loose coupling maintained.
- **Schema Checks**: Automated compatibility checks in CI.
- **Event Contracts**: Defined prior to handler implementation.
- **Migration Scripts**: Automated projection migrations when schemas evolve.

### CI/CD Strategies

- **Schema Validation**: Automated validation of schema changes.
- **Event Testing**: Producer and consumer contract tests.
- **Canary Techniques**: Gradual enablement of new handlers behind flags.
- **Blue‑Green Projections**: Build new projections in parallel; atomically swap.
- **Rollback**: Replay from checkpointed offsets.

### Engineering Approach: Event‑First & Stream‑Oriented

- **Event Storming**: Modeling business processes through events.
- **Domain Events**: Start with business events; derive commands and aggregates.
- **Stream Thinking**: Model flows as continuous streams rather than batches.
- **Temporal Modeling**: Treat time as a first‑class concept.
- **Replay‑First**: Support event replay for recovery and new features.

### Testing Strategies

Comprehensive strategy for eventual consistency:

- **Event Tests**: Schema, serialization, semantics.
- **Aggregate Tests**: Command handling and event emission.
- **Projection Tests**: Handler logic and consistency.
- **Integration Tests**: End‑to‑end event flow.
- **Replay Tests**: Recovery and new projection construction.
- **Performance Tests**: Throughput and latency under load.

Test organization:
```
tests/
├─ unit/
│  ├─ aggregates/
│  ├─ events/
│  └─ projections/
├─ integration/
│  ├─ event-flow/
│  └─ projections/
├─ performance/
│  ├─ throughput/
│  └─ latency/
└─ chaos/
   ├─ failures/
   └─ recovery/
```

### Validation Domains & Best Combination

| Validation Domain | Implementation Location | Strategy |
|------------------|-------------------------|----------|
| Command Validation | Command Handlers | Validate rules before event generation |
| Event Schema Validation | Serialization Layer | Validate structure and required fields |
| Business Invariants | Aggregates | Enforce domain rules within boundaries |
| Projection Consistency | Event Handlers | Validate updates; handle conflicts |
| Stream Processing | Local Processors | Validate transformations and windows |
| Cross‑Flow Consistency | Saga Coordinator | Validate completion and compensation |

**Best Practices:**
- Validate commands prior to event creation.
- Enforce schema compatibility checks.
- Implement idempotent handlers for duplicate safety.
- Monitor projection lag; alert on thresholds.
- Exercise eventual consistency with failure injection.
- Use correlation IDs across the processing chain.

