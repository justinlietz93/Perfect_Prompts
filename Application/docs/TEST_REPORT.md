# Perfect Prompts v2.0.3 Validation Report

## Regression fixed

`v2.0.2` moved the desktop runtime out of the repository, but repair mode incorrectly skipped reinstalling Perfect Prompts whenever that runtime already existed. An existing runtime could therefore still be bound by an editable install to an older checkout or a path that no longer existed. The launcher itself was valid, but launching it could fail immediately because the runtime imported the wrong source tree.

## v2.0.3 behavior

`python install.py --repair-launcher` now always refreshes the editable installation from the current repository before writing launchers. Runtime validation then imports `perfect_prompts`, `PySide6`, and the Qt main-window module and verifies that `perfect_prompts.__file__` is exactly the current repository's `Application/src/perfect_prompts/__init__.py`.

This closes both repair cases:

1. missing runtime;
2. existing runtime with stale checkout binding.

## Regression gates

- stable runtime remains outside `Application/`;
- missing runtime is recreated;
- existing runtime is still refreshed during repair;
- runtime source binding is validated before launcher generation;
- native launcher/icon behavior from v2.0.1 remains intact.
