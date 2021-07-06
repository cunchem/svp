#!/usr/bin/python
import hashlib
# Open a file

out = open("userid_hashed.txt",'w')

for line in open("user_id.txt",'r').readlines():
    ssn=line.rstrip()
    print "current userid: %s" % ssn
    hash = hashlib.md5(ssn).hexdigest()
    print hash
    out.write(hash)
    out.write("\n")
