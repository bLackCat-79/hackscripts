#!/usr/bin/env python
import sys
import os

import nmap                         
try:
    nm = nmap.PortScanner()         
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)


hlist = 'hostlist.txt'

nm = nmap.PortScanner()

with open(hlist) as f:
    for line in f:
        nm.scan(line, '-', arguments='-O')
        print(nm.command_line())
        nm.scaninfo()          
        for host in nm.all_hosts():     
            nm[host].hostname()        
            nm[host].state()           
            nm[host].all_protocols()  
            if ('tcp' in nm[host]):
                list(nm[host]['tcp'].keys()) # get all ports for tcp protocol

                nm[host].all_tcp()           # get all ports for tcp protocol (sorted version)
                nm[host].all_udp()           # get all ports for udp protocol (sorted version)
                nm[host].all_ip()            # get all ports for ip protocol (sorted version)
                nm[host].all_sctp()          # get all ports for sctp protocol (sorted version)
                if nm[host].has_tcp(22):     # is there any information for port 22/tcp on host 127.0.0.1
                    nm[host]['tcp'][22]          # get infos about port 22 in tcp on host 127.0.0.1
                    nm[host].tcp(22)             # get infos about port 22 in tcp on host 127.0.0.1
                    nm[host]['tcp'][22]['state'] # get state of port 22/tcp on host 127.0.0.1 (open


# a more usefull example :
                for host in nm.all_hosts():
                    print('----------------------------------------------------')
                    print('host : %s (%s)' % (host, nm[host].hostname()))
                    print('State : %s' % nm[host].state())
    
                    for proto in nm[host].all_protocols():
                        print('----------')
                        print('Protocol : %s' % proto)

                        lport = nm[host][proto].keys()
                        lport.sort()
                        for port in lport:
                               print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


                print('----------------------------------------------------')
# Asynchronous usage of PortScannerAsync


                nma = nmap.PortScannerAsync()

                def callback_result(host, scan_result):
                    print('------------------')
                    print(host, scan_result)


                while nma.still_scanning():
                    print("Waiting ...")
                    nma.wait(2)   # you can do whatever you want but I choose to wait after the end of the scan

                if (os.getuid() == 0):
                    print('----------------------------------------------------')
        # Os detection (need root privileges)
                    nm.scan(host, arguments="-O")
                    if nm[host].has_key('osclass'):
                        for osclass in nm[host]['osclass']:
                            print('OsClass.type : {0}'.format(osclass['type']))
                            print('OsClass.vendor : {0}'.format(osclass['vendor']))
                            print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                            print('OsClass.osgen : {0}'.format(osclass['osgen']))
                            print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
                            print('')

                    if nm[host].has_key('osmatch'):
                        for osmatch in nm[host]['osmatch']:
                            print('osmatch.name : {0}'.format(osmatch['name']))
                            print('osmatch.accuracy : {0}'.format(osmatch['accuracy']))
                            print('osmatch.line : {0}'.format(osmatch['line']))
                            print('')

                    if nm[host].has_key('fingerprint'):
                        print('Fingerprint : {0}'.format(nm[host]['fingerprint']))
    #for line in f:
        os.system('nmap -sV -O -P0 -p- --resolve-all --script ssh2-enum-algos,ssl-enum-ciphers,address-info,banner,docker-version,duplicates,enip-info,finger,rdp-enum-encryption,rdp-ntlm-info,ssl-cert,sslv2 '+line)
        print('------------------------------------------------------------------')
        print(' ')

