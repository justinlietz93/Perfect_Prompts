# Perfect Prompts v2.0.2 Validation Report

## Scope

`v2.0.2` repairs a launcher regression introduced by the Linux icon/launcher patch in `v2.0.1`.

The underlying failure was architectural rather than icon-related: the installed Python virtual environment lived at `Application/.venv/`, while the update instructions also treated `Application/` as a replaceable tracked directory. Replacing that directory could therefore delete the executable referenced by the desktop launcher while leaving the `.desktop` file intact.

## Repair

The default desktop runtime now lives outside the tracked repository:

- Linux: `~/.local/share/perfect-prompts/runtime/venv`
- Windows: `%LOCALAPPDATA%\\PerfectPrompts\\runtime\\venv`

The repository remains installed editable into that runtime, so application source continues to come from the checked-out `Application/src/` tree while the launcher target survives normal repository/application-folder updates.

`python install.py --repair-launcher` now:

1. resolves the stable per-user runtime;
2. recreates and installs it automatically if missing;
3. preserves the existing runtime when intact;
4. skips Prompt Beacon reindexing in repair mode;
5. rewrites the native launcher against the valid runtime executable.

The explicit `--venv` option remains available for development or custom installations.

## Automated Validation

```text
22 passed
```

Coverage includes:

- Prompt Beacon behavior and filesystem synchronization;
- artifact add/remove paths;
- icon asset validity;
- Linux launcher generation and absolute icon paths;
- package/version assertions;
- stable runtime location outside `Application/`;
- automatic runtime recreation in launcher repair mode.

## Regression Gate

The specific update failure now has a test: repair mode is executed with a missing runtime and must invoke runtime installation before generating the launcher. The default runtime path is also asserted not to live beneath `Application/`.

## Result

**PASS** — application updates can replace the tracked `Application/` directory without deleting the installed desktop runtime, and repair mode can recover an already-broken launcher without requiring manual filesystem diagnosis.
