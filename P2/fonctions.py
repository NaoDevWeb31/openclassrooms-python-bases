# Utilisez une fonction sans paramètres
def afficher_message():
    print("Bonjour, comment ça va ?")


afficher_message() # Appel de la fonction

# Utilisez une fonction avec paramètres
def afficher_nom_prenom(nom, prenom):
    print("Nom :", nom)
    print("Prénom :", prenom)

afficher_nom_prenom("Dupont", "Jean") # Appel de la fonction avec paramètres

# Utilisez une fonction avec une valeur de retour
def calculer_somme(a, b):
    resultat = a + b
    return resultat, a, b

somme = calculer_somme(2, 3)
print(somme) # Ce print affichera 5
