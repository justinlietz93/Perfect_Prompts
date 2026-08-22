#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", type=int, required=True)
    parser.add_argument("--branch", type=int, required=True)
    parser.add_argument("--version", type=int, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--title")
    parser.add_argument("--origin-role", required=True)
    parser.add_argument("--target-role", required=True)
    parser.add_argument("--parent-package-id")
    parser.add_argument("--parent-manifest-sha256")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if min(args.phase, args.branch, args.version) < 0:
        raise SystemExit("phase, branch, and version must be nonnegative")
    if not SLUG_RE.fullmatch(args.name):
        raise SystemExit("--name must be lowercase kebab-case")

    template_root = Path(__file__).resolve().parents[1]
    package_id = f"p{args.phase}-b{args.branch}-v{args.version}"
    timestamp = datetime.now().astimezone().strftime("%Y%m%d_%H%M%S")
    destination = args.output.resolve() / f"{package_id}_{args.name}_{timestamp}"
    if destination.exists():
        raise SystemExit(f"destination exists: {destination}")

    shutil.copytree(template_root, destination)
    for name in ("MANIFEST.json", "SHA256SUMS", "TEMPLATE_STATUS.md"):
        path = destination / name
        if path.exists():
            path.unlink()

    metadata_path = destination / "PACKAGE.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata.update(
        {
            "package_type": "orchestra_research_package",
            "package_id": package_id,
            "title": args.title or args.name.replace("-", " ").title(),
            "slug": args.name,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "phase": args.phase,
            "branch": args.branch,
            "version": args.version,
            "parent_package_id": args.parent_package_id,
            "parent_manifest_sha256": args.parent_manifest_sha256,
            "origin_role": args.origin_role,
            "target_role": args.target_role,
            "branch_goal": "REPLACE_ME",
            "terminal_condition": "REPLACE_ME",
            "active_authority": [],
            "authority_exclusions": [],
            "status": "WORKING",
        }
    )
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    (destination / "STATUS.md").write_text(
        f"# Working Package\n\n"
        f"- Package ID: `{package_id}`\n"
        "- Status: `WORKING`\n"
        "- No review verdict is implied.\n",
        encoding="utf-8",
    )

    handoff_path = destination / "HANDOFF.md"
    handoff = handoff_path.read_text(encoding="utf-8")
    handoff = handoff.replace("- Package ID: `REPLACE_ME`", f"- Package ID: `{package_id}`", 1)
    handoff = handoff.replace("- Origin role: `REPLACE_ME`", f"- Origin role: `{args.origin_role}`", 1)
    handoff = handoff.replace("- Target role: `REPLACE_ME`", f"- Target role: `{args.target_role}`", 1)
    handoff_path.write_text(handoff, encoding="utf-8")

    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
