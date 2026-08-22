#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path

from common import HEX64_RE, digest, iter_release_files, load_json

REQUIRED = {
    'README.md', 'PUBLICATION.json', 'SOURCE_RESEARCH_LINEAGE.json',
    'RELEASE_WORKFLOW.md', 'RELEASE_NOTES.md', 'CLOSURE_CERTIFICATE.md',
    'CITATION.cff', 'LICENSE_SELECTION.md',
    'claims/claims.json', 'claims/CLAIM_LEDGER.md',
    'claims/ASSUMPTION_LEDGER.md', 'claims/NONCLAIMS.md',
    'validation/coverage.json', 'validation/COVERAGE_MAP.md',
    'paper-source/main.tex', 'paper-source/metadata.tex',
    'paper-source/arxiv.sty', 'paper-source/orcid.pdf',
    'paper-source/ARXIV_FIGURES.txt',
    'zenodo/DEPOSIT_CHECKLIST.md', 'arxiv/SUBMISSION_CHECKLIST.md',
    'tools/init_publication.py', 'tools/compile_paper.py',
    'tools/build_arxiv_bundle.py', 'tools/build_manifest.py',
    'tools/validate_publication.py', 'tools/finalize_publication.py',
}
PLACEHOLDER_RE = re.compile(r'REPLACE_ME|TEMPLATE ONLY|0\.0\.0-template')
VALID_BURDENS = {'REQUIRED', 'NOT_APPLICABLE'}
VALID_COVERAGE = {'PASS', 'FAIL', 'MISSING', 'NOT_APPLICABLE'}
IMAGE_SUFFIXES = {'.pdf', '.png', '.jpg', '.jpeg', '.eps', '.svg'}


def notebook_text(output: dict) -> str:
    text = ''.join(output.get('text', []))
    data = output.get('data', {})
    plain = data.get('text/plain', [])
    if isinstance(plain, str):
        text += plain
    else:
        text += ''.join(plain)
    return text


def check_notebook(path: Path, errors: list[str], strict: bool) -> None:
    try:
        notebook = json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'invalid notebook {path}: {exc}')
        return
    cells = notebook.get('cells', [])
    if any(cell.get('cell_type') != 'code' for cell in cells):
        errors.append(f'notebook has non-code or infrastructure cells: {path}')
    if not cells:
        errors.append(f'notebook contains no claim cells: {path}')
    for index, cell in enumerate(cells, start=1):
        source = ''.join(cell.get('source', []))
        lowered = source.lower()
        for token in ('claim_id', 'threshold', 'negative_control', 'plt.show', 'pass', 'fail'):
            if token not in lowered:
                errors.append(f'{path} cell {index} missing {token}')
        forbidden = (
            'open(', 'path(', 'to_csv(', 'savefig(', 'write_text(', 'write_bytes(',
            'np.save(', 'pickle.', 'joblib.', 'h5py.', 'sqlite3.', 'requests.', 'urllib.'
        )
        if any(token in lowered for token in forbidden):
            errors.append(f'{path} cell {index} appears to perform file or network I/O')
        if strict:
            if 'REPLACE_ME' in source or 'NotImplementedError' in source:
                errors.append(f'{path} cell {index} retains placeholders')
            if cell.get('execution_count') is None:
                errors.append(f'{path} cell {index} is not executed')
            outputs = cell.get('outputs', [])
            has_figure = any(
                'image/png' in output.get('data', {}) or
                'image/svg+xml' in output.get('data', {})
                for output in outputs
            )
            if not has_figure:
                errors.append(f'{path} cell {index} has no rendered figure')
            text = '\n'.join(notebook_text(output) for output in outputs)
            if not re.search(r'\b(PASS|FAIL)\b', text):
                errors.append(f'{path} cell {index} output has no PASS/FAIL')
            if not re.search(r'[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?', text):
                errors.append(f'{path} cell {index} output has no numeric result')


