# 🚀 Séance 4 — Il pleut des étoiles ✨

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** une étoile tombe du ciel, encore et encore, à un endroit différent à chaque fois.

---

## 🧠 À savoir

**La boucle de jeu** : une fonction qui bouge un peu les objets, redessine l'écran, puis **se relance toute seule** 50 fois par seconde.

```python
def boucle_de_jeu():
    # ... on fait bouger les choses ...
    ecran.update()                     # on redessine
    ecran.ontimer(boucle_de_jeu, 20)   # on recommence dans 20 millisecondes
```

**Le hasard** :

```python
import random
random.randint(1, 6)    # un nombre au hasard entre 1 et 6, comme un dé
```

---

## 🖥️ Démarrage

Copie **`kit-seance-04`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

---

## 🎲 Étape 1 — Les réglages

- [ ] Sous `import turtle`, je **tape** : `import random`
- [ ] Je remplace le `___` de `vitesse_chute` par **4**

---

## ⭐ Étape 2 — L'étoile

Sous `etoile = turtle.Turtle()`, remplace les trois `___` par trois lignes :

- [ ] la forme ronde : `etoile.shape("circle")`
- [ ] la couleur jaune : `etoile.color(.........)`
- [ ] lever le crayon : `etoile.........()`

💡 Regarde comment tu as créé le **vaisseau** : c'est pareil !

---

## ⬇️ Étape 3 — L'étoile tombe

Dans `boucle_de_jeu`, partie **1** :

```python
    y = y - ___
```

- [ ] De combien l'étoile descend-elle à chaque fois ? Remplace `___` par la **variable** qui contient la vitesse de chute.
- [ ] **F5** : l'étoile tombe… et disparaît en bas 😢

---

## 🔁 Étape 4 — Elle revient en haut

Dans la partie **2**, sous les commentaires `>>> A TOI`, écris une condition :

**SI** `etoile.ycor()` est plus petit que `-300`, **ALORS** remets l'étoile en haut.

```python
    if ............................ :
        etoile.goto(random.randint(-370, 370), 300)
```

- [ ] **F5** : l'étoile tombe sans fin, à un endroit différent à chaque fois ! 🌟
- [ ] Mon vaisseau bouge toujours avec les flèches ? ☐ oui

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| `NameError: name 'random' is not defined` | as-tu écrit `import random` en haut ? |
| L'étoile ne bouge pas | as-tu bien `ecran.ontimer(boucle_de_jeu, 20)` **dans** la fonction (décalé) ? |
| Un trait jaune suit l'étoile | tu as oublié `etoile.penup()` |
| Rien ne s'affiche | la ligne `boucle_de_jeu()` est-elle bien en bas, **avant** `ecran.mainloop()` ? |

---

## 🏆 Défis bonus

- [ ] ⭐ Essaie d'autres vitesses de chute : 1, 10, 20
- [ ] ⭐⭐ L'étoile prend une **couleur au hasard** quand elle remonte : `etoile.color(random.choice(["gold", "orange", "pink"]))`
- [ ] ⭐⭐⭐ La **vitesse** de chute aussi est tirée au hasard (entre 2 et 8) quand l'étoile remonte

---

## 📝 Ce que j'ai appris

1. Pourquoi un jeu donne-t-il l'impression de bouger ? ...................................
2. Que fait `ecran.ontimer(boucle_de_jeu, 20)` ? ...................................
3. `random.randint(1, 100)` donne… ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance04.py` → je copie sur la clé
