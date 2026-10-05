# ==================================================
#   CHASSEUR D'ÉTOILES - mon jeu d'arcade en Python
#   Séance 2 - la fenêtre et le vaisseau qui bouge
#   Créé par : ............   <-- écris ton prénom ici
# ==================================================
#
#   Les lignes marquées  >>> A TOI  sont à compléter.
#   Remplace chaque  ___  par la bonne valeur, puis lance avec F5.

import turtle

# ----- La fenêtre du jeu -----
ecran = turtle.Screen()
ecran.title("Chasseur d'étoiles")
ecran.setup(800, 600)            # largeur 800, hauteur 600
ecran.bgcolor(___)               # >>> A TOI : une couleur entre guillemets, ex : "black"

# ----- Les réglages -----
vitesse = ___                    # >>> A TOI : de combien de pas bouge le vaisseau ? (essaie 20)

# ----- Le vaisseau -----
vaisseau = turtle.Turtle()
vaisseau.shape("triangle")       # sa forme
vaisseau.color(___)              # >>> A TOI : la couleur de ton vaisseau
vaisseau.speed(0)                # 0 = le plus rapide
vaisseau.penup()                 # on lève le crayon : pas de trait
vaisseau.setheading(90)          # il pointe vers le haut
vaisseau.goto(___, ___)          # >>> A TOI : en bas, au milieu (x, y)

# ----- Le titre (déjà prêt) -----
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
    # >>> A TOI : 3 lignes, comme aller_a_gauche... mais vers la droite !
    ___


ecran.listen()                              # l'écran écoute le clavier
ecran.onkeypress(aller_a_gauche, "Left")    # flèche gauche
# >>> A TOI : relie la fonction aller_a_droite à la flèche "Right"


ecran.mainloop()   # garde la fenêtre ouverte (toujours à la fin !)
