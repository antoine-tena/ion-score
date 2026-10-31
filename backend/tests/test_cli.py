import io

import pytest

from ion_score.cli import EXIT_OK, main
from ion_score.greeting import build_greeting


def test_main_writes_greeting_to_given_stream() -> None:
    out = io.StringIO()

    assert main(["Ada"], out=out) == EXIT_OK
    assert out.getvalue() == "Bonjour, Ada !\n"


def test_version_exits_cleanly(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])

    assert exit_info.value.code == EXIT_OK
    assert capsys.readouterr().out.startswith("ion-score ")


def test_blank_name_falls_back_to_default() -> None:
    assert build_greeting("  ") == "Bonjour, monde !"
