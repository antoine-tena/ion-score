"""`python -m ion_score`: the same entry point as the installed command."""

import sys

from ion_score.cli import main

sys.exit(main())
