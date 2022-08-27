from numpy import product
import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = 'https://www.fabellashop.com/categorie-produit/maquillageongles/teint/'

#Classe pour recuperer la donnee depuis url 

class DataSouper(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result

#Permet de creer des methodes
class Scrapper(object):
    
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
    def getProduct(cls, URL):
        all_products=[]
        soupering = cls.souper(URL)        
        
        soupering = soupering\
            .find_all(attrs={'class': 'product-small'})
        
        list_title=[]

        for souper in soupering:
            title = souper.find_all(attrs={"class":"woocommerce-loop-product__title"})
            title=title[0].string.strip()
            
            list_title.append(title)

        list_title = set(list_title)
        all_products=[
            {"title":title}
            for title in list_title
        ]

        return all_products    
                
                
    @classmethod
    def getPrice(cls, URL, products):
        
        soupering = cls.souper(URL)        
        
        soupering = soupering\
            .find_all('span', class_="woocommerce-Price-amount")

        soupering = soupering[1:]

        for (product, souper) in zip(products, soupering):
            souper=souper.text.split("\xa0")

            product.update({"price":souper[0].replace(".", '')})
            product.update({"currency": souper[-1]})
            product.update({"quantity": 1})

        return products
          
    

    @classmethod
    def main(cls):
        productsName = Scrapper.getProduct(URL)
        data = Scrapper.getPrice(URL, productsName)
        df=pd.DataFrame(data)
        print(df)

        

Scrapper.main()    