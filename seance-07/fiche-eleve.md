# 🚀 Séance 7 — Game over 💀

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** les météorites font perdre des vies. Plus de vies ? GAME OVER… et on peut rejouer !

---

## 🧠 À savoir

**Une fonction avec un paramètre** : la recette marche pour n'importe quel objet.

```python
def replacer_en_haut(objet):     # objet = le paramètre
    ...
    objet.goto(x, y)

replacer_en_haut(etoile)         # ici, objet = etoile
replacer_en_haut(m)              # ici, objet = m
```

**Un booléen** : vrai (`True`) ou faux (`False`).

```python
en_jeu = True
if en_jeu:
    # le jeu tourne
```

---

## 👀 Le fichier a changé

Ouvre **`depart.py`** et trouve ces nouveautés. Coche quand tu les as trouvées :

- [ ] la fonction `replacer_en_haut(objet)`
- [ ] la fonction `afficher_infos()` (elle remplace `afficher_score`)
- [ ] la fonction `afficher_message(texte)`
- [ ] le nouveau stylo `message`
- [ ] la touche `"r"` qui lance `recommencer`

---

## 🖥️ Démarrage

Copie **`kit-seance-07`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

---

## ❤️ Étape 1 — Les variables et les fonctions

- [ ] Dans *Les réglages*, je crée `vies = 3`
- [ ] … et `en_jeu = True`
- [ ] Dans `replacer_en_haut`, la position y au hasard : `random.randint(300, 500)`
- [ ] Dans `afficher_infos`, j'ajoute les vies au texte :

```python
    stylo.write("Score : " + str(score) + "    Vies : " + str(vies), font=("Arial", 18, "bold"))
```

- [ ] **F5** : je vois « Score : 0    Vies : 3 »

---

## 💥 Étape 2 — Aïe, une météorite !

Dans `boucle_de_jeu`, partie **3**, **dans** le `for`, sous les commentaires `>>> A TOI` :

**SI** `vaisseau.distance(m)` est plus petite que 35 :
- enlève 1 à `vies`
- remets `m` en haut (avec `replacer_en_haut`)
- affiche les infos

```python
            if ...................................:
                ...................................
                ...................................
                ...................................
```

- [ ] **F5** : je perds une vie quand une météorite me touche

---

## 💀 Étape 3 — Game over

Partie **4**, sous les commentaires `>>> A TOI` :

**SI** `vies <= 0` :
- `en_jeu` devient `False`
- `afficher_message("GAME OVER - touche R pour rejouer")`

- [ ] **F5** : quand je n'ai plus de vies, tout s'arrête et le message s'affiche

---

## 🔄 Étape 4 — Rejouer

Dans `recommencer()`, remplace `___` pour remettre **tout comme au début** :

- [ ] `score = 0` et `vies = 3`
- [ ] l'étoile en haut : `replacer_en_haut(etoile)`
- [ ] **chaque** météorite en haut :

```python
        for m in meteorites:
            replacer_en_haut(m)
```

- [ ] `message.clear()` puis `afficher_infos()`
- [ ] `en_jeu = True`
- [ ] **F5** : après le game over, la touche **R** relance une partie !

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| On perd toutes les vies d'un coup | la météorite est-elle bien remise en haut **dans** le `if` ? |
| `UnboundLocalError: ... 'vies'` | `global score, vies, en_jeu` au début de la fonction ? |
| `true` ou `TRUE` ne marche pas | ça s'écrit `True` et `False`, avec une majuscule |
| R ne fait rien | as-tu **cliqué dans la fenêtre du jeu** ? La partie est-elle bien finie ? |

---

## 🏆 Défis bonus

- [ ] ⭐ Commence avec **5 vies**
- [ ] ⭐⭐ Le vaisseau devient **rouge** quand il ne reste qu'**une** vie (et redevient normal quand on rejoue)
- [ ] ⭐⭐⭐ Crée une **étoile bonus** verte, plus rare, qui redonne une vie

---

## 📝 Ce que j'ai appris

1. C'est quoi, un paramètre ? ...................................
2. Quelles sont les deux valeurs d'un booléen ? ...................................
3. Pourquoi tout s'arrête quand `en_jeu` vaut `False` ? ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance07.py` → je copie sur la clé
