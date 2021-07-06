#!/usr/bin/python
from random import randint

dorder=2


def randssn():
    sex = str(randint(1,2)).zfill(1)
    year = str(randint(0,99)).zfill(2)
    month = str(randint(1,12)).zfill(2)
    #dept = str(randint(0,99)).zfill(2)
    dept= str(69)
    city = str(randint(1,9)).zfill(3)
    order = str(randint(1,(10**dorder)-1)).zfill(3)
    ssn = sex+year+month+dept+city+order
    key = 97 - (int(ssn) % 97) 
    ssn = ssn+str(key).zfill(2)
    print order
    return ssn



# Open a file
file = open("SSN.txt", 'w')
n=1000


# Prints out 3,4,5
for x in xrange(1,n): # or range(3, 6)
    ssn=randssn()
    file.write(str(ssn))
    file.write("\n")
    

file.close()
