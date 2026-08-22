## Objective
Conduct a thorough analysis of the entire repository to identify, prioritize, fix, and document ALL verifiable bugs, security vulnerabilities, and critical issues across any programming language, framework, or technology stack.

## Phase 1: Initial Repository Assessment

### 1.1 Architecture Mapping
- Map complete project structure (src/, lib/, tests/, docs/, config/, scripts/, etc.)
- Identify technology stack and dependencies (package.json, requirements.txt, go.mod, pom.xml, Gemfile, etc.)
- Document main entry points, critical paths, and system boundaries
- Analyze build configurations and CI/CD pipelines
- Review existing documentation (README, API docs, architecture diagrams)

### 1.2 Development Environment Analysis
- Identify testing frameworks (Jest, pytest, PHPUnit, Go test, JUnit, RSpec, etc.)
- Review linting/formatting configurations (ESLint, Prettier, Black, RuboCop, etc.)
- Check for existing issue tracking (GitHub Issues, TODO/FIXME/HACK/XXX comments)
- Analyze commit history for recent problematic areas
- Review existing test coverage reports if available

## Phase 2: Systematic Bug Discovery

### 2.1 Bug Categories to Identify
**Critical Bugs:**
- Security vulnerabilities (SQL injection, XSS, CSRF, auth bypass, etc.)
- Data corruption or loss risks
- System crashes or deadlocks
- Memory leaks or resource exhaustion

**Functional Bugs:**
- Logic errors (incorrect conditions, wrong calculations, off-by-one errors)
- State management issues (race conditions, inconsistent state, improper mutations)
- Incorrect API contracts or data mappings
- Missing or incorrect validations
- Broken business rules or workflows

**Integration Bugs:**
- Incorrect external API usage
- Database query errors or inefficiencies
- Message queue handling issues
- File system operation problems
- Network communication errors

**Edge Cases & Error Handling:**
- Null/undefined/nil handling
- Empty collections or zero-value edge cases
- Boundary conditions and limit violations
- Missing error propagation or swallowing exceptions
- Timeout and retry logic issues

**Code Quality Issues:**
- Type mismatches or unsafe casts
- Deprecated API usage
- Dead code or unreachable branches
- Circular dependencies
- Performance bottlenecks (N+1 queries, inefficient algorithms)

### 2.2 Discovery Methods
- Static code analysis using language-specific tools
- Pattern matching for common anti-patterns
- Dependency vulnerability scanning
- Code path analysis for unreachable or untested code
- Configuration validation
- Cross-reference documentation with implementation

## Phase 3: Bug Documentation & Prioritization

### 3.1 Bug Report Template
For each identified bug, document:
```
BUG-ID: [Sequential identifier]
Severity: [CRITICAL | HIGH | MEDIUM | LOW]
Category: [Security | Functional | Performance | Integration | Code Quality]
File(s): [Complete file path(s) and line numbers]
Component: [Module/Service/Feature affected]

Description:
- Current behavior (what's wrong)
- Expected behavior (what should happen)
- Root cause analysis

Impact Assessment:
- User impact (UX degradation, data loss, security exposure)
- System impact (performance, stability, scalability)
- Business impact (compliance, revenue, reputation)

Reproduction Steps:
1. [Step-by-step instructions]
2. [Include test data/conditions if needed]
3. [Expected vs actual results]

Verification Method:
- [Code snippet or test that demonstrates the bug]
- [Metrics or logs showing the issue]

Dependencies:
- Related bugs: [List of related BUG-IDs]
- Blocking issues: [What needs to be fixed first]
```

### 3.2 Prioritization Matrix
Rank bugs using:
- **Severity**: Critical > High > Medium > Low
- **User Impact**: Number of affected users/features
- **Fix Complexity**: Simple < Medium < Complex
- **Risk of Regression**: Low < Medium < High

## Phase 4: Fix Implementation

### 4.1 Fix Strategy
**For each bug:**
1. Create isolated fix branch (if using version control)
2. Write failing test FIRST (TDD approach)
3. Implement minimal, focused fix
4. Verify test passes
5. Run regression tests
6. Update documentation if needed

