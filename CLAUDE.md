# score

Le moteur de règles de la famille Ion : les règles sourcées et la note.

<!-- This file belongs to the project: ion-repo wrote it once and never changes it. ion-repo's rules live
in .claude/rules/ion-repo/ and are kept current by `ion repo update`. Write here what Claude cannot
guess about this project, and keep it under 200 lines: every session reads it. -->

## Repo map

Where to look, so as not to explore: read it before opening files, and update it in the commit
that adds, moves or removes a directory, a domain or an entry point. One line per place, what
it holds; no copy of the code.

- `backend/ion_score/`: commands (`cli.py`, entry point `__main__.py`) and
  business logic; `backend/tests/`: tests.
- `docs/backlog/`: the work to do; `charter.toml`: the checked rules; `.claude/rules/ion-repo/`:
  ion-repo's rules for Claude.

## Notes

<!-- Decisions, conventions and pitfalls of this project that Claude cannot guess from the code:
"we never call X directly, always through Y", "the staging database is reset every night"… -->
