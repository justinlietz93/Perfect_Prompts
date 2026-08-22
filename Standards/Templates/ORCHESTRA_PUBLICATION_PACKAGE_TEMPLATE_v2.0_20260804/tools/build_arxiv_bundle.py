#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path

from compile_paper import compile_stage
from stage_arxiv import referenced_graphics, stage_source


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    args = parser.parse_args()
    root = args.root.resolve()
    stage = root / '_build/arxiv-source'
    stage_source(root, stage)

    declared = {path.stem for path in (stage / 'figures').iterdir() if path.is_file()}
    referenced = {Path(name).stem for name in referenced_graphics(stage)}
    missing = sorted(referenced - declared)
    unused = sorted(declared - referenced)
    if missing:
        raise SystemExit(f'figures referenced but not declared: {missing}')
    if unused:
        raise SystemExit(f'declared arXiv figures not referenced: {unused}')

    compile_stage(stage)
    allowed_suffixes = {'.tex', '.sty', '.pdf', '.png', '.jpg', '.jpeg', '.eps'}
    bundle = root / 'arxiv-source.zip'
    with zipfile.ZipFile(bundle, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(stage.rglob('*')):
            if not path.is_file() or path.suffix.lower() not in allowed_suffixes:
                continue
            if path.name == 'main.pdf':
                continue
            archive.write(path, path.relative_to(stage).as_posix())

    with tempfile.TemporaryDirectory() as temporary:
        clean = Path(temporary)
        with zipfile.ZipFile(bundle) as archive:
            archive.testzip()
            archive.extractall(clean)
        compile_stage(clean)
    print(bundle)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
