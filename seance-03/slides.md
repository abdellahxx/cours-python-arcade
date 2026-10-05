---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 3"
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

# Séance 3
## Reste dans l'écran !

Les conditions : SI… ALORS…

---

<!-- _class: quiz -->

## 🔁 Rappel de la séance 2

1. Qu'est-ce qu'une **variable** ?
2. Que fait `x = x - vitesse` ?
3. Que se passait-il quand le vaisseau allait trop loin ?

<!--
Réponse 3 : il disparaissait de l'écran ! C'est le problème du jour.
Montrez-le en direct avec la solution de la séance 2.
-->

---

## 🚦 Les conditions : SI… ALORS…

Dans la vraie vie, on décide tout le temps :

- **SI** il pleut, **ALORS** je prends un parapluie ☔
- **SI** le feu est rouge, **ALORS** je m'arrête 🚦

En Python :

```python
if il_pleut:
    prendre_parapluie()
```

---

## ⚖️ Comparer

| En Python | Ça veut dire |
|---|---|
| `x < 380` | x est **plus petit** que 380 |
| `x > -380` | x est **plus grand** que -380 |
| `x <= 0` | plus petit **ou égal** |
| `x == 0` | x est **égal** à 0 (deux `=` !) |

⚠️ `=` range dans une boîte, `==` compare !

---

## 🛡️ Le vaisseau ne sort plus

```python
def aller_a_gauche():
    x = vaisseau.xcor()
    x = x - vitesse
    if x > -380:            # SI on reste dans l'écran...
        vaisseau.setx(x)    # ...ALORS on bouge
```

- le `if` se termine par **deux-points** `:`
- la ligne en dessous est **encore plus décalée**

<!--
Pourquoi -380 et pas -400 ? Parce que le vaisseau a une largeur :
à -400, il serait à moitié dehors.
-->

---

<!-- _class: quiz -->

## 🤔 Le vaisseau bouge-t-il ?

```python
x = 390
if x < 380:
    vaisseau.setx(x)
```

Et si `x = 100` ?

<!--
x = 390 : non (390 n'est pas plus petit que 380). x = 100 : oui.
-->

---

## 🔗 Deux conditions à la fois : `and`

Le vaisseau peut monter et descendre… mais **seulement dans la zone du bas** :

```python
if y > -280 and y < -100:
    vaisseau.sety(y)
```

`and` = **les deux** doivent être vrais

« SI y est plus grand que -280 **ET** plus petit que -100 »

---

<!-- _class: atelier -->

## Atelier — étape 1 : le bord droit

`aller_a_gauche` est déjà protégée. À toi `aller_a_droite` :

```python
if ___:
    vaisseau.setx(x)
```

Quelle condition pour **le bord droit** ? 🤔

---

<!-- _class: atelier -->

## Atelier — étape 2 : descendre

`monter()` est écrite. Écris `descendre()` : **4 lignes**.

Puis relie-la à la flèche `"Down"`.

**F5** et teste les 4 flèches !

---

<!-- _class: atelier -->

## Atelier — étape 3 : teste les limites

- Va tout à gauche, tout à droite : le vaisseau reste-t-il visible ?
- Monte au maximum : où s'arrête-t-il ?
- Change `-100` en `0` : que se passe-t-il ?

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ Le vaisseau change de **couleur** quand il touche un bord (`vaisseau.color("red")`)
- ⭐⭐ Utilise `else` : SINON, le vaisseau redevient `"cyan"`
- ⭐⭐⭐ **Téléportation** : s'il sort à droite, il réapparaît à gauche !

---

## 🧠 Aujourd'hui j'ai appris…

- `if` : **SI** la condition est vraie, **ALORS** on fait les lignes décalées
- comparer : `<`, `>`, `<=`, `>=`, `==`
- `and` : les **deux** conditions doivent être vraies
- `=` range, `==` compare

💾 **Ctrl + S**, renomme, copie sur la clé !
