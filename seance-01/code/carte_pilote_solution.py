# ==================================================
#   MA CARTE DE PILOTE
#   Séance 1 - corrigé
# ==================================================

print("==============================")
print("   BIENVENUE À L'ACADÉMIE")
print("        DES PILOTES !")
print("==============================")

# On pose des questions, et on range les réponses dans des variables
prenom = input("Comment t'appelles-tu ? ")
age = int(input("Quel âge as-tu ? "))         # int() : transforme le texte en nombre
planete = input("Quelle est ta planète préférée ? ")
couleur = input("De quelle couleur est ton vaisseau ? ")

# On affiche la carte
print()
print("****** CARTE DE PILOTE ******")
print("Pilote :", prenom)
print("Âge :", age, "ans")
print("Planète préférée :", planete)
print("Vaisseau :", couleur)
print("Dans 10 ans, tu auras", age + 10, "ans : prêt pour l'espace !")
print("*****************************")
