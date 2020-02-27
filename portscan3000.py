#!/usr/bin/env python3
#
import socket
import subprocess
import sys
import time
from datetime import datetime

#Welcome
print("-" * 50)
print("Python Port Scanner 3000")
print("A project by The Mayor/Dievus")
print("-" * 50)
time.sleep(1)
#Input
remoteServer = input("Enter your target IP address here: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Clear the screen
subprocess.call('clear', shell=True)
    
#Banner
print("-" * 50)
print("Scanning target "+remoteServerIP)
print("Time started: "+str(datetime.now()))
print("-" * 50)
t1 = datetime.now()
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((remoteServerIP,port)) #returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()    

t2 = datetime.now()
#Time total
total = t2 - t1
print("Port scan completed in "+str(total))
print("Press any button to continue...")
input()
