from scapy.all import *

# sniff(count=1, prn = lambda a: a.summary())
pkts = sniff(count = 1, prn=lambda x:x.sprintf(
  "%.time% %-15s,IP.src% -> %-15s,IP.dst% %IP.chksum% "
  "%03xr,IP.proto% %r,TCP.flags%"
))
#search API in documentation