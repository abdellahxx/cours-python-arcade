# 🚀 Séance 3 — Reste dans l'écran !

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** ton vaisseau ne sort plus de l'écran, et il peut monter et descendre.

---

## 🧠 À savoir

**Une condition** : SI quelque chose est vrai, ALORS on fait les lignes décalées.

```python
if x > -380:            # ← deux-points !
    vaisseau.setx(x)    # ← décalé
```

| Symbole | Veut dire |
|---|---|
| `<` | plus petit que |
| `>` | plus grand que |
| `<=` / `>=` | plus petit / plus grand **ou égal** |
| `==` | égal (⚠️ deux `=`) |
| `and` | les **deux** conditions sont vraies |

---

## 🤔 Échauffement : vrai ou faux ?

| Condition | Vrai ou faux ? |
|---|---|
| `5 < 10` | |
| `400 < 380` | |
| `-390 > -380` | |
| `-200 > -280 and -200 < -100` | |

---

## 🖥️ Démarrage

Copie **`kit-seance-03`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

---

## ➡️ Étape 1 — Le bord droit

Regarde comment `aller_a_gauche` est protégée :

```python
    if x > -380:
        vaisseau.setx(x)
```

Dans `aller_a_droite`, remplace `___` par la bonne condition :

```python
    if ___:
        vaisseau.setx(x)
```

- [ ] **F5** : le vaisseau s'arrête au bord droit

---

## ⬇️ Étape 2 — Descendre

La fonction `monter()` est écrite. Juste en dessous, écris `descendre()` (4 lignes).

💡 **Indice :** recopie `monter()` et change ce qu'il faut. Qu'est-ce qui est différent quand on descend ?

- [ ] J'ai écrit `descendre()` et supprimé le `___`
- [ ] J'ai ajouté en bas : `ecran.onkeypress(descendre, "Down")`
- [ ] **F5** : les 4 flèches marchent !

---

## 🧪 Étape 3 — Je teste les limites

- [ ] Tout à gauche / tout à droite : le vaisseau reste visible ? ☐ oui ☐ non
- [ ] Il monte jusqu'où ? ....................
- [ ] Si je remplace `-100` par `0` dans `monter()`, que se passe-t-il ? ....................

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| `SyntaxError` sur la ligne `if` | les **deux-points** `:` à la fin |
| `IndentationError` | la ligne sous le `if` est **plus décalée** que le `if` |
| `SyntaxError` avec `=` | dans un `if`, on compare avec `<`, `>` ou `==`, pas `=` |
| Le vaisseau ne bouge plus du tout | ta condition est-elle possible ? (`x > 380` au lieu de `x < 380` ?) |

---

## 🏆 Défis bonus

- [ ] ⭐ Quand le vaisseau est bloqué au bord, il devient **rouge** : `vaisseau.color("red")`
- [ ] ⭐⭐ Ajoute un `else:` (SINON) pour qu'il redevienne `"cyan"` quand il peut bouger
- [ ] ⭐⭐⭐ **Téléportation** : s'il dépasse le bord droit, il réapparaît à gauche (indice : `vaisseau.setx(-380)`)

---

## 📝 Ce que j'ai appris

1. Complète : **SI** ............ **ALORS** ............
2. Quelle est la différence entre `=` et `==` ? ...................................
3. Que veut dire `and` ? ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance03.py` → je copie sur la clé
