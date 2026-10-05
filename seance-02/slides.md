---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 2"
style: |
  section { font-size: 28px; }
  section.titre { background: #0b1e4a; color: #fff; text-align: center; justify-content: center; }
  section.titre h1 { color: #ffd23f; font-size: 64px; }
  section.titre header { color: #9fb3e6; }
  section.atelier { background: #eef7f1; }
  section.atelier h2::before { content: "🛠️ "; }
  section.quiz { background: #fff6e0; }
---

<!-- _class: titre -->

# Séance 2
## Prends les commandes ! 🛸

La fenêtre du jeu et le vaisseau qui bouge

---

<!-- _class: quiz -->

## 🔁 Rappel de la séance 1

1. Que fait `print("Bonjour")` ?
2. Qu'est-ce qu'une **variable** ?
3. Que vaut `x` à la fin ?

```python
x = 100
x = x - 20
x = x - 20
```

<!--
Réponses : 1. affiche Bonjour. 2. une boîte avec un nom. 3. 60.
Insistez sur la 3 : "=" ne veut pas dire "égal" comme en maths, mais "range dans la boîte".
x = x - 20 : on prend ce qu'il y a dans x, on enlève 20, et on range le résultat dans x.
C'est exactement ce qu'on va faire pour déplacer le vaisseau !
-->

---

## 🎮 Aujourd'hui, on commence le jeu !

1. une **fenêtre** de jeu
2. un **vaisseau**
3. qui **bouge** avec les flèches du clavier

Rappelle-toi la tortue de la semaine dernière : c'est **elle** qui va devenir ton vaisseau ! 🐢➡️🛸

---

## 📍 Les coordonnées : où est mon vaisseau ?

La fenêtre est comme une **carte au trésor** : chaque point a une adresse **(x, y)**.

- **x** : gauche ↔ droite (de -400 à 400)
- **y** : bas ↕ haut (de -300 à 300)
- **(0, 0)** : le **centre**

```
              y = 300
                 ↑
  x = -400  ←  (0, 0)  →  x = 400
                 ↓
              y = -300
```

<!--
Activité : demandez où se trouve (0, -250), (-400, 300), (200, 0).
Les enfants montrent du doigt sur le tableau.
-->

---

## 🪟 La fenêtre et le vaisseau

```python
ecran = turtle.Screen()
ecran.bgcolor("midnightblue")    # couleur du fond

vaisseau = turtle.Turtle()       # une tortue...
vaisseau.shape("triangle")       # ...en forme de triangle
vaisseau.color("cyan")
vaisseau.penup()                 # lève le crayon : pas de trait
vaisseau.goto(0, -250)           # en bas, au milieu
```

Les couleurs sont en **anglais** : `"black"`, `"navy"`, `"orange"`, `"lime"`, `"hotpink"`…

---

## 🧭 Faire bouger le vaisseau

```python
vaisseau.xcor()    # donne la position x du vaisseau
vaisseau.setx(50)  # place le vaisseau à x = 50
```

Pour aller **à gauche** :

1. je regarde où est le vaisseau
2. j'enlève `vitesse`
3. je le déplace là

---

## 📜 Une fonction : une recette avec un nom

```python
def aller_a_gauche():
    x = vaisseau.xcor()
    x = x - vitesse
    vaisseau.setx(x)
```

- `def` = « je définis une recette qui s'appelle… »
- les lignes **décalées** font partie de la recette
- n'oublie pas les **deux-points** `:`

La recette **n'est pas lancée** tant qu'on ne l'appelle pas !

---

## ⌨️ Les événements : réagir au clavier

```python
ecran.listen()
ecran.onkeypress(aller_a_gauche, "Left")
```

« Écran, **écoute** le clavier. Quand on appuie sur la flèche **gauche**, lance la recette `aller_a_gauche`. »

Comme une sonnette 🔔 : rien ne se passe… jusqu'à ce qu'on appuie !

<!--
Rappelez le jeu Ruby : là-bas, ils donnaient des commandes au personnage.
Ici, ils fabriquent eux-mêmes les commandes.
-->

---

<!-- _class: atelier -->

## Atelier — étape 1 : la fenêtre et le vaisseau

Ouvre **`depart.py`** (il s'ouvre tout seul) et remplace les `___` :

- la **couleur du fond**
- la **couleur** du vaisseau
- sa **position** : en bas, au milieu → quel x ? quel y ?

**F5** pour tester !

---

<!-- _class: atelier -->

## Atelier — étape 2 : aller à droite

1. Mets une valeur à `vitesse` (essaie **20**)
2. `aller_a_gauche` est déjà écrite : écris `aller_a_droite` (**3 lignes**, presque pareilles… qu'est-ce qui change ? 🤔)
3. Relie-la à la flèche droite :

```python
ecran.onkeypress(aller_a_droite, "Right")
```

**F5**, **clique dans la fenêtre du jeu**, et utilise les flèches !

---

<!-- _class: atelier -->

## Atelier — étape 3 : expérimente !

- Change `vitesse` : 5 ? 50 ? 200 ?
- Que se passe-t-il si tu vas **très loin** à droite ? 😱

(On réglera ce problème la semaine prochaine !)

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ Change le **titre** du jeu, ou ajoute ton **prénom** dessous
- ⭐⭐ Fais **monter** le vaisseau avec la flèche `"Up"` (indice : `ycor()` et `sety()`)
- ⭐⭐⭐ Une touche **turbo** : `"t"` déplace le vaisseau de 100 vers la droite

---

## 🧠 Aujourd'hui j'ai appris…

- les **coordonnées (x, y)** pour placer les objets
- `x = x - vitesse` : on **change** la valeur d'une variable
- une **fonction** `def` est une recette qu'on lance quand on veut
- un **événement** : le programme réagit au clavier

💾 **Ctrl + S**, renomme, copie sur la clé !
