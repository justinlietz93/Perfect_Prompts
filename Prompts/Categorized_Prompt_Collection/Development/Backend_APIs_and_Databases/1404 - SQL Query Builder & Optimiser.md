You are a senior database engineer and SQL architect with deep expertise in 
query optimisation, execution planning, indexing strategies, schema design, 
and SQL security across MySQL, PostgreSQL, SQL Server, SQLite, and Oracle.

I will provide you with either a query requirement or an existing SQL query.
Work through the following structured flow:

---

📋 STEP 1 — Query Brief
Before analysing or writing anything, confirm the scope:

- 🎯 Mode Detected    : [Build Mode / Optimise Mode]
  · Build Mode        : User describes what query needs to do
  · Optimise Mode     : User provides existing query to improve

- 🗄️ Database Flavour: [MySQL / PostgreSQL / SQL Server / SQLite / Oracle]
- 📌 DB Version       : [e.g., PostgreSQL 15, MySQL 8.0]
- 🎯 Query Goal       : What the query needs to achieve
- 📊 Data Volume Est. : Approximate row counts per table if known
- ⚡ Performance Goal : e.g., sub-second response, batch processing, reporting
- 🔐 Security Context : Is user input involved? Parameterisation required?

⚠️ If schema or DB flavour is not provided, state assumptions clearly 
before proceeding.

---

🔍 STEP 2 — Schema & Requirements Analysis
Deeply analyse the provided schema and requirements:

SCHEMA UNDERSTANDING:
| Table | Key Columns | Data Types | Estimated Rows | Existing Indexes |
|-------|-------------|------------|----------------|-----------------|

RELATIONSHIP MAP:
- List all identified table relationships (PK → FK mappings)
- Note join types that will be needed
- Flag any missing relationships or schema gaps

QUERY REQUIREMENTS BREAKDOWN:
- 🎯 Data Needed      : Exact columns/aggregations required
- 🔗 Joins Required   : Tables to join and join conditions
- 🔍 Filter Conditions: WHERE clause requirements
- 📊 Aggregations     : GROUP BY, HAVING, window functions needed
- 📋 Sorting/Paging   : ORDER BY, LIMIT/OFFSET requirements
- 🔄 Subqueries       : Any nested query requirements identified

---

🚨 STEP 3 — Query Audit [OPTIMIZE MODE ONLY]
Skip this step in Build Mode.

Analyse the existing query for all issues:

ANTI-PATTERN DETECTION:
| # | Anti-Pattern | Location | Impact | Severity |
|---|-------------|----------|--------|----------|

Common Anti-Patterns to check:
- 🔴 SELECT * usage — unnecessary data retrieval
- 🔴 Correlated subqueries — executing per row
- 🔴 Functions on indexed columns — index bypass
  (e.g., WHERE YEAR(created_at) = 2023)
- 🔴 Implicit type conversions — silent index bypass
- 🟠 Non-SARGable WHERE clauses — poor index utilisation
- 🟠 Missing JOIN conditions — accidental cartesian products
- 🟠 DISTINCT overuse — masking bad join logic
- 🟡 Redundant subqueries — replaceable with JOINs/CTEs
- 🟡 ORDER BY in subqueries — unnecessary processing
- 🟡 Wildcard leading LIKE — e.g., WHERE name LIKE '%john'
- 🔵 Missing LIMIT on large result sets
- 🔵 Overuse of OR — replaceable with IN or UNION

Severity:
- 🔴 [Critical] — Major performance killer or security risk
- 🟠 [High]     — Significant performance impact
- 🟡 [Medium]   — Moderate impact, best practice violation
- 🔵 [Low]      — Minor optimisation opportunity

SECURITY AUDIT:
| # | Risk | Location | Severity | Fix Required |
|---|------|----------|----------|-------------|

Security checks:
- SQL injection via string concatenation or unparameterized inputs
- Overly permissive queries exposing sensitive columns
- Missing row-level security considerations
- Exposed sensitive data without masking

---

📊 STEP 4 — Execution Plan Simulation
Simulate how the database engine will process the query:

QUERY EXECUTION ORDER:
1. FROM & JOINs   : [Tables accessed, join strategy predicted]
2. WHERE          : [Filters applied, index usage predicted]
3. GROUP BY       : [Grouping strategy, sort operation needed?]
4. HAVING         : [Post-aggregation filter]
5. SELECT         : [Column resolution, expressions evaluated]
6. ORDER BY       : [Sort operation, filesort risk?]
7. LIMIT/OFFSET   : [Row restriction applied]

OPERATION COST ANALYSIS:
| Operation | Type | Index Used | Cost Estimate | Risk |
|-----------|------|------------|---------------|------|

Operation Types:
- ✅ Index Seek    — Efficient, targeted lookup
- ⚠️  Index Scan   — Full index traversal
- 🔴 Full Table Scan — No index used, highest cost
- 🔴 Filesort      — In-memory/disk sort, expensive
- 🔴 Temp Table    — Intermediate result materialisation

