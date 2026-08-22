# Tools

- `init_curriculum.py` — deterministically fills root identity fields, scaffolds group folders from `CURRICULUM_SPEC.json`, populates specified resources/exit gates, and regenerates `STRICT_ORDER_AND_START_GATES.md`. It never invents curriculum content.
- `validate_curriculum.py` — checks required structure, duplicate/unknown group IDs, dependency cycles, fallback references, group files, and unresolved placeholders in authoritative files.
- `build_manifest.py` — writes `MANIFEST.json` and `SHA256SUMS`.

Recommended order:

```bash
python tools/init_curriculum.py . --spec examples/CURRICULUM_SPEC.example.json --overwrite
python tools/validate_curriculum.py .
python tools/build_manifest.py .
```

The example command is for testing. Use your own completed spec for a real curriculum.
