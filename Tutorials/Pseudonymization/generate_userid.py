#!/usr/bin/python
from random import randint


# Open a file
file = open("user_id.txt", 'w')
n=1000


# Prints out 3,4,5
for x in xrange(1,n): # or range(3, 6)
    id=str(randint(0,99999)).zfill(5)
    file.write(id)
    file.write("\n")
    

file.close()
