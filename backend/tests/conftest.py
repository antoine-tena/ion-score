from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def git_identity(tmp_path_factory: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch) -> None:
    """Tests away from the machine's git config, with an identity as on GitHub's CI, which has
    none: otherwise a test that passes here fails there."""
    config = Path(tmp_path_factory.mktemp("git")) / "gitconfig"
    config.write_text("[user]\n\tname = Test\n\temail = test@example.com\n")
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", str(config))
    monkeypatch.setenv("GIT_CONFIG_NOSYSTEM", "1")
    # Never the machine's GitHub through gh: a test that needs settings gives its own.
    monkeypatch.setattr("ion_score.forge.ENABLED", False)
