#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

EXCLUDED = {"MANIFEST.json", "SHA256SUMS"}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()

    metadata = json.loads((root / "PACKAGE.json").read_text(encoding="utf-8"))
    records: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative in EXCLUDED or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        records.append(
            {
                "path": relative,
                "size": path.stat().st_size,
                "sha256": digest(path),
            }
        )

    manifest = {
        "manifest_version": "2.0.0",
        "package_id": metadata["package_id"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "excluded_paths": sorted(EXCLUDED),
        "files": records,
    }
    (root / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    (root / "SHA256SUMS").write_text(
        "".join(f"{record['sha256']}  {record['path']}\n" for record in records),
        encoding="utf-8",
    )
    print(f"wrote {len(records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
