import scapy.all as scapy

def scan(ip):
    scapy.arping(ip, timeout = 5)

scan("192.168.10.0/24")