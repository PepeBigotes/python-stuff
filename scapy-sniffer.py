#!/usr/bin/env python3
#Created by PepeBigotes

from scapy.all import * #pip install scapy
from time import sleep
n_pkts = 0




# MAIN CONFIG #

FILTERED_LAYERS = [
    DHCP,
    #DNS,
    ARP,
    #ICMP,
    ]




# MISC CONFIG #

DEFAULT_BEFORE_HEADER = "  "
DEFAULT_AFTER_HEADER = ": "

ARP_TYPES = {
    1: "request",
    2: "reply",
    }
BOOTP_TYPES = {
    1: "request",
    2: "reply",
    }
DHCP_TYPES = {
    1: "discover",
    2: "offer",
    3: "request",
    4: "decline",
    5: "ack",
    6: "nak",
    }




# FUNCTIONS #

def handle_pkt(pkt):
    filter_pkt = True
    for layer in FILTERED_LAYERS:
        if pkt.haslayer(layer): filter_pkt = False
    if filter_pkt: return
    
    global n_pkts
    n_pkts += 1
    now_time = datetime.now().strftime("%H:%M:%S.%f")
    pkt_time = pkt.time
    print(f"[{now_time}] PACKET {n_pkts}")

    if pkt.haslayer(Ether): handle_Ether(pkt)
    if pkt.haslayer(ARP): handle_ARP(pkt)
    if pkt.haslayer(IP): handle_IP(pkt)
    if pkt.haslayer(UDP): handle_UDP(pkt)
    if pkt.haslayer(BOOTP): handle_BOOTP(pkt)
    if pkt.haslayer(DHCP): handle_DHCP(pkt)
    print()

def layer_print(header, *args, **kwargs):
    before_header = kwargs.get('before_header', DEFAULT_BEFORE_HEADER)
    after_header = kwargs.get('after_header', DEFAULT_AFTER_HEADER)
    if args:
        print(f"{before_header}{header}{after_header}{args[0]}")
        if len(args) == 1: return
        before_data = " " * len(f"{before_header}{header}{after_header}")
        for i in range(1, len(args)):
            print(f"{before_data}{args[i]}")
    if not args:
        print(f"{before_header}{header}")



def handle_Ether(pkt):
    eth = pkt[Ether]
    src = eth.src #Source Address
    dst = eth.dst #Destination Address
    t = hex(eth.type) #EtherType (https://en.wikipedia.org/wiki/EtherType#Values)
    layer_print("Ether", f"src={src} dst={dst}  type={t}")

def handle_ARP(pkt):
    arp = pkt[ARP]
    hwsrc = arp.hwsrc #Hardware Source Address (MAC)
    psrc = arp.psrc #Protocol Source Address (IP)
    hwdst = arp.hwdst #Hardware Destination Address (MAC)
    pdst = arp.pdst #Protocol Destination Address (IP)
    op = ARP_TYPES.get(arp.op) #Operation Code (Request or Response)
    hwtype = arp.hwtype #Hardware Type
    ptype = arp.ptype #Protocol Type
    hwlen = arp.hwlen #Hardware Address length
    plen = arp.plen #Protocol Adress length
    layer_print(f"ARP {op}", f"hwsrc={hwsrc} psrc={psrc}  hwdst={hwdst} pdst={pdst}")


def handle_IP(pkt):
    ip = pkt[IP]
    src = ip.src #Source Address
    dst = ip.dst #Destination Address
    ttl = ip.ttl #Packet Time-to-Live (Max Hops)
    lenght = ip.len #Packet length (in bytes)
    proto = ip.proto #Protocol number
    ver = ip.version #IP version (4 or 6)
    chksum = ip.chksum #Checksum
    ihl = ip.ihl #Internet Header Length (32 bit words)
    tos = ip.tos #Type of Service
    frag = ip.frag #Fragmented Packet Offset
    flags = ip.flags #IP Flags (DF, MF)
    fid = ip.id #Fragmentation Packet ID
    layer_print("IP", f"src={src} dst={dst}  ttl={ttl} len={lenght} proto={proto}")


