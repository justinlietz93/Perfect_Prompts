---
name: agent-organization-expert
description: Multi-agent orchestration skill for team assembly, task decomposition, workflow optimization, and coordination strategies to achieve optimal team performance and resource utilization.
---

# Agent Organization

Assemble and coordinate multi-agent teams through systematic task analysis, capability mapping, and workflow design.

## Configuration

- **Agent Count**: ${agent_count:3}
- **Task Type**: ${task_type:general}
- **Orchestration Pattern**: ${orchestration_pattern:parallel}
- **Max Concurrency**: ${max_concurrency:5}
- **Timeout (seconds)**: ${timeout_seconds:300}
- **Retry Count**: ${retry_count:3}

## Core Process

1. **Analyze Requirements**: Understand task scope, constraints, and success criteria
2. **Map Capabilities**: Match available agents to required skills
3. **Design Workflow**: Create execution plan with dependencies and checkpoints
4. **Orchestrate Execution**: Coordinate ${agent_count:3} agents and monitor progress
5. **Optimize Continuously**: Adapt based on performance feedback

## Task Decomposition

### Requirement Analysis
- Break complex tasks into discrete subtasks
- Identify input/output requirements for each subtask
- Estimate complexity and resource needs per component
- Define clear success criteria for each unit

### Dependency Mapping
- Document task execution order constraints
- Identify data dependencies between subtasks
- Map resource sharing requirements
- Detect potential bottlenecks and conflicts

### Timeline Planning
- Sequence tasks respecting dependencies
- Identify parallelization opportunities (up to ${max_concurrency:5} concurrent)
- Allocate buffer time for high-risk components
- Define checkpoints for progress validation

## Agent Selection

### Capability Matching
Select agents based on:
- Required skills versus agent specializations
- Historical performance on similar tasks
- Current availability and workload capacity
- Cost efficiency for the task complexity

### Selection Criteria Priority
1. **Capability fit**: Agent must possess required skills
2. **Track record**: Prefer agents with proven success
3. **Availability**: Sufficient capacity for timely completion
4. **Cost**: Optimize resource utilization within constraints

### Backup Planning
- Identify alternate agents for critical roles
- Define failover triggers and handoff procedures
- Maintain redundancy for single-point-of-failure tasks

## Team Assembly

### Composition Principles
- Ensure complete skill coverage for all subtasks
- Balance workload across ${agent_count:3} team members
- Minimize communication overhead
- Include redundancy for critical functions

### Role Assignment
- Match agents to subtasks based on strength
- Define clear ownership and accountability
- Establish communication channels between dependent roles
- Document escalation paths for blockers

### Team Sizing
- Smaller teams for tightly coupled tasks
- Larger teams for parallelizable workloads
- Consider coordination overhead in sizing decisions
- Scale dynamically based on progress

## Orchestration Patterns

### Sequential Execution
Use when tasks have strict ordering requirements:
- Task B requires output from Task A
- State must be consistent between steps
- Error handling requires ordered rollback

### Parallel Processing
Use when tasks are independent (${orchestration_pattern:parallel}):
- No data dependencies between tasks
- Separate resource requirements
- Results can be aggregated after completion
- Maximum ${max_concurrency:5} concurrent operations

### Pipeline Pattern
Use for streaming or continuous processing:
- Each stage processes and forwards results
- Enables concurrent execution of different stages
- Reduces overall latency for multi-step workflows

### Hierarchical Delegation
Use for complex tasks requiring sub-orchestration:
- Lead agent coordinates sub-teams
- Each sub-team handles a domain
- Results aggregate upward through hierarchy

### Map-Reduce
Use for large-scale data processing:
- Map phase distributes work across agents
- Each agent processes a partition
- Reduce phase combines results

## Workflow Design

### Process Structure
1. **Entry point**: Validate inputs and initialize state
2. **Execution phases**: Ordered task groupings
3. **Checkpoints**: State persistence and validation points
4. **Exit point**: Result aggregation and cleanup

### Control Flow
- Define branching conditions for alternative paths
- Specify retry policies for transient failures (max ${retry_count:3} retries)
- Establish timeout thresholds per phase (${timeout_seconds:300}s default)
- Plan graceful degradation for partial failures

### Data Flow
- Document data transformations between stages
- Specify data formats and validation rules
- Plan for data persistence at checkpoints
- Handle data cleanup after completion

## Coordination Strategies

### Communication Patterns
- **Direct**: Agent-to-agent for tight coupling
- **Broadcast**: One-to-many for status updates
- **Queue-based**: Asynchronous for decoupled tasks
- **Event-driven**: Reactive to state changes

### Synchronization
- Define sync points for dependent tasks
- Implement waiting mechanisms with timeouts (${timeout_seconds:300}s)
- Handle out-of-order completion gracefully
- Maintain consistent state across agents

### Conflict Resolution
- Establish priority rules for resource contention
- Define arbitration mechanisms for conflicts
- Document rollback procedures for deadlocks
- Prevent conflicts through careful scheduling

## Performance Optimization

### Load Balancing
- Distribute work based on agent capacity
- Monitor utilization and rebalance dynamically
- Avoid overloading high-performing agents
- Consider agent locality for data-intensive tasks

### Bottleneck Management
- Identify slow stages through monitoring
- Add capacity to constrained resources
- Restructure workflows to reduce dependencies
- Cache intermediate results where beneficial

### Resource Efficiency
- Pool shared resources across agents
- Release resources promptly after use
- Batch similar operations to reduce overhead
- Monitor and alert on resource waste

## Monitoring and Adaptation

### Progress Tracking
- Monitor completion status per task
- Track time spent versus estimates
- Identify tasks at risk of delay
- Report aggregated progress to stakeholders

### Performance Metrics
- Task completion rate and latency
- Agent utilization and throughput
- Error rates and recovery times
- Resource consumption and cost

### Dynamic Adjustment
- Reallocate agents based on progress
- Adjust priorities based on blockers
- Scale team size based on workload
- Modify workflow based on learning

## Error Handling

### Failure Detection
- Monitor for task failures and timeouts (${timeout_seconds:300}s threshold)
- Detect agent unavailability promptly
- Identify cascade failure patterns
- Alert on anomalous behavior

### Recovery Procedures
- Retry transient failures with backoff (up to ${retry_count:3} attempts)
- Failover to backup agents when needed
- Rollback to last checkpoint on critical failure
- Escalate unrecoverable issues

### Prevention
- Validate inputs before execution
- Test agent availability before assignment
- Design for graceful degradation
- Build redundancy into critical paths

## Quality Assurance

### Validation Gates
- Verify outputs at each checkpoint
- Cross-check results from parallel tasks
- Validate final aggregated results
- Confirm success criteria are met

### Performance Standards
- Agent selection accuracy target: >${agent_selection_accuracy:95}%
- Task completion rate target: >${task_completion_rate:99}%
- Response time target: <${response_time_threshold:5} seconds
- Resource utilization: optimal range ${utilization_min:60}-${utilization_max:80}%

## Best Practices

### Planning
- Invest time in thorough task analysis
- Document assumptions and constraints
- Plan for failure scenarios upfront
- Define clear success metrics

### Execution
- Start with minimal viable team (${agent_count:3} agents)
- Scale based on observed needs
- Maintain clear communication channels
- Track progress against milestones

### Learning
- Capture performance data for analysis
- Identify patterns in successes and failures
- Refine selection and coordination strategies
- Share learnings across future orchestrations
