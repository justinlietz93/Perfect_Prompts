---
name: aws-cloud-expert
description: |
  Designs and implements AWS cloud architectures with focus on Well-Architected Framework, cost optimization, and security. Use when:
  1. Designing or reviewing AWS infrastructure architecture
  2. Migrating workloads to AWS or between AWS services
  3. Optimizing AWS costs (right-sizing, Reserved Instances, Savings Plans)
  4. Implementing AWS security, compliance, or disaster recovery
  5. Troubleshooting AWS service issues or performance problems
---

**Region**: ${region:us-east-1}
**Secondary Region**: ${secondary_region:us-west-2}
**Environment**: ${environment:production}
**VPC CIDR**: ${vpc_cidr:10.0.0.0/16}
**Instance Type**: ${instance_type:t3.medium}

# AWS Architecture Decision Framework

## Service Selection Matrix

| Workload Type | Primary Service | Alternative | Decision Factor |
|---------------|-----------------|-------------|-----------------|
| Stateless API | Lambda + API Gateway | ECS Fargate | Request duration >15min -> ECS |
| Stateful web app | ECS/EKS | EC2 Auto Scaling | Container expertise -> ECS/EKS |
| Batch processing | Step Functions + Lambda | AWS Batch | GPU/long-running -> Batch |
| Real-time streaming | Kinesis Data Streams | MSK (Kafka) | Existing Kafka -> MSK |
| Static website | S3 + CloudFront | Amplify | Full-stack -> Amplify |
| Relational DB | Aurora | RDS | High availability -> Aurora |
| Key-value store | DynamoDB | ElastiCache | Sub-ms latency -> ElastiCache |
| Data warehouse | Redshift | Athena | Ad-hoc queries -> Athena |

## Compute Decision Tree

```
Start: What's your workload pattern?
|
+-> Event-driven, <15min execution
|   +-> Lambda
|       Consider: Memory ${lambda_memory:512}MB, concurrent executions, cold starts
|
+-> Long-running containers
|   +-> Need Kubernetes?
|       +-> Yes: EKS (managed) or self-managed K8s on EC2
|       +-> No: ECS Fargate (serverless) or ECS EC2 (cost optimization)
|
+-> GPU/HPC/Custom AMI required
|   +-> EC2 with appropriate instance family
|       g4dn/p4d (ML), c6i (compute), r6i (memory), i3en (storage)
|
+-> Batch jobs, queue-based
    +-> AWS Batch with Spot instances (up to 90% savings)
```

## Networking Architecture

### VPC Design Pattern

```
${environment:production} VPC (${vpc_cidr:10.0.0.0/16})
|
+-- Public Subnets (${public_subnet_cidr:10.0.0.0/24}, 10.0.1.0/24, 10.0.2.0/24)
|   +-- ALB, NAT Gateways, Bastion (if needed)
|
+-- Private Subnets (${private_subnet_cidr:10.0.10.0/24}, 10.0.11.0/24, 10.0.12.0/24)
|   +-- Application tier (ECS, EC2, Lambda VPC)
|
+-- Data Subnets (${data_subnet_cidr:10.0.20.0/24}, 10.0.21.0/24, 10.0.22.0/24)
    +-- RDS, ElastiCache, other data stores
```

### Security Group Rules

| Tier | Inbound From | Ports |
|------|--------------|-------|
| ALB | 0.0.0.0/0 | 443 |
| App | ALB SG | ${app_port:8080} |
| Data | App SG | ${db_port:5432} |

### VPC Endpoints (Cost Optimization)

Always create for high-traffic services:
- S3 Gateway Endpoint (free)
- DynamoDB Gateway Endpoint (free)
- Interface Endpoints: ECR, Secrets Manager, SSM, CloudWatch Logs

## Cost Optimization Checklist

### Immediate Actions (Week 1)
- [ ] Enable Cost Explorer and set up budgets with alerts
- [ ] Review and terminate unused resources (Cost Explorer idle resources report)
- [ ] Right-size EC2 instances (AWS Compute Optimizer recommendations)
- [ ] Delete unattached EBS volumes and old snapshots
- [ ] Review NAT Gateway data processing charges

### Cost Estimation Quick Reference

| Resource | Monthly Cost Estimate |
|----------|----------------------|
| ${instance_type:t3.medium} (on-demand) | ~$30 |
| ${instance_type:t3.medium} (1yr RI) | ~$18 |
| Lambda (1M invocations, 1s, ${lambda_memory:512}MB) | ~$8 |
| RDS db.${instance_type:t3.medium} (Multi-AZ) | ~$100 |
| Aurora Serverless v2 (${aurora_acu:8} ACU avg) | ~$350 |
| NAT Gateway + 100GB data | ~$50 |
| S3 (1TB Standard) | ~$23 |
| CloudFront (1TB transfer) | ~$85 |

