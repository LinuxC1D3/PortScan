print(r"""
                                   Created by
  _       _________ _                            _______  __    ______   ______  
 ( \      \__   __/( (    /||\     /||\     /|  (  ____ \/  \  (  __  \ / ___  \ 
 | (         ) (   |  \  ( || )   ( |( \   / )  | (    \/\/) ) | (  \  )\/   \  \
 | |         | |   |   \ | || |   | | \ (_) /   | |        | | | |   ) |   ___) / 
 | |         | |   | (\ \) || |   | |  ) _ (    | |        | | | |   | |  (___ (  
 | |         | |   | | \   || |   | | / ( ) \   | |        | | | |   ) |      ) \ 
 | (____/\___) (___| )  \  || (___) |( /   \ )  | (____/\__) (_| (__/  )/\___/  / 
 (_______/\_______/|/    )_)(_______)|/     \|  (_______/\____/(______/ \______/ 
""")

import scapy.all as scapy
import time
import os

# Funktion für den aggressiven SYN-FIN-RST-Scan
def aggressive_scan(host, port):
    # Erstelle ein SYN-Paket
    syn_packet = scapy.IP(dst=host) / scapy.TCP(dport=port, flags="S")  # SYN-Flag setzen
    syn_ack = scapy.sr1(syn_packet, timeout=1, verbose=False)  # Warten auf Antwort
    
    if syn_ack is None:
        # Keine Antwort = Port geschlossen
        print(f"\033[91mPort {port} ist geschlossen (keine Antwort)\033[0m")  # Rot
        return
    
    # Wenn ein SYN+ACK zurückgegeben wird, sende RST zur Beendigung
    if syn_ack.haslayer(scapy.TCP) and syn_ack.getlayer(scapy.TCP).flags == 18:  # SYN+ACK
        rst_packet = scapy.IP(dst=host) / scapy.TCP(dport=port, flags="R")  # Sende RST zur Beendigung
        scapy.send(rst_packet, verbose=False)
        print(f"\033[92mPort {port} ist offen (SYN+ACK empfangen)\033[0m")  # Grün
    
    # Prüfe nach einem RST (Port geschlossen)
    elif syn_ack.haslayer(scapy.TCP) and syn_ack.getlayer(scapy.TCP).flags == 20:  # RST-Flag
        print(f"\033[91mPort {port} ist geschlossen (RST empfangen)\033[0m")  # Rot

# Funktion, um eine Liste von Ports zu scannen
def scan_ports(host, port_range):
    for port in port_range:
        aggressive_scan(host, port)
        time.sleep(0.1)  # Kurze Pause zwischen den Scans (aggressiv, aber nicht zu schnell)

# Eingabe des Hosts und der Portbereiche
if __name__ == "__main__":
    os.system("title Linux C1D3")  # Ändere den CMD-Titel zu "Linux C1D3"
    target_host = input("Gib die IP-Adresse oder den Hostnamen ein: ")
    start_port = int(input("Gib den Startport ein: "))
    end_port = int(input("Gib den Endport ein: "))
    
    port_range = range(start_port, end_port + 1)
    scan_ports(target_host, port_range)
