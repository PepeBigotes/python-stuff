#!/usr/bin/env python3
#Created by PepeBigotes

import os

def try_input(msg) -> str:
    try: x = input(msg)
    except KeyboardInterrupt: print("\nKeyboardInterrupt"); exit()
    return x

try:
	try: from selenium import webdriver
	except ImportError:
		print("[!] Module 'selenium' in not installed")
		try_input("  Press ENTER to install it (or CTRL+C to exit)")
		os.system('pip3 install selenium')
		try: from selenium import webdriver
		except ImportError: print("\n[!] Selenium couldn't be installed"); exit(1)
		try_input("\n  Dependencies installed, press ENTER to continue")
except KeyboardInterrupt: print("\nKeyboardInterrupt"); exit()

import sys
import requests
from time import sleep
from bs4 import BeautifulSoup



# CONSTS / CONFIG
RAE_DOMAIN = "dle.rae.es"
BSOUP_PARSER = "html.parser"

VALID_CHARS = "qweértyuúiíoópaásdfghjklñzxcvbnm-"


# VERIFY INPUT
try: INPUT = sys.argv[1]
except IndexError:
    print("[!] You need to put the word you wanna look for:")
    print("    python3 raescraper.py <YOUR WORD HERE>")
    exit(1)

for char in INPUT:
    if not char in VALID_CHARS:
        print(f"[!] Invalid input: {INPUT} ({char})")
        exit(1)
        
URL = "https://"+RAE_DOMAIN+"/"+INPUT


# CHECK CONNECTION
try:
    x = requests.get(URL, timeout=5)
except requests.ConnectionError:
    print(f"[!] Cannot reach {URL}\n  Check your internet connection and try again")
    exit(1)


# GET CONTENT
print(f"[*] Getting the contents of {URL} ...",end='\r')
driver = webdriver.Firefox()
driver.get(URL)
sleep(1)
CONTENT = driver.page_source
print(f"[+] Got the contents of {URL}        ")
driver.quit()
sleep(.5)



# SCRAP CONTENT
soup = BeautifulSoup(CONTENT, BSOUP_PARSER)
#print(soup.prettify())
results = soup.find('div', attrs={'id':'resultados'})
if "no está en el Diccionario" in results.get_text():
    notfound = f"La palabra {INPUT} no está en el Diccionario."
    related = "Las entradas que se muestran a continuación podrían estar relacionadas:"
    itemlist = results.findAll('div', attrs={'class':'n1'})
    os.system('cls' if os.name=='nt' else 'clear')
    print('\n' + notfound)
    if len(itemlist) > 0:
        print('\n' + related)
        for i in itemlist: print("  " + i.get_text())
    exit()

definitions = results.find_all(attrs={'class':'j'})
synant = results.find(attrs={'class':'div-sin-ant'})
try: synonyms = synant.findChildren("ul", recursive=False)[0]
except IndexError: synonyms = []
try: antonyms = synant.findChildren("ul", recursive=False)[1]
except IndexError: antonyms = []



# PRINTS
os.system('cls' if os.name=='nt' else 'clear')
print('\n' + INPUT + '\n')
print("DEFINITIONS:")
for i in definitions: print("  " + i.get_text())
print("SYNONYMS:")
for i in synonyms: print("  " + i.get_text())
print("ANTONYMS:")
for i in antonyms: print("  " + i.get_text())