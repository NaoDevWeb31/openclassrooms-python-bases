# Écrivez votre code ici !
import csv

# retourne les données du fichier `input.csv`
def extract(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file, delimiter=',')
        return list(reader)

# transformer les données et la créer un nouveau conteneur avec toutes les nouvelles données
def transform(data_to_transform):
    names_to_load = []
    salaries_to_load = []

    for ligne in data_to_transform:
        names_to_load.append(ligne['nom'])
        salaries_to_load.append(int(ligne['heures_travaillees']) * 15)

    return names_to_load, salaries_to_load

# charger les nouvelles données dans le fichier `output.csv`
def load(names_to_load, salaries_to_load, filename='output.csv'):
    headers = ['nom', 'salaire']
    with open(filename, mode='w', newline='') as output_file:
            writer = csv.writer(output_file, delimiter=',')
            writer.writerow(headers)
            for name, salary in zip(names_to_load, salaries_to_load):
                writer.writerow([name, salary])

def main():
    data_to_transform = extract('input.csv')
    # print(data_to_transform)
    names_to_load, salaries_to_load = transform(data_to_transform)
    # print(names_to_load, salaries_to_load)
    load(names_to_load, salaries_to_load)
    # print("Données chargées dans output.csv")


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
