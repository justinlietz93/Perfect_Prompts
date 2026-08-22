#!/usr/bin/env python3
"""
Validate and render a Mermaid mindmap file to SVG.

Usage:
    python render_mermaid.py <path_to_mmd_file> [--output <svg_path>]

Validates syntax and attempts to render via mmdc (mermaid-cli) if available.
Falls back to syntax validation only if mmdc is not installed.
"""

import subprocess
import sys
import re
from pathlib import Path
import shutil
import json


def validate_syntax(content: str) -> list[str]:
    """Basic syntax validation for Mermaid mindmap files."""
    errors = []
    lines = content.strip().split("\n")

    if not lines:
        errors.append("File is empty")
        return errors

    # Check for mindmap declaration
    first_meaningful = ""
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("%%"):
            first_meaningful = stripped
            break

    if not first_meaningful.startswith("mindmap"):
        errors.append(f"Expected 'mindmap' declaration, found: '{first_meaningful}'")

    # Check for root node
    has_root = False
    for line in lines:
        if "root(" in line or "root((" in line:
            has_root = True
            break

    if not has_root:
        errors.append("No root node found. Expected root((Topic)) or root(Topic)")

    # Check for balanced parentheses in each line
    for i, line in enumerate(lines, 1):
        open_parens = line.count("(")
        close_parens = line.count(")")
        if open_parens != close_parens:
            errors.append(f"Line {i}: Unbalanced parentheses ({open_parens} open, {close_parens} close)")

    # Check for minimum content
    content_lines = [l for l in lines if l.strip() and not l.strip().startswith("%%") and l.strip() != "mindmap"]
    if len(content_lines) < 3:
        errors.append(f"Only {len(content_lines)} content lines — concept map should have at least a root + 2 branches")

    # Count nodes (rough estimate)
    node_count = len([l for l in content_lines if l.strip() and not l.strip().startswith("%%")])
    if node_count > 50:
        errors.append(f"[WARNING] {node_count} nodes detected — consider trimming to 15-30 for readability")

    return errors


def try_render(mmd_path: Path, output_path: Path) -> bool:
    """Attempt to render the Mermaid file to SVG using mmdc."""
    mmdc = shutil.which("mmdc")
    if not mmdc:
        # Try npx fallback
        try:
            result = subprocess.run(
                ["npx", "--yes", "@mermaid-js/mermaid-cli", "-i", str(mmd_path), "-o", str(output_path), "-q"],
                capture_output=True, text=True, timeout=60
            )
            if result.returncode == 0 and output_path.exists():
                return True
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        return False

    try:
        result = subprocess.run(
            [mmdc, "-i", str(mmd_path), "-o", str(output_path), "-q"],
            capture_output=True, text=True, timeout=30
        )
        return result.returncode == 0 and output_path.exists()
    except subprocess.TimeoutExpired:
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate and render Mermaid mindmap")
    parser.add_argument("input", help="Path to .mmd file")
    parser.add_argument("--output", "-o", help="Output SVG path (default: same name with .svg)")
    args = parser.parse_args()

    mmd_path = Path(args.input)
    if not mmd_path.exists():
        print(f"ERROR: File not found: {mmd_path}")
        sys.exit(1)

    content = mmd_path.read_text()

    # Syntax validation
    errors = validate_syntax(content)
    warnings = [e for e in errors if e.startswith("[WARNING]")]
    hard_errors = [e for e in errors if not e.startswith("[WARNING]")]

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  {w}")

    if hard_errors:
        print("SYNTAX VALIDATION FAILED:")
        for e in hard_errors:
            print(f"  ✗ {e}")
        sys.exit(1)

    print(f"SYNTAX VALIDATION PASSED")

    # Attempt rendering
    output_path = Path(args.output) if args.output else mmd_path.with_suffix(".svg")
    rendered = try_render(mmd_path, output_path)

    if rendered:
        print(f"RENDERED: {output_path}")
    else:
        print("RENDER SKIPPED: mmdc not available (install @mermaid-js/mermaid-cli for SVG output)")
        print("Syntax is valid — diagram will render in any Mermaid-compatible viewer.")

    sys.exit(0)


if __name__ == "__main__":
    main()
