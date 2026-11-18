# Créez un dictionnaire
nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

# créer un nouveau dictionnaire avec des accolades vides {}
taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
# créer un nouveau dictionnaire avec la fonction dict()
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

# Accédez à une valeur dans un dictionnaire
print(nouvelle_campagne['responsable_de_campagne'])
print(taux_de_conversion['facebook'])

# Ajoutez une paire clé-valeur
infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris" #  ajouter une nouvelle paire clé-valeur
print(infos_labradoodle)

infos_labradoodle["poids"] = "45 kg" # écraser la valeur existante de la clé "poids"
print(infos_labradoodle)

# Supprimez une paire clé-valeur
del infos_labradoodle["origine"]
print(infos_labradoodle)

# Vérifiez l’existence d’une clé spécifique
print("poids" in infos_labradoodle)
print("race" in infos_labradoodle)