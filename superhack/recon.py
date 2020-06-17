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
import subprocess


Yes = ['y', 'Y', 'yes', 'Yes', 'YES']
No = ['n', 'N', 'no', 'No', 'NO']
print ('\r\n\r\n------------------------------------------------------')
# Check if the OS is supported
print ("Checking OS and if python is installed: \n")
os = (os.name+', '+platform.system()+', '+platform.release()) 
os1 = str(os)
if "5.6.0-kali2-amd64" in os1:
    print ("Ok, this is Kali Rolling with the 5.6.0 kernel, your OS is supported")
else:
    print ("We never tested this os! It might get weird results!")
print ('\r\n\r\n------------------------------------------------------')


nmapv = nmap.__version__
print ("Checking if python-nmap is installed.")
if nmap.__version__ == ('0.6.1'):
 print ('The correct python-nmap is installed')
elif nmap.__version__ != ('0.6.1'):
 print ("Wrong version installed, I will update it now")
 os.system('pip3 install python-nmap') 
 print ("Now the right version is installed")
else:
    print ("Python-pip is not installed, please run apt-get install python3 python3-pip")
print ('\r\n\r\n------------------------------------------------------')
target = input ("Please enter a valild ip address (Currently only IP addresses supported): ")
valip = ip_checkv4(target)
valip1 = str(valip)

if "Valid" in valip1:
    confirm = input ("You want to nmap the host?  (Y)es / (N)o  ")
    if confirm in Yes:
        print ("Ok nmapping now")
        nm = nmap.PortScanner()
        nm.scan(target, '1-100')
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
            

        cont = input ('Nmap done, do you want to continue?  (Y)es/(N)o')
        if cont in Yes:
            print ("ok continueing")
            nm = nmap.PortScanner
            nm.scan(valip1, arguments=' -Pn -sC -sV --min-rate=1000 -T5')
            nmap.nm.get_nmap_last_output(target+'.xml')
            hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
            for host, status in hosts_list:
                print('{0}:{1}'.format(host, status))
        elif cont in No:
            print ("Ok stopping the script")
            exit()

    elif confirm in No:
        print ("Ok doing nothing")
    else:
        print ("Invalid response: Aborting,....  ")
        exit()
else:
    print ("Sorry, but if you cannot enter a valid ip, this program is nothing for you,...")
    exit()

