from pathlib import Path
from perfect_prompts.infrastructure.settings.user_settings import UserSettingsStore


def test_settings_round_trip(tmp_path: Path):
    repo = tmp_path / "repo"; repo.mkdir()
    store = UserSettingsStore(tmp_path / "settings.json"); store.save_last_root(repo)
    assert store.load_last_root() == repo.resolve()
