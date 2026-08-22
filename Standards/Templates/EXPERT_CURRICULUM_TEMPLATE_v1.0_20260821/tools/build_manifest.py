#!/usr/bin/env python3
"""Build deterministic SHA-256 manifest for curriculum text/config/tool files."""
from pathlib import Path
import argparse, hashlib, json

SKIP = {"MANIFEST.json", "SHA256SUMS"}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('root', nargs='?', default='.')
    a = ap.parse_args(); root = Path(a.root).resolve()
    records=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.name in SKIP or '.git' in p.parts: continue
        rel = p.relative_to(root).as_posix()
        data = p.read_bytes(); h = hashlib.sha256(data).hexdigest()
        records.append({'path': rel, 'bytes': len(data), 'sha256': h})
    manifest = {'manifest_version':'1.0','files':records}
    (root/'MANIFEST.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    (root/'SHA256SUMS').write_text(''.join(f"{r['sha256']}  {r['path']}\n" for r in records), encoding='utf-8')
    print(f"WROTE {len(records)} records")

if __name__ == '__main__': main()
