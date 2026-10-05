# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 9 - mon style : images, sons et niveaux
#   Créé par : ............
# ==================================================
#
#   Cette fois, pas de ___ : suis les missions de ta fiche
#   et ajoute toi-même le code aux endroits marqués  >>> MISSION

import turtle
import random
import os
import winsound

# Ligne magique : Python cherche les images et les sons
# dans le même dossier que ce fichier.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ----- La fenêtre du jeu -----
ecran = turtle.Screen()
ecran.title("Chasseur d'étoiles")
ecran.setup(800, 600)
ecran.bgcolor("midnightblue")
# >>> MISSION 1 : une image de fond
ecran.tracer(0)

# >>> MISSION 1 : on enregistre les images ici

# ----- Les réglages -----
vitesse = 20
vitesse_chute = 4
score = 0
vies = 3                         # le nombre de vies
# >>> MISSION 3 : une variable niveau
en_jeu = True                    # True = on joue, False = la partie est finie


# ----- Les fonctions utiles -----
def jouer_son(fichier):          # déjà prête : jouer_son("point.wav")
    winsound.PlaySound(fichier, winsound.SND_FILENAME | winsound.SND_ASYNC)


def replacer_en_haut(objet):
    x = random.randint(-370, 370)
    y = random.randint(300, 500)
    objet.goto(x, y)


def afficher_infos():
    stylo.clear()
    stylo.write("Score : " + str(score) + "    Vies : " + str(vies), font=("Arial", 18, "bold"))


def afficher_message(texte):
    message.clear()
    message.write(texte, align="center", font=("Arial", 26, "bold"))


# ----- Le vaisseau -----
vaisseau = turtle.Turtle()
vaisseau.shape("triangle")       # >>> MISSION 1 : ton image
vaisseau.color("cyan")
vaisseau.speed(0)
vaisseau.penup()
vaisseau.setheading(90)
vaisseau.goto(0, -250)

# ----- L'étoile -----
etoile = turtle.Turtle()
etoile.shape("circle")           # >>> MISSION 1 : ton image
etoile.color("gold")
etoile.penup()
replacer_en_haut(etoile)

# ----- Les météorites -----
meteorites = []
for i in range(5):
    m = turtle.Turtle()
    m.shape("circle")            # >>> MISSION 1 : ton image
    m.color("gray")
    m.shapesize(2)
    m.penup()
    replacer_en_haut(m)
    meteorites.append(m)

# ----- Les lasers -----
lasers = []                      # au début, aucun laser

# ----- Les stylos -----
stylo = turtle.Turtle()          # écrit le score en haut à gauche
stylo.hideturtle()
stylo.penup()
stylo.color("white")
stylo.goto(-380, 260)

message = turtle.Turtle()        # écrit les gros messages au milieu
message.hideturtle()
message.penup()
message.color("gold")
message.goto(0, 0)


# ----- Les commandes -----
def aller_a_gauche():
    x = vaisseau.xcor()
    x = x - vitesse
    if x > -380:
        vaisseau.setx(x)


def aller_a_droite():
    x = vaisseau.xcor()
    x = x + vitesse
    if x < 380:
        vaisseau.setx(x)


def monter():
    y = vaisseau.ycor()
    y = y + vitesse
    if y > -280 and y < -100:
        vaisseau.sety(y)


def descendre():
    y = vaisseau.ycor()
    y = y - vitesse
    if y > -280 and y < -100:
        vaisseau.sety(y)


def tirer():
    if en_jeu and len(lasers) < 3:   # 3 lasers maximum à l'écran
        laser = turtle.Turtle()
        laser.shape("square")
        laser.color("red")
        laser.shapesize(0.2, 1)      # un rectangle fin
        laser.setheading(90)         # tourné vers le haut
        laser.penup()
        laser.goto(vaisseau.xcor(), vaisseau.ycor() + 20)
        lasers.append(laser)         # on l'ajoute à la liste
        # >>> MISSION 2 : un son de laser


def recommencer():
    global score, vies, en_jeu
    if en_jeu == False:          # seulement si la partie est finie
        score = 0
        vies = 3
        replacer_en_haut(etoile)
        for m in meteorites:
            replacer_en_haut(m)
        for laser in lasers:
            laser.hideturtle()
        lasers.clear()
        message.clear()
        afficher_infos()
        en_jeu = True


ecran.listen()
ecran.onkeypress(aller_a_gauche, "Left")
ecran.onkeypress(aller_a_droite, "Right")
ecran.onkeypress(monter, "Up")
ecran.onkeypress(descendre, "Down")
ecran.onkeypress(tirer, "space")
ecran.onkeypress(recommencer, "r")


# ----- La boucle de jeu -----
def boucle_de_jeu():
    global score, vies, en_jeu

    if en_jeu:
        # 1. L'étoile tombe
        etoile.sety(etoile.ycor() - vitesse_chute)
        if etoile.ycor() < -300:
            replacer_en_haut(etoile)

        # 2. Le vaisseau attrape l'étoile
        if vaisseau.distance(etoile) < 30:
            score = score + 1
            # >>> MISSION 2 : un son quand on attrape une étoile
            replacer_en_haut(etoile)
            afficher_infos()

        # 3. Les météorites tombent
        for m in meteorites:
            m.sety(m.ycor() - vitesse_chute)
            if m.ycor() < -320:
                replacer_en_haut(m)
            if vaisseau.distance(m) < 35:    # aïe, une météorite nous touche !
                vies = vies - 1
                # >>> MISSION 2 : un son d'explosion
                replacer_en_haut(m)
                afficher_infos()

        # 4. Les lasers montent
        for laser in lasers.copy():          # on parcourt une copie de la liste
            laser.sety(laser.ycor() + 15)
            touche = False
            for m in meteorites:             # est-ce qu'il touche une météorite ?
                if laser.distance(m) < 30:
                    replacer_en_haut(m)
                    score = score + 1
                    afficher_infos()
                    touche = True
            if touche or laser.ycor() > 300:
                laser.hideturtle()           # on cache le laser...
                lasers.remove(laser)         # ...et on le retire de la liste

        # >>> MISSION 3 : niveau suivant tous les 10 points

        # 5. Fin de la partie ?
        if vies <= 0:
            en_jeu = False
            afficher_message("GAME OVER - touche R pour rejouer")

    ecran.update()
    ecran.ontimer(boucle_de_jeu, 20)


# ----- C'est parti ! -----
afficher_infos()
boucle_de_jeu()
ecran.mainloop()
