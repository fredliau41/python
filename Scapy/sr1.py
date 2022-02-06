from scapy.all import *

x = sr1(IP(dst="192.168.10.1")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.slashdot.org")))
