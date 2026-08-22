#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, sys

REQUIRED_SECTIONS = [
    'Purpose', 'Capability Boundary', 'Inputs', 'Procedure',
    'Output Contract', 'Validation and Quality Gates',
    'Failure and Escalation Behavior', 'Runtime and Dependencies',
    'Provenance and Lifecycle'
]
PLACEHOLDER_RE = re.compile(r'\{\{[^{}]+\}\}')

def fail(msg, errors): errors.append(msg)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default='.')
    ap.add_argument('--allow-placeholders', action='store_true')
    args=ap.parse_args()
    root=Path(args.root).resolve()
    errors=[]; warnings=[]
    for name in ['SKILL.md','SKILL_METADATA.json']:
        if not (root/name).is_file(): fail(f'missing required file: {name}', errors)
    if errors:
        for e in errors: print('FAIL:',e)
        return 1
    md=(root/'SKILL.md').read_text(encoding='utf-8', errors='replace')
    meta=json.loads((root/'SKILL_METADATA.json').read_text(encoding='utf-8'))
    for k in ['skill_id','title','version','status','purpose','entrypoint','use_when','do_not_use_when']:
        if k not in meta: fail(f'metadata missing required key: {k}', errors)
    if meta.get('entrypoint')!='SKILL.md': fail('entrypoint must be SKILL.md for this template family', errors)
    if meta.get('status') not in {'DRAFT','CANDIDATE','CANONICAL','DEPRECATED','ARCHIVED'}: fail('invalid status', errors)
    if not isinstance(meta.get('use_when'),list) or not meta.get('use_when'): fail('use_when must be a non-empty list', errors)
    if not isinstance(meta.get('do_not_use_when'),list) or not meta.get('do_not_use_when'): fail('do_not_use_when must be a non-empty list', errors)
    for s in REQUIRED_SECTIONS:
        if not re.search(r'^##\s+'+re.escape(s)+r'\s*$',md,re.M): fail(f'SKILL.md missing section: {s}', errors)
    if not args.allow_placeholders:
        found=sorted(set(PLACEHOLDER_RE.findall(md+'\n'+json.dumps(meta))))
        if found: fail('unresolved placeholders: '+', '.join(found[:12]), errors)
    for rel in meta.get('supporting_artifacts',[]):
        if not (root/rel).exists(): fail(f'supporting artifact missing: {rel}', errors)
        if rel not in md: warnings.append(f'supporting artifact not explicitly named in SKILL.md: {rel}')
    for w in warnings: print('WARN:',w)
    if errors:
        for e in errors: print('FAIL:',e)
        print(f'RESULT: FAIL ({len(errors)} errors, {len(warnings)} warnings)')
        return 1
    print(f'RESULT: PASS (0 errors, {len(warnings)} warnings)')
    return 0
if __name__=='__main__': raise SystemExit(main())
