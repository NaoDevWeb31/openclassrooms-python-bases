# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel):
    # retourne le salaire mensuel correspondant en divisant le salaire annuel par 12
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    # retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    # retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par le nombre d'heures travaillées par semaine
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

# Demandez à l'utilisateur de saisir son salaire annuel
salaire_annuel = input("Veuillez saisir votre salaire annuel : ")
salaire_annuel = float(salaire_annuel)

# Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine
heures_travaillees = input("Veuillez saisir le nombre d'heures travaillées par semaine : ")
heures_travaillees = float(heures_travaillees)

# Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant
salaire_mensuel_utilisateur = salaire_mensuel(salaire_annuel)
salaire_hebdomadaire_utilisateur = salaire_hebdomadaire(salaire_mensuel_utilisateur)
salaire_horaire_utilisateur = salaire_horaire(salaire_hebdomadaire_utilisateur, heures_travaillees)

# Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros"
print(f"Votre salaire horaire est de {salaire_horaire_utilisateur} euros")
