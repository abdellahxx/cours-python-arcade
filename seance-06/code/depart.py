# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 6 - une pluie de météorites (listes et boucles)
#   Créé par : ............
# ==================================================
#
#   Les lignes marquées  >>> A TOI  sont à compléter.

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
etoile.goto(random.randint(-370, 370), 300)

# ----- Les météorites -----
meteorites = []                  # une liste vide : le "train" des météorites
for i in range(___):             # >>> A TOI : combien de météorites ? (essaie 5)
    m = turtle.Turtle()          # ...on crée une météorite
    m.shape("circle")
    m.color("gray")
    m.shapesize(2)               # 2 fois plus grosse
    m.penup()
    m.goto(random.randint(-370, 370), random.randint(300, 600))
    # >>> A TOI : ajoute m au bout de la liste meteorites (avec append)
    ___

# ----- Le stylo (il écrit le score en haut à gauche) -----
stylo = turtle.Turtle()
stylo.hideturtle()
stylo.penup()
stylo.color("white")
stylo.goto(-380, 260)


def afficher_score():
    stylo.clear()
    stylo.write("Score : " + str(score), font=("Arial", 18, "bold"))


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


ecran.listen()
ecran.onkeypress(aller_a_gauche, "Left")
ecran.onkeypress(aller_a_droite, "Right")
ecran.onkeypress(monter, "Up")
ecran.onkeypress(descendre, "Down")


# ----- La boucle de jeu -----
def boucle_de_jeu():
    global score

    # 1. L'étoile tombe
    y = etoile.ycor()
    y = y - vitesse_chute
    etoile.sety(y)
    if etoile.ycor() < -300:
        etoile.goto(random.randint(-370, 370), 300)

    # 2. Le vaisseau attrape l'étoile
    if vaisseau.distance(etoile) < 30:
        score = score + 1
        afficher_score()
        etoile.goto(random.randint(-370, 370), 300)

    # 3. Les météorites tombent
    # >>> A TOI : POUR CHAQUE météorite m de la liste meteorites :
    #               - fais-la descendre de vitesse_chute
    #               - SI elle sort en bas (plus petit que -320), remets-la en haut
    #             (regarde comment on fait pour l'étoile juste au-dessus !)



    ecran.update()
    ecran.ontimer(boucle_de_jeu, 20)


# ----- C'est parti ! -----
afficher_score()
boucle_de_jeu()
ecran.mainloop()
