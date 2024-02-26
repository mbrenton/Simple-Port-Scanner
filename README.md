# Simple-Port-Scanner
A simple port scanner based off nmap

How to run:

Windows: python3 .\sps.py 127.0.0.1
Linux: ./sps.py 127.0.0.1

Command line utility tool with multiple optional arguments.

    usage: python3 sys.py [-h] [-u] [-pA] [-pR  PORTRANGE] IP     

    positional arguments:
    IP                    IP address to port scan

    options:
    -h, --help            show this help message and exit       
    -u, --udp             Chances a TCP Scan to a UDP Scan      
    -pA, --portAll        Scan all ports on TCP or UDP range    
    -pR  PORTRANGE, --portRange PORTRANGE
                            Specify specific ports, or port ranges

Initially pings the host with ping to make sure it is up. Had a 
problem with UDP still trying if host was down so this fixes that.
Has TCP and UDP Scanning with multiple arguments. Does Top 1000 UDP
and TCP ports by default with no arguments besides IP. 

-u for UDP scanning, default is TCP

-pA is for all ports on port range. 

-pR is to specify certain ports, either range, or specific
    ex. -pR 22,88,443
    ex. -pR 5000-10000

Can combine arguments for UDP scanning
    ex. -u -pA 127.0.0.1
    ex. -u -pR 1-100 127.0.0.1
