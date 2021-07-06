#!/usr/bin/python
import hashlib
# Open a file

def synthetizessn(sex,year,month,dept,city,order):
    ssn= str(sex).zfill(1)+str(year).zfill(2)+str(month).zfill(2)+str(dept).zfill(2)+str(city).zfill(3)+str(order).zfill(3)
    key = 97 - (int(ssn) % 97) 
    ssn = ssn+str(key).zfill(2)
    return ssn


def reversehash(hash):

                            


for line in open("SSN_hashed.txt",'r').readlines():
    hash=line.rstrip()
    print "current hash: %s" % hash
    reversehash(hash)
    
