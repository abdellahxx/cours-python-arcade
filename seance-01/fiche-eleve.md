# 🚀 Séance 1 — Bonjour Python ! 🐍

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** tu découvres ce qu'est un ordinateur, un programme et une IA… puis tu apprends à parler à l'ordinateur en Python et tu crées ta carte de pilote !

---

## 🖥️ Démarrage

1. Copie le dossier **`kit-seance-01`** sur le Bureau.
2. Double-clique sur **`demarrer.bat`** et patiente (Python s'installe).
3. **IDLE** s'ouvre : tu vois `>>>`. C'est le **Shell**, Python t'écoute !

---

## 💻 Partie 1 — L'informatique, c'est quoi ?

**🔍 Entoure les objets qui ont un ordinateur caché dedans :**

📱 téléphone   🥄 cuillère   🎮 console   🚗 voiture   📖 livre   ⌚ montre   🧺 machine à laver   ✏️ crayon

**🥪 Remets la recette du sandwich dans l'ordre (écris 1, 2, 3, 4) :**

| Étape | Numéro |
|---|---|
| Mange le sandwich | ...... |
| Prends deux tranches de pain | ...... |
| Mets le fromage sur une tranche | ...... |
| Pose la deuxième tranche dessus | ...... |

**✍️ Complète :** un **programme**, c'est une liste d'.................................... dans le bon .................

**🗣️ Un langage de programmation que je connais maintenant :** ....................................

---

## 🤖 Partie 2 — Le jeu du mot suivant

Fais comme une IA : devine le mot qui manque !

- Il était une ....................
- Le chat boit du ....................
- Je me brosse les ....................
- Le ciel est ....................

**✍️ Vrai ou faux ?**

| | Vrai | Faux |
|---|:---:|:---:|
| Une IA peut se tromper | ☐ | ☐ |
| Je peux donner mon adresse à une IA | ☐ | ☐ |
| Mistral AI est une entreprise française | ☐ | ☐ |
| Une IA, c'est un programme | ☐ | ☐ |

---

## 🐍 Partie 3 — À toi de programmer !

### 🧠 À savoir

| Je tape… | Ça veut dire… |
|---|---|
| `print("Bonjour")` | affiche le texte **Bonjour** |
| `"du texte"` | le texte se met **entre guillemets** |
| `prenom = "Lina"` | range **"Lina"** dans la boîte **prenom** |
| `input("Question ? ")` | pose une question et attend la réponse |
| `int(...)` | transforme le texte en **nombre** |
| `+  -  *  /` | plus, moins, multiplié, divisé |

---

## 🧮 Étape 1 — Le Shell

Tape chaque ligne après `>>>` puis **Entrée**. Écris ce que Python répond :

| Je tape | Python répond |
|---|---|
| `7 + 5` | |
| `6 * 8` | |
| `100 / 4` | |
| `print("Bonjour !")` | |
| `print("ha" * 10)` | |
| `print(Bonjour)` | |

🤔 **Devine avant de tester :** quelle est la différence ?

```python
print("2 + 3")
print(2 + 3)
```

Ma réponse : ..........................................................

---

## 📦 Étape 2 — Les variables

Toujours dans le Shell :

```python
prenom = "Lina"
print("Bonjour", prenom)
age = 11
print(age + 10)
```

- [ ] J'ai mis **mon** prénom et **mon** âge
- [ ] Que se passe-t-il si j'écris `prenom = "Tom"` puis à nouveau `print("Bonjour", prenom)` ? ..............................

---

## 📝 Étape 3 — Mon premier programme

Menu **File → New File**. Une nouvelle fenêtre s'ouvre. Tape :

```python
print("Bonjour !")
print("Je m'appelle Python.")
print("Je suis prêt pour la mission !")
```

- [ ] **F5** → enregistre sous `bonjour.py` → le résultat s'affiche dans le Shell
- [ ] J'ajoute 2 phrases à moi
- [ ] J'ajoute une question :

```python
prenom = input("Comment t'appelles-tu ? ")
print("Bienvenue à bord,", prenom, "!")
```

---

## 🪪 Étape 4 — Ma carte de pilote

Ouvre **`carte_pilote.py`** (menu *File → Open*). Remplace chaque `___` :

- [ ] la question pour la planète : `input("Quelle est ta planète préférée ? ")`
- [ ] demande la couleur du vaisseau avec `input(...)`
- [ ] affiche la planète (quelle variable ?)
- [ ] affiche la couleur du vaisseau (une ligne `print` à écrire toi-même)
- [ ] dans 10 ans : `age + 10`
- [ ] **F5** et réponds aux questions dans le Shell !

---

## 🐢 Étape 5 — La tortue qui dessine *(si tu as le temps)*

**Avant de tester**, devine : que va dessiner ce programme ? Dessine-le ici 👇

```python
tortue.forward(100)
tortue.left(90)
tortue.forward(100)
tortue.left(90)
tortue.forward(100)
tortue.left(90)
tortue.forward(100)
tortue.left(90)
```

<br><br><br>

Ouvre **`echauffement.py`** et lance-le avec **F5**.

- [ ] Ma prédiction était juste ? ☐ oui ☐ non
- [ ] Je transforme le carré en **triangle** (3 côtés, on tourne de 120°)
- [ ] Je dessine un **escalier**

> 🤔 Tu as recopié plusieurs fois les mêmes lignes ? On apprendra une astuce pour éviter ça à la séance 6 !

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| `NameError` | les **guillemets** autour du texte ? l'orthographe du nom de la variable ? |
| `SyntaxError` | une parenthèse `)` ou un guillemet `"` oublié ? |
| `ValueError: invalid literal for int()` | tu as répondu avec des lettres à une question qui attend un **nombre** |
| `NameError: name '___'` | il reste un trou `___` à remplacer |

---

## 🏆 Défis bonus

- [ ] ⭐ Ta carte demande ton **nombre préféré** et affiche ton **code secret** : le nombre × 7
- [ ] ⭐⭐ Affiche ton prénom **5 fois** sur la même ligne (indice : `print(prenom * 5)`)
- [ ] ⭐⭐⭐ Avec la tortue, dessine la **première lettre** de ton prénom

---

## 📝 Ce que j'ai appris

1. Dans quel ordre l'ordinateur lit-il les instructions ? ...................................
2. À quoi sert `print` ? Et `input` ? ...................................
3. Une variable, c'est comme… ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S**
- [ ] Je renomme ma carte : `carte-monprenom.py`
- [ ] Je la copie sur la clé de l'animateur
