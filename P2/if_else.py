# Définissez des conditions avec les instructions if/else
ensoleille = True
if ensoleille:
    print("on va à la plage !")
else:
    print("on reste à la maison !")

# Définissez des conditions alternatives en ajoutant une clause elif
ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")

# Définissez des conditions multiples avec des opérateurs logiques
avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")

# Définissez des conditions complexes avec des expressions comparatives
nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
    # autoriser plus d’invités
    print("On peut inviter plus de personnes.")
elif nombre_dinvites == nombre_de_sieges:
    # ne pas autoriser plus d’invités
    print("On ne peut pas inviter plus de personnes. Il y a déjà", nombre_de_sieges, "invités.")
else:
    # ne pas autoriser plus d’invités
    print("On ne peut pas inviter plus de personnes.")

# Simplifiez votre code avec les match cases
fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")

# Interagissez avec l’utilisateur
saisie = input("Entrez votre âge : ")

if saisie.isnumeric():
        age = int(saisie)
        if age >= 18:
            print("Vous êtes majeur.")
        else:
            print("Vous êtes mineur.")
else:
    print("Veuillez entrer un nombre valide.")
