#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil, re, json

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--id', required=True)
    ap.add_argument('--title', required=True)
    ap.add_argument('--destination', required=True)
    args=ap.parse_args()
    here=Path(__file__).resolve().parents[1]
    dest=Path(args.destination).resolve()/args.id
    if dest.exists(): raise SystemExit(f'destination exists: {dest}')
    shutil.copytree(here,dest,ignore=shutil.ignore_patterns('MANIFEST.json','SHA256SUMS'))
    # Avoid nesting template-only metadata in instantiated skill.
    for name in ['PACKAGE.json','TEMPLATE_STATUS.md','INSTANTIATION_GUIDE.md','BUILD_CHECKLIST.md','SOURCE_MAP.md','CHANGELOG.md','AUTHORITY.md']:
        p=dest/name
        if p.exists(): p.unlink()
    repl={'{{SKILL_ID}}':args.id,'{{SKILL_TITLE}}':args.title,'{{ONE_SENTENCE_ACTIVATION_DESCRIPTION}}':f'Use for the {args.title} capability.'}
    p=dest/'SKILL.md'; txt=p.read_text()
    for a,b in repl.items(): txt=txt.replace(a,b)
    p.write_text(txt)
    meta=json.loads((dest/'SKILL_METADATA.json').read_text())
    meta['skill_id']=args.id; meta['title']=args.title
    (dest/'SKILL_METADATA.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(dest)
if __name__=='__main__': main()
