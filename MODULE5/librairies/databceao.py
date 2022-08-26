import json
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import random

PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts'
URL = f'https://www.bceao.int/fr/{PATH_URL}'

#Classe pour recuperer la donnee depuis l'url 

class DataSouper(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result

class CurrencyScrapper(object):
    
    @classmethod
    def scrapLink(cls, URL):
        return DataSouper \
            .httpFetcher(URL)
    
    
    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result,
            'html.parser')
    
    @classmethod
    def getBoxCourse(cls, URL):
        soupering = cls.souper(URL)
        soupering = soupering \
            .find_all(attrs={
                'id': 'box_cours'})
        if soupering:
            table = soupering[0].table
            return table
        return None
    
    
    @classmethod
    def makeCurrencyList(cls, URL):
        soupering = cls.getBoxCourse(URL)
        if soupering:
            tr = soupering.find_all('tr')
            factory = [
                item.find_all('td')
                for item in tr
            ][1:]
            factory = [
                {
                    'Devise': x.string.strip(),
                    'Achat': float(y.string.strip().replace(',', '.')),
                    'Vente': float(z.string.strip().replace(',', '.')),
                }
                for (x, y, z) in factory
            ]
            return factory
        return None

    @classmethod
    def addRandomDevise(cls, factory):
        a = ["Euro", "Dollar", "Yen"]
        for item in factory:
            item.update( {"new_devise":random.choice(a)})
        return factory

    @classmethod
    def addXofConversion(cls, factory):
        for item in factory:
            if item["new_devise"] == "Euro":
                item.update( {"XOF_conversion": item["Vente"] * 654.23 })
            elif item["new_devise"] == "Dollar":
                item.update( {"XOF_conversion": item["Vente"] * 656.50 })
            else:
                item.update( {"XOF_conversion": item["Vente"] * 4.80 })
        return factory

    @classmethod
    def main(cls):
        data = CurrencyScrapper.makeCurrencyList(URL)
        result = CurrencyScrapper.addRandomDevise(data)
        myList = CurrencyScrapper.addXofConversion(result)
        
        return myList
        

CurrencyScrapper.main()
