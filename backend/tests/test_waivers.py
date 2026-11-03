"""The waivers file: `waivers.toml`, and the `kiln-waivers.toml` of before still read."""

import datetime
from pathlib import Path

from ion_score import waivers

WAIVER = (
    '[[waiver]]\nrule = "BARE-EXCEPT"\nreason = "legacy scripts"\nby = "a"\n'
    'since = 2026-10-20\nuntil = "never"\n'
)
TODAY = datetime.date(2026, 11, 3)


def test_waivers_toml_is_read(tmp_path: Path) -> None:
    (tmp_path / "waivers.toml").write_text(WAIVER)

    found = waivers.load(tmp_path, TODAY)

    assert [waiver.rule for waiver in found.actives] == ["BARE-EXCEPT"]
    assert not found.errors
    assert waivers.waivers_path(tmp_path) == tmp_path / "waivers.toml"


def test_kiln_waivers_toml_alone_is_still_read(tmp_path: Path) -> None:
    (tmp_path / "kiln-waivers.toml").write_text(WAIVER)

    found = waivers.load(tmp_path, TODAY)

    assert [waiver.rule for waiver in found.actives] == ["BARE-EXCEPT"]
    assert not found.errors
    assert waivers.waivers_path(tmp_path) == tmp_path / "kiln-waivers.toml"


def test_both_files_is_an_error_saying_which_to_keep(tmp_path: Path) -> None:
    (tmp_path / "waivers.toml").write_text(WAIVER)
    (tmp_path / "kiln-waivers.toml").write_text(WAIVER.replace("BARE-EXCEPT", "LOGGING"))

    found = waivers.load(tmp_path, TODAY)

    assert [waiver.rule for waiver in found.actives] == ["BARE-EXCEPT"]
    assert len(found.errors) == 1 and "keep waivers.toml" in found.errors[0]
    assert waivers.waivers_path(tmp_path) == tmp_path / "waivers.toml"


def test_without_a_file_the_new_name_is_where_a_first_waiver_goes(tmp_path: Path) -> None:
    assert waivers.waivers_path(tmp_path) == tmp_path / "waivers.toml"
    assert waivers.load(tmp_path, TODAY) == waivers.Waivers()
