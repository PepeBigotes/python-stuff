#!/usr/bin/env python3
#Created by PepeBigotes

import os

def try_input(msg) -> str:
    try: x = input(msg)
    except KeyboardInterrupt: print("\nKeyboardInterrupt"); exit()
    return x

try:
	try: from pyppeteer import launch
	except ImportError:
		print("[!] Module 'selenium' in not installed")
		try_input("  Press ENTER to install it (or CTRL+C to exit)")
		os.system('pip3 install pyppeteer')
		try: from pyppeteer import launch
		except ImportError: print("\n[!] Pyppeteer couldn't be installed"); exit(1)
		try_input("\n  Dependencies installed, press ENTER to continue")
except KeyboardInterrupt: print("\nKeyboardInterrupt"); exit()

import sys
import requests
import asyncio
from time import sleep
from bs4 import BeautifulSoup



# CONSTS / CONFIG
RAE_DOMAIN = "dle.rae.es"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
BSOUP_PARSER = "html.parser"

VALID_CHARS = "qweértyuúiíoópaásdfghjklñzxcvbnm-"

ERROR_CHROMIUM = """\
[!] pypeteer attempts to download an outdated version of Chromium
    Check these links:
    https://stackoverflow.com/questions/78023508/pyton-request-html-is-not-downloading-chromium
    https://github.com/pyppeteer/pyppeteer/issues/463
"""


# VERIFY INPUT
try: INPUT = sys.argv[1]
except IndexError:
    print("[!] You need to put the word you wanna look for:")
    print("    python3 rae-scraper.py <YOUR WORD HERE>")
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
async def get_content():
    try: browser = await launch(headless=True)
    except OSError:
        print(ERROR_CHROMIUM)
        exit(1)
    page = await browser.newPage()
    await page.setUserAgent(USER_AGENT)
    await page.goto(URL)
    await page.waitForNavigation()
    global CONTENT
    CONTENT = await page.content()
    await browser.close()

print(f"[*] Getting the contents of {URL} ...",end='\r')
asyncio.get_event_loop().run_until_complete(get_content())
print(f"[+] Got the contents of {URL}        ")


# SCRAP CONTENT
soup = BeautifulSoup(CONTENT, BSOUP_PARSER)
#print(soup.prettify())
results = soup.find('div', attrs={'id':'resultados'})

definitions = results.find_all(attrs={'class':'j'})
synant = results.find(attrs={'class':'div-sin-ant'})
try: synonyms = synant.findChildren("ul", recursive=False)[0]
except IndexError: synonyms = []
try: antonyms = synant.findChildren("ul", recursive=False)[1]
except IndexError: antonyms = []


# PRINTS
os.system('cls' if os.name=='nt' else 'clear')
print('\n' + INPUT + '\n')
print("DEFINICIONES:")
for i in definitions: print("  " + i.get_text())
print("SINÓNIMOS:")
for i in synonyms: print("  " + i.get_text())
print("ANTÓNIMOS:")
for i in antonyms: print("  " + i.get_text())