def check_manifest(root: Path, errors: list[str]) -> None:
    mpath = root / 'MANIFEST.json'
    spath = root / 'SHA256SUMS'
    if not mpath.is_file() or not spath.is_file():
        errors.append('MANIFEST.json and SHA256SUMS are required')
        return
    try:
        manifest = load_json(mpath)
    except Exception as exc:
        errors.append(f'invalid MANIFEST.json: {exc}')
        return
    listed = {record.get('path'): record for record in manifest.get('files', [])}
    actual = {}
    for path in iter_release_files(root):
        relative = path.relative_to(root).as_posix()
        if relative in {'MANIFEST.json', 'SHA256SUMS'}:
            continue
        actual[relative] = path
    for relative in sorted(set(listed) - set(actual)):
        errors.append(f'manifest lists missing file: {relative}')
    for relative in sorted(set(actual) - set(listed)):
        errors.append(f'manifest omits file: {relative}')
    for relative, path in actual.items():
        record = listed.get(relative)
        if not record:
            continue
        if record.get('size') != path.stat().st_size:
            errors.append(f'manifest size mismatch: {relative}')
        if record.get('sha256') != digest(path):
            errors.append(f'manifest hash mismatch: {relative}')
    sums = {}
    for line in spath.read_text(encoding='utf-8').splitlines():
        if line.strip():
            checksum, relative = line.split('  ', 1)
            sums[relative] = checksum
    expected = {path: record.get('sha256') for path, record in listed.items()}
    if sums != expected:
        errors.append('SHA256SUMS differs from MANIFEST.json')


