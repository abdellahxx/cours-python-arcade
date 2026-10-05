# 📒 Mon aide-mémoire Python

*À garder à côté du clavier !*

---

## 🖥️ IDLE

| Je veux… | Je fais… |
|---|---|
| lancer mon programme | **F5** |
| enregistrer | **Ctrl + S** |
| chercher un mot | **Ctrl + F** |
| annuler | **Ctrl + Z** |
| décaler une ligne | **Tab** (ou 4 espaces) |

---

## 💬 Les bases (séance 1)

```python
print("Bonjour !")                       # affiche un texte
print("Bonjour", prenom)                 # texte + variable (avec une virgule)
prenom = "Lina"                          # une variable (texte)
age = 11                                 # une variable (nombre)
prenom = input("Ton prénom ? ")          # pose une question
age = int(input("Ton âge ? "))           # pose une question et transforme en nombre
```

Calculs : `+` plus, `-` moins, `*` multiplié, `/` divisé.

---

## 🐢 La tortue (séances 1 et 2)

```python
import turtle
tortue = turtle.Turtle()
tortue.forward(100)        # avance
tortue.left(90)            # tourne à gauche
tortue.penup()             # lève le crayon
tortue.goto(0, -250)       # va au point (x, y)
tortue.color("cyan")       # couleur
tortue.shape("triangle")   # forme : "turtle", "circle", "square", "arrow"
```

**Coordonnées :** (0, 0) = le centre. x de -400 à 400, y de -300 (bas) à 300 (haut).

---

## 📦 Changer une variable (séance 2)

```python
vitesse = 20               # je range 20 dans la boîte "vitesse"
x = x + vitesse            # j'ajoute vitesse à x
```

## 📜 Les fonctions (séances 2 et 7)

```python
def aller_a_gauche():      # ← deux-points
    x = vaisseau.xcor()    # ← décalé
    vaisseau.setx(x - 20)

def replacer_en_haut(objet):   # objet = un paramètre
    objet.goto(0, 300)

replacer_en_haut(etoile)       # j'appelle la fonction
```

## ⌨️ Le clavier (séance 2)

```python
ecran.listen()
ecran.onkeypress(aller_a_gauche, "Left")
```

Touches : `"Left"`, `"Right"`, `"Up"`, `"Down"`, `"space"`, `"Return"`, `"a"`, `"b"`…

---

## 🚦 Les conditions (séances 3, 7, 8)

```python
if x < 380:
    vaisseau.setx(x)
else:
    vaisseau.color("red")
```

| `<` `>` | plus petit / plus grand |
|---|---|
| `<=` `>=` | … ou égal |
| `==` | égal (**deux** `=`) |
| `and` | les **deux** sont vraies |
| `or` | **au moins une** est vraie |
| `True` / `False` | vrai / faux |

---

## 🔄 La boucle de jeu (séance 4)

```python
def boucle_de_jeu():
    # ... on bouge les objets ...
    ecran.update()
    ecran.ontimer(boucle_de_jeu, 20)
```

## 🎲 Le hasard (séance 4)

```python
import random
random.randint(1, 6)                     # nombre entre 1 et 6
random.choice(["rouge", "vert"])         # un élément au hasard
```

---

## 🏅 Score et texte (séance 5)

```python
global score                             # dans une fonction, pour changer score
score = score + 1
stylo.write("Score : " + str(score))     # str() : nombre → texte
vaisseau.distance(etoile) < 30           # collision !
```

---

## 🚂 Listes et boucles (séances 6 et 8)

```python
meteorites = []                # liste vide
meteorites.append(m)           # ajoute à la fin
meteorites.remove(m)           # retire
len(meteorites)                # combien d'éléments ?

for i in range(5):             # répète 5 fois
    ...

for m in meteorites:           # pour chaque élément de la liste
    ...
```

---

## 🎨 Images et sons (séance 9)

```python
ecran.bgpic("fond.gif")
ecran.register_shape("vaisseau.gif")
vaisseau.shape("vaisseau.gif")
jouer_son("point.wav")
```
