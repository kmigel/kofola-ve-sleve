#!/usr/bin/env python3
import requests, random
from bs4 import BeautifulSoup

r = requests.get("https://www.kupi.cz/sleva/kofola")

soup = BeautifulSoup(r.content, "html.parser")
s = soup.find("div", class_="relative product_discounts product_discounts_overview")
discounts = s.find_all("tr", class_="discount_row only_discount")

l = ["Běž do obchodu ", "Zajdi do obchodu ", "Zaběhni do obchodu ", "Vleť do obchodu ", "Kup si buldozer a vjeď do obchodu "]

for discount in discounts:
    shopName = " ".join(discount.find("span", class_="discounts_shop_name").find("a").find("span").text.strip().split())
    litresAmount = discount.find("div", class_="discount_amount left").text.strip()[2:]
    price = discount.find("strong", class_="discount_price_value").text.strip()
    print(random.choice(l) + shopName + " a kup si " + litresAmount + " kofoly za " + price)