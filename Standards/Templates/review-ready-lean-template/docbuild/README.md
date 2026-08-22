# docbuild

This nested project follows the `doc-gen4` recommendation of building docs from a dedicated
subproject.

First run:

```bash
cd docbuild
lake update ReviewReadyTemplate
lake update doc-gen4
```

In a real project, commit the generated `docbuild/lake-manifest.json` after the first update so
that documentation builds are pinned and reproducible.
