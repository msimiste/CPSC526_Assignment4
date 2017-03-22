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
import re
import string

BUFFER_SIZE = 4096
READ = False
FILENAME = ''

def main():
    
    fileName = sys.argv[1]
    
    #count = 0
    with open(fileName) as f:
       #count = count+1
        content = [x.strip() for x in f.readlines()]
        testString =  "$adsfasdf #"
        #test = re.search(r'[#]',testString)
        #print(content)
        index = 0
        for x in content:
            if(re.search(r'[#]',x) is not None):
                content[index] = x.replace(' ',"")
                print(x)
            #else:
                #content[index] = x.replace(' ',"")
                #print("none" + x)
            index = index + 1
        #print(re.search(r'[^#]',x)) for x in content 
        rules = [x.split() for x in content]
        count = 0
        for r in rules:
            count = count + 1
            print(r)
    ports = [0] * 65535
    #print (subNetProof('136.159.1.0','136.159.1.1/32'))
   
    
def subNetProof(ip, nw):
    return ipaddress.ip_address(ip) in ipaddress.ip_network(nw)
    
def stdinProof():
    for line in sys.stdin:
        print(line.split())

if __name__ == '__main__':
    main()
