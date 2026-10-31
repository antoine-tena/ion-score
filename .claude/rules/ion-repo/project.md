<!-- Written by ion-repo and kept current by `ion repo update`: do not edit, it would be overwritten.
Project rules go in CLAUDE.md or in .claude/rules/ outside ion-repo/. -->
# score: working here

Le moteur de règles de la famille Ion : les règles sourcées et la note.

Size: **Small**, a small app or site, one or two people, low stakes (`ion repo set size=…` changes it).
Backend a Python command-line tool in `backend/`.
The repo is generated and kept current by [ion-repo](https://github.com/antoine-tena/ion-repo).

## Commands
- `cd backend && uv run ion-score --help`: run the tool; `uv tool install --editable backend`
  installs it on the machine.
- `ion repo check`: every check of the stack (ruff, mypy, pytest), then `charter`.
  Run it before saying a change is done.
- A Python dependency: `uv add <package>` in its directory (`--dev` for a tool); never pip.
- `ion repo update`: ion-repo's improvements and compatible dependency upgrades, on a branch, checks
  included; `ion repo set key=value` changes a setting of the project (stack, team, podman…).

## Language
- Talk with the user in French. Docs (README, `docs/`), commit messages, code
  comments, tickets and the texts users read are in French too.
- Code identifiers are always English. The keywords of `docs/backlog/` (`Type`, `Status`,
  `todo`, section titles) stay English whatever the language.

## Where the state of the project lives

- The README describes the project as it is now: a change to a command, a setting, a route or a
  way of running the project updates it in the same branch, never "later".

- `docs/backlog/` is the only up-to-date list of work: `backlog.md` (open tickets `T-NN` by
  priority, how to write them in its `README.md`), `done.md` (closed ones), `rejected.md` (what was turned down), `urgent.md`
  (what only a human of the team can do). Skill `/repo:backlog`.
- `.claude/`: committed, `settings.json`, `skills/` (the project's own skills), `rules/`,
  `hooks/` (the scripts of its own hooks) and `plans/` (plan mode's plans); local, ignored by
  git, `settings.local.json`, `worktrees/`, `memory/` and `sessions/`.
- `charter.toml`: the checked rules and their budgets; `kiln-waivers.toml`: deliberate
  deviations; `.copier-answers.yml`: the project's settings for ion-repo (changed by `ion repo set`,
  never by hand).

## Git

- **[NO-COMMIT-ON-MAIN]** Never commit on `main` nor on `develop`: always a dedicated branch,
  preferably in its own worktree (`/repo:worktree`, under `.claude/worktrees/`), so that two
  sessions never cross in the main tree. It is merged into `develop` by `/repo:merge`, directly:
  no pull request nor approval required (a PR stays possible to ask for an opinion). Enforced by
  the `no-commit-to-branch` pre-commit hook, ion-repo's branch guard, and GitHub rulesets (`develop`
  can be neither deleted nor force-pushed; `main` only takes releases, through `/repo:release`).
- **[BRANCHES]** Prefixes `feat/`, `fix/`, `refactor/`, `test/`, `chore/`, `docs/`; lowercase,
  no spaces (`feat/station-map`).
- **[COMMITS]** Small and atomic: 10 files at most, a title of 50
  characters at most, prefixed by its type with an optional scope (`feat:`, `fix:`,
  `refactor:`, `style:`, `docs:`, `perf:`, `test:`, `build:`, `ci:`, `chore:`, `revert:`;
  `fix(map): …`). Whether a commit says Claude helped (`Co-Authored-By: Claude`)
  is each machine's choice (`ion repo set ai_trailers=disclose|never`, ion-repo's branch guard enforces
  it); never a `Claude-Session:` line, never `--author`: the author stays the one of
  `git config`.
- **[MERGE]** Merge commits (`git merge --no-ff`), never squash nor rebase onto the integration
  branch; then the branch goes, local and remote, with its worktree (`/repo:merge`).

## Way of working

- **[REPRODUCE-FIRST]** A bug is reproduced, by a failing test or a command, before it is fixed.
  A diagnosis, one's own or another session's, is checked on a copy first.
- **[DIRECT-LINKS]** A step asked of a human online (a console, a back office, a form) comes with
  its direct link, as precise as possible, never a menu path.
