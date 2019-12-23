#!/usr/bin/env python

import os
import socket

hlist = 'delijnhosts.txt'
with open(hlist) as f:
    for line in f:
        try:
            host = (line.strip()+'.addelijn.be')
            addr = socket.gethostbyname(host)
            print (host)
            print (addr)
        except:
            pass
        try:
            host1 = (host-'.addelijn.be'+'.sbbdelijn.be')
            addr1 = socket.gethostbyname(host)
            print (host1)
            print (addr1)
        except:
            pass
        try:
            host2 = (host-'addelijn.be'+'.vvm.addelijn.be')
            addr2 = socket.gethostbyname(host)
            print (host2)
            print (addr2)
        except:
            print (host+', not found')
    
