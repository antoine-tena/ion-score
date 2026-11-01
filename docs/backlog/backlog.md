# Backlog

Everything left to do on score, in a single list ordered by priority. Started on
**2026-10-29**. How to write a ticket: [README.md](README.md); closed tickets are in
[done.md](done.md), what was turned down in [rejected.md](rejected.md). **Nothing else is open.**

North star: **Chaque règle sourcée et notée**.

**Next free: ion-score#T-03.**

---

## 🔴 Critical

### ion-score#T-02 · Finish the ion-repo update to v0.4.11
- **Type**: task
- **Status**: todo
- **Opened**: 2026-11-01
- **Effort**: XS · **Owner**: — · **Due**: —
- **Origin**: release notes of the ion-repo releases crossed (`ion repo update`)

What ion-repo cannot guess, to fill in right after the update (`/repo:update`):
- [ ] run `ion repo install --machine` once on each machine, so that its Claude Code catalogue moves from kiln to ion-repo. (v0.4.11)

## 🟠 Important

### T-01 · Reprendre de ion-repo la grille : règles, modèle, détecteurs, note
- **Type**: task
- **Status**: blocked — waiting for ion-repo T-394 (comment un outil arrive dans un repo) ; à faire après la bascule de ion-render
- **Opened**: 2026-10-30
- **Effort**: L · **Owner**: — · **Due**: —
- **Origin**: décision d'antoine du 2026-10-30, répartir ce que ion-repo porte hors de son métier ;
  la carte de la famille dit déjà « ion-score : règles sourcées et note, aujourd'hui la grille de ion-repo »

La grille vit dans `src/kiln/grid/` de ion-repo (143 règles dans `rules/<thème>/<ID>.toml`).
Partage retenu : ion-score prend ce qui **juge** ; ion-repo garde ce qui **modifie un repo**.

- [ ] Viennent dans ion-score : `rules/`, `model.py`, `facts.py`, `detectors.py`, `forge.py`,
  `score.py`, `show.py`, avec leurs tests et l'exemple réussi et raté de chaque règle.
- [ ] Restent dans ion-repo, appelant ion-score : `ion repo score`, `ion repo grid`, `fixers/`, `fix.py`,
  `checks.py`, `roadmap.py`. À trancher en le faisant : `gap_report.py`, `compressor/`.
- [ ] Le lien `charter_rule` des règles vers le moteur `charter` de ion-repo : garder une seule
  source pour les ID.
- [ ] Le contrat entre ion-score et ion-repo écrit (`docs/contract.md`, comme ion-render), versionné.
- [ ] ion-score sur PyPI (`ion-score`) et public avant que ion-repo en dépende : ion-repo est public.
- [ ] Mesuré : même note, règle par règle, avant et après, sur les repos d'entraînement.

Côté ion-repo : T-393.

## 🟡 Normal

## ⚪ Background — long-running work, debt and ideas