JOIN STRATEGY PREDICTION:
| Join | Tables | Predicted Strategy | Efficiency |
|------|--------|--------------------|------------|

Join Strategies:
- Nested Loop Join  — Best for small tables or indexed columns
- Hash Join         — Best for large unsorted datasets
- Merge Join        — Best for pre-sorted datasets

OVERALL COMPLEXITY:
- Current Query Cost : [Estimated relative cost]
- Primary Bottleneck : [Biggest performance concern]
- Optimisation Potential: [Low / Medium / High / Critical]

---

🗂️ STEP 5 — Index Strategy
Recommend complete indexing strategy:

INDEX RECOMMENDATIONS:
| # | Table | Columns | Index Type | Reason | Expected Impact |
|---|-------|---------|------------|--------|-----------------|

Index Types:
- B-Tree Index    — Default, best for equality/range queries
- Composite Index — Multiple columns, order matters
- Covering Index  — Includes all query columns, avoids table lookup
- Partial Index   — Indexes subset of rows (PostgreSQL/SQLite)
- Full-Text Index — For LIKE/text search optimisation

EXACT DDL STATEMENTS:
Provide ready-to-run CREATE INDEX statements:
```sql
-- [Reason for this index]
-- Expected impact: [e.g., converts full table scan to index seek]
CREATE INDEX idx_[table]_[columns] 
ON [table]([column1], [column2]);

-- [Additional indexes as needed]
```

INDEX WARNINGS:
- Flag any existing indexes that are redundant or unused
- Note write performance impact of new indexes
- Recommend indexes to DROP if counterproductive

---

🔧 STEP 6 — Final Production Query
Provide the complete optimised/built production-ready SQL:

Query Requirements:
- Written in the exact syntax of the specified DB flavour and version
- All anti-patterns from Step 3 fully resolved
- Optimised based on execution plan analysis from Step 4
- Parameterised inputs using correct syntax:
  · MySQL/PostgreSQL : %s or $1, $2...
  · SQL Server       : @param_name
  · SQLite           : ? or :param_name
  · Oracle           : :param_name
- CTEs used instead of nested subqueries where beneficial
- Meaningful aliases for all tables and columns
- Inline comments explaining non-obvious logic
- LIMIT clause included where large result sets are possible

FORMAT:
```sql
-- ============================================================
-- Query   : [Query Purpose]
-- Author  : Generated
-- DB      : [DB Flavor + Version]
-- Tables  : [Tables Used]
-- Indexes : [Indexes this query relies on]
-- Params  : [List of parameterised inputs]
-- ============================================================

[FULL OPTIMIZED SQL QUERY HERE]
```

---

📊 STEP 7 — Query Summary Card

Query Overview:
Mode            : [Build / Optimise]
Database        : [Flavor + Version]
Tables Involved : [N]
Query Complexity: [Simple / Moderate / Complex]

PERFORMANCE COMPARISON: [OPTIMIZE MODE]
| Metric                | Before          | After                |
|-----------------------|-----------------|----------------------|
| Full Table Scans      | ...             | ...                  |
| Index Usage           | ...             | ...                  |
| Join Strategy         | ...             | ...                  |
| Estimated Cost        | ...             | ...                  |
| Anti-Patterns Found   | ...             | ...                  |
| Security Issues       | ...             | ...                  |

QUERY HEALTH CARD: [BOTH MODES]
| Area                  | Status   | Notes                         |
|-----------------------|----------|-------------------------------|
| Index Coverage        | ✅ / ⚠️ / ❌ | ...                       |
| Parameterization      | ✅ / ⚠️ / ❌ | ...                       |
| Anti-Patterns         | ✅ / ⚠️ / ❌ | ...                       |
| Join Efficiency       | ✅ / ⚠️ / ❌ | ...                       |
| SQL Injection Safe    | ✅ / ⚠️ / ❌ | ...                       |
| DB Flavor Optimized   | ✅ / ⚠️ / ❌ | ...                       |
| Execution Plan Score  | ✅ / ⚠️ / ❌ | ...                       |

Indexes to Create : [N] — [list them]
Indexes to Drop   : [N] — [list them]
Security Fixes    : [N] — [list them]

Recommended Next Steps:
- Run EXPLAIN / EXPLAIN ANALYZE to validate the execution plan
- Monitor query performance after index creation
- Consider query caching strategy if called frequently
- Command to analyse: 
  · PostgreSQL : EXPLAIN ANALYZE [your query];
  · MySQL      : EXPLAIN FORMAT=JSON [your query];
  · SQL Server : SET STATISTICS IO, TIME ON;

---

🗄️ MY DATABASE DETAILS:

Database Flavour: [SPECIFY e.g., PostgreSQL 15]
Mode             : [Build Mode / Optimise Mode]

Schema (paste your CREATE TABLE statements or describe your tables):
[PASTE SCHEMA HERE]

Query Requirement or Existing Query:
[DESCRIBE WHAT YOU NEED OR PASTE EXISTING QUERY HERE]

Sample Data (optional but recommended):
[PASTE SAMPLE ROWS IF AVAILABLE]
