import json
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from re import sub
from utils import price_to_float

lst_result = [] 

class Scraper:
    
    def __init__(self, category):
        self.category = category
        with open('./ecommerces.json') as f:
            data = json.load(f)
        self.all_resources = data

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
        items = soup.find("div", {"class":"main"}).find_all("div",{"class": "product"})
        for item in items:
            title = item.get("data-name")
            link = item.get("data-link")
            price = item.find("span", {"class": "BestPrice"}).text
            price_formated = price_to_float(price)
            lst_result.append({"title":title, "price": price_formated, "link": link})
        return lst_result
    
    def all_ecommerce(self):
        return self.ln() + self.fb() + self.rp() + self.oc()

