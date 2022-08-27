from devoir1 import Scrapper
from numpy import product
import requests
from bs4 import BeautifulSoup
import pandas as pd

PRODUCT_URL = 'https://www.fabellashop.com/categorie-produit/maquillageongles/teint/'

URL='http://www.floatrates.com/daily/xof.xml'


#Classe pour recuperer la donnee depuis url 

class DataConver(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result

#Permet de creer des methodes
class Scrapper2(object):
    
    @classmethod
    def scrapLink(cls, URL):
        return DataConver \
            .httpFetcher(URL)
            
    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result, "lxml")
    
    @classmethod
    def getConv(cls, URL, oldProductList):
        soupering = cls.souper(URL)       

        soupering = soupering\
         .find_all('item')      
        #print(soupering)

        six_currency=[]

        for souper in soupering:
            item1 = souper.find('title') 
            item1=item1.text.split(" ")
            six_currency.append({
                    "Price":item1[3],
                    "Currency":item1[-1],
                })

        six_currency=six_currency[0:6]

        for currency in six_currency:
            for oldProduct in oldProductList:
                oldProduct.update({currency["Currency"]: float(oldProduct["price"])*float(currency["Price"])})  

        data_collect = pd.DataFrame(oldProductList)
        data_collect.to_csv("CollectedData.csv", index=False)

        data_collect_read = pd.read_csv("CollectedData.csv")

        print(data_collect_read)
        
        return oldProductList
        

    @classmethod
    def main(cls):
        productsName = Scrapper.getProduct(PRODUCT_URL)
        data = Scrapper.getPrice(PRODUCT_URL,productsName)
        Scrapper2.getConv(URL, data)
    

Scrapper2.main()    