# DUAL_PLANE_ARCHITECTURE_STANDARDS.md

**Status:** DRAFT v0.1
**Owners:** Engine Architecture WG
**Last Updated:** 2025-10-27
**Applies To:** Two-language, symbiotic systems (e.g., Python + C++/GPU) targeting instrument-grade performance and developer velocity.
**Notes:** Modeled to match the layout of `HEXAGONAL_ARCHITECTURE_STANDARDS.md` for drop-in consistency. 

---

### Overview

This document defines a **Dual Plane Architecture** (DPA) for engines and simulation systems that combine a **control-plane** (Python) with a **data-plane** (C++/GPU). The control-plane decides *what* and *when* via orchestration and policy; the data-plane executes *how* and *fast* via compiled kernels and GPU passes. Core properties:

* **Few, fat ports (FFI)** with **chunked** data exchange (SoA, zero-copy/memoryview)
* **Microplans** (code-as-data) compiled per frame by the control-plane and executed atomically by the data-plane
* **Sealed core** for determinism & ABI stability; **replaceable adapters** for GPU/physics/audio/net
* **Determinism-first** loop with explicit ordering; golden-image & replay testing baked in

---

### EXAMPLE ONLY Project Map of a Dual Plane engine using DPA

```text
dual-plane-engine/
├─ pyproject.toml
├─ CMakeLists.txt
├─ README.md
├─ src/
│  ├─ control_plane/                     # Python (authoring/orchestration/policy)
│  │  ├─ domain/                         # ECS schemas (dataclasses), scenes, events, time
│  │  ├─ application/                    # schedulers, use-cases, asset pipeline orchestration
│  │  ├─ plans/                          # microplan builders (render/physics/audio)
│  │  ├─ adapters/                       # DTO mappers, serializers, FFI bridges
│  │  └─ cli/                            # dev console, cook, package
│  ├─ data_plane/                        # Native (C++/GPU)
│  │  ├─ runtime/                        # job system, arenas, command queues
│  │  ├─ gpu/                            # device, framegraph executor, resource allocators
│  │  ├─ physics/                        # broadphase/narrowphase, solvers
│  │  └─ audio/                          # mixer, spatializer, DSP
│  ├─ ports/                             # IDL-generated stubs (Python) + headers (C++)
│  └─ editor/                            # Qt/PySide host + ImGui overlay
├─ tools/                                # cookers, validators, golden-image runner
├─ adr/                                  # architecture decision records
└─ tests/
   ├─ unit/                              
   ├─ contract/ports/                    # adapter contract tests
   ├─ integration/                       # adapters with real backends
   ├─ golden_images/                     # renderer proofs
   └─ determinism/                       # replay+hash proofs
```

---

### Dual Plane Architecture Implementation

#### Core Principles

* **Two-Plane Separation:** Python = **control-plane** (policy/orchestration); C++/GPU = **data-plane** (execution/perf).
* **Ports & Adapters:** All cross-plane interaction goes through **versioned ports** with **code-generated stubs**.
* **Microplans:** Control-plane emits immutable **render/physics/audio microplans** per frame; data-plane executes them atomically.
* **Few, Fat Calls:** ≤ 10 FFI calls per frame total (typical: `execute_render`, `step_physics`, `mix_audio`, `sync_transforms`).
* **Determinism-First:** Fixed-step tick; explicit phase order; nondeterministic features are opt-in and fenced.
* **Truthy Defaults:** Neutral rendering, honest physics, predictable input; taste added via presets, not hardwired heuristics.
* **Observability:** Every pass/system returns timings and counters; journals are schema-versioned.

---

### Layer Structure

1. **Sealed Core (Data-Plane Runtime)**

   * **Responsibilities:** ECS storage (archetype SoA), handle tables, framegraph execution, physics/audio kernels, job system
   * **Rules:** ABI-stable layouts; no modularity here without ADR; memory via arenas/slotmaps; zero allocations in hot path

2. **Control-Plane (Python)**

   * **Responsibilities:** Orchestration, policy (AI utility/BT/GOAP), editor automation, asset pipeline, plan building
   * **Rules:** Never per-entity per-frame FFI; batch requests; treat data-plane as a fast function

3. **Ports (IDL-Defined Contracts)**

   * **Responsibilities:** Language-neutral definitions for calls & DTO/SoA shapes; codegen to Python stubs & C++ headers
   * **Rules:** POD/SoA only; zero-copy buffers where possible; explicit versions & feature flags

4. **Adapters / Backends (Replaceable)**

   * **Categories:** GPU (OpenGL/Vulkan/Metal), Physics (Bullet/Jolt/etc.), Audio (OpenAL/FM middleware), Net (ENet/gRPC)
   * **Rules:** Adapters implement ports; contract-tested; hot-swap without touching control-plane

