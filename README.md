# SimplePacketSniffer

This is a simple network packet sniffer. It captures network traffic from an interface using Scapy and generates a .pcap file. It can also visualize the captured pcap onto Wireshark.

Tested and working on:
- Scapy 2.4.4
- Python 3.9.2
- Parrot OS 5.0
- Wireshark 3.4.4

Requires root privilege to run.

To execute: 
* clone the repo
* cd into it
* run "python3 sniffer.py" (w/o quotes)


Notes:
By default the script is told to capture 200 packets, but you can edit it to your needs.
Also by default the script uses interface eth0. You may also edit the "iface" argument value on line to whatever interface name you need. To find other interfaces on your linux box, run "ip addr" in terminal and a list of all interfaces will be presented to you. For example, if you want to capture wifi traffic from a wifi card, you can replace the value "eth0" to "wlan0".
