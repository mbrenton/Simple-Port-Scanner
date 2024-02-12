#Simple port scanner, based on nmap commands
#By mbrenton, base code based on Fault's "DIY Python PORT SCANNER | LIKE NMAP" YouTube Video.
#https://www.youtube.com/watch?v=XGFDXGyd7Uw

import pyfiglet
import argparse
import sys
import socket
from datetime import datetime
import socket, threading

def scan_ports(ip):

    #Detecting all open ports on the server
    try:

        #Scan every port in the target IP range
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            #Return open ports
            result = s.connect_ex((ip,port))
            if result == 0:
                print("[*] Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()

    except socket.error:
        print("\ Host is not responding :(")
        sys.exit()

def main():
    #Parsing
    parser = argparse.ArgumentParser("python3 sys.py")
    parser.add_argument("IP", help="IP address to port scan", type=str)
    parser.add_argument("-u", "--udp", action="store_true", help="Chances a TCP Scan to a UDP Scan")
    parser.add_argument("-pA", "--portAll", action="store_true", help="Scan all ports on TCP or UDP range")
    #parser.add_argument("-p ", "--port", help="Specify specific ports, or port ranges", type=str)
    args = parser.parse_args()
    IP = args.IP

    #parser.add_argument('')
    print(args)



    ascii_banner = pyfiglet.figlet_format("Simple Port Scanner")
    print(ascii_banner)

    #Default port for testing is 127.0.0.1
    #ip = input(str("Target IP:"))
    #ip = "127.0.0.1"

    #Banner
    print("_" * 54)
    print("Scanning Target: " + IP)
    print("Scanning started at: " + str(datetime.now()))
    print("_" * 54)

    #Scan IP
    scan_ports(IP)

if __name__ == "__main__":
    main()
