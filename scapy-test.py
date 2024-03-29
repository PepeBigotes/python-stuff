#!/usr/bin/env python3
#Created by PepeBigotes

try: from scapy.all import *
except ImportError:
    print("[!] You need to have Scapy installed to run this script")
    print("    Try 'pip3 install scapy' or 'sudo apt install python3-scapy'")
    exit()
import requests
from time import sleep


def fake_packet(ip_src= "192.168.0.1", ip_dst= "192.168.0.255", mac_src=RandMAC(), port= 80):
    pkt = Ether(src=mac_src) /\
          IP(ttl=64, src=ip_src, dst=ip_dst) /\
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

def get_mac_from_ip(i_ip):
    fake_mac = RandMAC()
    network = '.'.join(i_ip.split('.')[0:3]) + '.0/24'
    fake_ip = str(RandIP(network))
    fake_ip = IP(src=fake_ip).src
    pkt = Ether(src=fake_mac, dst='ff:ff:ff:ff:ff:ff') /\
          ARP(op=1, pdst=i_ip, hwsrc=fake_mac, psrc=fake_ip)
    ans = srp1(pkt, timeout=3, retry=-2, verbose=0)
    if not ans: return None
    return ans[ARP].hwsrc
#print(get_mac_from_ip('192.168.1.1'))

def arp_discover(dst="192.168.0.0/24", get_mac_vendors=True):
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") /\
          ARP(pdst=dst)
    answers, no_answers = srp(pkt, timeout=5, verbose=1, inter=0.03)
    vendors_cache = {}
    for i in answers:
        pkt = i.answer
        ip = pkt[ARP].psrc
        if get_mac_vendors:
            mac = pkt[Ether].src.split(":")
            mac = f"{mac[0]}:{mac[1]}:{mac[2]}"
            if vendors_cache.get(mac): vendor = vendors_cache.get(mac) # Get vendor from cache
            else:
                vendor = mac_vendor(mac) # Get vendor from API
                vendors_cache[mac] = vendor
        if not get_mac_vendors: vendor = ""
        mac = pkt[Ether].src
        fill = " " * (15 - len(ip))
        print(f"{mac}  {ip}{fill}  {vendor}")
#arp_discover("192.168.0.0/24")
#arp_discover(input("Select a network to scan (e.g 192.168.1.0/24) \n > "))