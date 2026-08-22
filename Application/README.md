# Perfect Prompts Application

This directory contains the optional desktop interface for the Perfect Prompts repository.

The application is deliberately subordinate to the library filesystem. It reads and mutates the same files visible through the operating system and GitHub; the only application-owned repository state is the disposable `.perfect-prompts/` search projection at the repository root.

## Run from source

From the repository root:

```bash
python install.py
```

For development:

```bash
cd Application
python -m venv .venv
source .venv/bin/activate
pip install -e ".[gui,pdf,dev]"
perfect-prompts --root ..
```

## Main surfaces

- **Search**: single-query Prompt Beacon search, filters, preview, open/copy/export/remove.
- **Batch**: several independent Beacon-style queries with independent exports.
- **Library**: a live native-filesystem tree with add, remove, open, reveal, and sync controls.

## Architecture

The implementation follows the supplied Lamina template principles: Python remains source of truth, application operations are separated from widgets, concrete wiring lives in a composition root, and indexing/synchronization work runs off the GUI thread.
