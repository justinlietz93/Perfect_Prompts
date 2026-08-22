# Package Tools

All tools use only the Python standard library.

- `init_package.py`: instantiate a named active package.
- `new_claim_notebook.py`: create a one-cell, no-I/O notebook shell.
- `validate_package.py`: validate template or strict active-package requirements.
- `build_manifest.py`: generate `MANIFEST.json` and `SHA256SUMS` from actual bytes.
- `finalize_package.py`: validate, generate integrity records, revalidate, build ZIP, and write external ZIP SHA-256.
