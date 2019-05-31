from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.newegg.com/global/in-en/p/pl?Submit=ENE&N=-1&IsNodeId=1&d=graphics%20card&page=1&bop=And&PageSize=36&order=BESTMATCH'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
#print(page_soup.h1)

# Grabs each product from the page
containers = page_soup.findAll("div",{"class":"item-container"})
container = containers[4]

filename = "items.csv"
f = open(filename, 'w')

headers = "product_title, brand, price\n"

f.write(headers)

for container in containers:
    title_container = container.img['alt']
    product_title = print("product_title: " + title_container)

    for brand in container.findAll('a',{"class":"item-brand"}):
        brand = print("brand: " + brand.img["title"])

    #price_container1 = container.findAll("span",{"class":"price-current-label"})
    #print(product_price)
    for price in container.findAll('li', {"class":"price-current"}):
        price = print("price: " + price.text.strip())

    #f.write(product_title +   +  brand  +   + price + "\n")

f.close()

#import pandas as pd

#df = pd.read_csv('items.csv')
