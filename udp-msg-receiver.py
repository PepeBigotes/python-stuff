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

from time import sleep


os.system('cls' if os.name=='nt' else 'clear')
print("""\
       _                                         _             
 _ _ _| |___    _____ ___ ___    ___ ___ ___ ___|_|_ _ ___ ___ 
| | | . | . |  |     |_ -| . |  |  _| -_|  _| -_| | | | -_|  _|
|___|___|  _|  |_|_|_|___|_  |  |_| |___|___|___|_|\_/|___|_|  
        |_|              |___|                                 

""")



try:
    LOCAL_IP = get_if_addr(conf.iface)
    print(f"Host: {LOCAL_IP}")
    PORT = int(input("Port: "))
except KeyboardInterrupt:
    print("\n\nKeyboardInterrupt")
    exit()



def handle_pkt(pkt):
    if not pkt.haslayer(IP): return
    if not pkt.haslayer(UDP): return
    if pkt[UDP].dport != PORT: return

    payload = bytes(pkt[UDP].payload)
    try: msg_utf8 = payload.decode("utf-8")
    except UnicodeDecodeError: pass
    if msg_utf8:
        src = pkt[IP].src
        print(f"[{src}] {msg_utf8}")



sniffer = AsyncSniffer(filter="udp", prn=handle_pkt, store=0)
sniffer.start()
print(f"\nListening for UDP messages on port {PORT}, press CTRL+C to stop")


try:
    while True: sleep(1)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
    sniffer.stop()
    exit()