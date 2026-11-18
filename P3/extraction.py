# Le package Requests
import requests

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# Voir le code html source
print(page.content)

# Le package Beautiful Soup
from bs4 import BeautifulSoup
with open("index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')

   # Récupération du titre de la page HTML: 
   print(soup.title) # ==> <title>Exercice extraction HTML</title> (un élément HTML) 

   # Récupération de la chaîne de caractères du titre HTML 
   print(soup.title.string) # ==> "Exercice extraction HTML" 

   # Trouver tous les éléments avec la balise <h2> 
   print(soup.find_all('h2')) # ==> renvoie une liste d'éléments HTML 

   # Trouver le premier élément avec l’id `titre`
   print(soup.find(id="titre")) # ==> <h1 id="titre">Bienvenue sur notre site web</h1> 

   # Trouver tous les éléments <li>: 
   print(soup.find_all("li"))

   # Trouver tous les éléments <li> avec la classe "product" en utilisant un sélecteur CSS: 
   print(soup.select("li.product")) # ==> renvoie une liste d'éléments HTML

