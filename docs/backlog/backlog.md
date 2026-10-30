# Backlog

Everything left to do on cone, in a single list ordered by priority. Started on
**2026-10-29**. How to write a ticket: [README.md](README.md); closed tickets are in
[done.md](done.md), what was turned down in [rejected.md](rejected.md). **Nothing else is open.**

North star: **Chaque règle sourcée et notée**.

**Next free: T-02.**

---

## 🔴 Critical

## 🟠 Important

### T-01 · Reprendre de kiln la grille : règles, modèle, détecteurs, note
- **Type**: task
- **Status**: blocked — waiting for kiln T-394 (comment un outil arrive dans un repo) ; à faire après la bascule de slake
- **Opened**: 2026-10-30
- **Effort**: L · **Owner**: — · **Due**: —
- **Origin**: décision d'antoine du 2026-10-30, répartir ce que kiln porte hors de son métier ;
  la carte de la famille dit déjà « cone : règles sourcées et note, aujourd'hui la grille de kiln »

La grille vit dans `src/kiln/grid/` de kiln (143 règles dans `rules/<thème>/<ID>.toml`).
Partage retenu : cone prend ce qui **juge** ; kiln garde ce qui **modifie un repo**.

- [ ] Viennent dans cone : `rules/`, `model.py`, `facts.py`, `detectors.py`, `forge.py`,
  `score.py`, `show.py`, avec leurs tests et l'exemple réussi et raté de chaque règle.
- [ ] Restent dans kiln, appelant cone : `kiln score`, `kiln grid`, `fixers/`, `fix.py`,
  `checks.py`, `roadmap.py`. À trancher en le faisant : `gap_report.py`, `compressor/`.
- [ ] Le lien `charter_rule` des règles vers le moteur `charter` de kiln : garder une seule
  source pour les ID.
- [ ] Le contrat entre cone et kiln écrit (`docs/contract.md`, comme slake), versionné.
- [ ] cone sur PyPI (`keramos-cone`) et public avant que kiln en dépende : kiln est public.
- [ ] Mesuré : même note, règle par règle, avant et après, sur les repos d'entraînement.

Côté kiln : T-393.

## 🟡 Normal

## ⚪ Background — long-running work, debt and ideas
