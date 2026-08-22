#!/usr/bin/env python3
"""Structural validator for Expert Curriculum Template instances."""
from pathlib import Path
import argparse, json, re, sys

REQ_ROOT = [
    "AUTHORITY.md", "CURRICULUM_SPEC.json", "00_MASTER_ROADMAP/DEPENDENCY_GRAPH.md",
    "00_MASTER_ROADMAP/STRICT_ORDER_AND_START_GATES.md", "00_MASTER_ROADMAP/MASTER_PROGRESS.md",
]
REQ_GROUP = ["README.md", "PROGRESS.md", "SOFTWARE.md", "resources/README.md"]
PLACEHOLDER = re.compile(r"\{\{[A-Z0-9_]+\}\}")

def topo_cycle(groups):
    deps = {g['id']: set(g.get('depends_on', [])) for g in groups}
    known = set(deps)
    for gid, ds in deps.items():
        unknown = ds - known
        if unknown: return f"Group {gid} depends on unknown group(s): {sorted(unknown)}"
    temp, perm = set(), set()
    def visit(n):
        if n in temp: return n
        if n in perm: return None
        temp.add(n)
        for d in deps[n]:
            c = visit(d)
            if c: return c
        temp.remove(n); perm.add(n)
        return None
    for n in deps:
        c = visit(n)
        if c: return f"Dependency cycle includes {c}"
    return None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('root', nargs='?', default='.')
    ap.add_argument('--allow-placeholders', action='store_true', help='Useful while editing the template itself')
    a = ap.parse_args(); root = Path(a.root).resolve()
    errors, warnings = [], []
    for rel in REQ_ROOT:
        if not (root / rel).exists(): errors.append(f"Missing required file: {rel}")
    specp = root / 'CURRICULUM_SPEC.json'
    if specp.exists():
        try: spec = json.loads(specp.read_text(encoding='utf-8'))
        except Exception as e: errors.append(f"Invalid CURRICULUM_SPEC.json: {e}"); spec = {}
        groups = spec.get('groups', []) if isinstance(spec, dict) else []
        ids = [g.get('id') for g in groups]
        if len(ids) != len(set(ids)): errors.append('Duplicate group IDs in CURRICULUM_SPEC.json')
        c = topo_cycle(groups) if groups else None
        if c: errors.append(c)
        known = set(ids)
        fallback = spec.get('single_thread_fallback', []) if isinstance(spec, dict) else []
        unknown = [x for x in fallback if x not in known]
        if unknown: errors.append(f"Fallback references unknown groups: {unknown}")
        for g in groups:
            for field in ('id','slug','name','type','start_gate','role','exit_gate'):
                if not g.get(field): errors.append(f"Group {g.get('id','?')} missing {field}")
            d = root / f"{g.get('id','')}_{g.get('slug','')}"
            if not d.is_dir():
                warnings.append(f"Group folder not instantiated: {d.name}")
            else:
                for rel in REQ_GROUP:
                    if not (d / rel).exists(): errors.append(f"{d.name} missing {rel}")
    if not a.allow_placeholders:
        for rel in ['AUTHORITY.md','CURRICULUM_SPEC.json','00_MASTER_ROADMAP/STRICT_ORDER_AND_START_GATES.md']:
            p = root / rel
            if p.exists() and PLACEHOLDER.search(p.read_text(encoding='utf-8')):
                errors.append(f"Authoritative file still contains template placeholders: {rel}")
    for w in warnings: print('WARN:', w)
    for e in errors: print('FAIL:', e)
    if errors: return 1
    print('PASS: curriculum structure is internally valid at the checked structural level')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
