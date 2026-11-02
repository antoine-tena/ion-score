"""Command-line interface: reads the arguments, calls the grid, writes the result.

No computation here ([THIN-CLI]): the work lives in the grid's modules. ion-repo builds its
`ion repo grid`, `ion repo score` and `ion repo fix` from the same `add_*_arguments` and `run_*`.
"""

import argparse
import sys
from collections.abc import Callable, Sequence
from importlib.metadata import version
from pathlib import Path
from typing import TextIO

from ion_score import score
from ion_score.model import LEVELS, THEMES
from ion_score.shell import IonError

PROGRAM = "ion-score"
# The installed package the version is read from.
DISTRIBUTION = "ion-score"
EXIT_OK = 0
EXIT_FAILURE = 1

# Asks the user a question, returns the answer; None: nobody to ask (a script, an agent).
type Ask = Callable[[str], str] | None


def add_grid_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("rule", nargs="?", help="one rule, in full (its ID)")
    parser.add_argument("--theme", choices=THEMES, help="only this theme")
    parser.add_argument("--scope", help="universal, language, framework, tool, domain, or a name")
    parser.add_argument("--level", choices=LEVELS, help="only this level")


def add_score_arguments(parser: argparse.ArgumentParser) -> None:
    _add_path_argument(parser)
    parser.add_argument("--json", action="store_true", help="the report as JSON")
    parser.add_argument("--all", action="store_true", help="every rule and every location")
    parser.add_argument("--badge", action="store_true", help="a README badge (Markdown)")
    parser.add_argument(
        "--online",
        action="store_true",
        help="refresh end-of-life dates from endoflife.date and the GitHub settings",
    )
    parser.add_argument(
        "--roadmap", action="store_true", help="what needs judgment, for Claude, with its places"
    )
    parser.add_argument(
        "--write", action="store_true", help="with --roadmap: the items as backlog tickets"
    )
    parser.add_argument("--rule", help="one rule only: fails while its gap is open")
    parser.add_argument(
        "--against", metavar="REF", help="the change since a commit (a pull request's base)"
    )


def add_fix_arguments(parser: argparse.ArgumentParser) -> None:
    _add_path_argument(parser)
    parser.add_argument("--dry-run", action="store_true", help="the plan and the diff only")
    parser.add_argument("--rule", help="only this rule (its ID)")


def _add_path_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "path", type=Path, nargs="?", default=Path(), help="the repo (default: here)"
    )


def run_grid(arguments: argparse.Namespace, out: TextIO) -> None:
    from ion_score import show

    if arguments.rule:
        _write(out, show.rule_card(arguments.rule))
    else:
        rules = show.rule_list(theme=arguments.theme, scope=arguments.scope, level=arguments.level)
        _write(out, rules)


def run_score(arguments: argparse.Namespace, ask: Ask, out: TextIO) -> None:
    """`ask`: who says yes to reporting the gaps upstream; None outside a person's terminal."""
    root = arguments.path.resolve()
    if not root.is_dir():
        raise IonError(f"no folder {arguments.path}")
    if arguments.online:
        from ion_score import forge

        score.refresh_end_of_life()
        forge.REFRESH = True
    report = score.score_repo(root)
    if arguments.against:
        from ion_score import fix

        with fix.scratch_worktree(root, "--detach", ref=arguments.against) as copy:
            _write(out, score.compared(score.score_repo(copy), report))
    elif arguments.rule or arguments.roadmap:
        _run_roadmap(arguments, root, report, out)
    elif arguments.json:
        _write(out, [score.as_json(report)])
    elif arguments.badge:
        _write(out, [score.badge(report)])
    else:
        from ion_score import gap_report

        _write(out, score.screen(report, every=arguments.all))
        gap_report.offer(root, report, ask)


def _run_roadmap(
    arguments: argparse.Namespace, root: Path, report: score.Report, out: TextIO
) -> None:
    from ion_score import roadmap

    if arguments.rule:
        found = score.rule_finding(report, arguments.rule)
        _write(out, roadmap.rule_screen(found, arguments.rule))
        if found is not None and roadmap.is_open(found):
            raise roadmap.still_open(found)
        return
    if arguments.write:
        written = roadmap.write_tickets(root, report)
        _write(
            out, [f"{len(written)} ticket(s) written in {roadmap.BACKLOG}: {', '.join(written)}"]
        )
    _write(out, roadmap.screen(report))


def run_fix(arguments: argparse.Namespace) -> None:
    from ion_score import fix

    fix.fix(arguments.path.resolve(), dry_run=arguments.dry_run, only=arguments.rule)


def _write(out: TextIO, lines: list[str]) -> None:
    out.write("".join(f"{line}\n" for line in lines))
    out.flush()


def is_interactive() -> bool:
    return sys.stdin.isatty() and sys.stdout.isatty()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=PROGRAM, description=__doc__)
    parser.add_argument("--version", action="version", version=f"%(prog)s {version(DISTRIBUTION)}")
    commands = parser.add_subparsers(dest="command", required=True)
    add_grid_arguments(commands.add_parser("grid", help="the rules held as the best, with sources"))
    add_score_arguments(
        commands.add_parser("grade", help="any repo measured against the grid, in seconds")
    )
    add_fix_arguments(
        commands.add_parser("fix", help="close by script every gap a script can close")
    )
    return parser


def main(
    argv: Sequence[str] | None = None, out: TextIO | None = None, err: TextIO | None = None
) -> int:
    """`out`, `err`: standard output and error unless given, read at the call (tests capture)."""
    out, err = out or sys.stdout, err or sys.stderr
    arguments = build_parser().parse_args(argv)
    try:
        if arguments.command == "grid":
            run_grid(arguments, out)
        elif arguments.command == "grade":
            # Only a person at a terminal says yes: a script or a Claude session is never asked.
            run_score(arguments, input if is_interactive() else None, out)
        else:
            run_fix(arguments)
    except IonError as error:
        err.write(f"{PROGRAM}: {error}\n")
        return EXIT_FAILURE
    return EXIT_OK