def check_claims(root: Path, metadata: dict, errors: list[str], strict: bool) -> None:
    try:
        claims = load_json(root / 'claims/claims.json').get('claims', [])
        coverage = load_json(root / 'validation/coverage.json').get('coverage', [])
    except Exception as exc:
        errors.append(f'invalid claim or coverage JSON: {exc}')
        return
    claim_ids = [claim.get('claim_id') for claim in claims]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append('duplicate claim IDs')
    coverage_by_id = {record.get('claim_id'): record for record in coverage}
    primary = []
    for claim in claims:
        claim_id = claim.get('claim_id')
        if not re.fullmatch(r'C\d{3,}', str(claim_id)):
            errors.append(f'invalid claim ID: {claim_id!r}')
        if claim.get('claim_class') == 'PRIMARY':
            primary.append(claim_id)
        burdens = claim.get('burdens', {})
        for burden in ('formal', 'symbolic', 'numerical', 'figure'):
            if burdens.get(burden) not in VALID_BURDENS:
                errors.append(f'{claim_id} invalid {burden} burden')
        record = coverage_by_id.get(claim_id)
        if not record:
            errors.append(f'coverage missing claim: {claim_id}')
            continue
        for burden in ('formal', 'symbolic', 'numerical', 'figure'):
            result = record.get(burden, {})
            status = result.get('status')
            if status not in VALID_COVERAGE:
                errors.append(f'{claim_id} invalid {burden} coverage status: {status}')
            expected = burdens.get(burden)
            if status == 'NOT_APPLICABLE' and not str(result.get('reason', '')).strip():
                errors.append(f'{claim_id} {burden} NOT_APPLICABLE lacks a reason')
            if expected == 'REQUIRED' and status == 'NOT_APPLICABLE':
                errors.append(f'{claim_id} {burden} declared REQUIRED but marked NOT_APPLICABLE')
            if expected == 'NOT_APPLICABLE' and status != 'NOT_APPLICABLE':
                errors.append(f'{claim_id} {burden} burden and coverage disagree')
            if strict and metadata.get('release_level') in {'preprint', 'final'} and status != 'PASS' and expected == 'REQUIRED':
                errors.append(f'{claim_id} required {burden} is not PASS')
            for artifact in result.get('artifacts', []):
                if not (root / artifact).is_file():
                    errors.append(f'{claim_id} missing {burden} artifact: {artifact}')
    if strict and not primary:
        errors.append('no primary claims declared')
    declared_primary = metadata.get('primary_claim_ids', [])
    if strict and sorted(primary) != sorted(declared_primary):
        errors.append('PUBLICATION.json primary_claim_ids disagrees with claims.json')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    parser.add_argument('--strict', action='store_true')
    parser.add_argument('--require-manifest', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    for relative in sorted(REQUIRED):
        if not (root / relative).is_file():
            errors.append(f'missing required file: {relative}')
    try:
        metadata = load_json(root / 'PUBLICATION.json')
    except Exception as exc:
        metadata = {}
        errors.append(f'invalid PUBLICATION.json: {exc}')

    package_type = metadata.get('package_type')
    template_mode = package_type == 'orchestra_publication_package_template'
    if package_type not in {'orchestra_publication_package_template', 'orchestra_publication_package'}:
        errors.append(f'invalid package_type: {package_type!r}')
    if args.strict and template_mode:
        errors.append('strict validation applies to active publication packages')

    for path in root.rglob('*'):
        if not path.is_file() or '_build' in path.parts or '__pycache__' in path.parts:
            continue
        if path.stat().st_size <= 1:
            errors.append(f'empty or one-byte placeholder: {path.relative_to(root)}')
        if path.suffix == '.ipynb':
            check_notebook(path, errors, args.strict)
        if path.suffix in {'.py', '.tex'} and path.name != 'arxiv.sty':
            lines = len(path.read_text(encoding='utf-8', errors='replace').splitlines())
            if lines > 500:
                errors.append(f'source exceeds 500 lines: {path.relative_to(root)} ({lines})')

    main_tex = root / 'paper-source/main.tex'
    if main_tex.is_file():
        tex = main_tex.read_text(encoding='utf-8')
        if '\\today' in tex:
            errors.append('main.tex uses dynamic \\today')
        if '\\usepackage{natbib}' in tex:
            errors.append('main.tex loads natbib; use a coherent bibliography route')
        if 'href{mailto:' not in tex:
            errors.append('main.tex email link does not use mailto:')

    check_claims(root, metadata, errors, args.strict)

    if args.strict:
        key_files = (
            'PUBLICATION.json', 'SOURCE_RESEARCH_LINEAGE.json',
            'claims/claims.json', 'claims/CLAIM_LEDGER.md',
            'claims/ASSUMPTION_LEDGER.md', 'claims/NONCLAIMS.md',
            'validation/coverage.json', 'CLOSURE_CERTIFICATE.md',
            'RELEASE_NOTES.md', 'paper-source/metadata.tex',
        )
        for relative in key_files:
            if PLACEHOLDER_RE.search((root / relative).read_text(encoding='utf-8')):
                errors.append(f'placeholder marker remains in {relative}')
        for path in [root / 'README.md', root / 'zenodo/ZENODO_METADATA.json'] + list((root / 'paper-source').rglob('*.tex')):
            if not path.is_file():
                errors.append(f'missing active release file: {path.relative_to(root)}')
                continue
            text = path.read_text(encoding='utf-8')
            if re.search(r'REPLACE_ME|TEMPLATE ONLY|Replace this|neutral template|publication template', text, re.IGNORECASE):
                errors.append(f'template text remains in {path.relative_to(root)}')
        if metadata.get('closure_status') != 'CLOSED':
            errors.append('PUBLICATION.json closure_status is not CLOSED')
        if metadata.get('scientific_status') in {'WORKING', 'UNVALIDATED_TEMPLATE', None, ''}:
            errors.append('scientific_status is not a closed release status')
        if metadata.get('license') in {None, '', 'REPLACE_ME'} or not (root / 'LICENSE.txt').is_file():
            errors.append('active release lacks matching LICENSE.txt')
        source_packages = metadata.get('source_research_packages', [])
        if not source_packages:
            errors.append('no source research packages declared')
        try:
            lineage = load_json(root / 'SOURCE_RESEARCH_LINEAGE.json')
            if not lineage.get('claim_migrations'):
                errors.append('source lineage contains no claim migrations')
            for source in lineage.get('source_packages', []):
                if not HEX64_RE.fullmatch(str(source.get('manifest_sha256', ''))):
                    errors.append(f"invalid source manifest hash for {source.get('package_id')}")
                if not HEX64_RE.fullmatch(str(source.get('auditor_verdict_sha256', ''))):
                    errors.append(f"invalid auditor verdict hash for {source.get('package_id')}")
        except Exception as exc:
            errors.append(f'invalid source lineage: {exc}')
        for relative in ('paper.pdf', 'arxiv-source.zip'):
            path = root / relative
            if not path.is_file() or path.stat().st_size < 1000:
                errors.append(f'missing release artifact: {relative}')
        if (root / 'arxiv-source.zip').is_file():
            try:
                with zipfile.ZipFile(root / 'arxiv-source.zip') as archive:
                    if archive.testzip() is not None:
                        errors.append('arxiv-source.zip failed CRC test')
                    names = archive.namelist()
                    if any(name.startswith('/') or '..' in Path(name).parts for name in names):
                        errors.append('arxiv-source.zip contains unsafe path')
            except Exception as exc:
                errors.append(f'invalid arxiv-source.zip: {exc}')
        certificate = (root / 'CLOSURE_CERTIFICATE.md').read_text(encoding='utf-8')
        if 'Closure status: `CLOSED`' not in certificate:
            errors.append('closure certificate does not declare CLOSED')
        check_manifest(root, errors)
    elif args.require_manifest or (root / 'MANIFEST.json').exists() or (root / 'SHA256SUMS').exists():
        check_manifest(root, errors)

    if errors:
        print('FAIL')
        for error in errors:
            print(f'- {error}')
        return 1
    print('PASS')
    print(f'- package_type: {package_type}')
    print(f'- strict: {args.strict}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
