import io
from bs4 import BeautifulSoup
import requests
import urllib
from art import *
import io
import os
from time import sleep
import pickle
import glob
from urllib.request import Request, urlopen

# Work on page numbers etc..

wooliesFruit = "https://www.woolworths.com.au/shop/browse/fruit-veg" # ?pageNumber=2 - 9
wooliesDeli = "https://www.woolworths.com.au/shop/browse/meat-seafood-deli" # ?pageNumber=2 - 28
wooliesBakery = "https://www.woolworths.com.au/shop/browse/bakery" # ?pageNumber=2 - 14
wooliesDairy = "https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge" # ?pageNumber=2 - 43
wooliesPantry = "https://www.woolworths.com.au/shop/browse/pantry" # ?pageNumber=2 - 171
wooliesFreezer = "https://www.woolworths.com.au/shop/browse/freezer" # ?pageNumber=2 - 29
wooliesDrinks = "https://www.woolworths.com.au/shop/browse/drinks" # ?pageNumber=2 - 35
wooliesLiqour = "https://www.woolworths.com.au/shop/browse/liquor" # One Page
wooliesBaby = "https://www.woolworths.com.au/shop/browse/baby" # ?pageNumber=2 - 17
wooliesHousehold = "https://www.woolworths.com.au/shop/browse/household" # ?pageNumber=2 - 112
wooliesHnB = "https://www.woolworths.com.au/shop/browse/health-beauty" # ?pageNumber=2 - 110

def fuckyou(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    print(soup)

fuckyou(wooliesLiqour)