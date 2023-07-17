#!/usr/bin/env python3
import requests, random, sys
from bs4 import BeautifulSoup

drink_url = "kofola"
drink_text = "kofoly"

if(len(sys.argv) > 2):
    print("Too many arguments")
    quit()
if(len(sys.argv) == 2 and sys.argv[1] == "-p"):
    drink_url = "limonada-pepsi"
    drink_text = "pepsi"

r = requests.get("https://www.kupi.cz/sleva/" + drink_url)

soup = BeautifulSoup(r.content, "html.parser")
s = soup.find("div", class_="relative product_discounts product_discounts_overview")
discounts = s.find_all("tr", class_="discount_row only_discount")

l = ["Běž do obchodu ", "Zajdi do obchodu ", "Zaběhni do obchodu ", "Vleť do obchodu ", "Kup si buldozer a vjeď do obchodu "]

for discount in discounts:
    shopName = " ".join(discount.find("span", class_="discounts_shop_name").find("a").find("span").text.strip().split())
    litresAmount = discount.find("div", class_="discount_amount left").text.strip()[2:]
    price = discount.find("strong", class_="discount_price_value").text.strip()
    print(random.choice(l) + shopName + " a kup si " + litresAmount + " " + drink_text + " za " + price)