from __future__ import annotations

import re
import shutil
from pathlib import Path

SOURCE_FILES = (
    'main.tex',
    'metadata.tex',
    'arxiv.sty',
    'orcid.pdf',
    'bibliography.tex',
)


def declared_figures(root: Path) -> list[str]:
    path = root / 'paper-source/ARXIV_FIGURES.txt'
    figures: list[str] = []
    for raw in path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        figures.append(line)
    return figures


def stage_source(root: Path, stage: Path) -> None:
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    source = root / 'paper-source'
    for name in SOURCE_FILES:
        candidate = source / name
        if not candidate.is_file():
            raise FileNotFoundError(candidate)
        shutil.copy2(candidate, stage / name)
    sections = source / 'sections'
    shutil.copytree(sections, stage / 'sections')
    (stage / 'figures').mkdir()
    for relative in declared_figures(root):
        candidate = root / relative
        if not candidate.is_file():
            raise FileNotFoundError(candidate)
        if candidate.suffix.lower() not in {'.pdf', '.png', '.jpg', '.jpeg', '.eps'}:
            raise ValueError(f'unsupported arXiv figure type: {relative}')
        target = stage / 'figures' / candidate.name
        if target.exists():
            raise ValueError(f'duplicate arXiv figure basename: {candidate.name}')
        shutil.copy2(candidate, target)


def referenced_graphics(stage: Path) -> set[str]:
    pattern = re.compile(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}')
    found: set[str] = set()
    for path in stage.rglob('*.tex'):
        for match in pattern.finditer(path.read_text(encoding='utf-8')):
            value = match.group(1)
            if value.startswith('figures/'):
                found.add(Path(value).name)
    return found
