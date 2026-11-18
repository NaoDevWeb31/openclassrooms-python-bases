# Ecrivez votre code ici !
nombres = input("Entrez une liste de nombres séparés par des espaces (ex: 1,2,3,4) : ")

nombres = nombres.split(",")
print("Liste de nombres sous forme de chaînes de caractères :", nombres)

liste_entiers = [int(nombre) for nombre in nombres]
print("Liste des nombres entiers :", liste_entiers)

somme = 0
for nombre in liste_entiers:
    print(nombre)
    somme += nombre
print("Somme des nombres :", somme)

moyenne = somme / len(liste_entiers)
print("Moyenne des nombres :", moyenne)

nombre_superieur_a_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_superieur_a_moyenne += 1
    else:
        continue
print("Nombre de nombres supérieurs à la moyenne :", nombre_superieur_a_moyenne)