#Simple port scanner, based on nmap commands
#By mbrenton, base code based on Fault's "DIY Python PORT SCANNER | LIKE NMAP" YouTube Video.
#https://www.youtube.com/watch?v=XGFDXGyd7Uw

import pyfiglet
import sys
import socket
from datetime import datetime
import socket, threading

ascii_banner = pyfiglet.figlet_format("Simple Port Scanner")
print(ascii_banner)

target = input(str("Target IP:"))

#Banner
print("_" * 54)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 54)

#Detecting all open ports on the server
try:

    #Scan every port in the target IP range
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open ports
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()

except socket.error:
    print("\ Host is not responding :(")
    sys.exit()


