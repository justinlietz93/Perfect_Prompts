#!/usr/bin/env python3
"""Instantiate a curriculum deterministically from CURRICULUM_SPEC.json.

The script scaffolds folders and derives only structure already encoded in the spec.
It does not choose subjects, dependencies, resources, gates, or mastery criteria.
"""
from pathlib import Path
import argparse, json, re, shutil

TOKENS = re.compile(r"\{\{([A-Z0-9_]+)\}\}")

def replace(text, mapping):
    return TOKENS.sub(lambda m: str(mapping.get(m.group(1), m.group(0))), text)

def root_mapping(spec):
    c = spec.get("curriculum", {})
    return {
        "CURRICULUM_NAME": c.get("name", ""),
        "DOMAIN": c.get("domain", ""),
        "LEARNER": c.get("learner", ""),
        "CAPABILITY_TARGET": c.get("capability_target", ""),
        "PURPOSE": c.get("purpose", ""),
    }

def group_dir_name(g):
    return f"{g['id']}_{g['slug']}"

def render_group_readme(g, base):
    text = base
    mapping = {
        "GROUP_ID": g["id"],
        "GROUP_NAME": g["name"],
        "ROLE_IN_CURRICULUM": g.get("role", ""),
        "START_GATE": g.get("start_gate", ""),
        "WHY_THIS_GROUP_IS_NEEDED": g.get("role", ""),
        "GROUP_WORK_DIR": g.get("slug", "group"),
    }
    text = replace(text, mapping)

    # Replace generic exit-gate placeholder block with exact spec criteria.
    marker = "- [ ] `{{OBSERVABLE_CAPABILITY}}`\n- [ ] `{{OBSERVABLE_CAPABILITY}}`\n- [ ] `{{DISTINCTION_OR_FAILURE_BOUNDARY}}`"
    exits = g.get("exit_gate", [])
    if exits:
        text = text.replace(marker, "\n".join(f"- [ ] {x}" for x in exits))

    # Replace generic resource examples when resources are supplied.
    resources = g.get("resources", [])
    if resources:
        start = text.index("## Resource order")
        end = text.index("## What to do")
        block = ["## Resource order", ""]
        for i, r in enumerate(resources, 1):
            avail = r.get("availability", "AVAILABLE")
            role = r.get("role", "REFERENCE").replace("_", " ").lower()
            block += [f"### {i}. {avail} — {role}", "", f"**{r.get('title','Unnamed resource')}**", "", r.get("note", ""), ""]
        text = text[:start] + "\n".join(block) + "\n" + text[end:]
    return text

def render_progress(g, base):
    text = replace(base, {"GROUP_NAME": g["name"]})
    marker = "- [ ] `{{OBSERVABLE_CAPABILITY}}`\n- [ ] `{{OBSERVABLE_CAPABILITY}}`\n- [ ] `{{OBSERVABLE_CAPABILITY}}`"
    exits = g.get("exit_gate", [])
    if exits:
        text = text.replace(marker, "\n".join(f"- [ ] {x}" for x in exits))
    return text

def write_strict_order(root, spec):
    groups = spec.get("groups", [])
    spine = [g for g in groups if g.get("type") == "primary_spine"]
    branches = [g for g in groups if g.get("type") != "primary_spine"]
    lines = ["# Strict Order and Start Gates", "", "This file is generated from `CURRICULUM_SPEC.json`. Edit the spec and regenerate rather than hand-editing this file into disagreement with the machine specification.", "", "## Primary spine", ""]
    if spine:
        for i, g in enumerate(spine, 1):
            lines.append(f"{i}. `{group_dir_name(g)}` — {g['name']}")
    else:
        lines.append("No primary spine groups are currently defined.")
    lines += ["", "A primary group stops controlling progression when its core-pass exit gate is met. Deepening/reference work may continue without blocking unless the spec deliberately says otherwise.", "", "## Parallel / targeted branches", ""]
    if branches:
        lines += ["| Group | Type | Earliest start gate | Depends on |", "|---|---|---|---|"]
        for g in branches:
            deps = ", ".join(g.get("depends_on", [])) or "none"
            lines.append(f"| `{group_dir_name(g)}` | {g.get('type','')} | {g.get('start_gate','')} | {deps} |")
    else:
        lines.append("No parallel branches are currently defined.")
    lines += ["", "## Single-thread fallback", ""]
    fb = spec.get("single_thread_fallback", [])
    lines.append(" → ".join(f"`{x}`" for x in fb) if fb else "No fallback is currently defined.")
    lines += ["", "The fallback must contain no prerequisite inversions.", ""]
    (root / "00_MASTER_ROADMAP/STRICT_ORDER_AND_START_GATES.md").write_text("\n".join(lines), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--spec", help="Alternate spec JSON; copied into CURRICULUM_SPEC.json before generation")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    specp = Path(args.spec).resolve() if args.spec else root / "CURRICULUM_SPEC.json"
    spec = json.loads(specp.read_text(encoding="utf-8"))
    if args.spec:
        (root / "CURRICULUM_SPEC.json").write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")

    # Deterministically fill root identity fields that come directly from the spec.
    mapping = root_mapping(spec)
    for rel in ["AUTHORITY.md"]:
        p = root / rel
        if p.exists():
            p.write_text(replace(p.read_text(encoding="utf-8"), mapping), encoding="utf-8")

    tmpl = root / "_GROUP_TEMPLATE"
    if not tmpl.is_dir():
        raise SystemExit("Missing _GROUP_TEMPLATE")
    readme_base = (tmpl / "README.md").read_text(encoding="utf-8")
    progress_base = (tmpl / "PROGRESS.md").read_text(encoding="utf-8")
    software_base = (tmpl / "SOFTWARE.md").read_text(encoding="utf-8")
    resource_base = (tmpl / "resources/README.md").read_text(encoding="utf-8")

    for g in spec.get("groups", []):
        name = group_dir_name(g)
        dst = root / name
        if dst.exists():
            if not args.overwrite:
                print(f"SKIP {name}: exists")
                continue
            shutil.rmtree(dst)
        (dst / "resources").mkdir(parents=True)
        (dst / "README.md").write_text(render_group_readme(g, readme_base), encoding="utf-8")
        (dst / "PROGRESS.md").write_text(render_progress(g, progress_base), encoding="utf-8")
        gm = {"GROUP_NAME": g["name"], "GROUP_WORK_DIR": g.get("slug", "group")}
        (dst / "SOFTWARE.md").write_text(replace(software_base, gm), encoding="utf-8")
        (dst / "resources/README.md").write_text(replace(resource_base, {"GROUP_NAME": g["name"]}), encoding="utf-8")
        print(f"CREATED {name}")

    write_strict_order(root, spec)
    print("GENERATED 00_MASTER_ROADMAP/STRICT_ORDER_AND_START_GATES.md from spec")

if __name__ == "__main__":
    main()
