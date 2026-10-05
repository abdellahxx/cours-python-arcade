# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 3 - rester dans l'écran (les conditions)
#   Créé par : ............
# ==================================================
#
#   Les lignes marquées  >>> A TOI  sont à compléter.

import turtle

# ----- La fenêtre du jeu -----
ecran = turtle.Screen()
ecran.title("Chasseur d'étoiles")
ecran.setup(800, 600)
ecran.bgcolor("midnightblue")

# ----- Les réglages -----
vitesse = 20

# ----- Le vaisseau -----
vaisseau = turtle.Turtle()
vaisseau.shape("triangle")
vaisseau.color("cyan")
vaisseau.speed(0)
vaisseau.penup()
vaisseau.setheading(90)
vaisseau.goto(0, -250)

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
    if x > -380:                 # SI on reste dans l'écran...
        vaisseau.setx(x)         # ...ALORS on bouge


def aller_a_droite():
    x = vaisseau.xcor()
    x = x + vitesse
    if ___:                      # >>> A TOI : quelle condition pour le bord droit ?
        vaisseau.setx(x)


def monter():
    y = vaisseau.ycor()
    y = y + vitesse
    if y > -280 and y < -100:    # seulement dans la zone du bas
        vaisseau.sety(y)


def descendre():
    # >>> A TOI : 4 lignes, comme monter()... mais vers le bas !
    ___


ecran.listen()
ecran.onkeypress(aller_a_gauche, "Left")
ecran.onkeypress(aller_a_droite, "Right")
ecran.onkeypress(monter, "Up")
# >>> A TOI : relie descendre à la flèche "Down"


ecran.mainloop()
