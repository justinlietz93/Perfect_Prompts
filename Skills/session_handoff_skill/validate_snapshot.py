#!/usr/bin/env python3
"""
Validate a session state snapshot JSON file against the handoff schema.

Usage:
    python validate_snapshot.py <path_to_json>

Exits 0 on valid, 1 on invalid with diagnostic output.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

REQUIRED_TOP_LEVEL = ["meta", "domain", "status", "focus", "entities", "relationships", "decisions"]
VALID_DOMAINS = ["software_engineering", "physics_math", "philosophy", "creative", "business_strategy", "mixed"]
VALID_STATUSES = ["stable", "volatile", "blocked", "complete"]
VALID_SCOPES = ["ideation", "debugging", "refactoring", "architecture", "creative_writing", "research", "mixed"]
VALID_DEPTHS = ["short", "deep_dive", "marathon"]
VALID_URGENCIES = ["low", "medium", "critical"]
VALID_CONFIDENCES = ["high", "medium", "low"]
VALID_REVERSIBILITIES = ["easy", "hard", "irreversible"]
VALID_MOMENTA = ["accelerating", "steady", "decelerating", "stalled"]


def validate(data: dict) -> list[str]:
    """Return list of validation errors. Empty list = valid."""
    errors = []

    # Top-level required fields
    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            errors.append(f"Missing required top-level field: '{field}'")

    if errors:
        return errors  # Can't validate further without structure

    # --- meta ---
    meta = data.get("meta", {})
    if not isinstance(meta, dict):
        errors.append("'meta' must be an object")
    else:
        for req in ["timestamp", "session_scope", "depth", "urgency", "next_owner"]:
            if req not in meta:
                errors.append(f"Missing required field in meta: '{req}'")

        if "timestamp" in meta:
            try:
                datetime.fromisoformat(meta["timestamp"].replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                errors.append(f"meta.timestamp is not valid ISO 8601: '{meta.get('timestamp')}'")

        if meta.get("session_scope") and meta["session_scope"] not in VALID_SCOPES:
            errors.append(f"meta.session_scope '{meta['session_scope']}' not in {VALID_SCOPES}")

        if meta.get("depth") and meta["depth"] not in VALID_DEPTHS:
            errors.append(f"meta.depth '{meta['depth']}' not in {VALID_DEPTHS}")

        if meta.get("urgency") and meta["urgency"] not in VALID_URGENCIES:
            errors.append(f"meta.urgency '{meta['urgency']}' not in {VALID_URGENCIES}")

        # Quality scores
        qs = meta.get("quality_scores", {})
        if qs:
            for score_name in ["resumability", "ambiguity_reduction", "context_density", "liminal_capture", "completeness"]:
                val = qs.get(score_name)
                if val is not None and (not isinstance(val, int) or val < 0 or val > 5):
                    errors.append(f"meta.quality_scores.{score_name} must be integer 0-5, got: {val}")
            total = qs.get("total")
            if total is not None and (not isinstance(total, int) or total < 0 or total > 25):
                errors.append(f"meta.quality_scores.total must be integer 0-25, got: {total}")

    # --- domain ---
    if data.get("domain") not in VALID_DOMAINS:
        errors.append(f"domain '{data.get('domain')}' not in {VALID_DOMAINS}")

    # --- status ---
    if data.get("status") not in VALID_STATUSES:
        errors.append(f"status '{data.get('status')}' not in {VALID_STATUSES}")

    # --- focus ---
    focus = data.get("focus", {})
    if not isinstance(focus, dict):
        errors.append("'focus' must be an object")
    else:
        if "primary_topic" not in focus:
            errors.append("Missing focus.primary_topic")
        if "cursor_position" not in focus:
            errors.append("Missing focus.cursor_position")
        elif len(focus.get("cursor_position", "")) < 20:
            errors.append("focus.cursor_position is suspiciously short — should be a detailed description of conceptual location")

    # --- entities ---
    entities = data.get("entities", [])
    if not isinstance(entities, list):
        errors.append("'entities' must be an array")
    else:
        entity_names = set()
        for i, ent in enumerate(entities):
            if not isinstance(ent, dict):
                errors.append(f"entities[{i}] must be an object")
                continue
            if "name" not in ent:
                errors.append(f"entities[{i}] missing required field 'name'")
            else:
                entity_names.add(ent["name"])
            if "type" not in ent:
                errors.append(f"entities[{i}] missing required field 'type'")

        if len(entities) < 3:
            errors.append(f"Only {len(entities)} entities found — most sessions should have more. Check for missing concepts.")

    # --- relationships ---
    rels = data.get("relationships", {})
    if not isinstance(rels, dict):
        errors.append("'relationships' must be an object (adjacency list)")
    else:
        all_rel_names = set(rels.keys())
        for source, targets in rels.items():
            if not isinstance(targets, list):
                errors.append(f"relationships['{source}'] must be an array")
                continue
            for j, edge in enumerate(targets):
                if not isinstance(edge, dict):
                    errors.append(f"relationships['{source}'][{j}] must be an object")
                    continue
                if "target" not in edge:
                    errors.append(f"relationships['{source}'][{j}] missing 'target'")
                if "relation" not in edge:
                    errors.append(f"relationships['{source}'][{j}] missing 'relation'")

    # --- decisions ---
    decisions = data.get("decisions", [])
    if not isinstance(decisions, list):
        errors.append("'decisions' must be an array")
    else:
        for i, dec in enumerate(decisions):
            if not isinstance(dec, dict):
                errors.append(f"decisions[{i}] must be an object")
                continue
            for req in ["title", "chosen", "rationale"]:
                if req not in dec:
                    errors.append(f"decisions[{i}] missing required field '{req}'")
            if dec.get("confidence") and dec["confidence"] not in VALID_CONFIDENCES:
                errors.append(f"decisions[{i}].confidence '{dec['confidence']}' not in {VALID_CONFIDENCES}")
            if dec.get("reversibility") and dec["reversibility"] not in VALID_REVERSIBILITIES:
                errors.append(f"decisions[{i}].reversibility '{dec['reversibility']}' not in {VALID_REVERSIBILITIES}")

    # --- sentiment (optional but validated if present) ---
    sentiment = data.get("sentiment")
    if sentiment:
        if not isinstance(sentiment, dict):
            errors.append("'sentiment' must be an object")
        else:
            fl = sentiment.get("frustration_level")
            if fl is not None and (not isinstance(fl, (int, float)) or fl < 0 or fl > 1):
                errors.append(f"sentiment.frustration_level must be 0.0-1.0, got: {fl}")
            if sentiment.get("momentum") and sentiment["momentum"] not in VALID_MOMENTA:
                errors.append(f"sentiment.momentum '{sentiment['momentum']}' not in {VALID_MOMENTA}")

    # --- top_risk (optional but encouraged) ---
    if "top_risk" not in data:
        errors.append("[WARNING] 'top_risk' field is missing — strongly recommended")

    return errors


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_state_snapshot.json>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: File not found: {path}")
        sys.exit(1)

    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)

    errors = validate(data)
    warnings = [e for e in errors if e.startswith("[WARNING]")]
    hard_errors = [e for e in errors if not e.startswith("[WARNING]")]

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  {w}")

    if hard_errors:
        print("VALIDATION FAILED:")
        for e in hard_errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        entity_count = len(data.get("entities", []))
        rel_count = sum(len(v) for v in data.get("relationships", {}).values())
        dec_count = len(data.get("decisions", []))
        print(f"VALIDATION PASSED")
        print(f"  Entities: {entity_count}")
        print(f"  Relationships: {rel_count}")
        print(f"  Decisions: {dec_count}")
        print(f"  Status: {data.get('status')}")
        print(f"  Domain: {data.get('domain')}")
        sys.exit(0)


if __name__ == "__main__":
    main()
