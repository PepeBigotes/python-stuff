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


LOGO = r"""
           _           _              _    _   _                                 ___  
          | |         ( )            | |  | | (_)                               |__ \ 
 __      _| |__   ___ |/ ___    _ __ | | _| |_ _ _ __   __ _    _ __ ___   ___     ) |
 \ \ /\ / / '_ \ / _ \  / __|  | '_ \| |/ / __| | '_ \ / _` |  | '_ ` _ \ / _ \   / / 
  \ V  V /| | | | (_) | \__ \  | |_) |   <| |_| | | | | (_| |  | | | | | |  __/  |_|  
   \_/\_/ |_| |_|\___/  |___/  | .__/|_|\_\\__|_|_| |_|\__, |  |_| |_| |_|\___|  (_)  
                               | |                      __/ |                         
                               |_|                     |___/                          
"""
LOCAL_IP = get_if_addr(conf.iface)
LOCAL_MAC = get_if_hwaddr(conf.iface)
GATEWAY_IP = conf.route.route("0.0.0.0")[2]
GATEWAY_MAC = getmacbyip(GATEWAY_IP)

pkters = {}


def handle_pkt(pkt):
    src = pkt[0].src
    pkts = pkters.get(src, 0) +1
    pkters[src] = pkts

def display_pkters():
    os.system('cls' if os.name=='nt' else 'clear')
    print(LOGO)
    print(f"iface: {LOCAL_IP} ({LOCAL_MAC})")
    if GATEWAY_MAC: print(f"GW:    {GATEWAY_IP} ({GATEWAY_MAC})\n")
    global pkters
    if pkters:
        print("         MAC        │ Nº of packets")
        print(" ───────────────────┼───────────────")
        for src in pkters.keys():
            pkts = pkters.get(src)
            if src == LOCAL_MAC: src = "     YOURSELF    "
            if src == GATEWAY_MAC: src = "        GW       "
            print(f"  {src} │ {pkts}")



sniffer = AsyncSniffer(store=0, prn=handle_pkt)
sniffer.start()

try:
    while True:
        display_pkters()
        sleep(1)
except KeyboardInterrupt:
    sniffer.stop()
    display_pkters()
    print("\nKeyboardInterrupt")
    exit()