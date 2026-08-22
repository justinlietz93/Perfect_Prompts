# Publication Tools

- `init_publication.py`: create an active package and seed exact source lineage.
- `new_claim_notebook.py`: create a code-only one-claim notebook scaffold.
- `compile_paper.py`: stage declared inputs and compile `paper.pdf` cleanly.
- `build_arxiv_bundle.py`: create and clean-test `arxiv-source.zip`.
- `build_manifest.py`: generate exact file hashes and `SHA256SUMS`.
- `validate_publication.py`: enforce template or release closure rules.
- `finalize_publication.py`: compile, bundle, hash, strict-validate, freeze, and clean-extraction test the release.

All tools use the Python standard library except the external TeX engine invoked for compilation.
