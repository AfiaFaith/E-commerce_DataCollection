# Voir le output de notre trvail:

import requests

# Lien du site web où on va collecter nos données:

URL_Countries = 'https://restcountries.com/v2/all'


# Recuperation et visualisation de nos données:

donnée = requests.get(URL_Countries)
# print(donnée.json()) pour affichier le resultat

# Effectuons une correspondance entre les noms des pays et leur drapeau:

countries = donnée.json()
mappedCountryData = []

for country in countries:
    # print(country['name']) pour affichier le resultat
    
    mappedCountryData.append({'nom': country['name']})

# print(mappedCountryData) pour affichier le resultat

for data in mappedCountryData:
    flag = {'flag': country['flag']}
    for country in countries:
     data.update() 