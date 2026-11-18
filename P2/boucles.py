# Utilisez la boucle for
races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

# Comprenez le fonctionnement de la boucle for
for x in range(5):
    print(x)

for x in range(100):
    print(f"{x} bouteilles de bières au mur !")

# Utilisez la boucle while
capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print(f"Capacité actuelle : {capacite_actuelle}")

# Utilisez les mot-clés break et continue
for i in range(10):
    if i == 5:
        break
    print(i)

liste = [1, 2, 3, 4, 5]
# Boucle for sur la liste
for element in liste:
    if element == 3:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
    # Dans tous les autres cas, on exécute le reste du code
    print(element)