#!/usr/bin/env bash
set -euo pipefail

ROOT_MODULE="${1:-ReviewReadyTemplate}"
THEOREMS_FILE="${2:-Audit/flagship-theorems.txt}"
OUT_FILE="${3:-Audit/AxiomAudit.generated.lean}"
REPORT_FILE="${4:-Audit/axioms-report.txt}"

{
  printf 'import %s\n\n' "$ROOT_MODULE"
  while IFS= read -r theorem_name; do
    [[ -z "$theorem_name" ]] && continue
    [[ "$theorem_name" =~ ^# ]] && continue
    printf '#print axioms %s\n' "$theorem_name"
  done < "$THEOREMS_FILE"
} > "$OUT_FILE"

lake env lean "$OUT_FILE" | tee "$REPORT_FILE"
