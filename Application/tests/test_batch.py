from pathlib import Path
from perfect_prompts.application.use_cases.batch_query import BatchQuery, split_batch_queries
from perfect_prompts.infrastructure.search.prompt_beacon import PromptBeaconIndex


def test_batch_split_preserves_quoted_commas():
    assert split_batch_queries('alpha,"beta,gamma",delta') == ["alpha", '"beta,gamma"', "delta"]


def test_batch_exports_each_query(tmp_path: Path):
    p = tmp_path / "Prompts" / "Portable" / "Plaintext"; p.mkdir(parents=True)
    (p / "p.txt").write_text("alpha beta gamma", encoding="utf-8")
    index = PromptBeaconIndex(tmp_path); index.rebuild()
    results = BatchQuery(index, tmp_path).execute("alpha\nbeta")
    assert len(results) == 2 and all(Path(item.export_path).exists() for item in results)
