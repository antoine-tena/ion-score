import subprocess
from pathlib import Path

from ion_score.tickets import NEXT_FREE, repo_name, ticket_id


def test_the_answers_name_the_tickets(tmp_path: Path) -> None:
    (tmp_path / ".copier-answers.yml").write_text("name: atelier\n")

    assert ticket_id(tmp_path, 7) == "atelier#T-07"


def test_without_answers_pyproject_then_the_main_tree_folder(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text('[project]\nname = "outil"\n')
    assert repo_name(tmp_path) == "outil"

    main = tmp_path / "Mon Repo"
    subprocess.run(["git", "init", "-q", str(main)], check=True)
    assert repo_name(main) == "mon-repo"


def test_next_free_reads_with_or_without_prefix() -> None:
    prefixed = NEXT_FREE.search("Next free: ion-score#T-12")
    bare = NEXT_FREE.search("Next free: T-03")

    assert prefixed is not None and prefixed[1] == "12"
    assert bare is not None and bare[1] == "03"
