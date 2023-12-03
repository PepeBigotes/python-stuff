#!/usr/bin/env python3
#Created by PepeBigotes

from scapy.all import * #pip install scapy
import requests
from time import sleep


def fake_packet(ip_src= "192.168.0.1", ip_dst= "192.168.0.255", mac_src=RandMAC(), port= 80):
    ip = IP(ttl=64, src=ip_src, dst=ip_dst)
    fakemac = Ether(src=mac_src)
    ports = TCP(sport=port,dport=port)
    return fakemac/ip/ports
#mypacket = fake_packet()
#sendp(mypacket, count=100)

def dns_query(ip_dst, query):
    ip = IP(ttl=64, dst=ip_dst)
    udp = UDP(dport=53)
    dns = DNS(rd=1, qd=DNSQR(qname=query))
    answer = sr1(ip/udp/dns, verbose=0)[DNS].summary()
    return answer.split('"')[1]
#print(dns_query("8.8.8.8", "google.com"))

def mac_vendor(mac_address):
    url = "https://api.macvendors.com/"
    response = requests.get(url+mac_address)
    if response.status_code != 200: return("")
    return response.content.decode()
#print(mac_vendor("00-1B-63-84-45-E6"))

def arp_discover(dst="192.168.0.0/24"):
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=dst)
    answer, no_answer = srp(ether/arp, timeout=5, verbose=1, inter=0.03)
    answer.summary(lambda s, r: r.sprintf(f"%Ether.src%  %ARP.psrc% {mac_vendor(r.sprintf('%Ether.src%') )}") )
#arp_discover("192.168.0.0/24")
