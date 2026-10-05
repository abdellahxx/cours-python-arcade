# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 5 - attraper les étoiles et compter les points
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
# >>> A TOI : crée une variable score qui vaut 0 au début


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

# ----- Le stylo (il écrit le score en haut à gauche) -----
stylo = turtle.Turtle()
stylo.hideturtle()
stylo.penup()
stylo.color("white")
stylo.goto(___, ___)             # >>> A TOI : en haut à gauche (essaie -380, 260)


def afficher_score():
    stylo.clear()                                        # efface l'ancien score
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
    global score                 # on va modifier la variable score du jeu

    # 1. L'étoile tombe
    y = etoile.ycor()
    y = y - vitesse_chute
    etoile.sety(y)
    if etoile.ycor() < -300:
        etoile.goto(random.randint(-370, 370), 300)

    # 2. Le vaisseau attrape l'étoile
    # >>> A TOI : SI la distance entre le vaisseau et l'étoile est plus petite que 30 :
    #               - ajoute 1 au score
    #               - affiche le score
    #               - remets l'étoile en haut


    ecran.update()
    ecran.ontimer(boucle_de_jeu, 20)


# ----- C'est parti ! -----
afficher_score()
boucle_de_jeu()
ecran.mainloop()
