#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for user input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Banner print with info on target host
print "*" * 50
print "One moment... scanning specified host", remoteServerIP
print "*" * 50

# DT Scan Start
DT1 = datetime.now()

# default scan all ports from 1 to 1024

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:  Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
DT2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = DT2 - DT1

# Printing the information to screen
print 'Scanning Completed in: ', total
