#!/usr/bin/python           # This is client.py file

#Name: Mike Simister
#StudentID: 10095107
#Tutorial Section: T02


import sys  
import string
import os
import ipaddress
import re

class firewall(object):
    def __init__(self, rules):
        self.rules = rules
        
def main():
    fileName = sys.argv[1]    
    fw = firewall(getRules(fileName))    
    parsePackets(fw)    

def getRules(fileName):
    with open(fileName) as f:
        content = [x.strip() for x in f.readlines()]
        index = 0
        for x in content:
            if(re.search(r'[#]',x) is not None):
                 content[index] = x.replace(' ',"")
            index = index + 1
        rules = [x.split() for x in content]
    for x in rules:
        if(len(x) > 3):
            x[3] = x[3].split(',')
    
    return rules

def parsePackets(fWall):
    for line in sys.stdin:
        accept = False
        packet = line.split()
        index = 0
        for r in fWall.rules:
            index = index + 1
            accept = comparePacketToRule(packet,r)
            if(accept):
                print('{}({}) {} {} {} {}'.format(r[1], index,packet[0],packet[1],packet[2],packet[3]))   
                break
        else:
            print("drop() {} {} {} {}".format(packet[0], packet[1], packet[2],packet[3]))       

def comparePacketToRule(packet, rule):
    if(len(rule) <= 1):
        return False
    valid = False        
    valid = (packet[0] == rule[0]) 
    valid = ((rule[2] == '*') or (ipaddress.ip_address(packet[1]) in ipaddress.ip_network(rule[2],False))) and valid   
    valid = ((packet[2] in rule[3]) or (rule[3][0] == '*')) and valid    
    if(len(rule) == 5):
        valid = (packet[3] == str(1)) and valid     
    return valid
            
         
if __name__ == '__main__':
    main()
