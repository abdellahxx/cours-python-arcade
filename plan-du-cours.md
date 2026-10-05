# 🚀 Chasseur d'étoiles — Plan du cours

**Public :** enfants de 10 à 12 ans, qui n'ont **jamais fait de Python** (ils ont déjà déplacé un personnage avec des commandes en Ruby)
**Groupe :** 6 enfants, 1 ordinateur Windows chacun
**Rythme :** 10 séances de 1 h 30, d'octobre à décembre
**Projet :** chaque enfant construit **son propre jeu d'arcade** et le présente à ses parents à la fin

![Le jeu final](ressources/images/apercu-jeu.png)

Le joueur pilote un vaisseau, attrape des étoiles pour gagner des points, évite (ou détruit au laser) les météorites, et passe des niveaux de plus en plus rapides.

---

## 🎯 Objectifs

À la fin du cycle, chaque enfant saura :

- écrire et lancer un programme Python (`print`, `input`), et **lire un message d'erreur** sans paniquer ;
- utiliser des **variables**, des **conditions** (`if`, `and`), des **fonctions** (`def`, paramètres) ;
- comprendre la **boucle de jeu** et les **événements** (clavier) ;
- utiliser des **listes** et des **boucles `for`** ;
- découper un gros problème en petites étapes ;
- **présenter** son travail devant un public.

Tout cela en n'utilisant **que ce qui est fourni avec Python** (`turtle`, `random`, `os`, `winsound`) et l'éditeur **IDLE**.

---

## 🗺️ Les 10 séances

| # | Titre | Ce qu'on construit | Notion de programmation |
|---|---|---|---|
| 1 | **Bonjour Python !** | Découverte de l'informatique et de l'IA, premiers programmes, une « carte de pilote » (pas encore de jeu) | Ordinateur, **programme**, langages, **IA / LLM** (zoom sur Mistral), `print`, **variables**, `input` |
| 2 | **Prends les commandes** | La fenêtre, le vaisseau, qui bouge avec les flèches | Coordonnées (x, y), changer une variable, première fonction `def`, **événements** |
| 3 | **Reste dans l'écran !** | Le vaisseau ne sort plus de l'écran, il monte et descend | **Conditions** `if`, comparaisons, **`and`** |
| 4 | **Il pleut des étoiles** | Une étoile tombe et revient au hasard | **Boucle de jeu**, module **`random`** |
| 5 | **Attrape-les toutes !** | Attraper l'étoile donne des points | **Collisions**, **score**, texte + nombre, `global` |
| 6 | **Pluie de météorites** | 5 météorites tombent en même temps | ⭐ **Listes** et **boucles `for`** |
| 7 | **Game over** | Vies, fin de partie, rejouer | **Fonctions avec paramètre**, **booléens** (`True` / `False`) |
| 8 | **Pew pew ! Les lasers** | Le vaisseau tire et détruit les météorites | Ajouter / retirer dans une liste, `len()`, **boucles imbriquées**, `or` |
| 9 | **Mon style** | Images, sons, niveaux | Fichiers, modules `os` et `winsound`, réglages |
| 10 | **Les finitions et le grand jour** | Record, écran d'accueil, démo aux parents | Tester, corriger, **présenter** |

> Les vacances de la Toussaint tombent pendant le cycle : la séance 5 est un bon point de reprise (la séance commence par un grand rappel).

---

## 🧩 Comment les enfants écrivent le code

On ne donne **ni une page blanche, ni du code à copier-coller en entier**. On réduit l'aide petit à petit :

| Séances | Ce que l'enfant reçoit | Ce qu'il écrit |
|---|---|---|
| 1 – 3 | Fichier presque complet avec des trous `___` | Des valeurs, puis des lignes recopiées et adaptées |
| 4 – 6 | Squelette + commentaires `>>> A TOI` qui disent **quoi** faire | Le **comment** (quelques lignes) |
| 7 – 8 | Commentaires qui décrivent le but | Des blocs entiers (5–10 lignes) |
| 9 – 10 | Des **missions** (« ajoute un son quand… ») | Tout, en choisissant où placer le code |

Trois règles simples :

1. **Le nouveau code se tape au clavier**, jamais copié-collé : on lit chaque caractère et on apprend en corrigeant ses fautes de frappe.
2. **Le code déjà vu peut se copier** (par exemple recopier `aller_a_gauche` pour écrire `aller_a_droite`).
3. **Chaque séance repart d'un fichier `depart.py`** qui contient tout le jeu des séances précédentes : personne n'est perdu après une absence.

---

## ⏱️ Déroulé type d'une séance (1 h 30)

| Durée | Moment | Détail |
|---|---|---|
| 5 min | 🖥️ **Démarrage** | Copier le kit, lancer `demarrer.bat` (pendant le rappel) |
| 10 min | 🔁 **Rappel** | Quiz rapide sur la séance précédente, montrer le jeu |
| 15 min | 💡 **La notion du jour** | Expliquée avec une image du quotidien + « Que va faire ce code ? » |
| 45 min | 🛠️ **Atelier** | Étapes de la fiche, l'animateur circule |
| 10 min | 🏆 **Défis bonus** | Pour ceux qui ont fini ; les autres terminent |
| 5 min | 💾 **Sauvegarde et bilan** | Copier le fichier sur la clé, « aujourd'hui j'ai appris… » |

---

## 📁 Contenu du dossier

```
cours-python-arcade/
├── README.md                 ← par où commencer
├── plan-du-cours.md          ← ce document
├── guide-animateur.md        ← pédagogie, pièges, conseils séance par séance
├── aide-memoire.md           ← à imprimer pour chaque enfant
├── detective-des-bugs.md     ← affiche des erreurs fréquentes
├── saison-2.md               ← idées pour 8 séances de plus
├── installation/             ← kit de démarrage Windows
├── ressources/               ← images et sons du jeu
├── outils/                   ← tester les solutions, générer les PDF
└── seance-01/ … seance-10/
    ├── slides.md             ← diaporama (cours + atelier), notes animateur incluses
    ├── fiche-eleve.md        ← fiche de TP à imprimer
    └── code/
        ├── depart.py         ← fichier de départ de l'enfant
        └── solution.py       ← corrigé (ne pas mettre dans le kit !)
```
