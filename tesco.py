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

try:
    def clear():
        if name == 'nt':
            system('cls')

        else:
            system('clear')

    clear()

    def eatShit(url, numnuts):
        assz = ("line \n" * numnuts)
        numnuts2 = numnuts + 1
        initnum = 2
        url2 = url + "?page=" + str(initnum)
        clear()
        print("[*] Scanning " + url)
        print("\n [*] Scanning Page 1")
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
        finalvalue = []
        for div in soup2:
            finalvalue.append(div.text + '\n') 
        while initnum < numnuts2:
            url2 = url + "?page=" + str(initnum)
            print("\n [*] Scanning Page " + str(initnum))
            req = Request(url2, headers=hdr)
            page = urlopen(req).read()
            soup = BeautifulSoup(page, "html.parser")
            soup2 = soup.findAll(class_="sc-chPdSV gRJrUF")
            for div in soup2:
                finalvalue.append(div.text + "\n")
            initnum = initnum + 1
        finalvalue2 = ''.join(finalvalue)
        finalvalue3 = finalvalue.replace("Tesco ", "")
        print("All done!")
        print("Writing to output.txt...")
        outputt = open("output.txt","w+")
        outputt.write(finalvalue3)
        outputt.close()
        print("Done!")

    def allinone(url1,url2,url3,url4,url5,url6,url7,numnuts2,numnuts3,numnuts4,numnuts5,numnuts6,numnuts7,numnuts8):
        urlnum = 1
        finalvalue = []
        while urlnum < 8:
            if urlnum == 1:
                url = url1
                numnuts = numnuts2
            elif urlnum == 2:
                url = url2
                numnuts = numnuts3
            elif urlnum == 3:
                url = url3
                numnuts = numnuts4
            elif urlnum == 4:
                url = url4
                numnuts = numnuts5
            elif urlnum == 5:
                url = url5
                numnuts = numnuts6
            elif urlnum == 6:
                url = url6
                numnuts = numnuts7
            elif urlnum == 7:
                url = url7
                numnuts = numnuts8
            else:
                print("Done!")
            assz = ("line \n" * numnuts)
            numnuts2 = numnuts + 1
            initnum = 2
            url2 = url + "?page=" + str(initnum)
            clear()
            print("[*] Scanning " + url)
            print("\n [*] Scanning Page 1")
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
                finalvalue.append(div.text + '\n')
            
            while initnum < numnuts2:
                url2 = url + "?page=" + str(initnum)
                print("\n [*] Scanning Page " + str(initnum))
                req = Request(url2, headers=hdr)
                page = urlopen(req).read()
                soup = BeautifulSoup(page, "html.parser")
                soup2 = soup.findAll(class_="sc-chPdSV gRJrUF")
                for div in soup2:
                    finalvalue.append(div.text + "\n")
                initnum = initnum + 1
            finalvalue2 = ''.join(finalvalue)
            finalvalue3 = finalvalue2.replace("Tesco ", "")
            print("All done!")
            print("Writing to output.txt...")
            outputt = open("output.txt", "w+")
            outputt.write(finalvalue3)
            outputt.close()
            print("Done!")
            urlnum = urlnum + 1
        
    
    # The /all is the same one in the first link, do not double up /all
    tescoFresh = "https://www.tesco.com/groceries/en-GB/shop/fresh-food/all" #/all?page=2 - 164
    tescoBakery = "https://www.tesco.com/groceries/en-GB/shop/bakery/all" #/all?page=2 - 31
    tescoFrozen = "https://www.tesco.com/groceries/en-GB/shop/frozen-food/all" #/all?page=2 - 43
    tescoCupboard = "https://www.tesco.com/groceries/en-GB/shop/food-cupboard/all" #/all?page=2 - 296
    tescoDrinks = "https://www.tesco.com/groceries/en-GB/shop/drinks/all" #/all?page=2 - 124
    tescoBaby = "https://www.tesco.com/groceries/en-GB/shop/baby/all" #/all?page=2 - 35
    tescoHousehold = "https://www.tesco.com/groceries/en-GB/shop/household/all" #/all?page=2 - 48

    print("Do you want \n [+] 1. Fresh Food \n [+] 2. Bakery Food \n [+] 3. Frozen Food \n [+] 4. Cupboard Food? \n [+] 5. Drinks \n [+] 6. Baby Isle? \n [+] 7. Household Items \n [+] 8. All of them *SCANS 741 PAGES*")
    print("This will be automated eventually, i'm just retarded.")
    ass = input("Eat ass or skate fast? \n [-] : ")
    if ass == "1":
        eatShit(tescoFresh, 164)
    elif ass == "2":
        eatShit(tescoBakery, 31)
    elif ass == "3":
        eatShit(tescoFrozen, 43)
    elif ass == "4":
        eatShit(tescoCupboard, 296)
    elif ass == "5":
        eatShit(tescoDrinks, 124)
    elif ass == "6":
        eatShit(tescoBaby, 35)
    elif ass == "7":
        eatShit(tescoHousehold, 48)
    elif ass == "8":
        allinone(tescoFresh,tescoBakery,tescoFrozen,tescoCupboard,tescoDrinks,tescoBaby,tescoHousehold,164,31,43,296,124,35,48)
    else:
        print("Wrong Answer Buddy..")

except KeyboardInterrupt:
    clear()
    print("Exiting Program...")
#except:
#    clear()
#    print("Unexpected Error")
