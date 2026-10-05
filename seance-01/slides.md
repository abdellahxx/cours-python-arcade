---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 1"
style: |
  section { font-size: 28px; }
  section.titre { background: #0b1e4a; color: #fff; text-align: center; justify-content: center; }
  section.titre h1 { color: #ffd23f; font-size: 64px; }
  section.titre header { color: #9fb3e6; }
  section.atelier { background: #eef7f1; }
  section.atelier h2::before { content: "🛠️ "; }
  section.quiz { background: #fff6e0; }
  section.partie { background: #4b2a85; color: #fff; text-align: center; justify-content: center; }
  section.partie h1 { color: #ffd23f; font-size: 56px; }
  section.partie header { color: #cdb8f0; }
  section.mistral { background: #fff4ea; }
  section.mistral h2 { color: #e8590c; }
  section.serre { font-size: 23px; }
  .gros { font-size: 64px; text-align: center; margin: 10px 0; }
  img[alt~="centre"] { display: block; margin: 0 auto; }
---

<!-- _class: titre -->

# Séance 1
## Bonjour Python ! 🐍

Tes tout premiers programmes

<!--
Note animateur : pendant que vous vous présentez, les enfants copient le kit
et lancent demarrer.bat (voir installation/guide-installation.md).
Cette séance, IDLE s'ouvre directement sur le "Shell" (pas de fichier depart.py).
-->

---

## 🎮 Ce que tu vas construire d'ici décembre

![centre w:620](../ressources/images/apercu-jeu.png)

**Ton propre jeu d'arcade**, que tu présenteras à tes parents !

<!--
Montrez le jeu final en vrai (seance-10/code/solution.py) : 1 minute de jeu.
"Aujourd'hui on apprend à parler à l'ordinateur. Dès la semaine prochaine, on attaque le jeu !"
-->

---

## 🗺️ Le voyage

| Séance | On construit… |
|---|---|
| 1 | **on apprend à parler Python** |
| 2 – 3 | la fenêtre, le vaisseau qui bouge |
| 4 – 5 | les étoiles tombent, on gagne des points |
| 6 – 7 | les météorites, les vies, le game over |
| 8 | les lasers ! |
| 9 – 10 | tes images, tes sons… et la démo ! |

---

<!-- _class: partie -->

# Partie 1
## L'informatique, c'est quoi ? 💻

<!--
Cette partie (≈ 25 min) est pensée pour être comprise dès 6–8 ans :
phrases courtes, exemples du quotidien, beaucoup de questions aux enfants.
Les installations de Python tournent pendant ce temps.
-->

---

## 🏠 Les ordinateurs sont partout !

Un ordinateur, ce n'est pas seulement l'écran de l'école…

| | | |
|:---:|:---:|:---:|
| 📱 le téléphone | 🎮 la console | 🚗 la voiture |
| ⌚ la montre | 🧺 la machine à laver | 🚦 les feux rouges |

**Et chez toi ? Où vois-tu des ordinateurs cachés ?** 🔍

<!--
Laissez les enfants proposer : télé, four, robot aspirateur, caisse du supermarché…
Petite question piège : "Une cuillère, c'est un ordinateur ?" (non !)
-->

---

## 🧠 Comment marche un ordinateur ?

Un ordinateur fonctionne un peu comme **toi** :

| | Toi 🧒 | L'ordinateur 💻 |
|---|---|---|
| 1. **Il reçoit** | tes yeux 👀, tes oreilles 👂 | le clavier ⌨️, la souris 🖱️, le micro 🎤 |
| 2. **Il réfléchit** | ton cerveau 🧠 | le processeur 🔲 |
| 3. **Il répond** | ta bouche 👄, tes mains 👋 | l'écran 🖥️, le haut-parleur 🔊 |

<!--
Exemple vécu : j'appuie sur la flèche → l'ordinateur calcule → le personnage bouge à l'écran.
-->

---

## 💪 Très fort… mais pas malin !

Un ordinateur peut faire **des milliards de calculs** en une seconde. ⚡

Mais il **ne réfléchit pas tout seul**. 🤷

Il fait **exactement** ce qu'on lui dit… **même si c'est bête !**

<p class="gros">🤖 = 🦜</p>

Il a besoin qu'on lui donne des **instructions**, une par une.

<!--
L'image du perroquet : il répète exactement, sans comprendre.
-->

---

## 📜 C'est quoi, un programme ?

Un **programme**, c'est une **liste d'instructions**, dans le **bon ordre**.

Comme une **recette de cuisine** 🍳 :

1. Casse les œufs 🥚
2. Mélange 🥄
3. Verse dans la poêle 🍳
4. Fais cuire 🔥

Si on change l'ordre… 😱 on fait cuire la poêle vide, puis on casse les œufs !

---

<!-- _class: quiz -->

## 🥪 Remets la recette dans l'ordre !

Le robot veut faire un sandwich. Aide-le !

- 🅰️ Mange le sandwich
- 🅱️ Prends deux tranches de pain
- 🅲 Mets le fromage sur une tranche
- 🅳 Pose la deuxième tranche dessus

Le bon ordre : **? → ? → ? → ?**

<!--
Réponse : B → C → D → A.
Demandez : "Et si le robot fait A en premier ?" → il mange... rien du tout !
-->

---

## 👩‍💻 Et programmer, alors ?

On a vu deux idées :

1. 💻 L'ordinateur **ne réfléchit pas** : il obéit à des **instructions**
2. 📜 Un **programme**, c'est la **liste** de ces instructions, dans l'ordre

Donc **programmer**, c'est **écrire cette liste** pour l'ordinateur…
dans une **langue qu'il comprend** ! 🗣️

**Le programmeur, c'est toi : c'est toi le chef du robot !** 👑

<!--
Mini-jeu (5 min) : "Le robot". Un enfant joue le robot, les autres lui donnent
des instructions pour aller jusqu'à la porte ("avance de 2 pas", "tourne à droite").
Le robot obéit à la lettre, même si c'est absurde. Morale : l'ordre et la précision comptent.
C'est exactement ce que fait un programmeur !
-->

---

<!-- _class: serre -->

## 🗣️ Les langages de programmation

Les humains parlent des **langues** : français 🇫🇷, anglais 🇬🇧, arabe, espagnol…

Les ordinateurs aussi ont leurs **langages** !

| Langage | On s'en sert pour… |
|---|---|
| 🧩 **Scratch** | apprendre avec des blocs de couleur |
| 🐍 **Python** | les jeux, les robots, l'intelligence artificielle |
| 🌐 **JavaScript** | les sites internet |
| 💎 **Ruby** | ton jeu du personnage (tu l'as déjà utilisé !) |
| ☕ **Java** | Minecraft ! |
| 🎮 **C++** | les grands jeux vidéo |
| 🟦 **Lua** | les jeux Roblox |

<!--
Faites réagir : "Qui connaît Minecraft ? Roblox ?" Les enfants sont souvent surpris
d'apprendre que leurs jeux préférés ont été programmés par des gens.
-->

---

## 🐍 Pourquoi Python ?

- Il ressemble à de l'**anglais** : facile à lire 📖
- Les **vrais programmeurs** l'utilisent : la NASA 🚀, YouTube ▶️, Instagram 📷
- C'est le langage préféré pour fabriquer des **intelligences artificielles** 🤖

On écrit en Python dans **IDLE**, avec deux fenêtres :
- le **Shell** `>>>` : on tape une ligne, Python répond **tout de suite**
- l'**éditeur** : on écrit un programme entier, et on le lance avec **F5**

---

<!-- _class: partie -->

# Partie 2
## Et l'intelligence artificielle ? 🤖

---

## 🤖 C'est quoi, l'IA ?

**IA** = **I**ntelligence **A**rtificielle

C'est un **programme** qui **apprend avec des exemples**, au lieu qu'on lui écrive toutes les règles.

Pour reconnaître un chat 🐱, on ne lui explique pas : on lui montre **des milliers de photos de chats** !

Tu en utilises déjà : 🗣️ les assistants vocaux, 🌍 les traducteurs, ▶️ les vidéos proposées, 📸 les filtres photo

---

## 💬 Les IA qui discutent : comment ça marche ?

On les appelle des **LLM** (« grands modèles de langage »).

1. 📚 **Elle a lu énormément** : plus de textes que tu pourrais en lire en mille vies !
2. 🎯 **Elle a appris un jeu** : deviner **le mot qui vient après**
3. ✍️ **Quand tu lui poses une question**, elle écrit sa réponse **mot par mot**, en devinant à chaque fois le mot suivant

C'est comme les **suggestions de mots** du téléphone 📱… mais en **super fort** !

---

<!-- _class: quiz -->

## 🎯 Le jeu du mot suivant

Devine le mot qui manque :

- Il était une … 
- Le chat boit du …
- Je me brosse les …
- Le ciel est …

**Bravo : tu viens de faire exactement comme une IA !** 🎉

<!--
Réponses attendues : fois, lait, dents, bleu.
Pour "Le ciel est …", plusieurs réponses sont possibles (bleu, gris, nuageux) :
l'IA choisit le mot le plus probable... et elle peut se tromper !
-->

---

## ⚠️ L'IA n'est pas magique

- 🤔 Elle **ne pense pas** comme toi : elle **devine** des mots
- ❌ Elle peut **se tromper**, et même **inventer** des choses fausses
- 🔒 Ne lui donne **jamais** ton nom, ton adresse ou tes photos
- 🧑‍🏫 Utilise-la **avec un adulte**

Et le secret : **une IA, c'est un programme !**
Écrit par des programmeurs… très souvent en **Python** 🐍

---

<!-- _class: mistral -->

## 🌬️ Zoom sur Mistral AI 🇫🇷

- Une entreprise **française**, créée en **2023** à **Paris**
- Son nom vient du **mistral** : un **vent** très fort qui souffle dans le **sud de la France**
- Elle fabrique des **IA qui parlent et écrivent** (des LLM)
- Son assistant s'appelle **Le Chat** 🐱 : on peut lui poser des questions en français
- Elle partage certaines de ses IA : **tout le monde** peut les télécharger, comme une recette qu'on donne à ses amis 🎁
- Elle a même une IA qui **aide à programmer** : **Codestral** 👩‍💻

<!--
Mistral AI a été fondée par trois chercheurs français : Arthur Mensch, Guillaume Lample
et Timothée Lacroix. Clin d'œil : "chat" veut dire "discussion" en anglais... et c'est
aussi l'animal en français !
-->

---

<!-- _class: partie -->

# Partie 3
## À toi de programmer ! 🐍

---

## 🧮 Python est une calculatrice

Dans le Shell, après `>>>`, tape :

```python
>>> 2 + 3
5
>>> 10 * 4
40
>>> 100 / 4
25.0
```

`*` = multiplier, `/` = diviser

<!--
Faites-les essayer de très grands calculs : 123456789 * 987654321. Ils adorent.
-->

---

## 💬 `print` : faire parler l'ordinateur

```python
>>> print("Bonjour !")
Bonjour !
```

- `print` = « affiche »
- le **texte** se met **entre guillemets** `" "`

```python
>>> print("ha" * 10)
hahahahahahahahahaha
```

---

<!-- _class: quiz -->

## 🤔 Que va afficher Python ?

```python
print("2 + 3")
print(2 + 3)
```

<!--
Réponse : la 1re ligne affiche le texte "2 + 3" (entre guillemets = du texte, Python ne calcule pas),
la 2e affiche 5. Faites deviner avant de tester !
-->

---

## 🔍 Ton premier bug !

```python
>>> print(Bonjour)
NameError: name 'Bonjour' is not defined
```

Sans guillemets, Python cherche un mot qu'il ne connaît pas.

**Une erreur, c'est normal !** Python te dit **quoi** et **où**. On lit le message rouge et on corrige.

<!--
Faites l'erreur exprès au tableau. Donnez le ton dès le départ : les erreurs ne sont pas
des échecs, ce sont des indices. Introduisez "le détective des bugs".
-->

---

## 📦 Les variables : des boîtes avec une étiquette

```python
>>> prenom = "Lina"
>>> age = 11
>>> print("Bonjour", prenom)
Bonjour Lina
>>> print(age + 10)
21
```

Une **variable** = une **boîte** avec un **nom**, qui contient une **valeur**.

`=` veut dire « **range dans la boîte** »

<!--
Activité débranchée (3 min) : une boîte (ou une enveloppe) avec l'étiquette "prenom",
un papier "Lina" dedans. Puis prenom = "Tom" : on remplace le papier.
-->

---

## 🎤 `input` : poser une question

```python
prenom = input("Comment t'appelles-tu ? ")
print("Bonjour", prenom, "!")
```

```
Comment t'appelles-tu ? Lina
Bonjour Lina !
```

`input` attend que tu écrives une réponse, puis la range dans la variable.

---

## 🔢 Texte ou nombre ?

`input` donne toujours du **texte**. Pour faire des calculs, on le transforme en **nombre** :

```python
age = int(input("Quel âge as-tu ? "))
print("Dans 10 ans, tu auras", age + 10, "ans")
```

`int( )` = « transforme en nombre entier »

---

<!-- _class: atelier -->

## Atelier — étapes 1 et 2 : le Shell

Dans le Shell `>>>`, essaie :

- 3 calculs de ton choix
- `print("Bonjour !")` et `print("ha" * 10)`
- `print(Bonjour)` sans guillemets… que dit Python ?
- des **variables** : `prenom = "..."` puis `print("Bonjour", prenom)`

---

<!-- _class: atelier -->

## Atelier — étape 3 : mon premier programme

**File → New File**, tape :

```python
print("Bonjour !")
print("Je m'appelle Python.")
print("Je suis prêt pour la mission !")
```

**F5** → enregistre-le sous `bonjour.py` → le résultat apparaît dans le Shell !

Change les phrases, ajoute-en d'autres.

---

<!-- _class: atelier -->

## Atelier — étape 4 : ma carte de pilote 🪪

Ouvre **`carte_pilote.py`** (File → Open), remplace les `___`, puis **F5** :

```
****** CARTE DE PILOTE ******
Pilote : Lina
Âge : 11 ans
Planète préférée : Mars
Vaisseau : rouge
Dans 10 ans, tu auras 21 ans : prêt pour l'espace !
```

---

<!-- _class: atelier -->

## Atelier — étape 5 : la tortue qui dessine 🐢 (si on a le temps)

Ouvre **`echauffement.py`**. **Avant de lancer**, devine ce qu'elle va dessiner !

```python
tortue.forward(100)   # avance de 100 pas
tortue.left(90)       # tourne à gauche de 90°
```

Puis transforme le dessin en **triangle**, en **escalier**…

<!--
Cette tortue sera la vedette du jeu dès la séance 2 : c'est elle qui deviendra le vaisseau !
Si le temps manque (l'introduction prend ~25 min), lancez echauffement.py vous-même au tableau (2 min).
-->

---

<!-- _class: atelier -->

## 🏆 Défis bonus

- ⭐ La carte demande aussi ton **nombre préféré** et affiche ton **code secret** : le nombre × 7
- ⭐⭐ Affiche ton prénom **5 fois** sur la même ligne (indice : `*`)
- ⭐⭐⭐ Avec la tortue, dessine la **première lettre** de ton prénom

---

## 💾 Avant de partir

1. **Ctrl + S** pour enregistrer
2. Renomme ta carte : `carte-tonprenom.py`
3. Copie-la sur la clé de l'animateur

## 🧠 Aujourd'hui j'ai appris…

- l'ordinateur **obéit**, il ne réfléchit pas : un **programme** = des instructions **dans l'ordre**
- **programmer**, c'est écrire ces instructions dans un **langage** (Python, Scratch, Java…)
- une **IA** est un programme qui apprend avec des exemples ; un LLM devine **le mot suivant**
- `print()` affiche, `input()` pose une question
- une **variable** est une boîte avec un nom
- texte `"entre guillemets"` ≠ nombre, et `int()` transforme le texte en nombre
- une erreur, c'est un **indice** !
