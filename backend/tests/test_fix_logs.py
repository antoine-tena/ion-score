"""The logs of reverted converters: under `.git/ion-score/fix`, kiln's old place still read."""

import subprocess
from pathlib import Path

import pytest

from ion_score import checks

FAILURE = checks.Result(checks.Check(("pytest",)), checks.RED, "1 failed")


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    return tmp_path


def test_a_log_is_kept_under_the_ion_score_place(repo: Path) -> None:
    path = checks.keep_log(repo, "BARE-EXCEPT", FAILURE)

    assert path == repo / ".git" / "ion-score" / "fix" / "BARE-EXCEPT.log"
    assert checks.reverted(repo) == {"BARE-EXCEPT": path}


def test_a_log_under_the_kiln_place_of_before_is_still_read_and_forgotten(repo: Path) -> None:
    legacy = repo / ".git" / "kiln" / "fix"
    legacy.mkdir(parents=True)
    (legacy / "BARE-EXCEPT.log").write_text("$ pytest\n1 failed")

    assert checks.reverted(repo) == {"BARE-EXCEPT": legacy / "BARE-EXCEPT.log"}

    checks.forget_log(repo, "BARE-EXCEPT")

    assert checks.reverted(repo) == {}