5. **Application (Use-Case Orchestration)**

   * **Responsibilities:** System scheduling, plan compilation, save/replay, editor live-link

6. **Editor & Tools**

   * **Responsibilities:** Panels (Hierarchy/Inspector/Profiler/FrameGraph), cook/validate, golden-image runner, determinism lab

7. **Configuration (Wiring/DI)**

   * **Responsibilities:** Port→adapter binding, environment selection, feature toggles

---

### Interfaces, Contracts, and API Requirements

* **Port Design Principles**

  * Ports are **data-plane verbs** with **POD/SoA** payloads: no Python objects.
  * Microplans are **opaque binaries** (render plan, physics batch) with version headers.
  * All ports return a **journal** (timings, counters, summaries) for policy decisions and profiling.

* **Dependency Direction (strictly enforced)**

  * `control_plane` → `ports` (stubs)
  * `data_plane` ↔ `ports` (headers)
  * `adapters` → `ports` and external libs
  * `editor/tools` → `control_plane` (never into `data_plane` directly)
  * Only **configuration** knows concrete adapters

* **Port Taxonomy (essential ports)**

  * **Render Port:** `execute_render(plan, draw_buckets) -> RenderJournal`
  * **Physics Port:** `step_physics(dt, substeps, rays, overlaps) -> PhysicsJournal`
  * **Audio Port:** `mix_audio(plan, emitters, listener) -> AudioJournal`
  * **Sync Port:** `sync_transforms(write_mask) -> TransformSoA` / `apply_transforms(SoA)`
  * **Net Port (opt):** `replicate(snapshot_in) -> snapshot_out`

* **Error Handling Strategy**

  * Port calls return **status codes** + **journal warnings**; no exceptions across FFI.
  * Adapters translate native errors to port statuses; control-plane escalates via policy.

* **Testing Strategy**

  * **Contract tests** per port; **adapter integration** with real backends; **golden-image** (render), **replay+hash** (determinism), **perf smoke** in CI.

---

### Dependency Flow

```
[ Editor / Tools ] → [ Control-Plane (Python) ] → [ Ports (IDL) ] → [ Data-Plane Runtime (C++/GPU) ]
           |                 |                         |                     |
         Assets          Plans/Policy              Stubs/Headers          Kernels/Passes
```

---

### External Integration Points

* New GPU/physics/audio backends are added by **implementing the port contracts** only; no control-plane edits.
* Import/cooking stages (glTF, KTX2, USD) live in control-plane; encoders/decoders may call native helpers via **aux ports**.

---

### Rules for AI Agents (that generate or modify code)

1. Generate/modify **ports first**, then adapters.
2. Never introduce per-entity per-frame FFI calls.
3. Prefer **SoA** buffers and **memoryview** returns for zero-copy reads.
4. Keep sealed-core structs (handles, transforms, framegraph resources) **unchanged** unless ADR approved.
5. Add **contract tests** whenever a port or adapter changes.

---

### Example Implementation (excerpt)

**Python (control-plane):**

```python
# build microplans and call into data-plane
r_journal = gpu.execute_render(framegraph_plan, draw_buckets)
p_journal = physics.step_physics(dt, substeps, rays_soa, overlaps_soa)

# policy decisions from summaries
for hit in p_journal.hits:
    score_crit_window(hit)
```

**C++ (data-plane port header, generated):**

```cpp
struct RenderIn { std::span<const std::byte> plan, draws; };
struct RenderOut { Timings timings; RenderStats stats; };
RenderOut execute_render(const RenderIn&);

struct PhysicsIn {
  float dt; uint8_t substeps;
  RaySoA rays; AabbSoA overlaps;
};
struct PhysicsOut { HitSoA hits; ContactsSummary contacts; Timings timings; };
PhysicsOut step_physics(const PhysicsIn&);
```

---

### AI Agent Development Guidelines

**Critical Rules**

* Respect **few, fat call** rule; batch or refuse fine-grained requests.
* Emit **microplans** as immutable blobs; never keep Python in inner loops.
* Generate **contract tests** for every port change.
* Favor **data→function** patterns (graphs compiled to micro-kernels).

**Code Review Checklist**

* [ ] No control-plane import of `data_plane` internals
* [ ] Ports use POD/SoA; zero Python objects across FFI
* [ ] Batch sizes & buffer strides documented and tested
* [ ] Journals include timings/counters with schema version
* [ ] Golden-image & determinism tests updated

---

### Architectural Concepts

* **Microplan:** Per-frame immutable plan (render/physics/audio) executed atomically.
* **FaaDG (Function-as-Data Graph):** Material/animation/AI graphs stored as typed DAGs; executor interprets or JITs into micro-kernels.
* **Sealed Core:** Generational handles, archetype SoA, framegraph resource model, event rings, math layouts.
* **Replaceable Adapters:** Swap GPU/physics/audio without touching control-plane.

