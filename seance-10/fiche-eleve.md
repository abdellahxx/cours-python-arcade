# 🚀 Séance 10 — Les finitions et le grand jour 🏆

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** tu ajoutes un record et un écran d'accueil, tu fais tester ton jeu… et tu le présentes !

---

## 🖥️ Démarrage

Copie **`kit-seance-10`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

Cherche les `>>> MISSION` dans ton fichier (**Ctrl + F**).

---

## 🥇 Mission 1 — Le record

- [ ] Dans les réglages, je crée `record = 0`
- [ ] Je l'ajoute à la ligne `global` de `boucle_de_jeu`
- [ ] Au GAME OVER, **SI** le score est plus grand que le record, **ALORS** le record devient le score :

```python
            if score > record:
                record = score
            afficher_infos()
```

- [ ] J'affiche le record dans `afficher_infos` : `"    Record : " + str(record)`
- [ ] **F5** : je joue 2 parties, le record reste affiché !

---

## 🏁 Mission 2 — L'écran d'accueil

- [ ] Dans les réglages, `en_jeu` vaut maintenant `False` au début
- [ ] La touche **Entrée** lance aussi la partie : `ecran.onkeypress(recommencer, "Return")`
- [ ] Tout en bas, avant `boucle_de_jeu()` : `afficher_message("Appuie sur Entrée pour jouer")`
- [ ] Je change le message de GAME OVER : `"GAME OVER - Entrée pour rejouer"`
- [ ] **F5** : le jeu attend que j'appuie sur Entrée !

---

## ✨ Ma touche perso

Ce que je change pour que le jeu soit **vraiment le mien** :

- [ ] le nom du jeu (titre de la fenêtre) : ....................................
- [ ] les couleurs / les images
- [ ] la vitesse, le nombre de météorites, le nombre de vies
- [ ] autre : ....................................

---

## 🔍 Mission 3 — Les testeurs

Échange de place avec un voisin. Joue à **son** jeu 5 minutes et écris-lui un petit mot :

| | |
|---|---|
| 👍 Ce qui est génial : | |
| 🐛 Un bug trouvé : | |
| 💡 Une idée : | |

Puis retourne à ton jeu et corrige ce que ton testeur a trouvé.

---

## 🎤 Ma présentation (2 minutes)

**Le nom de mon jeu :** ..................................................................

**Comment on joue :** ..................................................................

..................................................................................................

**Une partie du code dont je suis fier(e), et ce qu'elle fait :**

..................................................................................................

..................................................................................................

**Ce qui a été difficile, et comment j'ai réussi :**

..................................................................................................

..................................................................................................

**Mon record :** .............. points. Qui arrivera à le battre ? 🕹️

---

## 📝 Ce que j'ai appris pendant ces 10 séances

La chose que j'ai **préférée** : ..................................................................

La notion la plus **difficile** : ..................................................................

Ce que j'aimerais **ajouter** à mon jeu : ..................................................................

## 💾 Dernière sauvegarde

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-final.py` → je copie sur la clé **avec mes images et mes sons**

> 🏠 **Pour rejouer à la maison :** installe Python depuis **python.org**, mets le jeu, les images et les sons dans le même dossier, ouvre le jeu avec **IDLE** et appuie sur **F5**.
