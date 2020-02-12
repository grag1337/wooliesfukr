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

#https://www.telegraph.co.uk/food-and-drink/features/best-online-grocery-shopping-sites-one-delivers-goods/
# The /all is the same one in the first link, do not double up /all
tescoFresh = "https://www.tesco.com/groceries/en-GB/shop/fresh-food/all" #/all?page=2 - 164
tescoBakery = "https://www.tesco.com/groceries/en-GB/shop/bakery/all" #/all?page=2 - 31
tescoFrozen = "https://www.tesco.com/groceries/en-GB/shop/frozen-food/all" #/all?page=2 - 43
tescoCupboard = "https://www.tesco.com/groceries/en-GB/shop/food-cupboard/all" #/all?page=2 - 296
tescoDrinks = "https://www.tesco.com/groceries/en-GB/shop/drinks/all" #/all?page=2 - 124
tescoBaby = "https://www.tesco.com/groceries/en-GB/shop/baby/all" #/all?page=2 - 35
tescoHousehold = "https://www.tesco.com/groceries/en-GB/shop/household/all" #/all?page=2 - 48

def eatShit():
    url = "https://www.tesco.com/groceries/en-GB/shop/fresh-food/all"
    hdr = {"User Agent": "Firefox/5.0"}
    req = Request(url, headers=hdr)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    soup2 = soup.findAll(class_="sc-kAzzGY fvsqm")
    print(soup2)

eatShit()