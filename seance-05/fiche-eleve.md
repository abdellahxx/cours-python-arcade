# 🚀 Séance 5 — Attrape-les toutes !

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** quand ton vaisseau attrape l'étoile, tu gagnes un point !

---

## 🧠 À savoir

**Collision** : deux objets se touchent si la **distance** entre eux est petite.

```python
if vaisseau.distance(etoile) < 30:
    # ils se touchent !
```

**Score** : une variable qui grandit.

```python
score = score + 1
```

**`global`** : dans une fonction, pour **changer** une variable du jeu.

```python
def boucle_de_jeu():
    global score
```

**`str()`** : transforme un nombre en texte pour l'écrire.

```python
"Score : " + str(score)
```

---

## 🤔 Échauffement

```python
score = 3
score = score + 1
score = score + 1
print("Score : " + str(score))
```

Ça affiche : ..................................

---

## 🖥️ Démarrage

Copie **`kit-seance-05`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

---

## 🏅 Étape 1 — Le score

- [ ] Dans *Les réglages*, je **tape** : `score = 0`
- [ ] Je place le stylo en haut à gauche : remplace `stylo.goto(___, ___)` par `stylo.goto(-380, 260)`
- [ ] **F5** : je vois « Score : 0 » en haut à gauche

---

## 💥 Étape 2 — Attraper l'étoile

Dans `boucle_de_jeu`, partie **2**, sous les commentaires `>>> A TOI`, tape ce bloc et complète les trous :

```python
    if vaisseau.distance(etoile) < ......:
        score = ...............
        afficher_score()
        etoile.goto(random.randint(-370, 370), 300)
```

- [ ] **F5** : j'attrape une étoile et le score augmente ! ⭐
- [ ] Mon record de la séance : ............ points

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| `UnboundLocalError: ... 'score'` | as-tu `global score` au début de `boucle_de_jeu` ? |
| `TypeError: can only concatenate str` | as-tu mis `str(score)` et pas juste `score` ? |
| Le score ne change pas à l'écran | appelles-tu bien `afficher_score()` dans le `if` ? |
| On gagne plein de points d'un coup | as-tu remis l'étoile en haut **dans** le `if` ? |

---

## 🏆 Défis bonus

- [ ] ⭐ Chaque étoile rapporte **5 points**
- [ ] ⭐⭐ L'étoile tombe **plus vite** à chaque fois qu'on l'attrape (indice : `global vitesse_chute` et `vitesse_chute = vitesse_chute + 1`)
- [ ] ⭐⭐⭐ Ajoute une **2e étoile**, rose, qui rapporte 10 points

---

## 📝 Ce que j'ai appris

1. Comment l'ordinateur sait-il que deux objets se touchent ? ...................................
2. À quoi sert `global` ? ...................................
3. Pourquoi écrire `str(score)` ? ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance05.py` → je copie sur la clé