## Security Implementation

### IAM Best Practices

```
Principle: Least privilege with explicit deny

1. Use IAM roles (not users) for applications
2. Require MFA for all human users
3. Use permission boundaries for delegated admin
4. Implement SCPs at Organization level
5. Regular access reviews with IAM Access Analyzer
```

### Example IAM Policy Pattern

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3BucketAccess",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::${bucket_name:my-bucket}/*",
      "Condition": {
        "StringEquals": {"aws:PrincipalTag/Environment": "${environment:production}"}
      }
    }
  ]
}
```

### Security Checklist

- [ ] Enable CloudTrail in all regions with log file validation
- [ ] Configure AWS Config rules for compliance monitoring
- [ ] Enable GuardDuty for threat detection
- [ ] Use Secrets Manager or Parameter Store for secrets (not env vars)
- [ ] Enable encryption at rest for all data stores
- [ ] Enforce TLS 1.2+ for all connections
- [ ] Implement VPC Flow Logs for network monitoring
- [ ] Use Security Hub for centralized security view

## High Availability Patterns

### Multi-AZ Architecture (${availability_target:99.99%} target)

```
Region: ${region:us-east-1}
|
+-- AZ-a                    +-- AZ-b                    +-- AZ-c
    |                           |                           |
    ALB (active)                ALB (active)                ALB (active)
    |                           |                           |
    ECS Tasks (${replicas_per_az:2})  ECS Tasks (${replicas_per_az:2})  ECS Tasks (${replicas_per_az:2})
    |                           |                           |
    Aurora Writer               Aurora Reader               Aurora Reader
```

### Multi-Region Architecture (99.999% target)

```
Primary: ${region:us-east-1}              Secondary: ${secondary_region:us-west-2}
|                               |
Route 53 (failover routing)     Route 53 (health checks)
|                               |
CloudFront                      CloudFront
|                               |
Full stack                      Full stack (passive or active)
|                               |
Aurora Global Database -------> Aurora Read Replica
     (async replication)
```

### RTO/RPO Decision Matrix

| Tier | RTO Target | RPO Target | Strategy |
|------|------------|------------|----------|
| Tier 1 (Critical) | <${rto:15 min} | <${rpo:1 min} | Multi-region active-active |
| Tier 2 (Important) | <1 hour | <15 min | Multi-region active-passive |
| Tier 3 (Standard) | <4 hours | <1 hour | Multi-AZ with cross-region backup |
| Tier 4 (Non-critical) | <24 hours | <24 hours | Single region, backup/restore |

## Monitoring and Observability

### CloudWatch Implementation

| Metric Type | Service | Key Metrics |
|-------------|---------|-------------|
| Compute | EC2/ECS | CPUUtilization, MemoryUtilization, NetworkIn/Out |
| Database | RDS/Aurora | DatabaseConnections, ReadLatency, WriteLatency |
| Serverless | Lambda | Duration, Errors, Throttles, ConcurrentExecutions |
| API | API Gateway | 4XXError, 5XXError, Latency, Count |
| Storage | S3 | BucketSizeBytes, NumberOfObjects, 4xxErrors |

### Alerting Thresholds

| Resource | Warning | Critical | Action |
|----------|---------|----------|--------|
| EC2 CPU | >${cpu_warning:70%} 5min | >${cpu_critical:90%} 5min | Scale out, investigate |
| RDS CPU | >${rds_cpu_warning:80%} 5min | >${rds_cpu_critical:95%} 5min | Scale up, query optimization |
| Lambda errors | >1% | >5% | Investigate, rollback |
| ALB 5xx | >0.1% | >1% | Investigate backend |
| DynamoDB throttle | Any | Sustained | Increase capacity |

## Verification Checklist

### Before Production Launch

- [ ] Well-Architected Review completed (all 6 pillars)
- [ ] Load testing completed with expected peak + 50% headroom
- [ ] Disaster recovery tested with documented RTO/RPO
- [ ] Security assessment passed (penetration test if required)
- [ ] Compliance controls verified (if applicable)
- [ ] Monitoring dashboards and alerts configured
- [ ] Runbooks documented for common operations
- [ ] Cost projection validated and budgets set
- [ ] Tagging strategy implemented for all resources
- [ ] Backup and restore procedures tested
