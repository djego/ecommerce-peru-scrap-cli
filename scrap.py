import csv
import json
import os
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from re import sub
from utils import *

lst_result = [] 

class Scraper:
    


    def __init__(self, category):
        self.category = category
        self.all_resources = {
            "laptop": {
                "linio": "https://www.linio.com.pe/c/portatiles/laptops",
                "falabella": "https://www.falabella.com.pe/falabella-pe/category/cat40712/Laptops",
                "ripley": "https://simple.ripley.com.pe/tecnologia/computadoras/laptops",
                "oechsle": "https://www.oechsle.pe/tecnologia/computo/laptops",
            },
            "celular": {
                "linio": "https://www.linio.com.pe/c/celulares-y-tablets/celulares-y-smartphones",
                "falabella": "https://www.falabella.com.pe/falabella-pe/category/cat760706/Celulares-y-Smartphones",
                "ripley": "https://simple.ripley.com.pe/tecnologia/celulares/ver-todo-celulares",
                "oechsle": "https://www.oechsle.pe/tecnologia/telefonia/celulares",
            }
        }  

    def ln(self): 
        req = requests.get(self.all_resources[self.category]["linio"])
        soup = BeautifulSoup(req.text, "lxml")
        lst_result = []
        for item in soup.find_all("div",{"class": "catalogue-product"}):
            title = item.find("a").get('title')
            link  = item.find("a").get('href')
            price = item.find("a").find("div",{'class':'price-section'}).find("meta",{"itemprop":"price"}).get("content")
            link_trans = 'https://linio.com.pe'+link
            price_formated = price_to_float(price)
            lst_result.append({"title":title, "price": price_formated, "link": link_trans})
        return lst_result
    def fb(self):
        req = requests.get(self.all_resources[self.category]["falabella"])
        soup = BeautifulSoup(req.text, "lxml")
        lst_result = []
        if self.category == 'celular':
            items = soup.find("div",{"id": "testId-searchResults-products"}).find_all("div",{"class": "search-results-4-grid"})

        else:
            items = soup.find("div",{"id": "testId-searchResults-products"}).find_all("div",{"class": "search-results-list"})
        for item in items:
            link  = item.find("a").get('href')
            title = item.find("b",{"class": "pod-subTitle"}).text
            price = item.find("ol",{"class":"fa--prices"}).find("li",{"class": "price-0"}).get("data-undefined-price")
            price_formated = price_to_float(price)
            lst_result.append({"title":title, "price": price_formated, "link": link})
        return lst_result

    def rp(self):
        req = requests.get(self.all_resources[self.category]["ripley"])
        soup = BeautifulSoup(req.text, "lxml")

        lst_result = []
        if self.category == 'celular':
            items = soup.find("div",{"class": "catalog-container"}).find_all("a",{"class": "catalog-product-item"})
            for item in items:
                title = item.find("div",{"class": "catalog-product-details__name"}).text
                link =  item.get("href")
                price_el = item.find("li",{"class": "catalog-prices__offer-price"})
                price2_el  = item.find("li",{"class": "catalog-prices__list-price"})
                price = price_el.text if price_el != None else None
                if price == '':
                    price = price2_el.text if price2_el != None else None
                
                price_formated = price_to_float(price)
                link_trans = 'https://simple.ripley.com.pe'+link
                lst_result.append({"title":title, "price": price_formated, "link": link_trans})
            return lst_result
        else:
            items = soup.find("div",{"id": "catalog-page"}).find_all("div",{"class": "ProductItem"})
            for item in items:
                title = item.find("a",{"class":"ProductItem__Name"}).text
                link  = item.find("a",{"class":"ProductItem__Name"}).get("href")
                price_el = item.find("li",{"class": "catalog-prices__offer-price"})
                price2_el  = item.find("li",{"class": "catalog-prices__list-price"})
                price = price_el.text if price_el != None else None
                if price == '':
                    price = price2_el.text if price2_el != None else None
                
                price_formated = price_to_float(price)
                link_trans = 'https://simple.ripley.com.pe'+link
                lst_result.append({"title":title, "price": price_formated, "link": link_trans})
            return lst_result

    def oc(self):
        req = requests.get(self.all_resources[self.category]["oechsle"])
        soup = BeautifulSoup(req.text, "lxml")
        lst_result = []    
        items = soup.find("div", {"class":"vitrina"}).find_all("div",{"class": "product"})
        for item in items:
            title = item.get("data-name")
            link = item.get("data-link")
            price = item.get("data-product-price")
            price_formated = price_to_float(price)
            lst_result.append({"title":title, "price": price_formated, "link": link})
        return lst_result
    
    #TODO este metodo no corresponde a la naturaleza de la clase
    def export(self, data, format="csv", filename="out"):

        all_formats = ("csv","json")
        filename_path = os.getcwd() + "/out/"+filename+"."+format
        #FIXME go to class in fhe future
        if not os.path.exists(os.path.dirname(filename_path)):
            try:
                os.makedirs(os.path.dirname(filename_path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        
        if format in all_formats:
            if format == "csv":
                keys = data[0].keys()
                with open(filename_path, "w", newline="") as f:
                    dict_writer = csv.DictWriter(f, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(data)
            if format == "json":
                with open(filename_path, 'w') as outfile:
                    json.dump(data, outfile)

        print("Exported: %s items" % str(len(data)))