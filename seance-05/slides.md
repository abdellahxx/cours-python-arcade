---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 5"
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

# Séance 5
## Attrape-les toutes !

Les collisions et le score

<!--
Si c'est la reprise après les vacances de la Toussaint, prenez 5 minutes de plus
pour le rappel : faites jouer à la version de la séance 4 et reposez les bases
(variable, fonction, if, boucle de jeu).
-->

---

<!-- _class: quiz -->

## 🔁 Grand rappel

| Mot | Ça veut dire… |
|---|---|
| **variable** | ? |
| **fonction** (`def`) | ? |
| **condition** (`if`) | ? |
| **boucle de jeu** | ? |
| `random.randint(1, 6)` | ? |

---

## 💥 Une collision, c'est quoi ?

Deux objets qui se **touchent** !

Comment savoir si le vaisseau touche l'étoile ?
→ on mesure la **distance** entre les deux 📏

```python
vaisseau.distance(etoile)
```

**SI** la distance est **plus petite que 30**, ils se touchent !

<!--
Activité : deux enfants debout. "Quand vous êtes à moins d'un bras l'un de l'autre,
c'est une collision." Ils s'approchent : "collision !"
-->

---

## 🏅 Le score : une variable qui grandit

```python
score = 0               # au début du jeu
```

À chaque étoile attrapée :

```python
score = score + 1
```

Rappel : on prend ce qu'il y a dans la boîte, on ajoute 1, on range.

---

## 🌍 `global` : la variable du jeu

Dans une fonction, pour **modifier** une variable créée en dehors, il faut prévenir Python :

```python
def boucle_de_jeu():
    global score        # "je parle du score du jeu !"
    ...
    score = score + 1
```

Sans `global`, Python croit que c'est une **nouvelle** boîte, rien qu'à la fonction.

<!--
Ne vous attardez pas : retenez juste "si je change une variable du jeu dans
une fonction, j'écris global". L'erreur sans global est UnboundLocalError.
-->

---

## ✏️ Écrire le score à l'écran

Texte et nombre, ça ne se mélange pas directement :

```python
"Score : " + str(score)
```

`str(5)` transforme le **nombre** 5 en **texte** `"5"`

```python
stylo.clear()                                    # efface l'ancien
stylo.write("Score : " + str(score), font=("Arial", 18, "bold"))
```

---

<!-- _class: quiz -->

## 🤔 Que va afficher ce code ?

```python
score = 3
score = score + 1
print("Score : " + str(score))
```

Et sans `str()` ? 😬

<!--
Réponse : "Score : 4". Sans str : TypeError (on ne peut pas ajouter un texte et un nombre).
Testez-le en direct dans le Shell d'IDLE !
-->

---

<!-- _class: atelier -->

## Atelier — étape 1 : le score

1. Dans les réglages, crée `score = 0`
2. Place le stylo **en haut à gauche** : `stylo.goto(-380, 260)`

**F5** : « Score : 0 » s'affiche !

---

<!-- _class: atelier -->

## Atelier — étape 2 : la collision

Dans `boucle_de_jeu`, partie **2** :

**SI** la distance entre le vaisseau et l'étoile est plus petite que 30 :
- ajoute 1 au score
- affiche le score
- remets l'étoile en haut

**F5** et attrape des étoiles ! ⭐

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ Chaque étoile rapporte **5 points**
- ⭐⭐ L'étoile tombe **plus vite** à chaque fois qu'on l'attrape
- ⭐⭐⭐ Une **2e étoile**, rose, qui rapporte 10 points

---

## 🧠 Aujourd'hui j'ai appris…

- une **collision** = une distance plus petite qu'une limite
- `score = score + 1` pour compter
- `global` pour modifier une variable du jeu dans une fonction
- `str()` transforme un nombre en texte

💾 **Ctrl + S**, renomme, copie sur la clé !
