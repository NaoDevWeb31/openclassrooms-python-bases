# Écrivez votre code ici !

from bs4 import BeautifulSoup

# Récupérez les éléments suivants dans le code html et stockez-les dans des variables, puis affichez-les dans la console :
with open("index.html", "r") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

# le titre de la page (<title> )
    title = soup.title.string
    print(title)

# le texte de la balise <h1> avec ID "titre"
    h1 = soup.find(id="titre")
    h1_text = h1.string
    print(h1_text)

# les informations sur les produits :
all_products = {}
products = soup.find_all("li")
for product in products:
    # nom du produits
    name = product.find("h2").string
    # prix du produit (par exemple: 20€)
    price = product.find(class_="price")
    # description
    description = product.find("p", {"class": None })
    # utilisez un dictionnaire pour stocker ces informations pour tous les produits.
    all_products[name] = {
        "price": price.string,
        "description": description.string
    }


for name, product in all_products.items():
    # Nettoyez les prix des produits pour ne garder qu'un nombre (retirez le mot prix, et:). Vous pouvez utiliser la fonction Python split
    product["price"] = product["price"].split("Prix: ")[1]
    product["description"] = product["description"].split("Description : ")[1]

    # Convertissez les prix en euro vers le dollar (considérez que le prix dollar = euro * 1.2)
    product["price_dollar"] = f"{float(product["price"].replace("€", "")) * 1.2}$"

print(all_products)