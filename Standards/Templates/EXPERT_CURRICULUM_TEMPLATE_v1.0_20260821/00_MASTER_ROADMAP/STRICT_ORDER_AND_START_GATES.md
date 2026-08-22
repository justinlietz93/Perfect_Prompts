# Strict Order and Start Gates

This is the controlling human-readable progression document.

## Primary spine

Activate the primary groups in this order:

1. `01_{{GROUP_NAME}}`
2. `02_{{GROUP_NAME}}`
3. `03_{{GROUP_NAME}}`

A primary group stops controlling progression when its **core-pass exit gate** is met. Deepening and reference work may continue later without blocking the spine unless this curriculum explicitly states otherwise.

## Parallel branch activation

Parallel branches are not a second competing order. Each branch has an exact start gate.

| Branch | Earliest start gate | First active resource / task | Reason |
|---|---|---|---|
| `{{BRANCH}}` | `{{GATE}}` | `{{FIRST_STEP}}` | `{{WHY}}` |

## Targeted activation

If enabled in `CURRICULUM_SPEC.json`, advanced material may be opened early for a live problem only when the exact missing prerequisite is identified and repaired sufficiently for that narrow use.

Targeted activation does **not** mark the containing group complete.

## Recommended activation waves

Use waves only if they make the actual schedule clearer. They summarize the gate structure; they do not replace it.

- **Wave A** — `{{GROUPS}}`
- **Wave B** — `{{GROUPS}}`

## Single-thread fallback

When parallel study becomes counterproductive, follow:

`{{GROUP_ID}} → {{GROUP_ID}} → {{GROUP_ID}}`

The fallback must contain no prerequisite inversions.
