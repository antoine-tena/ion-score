import io
from pathlib import Path

import pytest

from ion_score.cli import EXIT_FAILURE, EXIT_OK, main


def test_version_exits_cleanly(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])

    assert exit_info.value.code == EXIT_OK
    assert capsys.readouterr().out.startswith("ion-score ")


def test_grid_shows_a_rule_on_the_given_stream() -> None:
    out = io.StringIO()

    assert main(["grid", "PINNED-ACTIONS"], out=out) == EXIT_OK
    assert "PINNED-ACTIONS" in out.getvalue()


def test_an_expected_error_is_one_line_without_traceback(tmp_path: Path) -> None:
    err = io.StringIO()

    assert main(["grade", str(tmp_path / "nowhere")], err=err) == EXIT_FAILURE
    assert err.getvalue() == f"ion-score: no folder {tmp_path / 'nowhere'}\n"
