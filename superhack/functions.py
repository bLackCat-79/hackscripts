#!/usr/bin/env python 

import nmap
import xml.etree.ElementTree as ET
import subprocess
import time
import os
#http://xael.org/pages/python-nmap-en.html
import nmap

port = ' -p-'

#This function checks if a given ip adress is a valid ip adress.
def ip_checkv4(ip):
        parts=ip.split(".")
        if len(parts)<4 or len(parts)>4:
            return "invalid IP length should be 4 not greater or less than 4"
        else:
            while len(parts)== 4:
                a=int(parts[0])
                b=int(parts[1])
                c=int(parts[2])
                d=int(parts[3])
                if a<= 0 or a == 127 :
                    return "invalid IP address"
                elif d == 0:
                    return "host id  should not be 0 or less than zero " 
                elif a>=255:
                    return "should not be 255 or greater than 255 or less than 0 A"
                elif b>=255 or b<0: 
                    return "should not be 255 or greater than 255 or less than 0 B"
                elif c>=255 or c<0:
                    return "should not be 255 or greater than 255 or less than 0 C"
                elif d>=255 or c<0:
                    return "should not be 255 or greater than 255 or less than 0 D"
                else:
                    return "Valid IP address ", ip


#This function can search for words
def find_words(text, search):
    """Find exact words"""
    dText   = text.split()
    dSearch = search.split()

    found_word = 0

    for text_word in dText:
        for search_word in dSearch:
            if search_word == text_word:
                found_word += 1

    if found_word == len(dSearch):
        return len(dSearch)
    else:
        return False
#This function is an nmap function
def nmapScan(host, port):
	nm = nmap.PortScanner()
	nm.scan(host,port)
	state = nm[host]['tcp'][int(port)]['state']
	print (host+ " tcp/"+port+" "+state )
