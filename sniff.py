from scapy.all import *
from time import sleep
from random import randint
from os import system
import sys

system('clear')

num = 0

# cores do terminal
red = "\033[2;31m"    # vemelho
green = "\033[0;32m"  # verde
bank = "\033[0;37m"   # banco
yellow = "\033[0;33m" # amarelo
blue = "\033[1;34m"   # azul
green2 = "\033[2;32m" # verde destacado

print("""
{}                          {}         _________________ 
{} _____                    {}        (_________________)
{}|_   _|    ___  ___ __ _ _ __   {}    (_____________)
{}  | |_____/ __|/ __/ _` | '_ \  {}      (_________)	
{}  | |_____\__ \ (_| (_| | | | | {}        (_____)  
{}  |_|     |___/\___\__,_|_| |_| {}          (_){}
           Author: Pemakerin""".format(bank,green,blue,green2,blue,green2,blue,yellow,blue,yellow,blue,red,bank))

print("\n[{}!{}] {} Press CTRL+C to stop sniffing...{}\n".format(red,bank,red,bank))

if len(sys.argv) != 2:
    print("\nModo de Use:\n\tpython3 text_sacn.py wlan0mon")
    sys.exit(1)

print("NUM     BSSID\t\t\tESSID\t\t\t\tCHANNEL")
print(f'{"-"*3}     {"-"*63}')

# interface de rede wifi
face = str(sys.argv[1])

lbssd = [] # list que rede já fora encontrados

def cha():
    ch = randint(1,14) # canais aleatorio entre 1 e 14
    system("iwconfig {} channel {}".format(face, ch))

def call_pack(pkt):
    global num
    if pkt.haslayer(Dot11Beacon):
        bssid = pkt[Dot11].addr2 # MAC DO WIFI
        essid = pkt[Dot11Elt].info.decode('utf-8') # Nome da wifi
        if str(essid) == "":
            essid = "unknown" # wifi deconhecida
            pass
        
        chanel = int(ord(pkt[Dot11Elt:3].info))
        
        if bssid not in lbssd:
            lbssd.append(bssid)
            num += 1
            print(" {}\t{}\t{}\t\r\t\t\t\t\t\t\t\t   {}".format(num,bssid.upper(), str(essid), chanel))
            pass
    cha()

sniff(prn=call_pack, iface=face)
