#Simple port scanner, based on nmap commands
#By mbrenton, base code based on Fault's "DIY Python PORT SCANNER | LIKE NMAP" YouTube Video.
#https://www.youtube.com/watch?v=XGFDXGyd7Uw

import pyfiglet
import sys
import socket
from datetime import datetime
import socket, threading

def tcp_scan(ip, port, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port))
        output[port] = 'Listening'
    except:
        output[port] = ''

    '''
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
    '''
    
    
def scan_ports(ip):

    #For multithreading
    threads = []
    output = {}
    delay = 0.5

    # Spawning threads to scan ports
    for i in range(65535):
        t = threading.Thread(target=tcp_scan, args=(ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(65535):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(65535):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(65535):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])

def main():
    ascii_banner = pyfiglet.figlet_format("Simple Port Scanner")
    print(ascii_banner)

    ip = input(str("Target IP:"))

    #Banner
    print("_" * 54)
    print("Scanning Target: " + ip)
    print("Scanning started at: " + str(datetime.now()))
    print("_" * 54)

    #Scan IP
    scan_ports(ip)

if __name__ == "__main__":
    main()
