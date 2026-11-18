# Ecrivez votre code ici !
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")

if nombre1.isnumeric() and nombre2.isnumeric():
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
    operation = input("Entrez l'opération (+, -, *, /) : ")

    match operation:
        case "+":
            result = nombre1 + nombre2
        case "-":
            result = nombre1 - nombre2
        case "*":
            result = nombre1 * nombre2
        case "/":
            if nombre2 == 0:
                print("Erreur: impossible de diviser par zéro.")
                raise SystemExit("Fin du programme")
            else:
                result = nombre1 / nombre2
        case _:
            print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
            raise SystemExit("Fin du programme")

    print("Le résultat est :", round(result, 2))
else:
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")