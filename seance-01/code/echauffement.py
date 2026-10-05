# ==================================================
#   ÉCHAUFFEMENT - la tortue qui dessine
#   Séance 1
# ==================================================

import turtle

tortue = turtle.Turtle()
tortue.shape("turtle")      # elle ressemble à une tortue
tortue.color("green")       # couleur de la tortue et du trait
tortue.pensize(3)           # épaisseur du trait

# Un carré : 4 fois "avance, puis tourne à gauche"
tortue.forward(100)
tortue.left(90)

tortue.forward(100)
tortue.left(90)

tortue.forward(100)
tortue.left(90)

tortue.forward(100)
tortue.left(90)

turtle.done()   # garde la fenêtre ouverte