def handle_UDP(pkt):
    udp = pkt[UDP]
    sport = udp.sport #Source Port
    dport = udp.dport #Destination Port
    lenght = udp.len #Packet length (in bytes)
    chksum = udp.chksum #Checksum
    layer_print("UDP", f"sport={sport} dport={dport}  len={lenght}")


def handle_BOOTP(pkt):
    bootp = pkt[BOOTP]
    op = BOOTP_TYPES.get(bootp.op) #Operation Code (BOOTREQUEST or BOOTREPLY)
    htype = bootp.htype #Hardware Type
    hlen = bootp.hlen #Hardware Address Lenght
    hops = bootp.hops #Number of Relay Agent Hops
    xid = bootp.xid #Transaction ID
    secs = bootp.secs #Seconds since initialization
    flags = bootp.flags #Flags (Unicast or Broadcast)
    ciaddr = bootp.ciaddr #Client IP Address (Existing/Old IP if there is one)
    yiaddr = bootp.yiaddr #Your (Client) IP Address (Offered IP)
    siaddr = bootp.siaddr #Server IP Address
    giaddr = bootp.giaddr #Gateway IP Address
    chaddr = Ether(src=bootp.chaddr[:bootp.chaddr.index(0x00)]).src #Client Hardware Address (MAC)
    sname = bootp.sname #Server Name (64 Bytes, not a string)
    file = bootp.file #Boot File Name
    options = bootp.options #DHCP Options
    s_yiaddr = f" yiaddr={yiaddr}" if (yiaddr != "0.0.0.0") else ""
    s_siaddr = f" siaddr={siaddr}" if (siaddr != "0.0.0.0") else ""
    s_giaddr = f" giaddr={giaddr}" if (giaddr != "0.0.0.0") else ""
    s_ciaddr = f" ciaddr={ciaddr}" if (ciaddr != "0.0.0.0") else ""
    s_chaddr = f"chaddr={chaddr}"
    s_flags = f"flags={flags} " if flags else ""
    s_sname = f"sname={sname.decode()} " if int.from_bytes(sname) else ""
    layer_print(f"BOOTP {op}", f"{s_chaddr}{s_ciaddr} {s_yiaddr} {s_siaddr}{s_giaddr}" ,\
                               f"{s_flags}{s_sname}xid={xid}")


def handle_DHCP(pkt):
    dhcp = pkt[DHCP].options
    def get_opt(option):
        for opt in dhcp:
            if isinstance(opt, tuple) and opt[0] == option: return opt[1]
        return None
    mtype = DHCP_TYPES.get(get_opt("message-type")) #Message type
    client_id = get_opt("client_id") #Client Identifier
    server_id = get_opt("server_id") #Server Identifier (Server IP, MAC, or other)
    requested_addr = get_opt("requested_addr") #Requested IP Address
    max_dhcp_size = get_opt("max_dhcp_size") #Max packet size (in bytes)
    vendor_class_id = get_opt("vendor_class_id") #Vendor Class Identifier (e.g 'android-dhcp-24')
    hostname = get_opt("hostname").decode() if get_opt("hostname") else None #Client Hostname
    s_hostname = f"hostname={hostname} " if hostname else ""
    layer_print(f"DHCP {mtype}", f"req_ip={requested_addr} server={server_id}  {s_hostname}id={client_id}")




# MAIN LOOP #

sniffer = AsyncSniffer(store=0, prn=handle_pkt)
sniffer.start()

while True:
    try: sleep(1)
    except KeyboardInterrupt:
        print()
        print("KeyboardInterrupt, stopping sniffer...")
        sniffer.stop()
        print(f"Sniffed a total of {n_pkts} packets")
        exit()