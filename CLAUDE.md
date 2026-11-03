# score

Le moteur de règles de la famille Ion : les règles sourcées et la note.

## Repo map

- `backend/ion_score/`: `cli.py` (`grid`, `grade`, `fix`; ion-repo builds `ion repo grid|score|fix`
  from its `add_*_arguments`/`run_*`), entry point `__main__.py`. The grid: `rules/<theme>/<ID>.toml`,
  `model.py`, `facts.py`, `detectors.py`, `forge.py` (`gh`, cached a day), `score.py`, `show.py`,
  `roadmap.py`, `gap_report.py`, `fixers/`, `fix.py`, `checks.py`, `compressor/`. Ground shared
  with ion-repo, which imports it: `ui.py`, `shell.py` (`IonError` = ion-repo's `KilnError`),
  `waivers.py`, `rule_ids.py`, `tickets.py`.
- `backend/tests/`: each rule's pass/fail examples in `test_grid.py`; `conftest.py` (git config
  aside, `gh` off).
- `docs/backlog/`; `charter.toml`; `.claude/rules/ion-repo/`.
