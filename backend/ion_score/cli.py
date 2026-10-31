"""Command-line interface: reads the arguments, calls the core, writes the result.

No computation here ([THIN-CLI]): the work lives in pure modules, tested without a terminal.
"""

import argparse
import sys
from collections.abc import Sequence
from importlib.metadata import version
from typing import TextIO

from ion_score.greeting import build_greeting

PROGRAM = "ion-score"
# The installed package the version is read from.
DISTRIBUTION = "ion-score"
EXIT_OK = 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=PROGRAM, description=__doc__)
    parser.add_argument("--version", action="version", version=f"%(prog)s {version(DISTRIBUTION)}")
    parser.add_argument("name", nargs="?", default="", help="à qui dire bonjour")
    return parser


def main(argv: Sequence[str] | None = None, out: TextIO = sys.stdout) -> int:
    args = build_parser().parse_args(argv)
    out.write(build_greeting(args.name) + "\n")
    return EXIT_OK
