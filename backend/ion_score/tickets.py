"""Ticket identifiers of a repo's backlog: `<repo>#T-NN`, the prefix being the repo's name.

The same naming as ion-repo's `ion repo tickets`: the name of `.copier-answers.yml`, else of
`pyproject.toml`, else the folder of the main tree (a worktree's folder is named after its branch).
"""

import re
import tomllib
from pathlib import Path

import yaml

from ion_score.shell import IonError, capture

REPO_PREFIX = r"[a-z][a-z0-9-]*#"
NEXT_FREE = re.compile(rf"Next free: (?:{REPO_PREFIX})?T-(\d+)")
ANSWERS_FILE = ".copier-answers.yml"
# The key of the name in the answers, and the one ion-repo wrote before 0.4.0.
NAME_KEYS = ("name", "nom")
FALLBACK_PREFIX = "projet"


def repo_name(root: Path) -> str:
    """The prefix of this repo's tickets."""
    return _declared_name(root) or _folder_name(root)


def ticket_id(root: Path, number: int) -> str:
    return f"{repo_name(root)}#T-{number:02d}"


def _declared_name(root: Path) -> str | None:
    answers_path = root / ANSWERS_FILE
    if answers_path.is_file():
        answers = yaml.safe_load(answers_path.read_text())
        if isinstance(answers, dict):
            for key in NAME_KEYS:
                if isinstance(answers.get(key), str) and answers[key]:
                    return str(answers[key])
    pyproject = root / "pyproject.toml"
    if pyproject.is_file():
        declared = tomllib.loads(pyproject.read_text()).get("project", {}).get("name")
        if isinstance(declared, str) and declared:
            return declared
    return None


def _folder_name(root: Path) -> str:
    """Short name in the template's format (lowercase, digits, dashes)."""
    try:
        common = capture(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], root)
        folder = Path(common).parent.name
    except IonError, OSError:  # not a git repo, or no such folder yet
        folder = root.name
    name = re.sub(r"[^a-z0-9]+", "-", folder.lower()).strip("-")
    return name if re.match(r"[a-z]", name) else f"{FALLBACK_PREFIX}-{name}".rstrip("-")
