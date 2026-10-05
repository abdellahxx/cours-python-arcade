# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 4 - la boucle de jeu et le hasard
#   Créé par : ............
# ==================================================

import turtle
import random

# ----- La fenêtre du jeu -----
ecran = turtle.Screen()
ecran.title("Chasseur d'étoiles")
ecran.setup(800, 600)
ecran.bgcolor("midnightblue")
ecran.tracer(0)                  # c'est nous qui rafraîchissons l'écran

# ----- Les réglages -----
vitesse = 20                     # vitesse du vaisseau
vitesse_chute = 4                # vitesse de l'étoile qui tombe

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
etoile.goto(random.randint(-370, 370), 300)   # x au hasard, tout en haut

# ----- Le titre -----
stylo = turtle.Turtle()
stylo.hideturtle()
stylo.penup()
stylo.color("white")
stylo.goto(0, 200)
stylo.write("Chasseur d'étoiles", align="center", font=("Arial", 32, "bold"))


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
    # 1. L'étoile tombe
    y = etoile.ycor()
    y = y - vitesse_chute
    etoile.sety(y)

    # 2. Si elle sort en bas, elle revient en haut à un endroit au hasard
    if etoile.ycor() < -300:
        etoile.goto(random.randint(-370, 370), 300)

    ecran.update()                     # on redessine l'écran
    ecran.ontimer(boucle_de_jeu, 20)   # et on recommence dans 20 millisecondes


# ----- C'est parti ! -----
boucle_de_jeu()
ecran.mainloop()
