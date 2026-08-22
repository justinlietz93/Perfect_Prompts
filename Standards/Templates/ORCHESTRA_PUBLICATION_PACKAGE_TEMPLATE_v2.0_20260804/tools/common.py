from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

EXCLUDED_PARTS = {'.git', '__pycache__', '_build'}
HEX64_RE = re.compile(r'^[0-9a-fA-F]{64}$')


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            hasher.update(block)
    return hasher.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def dump_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def iter_release_files(root: Path):
    for path in sorted(root.rglob('*')):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        yield path


def copy_clean(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(
        source,
        target,
        ignore=shutil.ignore_patterns('.git', '__pycache__', '_build', '*.pyc'),
    )


def tex_escape(value: str) -> str:
    replacements = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
    }
    return ''.join(replacements.get(char, char) for char in value)
