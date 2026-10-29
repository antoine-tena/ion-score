# cone

Le moteur de règles de la famille Keramos : les règles sourcées et la note.

## Démarrage rapide

Après le clone, depuis la racine du dépôt (prérequis : [uv](https://docs.astral.sh/uv/)) :

```sh
uv tool install kiln-cli   # une fois par poste
kiln install
```

Puis lancer l'outil : `cd backend && uv run cone --help`, ou l'installer sur le poste par
`uv tool install --editable backend`.

## Équipe

- [@antoine-tena](https://github.com/antoine-tena)
- [@amnkd555](https://github.com/amnkd555)

## Organisation

- `backend/` : l'outil en ligne de commande `cone`.
- [`CLAUDE.md`](CLAUDE.md) et [`.claude/rules/kiln/`](.claude/rules/kiln/) : la charte du code
  et la façon de travailler, pour les humains comme pour les agents.
- `.vscode/` : réglages et extensions recommandées, partagés par toute l'équipe.
- `plugins/cone/` et `.claude-plugin/marketplace.json` : le plugin Claude Code de la
  commande, et le catalogue qui le publie.

Le projet est généré et tenu à jour par [kiln](https://github.com/antoine-tena/kiln). Changer un
paramètre (équipe, frameworks, podman…) : `kiln set <clé>=<valeur>`, sur une branche.

## Installation

Prérequis : ceux du démarrage rapide.
`kiln install` installe les dépendances (backend) et active les garde-fous du
commit (pre-commit, dont le refus de commiter sur `main` ou `develop`). On peut la relancer sans
risque.

## Lancer le projet

```sh
cd backend && uv run cone --help
uv tool install --editable backend   # depuis la racine : la commande sur tout le poste
```

## Vérifier le code

```sh
kiln check
```

Ruff, mypy et pytest pour chaque projet Python, puis la charte (`charter`).

## Mettre à jour

Sur une branche dédiée, avec un arbre propre : `kiln update` (mises à jour compatibles) ou
`kiln update --major` (versions majeures comprises). La commande rapporte les évolutions de kiln
sans écraser les modifications locales, met à jour les dépendances, puis lance les contrôles.
Avec Claude Code, le skill `/kiln:update` fait tout : l'outil kiln, puis le dépôt.

## Suivi du travail

Ce qui reste à faire est dans [`docs/backlog/`](docs/backlog/) : `backlog.md` (les tickets, par
priorité), `done.md` (ceux qui sont faits), `rejected.md` (ce qui a été refusé) et `urgent.md` (ce que seul un humain peut faire).

## Contribuer

1. Créer une branche depuis `develop` : `feat/…`, `fix/…` ([BRANCHES]).
2. Respecter la charte ([`.claude/rules/kiln/`](.claude/rules/kiln/), [`CLAUDE.md`](CLAUDE.md)).
3. Fusionner la branche dans `develop` (`git merge --no-ff`, puis push), sans attendre
   d'approbation : skill `/kiln:merge` avec Claude Code. Une pull request reste possible pour
   demander un avis. On ne commite jamais directement sur `main` ou `develop`.
