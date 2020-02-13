import keyboard  # using module keyboard
import tweepy
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

auth = tweepy.OAuthHandler("DjljXGx9rF9QlqaIkuIEI4NmG","GTSz0vOc1qCiVb4Yg7XmCWZz4NENtYNsNytEFqdY8km0hs0Bxe")

auth.set_access_token("1227579454945255425-AF61yS6PyYxmnVXcld3TT6QgYY4AvI", "HhFLiTdzAa22On655Bp5oAjivAzYXOwVOCMR5ObVPPl3b")

api = tweepy.API(auth)

url = "https://ghostbin.co/paste/j2d54/raw"
hdr = {'User Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")
soup2 = str(soup)
soup3 = soup2.splitlines()
def eatmyass(soup3):

    try:
        for index, value in enumerate(soup3):
            api.update_status("[+] 9gag " + value)
            soup3.pop(0)
            print("[*] Tweeted [+] 9gag " + value + "!")
            print("[+] Waiting 10 minutes.")
            sleep(600)
    except KeyboardInterrupt:
        print("Exiting Program...")
    except tweepy.TweepError:   
        soup3.pop(0)
        print("Found Duplicate, Skipping...")
        eatmyass(soup3)

eatmyass(soup3)
