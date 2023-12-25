#!/usr/bin/env python3
#Created by PepeBigotes

from scapy.all import * #pip install scapy
import requests
from time import sleep


def fake_packet(ip_src= "192.168.0.1", ip_dst= "192.168.0.255", mac_src=RandMAC(), port= 80):
    pkt = IP(ttl=64, src=ip_src, dst=ip_dst) /\
          Ether(src=mac_src) /\
          TCP(sport=port,dport=port)
    return pkt
#mypacket = fake_packet()
#sendp(mypacket, count=100)

def dns_query(query, ip_dst="8.8.8.8", t_out=1):
    pkt = IP(dst=ip_dst) /\
          UDP(dport=53) /\
          DNS(rd=1, qd=DNSQR(qname=query))
    try:
        answer = sr1(pkt, verbose=0, timeout=t_out)[DNS].summary()
        ans = answer.split('"')[1]
        if ans == f"b'{query}.'": return None
        return ans
    except TypeError:
        return None
#print(dns_query("google.com"))

def mac_vendor(mac_address):
    url = "https://api.macvendors.com/"
    response = requests.get(url+mac_address)
    if response.status_code != 200: return("")
    return response.content.decode()
#print(mac_vendor("00-1B-63-84-45-E6"))

def arp_discover(dst="192.168.0.0/24"):
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") /\
          ARP(pdst=dst)
    answers, no_answers = srp(pkt, timeout=5, verbose=1, inter=0.03)
    for i in answers:
        pkt = i.answer
        mac = pkt[Ether].src
        ip = pkt[ARP].psrc
        fill = " " * (15 - len(ip))
        vendor = mac_vendor(mac)
        print(f"{mac}  {ip}{fill}  {vendor}")
#arp_discover("192.168.0.0/24")
