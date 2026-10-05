# 🚀 Séance 2 — Prends les commandes ! 🛸

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** tu commences ton jeu ! Une fenêtre, un vaisseau… qui bouge avec les flèches du clavier.

---

## 🧠 À savoir

**Les coordonnées** : chaque point de la fenêtre a une adresse (x, y).

```
              y = 300
                 ↑
  x = -400  ←  (0, 0)  →  x = 400
                 ↓
              y = -300
```

**Changer une variable** :

```python
x = x - vitesse     # je prends x, j'enlève vitesse, je range le résultat dans x
```

**Une fonction** = une recette avec un nom. Les lignes **décalées** font partie de la recette.

```python
def aller_a_gauche():       # ← les deux-points !
    x = vaisseau.xcor()     # ← décalé de 4 espaces
    x = x - vitesse
    vaisseau.setx(x)
```

**Un événement** = « quand on appuie sur cette touche, lance cette recette ».

```python
ecran.onkeypress(aller_a_gauche, "Left")
```

---

## 🤔 Échauffement : que vaut `x` à la fin ?

```python
x = 100
x = x - 20
x = x + 50
```

Ma réponse : x = ..........

---

## 🖥️ Démarrage

Copie **`kit-seance-02`** sur le Bureau, puis double-clique sur **`demarrer.bat`**. Le fichier **`depart.py`** s'ouvre tout seul.

---

## 🪟 Étape 1 — La fenêtre et le vaisseau

Remplace les `___` :

- [ ] la couleur du fond : `ecran.bgcolor(___)` → idées : `"black"`, `"navy"`, `"midnightblue"`
- [ ] la couleur du vaisseau : `vaisseau.color(___)` → idées : `"cyan"`, `"orange"`, `"lime"`, `"hotpink"`
- [ ] la position du vaisseau, **en bas, au milieu** : `vaisseau.goto(___, ___)` → x = ...... y = ......

⚠️ Les couleurs s'écrivent **en anglais** et **entre guillemets**.

Pour l'instant, remplace aussi `vitesse = ___` par `vitesse = 20`.

- [ ] **F5** : je vois ma fenêtre, mon vaisseau en bas et le titre !

---

## ➡️ Étape 2 — Aller à droite

La fonction `aller_a_gauche` est déjà écrite. Juste en dessous, complète `aller_a_droite` :

```python
def aller_a_droite():
    # 3 lignes, comme aller_a_gauche... mais vers la droite !
```

💡 **Indice :** une seule chose change entre gauche et droite. Laquelle ?

- [ ] J'ai écrit mes 3 lignes, bien **décalées** sous le `def`
- [ ] J'ai supprimé la ligne `___`
- [ ] Sous `ecran.onkeypress(aller_a_gauche, "Left")`, j'ajoute :

```python
ecran.onkeypress(aller_a_droite, "Right")
```

- [ ] **F5**, je **clique dans la fenêtre du jeu**, et j'utilise les flèches ← →

---

## 🧪 Étape 3 — J'expérimente

| Si `vitesse` vaut… | Le vaisseau… |
|---|---|
| 5 | |
| 50 | |
| 200 | |

- [ ] Que se passe-t-il si je vais très loin à droite ? ........................................

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| `NameError: name '___'` | il reste un `___` à remplacer |
| `TclError: bad color name` | la couleur est en anglais, entre guillemets, bien écrite ? |
| `IndentationError` | les lignes sous `def` sont bien **décalées** (toutes pareil) |
| `SyntaxError` sur la ligne `def` | les **deux-points** `:` à la fin |
| Le vaisseau ne bouge pas | as-tu **cliqué dans la fenêtre du jeu** ? `"Right"` avec un R majuscule ? |

---

## 🏆 Défis bonus

- [ ] ⭐ Change le **titre** du jeu, ou écris ton **prénom** dessous (un deuxième `goto` puis `write`)
- [ ] ⭐⭐ Fais **monter** le vaisseau avec la flèche `"Up"` (indices : `vaisseau.ycor()` et `vaisseau.sety(y)`)
- [ ] ⭐⭐⭐ Crée une touche **turbo** `"t"` qui déplace le vaisseau de 100 vers la droite

---

## 📝 Ce que j'ai appris

1. Où se trouve le point (0, 0) ? ...................................
2. Que veut dire `def` ? ...................................
3. Pourquoi les lignes sont-elles décalées sous `def` ? ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance02.py` → je copie sur la clé
