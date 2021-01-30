import base64
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
import re

dns_packets = rdpcap('flag.pcapng')
encoded_message = ""
for packet in dns_packets:
    if packet.haslayer(DNS):
        encoded_message += bytes(packet[DNS].payload).decode("utf-8")

decoded = base64.b64decode(encoded_message + '===').decode('ascii')
test = re.findall("19C4{\w+}", decoded)
print(test)
