# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 2 - la fenêtre et le vaisseau qui bouge
#   Créé par : ............
# ==================================================

import turtle

# ----- La fenêtre du jeu -----
ecran = turtle.Screen()
ecran.title("Chasseur d'étoiles")
ecran.setup(800, 600)
ecran.bgcolor("midnightblue")

# ----- Les réglages -----
vitesse = 20                     # de combien de pas bouge le vaisseau

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
    x = vaisseau.xcor()          # où est le vaisseau ?
    x = x - vitesse              # un peu plus à gauche
    vaisseau.setx(x)             # on le déplace


def aller_a_droite():
    x = vaisseau.xcor()
    x = x + vitesse
    vaisseau.setx(x)


ecran.listen()                              # l'écran écoute le clavier
ecran.onkeypress(aller_a_gauche, "Left")    # flèche gauche
ecran.onkeypress(aller_a_droite, "Right")   # flèche droite

ecran.mainloop()
