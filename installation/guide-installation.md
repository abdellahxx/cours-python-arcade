# Guide d'installation — pour l'animateur

Les PC de la salle **effacent tout au redémarrage**. On ne peut donc rien installer « une fois pour toutes ».
La solution : un **kit** qu'on copie au début de chaque séance, et une **sauvegarde** à la fin.

Le jeu n'utilise **que des modules fournis avec Python sous Windows** :

| Module | Rôle | Fourni avec Python ? |
|---|---|---|
| `turtle` | dessiner, animer, lire le clavier | ✅ oui |
| `random` | le hasard | ✅ oui |
| `os` | trouver le dossier du jeu (séances 9–10) | ✅ oui |
| `winsound` | jouer des sons `.wav` (séances 9–10) | ✅ oui (Windows uniquement) |

L'éditeur utilisé est **IDLE**, lui aussi fourni avec Python. Rien d'autre à installer.

---

## 1. Préparer le kit (une seule fois, chez vous)

1. Sur <https://www.python.org/downloads/windows/>, téléchargez le **« Windows installer (64-bit) »**
   de la dernière version 3.13 ou 3.14.
   *(Ne prenez pas la version « embeddable » : elle ne contient pas `turtle`.)*
2. Renommez le fichier en **`python-installer.exe`**.
3. Pour chaque séance, préparez un dossier `kit-seance-XX` contenant :
   - `python-installer.exe`
   - `demarrer.bat` (dans ce dossier `installation/`)
   - tout le contenu de `seance-XX/code/` **sauf `solution.py`** (et sauf `carte_pilote_solution.py` pour la séance 1)
4. Copiez les kits sur une clé USB (ou un dossier partagé / Google Drive).

```
kit-seance-04/
├── demarrer.bat
├── python-installer.exe
└── depart.py
```

## 2. Début de séance (≈ 3 minutes)

Chaque enfant :

1. copie le dossier `kit-seance-XX` sur le **Bureau** ;
2. double-clique sur **`demarrer.bat`** ;
3. attend 1 à 2 minutes : Python s'installe sans rien demander, puis **IDLE s'ouvre avec `depart.py`** (à la séance 1, il n'y a pas de `depart.py` : IDLE s'ouvre sur le Shell) ;
4. lance le programme avec **F5**.

> 💡 Astuce : lancez les installations pendant que vous faites le rappel de la séance précédente.

## 3. Fin de séance (≈ 3 minutes)

1. Chaque enfant enregistre (**Ctrl + S**).
2. Il renomme son fichier avec son prénom : `jeu-lina-seance04.py`.
3. Il le copie sur **votre clé USB** (dossier `sauvegardes/seance-04/`).

Ces sauvegardes servent pour la démo finale et pour les enfants qui veulent reprendre leur propre version.

## 4. Si un enfant était absent ou a perdu son fichier

Pas de panique : chaque `depart.py` contient **tout le jeu des séances précédentes**.
Tout le monde repart du même point à chaque séance.

## 5. Problèmes fréquents

| Problème | Solution |
|---|---|
| `demarrer.bat` affiche « Python ne s'est pas installé » | Lancez `python-installer.exe` à la main, cochez **« Add python.exe to PATH »**, cliquez « Install Now », puis relancez `demarrer.bat`. |
| Windows affiche « Windows a protégé votre ordinateur » | Cliquez sur **Informations complémentaires → Exécuter quand même**. |
| L'installation demande un mot de passe administrateur | Le PC bloque les installations : voyez avec le responsable de la salle (l'installation « pour l'utilisateur » n'en demande normalement pas). |
| La fenêtre du jeu ne réagit pas au clavier | Cliquez une fois **dans** la fenêtre du jeu. |
| La fenêtre du jeu reste figée après une erreur | Fermez-la, corrigez l'erreur dans IDLE, relancez avec F5. |
| Pas de son (séances 9–10) | Vérifiez le volume / le casque, et que les fichiers `.wav` sont dans le même dossier que le jeu. |
| `couldn't open "fond.gif"` | Les images ne sont pas dans le même dossier que le jeu. |

## 6. Tester avant la première séance

Sur un PC de la salle, faites le parcours complet avec `kit-seance-01` **avant** la première séance.
Vérifiez aussi que les enfants ont le droit d'utiliser une clé USB.
