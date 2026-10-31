---
name: run
description: Run the `ion-score` command for the user (Le moteur de règles de la famille Keramos : les règles sourcées et la note). Use when the user asks for what ion-score does, or names it.
argument-hint: "[arguments of ion-score]"
---

<!-- First skill of the plugin, the counterpart of the example command: replace it with the
tool's real skills, one folder per verb (`skills/<verb>/SKILL.md`, `name` = the folder). -->

1. Find the command: `ion-score` when it is installed on the machine (`uv tool install
   --editable backend` in its repo), otherwise `uv run --project <its repo>/backend ion-score`.
2. Run `ion-score $ARGUMENTS`; when the arguments are unclear, read `ion-score --help` first
   rather than guessing an option.
3. Report what the command printed, and its exit code when it is not 0, without hiding an error.
