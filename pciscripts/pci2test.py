#!/usr/bin/env python

import os

hlist = 'hostlist.txt'

with open(hlist) as f:
        for line in f:
            os.system('nmap -sV -O -p 1-2024 --resolve-all --script ssh2-enum-algos,ssl-enum-ciphers,address-info,banner,docker-version,duplicates,enip-info,finger,rdp-enum-encryption,rdp-ntlm-info,ssl-cert,sslv2 '+line)
            print('------------------------------------------------------------------')
            print(' ')
            #print line

