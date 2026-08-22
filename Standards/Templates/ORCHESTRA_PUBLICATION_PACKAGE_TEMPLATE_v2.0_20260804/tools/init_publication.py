#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path

from common import dump_json, load_json, tex_escape


def license_text(name: str) -> str:
    if name == 'cc-by-4.0':
        return (
            'This work is licensed under the Creative Commons Attribution 4.0 '
            'International License. Full terms: https://creativecommons.org/licenses/by/4.0/\n'
        )
    if name == 'all-rights-reserved':
        return (
            'All rights reserved. No reuse license is granted except as required by applicable law.\n'
        )
    raise ValueError(name)


def replace_macro(text: str, macro: str, value: str) -> str:
    pattern = re.compile(rf'\\newcommand\{{\\{re.escape(macro)}\}}\{{.*?\}}')
    replacement = rf'\newcommand{{\{macro}}}{{{tex_escape(value)}}}'
    updated, count = pattern.subn(lambda _: replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f'macro not found: {macro}')
    return updated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--short-title', required=True)
    parser.add_argument('--slug', required=True)
    parser.add_argument('--version', required=True)
    parser.add_argument('--release-level', choices=('draft', 'preprint', 'final'), required=True)
    parser.add_argument('--license', choices=('cc-by-4.0', 'all-rights-reserved'), required=True)
    parser.add_argument('--source-package-id', required=True)
    parser.add_argument('--source-manifest-sha256', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--doi', default='')
    parser.add_argument('--repository-url', default='')
    parser.add_argument('--timestamp', default='')
    parser.add_argument('--publication-date', default='')
    parser.add_argument('--created-at', default='')
    parser.add_argument('--keyword', action='append', default=[])
    args = parser.parse_args()

    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.slug):
        raise SystemExit('slug must use lowercase letters, numbers, and hyphens')
    if not re.fullmatch(r'[0-9a-fA-F]{64}', args.source_manifest_sha256):
        raise SystemExit('source manifest hash must be 64 hexadecimal characters')

    template = Path(__file__).resolve().parents[1]
    timestamp = args.timestamp or datetime.now().astimezone().strftime('%Y%m%d_%H%M%S')
    date = args.publication_date or datetime.now().astimezone().date().isoformat()
    created_at = args.created_at or datetime.now().astimezone().isoformat(timespec='seconds')
    keywords = args.keyword or ['Phase Calculus']
    directory = args.output.resolve() / f'{args.slug}_v{args.version}_{timestamp}'
    if directory.exists():
        raise SystemExit(f'refusing to overwrite: {directory}')
    shutil.copytree(
        template,
        directory,
        ignore=shutil.ignore_patterns('.git', '__pycache__', '_build', 'MANIFEST.json', 'SHA256SUMS'),
    )
    (directory / 'TEMPLATE_STATUS.md').unlink(missing_ok=True)

    active_readme = f'''# {args.title}

Publication package `{args.slug}-v{args.version}`.

- Release level: `{args.release_level}`
- Status: `WORKING`
- Source research package: `{args.source_package_id}`
- Source manifest SHA-256: `{args.source_manifest_sha256.lower()}`

## Build

```bash
python tools/validate_publication.py .
python tools/compile_paper.py .
python tools/build_arxiv_bundle.py .
```

## Close and freeze

After the claim, lineage, validation, manuscript, metadata, and closure records are complete:

```bash
python tools/finalize_publication.py .
```

A closed release is immutable. Create a new publication version for changed files.
'''
    (directory / 'README.md').write_text(active_readme, encoding='utf-8')

    publication_id = f'{args.slug}-v{args.version}'
    metadata = load_json(directory / 'PUBLICATION.json')
    metadata.update({
        'package_type': 'orchestra_publication_package',
        'publication_id': publication_id,
        'title': args.title,
        'short_title': args.short_title,
        'slug': args.slug,
        'version': args.version,
        'created_at': created_at,
        'publication_date': date,
        'release_level': args.release_level,
        'scientific_status': 'WORKING',
        'closure_status': 'OPEN',
        'license': args.license,
        'keywords': keywords,
        'repository_url': args.repository_url or None,
        'source_research_packages': [args.source_package_id],
        'external_identifiers': {
            'doi': args.doi or None,
            'zenodo_record': None,
            'arxiv_id': None,
        },
    })
    dump_json(directory / 'PUBLICATION.json', metadata)

    lineage = load_json(directory / 'SOURCE_RESEARCH_LINEAGE.json')
    lineage.update({
        'publication_id': publication_id,
        'source_packages': [{
            'package_id': args.source_package_id,
            'manifest_sha256': args.source_manifest_sha256.lower(),
            'auditor_verdict_path': 'REPLACE_ME',
            'auditor_verdict_sha256': 'REPLACE_ME',
            'accepted_status': 'REPLACE_ME',
        }],
    })
    dump_json(directory / 'SOURCE_RESEARCH_LINEAGE.json', lineage)

    claim_data = load_json(directory / 'claims/claims.json')
    claim_data['publication_id'] = publication_id
    dump_json(directory / 'claims/claims.json', claim_data)
    coverage = load_json(directory / 'validation/coverage.json')
    coverage['publication_id'] = publication_id
    dump_json(directory / 'validation/coverage.json', coverage)

    tex_path = directory / 'paper-source/metadata.tex'
    tex = tex_path.read_text(encoding='utf-8')
    replacements = {
        'PaperTitle': args.title,
        'PaperShortTitle': args.short_title,
        'PaperDOIText': args.doi or 'DOI not assigned',
        'PaperDOIURL': f'https://doi.org/{args.doi}' if args.doi else 'https://doi.org/',
        'PaperDate': date,
        'PaperVersion': args.version,
        'PaperReleaseStatus': f'{args.release_level.upper()} WORKING',
    }
    for macro, value in replacements.items():
        tex = replace_macro(tex, macro, value)
    keyword_value = r' \and '.join(tex_escape(keyword) for keyword in keywords)
    keyword_pattern = re.compile(r'\\newcommand\{\\PaperKeywords\}\{.*?\}')
    tex, count = keyword_pattern.subn(
        lambda _: r'\newcommand{\PaperKeywords}{' + keyword_value + '}', tex, count=1
    )
    if count != 1:
        raise RuntimeError('macro not found: PaperKeywords')
    tex_path.write_text(tex, encoding='utf-8')

    (directory / 'LICENSE.txt').write_text(license_text(args.license), encoding='utf-8')
    cff = (directory / 'CITATION.cff').read_text(encoding='utf-8')
    cff = cff.replace('TEMPLATE ONLY - initialize before citation', 'Please cite this release using the metadata below.')
    cff = cff.replace('Publication Package Template', args.title)
    cff = cff.replace('0.0.0-template', args.version)
    cff = cff.replace('2026-08-04', date)
    if args.repository_url:
        cff = cff.replace('REPLACE_ME', args.repository_url, 1)
    else:
        cff = cff.replace('repository-code: "REPLACE_ME"\n', '')
    cff = cff.replace('REPLACE_ME', args.license, 1)
    (directory / 'CITATION.cff').write_text(cff, encoding='utf-8')

    zpath = directory / 'zenodo/ZENODO_METADATA_TEMPLATE.json'
    zenodo = load_json(zpath)
    zenodo.update({
        'template_status': 'ACTIVE_DRAFT',
        'title': args.title,
        'publication_date': date,
        'version': args.version,
        'license': args.license,
        'keywords': keywords,
        'repository_url': args.repository_url or None,
        'keywords': keywords,
    })
    dump_json(directory / 'zenodo/ZENODO_METADATA.json', zenodo)
    zpath.unlink()

    print(directory)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
