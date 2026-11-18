# Chargez des données avec les fonctions intégrées de Python
fichier = open("hello.txt", "w") # pour créer un nouveau fichier
fichier.write("Hello, world!")
fichier.close()

with open("hello.txt") as fichier: # pour fermer automatiquement le fichier à la fin du bloc
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)

import csv

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])