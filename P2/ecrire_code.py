# Ne vous répétez pas
premiere_campagne = {'visiteurs': 1000, 'conversions': 50}
seconde_campagne = {'visiteurs': 1500, 'conversions': 75}
troisieme_campagne = {'visiteurs': 2000, 'conversions': 100}

# taux_de_conversion1 = premiere_campagne['visiteurs'] / premiere_campagne['conversions']
# taux_de_conversion2 = seconde_campagne['visiteurs'] / seconde_campagne['conversions']
# taux_de_conversion3 = troisieme_campagne['visiteurs'] / troisieme_campagne['conversions']

def calculer_taux_de_conversion(campagne): #  transformer en fonction
    taux_de_conversion = campagne['visiteurs'] / campagne['conversions']
    return taux_de_conversion
taux_de_conversion1 = calculer_taux_de_conversion(premiere_campagne)
taux_de_conversion2 = calculer_taux_de_conversion(seconde_campagne)
taux_de_conversion3 = calculer_taux_de_conversion(troisieme_campagne)

# Documentez votre code
def somme(a, b):
    """
    Cette fonction calcule la somme de deux nombres et retourne le résultat.

    Parameters:
    a (int): le premier nombre
    b (int): le deuxième nombre

    Returns:
    int: la somme de a et b
    """
    return a + b

help(somme) # pour afficher la docstring

# Gérez les erreurs et les exceptions
while True:
    try:
        x = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Oops ! Ce n'est pas un nombre entier. Essayez encore...")
    # except Exception as err:
    #     print(f"Unexpected {err=}, {type(err)=}")
    # finally:
    #     print(f"Vous avez entré le nombre entier : {x}")
