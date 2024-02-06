#!/usr/bin/env python3
from time import sleep
chars = ['|', '/', '-', '\\']

try:
    while True:
        for i in chars:
            sleep(0.2)
            print(i, end='\r')
except KeyboardInterrupt: exit()