# 🚀 Séance 8 — Pew pew ! Les lasers 🔫

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** ton vaisseau tire des lasers avec la barre d'espace et détruit les météorites !

---

## 🧠 À savoir

```python
lasers = []                # une liste vide
lasers.append(laser)       # ajoute un laser
lasers.remove(laser)       # retire un laser
len(lasers)                # combien de lasers ?
```

| `and` | `or` |
|---|---|
| les **deux** conditions vraies | **au moins une** condition vraie |

**Boucles imbriquées** : une boucle dans une boucle.

```python
for laser in lasers.copy():     # pour chaque laser...
    for m in meteorites:        # ...on regarde chaque météorite
```

---

## 🤔 Échauffement

```python
lasers = []
lasers.append("laser 1")
lasers.append("laser 2")
lasers.append("laser 3")
lasers.remove("laser 1")
print(len(lasers))
```

Ça affiche : ..........

---

## 🖥️ Démarrage

Copie **`kit-seance-08`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

---

## 🔫 Étape 1 — Tirer

- [ ] Partie *Les lasers* : je crée la liste vide `lasers = []`
- [ ] Dans `tirer()`, le laser part du vaisseau :

```python
        laser.goto(vaisseau.xcor(), vaisseau.ycor() + 20)
```

- [ ] Juste en dessous, j'ajoute le laser à la liste `lasers` (avec `append`)
- [ ] En bas, avec les autres touches : `ecran.onkeypress(tirer, "space")`
- [ ] **F5** + **Espace** : un laser apparaît… mais il ne bouge pas (normal !)

---

## ⬆️ Étape 2 — Les lasers montent

Dans `boucle_de_jeu`, partie **4** :

- [ ] Sous le commentaire `>>> A TOI`, je fais monter le laser de 15 :

```python
            laser.sety(laser.ycor() + 15)
```

- [ ] **F5** : les lasers montent ! Et je ne peux en tirer que 3 à la fois.

---

## 💥 Étape 3 — Détruire les météorites

Toujours partie **4**, dans le `for m in meteorites:`, remplace la ligne `pass` par :

**SI** `laser.distance(m)` est plus petite que 30 :

```python
                if ...................................:
                    replacer_en_haut(m)
                    score = .....................
                    afficher_infos()
                    touche = .....................
```

- [ ] **F5** : je détruis les météorites ! 💥
- [ ] Mon meilleur score : ............

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| Rien ne se passe avec Espace | la touche s'écrit `"space"` en minuscules |
| `NameError: name 'lasers'` | as-tu créé `lasers = []` en haut ? |
| Le laser part du milieu de l'écran | as-tu bien mis la position du vaisseau dans `goto` ? |
| Après 3 tirs, on ne peut plus tirer | le laser est-il bien **retiré** de la liste quand il sort ? (lignes `hideturtle` et `remove`) |

---

## 🏆 Défis bonus

- [ ] ⭐ Des lasers **verts** et plus **épais** (indice : `laser.shapesize(0.4, 1)`)
- [ ] ⭐⭐ Jusqu'à **5** lasers à la fois
- [ ] ⭐⭐⭐ Une météorite détruite rapporte **2 points**, une étoile attrapée **1 point**

---

## 📝 Ce que j'ai appris

1. Comment retirer un élément d'une liste ? ...................................
2. À quoi sert `len()` ? ...................................
3. Différence entre `and` et `or` ? ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance08.py` → je copie sur la clé
