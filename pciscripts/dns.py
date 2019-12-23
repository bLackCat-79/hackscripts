#!/usr/bin/env python

import os
import socket

hlist = 'delijnhosts.txt'
with open(hlist) as f:
    for line in f:
        host = (line.strip())
        try:
            host1 = (host+'.be')
            addr1 = socket.gethostbyname(host1)
            print (host1)
            print (addr)
        except:
            pass
        try:
            host2 = (host+'.net')
            addr2 = socket.gethostbyname(host2)
            print (host2)
            print (addr2)
        except:
            pass
        try:
            host3 = (host+'.com')
            addr3 = socket.gethostbyname(host3)
            print (host3)
            print (addr3)
        except:
            print (host+', not found')
    
