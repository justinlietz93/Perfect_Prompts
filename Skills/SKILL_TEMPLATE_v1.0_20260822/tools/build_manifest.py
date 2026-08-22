#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.')
    root=Path(ap.parse_args().root).resolve()
    entries=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name not in {'MANIFEST.json','SHA256SUMS'}:
            entries.append({'path':p.relative_to(root).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
    (root/'MANIFEST.json').write_text(json.dumps({'files':entries},indent=2)+'\n')
    (root/'SHA256SUMS').write_text('\n'.join(f"{e['sha256']}  {e['path']}" for e in entries)+'\n')
    print(f'wrote {len(entries)} manifest entries')
if __name__=='__main__': main()
