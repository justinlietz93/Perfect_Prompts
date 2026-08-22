<!-- **How to use:** Replace every `<PLACEHOLDER>` and delete optional sections you don’t need. Paste the whole thing into your analysis agent. -->

# EXHAUSTIVE ARCHITECTURE REVIEW & MAPPING — PROMPT TEMPLATE

**Mission**
Exhaustively analyze the `<PROJECT_NAME>` codebase and produce a layered architectural map from **high‑level (context, containers)** down to **low‑level (components, modules, hot paths)**. Output must be **complete, navigable, reproducible, and visually polished.**

---
<!-- Mini “Fill Sheet” (copy this block below for fast reuse) -->
### 0) Inputs (fill these)

* **Repo:** `<org>/<repo>`
* **Default branch:** `<main|master>`
* **Commit SHA for review:** `<sha>`
* **Languages/Frameworks:** `<python/node/go/java/...>`
* **Infra & external services:** `<dbs, caches, queues, vector/graph stores, LLM providers, search/index, cloud services>`
* **Primary runtime targets:** `<local/docker/k8s/serverless>`
* **Pipelines/Flows of interest (name each):**

  1. `<Pipeline A>`
  2. `<Pipeline B>`
  3. `<Pipeline C>`
* **Non‑functional priorities:** `<performance, reliability, security, privacy, cost, maintainability>`
* **Architecture ideals to check against:** `<Clean Architecture, modular monolith, microservices, hexagonal, CQRS, event‑driven, etc.>`

---

### 1) Output Package (exact files to produce)

```
docs/architecture/
  00_executive_summary.md
  01_context_c4.mmd                 # Mermaid C4 Context
  02_containers_c4.mmd              # Mermaid C4 Containers
  03_components_*.mmd               # Mermaid C4 Components (one per container)
  04_code_map.md                    # Key modules/classes with responsibilities
  05_dependency_graph.dot           # Graphviz imports/packages
  06_dependency_matrix.csv          # adjacency; cycles flagged
  07_runtime_sequence_*.mmd         # Sequence diagrams for hot paths & pipelines
  08_dataflow_*.mmd                 # End-to-end dataflow/storage/caches
  09_domain_model.mmd               # Entities/aggregates/value objects
  10_quality_gates.md               # smells, cycles, hotspots, coverage snapshot
  11_non_functionals.md             # perf, scalability, reliability, security, privacy
  12_operability.md                 # logging, tracing, metrics, config, feature flags
  13_refactor_plan.md               # roadmap (quick wins → strategic)
  14_arch_alignment.md              # gaps vs chosen architectural ideals
  15_pipelines/
     <pipelineA>.mmd                # activity + sequence + artifacts
     <pipelineB>.mmd
     <pipelineC>.mmd
  16_ux_touchpoints.md              # how APIs/CLI/jobs surface to product UX
  17_api_surface_openapi.json       # if present; else generated draft
  architecture-map.json             # machine-readable graph (schema below)
  assets/                           # rendered PNG/SVGs for all diagrams
```

---