---

### UI/UX Strategies (Editor)

* Dockable panels for **Hierarchy / Inspector / Profiler / FrameGraph**.
* **Live journals**: timings, culling, contacts; toggle overlays with zero-cost when disabled.
* Scripts hot-reload at **plan level** (rebuild microplans, not kernels).

---

### Performance Strategies (Speed & Power)

* **SoA everywhere**; vector-friendly strides; interleave only when proven.
* **Arenas & slotmaps**; no `new/delete` in hot path.
* **Batched FFI**; memoryviews for read-only snapshots; command buffers for mutations.
* **Plan JIT** (optional): cache micro-kernels by graph hash.
* **Frame budgets in CI** with failure thresholds.

---

### Memory Optimization & Safety

* **64-bit generational handles** (index|generation|world).
* **Archetype tables** with stable column order for transforms/velocities.
* **Lock-free rings** (SPSC) for events with epoch counters.
* **Strict lifetimes** (transient frame arenas vs persistent arenas).

---

### Logging Strategies

* **Per-pass/system timings** auto-collected into frame journals.
* **Port-level statuses** (enum + human message) instead of exceptions across FFI.
* **Correlation IDs** propagate through microplans/journals.

---

### Security Strategies

* **Sandboxed control-plane** (allowlist imports for user scripts).
* **Resource caps** at import/cook time with clear diagnostics.
* **Native safety**: RAII, bounds checks, ASan/UBSan in debug.

---

### Networking / API Strategies

* **Authoritative server** friendly: determinism + snapshot deltas in ports.
* **Relevance/phasing** decided in control-plane; serialization/compression native.

---

### Controller / Backend Logic Strategies

* Controllers (editor, CLI) stay thin: translate UX to **plans**, never to per-entity calls.
* Complex flows = **application orchestration** + **plan compilation**, not ad-hoc native calls.

---

### Data Activities & ACID Strategies

* **Unit of Work:** a tick is the transaction; rollback = replay last N ticks.
* **Outbox pattern** for cross-process telemetry; scene/save schemas versioned with migration scripts.

---

### Database Design & Optimizations (if used)

* Asset DB/cache adapters are replaceable; keep scene schemas domain-centric.
* Use **hash-addressed** cooked artifacts for immutability & cache hits.

---

### Source Control Strategies

* Sealed core & ports evolve via ADRs; **SemVer** on ports/microplan schemas.
* Adapters can iterate independently as long as they pass **contract tests**.

---

### CI/CD Strategies

* Matrix builds for native wheels; **cibuildwheel** for releases.
* CI gates: **golden-image**, **determinism/replay**, **port contracts**, **perf smoke**.
* Release artifacts: `engine-core`, `engine-editor`, adapter wheels.

---

### Engineering Approach: Inside-Out & Outside-In

* **Inside-Out:** Define sealed core + ports + microplan formats → build adapters.
* **Outside-In:** Start from render/physics/audio requirements → refine ports → map to core.
* Iterate with ADRs; never bypass the ports.

---

### Testing Strategies

* **Domain (control-plane):** pure unit tests (no FFI).
* **Ports:** contract tests & fuzz on parsers.
* **Adapters:** integration with real backends.
* **Renderer:** golden images with tolerances per platform.
* **Determinism:** replay+hash ECS hot columns across OSes.
* **Perf smoke:** budgets enforced in CI.

```
tests/
├─ unit/control_plane/
├─ contract/ports/
├─ integration/adapters/
├─ golden_images/
└─ determinism/
```

---

### Validation Domains & Best Combination

| Validation Domain   | Implementation Location | Strategy                          |
| ------------------- | ----------------------- | --------------------------------- |
| Tick determinism    | Data-plane runtime      | Replay & hash SoA columns         |
| Render correctness  | Ports + adapters        | Golden-image diffs (tolerances)   |
| Port contracts      | Ports                   | Contract tests + fuzz parsers     |
| Performance budgets | CI                      | Frame budgets, per-pass timings   |
| Editor correctness  | Control-plane           | Command/undo/redo snapshot tests  |
| Security            | Adapters                | Sandbox allowlists, resource caps |

---

#### Minimal Port Sketch (IDL → generated)

```yaml
api: 1
calls:
  - name: execute_render
    in:  { framegraph_plan: bytes, draw_buckets: bytes }
    out: { timings: timings_v1, stats: render_stats_v1 }

  - name: step_physics
    in:  { dt: f32, substeps: u8, rays: soa_ray_v1, overlaps: soa_aabb_v1 }
    out: { hits: soa_hit_v1, contacts: contacts_v1, timings: timings_v1 }
```

This template provides a **repeatable pattern** for multi-language engines: sealed performance core, chunky ports, code-as-data plans, and contract-tested adapters.
