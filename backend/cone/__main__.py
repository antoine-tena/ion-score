"""`python -m cone`: the same entry point as the installed command."""

import sys

from cone.cli import main

sys.exit(main())
