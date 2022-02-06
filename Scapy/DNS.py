from scapy.all import *


def getdns(pkt):
    if pkt.haslayer(IP):
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
    else:
        ip_src = pkt[IPv6].src
        ip_dst = pkt[IPv6].dst
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        return f"{ip_src} -> {ip_dst}, {pkt.getlayer(DNS).qd.qname}"


sniff(filter="port 53", prn=getdns, store=0, count=1)
