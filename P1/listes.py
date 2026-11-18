# Qu’est-ce qu’une liste et pourquoi l’utiliser ?
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

# Accédez aux éléments d’une liste
print(plateformes_sociales[0]) # accéder au premier élément
print(plateformes_sociales[1]) # accéder au deuxième élément
print(plateformes_sociales[-1]) # accéder au dernier élément de la liste

# Accédez aux caractères d’une chaîne comme un élément d’une liste
langage_de_programmation = "PYTHON"
print(langage_de_programmation[2])
print(langage_de_programmation[-4])

# Modifiez les éléments d’une liste
plateformes_sociales[2] = "LinkedIn"
print(plateformes_sociales)

# Ajoutez, retirez et triez les listes
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
plateformes_sociales.append("TikTok")
print(plateformes_sociales) # ajouter une plateforme de réseau social à la fin de la liste existante

plateformes_sociales.remove("Snapchat")
print(plateformes_sociales) # retirer la première instance d'une plateforme de réseau social de la liste existante

print(len(plateformes_sociales)) # connaître la longueur de la liste

plateformes_sociales.sort() # trier les éléments de la liste (alphabétiquement pour les listes de chaînes et numériquement pour les listes de nombres)
print(plateformes_sociales)

del plateformes_sociales[0] # supprimer un élément de la liste
print(plateformes_sociales)

# Découvrez les tuples
plateformes_sociales_tuple = ("Facebook", "Instagram", "TikTok", "Twitter")

# Trouvez un élément
nombres = [1,2,3,4,5]
print(5 in nombres)
print(8 in nombres)

