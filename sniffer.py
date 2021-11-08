from scapy.all import *
import time



def asyncSniff():
    print ("Sniffing packets on interface eth0...")
    t = AsyncSniffer(iface='eth0', count= 200)
    t.start()
    t.join()
    wrpcap('cap.pcap', t.results)
    print ("Generated a capture file.")

def visualizeResults():
    userInput = input("Put results up on wireshark? (Y/N): ")
    if ((userInput == 'Y') or  (userInput == 'y')):
        print ("I will present it on wireshark shortly...")
        time.sleep(5)
        wireshark('cap.pcap')
    else:
        print("Exiting...")
        exit(0)

    
if __name__ == "__main__":   
    asyncSniff()
    visualizeResults()