---
name: run
description: Run the `cone` command for the user (Le moteur de règles de la famille Keramos : les règles sourcées et la note). Use when the user asks for what cone does, or names it.
argument-hint: "[arguments of cone]"
---

<!-- First skill of the plugin, the counterpart of the example command: replace it with the
tool's real skills, one folder per verb (`skills/<verb>/SKILL.md`, `name` = the folder). -->

1. Find the command: `cone` when it is installed on the machine (`uv tool install
   --editable backend` in its repo), otherwise `uv run --project <its repo>/backend cone`.
2. Run `cone $ARGUMENTS`; when the arguments are unclear, read `cone --help` first
   rather than guessing an option.
3. Report what the command printed, and its exit code when it is not 0, without hiding an error.
