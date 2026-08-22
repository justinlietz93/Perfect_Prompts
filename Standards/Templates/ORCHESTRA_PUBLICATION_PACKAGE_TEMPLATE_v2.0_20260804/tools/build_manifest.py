#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from common import digest, dump_json, iter_release_files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    args = parser.parse_args()
    root = args.root.resolve()
    records = []
    for path in iter_release_files(root):
        relative = path.relative_to(root).as_posix()
        if relative in {'MANIFEST.json', 'SHA256SUMS'}:
            continue
        records.append({
            'path': relative,
            'size': path.stat().st_size,
            'sha256': digest(path),
        })
    manifest = {
        'schema_version': '2.0.0',
        'root_name': root.name,
        'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'files': records,
    }
    dump_json(root / 'MANIFEST.json', manifest)
    lines = [f"{record['sha256']}  {record['path']}" for record in records]
    (root / 'SHA256SUMS').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'{len(records)} files')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
