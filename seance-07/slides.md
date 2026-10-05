---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 7"
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

# Séance 7
## Game over 💀

Les vies, la fin de partie et nos propres fonctions

---

<!-- _class: quiz -->

## 🔁 Rappel de la séance 6

1. Comment répéter 5 fois ?
2. Comment ajouter un élément à une liste ?
3. Que veut dire `for m in meteorites:` ?

---

## 🆕 Le fichier a un peu changé !

Ouvre **`depart.py`** et regarde. Il y a de **nouvelles fonctions** :

- `replacer_en_haut(objet)`
- `afficher_infos()`
- `afficher_message(texte)`

Et un **nouveau stylo** : `message`, pour les gros messages au milieu.

<!--
Montrez le fichier au tableau. Expliquez qu'un vrai programmeur "range" son code
de temps en temps : on a regroupé les lignes répétées dans des fonctions.
-->

---

## 📦 Une fonction avec un paramètre

```python
def replacer_en_haut(objet):
    x = random.randint(-370, 370)
    y = random.randint(300, 500)
    objet.goto(x, y)
```

`objet` est un **paramètre** : une boîte remplie **au moment de l'appel**.

```python
replacer_en_haut(etoile)      # objet = l'étoile
replacer_en_haut(m)           # objet = la météorite m
```

Une seule recette… pour **n'importe quel** objet ! 🍳

<!--
Analogie : la recette "faire un jus de ___". Avec une orange : jus d'orange.
Avec une pomme : jus de pomme. Le fruit est le paramètre.
-->

---

## ✅❌ Vrai ou faux : les booléens

Une variable peut contenir **vrai** ou **faux** :

```python
en_jeu = True       # on joue
en_jeu = False      # c'est fini
```

```python
if en_jeu:
    # tout ce qui bouge dans le jeu
```

Quand `en_jeu` devient `False`… **tout s'arrête** !

---

## ❤️ Les vies

```python
vies = 3
```

Une météorite touche le vaisseau ?

```python
if vaisseau.distance(m) < 35:
    vies = vies - 1
```

Plus de vies ?

```python
if vies <= 0:
    en_jeu = False
    afficher_message("GAME OVER - touche R pour rejouer")
```

---

<!-- _class: quiz -->

## 🤔 Que vaut `vies` ?

```python
vies = 3
vies = vies - 1
vies = vies - 1
```

La partie est-elle finie ? `vies <= 0` est-il vrai ?

---

<!-- _class: atelier -->

## Atelier — étape 1 : les variables

Dans les réglages, crée :

```python
vies = 3
en_jeu = True
```

Puis complète `replacer_en_haut` et `afficher_infos` (les vies dans le texte).

---

<!-- _class: atelier -->

## Atelier — étape 2 : aïe !

Dans la boucle de jeu, partie **3**, à l'intérieur du `for` :

**SI** la météorite touche le vaisseau (distance < 35) :
- enlève une vie
- remets la météorite en haut
- affiche les infos

---

<!-- _class: atelier -->

## Atelier — étape 3 : game over

Partie **4** :

**SI** il ne reste plus de vies :
- `en_jeu` devient `False`
- affiche « GAME OVER - touche R pour rejouer »

---

<!-- _class: atelier -->

## Atelier — étape 4 : rejouer

Complète `recommencer()` : remets **tout comme au début**.

- score à 0, vies à 3
- l'étoile et **chaque** météorite en haut (boucle `for` !)
- efface le message, affiche les infos
- `en_jeu = True`

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ Commence avec **5 vies**
- ⭐⭐ Le vaisseau devient **rouge** quand il ne reste qu'**une** vie
- ⭐⭐⭐ Une **étoile bonus** verte qui redonne une vie

---

## 🧠 Aujourd'hui j'ai appris…

- une fonction peut avoir un **paramètre** : `replacer_en_haut(objet)`
- **ranger son code** dans des fonctions évite de se répéter
- un **booléen** vaut `True` ou `False`
- une variable **d'état** (`en_jeu`) peut tout arrêter

💾 **Ctrl + S**, renomme, copie sur la clé !
