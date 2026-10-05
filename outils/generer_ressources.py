# ==================================================
#   Outil pour l'animateur : fabrique les images (.gif)
#   et les sons (.wav) du jeu, sans aucune bibliothèque
#   à installer (uniquement Python de base).
#
#   Utilisation :  python generer_ressources.py
#   Les fichiers sont créés dans ../ressources/
# ==================================================

import math
import os
import random
import struct
import wave

ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER_IMAGES = os.path.join(ICI, "..", "ressources", "images")
DOSSIER_SONS = os.path.join(ICI, "..", "ressources", "sons")


# ---------------------------------------------------------------
#  GIF : écriture "non compressée" (codes LZW de largeur fixe)
# ---------------------------------------------------------------
def ecrire_gif(chemin, largeur, hauteur, pixels, palette, transparent=None):
    """pixels : liste d'index dans la palette (max 128 couleurs)."""
    assert len(palette) <= 128
    palette = list(palette) + [(0, 0, 0)] * (128 - len(palette))
    taille_min = 7
    clear, fin = 128, 129

    # flux de codes : on remet le dictionnaire à zéro souvent
    # pour que chaque code tienne toujours sur 8 bits.
    codes = []
    for i in range(0, len(pixels), 100):
        codes.append(clear)
        codes.extend(pixels[i:i + 100])
    codes.append(fin)
    donnees = bytes(codes)       # 8 bits par code, ordre des bits identique

    sortie = bytearray(b"GIF89a")
    sortie += struct.pack("<HHBBB", largeur, hauteur, 0xF6, 0, 0)   # palette globale 128 couleurs
    for r, g, b in palette:
        sortie += bytes((r, g, b))
    if transparent is not None:
        sortie += bytes((0x21, 0xF9, 4, 0x01, 0, 0, transparent, 0))
    sortie += b"\x2C" + struct.pack("<HHHHB", 0, 0, largeur, hauteur, 0)
    sortie += bytes((taille_min,))
    for i in range(0, len(donnees), 255):
        bloc = donnees[i:i + 255]
        sortie += bytes((len(bloc),)) + bloc
    sortie += b"\x00\x3B"
    with open(chemin, "wb") as f:
        f.write(sortie)


def pixel_art(chemin, dessin, couleurs, echelle):
    """dessin : liste de lignes de texte, '.' = transparent."""
    symboles = ["."] + [c for c in couleurs]
    palette = [(255, 0, 255)] + [couleurs[c] for c in couleurs]
    h = len(dessin)
    w = max(len(ligne) for ligne in dessin)
    pixels = []
    for ligne in dessin:
        ligne = ligne.ljust(w, ".")
        rangee = [symboles.index(c) for c in ligne]
        rangee = [p for p in rangee for _ in range(echelle)]
        for _ in range(echelle):
            pixels.extend(rangee)
    ecrire_gif(chemin, w * echelle, h * echelle, pixels, palette, transparent=0)


VAISSEAU = [
    ".......WW.......",
    "......WCCW......",
    "......WCCW......",
    ".....WCBBCW.....",
    ".....WCBBCW.....",
    "....WCCCCCCW....",
    "....WCCCCCCW....",
    "...WCCCCCCCCW...",
    "..RWCCCCCCCCWR..",
    ".RRWCCWCCWCCWRR.",
    "RRRWCCWCCWCCWRRR",
    "RR.WWWWWWWWWW.RR",
    "R....OYYYYO....R",
    "......OYYO......",
    ".......OO.......",
]
ETOILE = [
    ".....Y.....",
    ".....Y.....",
    "....YYY....",
    "....YWY....",
    "YYYYYWYYYYY",
    ".YYYWWWYYY.",
    "..YYYWYYY..",
    "..YYYYYYY..",
    ".YYYY.YYYY.",
    ".YYY...YYY.",
    "YY.......YY",
]
METEORITE = [
    ".....GGGGG.....",
    "...GGLLLGGGG...",
    "..GLLGGGGDGGG..",
    ".GLGGDDGGGGGGG.",
    ".GLGGDDGGGGDDG.",
    "GLGGGGGGGGGDDGG",
    "GGGGGGGGDGGGGGG",
    "GGGDDGGGGGGGGGG",
    "GGGDDGGGGGGDGGG",
    "GGGGGGGGGGGGGGG",
    ".GGGGGDDGGGGGG.",
    ".GGGGGDDGGGGGG.",
    "..GGGGGGGGGGG..",
    "...GGGGGGGGG...",
    ".....GGGGG.....",
]


