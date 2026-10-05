---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 6"
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

# Séance 6
## Pluie de météorites ☄️

Les listes et les boucles `for`

<!--
C'est LA séance clé du cycle. Prenez votre temps sur la partie débranchée.
Prévoyez plus d'aide pendant l'atelier : c'est normal que certains bloquent.
-->

---

<!-- _class: quiz -->

## 🔁 Rappel de la séance 5

1. Comment sait-on que le vaisseau touche l'étoile ?
2. Pourquoi écrit-on `global score` ?
3. Que fait `str(score)` ?

---

## 😩 Le problème

On veut **5 météorites**. Faut-il écrire tout ça **5 fois** ?

```python
m1 = turtle.Turtle()
m1.shape("circle")
m1.color("gray")
...
m2 = turtle.Turtle()
m2.shape("circle")
...
```

Et pour **100** météorites ? 😱

Souviens-toi du carré de la séance 1…

---

## 🔁 La boucle `for` : répéter

```python
for i in range(4):
    tortue.forward(100)
    tortue.left(90)
```

« **Répète 4 fois** les lignes décalées »

→ Le carré de la séance 1 en **3 lignes** au lieu de 8 ! 🎉

<!--
Faites-le en direct : ouvrez echauffement.py et remplacez les 8 lignes par la boucle.
Effet "waouh" garanti.
-->

---

## 🚂 Une liste : un train de wagons

```python
fruits = ["pomme", "banane", "cerise"]
```

- une **liste** range **plusieurs** valeurs dans **une seule** variable
- entre **crochets** `[ ]`, séparées par des **virgules**

```python
fruits.append("kiwi")      # ajoute un wagon à la fin du train
```

<!--
Activité débranchée (5 min) : "Le train". La liste "meteorites" est vide (personne).
append : un enfant vient se placer au bout du train. On recommence 3 fois.
Puis le "for" : l'animateur passe devant chaque wagon, un par un, et lui dit "descends d'un pas !".
-->

---

## 🚂 + 🔁 Parcourir une liste

```python
for fruit in fruits:
    print(fruit)
```

« **Pour chaque** fruit **dans** la liste, affiche-le »

```
pomme
banane
cerise
kiwi
```

---

<!-- _class: quiz -->

## 🤔 Qu'est-ce qui s'affiche ?

```python
nombres = [10, 20, 30]
for n in nombres:
    print(n + 1)
```

<!--
Réponse : 11, 21, 31 (un par ligne). Testez dans le Shell d'IDLE.
-->

---

## ☄️ Créer 5 météorites

```python
meteorites = []                  # un train vide
for i in range(5):               # répète 5 fois :
    m = turtle.Turtle()          #   crée une météorite
    m.shape("circle")
    ...
    meteorites.append(m)         #   ajoute-la au train
```

---

## ⬇️ Faire tomber toutes les météorites

Dans la boucle de jeu :

```python
for m in meteorites:             # pour chaque météorite...
    m.sety(m.ycor() - vitesse_chute)
    if m.ycor() < -320:
        m.goto(random.randint(-370, 370), random.randint(300, 600))
```

Écrit **une fois**, marche pour **toutes** ! 🚀

---

<!-- _class: atelier -->

## Atelier — étape 1 : le carré magique

Nouveau fichier (**File → New File**), tape :

```python
import turtle
tortue = turtle.Turtle()
for i in range(4):
    tortue.forward(100)
    tortue.left(90)
turtle.done()
```

Puis : un **hexagone** (6 côtés, tourne de 60°) ?

---

<!-- _class: atelier -->

## Atelier — étape 2 : créer les météorites

Dans **`depart.py`**, partie *Les météorites* :

1. combien de météorites ? → `range(___)`
2. ajoute `m` au train → `meteorites.append(m)`

**F5** : les météorites sont là… mais immobiles !

---

<!-- _class: atelier -->

## Atelier — étape 3 : les faire tomber

Dans `boucle_de_jeu`, partie **3** :

**Pour chaque** météorite `m` de la liste :
- fais-la descendre
- **SI** elle sort en bas, remets-la en haut

💡 Regarde comment on fait pour l'**étoile**, juste au-dessus !

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ **10** météorites au lieu de 5 !
- ⭐⭐ Chaque météorite a une **couleur au hasard** : `random.choice(["gray", "brown", "darkred"])`
- ⭐⭐⭐ Chaque météorite a une **taille au hasard** : `m.shapesize(random.randint(1, 3))`

---

## 🧠 Aujourd'hui j'ai appris…

- `for i in range(5):` → **répète** 5 fois
- une **liste** `[ ]` range plusieurs choses dans une variable
- `.append()` ajoute à la fin de la liste
- `for m in meteorites:` → fait quelque chose **pour chaque** élément

💾 **Ctrl + S**, renomme, copie sur la clé !
