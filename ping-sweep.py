#!/usr/bin/env python3
#Created by PepeBigotes

import os
import threading
import time
import socket

os.system('cls' if os.name == 'nt' else 'clear')
print("""\
┌─┐┬┌┐┌┌─┐   ┌─┐┬ ┬┌─┐┌─┐┌─┐
├─┘│││││ ┬───└─┐│││├┤ ├┤ ├─┘
┴  ┴┘└┘└─┘   └─┘└┴┘└─┘└─┘┴ 
""")

print("Select a target IP (default is 192.168.0.1):")
target = str(input(" > "))
if not target: target = "192.168.0.1"
os.system('cls' if os.name == 'nt' else 'clear')

print(f"[ Ping-Sweeping {target} ... ] Hold CTRL+C to stop")
print()

argument = ('-n 1' if os.name == 'nt' else '-c 1')
nuller = ('>nul' if os.name == 'nt' else '>/dev/null')

dot = target.rfind(".")
target = target[0:dot + 1]


def ping(x):
    global target
    host = target + str(x)
    for i in range(0, 5):
        response = os.system(f"ping {argument} -w 1000 {host} {nuller}")
        time.sleep(1)
        if response == 0:
            hostname = socket.getfqdn(host)
            hostname = hostname if hostname is not host else "-"
            space = " " * (18 -len(host))
            print(f"+ {host}{space}Hostname: {hostname}")
            return
        

for y in range(1, 255):
    thread = threading.Thread(target=ping, args=[y])
    thread.start()
    time.sleep(0.1)