from bs4 import BeautifulSoup
from os import system, name
from time import sleep
from subprocess import call
import urllib
import socket
import requests
from urllib.request import Request, urlopen
from art import *
import re
import keyboard
import os

def clear():
    if name == 'nt':
        system('cls')

    else:
        system('clear')

def eatShit(url):
    clear()
    print("[*] Scanning " + url)
    print()
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = Request(url, headers=hdr)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    soup2 = soup.findAll(class_="sc-chPdSV gRJrUF")
    for div in soup2:
        print(div.text)

#https://www.telegraph.co.uk/food-and-drink/features/best-online-grocery-shopping-sites-one-delivers-goods/
# The /all is the same one in the first link, do not double up /all
tescoFresh = "https://www.tesco.com/groceries/en-GB/shop/fresh-food/all" #/all?page=2 - 164
tescoBakery = "https://www.tesco.com/groceries/en-GB/shop/bakery/all" #/all?page=2 - 31
tescoFrozen = "https://www.tesco.com/groceries/en-GB/shop/frozen-food/all" #/all?page=2 - 43
tescoCupboard = "https://www.tesco.com/groceries/en-GB/shop/food-cupboard/all" #/all?page=2 - 296
tescoDrinks = "https://www.tesco.com/groceries/en-GB/shop/drinks/all" #/all?page=2 - 124
tescoBaby = "https://www.tesco.com/groceries/en-GB/shop/baby/all" #/all?page=2 - 35
tescoHousehold = "https://www.tesco.com/groceries/en-GB/shop/household/all" #/all?page=2 - 48

print("Do you want \n [+] 1. Fresh Food \n [+] 2. Bakery Food \n [+] 3. Frozen Food \n [+] 4. Cupboard Food? \n [+] 5. Drinks \n [+] 6. Baby Isle? \n [+] 7. Household Items")
print("This will be automated eventually, i'm just retarded.")
ass = input("Eat ass or skate fast? \n [-] : ")
if ass == "1":
    eatShit(tescoFresh)
elif ass == "2":
    eatShit(tescoBakery)
elif ass == "3":
    eatShit(tescoFrozen)
elif ass == "4":
    eatShit(tescoCupboard)
elif ass == "5":
    eatShit(tescoDrinks)
elif ass == "6":
    eatshit(tescoBaby)
elif ass == "7":
    eatshit(tescoHousehold)
else:
    print("Wrong Answer Buddy..")

