from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


INSTALL_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install.py"


def _load_install_module():
    spec = importlib.util.spec_from_file_location("perfect_prompts_install_script", INSTALL_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_default_runtime_is_outside_application(monkeypatch, tmp_path):
    module = _load_install_module()
    monkeypatch.setattr(module.Path, "home", classmethod(lambda cls: tmp_path / "home"))
    monkeypatch.delenv("XDG_DATA_HOME", raising=False)
    runtime = module._default_venv_dir()
    assert runtime == tmp_path / "home" / ".local" / "share" / "perfect-prompts" / "runtime" / "venv"
    assert "Application" not in runtime.parts


def test_repair_recreates_missing_runtime(monkeypatch, tmp_path):
    module = _load_install_module()
    fake_env = tmp_path / "runtime" / "venv"
    fake_python = fake_env / "bin" / "python"
    fake_cli = fake_env / "bin" / "perfect-prompts-cli"
    fake_gui = fake_env / "bin" / "perfect-prompts"

    monkeypatch.setattr(module, "_resolve_env_dir", lambda _app, _requested: fake_env)

    installed = {"called": False}

    def fake_install_runtime(*, env_dir, application_dir, without_pdf):
        installed["called"] = True
        assert env_dir == fake_env
        fake_python.parent.mkdir(parents=True, exist_ok=True)
        for path in (fake_python, fake_cli, fake_gui):
            path.write_text("stub", encoding="utf-8")
        return fake_python, fake_cli, fake_gui

    monkeypatch.setattr(module, "_install_runtime", fake_install_runtime)
    calls = []

    def fake_run(args, check=True, **kwargs):
        calls.append([str(x) for x in args])
        class Result:
            returncode = 0
        return Result()

    monkeypatch.setattr(module.subprocess, "run", fake_run)
    monkeypatch.setattr(sys, "argv", [str(INSTALL_SCRIPT), "--repair-launcher", "--no-desktop"])

    assert module.main() == 0
    assert installed["called"] is True
    assert calls == [[str(fake_cli), "install-launcher", "--root", str(INSTALL_SCRIPT.parents[2]), "--no-desktop"]]
