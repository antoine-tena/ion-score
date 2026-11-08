# Backlog

Everything left to do on score, in a single list ordered by priority. Started on
**2026-10-29**. How to write a ticket: [README.md](README.md); closed tickets are in
[done.md](done.md), what was turned down in [rejected.md](rejected.md). **Nothing else is open.**

North star: **Chaque règle sourcée et notée**.

**Next free: ion-score#T-6.**

---

## 🔴 Critical

### ion-score#T-04 · Finish the ion-repo update to v0.4.15
- **Type**: task
- **Status**: todo
- **Opened**: 2026-11-09
- **Effort**: XS · **Owner**: — · **Due**: —
- **Origin**: release notes of the ion-repo releases crossed (`ion repo update`)

What ion-repo cannot guess, to fill in right after the update (`/repo:update`):
- [ ] run `ion repo install --machine` so the status line runs on ion-repo's Python (it stayed empty on macOS). (v0.4.13)
- [ ] run `ion repo tickets` if the update had nobody to ask. (v0.4.14)

### ion-score#T-02 · Finish the ion-repo update to v0.4.11
- **Type**: task
- **Status**: todo
- **Opened**: 2026-11-01
- **Effort**: XS · **Owner**: — · **Due**: —
- **Origin**: release notes of the ion-repo releases crossed (`ion repo update`)

What ion-repo cannot guess, to fill in right after the update (`/repo:update`):
- [ ] run `ion repo install --machine` once on each machine, so that its Claude Code catalogue moves from kiln to ion-repo. (v0.4.11)

## 🟠 Important

### ion-score#T-01 · Reprendre de ion-repo la grille : règles, modèle, détecteurs, note
- **Type**: task
- **Status**: in progress — branch feat/grid-from-ion-repo, since 2026-11-02
- **Opened**: 2026-10-30
- **Effort**: L · **Owner**: — · **Due**: —
- **Origin**: décision d'antoine du 2026-10-30, répartir ce que ion-repo porte hors de son métier ;
  la carte de la famille dit déjà « ion-score : règles sourcées et note, aujourd'hui la grille de ion-repo »

Décision d'antoine du 2026-11-02 : toute la grille vient (correctifs, roadmap, rapport d'écarts
compris) ; ion-repo dépend du paquet `ion-score`, sans sous-processus, et en importe aussi le socle
commun (`ui`, `shell`, `waivers`, `rule_ids`).

- [x] La grille entière dans `backend/ion_score/`, historique gardé (git filter-repo), ses tests.
- [x] `ion repo grid|score|fix` appellent `ion_score.cli` ; `ion-score grid|grade|fix` en propre.
- [x] Une seule source pour les ID de règles (`rule_ids.py`), lue par le `charter` de ion-repo.
- [ ] Le contrat entre ion-score et ion-repo écrit (`docs/contract.md`, comme ion-render), versionné.
- [x] ion-score sur PyPI (`ion-score`) et public **avant la prochaine release de ion-repo** : ion-repo
  est public, sa CI ne lit pas un dépôt privé (dépendance git en attendant PyPI). Public, 0.1.2 sur
  PyPI le 2026-11-03 (noms sans kiln, `waivers_path`).
- [x] Mesuré : même note, règle par règle, avant et après, sur les repos d'entraînement (2026-11-02, quatre copies : identiques).

Côté ion-repo : ion-repo#T-393.

## 🟡 Normal

### ion-score#T-5 · Compter les valeurs en dur restantes
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-11-09
- **Effort**: M · **Owner**: — · **Due**: —
- **Origin**: `/learn:distill` des sessions du 2026-11-03 au 2026-11-09, « il reste des jetons ? » quatre fois, chaque recherche à la main en trouvait d'autres (`d92265f7` 22:25-22:42)

- [ ] Un rapport déterministe : couleurs, tailles arbitraires, adresses de pages et textes répétés, attributs comme `link-to` compris.
- [ ] Le chiffre sert de réponse et de cliquet.

### ion-score#T-03 · Ramener sous 300 lignes les douze fichiers venus de ion-repo
- **Type**: improvement
- **Status**: todo
- **Opened**: 2026-11-02
- **Effort**: M · **Owner**: — · **Due**: —
- **Origin**: arrivée de la grille ; budget [FILE-SIZE] de `charter.toml` monté de 0 à 12

`detectors.py`, `score.py`, `fix.py`, `compressor/candidates.py`, `fixers/containers.py`,
`fixers/ci.py`, `fixers/workflows.py`, `ui.py` et les tests `test_fix.py`, `test_grid.py`,
`test_compressor.py`, `test_score.py` : un paquet par module qui grossit, le budget baissé dans
le commit qui en règle un.

## ⚪ Background — long-running work, debt and ideas
