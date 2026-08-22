{
  "task": "comprehensive_repository_analysis",
  "objective": "Conduct exhaustive analysis of entire codebase to identify, prioritize, fix, and document ALL verifiable bugs, security vulnerabilities, and critical issues across any technology stack",
  "analysis_phases": [
    {
      "phase": 1,
      "name": "Repository Discovery & Mapping",
      "steps": [
        {
          "step": "1.1",
          "title": "Architecture & Structure Analysis",
          "actions": [
            "Map complete directory structure (src/, lib/, tests/, docs/, config/, scripts/, build/, deploy/)",
            "Identify all technology stacks and frameworks in use",
            "Parse dependency manifests (package.json, requirements.txt, go.mod, pom.xml, Gemfile, Cargo.toml, composer.json)",
            "Document entry points, main execution paths, and module boundaries",
            "Analyze build systems (Webpack, Gradle, Maven, Make, CMake)",
            "Review CI/CD configurations (GitHub Actions, GitLab CI, Jenkins, CircleCI)",
            "Examine existing documentation (README, CONTRIBUTING, API specs, architecture diagrams)"
          ]
        },
        {
          "step": "1.2",
          "title": "Development Environment Inventory",
          "actions": [
            "Identify testing frameworks (Jest, Mocha, pytest, PHPUnit, Go test, JUnit, RSpec, xUnit)",
            "Review linter/formatter configs (ESLint, Prettier, Black, Flake8, RuboCop, golangci-lint, Checkstyle)",
            "Scan for inline issue markers (TODO, FIXME, HACK, XXX, BUG, NOTE)",
            "Analyze git history for problematic patterns and recent hotfixes",
            "Extract existing test coverage reports and metrics",
            "Identify code analysis tools already in use (SonarQube, CodeClimate, etc.)"
          ]
        }
      ]
    },
    {
      "phase": 2,
      "name": "Systematic Bug Discovery",
      "bug_categories": [
        {
          "category": "CRITICAL",
          "severity": "P0",
          "types": [
            "SQL Injection vulnerabilities",
            "Cross-Site Scripting (XSS) flaws",
            "Cross-Site Request Forgery (CSRF) vulnerabilities",
            "Authentication/Authorization bypass",
            "Remote Code Execution (RCE) risks",
            "Data corruption or permanent data loss",
            "System crashes, deadlocks, or infinite loops",
            "Memory leaks and resource exhaustion",
            "Insecure cryptographic implementations",
            "Hardcoded secrets or credentials"
          ]
        },
        {
          "category": "FUNCTIONAL",
          "severity": "P1-P2",
          "types": [
            "Logic errors (incorrect conditionals, wrong calculations, off-by-one errors)",
            "State management issues (race conditions, stale state, improper mutations)",
            "Incorrect API contracts or request/response mappings",
            "Missing or insufficient input validation",
            "Broken business logic or workflow violations",
            "Incorrect data transformations or serialization",
            "Type mismatches or unsafe type coercions",
            "Incorrect exception handling or error propagation"
          ]
        },
        {
          "category": "INTEGRATION",
          "severity": "P2",
          "types": [
            "Incorrect external API usage or outdated endpoints",
            "Database query errors, SQL syntax issues, or N+1 problems",
            "Message queue handling failures (RabbitMQ, Kafka, SQS)",
            "File system operation errors (permissions, path traversal)",
            "Network communication issues (timeouts, retries, connection pooling)",
            "Cache inconsistency or invalidation problems",
            "Third-party library misuse or version incompatibilities"
          ]
        },
        {
          "category": "EDGE_CASES",
          "severity": "P2-P3",
          "types": [
            "Null/undefined/nil/None pointer dereferences",
            "Empty array/list/collection handling",
            "Zero or negative value edge cases",
            "Boundary conditions (max/min integers, string length limits)",
            "Missing error handling or swallowed exceptions",
            "Timeout and retry logic failures",
            "Concurrent access issues without proper locking",
            "Overflow/underflow in numeric operations"
          ]
        },
        {
          "category": "CODE_QUALITY",
          "severity": "P3-P4",
          "types": [
            "Deprecated API usage",
            "Dead code or unreachable code paths",
            "Circular dependencies",
            "Performance bottlenecks (inefficient algorithms, redundant operations)",
            "Missing or incorrect type annotations",
            "Inconsistent error handling patterns",
            "Resource leaks (file handles, database connections, network sockets)",
            "Improper logging (sensitive data exposure, insufficient context)"
          ]
        }
      ],
      "discovery_methods": [
        "Static code analysis using language-specific tools",
        "Pattern matching for common anti-patterns and code smells",
        "Dependency vulnerability scanning (npm audit, pip-audit, bundle-audit, cargo audit)",
        "Control flow and data flow analysis",
        "Dead code detection",
        "Configuration validation against best practices",
        "Documentation-to-implementation cross-verification",
        "Security-focused code review"
      ]
    },
    {
      "phase": 3,
      "name": "Bug Documentation & Prioritization",
      "bug_report_schema": {
        "bug_id": "Sequential identifier (BUG-001, BUG-002, etc.)",
        "severity": {
          "type": "enum",
          "values": [
            "CRITICAL",
            "HIGH",
            "MEDIUM",
            "LOW"
          ],
          "description": "Bug severity level"
        },
        "category": {
          "type": "enum",
          "values": [
            "SECURITY",
            "FUNCTIONAL",
            "PERFORMANCE",
            "INTEGRATION",
            "CODE_QUALITY"
          ],
          "description": "Bug classification"
        },
        "location": {
          "files": [
            "Array of affected file paths with line numbers"
          ],
          "component": "Module/Service/Feature name",
          "function": "Specific function or method name"
        },
        "description": {
          "current_behavior": "What's broken or wrong",
          "expected_behavior": "What should happen instead",
          "root_cause": "Technical explanation of why it's broken"
        },
        "impact_assessment": {
          "user_impact": "Effect on end users (data loss, security exposure, UX degradation)",
          "system_impact": "Effect on system (performance, stability, scalability)",
          "business_impact": "Effect on business (compliance, revenue, reputation, legal)"
        },
        "reproduction": {
          "steps": [
            "Step-by-step instructions to reproduce"
          ],
          "test_data": "Sample data or conditions needed",
          "actual_result": "What happens when reproduced",
          "expected_result": "What should happen"
        },
        "verification": {
          "code_snippet": "Demonstrative code showing the bug",
          "test_case": "Test that would fail due to this bug",
          "logs_or_metrics": "Evidence from logs or monitoring"
        },
        "dependencies": {
          "related_bugs": [
            "Array of related BUG-IDs"
          ],
          "blocking_issues": [
            "Array of bugs that must be fixed first"
          ],
          "blocked_by": [
            "External factors preventing fix"
          ]
        },
        "metadata": {
          "discovered_date": "ISO 8601 timestamp",
          "discovered_by": "Tool or method used",
          "cve_id": "If applicable, CVE identifier",
          "cwe_id": "If applicable, CWE identifier"
        }
      },
      "prioritization_matrix": {
        "criteria": [
          {
            "factor": "severity",
            "weight": 0.4,
            "scale": "CRITICAL=100, HIGH=70, MEDIUM=40, LOW=10"
          },
          {
            "factor": "user_impact",
            "weight": 0.3,
            "scale": "All users=100, Many=70, Some=40, Few=10"
          },
          {
            "factor": "fix_complexity",
            "weight": 0.15,
            "scale": "Simple=100, Medium=60, Complex=20"
          },
          {
            "factor": "regression_risk",
            "weight": 0.15,
            "scale": "Low=100, Medium=60, High=20"
          }
        ],
        "formula": "priority_score = Σ(factor_value × weight)"
      }
    },
    {
      "phase": 4,
      "name": "Fix Implementation",
      "fix_workflow": [
        {
          "step": 1,
          "action": "Create isolated fix branch",
          "naming": "fix/BUG-{id}-{short-description}"
        },
        {
          "step": 2,
          "action": "Write failing test FIRST",
          "rationale": "Test-Driven Development ensures fix is verifiable"
        },
        {
          "step": 3,
          "action": "Implement minimal, focused fix",
          "principle": "Smallest change that correctly resolves the issue"
        },
        {
          "step": 4,
          "action": "Verify test now passes",
          "validation": "Run specific test and related test suite"
        },
        {
          "step": 5,
          "action": "Run full regression test suite",
          "validation": "Ensure no existing functionality breaks"
        },
        {
          "step": 6,
          "action": "Update documentation",
          "scope": "API docs, inline comments, changelog"
        }
      ],
      "fix_principles": [
        "MINIMAL_CHANGE: Make the smallest change that correctly fixes the issue",
        "NO_SCOPE_CREEP: Avoid unrelated refactoring or feature additions",
        "BACKWARDS_COMPATIBLE: Preserve existing API contracts unless bug itself is breaking",
        "FOLLOW_CONVENTIONS: Adhere to project's existing code style and patterns",
        "DEFENSIVE_PROGRAMMING: Add guards to prevent similar bugs in the future",
        "EXPLICIT_OVER_IMPLICIT: Make intent clear through code structure and comments",
        "FAIL_FAST: Validate inputs early and fail with clear error messages"
      ],
      "code_review_checklist": [
        "Fix addresses root cause, not just symptoms",
        "All edge cases are properly handled",
        "Error messages are clear, actionable, and don't expose sensitive info",
        "Performance impact is acceptable (no O(n²) where O(n) suffices)",
        "Security implications thoroughly considered",
        "No new compiler warnings or linting errors",
        "Changes are covered by tests",
        "Documentation is updated and accurate",
        "Breaking changes are clearly marked and justified",
        "Dependencies are up-to-date and secure"
      ]
    },
    {
      "phase": 5,
      "name": "Testing & Validation",
      "test_requirements": {
        "mandatory_tests_per_fix": [
          {
            "type": "unit_test",
            "description": "Isolated test for the specific bug fix",
            "coverage": "Must cover the exact code path that was broken"
          },
          {
            "type": "integration_test",
            "description": "Test if bug involves multiple components",
            "coverage": "End-to-end flow through affected systems"
          },
          {
            "type": "regression_test",
            "description": "Ensure fix doesn't break existing functionality",
            "coverage": "All related features and code paths"
          },
          {
            "type": "edge_case_tests",
            "description": "Cover boundary conditions and corner cases",
            "coverage": "Null values, empty inputs, limits, error conditions"
          }
        ]
      },
      "test_structure_template": {
        "description": "Language-agnostic test structure",
        "template": [
          "describe('BUG-{ID}: {description}', () => {",
          "  test('reproduces original bug', () => {",
          "    // This test demonstrates the bug existed",
          "    // Should fail before fix, pass after",
          "  });",
          "",
          "  test('verifies fix resolves issue', () => {",
          "    // This test proves correct behavior after fix",
          "  });",
          "",
          "  test('handles edge case: {case}', () => {",
          "    // Additional coverage for related scenarios",
          "  });",
          "});"
        ]
      },
      "validation_steps": [
        {
          "step": "Run full test suite",
          "commands": {
            "javascript": "npm test",
            "python": "pytest",
            "go": "go test ./...",
            "java": "mvn test",
            "ruby": "bundle exec rspec",
            "rust": "cargo test",
            "php": "phpunit"
          }
        },
        {
          "step": "Measure code coverage",
          "tools": [
            "Istanbul/NYC",
            "Coverage.py",
            "JaCoCo",
            "SimpleCov",
            "Tarpaulin"
          ]
        },
        {
          "step": "Run static analysis",
          "tools": [
            "ESLint",
            "Pylint",
            "golangci-lint",
            "SpotBugs",
            "Clippy"
          ]
        },
        {
          "step": "Performance benchmarking",
          "condition": "If fix affects hot paths or critical operations"
        },
        {
          "step": "Security scanning",
          "tools": [
            "Snyk",
            "OWASP Dependency-Check",
            "Trivy",
            "Bandit"
          ]
        }
      ]
    },
    {
      "phase": 6,
      "name": "Documentation & Reporting",
      "fix_documentation_requirements": [
        "Update inline code comments explaining the fix and why it was necessary",
        "Revise API documentation if behavior changed",
        "Update CHANGELOG.md with bug fix entry",
        "Create or update troubleshooting guides",
        "Document any workarounds for deferred/unfixed issues",
        "Add migration notes if fix requires user action"
      ],
      "executive_summary_template": {
        "title": "Bug Fix Report - {repository_name}",
        "metadata": {
          "date": "ISO 8601 date",
          "analyzer": "Tool/Person name",
          "repository": "Full repository path",
          "commit_hash": "Git commit SHA",
          "duration": "Analysis duration in hours"
        },
        "overview": {
          "total_bugs_found": "integer",
          "total_bugs_fixed": "integer",
          "bugs_deferred": "integer",
          "test_coverage_before": "percentage",
          "test_coverage_after": "percentage",
          "files_analyzed": "integer",
          "lines_of_code": "integer"
        },
        "critical_findings": [
          "Top 3-5 most critical bugs found and their fixes"
        ],
        "fix_summary_by_category": {
          "security": "count",
          "functional": "count",
          "performance": "count",
          "integration": "count",
          "code_quality": "count"
        },
        "detailed_fix_table": {
          "columns": [
            "BUG-ID",
            "File",
            "Line",
            "Category",
            "Severity",
            "Description",
            "Status",
            "Test Added"
          ],
          "format": "Markdown table or CSV"
        },
        "risk_assessment": {
          "remaining_high_priority": [
            "List of unfixed critical issues"
          ],
          "recommended_next_steps": [
            "Prioritized action items"
          ],
          "technical_debt": [
            "Summary of identified tech debt"
          ],
          "breaking_changes": [
            "Any backwards-incompatible fixes"
          ]
        },
        "testing_results": {
          "test_command": "Exact command used to run tests",
          "tests_passed": "X out of Y",
          "tests_failed": "count with reasons",
          "tests_added": "count",
          "coverage_delta": "+X% or -X%"
        }
      },
      "deliverables_checklist": [
        "All bugs documented in standardized format",
        "Fixes implemented with minimal scope",
        "Test suite updated and passing",
        "Documentation updated (code, API, user guides)",
        "Code review completed and approved",
        "Performance impact assessed and acceptable",
        "Security review conducted for security-related fixes",
        "Deployment notes and rollback plan prepared",
        "Changelog updated with user-facing changes",
        "Stakeholders notified of critical fixes"
      ]
    },
    {
      "phase": 7,
      "name": "Continuous Improvement",
      "pattern_analysis": {
        "objectives": [
          "Identify recurring bug patterns across codebase",
          "Detect architectural issues enabling bugs",
          "Find gaps in testing strategy",
          "Highlight areas with technical debt"
        ],
        "outputs": [
          "Common bug pattern report",
          "Preventive measure recommendations",
          "Tooling improvement suggestions",
          "Architectural refactoring proposals"
        ]
      },
      "monitoring_recommendations": {
        "metrics_to_track": [
          "Bug discovery rate over time",
          "Time to resolution by severity",
          "Regression rate (bugs reintroduced)",
          "Test coverage percentage",
          "Code churn in bug-prone areas",
          "Dependency vulnerability count"
        ],
        "alerting_rules": [
          "Critical security vulnerabilities in dependencies",
          "Test suite failures",
          "Code coverage drops below threshold",
          "Performance degradation in key operations"
        ],
        "logging_improvements": [
          "Add structured logging where missing",
          "Include correlation IDs for request tracing",
          "Log security-relevant events",
          "Ensure error logs include stack traces and context"
        ]
      }
    }
  ],
  "constraints_and_best_practices": [
    "NEVER compromise security for simplicity or convenience",
    "MAINTAIN complete audit trail of all changes",
    "FOLLOW semantic versioning if fixes change public API",
    "RESPECT rate limits when testing external services",
    "USE feature flags for high-risk or gradual rollout fixes",
    "DOCUMENT all assumptions made during analysis",
    "CONSIDER rollback strategy for every fix",
    "PREFER backwards-compatible fixes when possible",
    "AVOID introducing new dependencies without justification",
    "TEST in multiple environments when applicable"
  ],
  "output_formats": [
    {
      "format": "markdown",
      "purpose": "Human-readable documentation and reports",
      "filename_pattern": "bug_report_{date}.md"
    },
    {
      "format": "json",
      "purpose": "Machine-readable for automated processing",
      "filename_pattern": "bug_data_{date}.json",
      "schema": "Follow bug_report_schema defined in Phase 3"
    },
    {
      "format": "csv",
      "purpose": "Import into bug tracking systems (Jira, GitHub Issues)",
      "filename_pattern": "bugs_{date}.csv",
      "columns": [
        "BUG-ID",
        "Severity",
        "Category",
        "File",
        "Line",
        "Description",
        "Status"
      ]
    },
    {
      "format": "yaml",
      "purpose": "Configuration-friendly format for CI/CD integration",
      "filename_pattern": "bug_config_{date}.yaml"
    }
  ],
  "special_considerations": {
    "monorepos": "Analyze each package/workspace separately with cross-package dependency tracking",
    "microservices": "Consider inter-service contracts, API compatibility, and distributed tracing",
    "legacy_code": "Balance fix risk vs benefit; prioritize high-impact, low-risk fixes",
    "third_party_dependencies": "Report vulnerabilities upstream; consider alternatives if unmaintained",
    "high_traffic_systems": "Consider deployment strategies (blue-green, canary) for fixes",
    "regulated_industries": "Ensure compliance requirements met (HIPAA, PCI-DSS, SOC2, GDPR)",
    "open_source_projects": "Follow contribution guidelines; engage with maintainers before large changes"
  },
  "success_criteria": {
    "quantitative": [
      "All CRITICAL and HIGH severity bugs addressed",
      "Test coverage increased by at least X%",
      "Zero security vulnerabilities in dependencies",
      "All tests passing",
      "Code quality metrics improved (cyclomatic complexity, maintainability index)"
    ],
    "qualitative": [
      "Codebase is more maintainable",
      "Documentation is clear and comprehensive",
      "Team can confidently deploy fixes",
      "Future bug prevention mechanisms in place",
      "Development velocity improved"
    ]
  }
}
