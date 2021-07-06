#!/usr/bin/python
import hashlib
# Open a file

out = open("SSN_hashed.txt",'w')

for line in open("SSN.txt",'r').readlines():
    ssn=line.rstrip()
    print "current ssn: %s" % ssn
    hash = hashlib.md5(ssn).hexdigest()
    print hash
    out.write(hash)
    out.write("\n")
