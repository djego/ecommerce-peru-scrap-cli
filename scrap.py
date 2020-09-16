import csv
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from re import sub
 

lst_result = [] 
def scrap_ln(): 
    ## Linio
    req = requests.get('https://www.linio.com.pe/c/portatiles/laptops?price=1000-37539')
    soup = BeautifulSoup(req.text, "lxml")
    lst_result = []
    for item in soup.find_all("div",{"class": "catalogue-product"}):
        title = item.find("a").get('title')
        link  = item.find("a").get('href')
        price = item.find("a").find("div",{'class':'price-section'}).find("meta",{"itemprop":"price"}).get("content")
        link_trans = 'https://linio.com.pe'+link
        price_formated = Decimal(price)
        lst_result.append({"title":title, "price": price_formated, "link": link_trans})
    return lst_result
def scrap_fb():
    ## Falabella
    req = requests.get('https://www.falabella.com.pe/falabella-pe/category/cat40712/Laptops')
    soup = BeautifulSoup(req.text, "lxml")
    lst_result = []
    for item in soup.find("div",{"id": "testId-searchResults-products"}).find_all("div",{"class": "search-results-list"}):
        link  = item.find("a").get('href')
        title = item.find("b",{"class": "pod-subTitle"}).text
        price = item.find("ol",{"class":"fa--prices"}).find("li",{"class": "price-0"}).get("data-undefined-price")
        price_formated = Decimal(sub(r'[^\d.]', '', price))
        lst_result.append({"title":title, "price": price_formated, "link": link})
    return lst_result

def scrap_rp():
    ## Ripley 
    req = requests.get('https://simple.ripley.com.pe/tecnologia/computadoras/laptops')
    soup = BeautifulSoup(req.text, "lxml")

    lst_result = []
    items = soup.find("div",{"id": "catalog-page"}).find_all("div",{"class": "ProductItem"})
    for item in items:
        title = item.find("a",{"class":"ProductItem__Name"}).text
        link  = item.find("a",{"class":"ProductItem__Name"}).get("href")
        price_el = item.find("li",{"class": "catalog-prices__offer-price"})
        price2_el  = item.find("li",{"class": "catalog-prices__list-price"})
        if price_el:
            price_formated = Decimal(sub(r'[^\d.]', '', price_el.text))
        else: 
            if price2_el:
                price_formated = Decimal(sub(r'[^\d.]', '', price2_el.text))
            else:
                price_formated = Decimal(0)
        
        link_trans = 'https://simple.ripley.com.pe'+link
        lst_result.append({"title":title, "price": price_formated, "link": link_trans})

    return lst_result


if __name__ == '__main__':
    fb = scrap_fb()
    rp = scrap_rp()
    ln = scrap_ln()
    total = fb + rp + ln 
    keys = total[0].keys()
    with open("products.csv", "w", newline="") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(total)
    