def fond(chemin, largeur=800, hauteur=600):
    random.seed(7)
    palette = []
    for i in range(40):                       # dégradé bleu nuit
        t = i / 39
        palette.append((int(8 + 22 * t), int(10 + 20 * t), int(40 + 60 * t)))
    palette += [(255, 255, 255), (180, 200, 255), (255, 230, 150)]
    blanc, bleute, jaune = 40, 41, 42
    pixels = []
    etoiles = {}
    for _ in range(260):
        etoiles[(random.randrange(largeur), random.randrange(hauteur))] = random.choice((blanc, bleute, bleute, jaune))
    for y in range(hauteur):
        base = int(y / hauteur * 39)
        for x in range(largeur):
            pixels.append(etoiles.get((x, y), base))
    ecrire_gif(chemin, largeur, hauteur, pixels, palette)


# ---------------------------------------------------------------
#  Sons WAV
# ---------------------------------------------------------------
TAUX = 22050


def ecrire_wav(chemin, echantillons):
    with wave.open(chemin, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(TAUX)
        f.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, e)) * 20000)) for e in echantillons))


def balayage(f_debut, f_fin, duree, forme="carre"):
    n = int(TAUX * duree)
    phase = 0.0
    sortie = []
    for i in range(n):
        t = i / n
        freq = f_debut + (f_fin - f_debut) * t
        phase += 2 * math.pi * freq / TAUX
        v = math.sin(phase)
        if forme == "carre":
            v = 0.6 if v > 0 else -0.6
        sortie.append(v * (1 - t))           # le son s'éteint doucement
    return sortie


def explosion(duree):
    random.seed(3)
    n = int(TAUX * duree)
    sortie, v = [], 0.0
    for i in range(n):
        v = 0.7 * v + 0.3 * random.uniform(-1, 1)   # bruit "grave"
        sortie.append(v * 2.2 * (1 - i / n) ** 2)
    return sortie


def main():
    os.makedirs(DOSSIER_IMAGES, exist_ok=True)
    os.makedirs(DOSSIER_SONS, exist_ok=True)

    pixel_art(os.path.join(DOSSIER_IMAGES, "vaisseau.gif"), VAISSEAU,
              {"W": (230, 240, 255), "C": (40, 200, 230), "B": (20, 60, 140),
               "R": (230, 60, 70), "O": (255, 140, 0), "Y": (255, 230, 80)}, 3)
    pixel_art(os.path.join(DOSSIER_IMAGES, "etoile.gif"), ETOILE,
              {"Y": (255, 205, 40), "W": (255, 250, 210)}, 3)
    pixel_art(os.path.join(DOSSIER_IMAGES, "meteorite.gif"), METEORITE,
              {"G": (120, 110, 100), "L": (170, 160, 150), "D": (70, 62, 56)}, 3)
    fond(os.path.join(DOSSIER_IMAGES, "fond.gif"))

    ecrire_wav(os.path.join(DOSSIER_SONS, "point.wav"), balayage(600, 1400, 0.12))
    ecrire_wav(os.path.join(DOSSIER_SONS, "laser.wav"), balayage(1800, 300, 0.15))
    ecrire_wav(os.path.join(DOSSIER_SONS, "boom.wav"), explosion(0.45))
    ecrire_wav(os.path.join(DOSSIER_SONS, "fin.wav"),
               balayage(523, 523, 0.18) + balayage(392, 392, 0.18) + balayage(262, 200, 0.45))
    print("Images et sons créés dans le dossier ressources/")


main()
