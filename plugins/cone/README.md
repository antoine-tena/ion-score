# Le plugin Claude Code `cone`

Ce que Claude Code sait faire avec la commande `cone` : `/cone:…`.

- `.claude-plugin/plugin.json` : son nom et sa description, sans `version` exprès (Claude Code
  suit alors les commits) ; le catalogue qui le publie est `.claude-plugin/marketplace.json`, à
  la racine du dépôt.
- `skills/` : un dossier par skill, nommé d'un verbe (`skills/<verbe>/SKILL.md`, son `name` est
  le nom du dossier) ; `run` est l'exemple de départ, à remplacer.
- Des hooks s'ajoutent dans `hooks/hooks.json`, des serveurs MCP dans `.mcp.json`.

Les sessions ouvertes dans ce dépôt l'activent (`.claude/settings.json`, à l'état de `main`).
Ailleurs : `claude plugin marketplace add antoine-tena/cone`, puis
`claude plugin install cone@cone`.
