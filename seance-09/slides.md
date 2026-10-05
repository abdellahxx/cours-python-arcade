---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 9"
style: |
  section { font-size: 28px; }
  section.titre { background: #0b1e4a; color: #fff; text-align: center; justify-content: center; }
  section.titre h1 { color: #ffd23f; font-size: 64px; }
  section.titre header { color: #9fb3e6; }
  section.atelier { background: #eef7f1; }
  section.atelier h2::before { content: "🛠️ "; }
  section.quiz { background: #fff6e0; }
  img[alt~="centre"] { display: block; margin: 0 auto; }
---

<!-- _class: titre -->

# Séance 9
## Mon style 🎨🔊

Images, sons et niveaux

---

<!-- _class: quiz -->

## 🔁 Rappel de la séance 8

1. Comment **ajouter** et **retirer** un élément d'une liste ?
2. Que donne `len(lasers)` ?
3. Différence entre `and` et `or` ?

---

## 🎯 Aujourd'hui : des missions !

Plus de `___` à remplir : tu reçois des **missions**, et c'est **toi** qui décides où écrire le code.

Cherche les commentaires `>>> MISSION` dans ton fichier 🔍

![centre w:520](../ressources/images/apercu-jeu.png)

---

## 🖼️ Mission 1 : des images

Les images doivent être des fichiers **`.gif`**, dans le **même dossier** que le jeu.

```python
ecran.bgpic("fond.gif")                  # image de fond
ecran.register_shape("vaisseau.gif")     # "Python, retiens cette image"
vaisseau.shape("vaisseau.gif")           # le vaisseau prend cette forme
```

⚠️ D'abord `register_shape`, **ensuite** `shape` !

<!--
La "ligne magique" os.chdir(...) est déjà dans le fichier : elle dit à Python de chercher
les fichiers dans le dossier du jeu. Inutile de l'expliquer en détail.
-->

---

## 🔊 Mission 2 : des sons

La fonction est **déjà prête** :

```python
jouer_son("point.wav")
```

Sons disponibles : `point.wav`, `laser.wav`, `boom.wav`, `fin.wav`

Où faut-il appeler `jouer_son` ? À toi de trouver ! 🕵️

<!--
winsound est un module fourni avec Python sous Windows. Le "|" dans jouer_son
combine deux options (jouer un fichier + ne pas bloquer le jeu) : pas besoin de l'expliquer.
-->

---

## 📈 Mission 3 : les niveaux

Tous les **10 points**, on passe au niveau suivant et ça va **plus vite** !

```python
if score >= niveau * 10:
    niveau = niveau + 1
    vitesse_chute = vitesse_chute + 1
```

<!--
Pièges : penser à ajouter niveau et vitesse_chute dans les lignes global
(boucle_de_jeu ET recommencer), et à remettre niveau = 1 et vitesse_chute = 4 dans recommencer.
-->

---

<!-- _class: quiz -->

## 🤔 À quel niveau es-tu ?

```python
niveau = 1
score = 10
if score >= niveau * 10:
    niveau = niveau + 1
```

Et quand `score` vaut 15 ? Et 20 ?

<!--
score 10 : 10 >= 10 → niveau 2. score 15 : 15 >= 20 ? non, toujours 2. score 20 : niveau 3.
-->

---

## 🎨 Dessine ton propre vaisseau !

- Site **Piskel** (piskelapp.com) : dessin en pixels, gratuit
- Taille conseillée : **32 × 32** ou **48 × 48** pixels
- Exporte en **GIF** (fond transparent) 
- Range-le dans le dossier du jeu, et change le nom dans le code

<!--
Piskel demande Internet. Sans Internet : Paint (Fichier > Enregistrer sous > GIF),
mais le fond ne sera pas transparent : dessinez sur un fond bleu nuit.
Gardez les images fournies comme solution de secours.
-->

---

<!-- _class: atelier -->

## Atelier — les 3 missions

1. 🖼️ **Images** : fond, vaisseau, étoile, météorites
2. 🔊 **Sons** : point, laser, boom, fin
3. 📈 **Niveaux** : afficher le niveau, accélérer tous les 10 points

**F5 après chaque petit changement !**

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ Dessine **ton** vaisseau dans Piskel
- ⭐⭐ Chaque niveau ajoute **une météorite** de plus
- ⭐⭐⭐ Le **fond change** de couleur à chaque niveau (`ecran.bgcolor(...)`, sans `bgpic`)

---

## 🧠 Aujourd'hui j'ai appris…

- utiliser des **fichiers** (images `.gif`, sons `.wav`) dans un programme
- les fichiers doivent être dans le **bon dossier**
- un réglage (`vitesse_chute`) peut **changer pendant le jeu**
- décider **moi-même** où placer mon code

💾 **Ctrl + S**, renomme, copie sur la clé… **avec tes images** si tu en as dessiné !
