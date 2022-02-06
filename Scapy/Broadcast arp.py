from scapy.all import *

def scan(ip):
    arp_request = ARP(pdst = ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    ether_ip = broadcast/arp_request
    answered_list = srp(ether_ip, timeout = 2)[0]

    client_list= []
    print("IP\t\t\t\t\tMac Add\n====================================")
    for x in answered_list:
        d = {"ip": x[1].psrc, "mac": x[1].hwsrc}
        client_list.append(d)
        print(x[1].psrc + '\t\t' + x[1].hwsrc)            #second element in couple of (sent, answer)
        print("-----------------------")
    return client_list


def print_result(results):
    print("IP\t\t\t\t\tMac Add\n====================================")
    for x in results:
        print(x['ip'] + "\t\t" + x['mac'])


scan_results = scan("192.168.10.0/24")
print_result(scan_results)