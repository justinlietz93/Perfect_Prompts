# Repository Organization

Perfect Prompts previously grew around several implementation formats at the repository root. That made historical sense but caused the physical layout to answer "what format is this?" before "what kind of thing is this?"

v0.2 reorganizes the filesystem around artifact meaning.

## Root taxonomy

| Area | Contains |
|---|---|
| `Agent_Instructions/` | Persistent AGENTS-style behavioral instructions |
| `Guidelines/` | Cross-cutting guidance |
| `Methodologies/` | Higher-level methods such as Guided Autonomy and emergence-based design |
| `Personas/` | Role definitions, grouped by representation/target system |
| `Prompts/` | Prompt templates, portable forms, and runtime bindings |
| `Rules/` | Scoped technical/scientific/domain rulesets |
| `Skills/` | Procedural skill packages and supporting files |
| `Standards/` | APEX, architecture, NASA, and research standards |
| `External_References/` | Separately maintained/reference libraries and submodules |
| `Application/` | Optional desktop application implementation |

## Prompt organization

`Prompts/` intentionally preserves two different reuse modes:

```text
Prompts/
├── Templates/
├── Portable/
│   ├── Plaintext/
│   ├── Structured_Text/
│   └── JSON/
└── Runtime_Bindings/
    ├── Python/
    ├── TypeScript/
    ├── Rust/
    └── Go/
```

Runtime-specific trees remain intact because embedded prompt implementations can legitimately differ in API shape, escaping, types, examples, and integration details. The reorganization does not force them into an artificial one-file-per-concept abstraction.

## Path-only edits

Where project-authored prompt templates contained direct links to the relocated APEX standard, those paths were updated to `Standards/APEX/APEX_STANDARDS.md`. Go documentation/example import paths were likewise adjusted to their new runtime-binding location. Those edits repair navigation after the move; they do not attempt to modernize the underlying prompt semantics.
