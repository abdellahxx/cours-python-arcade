---
marp: true
theme: default
paginate: true
header: "🚀 Chasseur d'étoiles · Séance 10"
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

# Séance 10
## Les finitions et le grand jour 🏆

Record, écran d'accueil… et démo !

<!--
Organisation conseillée :
- 0:00–0:45 finitions (missions + polish)
- 0:45–1:05 testeurs croisés + préparation de la présentation
- 1:05–1:30 démo aux parents (ou dans une séance dédiée si les parents viennent à un autre moment)
-->

---

## 🗺️ Regarde le chemin parcouru !

| Séance | Tu as appris… |
|---|---|
| 1 | programme, instructions, coordonnées |
| 2 | variables, fonctions, événements |
| 3 | conditions `if`, `and` |
| 4 | boucle de jeu, hasard |
| 5 | collisions, score |
| 6 | **listes** et **boucles `for`** |
| 7 | paramètres, booléens |
| 8 | ajouter / retirer dans une liste, `or` |
| 9 | images, sons, niveaux |

**Tu es un vrai programmeur !** 🎉

---

## 🥇 Mission 1 : le record

```python
record = 0
```

À la fin de la partie :

```python
if score > record:
    record = score
```

Et on l'affiche dans `afficher_infos` !

---

## 🏁 Mission 2 : l'écran d'accueil

Au lieu de démarrer tout de suite, le jeu **attend** :

```python
en_jeu = False                              # au début, on attend
...
ecran.onkeypress(recommencer, "Return")     # Entrée lance la partie
...
afficher_message("Appuie sur Entrée pour jouer")
```

`recommencer()` fait déjà tout le travail ! 🎁

<!--
Montrez que recommencer() sert maintenant aussi à "commencer" : c'est l'intérêt
d'avoir rangé le code dans une fonction à la séance 7.
-->

---

## 🔍 Mission 3 : les testeurs

Échange de place avec un voisin et **joue à son jeu** pendant 5 minutes.

Note sur un papier :
- 👍 une chose **géniale**
- 🐛 un **bug** trouvé (s'il y en a)
- 💡 une **idée** d'amélioration

Puis retourne corriger **ton** jeu !

---

## 🎤 Préparer ta présentation (2 minutes)

1. **Le nom** de ton jeu
2. **Comment on joue** (les touches, le but)
3. **Une partie du code** dont tu es fier — explique-la !
4. **Ce qui a été difficile**, et comment tu as réussi
5. **Démo** : un parent essaie de battre ton record ! 🕹️

---

<!-- _class: atelier -->

## Atelier — les finitions

1. 🥇 Mission 1 : le **record**
2. 🏁 Mission 2 : l'**écran d'accueil**
3. ✨ Ton touche perso : couleurs, sons, vitesse, nom du jeu…
4. 🔍 Mission 3 : les **testeurs**
5. 🎤 Remplis ta **fiche de présentation**

---

## 🏆 Bravo, pilotes !

Vous avez construit **un vrai jeu vidéo** en Python, ligne par ligne.

Et ce n'est que le début… 🚀

💾 Dernière sauvegarde : copie ton jeu **et ses images** sur la clé.
Tu pourras le rejouer chez toi !

<!--
Pour rejouer à la maison : installer Python depuis python.org, puis double-cliquer
sur le fichier du jeu (ou l'ouvrir avec IDLE et F5). Donnez la consigne aux parents.
Remettez les diplômes (seance-10/diplome.md).
-->
