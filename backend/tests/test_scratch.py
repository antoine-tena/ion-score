"""The throwaway worktrees of `ion repo fix`: under the ion-score cache, kiln's orphans removed."""

import subprocess
from pathlib import Path

import pytest

from ion_score import fix


def git(root: Path, *arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments], cwd=root, capture_output=True, text=True, check=True
    ).stdout


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(fix, "SCRATCH", tmp_path / "cache" / "ion-score" / "worktrees")
    monkeypatch.setattr(fix, "LEGACY_SCRATCH", tmp_path / "cache" / "kiln" / "worktrees")
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init", "-q")
    (root / "README.md").write_text("x\n")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "first")
    return root


def test_a_scratch_worktree_lives_under_the_ion_score_cache(repo: Path) -> None:
    with fix.scratch_worktree(repo, "--detach") as copy:
        assert copy.is_relative_to(fix.SCRATCH)
        assert str(copy) in git(repo, "worktree", "list")

    assert str(copy) not in git(repo, "worktree", "list")


def test_an_orphan_left_under_the_kiln_cache_is_removed(repo: Path) -> None:
    orphan = fix.LEGACY_SCRATCH / "ion-repo-fix-abc" / "repo"
    orphan.parent.mkdir(parents=True)
    git(repo, "worktree", "add", "-q", "--detach", str(orphan), "HEAD")

    with fix.scratch_worktree(repo, "--detach"):
        pass

    assert not orphan.parent.exists()
    assert str(orphan) not in git(repo, "worktree", "list")
