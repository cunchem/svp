#!/usr/bin/python
import hashlib
# Open a file



def reversehash(hash):

                            


for line in open("userid_hashed.txt",'r').readlines():
    hash=line.rstrip()
    print "current hash: %s" % hash
    reversehash(hash)
    
