# 🚀 Séance 6 — Pluie de météorites ☄️

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** 5 météorites tombent en même temps… sans écrire 5 fois le même code !

---

## 🧠 À savoir

**Répéter** avec `for` :

```python
for i in range(4):          # répète 4 fois...
    tortue.forward(100)     # ...les lignes décalées
    tortue.left(90)
```

**Une liste** = un train de wagons 🚂

```python
fruits = ["pomme", "banane"]   # une liste
fruits.append("kiwi")          # ajoute un wagon à la fin
```

**Pour chaque** élément d'une liste :

```python
for fruit in fruits:
    print(fruit)
```

---

## 🤔 Échauffement

```python
nombres = [10, 20, 30]
for n in nombres:
    print(n + 1)
```

Ça affiche : ..............................................

---

## 🖥️ Démarrage

Copie **`kit-seance-06`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

---

## 🟦 Étape 1 — Le carré magique

Menu **File → New File**, puis tape :

```python
import turtle
tortue = turtle.Turtle()
for i in range(4):
    tortue.forward(100)
    tortue.left(90)
turtle.done()
```

- [ ] **F5** (enregistre-le sous `carre.py`) : un carré en 3 lignes au lieu de 8 ! 🎉
- [ ] Je dessine un **hexagone** : ............ côtés, je tourne de ............ degrés
- [ ] Je dessine un **cercle** (indice : 360 fois, avance de 1, tourne de 1 ; ajoute `tortue.speed(0)` pour aller plus vite)

Ferme cette fenêtre et reviens à **`depart.py`**.

---

## ☄️ Étape 2 — Créer les météorites

Dans la partie *Les météorites* :

- [ ] `range(___)` : je mets **5**
- [ ] je remplace le `___` par la ligne qui ajoute `m` au bout de la liste :

```python
    meteorites.append(m)
```

- [ ] **F5** : je vois des météorites grises… qui ne bougent pas (normal !)

---

## ⬇️ Étape 3 — Les faire tomber

Dans `boucle_de_jeu`, partie **3**, sous les commentaires `>>> A TOI`, tape cette boucle et complète le trou :

```python
    for m in ...........:
        m.sety(m.ycor() - vitesse_chute)
        if m.ycor() < -320:
            m.goto(random.randint(-370, 370), random.randint(300, 600))
```

💡 La 1re ligne : **pour chaque** météorite `m` **dans** la liste… comment s'appelle la liste ?

- [ ] **F5** : il pleut des météorites ! ☄️☄️☄️

> Pour l'instant, elles traversent le vaisseau sans rien faire. On s'en occupe la semaine prochaine !

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| Une seule météorite bouge | `meteorites.append(m)` est-il bien **décalé** dans la boucle `for` ? |
| `NameError: name 'meteorite'` | la liste s'appelle `meteorites`, avec un **s** |
| `IndentationError` | les lignes sous `for` et sous `if` sont bien décalées ? |
| `SyntaxError` sur `for` | les **deux-points** `:` à la fin |

---

## 🏆 Défis bonus

- [ ] ⭐ **10** météorites au lieu de 5
- [ ] ⭐⭐ Chaque météorite a une **couleur au hasard** : `m.color(random.choice(["gray", "brown", "darkred"]))`
- [ ] ⭐⭐⭐ Chaque météorite a une **taille au hasard** : `m.shapesize(random.randint(1, 3))`

---

## 📝 Ce que j'ai appris

1. Comment répéter 10 fois une instruction ? ...................................
2. Une liste, c'est comme… ...................................
3. Que fait `meteorites.append(m)` ? ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance06.py` → je copie sur la clé
