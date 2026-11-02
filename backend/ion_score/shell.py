"""Running external commands (git, uv, pnpm, gh) and the error shown to the user.

ion-repo runs its own commands through this module: one error class and one spinner for both.
"""

import os
import subprocess
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from ion_score import ui


class IonError(Exception):
    """Expected error, shown to the user without a traceback."""


ENV_PREFIX = "ION_REPO_"
# The variables' prefix before the Ion family (kiln until 31 October 2026), still read.
LEGACY_ENV_PREFIX = "KILN_"
# Full output of the commands, without the spinner (diagnosis).
VERBOSE_VARIABLE = "ION_REPO_VERBOSE"


def environment(variable: str) -> str | None:
    """An `ION_REPO_…` variable of the environment, or the `KILN_…` it was called before."""
    value = os.environ.get(variable)
    if value is None and variable.startswith(ENV_PREFIX):
        value = os.environ.get(LEGACY_ENV_PREFIX + variable.removeprefix(ENV_PREFIX))
    return value


def run(
    command: list[str], cwd: Path, env: dict[str, str] | None = None, *, live: bool = False
) -> None:
    """Runs a command; fails if it fails. `live`: output shown as is, for an interactive command
    or one whose output is the result."""
    returncode = run_status(command, cwd, env, live=live)
    if returncode != 0:
        raise IonError(f"`{' '.join(command)}` failed (code {returncode})")


def run_status(
    command: list[str], cwd: Path, env: dict[str, str] | None = None, *, live: bool = False
) -> int:
    """Runs a command and returns its code. In a terminal, a spinner replaces its output, shown
    in full only if it fails."""
    if live or not shows_spinner():
        return subprocess.run(command, cwd=cwd, env=env, check=False).returncode
    spinner = ui.Spinner(" ".join(command))
    output: list[str] = []
    spinner.start()
    try:
        process = subprocess.Popen(
            command,
            cwd=cwd,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            errors="replace",
        )
        for line in process.stdout or ():
            output.append(line)
            spinner.show(line)
        returncode = process.wait()
    finally:
        spinner.stop()
    spinner.finish(succeeded=returncode == 0, output="".join(output))
    return returncode


def shows_spinner() -> bool:
    """Whether a spinner replaces what runs: in a terminal, unless the full output is asked for."""
    return ui.is_styled() and not environment(VERBOSE_VARIABLE)


@contextmanager
def spinner_line(label: str) -> Iterator[None]:
    """Work done in ion-repo itself shown like a command: the spinner, then ✓ or ✗ and its
    duration."""
    spinner = ui.Spinner(label)
    spinner.start()
    succeeded = False
    try:
        yield
        succeeded = True
    finally:
        spinner.finish(succeeded=succeeded)


def capture(command: list[str], cwd: Path) -> str:
    """Runs a command and returns its standard output, stripped."""
    completed = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        raise IonError(f"`{' '.join(command)}` failed: {completed.stderr.strip()}")
    return completed.stdout.strip()


INSTALL_HINTS = {
    "git": "https://git-scm.com/downloads",
    "uv": "curl -LsSf https://astral.sh/uv/install.sh | sh",
    "pnpm": "npm install -g pnpm (Node 24 required)",
    "gh": "https://cli.github.com, then gh auth login",
}
