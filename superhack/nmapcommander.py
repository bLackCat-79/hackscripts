#!/usr/bin/env python 

#Import libraries
import os
import sys
import nmap
import ipaddress
import platform
import re
from functions import ip_checkv4
from functions import find_words

nm = nmap.PortScanner()
nm.scan('192.168.1.254 ', '20-1024')
print(nm.command_line())

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : {} ({})'.format(host, nm[host].hostname()))
    print('State : {}'.format(nm[host].state()))
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {}'.format(proto))
 
        lport = nm[host][proto].keys()
        for port in lport:
            print ('port : {}\tstate : {}'.format(port, nm[host][proto][port]['state']))