# score

Le moteur de règles de la famille Ion : les règles sourcées et la note.

## Démarrage rapide

Après le clone, depuis la racine du dépôt (prérequis : [uv](https://docs.astral.sh/uv/)) :

```sh
uv tool install ion-sh && ion add repo   # une fois par poste
ion repo install
```

Puis lancer l'outil : `cd backend && uv run ion-score --help`, ou l'installer sur le poste par
`uv tool install --editable backend`.

## Équipe

- [@antoine-tena](https://github.com/antoine-tena)

## Organisation

- `backend/` : l'outil en ligne de commande `ion-score`.
- [`CLAUDE.md`](CLAUDE.md) et [`.claude/rules/ion-repo/`](.claude/rules/ion-repo/) : la charte du code
  et la façon de travailler, pour les humains comme pour les agents.
- `.vscode/` : réglages et extensions recommandées, partagés par toute l'équipe.
- `plugins/score/` et `.claude-plugin/marketplace.json` : le plugin Claude Code de la
  commande, et le catalogue qui le publie.

Le projet est généré et tenu à jour par [ion-repo](https://github.com/antoine-tena/ion-repo). Changer un
paramètre (équipe, frameworks, podman…) : `ion repo set <clé>=<valeur>`, sur une branche.

## Installation

Prérequis : ceux du démarrage rapide.
`ion repo install` installe les dépendances (backend) et active les garde-fous du
commit (pre-commit, dont le refus de commiter sur `main` ou `develop`). On peut la relancer sans
risque.

## Lancer le projet

```sh
cd backend && uv run ion-score --help
uv tool install --editable backend   # depuis la racine : la commande sur tout le poste
```

## Vérifier le code

```sh
ion repo check
```

Ruff, mypy et pytest pour chaque projet Python, puis la charte (`charter`).

## Mettre à jour

Sur une branche dédiée, avec un arbre propre : `ion repo update` (mises à jour compatibles) ou
`ion repo update --major` (versions majeures comprises). La commande rapporte les évolutions d'ion-repo
sans écraser les modifications locales, met à jour les dépendances, puis lance les contrôles.
Avec Claude Code, le skill `/repo:update` fait tout : l'outil ion-repo, puis le dépôt.

## Suivi du travail

Ce qui reste à faire est dans [`docs/backlog/`](docs/backlog/) : `backlog.md` (les tickets, par
priorité), `done.md` (ceux qui sont faits), `rejected.md` (ce qui a été refusé) et `urgent.md` (ce que seul un humain peut faire).

## Contribuer

1. Créer une branche depuis `develop` : `feat/…`, `fix/…` ([BRANCHES]).
2. Respecter la charte ([`.claude/rules/ion-repo/`](.claude/rules/ion-repo/), [`CLAUDE.md`](CLAUDE.md)).
3. Fusionner la branche dans `develop` (`git merge --no-ff`, puis push), sans attendre
   d'approbation : skill `/repo:merge` avec Claude Code. Une pull request reste possible pour
   demander un avis. On ne commite jamais directement sur `main` ou `develop`.
