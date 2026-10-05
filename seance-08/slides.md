---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 8"
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

# Séance 8
## Pew pew ! Les lasers 🔫

Ajouter et retirer dans une liste

---

<!-- _class: quiz -->

## 🔁 Rappel de la séance 7

1. C'est quoi, un **paramètre** ?
2. `True` et `False`, ça s'appelle comment ?
3. Que fait `replacer_en_haut(m)` ?

---

## 🔫 Les lasers : une liste qui change tout le temps

- on appuie sur **Espace** → un laser **apparaît** → on l'**ajoute** à la liste
- le laser sort de l'écran ou touche une météorite → il **disparaît** → on le **retire**

```python
lasers = []                # au début : aucun laser
lasers.append(laser)       # pew ! un laser de plus
lasers.remove(laser)       # il a disparu
len(lasers)                # combien de lasers en ce moment ?
```

<!--
Activité débranchée : reprenez le "train" de la séance 6.
Espace = un enfant monte dans le train. Il "sort de l'écran" = il descend du train.
-->

---

## 🛑 Pas plus de 3 lasers

```python
def tirer():
    if en_jeu and len(lasers) < 3:
        laser = turtle.Turtle()
        ...
        lasers.append(laser)
```

`len(lasers)` = la **longueur** du train = le nombre de lasers

Sinon, on pourrait tirer 1 000 lasers et le jeu ralentirait ! 🐌

---

## 🎯 Le laser touche-t-il une météorite ?

Pour **chaque laser**, on regarde **chaque météorite** :

```python
for laser in lasers.copy():
    laser.sety(laser.ycor() + 15)
    touche = False
    for m in meteorites:
        if laser.distance(m) < 30:
            ...
            touche = True
```

Une boucle **dans** une boucle : des **boucles imbriquées** 🪆

<!--
Pourquoi lasers.copy() ? Parce qu'on retire des lasers pendant qu'on parcourt la liste.
Retirer un wagon pendant qu'on passe devant fait sauter le wagon suivant.
On parcourt donc une copie. Pas besoin que les enfants le retiennent : la ligne est déjà écrite.
-->

---

## 🔀 `or` : l'une OU l'autre

```python
if touche or laser.ycor() > 300:
    laser.hideturtle()
    lasers.remove(laser)
```

**SI** le laser a touché **OU** s'il est sorti en haut → il disparaît

| `and` | `or` |
|---|---|
| les **deux** doivent être vraies | **au moins une** doit être vraie |

---

<!-- _class: quiz -->

## 🤔 Vrai ou faux ?

```python
touche = False
y = 350
touche or y > 300
```

Et avec `and` ?

<!--
or : vrai (y > 300 est vrai). and : faux (touche est faux).
-->

---

<!-- _class: atelier -->

## Atelier — étape 1 : la liste et le tir

1. Crée la liste vide `lasers = []`
2. Dans `tirer()` : le laser part du vaisseau → `laser.goto(vaisseau.xcor(), vaisseau.ycor() + 20)`
3. Ajoute le laser à la liste
4. Relie `tirer` à la touche `"space"`

---

<!-- _class: atelier -->

## Atelier — étape 2 : les lasers montent

Dans la boucle de jeu, partie **4** :

1. fais monter le laser de 15
2. **SI** il touche une météorite :
   - remets la météorite en haut
   - +1 au score, affiche les infos
   - `touche = True`

**F5** et détruis les météorites ! 💥

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ Des lasers **verts** et plus **épais**
- ⭐⭐ Jusqu'à **5** lasers à la fois
- ⭐⭐⭐ Une météorite détruite rapporte **2 points**, une étoile attrapée **1 point**

---

## 🧠 Aujourd'hui j'ai appris…

- `.append()` ajoute, `.remove()` retire un élément d'une liste
- `len(liste)` donne le nombre d'éléments
- une boucle **dans** une boucle
- `or` : au moins une condition vraie

💾 **Ctrl + S**, renomme, copie sur la clé !
