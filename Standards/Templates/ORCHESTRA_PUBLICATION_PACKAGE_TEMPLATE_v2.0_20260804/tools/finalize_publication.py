#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            hasher.update(block)
    return hasher.hexdigest()


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    args = parser.parse_args()
    root = args.root.resolve()
    tools = root / 'tools'

    run(sys.executable, str(tools / 'validate_publication.py'), str(root))
    run(sys.executable, str(tools / 'compile_paper.py'), str(root))
    run(sys.executable, str(tools / 'build_arxiv_bundle.py'), str(root))
    run(sys.executable, str(tools / 'build_manifest.py'), str(root))
    run(sys.executable, str(tools / 'validate_publication.py'), str(root), '--strict')

    archive_path = root.parent / f'{root.name}.zip'
    if archive_path.exists():
        raise SystemExit(f'refusing to overwrite closed archive: {archive_path}')
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(root.rglob('*')):
            if not path.is_file():
                continue
            if any(part in {'.git', '__pycache__', '_build'} for part in path.parts):
                continue
            archive.write(path, (Path(root.name) / path.relative_to(root)).as_posix())

    with tempfile.TemporaryDirectory() as temporary:
        clean = Path(temporary)
        with zipfile.ZipFile(archive_path) as archive:
            archive.testzip()
            archive.extractall(clean)
        extracted = clean / root.name
        run(sys.executable, str(extracted / 'tools/validate_publication.py'), str(extracted), '--strict')
        run(sys.executable, str(extracted / 'tools/compile_paper.py'), str(extracted))

    checksum = Path(str(archive_path) + '.sha256')
    checksum.write_text(f'{digest(archive_path)}  {archive_path.name}\n', encoding='utf-8')
    print(archive_path)
    print(checksum)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