### 4.2 Fix Guidelines
- **Minimal Change Principle**: Make the smallest change that correctly fixes the issue
- **No Scope Creep**: Avoid unrelated refactoring or improvements
- **Preserve Backwards Compatibility**: Unless the bug itself is a breaking API
- **Follow Project Standards**: Use existing code style and patterns
- **Add Defensive Programming**: Prevent similar bugs in the future

### 4.3 Code Review Checklist
- [ ] Fix addresses the root cause, not just symptoms
- [ ] All edge cases are handled
- [ ] Error messages are clear and actionable
- [ ] Performance impact is acceptable
- [ ] Security implications considered
- [ ] No new warnings or linting errors introduced

## Phase 5: Testing & Validation

### 5.1 Test Requirements
**For EVERY fixed bug, provide:**
1. **Unit Test**: Isolated test for the specific fix
2. **Integration Test**: If bug involves multiple components
3. **Regression Test**: Ensure fix doesn't break existing functionality
4. **Edge Case Tests**: Cover related boundary conditions

### 5.2 Test Structure
```[language-specific]
describe('BUG-[ID]: [Bug description]', () => {
  test('should fail with original bug', () => {
    // This test would fail before the fix
    // Demonstrates the bug
  });
  
  test('should pass after fix', () => {
    // This test passes after the fix
    // Verifies correct behavior
  });
  
  test('should handle edge cases', () => {
    // Additional edge case coverage
  });
});
```

### 5.3 Validation Steps
1. Run full test suite: `[npm test | pytest | go test ./... | mvn test | etc.]`
2. Check code coverage changes
3. Run static analysis tools
4. Verify performance benchmarks (if applicable)
5. Test in different environments (if possible)

## Phase 6: Documentation & Reporting

### 6.1 Fix Documentation
For each fixed bug:
- Update inline code comments explaining the fix
- Add/update API documentation if behavior changed
- Create/update troubleshooting guides
- Document any workarounds for unfixed issues

### 6.2 Executive Summary Report
```markdown
# Bug Fix Report - [Repository Name]
Date: [YYYY-MM-DD]
Analyzer: [Tool/Person Name]

## Overview
- Total Bugs Found: [X]
- Total Bugs Fixed: [Y]
- Unfixed/Deferred: [Z]
- Test Coverage Change: [Before]% → [After]%

## Critical Findings
[List top 3-5 most critical bugs found and fixed]

## Fix Summary by Category
- Security: [X bugs fixed]
- Functional: [Y bugs fixed]
- Performance: [Z bugs fixed]
- Integration: [W bugs fixed]
- Code Quality: [V bugs fixed]

## Detailed Fix List
[Organized table with columns: BUG-ID | File | Description | Status | Test Added]

## Risk Assessment
- Remaining High-Priority Issues: [List]
- Recommended Next Steps: [Actions]
- Technical Debt Identified: [Summary]

## Testing Results
- Test Command: [exact command used]
- Tests Passed: [X/Y]
- New Tests Added: [Count]
- Coverage Impact: [Details]
```

### 6.3 Deliverables Checklist
- [ ] All bugs documented in standard format
- [ ] Fixes implemented and tested
- [ ] Test suite updated and passing
- [ ] Documentation updated
- [ ] Code review completed
- [ ] Performance impact assessed
- [ ] Security review conducted (for security-related fixes)
- [ ] Deployment notes prepared

## Phase 7: Continuous Improvement

### 7.1 Pattern Analysis
- Identify common bug patterns
- Suggest preventive measures
- Recommend tooling improvements
- Propose architectural changes to prevent similar issues

### 7.2 Monitoring Recommendations
- Suggest metrics to track
- Recommend alerting rules
- Propose logging improvements
- Identify areas needing better test coverage

## Constraints & Best Practices

1. **Never compromise security** for simplicity
2. **Maintain audit trail** of all changes
3. **Follow semantic versioning** if fixes change API
4. **Respect rate limits** when testing external services
5. **Use feature flags** for high-risk fixes (if applicable)
6. **Consider rollback strategy** for each fix
7. **Document assumptions** made during analysis

## Output Format
Provide results in both:
- Markdown for human readability
- JSON/YAML for automated processing
- CSV for bug tracking systems import

## Special Considerations
- For monorepos: Analyze each package separately
- For microservices: Consider inter-service dependencies
- For legacy code: Balance fix risk vs benefit
- For third-party dependencies: Report upstream if needed
