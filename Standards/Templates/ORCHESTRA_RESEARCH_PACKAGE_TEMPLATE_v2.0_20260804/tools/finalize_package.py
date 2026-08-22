#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path


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
    tools = root / "tools"
    subprocess.run(
        [sys.executable, str(tools / "validate_package.py"), str(root)],
        check=True,
    )
    subprocess.run(
        [sys.executable, str(tools / "build_manifest.py"), str(root)],
        check=True,
    )
    subprocess.run(
        [sys.executable, str(tools / "validate_package.py"), str(root), "--strict"],
        check=True,
    )

    zip_path = root.parent / f"{root.name}.zip"
    if zip_path.exists():
        raise SystemExit(f"refusing to overwrite closed archive: {zip_path}")
    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            archive.write(
                path,
                arcname=(Path(root.name) / path.relative_to(root)).as_posix(),
            )

    checksum_path = Path(str(zip_path) + ".sha256")
    checksum_path.write_text(
        f"{digest(zip_path)}  {zip_path.name}\n",
        encoding="utf-8",
    )
    print(zip_path)
    print(checksum_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
