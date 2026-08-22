# Version-Control Rules

## Canonical root

Maintain exactly one active project root.

Suggested naming:

`NOVEL_SLUG_CANONICAL_YYYYMMDD_vN/`

## Structural changes

A structural change includes:

- changing the governing law / Frame Lock
- changing the reader-experience arc
- changing major character architecture
- adding/removing macro movements
- changing frame/timeline logic
- changing the ending obligation
- changing the role of a major source artifact

Record these in `CHANGELOG.md`.

## Draft changes

Normal prose edits do not require a new canonical version by themselves.

Create a new canonical version when the project's **meaningful structural state** changes or when a milestone deserves a frozen recovery point.

## Archive rule

Old canonical versions go in `/archive_previous_versions/` or external version control. Do not edit them.

## No duplicate active bibles

One workbook is authoritative. Exports and snapshots are read-only derivatives.

## Status vocabulary

Use explicit status labels:

- PROPOSED — candidate idea, not yet adopted
- ACTIVE — current working decision
- LOCKED — change only with explicit reason
- DEPRECATED — superseded but retained for provenance

This prevents speculative scaffold text from silently becoming canon.
