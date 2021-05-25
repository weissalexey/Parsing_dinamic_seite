import requests, lxml
from bs4 import BeautifulSoup
#import json
#import csv

def get_data(url):
    headers =  { 
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    } 

    #req = requests.get( url, headers)
    #print (req.text)
    #with open("index.html", "a", encoding='utf-8' ) as file:
    #    file.write(req.text)



get_data("http://www.edutainme.ru/edindex/")

with open("index.html") as file:
    src=file.read()

soup=BeautifulSoup(src,"lxml")
articles=soup.find_all("article",class_="ib19")

for article in articles:
    projekt_u