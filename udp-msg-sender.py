#!/usr/bin/env python3
#Created by PepeBigotes

import os, ctypes
try: is_admin = (os.getuid() == 0)
except AttributeError: is_admin = (ctypes.windll.shell32.IsUserAnAdmin() != 0)
if not is_admin:
    print("[!] You need root/admin priviledges to run this script")
    print("    Forgot to use sudo?")
    exit()

try: from scapy.all import *
except ImportError:
    print("[!] You need to have Scapy installed to run this script")
    print("    Try 'pip3 install scapy' or 'sudo apt install python3-scapy'")
    exit()


os.system('cls' if os.name=='nt' else 'clear')
print("""\
       _                                       _         
 _ _ _| |___    _____ ___ ___    ___ ___ ___ _| |___ ___ 
| | | . | . |  |     |_ -| . |  |_ -| -_|   | . | -_|  _|
|___|___|  _|  |_|_|_|___|_  |  |___|___|_|_|___|___|_|  
        |_|              |___|                           

   KEEP IN MIND THAT YOUR MESSAGES ARE NOT ENCRYPTED!
""")



try:
    LOCAL_IP = get_if_addr(conf.iface)
    print(f"Host: {LOCAL_IP}")
    PORT = int(input("Port: "))
    DEST_IP = input("Dest IP: ")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
    exit()


def send_msg(dst, msg):
    pkt = IP(dst=dst) /\
          UDP(sport=PORT ,dport=PORT) /\
          msg
    send(pkt, verbose=0)
    #print(bytes(pkt[UDP].payload).decode("utf-8"))

print("\nWrite your message and press ENTER to send it. Press CTRL+C to exit script")
try:
    while True:
        msg = str(input(" > "))
        send_msg(DEST_IP, msg)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
    exit()