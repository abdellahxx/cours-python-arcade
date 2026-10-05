# 🚀 Séance 9 — Mon style 🎨🔊

**Prénom :** ............................................

> 🎯 **Aujourd'hui :** ton jeu devient beau et bruyant ! Images, sons et niveaux.
>
> Cette fois, **pas de `___`** : cherche les commentaires `>>> MISSION` dans ton fichier (**Ctrl + F** dans IDLE).

---

## 🖥️ Démarrage

Copie **`kit-seance-09`** sur le Bureau, puis double-clique sur **`demarrer.bat`**.

Dans le dossier, tu trouves : `fond.gif`, `vaisseau.gif`, `etoile.gif`, `meteorite.gif`, `point.wav`, `laser.wav`, `boom.wav`, `fin.wav`.

---

## 🖼️ Mission 1 — Des images

**a)** Une image de fond. Sous `>>> MISSION 1 : une image de fond`, tape :

```python
ecran.bgpic("fond.gif")
```

**b)** Enregistrer les images. Sous `>>> MISSION 1 : on enregistre les images ici` :

```python
ecran.register_shape("vaisseau.gif")
ecran.register_shape("etoile.gif")
ecran.register_shape("meteorite.gif")
```

**c)** Utiliser les images. Trouve les 3 lignes `shape(...)` marquées `>>> MISSION 1 : ton image` et remplace la forme :

```python
vaisseau.shape("vaisseau.gif")
```

- [ ] le fond
- [ ] le vaisseau
- [ ] l'étoile
- [ ] les météorites
- [ ] **F5** : waouh ! 🤩

---

## 🔊 Mission 2 — Des sons

La fonction `jouer_son` est déjà prête. Il suffit de l'appeler au bon endroit :

```python
jouer_son("point.wav")
```

| Quand ? | Quel son ? | Fait ? |
|---|---|---|
| on attrape une étoile | `point.wav` | ☐ |
| on tire un laser | `laser.wav` | ☐ |
| une météorite nous touche | `boom.wav` | ☐ |
| GAME OVER | `fin.wav` | ☐ |

💡 Les trois premiers endroits sont marqués `>>> MISSION 2`. Le dernier… à toi de le trouver !

---

## 📈 Mission 3 — Les niveaux

**a)** Sous `>>> MISSION 3 : une variable niveau`, crée `niveau = 1`

**b)** Sous `>>> MISSION 3 : niveau suivant tous les 10 points` :

```python
        if score >= niveau * 10:
            niveau = niveau + 1
            vitesse_chute = vitesse_chute + 1
            afficher_infos()
```

**c)** Ajoute `niveau` et `vitesse_chute` dans la ligne `global` de `boucle_de_jeu`.

**d)** Affiche le niveau dans `afficher_infos` (comme le score et les vies).

**e)** Dans `recommencer()` : ajoute-les à la ligne `global`, et remets `niveau = 1` et `vitesse_chute = 4`.

- [ ] **F5** : à 10 points, je passe au niveau 2 et tout va plus vite !

---

## 🔍 Le détective des bugs

| Si tu vois… | Vérifie… |
|---|---|
| `couldn't open "fond.gif"` | le fichier est-il dans le **même dossier** ? Le nom est-il bien écrit ? |
| `TurtleGraphicsError: There is no shape named` | as-tu fait `register_shape` **avant** `shape` ? |
| Pas de son | le volume ? le casque ? le nom du fichier `.wav` ? |
| `UnboundLocalError: ... 'niveau'` | `niveau` dans la ligne `global` ? |
| On rejoue et ça va toujours aussi vite | dans `recommencer`, remets `vitesse_chute = 4` |

---

## 🎨 Bonus — Dessine ton vaisseau

1. Va sur **piskelapp.com** → *Create Sprite*
2. Taille : **32 × 32** (menu *Resize*)
3. Dessine ton vaisseau (le fond doit rester transparent)
4. *Export* → *GIF* → enregistre-le dans le dossier du jeu, par exemple `mon_vaisseau.gif`
5. Dans le code : `register_shape("mon_vaisseau.gif")` et `vaisseau.shape("mon_vaisseau.gif")`

---

## 🏆 Défis bonus

- [ ] ⭐ Dessine **ton** vaisseau, **ton** étoile ou **ta** météorite
- [ ] ⭐⭐ Chaque nouveau niveau ajoute **une météorite** de plus
- [ ] ⭐⭐⭐ Change la couleur du fond à chaque niveau (enlève `bgpic` et utilise `ecran.bgcolor(...)`)

---

## 📝 Ce que j'ai appris

1. Où doivent se trouver les images et les sons ? ...................................
2. Pourquoi `register_shape` avant `shape` ? ...................................
3. Mon jeu passe au niveau 2 à combien de points ? ...................................

## 💾 Avant de partir

- [ ] **Ctrl + S** → je renomme `jeu-monprenom-seance09.py` → je copie sur la clé
- [ ] Si j'ai dessiné des images, je les copie aussi !
