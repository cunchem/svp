import sys
import re
# Note -- data attributes indexes are for the following
#  0 - age
#  1 - workclass
#  2 - fnlwgt
#  3 - education
#  4 - education-num
#  5 - marital-status
#  6 - occupation
#  7 - relationship
#  8 - race
#  9 - sex
# 10 - capital-gain
# 11 - capital-loss
# 12 - hours-per-week
# 13 - native-country
# 14 - salary (>50K, <=50K)

continent = {"United-States" : "AM", "Cambodia" : "AS", "England" : "EU", "Puerto-Rico" : "AM", "Canada" : "AM", "Germany" : "EU", "Outlying-US(Guam-USVI-etc)":"AM", "India":"AS", "Japan":"AS", "Greece" : "EU", "South":"AM", "China":"AS", "Cuba":"AM", "Iran":"AS", "Honduras":"AM", "Philippines":"OC", "Italy":"EU", "Poland":"EU", "Jamaica":"AM", "Vietnam":"AS", "Mexico":"AM", "Portugal":"EU", "Ireland":"EU", "France":"EU", "Dominican-Republic":"AM", "Laos":"AS", "Ecuador":"AM", "Taiwan":"AS", "Haiti":"AM", "Columbia":"AM", "Hungary":"EU", "Guatemala":"AM", "Nicaragua":"AM", "Scotland":"EU", "Thailand":"AS", "Yugoslavia":"EU", "El-Salvador":"AM", "Trinadad&Tobago":"AM", "Peru":"AM", "Hong":"AS", "Holand-Netherlands":"EU","?":"?"}

def generalize_age(a):
    b = a
    ### TODO    

    #print "generalizing age: %d -> %s" % (a,b)
    return b

def generalize_country(c):
    d=c
    ### TODO	 

    #print "generalizing country: %s -> %s" % (c,d)

    return d
    

infile =  str(sys.argv[1])
print ("Input file name: %s" % infile)
outfile = re.sub("\.","_generalized.",infile)
print ("Output file name: %s" % infile)

out = open(outfile,'w')




for l in open(infile, "r").readlines():
    r_ = l.replace('\r', '').replace('\n', '').replace(', ', ',').split(',')
    if len(r_) < 15:
        continue
        
    r = [""] *  len(r_)
    for ix, a in enumerate(r_):
        
        if(ix==0): # age
            r[ix] = generalize_age(a)
        elif(ix==13): # country
            r[ix] = generalize_country(a)
        else:
            r[ix]  =a # other
            
            
            
    #print r
    #out.write(["%s," % item  for item in r])
    out.write(",".join(r))
    out.write("\n")
print "done!"






