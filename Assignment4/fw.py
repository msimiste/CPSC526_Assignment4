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

def main():
    fileName = sys.argv[1]
    
    with open(fileName) as f:
        content = [x.strip() for x in f.readlines()]
        rules = [x.split() for x in content]
    out = map(lambda x: x[3].split(','), rules)
        
    for x in rules:
        x[3] = x[3].split(',')
    print(rules)
if __name__ == '__main__':
    main()
