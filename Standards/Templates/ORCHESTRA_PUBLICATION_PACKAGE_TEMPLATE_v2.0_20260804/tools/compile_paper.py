#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path

from stage_arxiv import stage_source


def compile_stage(stage: Path) -> Path:
    env = os.environ.copy()
    env['HOME'] = str(stage / '.home')
    Path(env['HOME']).mkdir(exist_ok=True)
    command = [
        'latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error',
        '-file-line-error', '-synctex=0', 'main.tex'
    ]
    subprocess.run(command, cwd=stage, env=env, check=True)
    subprocess.run(command, cwd=stage, env=env, check=True)
    pdf = stage / 'main.pdf'
    if not pdf.is_file() or pdf.stat().st_size < 1000:
        raise RuntimeError('paper build produced no usable PDF')
    return pdf


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    args = parser.parse_args()
    root = args.root.resolve()
    stage = root / '_build/paper'
    stage_source(root, stage)
    pdf = compile_stage(stage)
    shutil.copy2(pdf, root / 'paper.pdf')
    print(root / 'paper.pdf')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
