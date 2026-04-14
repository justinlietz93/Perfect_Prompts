# State Snapshot JSON Schema — Reference

This document defines the exact schema for `01_state_snapshot.json`.
Every handoff package must produce a JSON file that validates against this schema.

---

## Full Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Session State Object",
  "type": "object",
  "required": ["meta", "domain", "status", "focus", "entities", "relationships", "decisions"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["timestamp", "session_scope", "depth", "urgency", "next_owner"],
      "properties": {
        "timestamp": {
          "type": "string",
          "description": "ISO 8601 timestamp of snapshot creation"
        },
        "session_scope": {
          "type": "string",
          "enum": ["ideation", "debugging", "refactoring", "architecture", "creative_writing", "research", "mixed"],
          "description": "Primary mode of the session"
        },
        "depth": {
          "type": "string",
          "enum": ["short", "deep_dive", "marathon"],
          "description": "Session length/complexity"
        },
        "urgency": {
          "type": "string",
          "enum": ["low", "medium", "critical"]
        },
        "next_owner": {
          "type": "string",
          "description": "Who picks this up next: user, ai, or a specific role name"
        },
        "quality_scores": {
          "type": "object",
          "properties": {
            "resumability": { "type": "integer", "minimum": 0, "maximum": 5 },
            "ambiguity_reduction": { "type": "integer", "minimum": 0, "maximum": 5 },
            "context_density": { "type": "integer", "minimum": 0, "maximum": 5 },
            "liminal_capture": { "type": "integer", "minimum": 0, "maximum": 5 },
            "completeness": { "type": "integer", "minimum": 0, "maximum": 5 },
            "total": { "type": "integer", "minimum": 0, "maximum": 25 }
          }
        }
      }
    },
    "domain": {
      "type": "string",
      "enum": ["software_engineering", "physics_math", "philosophy", "creative", "business_strategy", "mixed"],
      "description": "Primary knowledge domain"
    },
    "status": {
      "type": "string",
      "enum": ["stable", "volatile", "blocked", "complete"],
      "description": "stable = safe stopping point; volatile = mid-work, state may shift; blocked = waiting on something; complete = session goals met"
    },
    "focus": {
      "type": "object",
      "required": ["primary_topic", "cursor_position"],
      "properties": {
        "primary_topic": {
          "type": "string",
          "description": "The central subject of the session in plain language"
        },
        "active_files": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Files actively being worked on (paths or names)"
        },
        "cursor_position": {
          "type": "string",
          "description": "Conceptual location in the problem space. Not a file path — a plain-language description of where we are. E.g., 'Midway through deriving the commutation relations for the phase operator' or 'Have identified the race condition, need to determine if it's the mutex or the semaphore'"
        },
        "hot_paths": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Active lines of investigation that are promising"
        },
        "blockers": {
          "type": "array",
          "items": { "type": "string" },
          "description": "What's preventing progress"
        }
      }
    },
    "entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "type"],
        "properties": {
          "name": { "type": "string", "description": "Entity identifier" },
          "type": {
            "type": "string",
            "description": "Category: project, module, function, theorem, concept, person, file, variable, axiom, constraint, tool, dataset, etc."
          },
          "state": {
            "type": "string",
            "description": "Current condition: active, resolved, blocked, deprecated, proposed, rejected"
          },
          "definition": {
            "type": "string",
            "description": "Brief definition sufficient for a new agent to understand what this is"
          }
        }
      },
      "description": "Every significant noun in the session — exhaustive, not sampled"
    },
    "relationships": {
      "type": "object",
      "description": "Adjacency list. Keys are entity names, values are arrays of {target, relation} objects",
      "additionalProperties": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["target", "relation"],
          "properties": {
            "target": { "type": "string" },
            "relation": {
              "type": "string",
              "description": "Edge label: depends_on, derives_from, contradicts, extends, implements, blocks, replaces, relates_to, etc."
            }
          }
        }
      }
    },
    "decisions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["title", "chosen", "rationale"],
        "properties": {
          "title": { "type": "string" },
          "chosen": { "type": "string" },
          "alternatives": {
            "type": "array",
            "items": { "type": "string" }
          },
          "rationale": { "type": "string" },
          "confidence": {
            "type": "string",
            "enum": ["high", "medium", "low"]
          },
          "reversibility": {
            "type": "string",
            "enum": ["easy", "hard", "irreversible"]
          }
        }
      }
    },
    "sentiment": {
      "type": "object",
      "properties": {
        "tone": {
          "type": "string",
          "description": "Brief characterization: exploratory, focused, frustrated, triumphant, cautious, etc."
        },
        "frustration_level": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "0.0 = calm exploration, 1.0 = deeply blocked/frustrated"
        },
        "momentum": {
          "type": "string",
          "enum": ["accelerating", "steady", "decelerating", "stalled"],
          "description": "Direction of progress velocity"
        }
      }
    },
    "liminal": {
      "type": "object",
      "properties": {
        "assumptions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "claim": { "type": "string" },
              "confidence": { "type": "string", "enum": ["high", "medium", "low"] },
              "basis": { "type": "string", "description": "Why this was assumed true" }
            }
          }
        },
        "rejected_paths": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "idea": { "type": "string" },
              "reason_rejected": { "type": "string" }
            }
          }
        },
        "open_questions": {
          "type": "array",
          "items": { "type": "string" }
        },
        "intuitions": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Hunches and pattern-recognitions not yet formalized"
        }
      }
    },
    "top_risk": {
      "type": "string",
      "description": "The single most critical piece of missing or ambiguous context"
    }
  }
}
```

---

## Field Guidance

### `status` — Choosing the Right Value

| Status | When to use |
|--------|-------------|
| `stable` | Work is at a natural pause point. State is consistent. Safe to hand off. |
| `volatile` | Mid-operation. State may be inconsistent. The next agent needs to verify before proceeding. |
| `blocked` | Cannot proceed without external input (user decision, API key, missing data, etc.) |
| `complete` | Session goals fully achieved. Handoff is archival, not operational. |

### `cursor_position` — How to Write It

Bad: "Working on the code"
Bad: "src/main.py:42"
Good: "Debugging the race condition in sync_manager.py where the mutex lock doesn't release on timeout — have narrowed it to the finally block but haven't confirmed the fix"
Good: "Derived the commutation relations for the phase operator through step 4; step 5 requires choosing between the Weyl and Born-Jordan orderings"

The cursor position should let a new agent know *exactly where to pick up the thread*.

### `entities` — Completeness Standard

Every significant noun should appear. If in doubt, include it. A missing entity is
worse than an extra one. Each entity needs enough definition that someone with zero
session context can understand what it refers to.

### `relationships` — Edge Labels

Use precise, directional labels. The relationship `A -> depends_on -> B` means
A cannot proceed without B. Common labels:

- `depends_on` — A requires B
- `derives_from` — A is mathematically/logically derived from B
- `contradicts` — A and B cannot both be true
- `extends` — A builds on B
- `implements` — A is a concrete realization of B
- `blocks` — A prevents B from proceeding
- `replaces` — A supersedes B
- `relates_to` — A and B are connected but the relationship is informal
