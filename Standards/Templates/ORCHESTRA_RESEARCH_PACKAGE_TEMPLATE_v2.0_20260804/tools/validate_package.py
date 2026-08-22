#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

REQUIRED = {
    "README.md",
    "PACKAGE.json",
    "WORKFLOW.md",
    "AUTHORITY.md",
    "HANDOFF.md",
    "CLAIMS.md",
    "FINDINGS.md",
    "LAB_JOURNAL.md",
    "CHANGELOG.md",
    "inputs/README.md",
    "src/README.md",
    "notebooks/README.md",
    "figures/README.md",
    "output_data/README.md",
    "source_maps/README.md",
    "trace_logs/README.md",
    "lean/README.md",
    "review/README.md",
    "tools/build_manifest.py",
    "tools/validate_package.py",
    "tools/finalize_package.py",
}
ID_RE = re.compile(r"^p(?P<p>\d+)-b(?P<b>\d+)-v(?P<v>\d+)$")
PLACEHOLDER_RE = re.compile(r"REPLACE_ME|p#-b#-v#")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".svg", ".pdf"}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def check_notebook(path: Path, errors: list[str], strict: bool) -> None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid notebook {path}: {exc}")
        return

    code_cells = [cell for cell in notebook.get("cells", []) if cell.get("cell_type") == "code"]
    markdown_cells = [cell for cell in notebook.get("cells", []) if cell.get("cell_type") == "markdown"]
    if markdown_cells:
        errors.append(f"notebook contains markdown/infrastructure cells: {path}")
    if not code_cells:
        errors.append(f"notebook contains no claim cells: {path}")

    for index, cell in enumerate(code_cells, start=1):
        source = "".join(cell.get("source", []))
        lowered = source.lower()
        for token in ("threshold", "negative_control", "pass", "fail", "plt.show"):
            if token not in lowered:
                errors.append(f"{path} cell {index} missing {token}")
        forbidden = ("open(", "to_csv(", "savefig(", "write_text(", "write_bytes(", "np.save(")
        if any(token in lowered for token in forbidden):
            errors.append(f"{path} cell {index} appears to perform file I/O")

        if strict:
            if "REPLACE_ME" in source or "NotImplementedError" in source:
                errors.append(f"{path} cell {index} retains placeholders")
            if cell.get("execution_count") is None:
                errors.append(f"{path} cell {index} is not executed")
            outputs = cell.get("outputs", [])
            has_figure = any(
                "image/png" in output.get("data", {})
                or "image/svg+xml" in output.get("data", {})
                for output in outputs
            )
            if not has_figure:
                errors.append(f"{path} cell {index} has no rendered figure")
            output_text = "\n".join(
                "".join(output.get("text", []))
                + "".join(output.get("data", {}).get("text/plain", []))
                for output in outputs
            )
            if "PASS" not in output_text and "FAIL" not in output_text:
                errors.append(f"{path} cell {index} output has no PASS/FAIL")


def check_manifest(root: Path, errors: list[str]) -> None:
    manifest_path = root / "MANIFEST.json"
    sums_path = root / "SHA256SUMS"
    if not manifest_path.exists() or not sums_path.exists():
        errors.append("MANIFEST.json and SHA256SUMS are required")
        return

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid MANIFEST.json: {exc}")
        return

    listed = {record.get("path"): record for record in manifest.get("files", [])}
    actual: dict[str, Path] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative in {"MANIFEST.json", "SHA256SUMS"}:
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        actual[relative] = path

    for relative in sorted(set(listed) - set(actual)):
        errors.append(f"manifest lists missing file: {relative}")
    for relative in sorted(set(actual) - set(listed)):
        errors.append(f"manifest omits file: {relative}")

    for relative, path in actual.items():
        record = listed.get(relative)
        if not record:
            continue
        if record.get("size") != path.stat().st_size:
            errors.append(f"manifest size mismatch: {relative}")
        if record.get("sha256") != digest(path):
            errors.append(f"manifest hash mismatch: {relative}")

    sums: dict[str, str] = {}
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            checksum, relative = line.split("  ", 1)
            sums[relative] = checksum
    expected = {relative: record.get("sha256") for relative, record in listed.items()}
    if sums != expected:
        errors.append("SHA256SUMS differs from MANIFEST.json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--require-manifest", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []
    for relative in sorted(REQUIRED):
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    try:
        metadata = json.loads((root / "PACKAGE.json").read_text(encoding="utf-8"))
    except Exception as exc:
        metadata = {}
        errors.append(f"invalid PACKAGE.json: {exc}")

    package_type = metadata.get("package_type")
    template_mode = package_type == "orchestra_research_package_template"
    if package_type not in {
        "orchestra_research_package_template",
        "orchestra_research_package",
    }:
        errors.append(f"invalid package_type: {package_type!r}")
    if args.strict and template_mode:
        errors.append("strict validation applies to active packages")

    if not template_mode:
        match = ID_RE.fullmatch(str(metadata.get("package_id", "")))
        if not match:
            errors.append("active package_id must match p<phase>-b<branch>-v<version>")
        else:
            expected = (
                int(match.group("p")),
                int(match.group("b")),
                int(match.group("v")),
            )
            actual = (
                metadata.get("phase"),
                metadata.get("branch"),
                metadata.get("version"),
            )
            if actual != expected:
                errors.append(f"phase/branch/version {actual} disagree with package_id {expected}")

    for path in root.rglob("*"):
        if path.is_file() and path.stat().st_size <= 1:
            errors.append(f"empty or one-byte placeholder: {path.relative_to(root)}")
        if path.suffix == ".ipynb":
            check_notebook(path, errors, args.strict)

    if args.strict:
        for relative in (
            "PACKAGE.json",
            "AUTHORITY.md",
            "HANDOFF.md",
            "CLAIMS.md",
            "FINDINGS.md",
        ):
            if PLACEHOLDER_RE.search((root / relative).read_text(encoding="utf-8")):
                errors.append(f"placeholder marker remains in {relative}")
        if metadata.get("branch_goal") in {None, "", "REPLACE_ME"}:
            errors.append("branch_goal is not declared")
        if metadata.get("terminal_condition") in {None, "", "REPLACE_ME"}:
            errors.append("terminal_condition is not declared")
        if not metadata.get("active_authority"):
            errors.append("active_authority is empty")
        figures = [
            path
            for path in (root / "figures").iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
        ]
        if not figures:
            errors.append("strict Operator package requires a top-level decision figure")
        if not re.search(
            r"\| C\d{3,} \|",
            (root / "CLAIMS.md").read_text(encoding="utf-8"),
        ):
            errors.append("CLAIMS.md contains no stable claim row")
        check_manifest(root, errors)
    elif (
        args.require_manifest
        or (root / "MANIFEST.json").exists()
        or (root / "SHA256SUMS").exists()
    ):
        check_manifest(root, errors)

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print(f"- package_type: {package_type}")
    print(f"- strict: {args.strict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
