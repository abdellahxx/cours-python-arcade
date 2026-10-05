# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 7 - les vies, la fin de partie et nos propres fonctions
#   Créé par : ............
# ==================================================

import turtle
import random

# ----- La fenêtre du jeu -----
ecran = turtle.Screen()
ecran.title("Chasseur d'étoiles")
ecran.setup(800, 600)
ecran.bgcolor("midnightblue")
ecran.tracer(0)

# ----- Les réglages -----
vitesse = 20
vitesse_chute = 4
score = 0
vies = 3                         # le nombre de vies
en_jeu = True                    # True = on joue, False = la partie est finie


# ----- Les fonctions utiles -----
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
vaisseau.shape("triangle")
vaisseau.color("cyan")
vaisseau.speed(0)
vaisseau.penup()
vaisseau.setheading(90)
vaisseau.goto(0, -250)

# ----- L'étoile -----
etoile = turtle.Turtle()
etoile.shape("circle")
etoile.color("gold")
etoile.penup()
replacer_en_haut(etoile)

# ----- Les météorites -----
meteorites = []
for i in range(5):
    m = turtle.Turtle()
    m.shape("circle")
    m.color("gray")
    m.shapesize(2)
    m.penup()
    replacer_en_haut(m)
    meteorites.append(m)

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


def recommencer():
    global score, vies, en_jeu
    if en_jeu == False:          # seulement si la partie est finie
        score = 0
        vies = 3
        replacer_en_haut(etoile)
        for m in meteorites:
            replacer_en_haut(m)
        message.clear()
        afficher_infos()
        en_jeu = True


ecran.listen()
ecran.onkeypress(aller_a_gauche, "Left")
ecran.onkeypress(aller_a_droite, "Right")
ecran.onkeypress(monter, "Up")
ecran.onkeypress(descendre, "Down")
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
            replacer_en_haut(etoile)
            afficher_infos()

        # 3. Les météorites tombent
        for m in meteorites:
            m.sety(m.ycor() - vitesse_chute)
            if m.ycor() < -320:
                replacer_en_haut(m)
            if vaisseau.distance(m) < 35:    # aïe, une météorite nous touche !
                vies = vies - 1
                replacer_en_haut(m)
                afficher_infos()

        # 4. Fin de la partie ?
        if vies <= 0:
            en_jeu = False
            afficher_message("GAME OVER - touche R pour rejouer")

    ecran.update()
    ecran.ontimer(boucle_de_jeu, 20)


# ----- C'est parti ! -----
afficher_infos()
boucle_de_jeu()
ecran.mainloop()
