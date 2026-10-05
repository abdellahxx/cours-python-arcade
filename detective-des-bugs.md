# 🔍 Le détective des bugs

## Un message rouge ? Pas de panique !

**Tous les programmeurs font des erreurs.** Même ceux de la NASA. 🚀
Le message rouge est un **indice** : il te dit **où** et **quoi**.

---

## 🕵️ Les 4 étapes du détective

1. **Lis** le message : quel est le **type** d'erreur ? (la dernière ligne en rouge)
2. **Trouve** la ligne : IDLE la surligne, ou cherche `line 42`
3. **Regarde** cette ligne **et celle juste au-dessus**
4. **Corrige**, puis **F5** pour vérifier

---

## 📋 Les suspects habituels

| Le message | Le coupable | L'indice |
|---|---|---|
| 🔤 `NameError` | Un mot mal écrit, ou un `___` oublié | `vaisseau` ≠ `vaiseau` ≠ `Vaisseau` |
| ✏️ `SyntaxError` | Un caractère manquant | `:` à la fin du `def`, `if`, `for` ? Une `)` ou un `"` ? |
| ↔️ `IndentationError` | Les lignes mal décalées | Toutes les lignes d'un bloc commencent au **même endroit** |
| 🌍 `UnboundLocalError` | `global` oublié | Dans une fonction : `global score` |
| ➕ `TypeError` … `str` | Texte + nombre | `"Score : " + str(score)` |
| 🎨 `bad color name` | Couleur inconnue | En anglais : `"red"`, `"blue"`, `"gold"` |
| 🖼️ `couldn't open` | Fichier introuvable | L'image est-elle dans le **même dossier** ? |

---

## 🤫 Les bugs silencieux (pas de message, mais ça ne marche pas)

| Ce qui se passe | Vérifie… |
|---|---|
| Les touches ne font rien | **Clique** dans la fenêtre du jeu |
| Rien ne bouge | `boucle_de_jeu()` est appelée en bas ? |
| Le jeu est figé | Regarde le **Shell** d'IDLE : une erreur s'y cache |
| Il manque des choses | Rien n'est écrit **après** `ecran.mainloop()` ? |

---

## 🙋 La règle des 3 avant l'animateur

1. Je relis ma **fiche**
2. Je regarde cette **affiche**
3. Je demande à un **voisin**

… et si je suis toujours bloqué, je lève la main ! ✋
