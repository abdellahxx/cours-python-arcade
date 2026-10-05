# 🚀 Chasseur d'étoiles — Cours de Python pour enfants (10–12 ans)

Un cycle de **10 séances de 1 h 30** pendant lesquelles chaque enfant construit **son propre jeu d'arcade** en Python, puis le présente à ses parents.

![Aperçu du jeu](ressources/images/apercu-jeu.png)

**Uniquement avec Python de base sous Windows** : `turtle`, `random`, `os`, `winsound`, et l'éditeur IDLE. Aucune bibliothèque à installer.

---

## 📖 Par où commencer ?

1. **`plan-du-cours.md`** : la vue d'ensemble (objectifs, les 10 séances, la méthode).
2. **`guide-animateur.md`** : comment animer, aider un enfant bloqué, les pièges de chaque séance.
3. **`installation/guide-installation.md`** : préparer le kit pour des PC qui s'effacent au redémarrage.
4. Puis, pour chaque séance, dans `seance-XX/` :
   - **`slides.md`** : le diaporama (cours + atelier), avec des notes pour vous en commentaire ;
   - **`fiche-eleve.md`** : la fiche de TP à imprimer ;
   - **`code/depart.py`** : le fichier de départ de l'enfant ;
   - **`code/solution.py`** : le corrigé (à ne pas mettre dans le kit !).

À imprimer une fois pour chaque enfant : **`aide-memoire.md`**. À afficher dans la salle : **`detective-des-bugs.md`**.

---

## 🖨️ Construire les PDF

Les diaporamas sont au format **[Marp](https://marp.app)**, les fiches en Markdown classique.

Avec Node.js installé :

```bash
bash outils/construire-pdf.sh
```

Les PDF sont créés dans `pdf/`.

Autres possibilités :
- **VS Code** + extension « Marp for VS Code » : ouvrir un `slides.md` → *Export Slide Deck* → PDF ;
- **VS Code** + extension « Markdown PDF » pour les fiches ;
- en ligne de commande : `npx @marp-team/marp-cli slides.md --pdf --allow-local-files`.

---

## 🛠️ Outils pour l'animateur

| Commande | Rôle |
|---|---|
| `python outils/tester_solutions.py` | lance les 10 solutions, simule des parties, signale les erreurs |
| `python outils/generer_ressources.py` | refabrique les images `.gif` et les sons `.wav` du jeu |
| `bash outils/construire-pdf.sh` | construit tous les PDF |
