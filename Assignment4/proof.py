#!/usr/bin/python           # This is client.py file

#Name: Mike Simister
#StudentID: 10095107
#Tutorial Section: T02


import socket
import sys  
import time
import random
import string
import os
import hashlib
import hmac
import ipaddress

BUFFER_SIZE = 4096
READ = False
FILENAME = ''

def main():
    
    fileName = sys.argv[1]
    one = 1
    zero = 0
    
    with open(fileName) as f:
        content = [x.strip() for x in f.readlines()]
        rules = [x.split() for x in content]
    ports = [0] * 65535
    print (subNetProof('136.159.1.0','136.159.1.1/32'))
    if(one):
        print(one)
    if(not zero):
        print(zero)
    print(rules)
    
def subNetProof(ip, nw):
    return ipaddress.ip_address(ip) in ipaddress.ip_network(nw)

if __name__ == '__main__':
    main()
