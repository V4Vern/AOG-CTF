from scapy.all import *
from base64 import b64encode
import re
from time import sleep
from multiprocessing import Process
import sys


def generate_dns_flag(text):
    packet = IP(dst='1.0.1.0') / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname='www.facebook.com')) / text
    send(packet, verbose=0)


def generate_ping_noise():
    while True:
        packet = IP(dst="8.8.8.8") / ICMP()
        send(packet)
        sleep(0.5)


def generate_http_noise():
    while True:
        packet = IP(dst="192.168.75.128") / TCP() / "GET /flag.txt HTTP/1.0 \n\n"
        send(packet)
        sleep(3)


def main():
    with open("text.txt", "r") as file:
        text = file.read().encode("UTF-8")
        file.close()
    chunks = re.findall("." * 50, b64encode(text).decode("UTF-8"))
    p1 = Process(target=generate_http_noise)
    p1.start()
    p2 = Process(target=generate_ping_noise)
    p2.start()
    for i in range(len(chunks)):
        generate_dns_flag(chunks[i])
        time.sleep(0.3)
    p1.terminate()
    p2.terminate()
    sys.exit()


if __name__ == "__main__":
    main()
