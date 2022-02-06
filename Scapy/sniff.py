from scapy.all import *

#see what sprintf does
# sniff(count=1, prn = lambda a: a.summary())
# pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))

def arp_display(aab):
    if aab[ARP].op == 1:  # who-has (request)
        return f"Request: {aab[ARP].psrc} is asking about {aab[ARP].pdst}"
    if aab[ARP].op == 2:  # is-at (response)
        return f"*Response: {aab[ARP].hwsrc} has address {aab[ARP].psrc}"

sniff(prn=arp_display, filter="arp", store=0, count=10)