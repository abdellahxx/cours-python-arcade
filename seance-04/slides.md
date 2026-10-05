---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 4"
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

# Séance 4
## Il pleut des étoiles ✨

La boucle de jeu et le hasard

---

<!-- _class: quiz -->

## 🔁 Rappel de la séance 3

1. Complète : `if x < 380` ___ (qu'est-ce qui manque à la fin ?)
2. Différence entre `=` et `==` ?
3. Que veut dire `and` ?

<!--
Réponses : 1. les deux-points. 2. = range, == compare. 3. les deux conditions vraies.
-->

---

## 🎬 Comment un jeu vidéo bouge-t-il ?

Un jeu, c'est comme un **dessin animé** ou un **flipbook** 📖

On dessine une image… on change un petit peu… on redessine…
**50 fois par seconde !**

Nos yeux voient un **mouvement**.

<!--
Si possible, apportez un petit flipbook, ou dessinez 3 images au tableau
(une balle un peu plus bas à chaque fois).
-->

---

## 🔄 La boucle de jeu

```python
def boucle_de_jeu():
    # 1. on fait bouger les choses un tout petit peu
    # 2. on vérifie ce qui se passe
    ecran.update()                     # on redessine
    ecran.ontimer(boucle_de_jeu, 20)   # on recommence dans 20 ms
```

`ontimer` = « dans 20 millisecondes, relance cette fonction »

→ la fonction se relance **sans fin** : c'est une **boucle** !

---

## 🖌️ `ecran.tracer(0)`

```python
ecran.tracer(0)
```

« Écran, ne redessine pas tout seul : **c'est moi** qui te dirai quand (`ecran.update()`) »

→ Le jeu devient **beaucoup plus fluide**.

---

## 🎲 Le hasard : `random`

```python
import random

random.randint(1, 6)        # un nombre au hasard entre 1 et 6 (comme un dé !)
random.randint(-370, 370)   # une position x au hasard
```

`import random` = « Python, sors ta boîte à outils **hasard** »

---

<!-- _class: quiz -->

## 🤔 Que fait ce code ?

```python
y = etoile.ycor()
y = y - 4
etoile.sety(y)
```

Et si on le répète 50 fois par seconde ?

<!--
Réponse : l'étoile descend de 4 pas. 50 fois par seconde : elle tombe doucement.
-->

---

## ⬆️ Et quand l'étoile sort en bas ?

```python
if etoile.ycor() < -300:
    etoile.goto(random.randint(-370, 370), 300)
```

**SI** elle sort en bas, **ALORS** elle remonte tout en haut, **à un endroit au hasard**.

---

<!-- _class: atelier -->

## Atelier — étape 1 : les réglages

Ouvre **`depart.py`** :

1. Sous `import turtle`, **tape** `import random`
2. Mets une valeur à `vitesse_chute` (essaie **4**)

---

<!-- _class: atelier -->

## Atelier — étape 2 : l'étoile

Crée l'étoile, comme tu as créé le vaisseau :

```python
etoile = turtle.Turtle()
etoile.shape(___)      # ronde
etoile.color(___)      # jaune
etoile.___()           # lève le crayon !
```

---

<!-- _class: atelier -->

## Atelier — étape 3 : elle tombe !

Dans `boucle_de_jeu` :

1. complète `y = y - ___`
2. **SI** l'étoile sort en bas (`< -300`), **ALORS** remets-la en haut

**F5** : l'étoile tombe encore et encore ! 🌟

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ Change la **vitesse** de chute : 1 ? 10 ? 20 ?
- ⭐⭐ L'étoile change de **couleur au hasard** à chaque fois : `random.choice(["gold", "orange", "pink"])`
- ⭐⭐⭐ La **vitesse** de chute aussi est au hasard (entre 2 et 8)

---

## 🧠 Aujourd'hui j'ai appris…

- un jeu = des images qui changent **très vite**
- la **boucle de jeu** se relance toute seule avec `ontimer`
- `import random` et `random.randint(a, b)` pour le **hasard**

💾 **Ctrl + S**, renomme, copie sur la clé !
