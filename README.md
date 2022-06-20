# Sniffpy
Captura rede wi-fi que está  ao redor

# Modo de instalação no linux
Use o terminal para fazer as instalações

* `git clone https://github.com/Pemakerin/Sniffpy.git`
* `cd Sniddpy`
* `pip3 install scapy`


# Coloque sua rede em modo monitoramento
Use o aircrack-ng no terminal

* `airmon-ng start wlan0`
* `python3 sniff.py wlan0mon`
