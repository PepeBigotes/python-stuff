#!/usr/bin/env python3
#Created by PepeBigotes

import os
import threading
import time

os.system('cls' if os.name == 'nt' else 'clear')
print("┌─┐┬┌┐┌┌─┐   ┌─┐┬ ┬┌─┐┌─┐┌─┐")
print("├─┘│││││ ┬───└─┐│││├┤ ├┤ ├─┘")
print("┴  ┴┘└┘└─┘   └─┘└┴┘└─┘└─┘┴  ")
print()

print("Select a target IP (default is 192.168.0.1):")
target = str(input(" > "))
if not target: target = "192.168.0.1"
print()

argument = ('-n 1' if os.name == 'nt' else '-c 1')
nuller = ('>nul' if os.name == 'nt' else '>/dev/null')

dot = target.rfind(".")
target = target[0:dot + 1]


def ping(x):
    global target
    host = target + str(x)
    response = os.system(f"ping {argument} -w 1000 {host} {nuller}")
 
    if response == 0:
        print(host)
#    else:
#        print(host + " is down")
        

for y in range(1, 255):
    thread = threading.Thread(target=ping, args=[y])
    thread.start()
    time.sleep(0.1)