### 2) Machine‑Readable Graph — `architecture-map.json` (JSON Schema)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Architecture Map",
  "type": "object",
  "required": ["system", "commit", "containers", "components"],
  "properties": {
    "system": { "type": "string" },
    "commit": { "type": "string" },
    "languages": { "type": "array", "items": { "type": "string" } },
    "containers": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "tech"],
        "properties": {
          "name": { "type": "string" },
          "tech": { "type": "string" },
          "responsibilities": { "type": "array", "items": { "type": "string" } },
          "deps": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    "components": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["container", "name", "path"],
        "properties": {
          "container": { "type": "string" },
          "name": { "type": "string" },
          "path": { "type": "string" },
          "deps": { "type": "array", "items": { "type": "string" } },
          "layer": { "type": "string", "enum": ["presentation","application","domain","infrastructure","common"] }
        }
      }
    },
    "pipelines": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name"],
        "properties": {
          "name": { "type": "string" },
          "stages": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["id", "title"],
              "properties": {
                "id": { "type": "string" },
                "title": { "type": "string" },
                "files": { "type": "array", "items": { "type": "string" } },
                "inputs": { "type": "array", "items": { "type": "string" } },
                "outputs": { "type": "array", "items": { "type": "string" } }
              }
            }
          },
          "entrypoints": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    "stores": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": { "type": "string" },
          "usage": { "type": "string" },
          "collections": { "type": "array", "items": { "type": "string" } },
          "tables": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    "integrations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "paths": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    "apis": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "type": { "type": "string", "enum": ["rest","grpc","graphql","cli","events"] },
          "endpoints": { "type": "array", "items": { "type": "string" } },
          "spec": {}
        }
      }
    },
    "metrics": {
      "type": "object",
      "properties": {
        "cycles": { "type": "array", "items": { "type": "array", "items": { "type": "string" } } },
        "hotspots": { "type": "array", "items": { "type": "string" } },
        "test_coverage": {
          "type": "object",
          "properties": {
            "overall": { "type": "number" },
            "by_module": { "type": "object", "additionalProperties": { "type": "number" } }
          }
        }
      }
    },
    "risks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "title": { "type": "string" },
          "severity": { "type": "string", "enum": ["H","M","L"] },
          "where": { "type": "string" },
          "rationale": { "type": "string" }
        }
      }
    }
  }
}
```

---

### 3) Process & Method (what to do)

**3.1 Inventory & Footprint**

* Detect languages, build tools, entrypoints (API routes, CLIs, workers).
* Map external services and secrets. Produce tables in `04_code_map.md`.

**3.2 Static Structure (imports & modules)**

* Build an import/dependency graph using AST (not regex).
* Compute: strongly connected components (cycles), fan‑in/fan‑out, instability.
* Export to `05_dependency_graph.dot` + `06_dependency_matrix.csv` and annotate cycles.

**3.3 C4 Views**

* **Context:** users, external systems.
* **Containers:** API, workers, pipelines/orchestrators, embedding/indexers, storage (SQL/vector/graph), web UI.
* **Components:** controllers, use‑cases/services, domain, adapters.
* Render **Mermaid** diagrams; export SVG/PNG to `assets/`.

**3.4 Domain Model**

* Identify entities/value objects/aggregates and invariants. Output `09_domain_model.mmd`.

**3.5 Runtime & Hot Paths**

* Choose 3–5 hot paths (e.g., “Submit bundle → Pipeline → Result”).
* Generate `07_runtime_sequence_*.mmd` and `08_dataflow_*.mmd` covering async boundaries, caches, vector/graph queries, and notable latencies.

**3.6 Pipelines (deep dive)**

* For each named pipeline (§0), produce:

  * **Activity diagram** (stages & artifacts).
  * **Sequence diagram** (calls across components/services).
  * **Inputs/Outputs** table per stage, with file/code references and configuration knobs.

**3.7 Non‑functionals & Operability**

* **Performance:** critical O‑notation, token/latency hotspots, batching/concurrency.
* **Reliability:** retries, idempotency, delivery semantics (at‑least/exactly‑once).
* **Security/Privacy:** secret handling, PII, model/data egress, rate limits.
* **Observability:** logs/metrics/traces, correlation IDs, provenance/versioning.
* **Reproducibility:** seeds, prompt & schema versioning, artifact hashing.

**3.8 Architectural Alignment**

* Check against chosen ideals (§0): boundary discipline, dependency direction, file size caps, adapter separation.
* Document violations with code paths and suggested ports/adapters.

**3.9 Refactor Plan**

* **Quick wins (1–2 days)**: break cycles, config normalization, error taxonomy, log correlation IDs.
* **Medium (1–2 sprints)**: extract ports/adapters, stabilize module boundaries, test harnesses.
* **Strategic**: split modules or consolidate; performance architecture; data/knowledge graph unification.

---

### 4) Visual & UX Standards (craftsmanship rules)

* Export **both SVG and PNG** for every diagram. Legible at **125% zoom** minimum.
* Mermaid themes: provide **light and dark** variants; include a legend and last‑updated + commit SHA.
* Use consistent shapes per layer (e.g., hex for external, rounded for containers, rectangles for components).
* Include linkbacks to source files in `04_code_map.md`.

---

### 5) GitHub Automation (optional)

If repo permissions allow, open a PR that adds all artifacts.

* **Branch:** `architecture-map/<YYYY-MM-DD>`
* **PR title:** `<PROJECT_NAME>: Architectural Review & Layered Map`
* **PR body:** summary + screenshots + checklist of artifacts.

---

### 6) Constraints

* Read‑only analysis; do not change app logic unless explicitly asked.
* No sensitive data exfiltration.
* Deterministic generation (seeded).
* No chain‑of‑thought in artifacts—use concise summaries and diagrams.

---

### 7) Scoring & Quality Gates

Produce a rubric (0–5) for:

* Architecture clarity
* Boundary discipline
* Pipeline separability
* Observability & operability
* Reproducibility & data provenance
* Security basics
* Performance hygiene
* Test depth

List **top 10 risks** with severity and mitigation.

---

### 8) Acceptance Criteria (must pass)

1. `docs/architecture/` contains all files in §1; diagrams render in both themes.
2. `architecture-map.json` validates against schema; counts match codebase.
3. At least **one** complete C4 stack (Context → Containers → Components) and **three** runtime sequences.
4. Dependency graph identifies cycles and proposes specific breaks.
5. Non‑functional analysis includes measurable recommendations with likely impact.
6. Refactor plan is prioritized with effort estimates and owners (if CODEOWNERS exists).
7. PR opened (or ZIP delivered) with screenshots and executive summary.
