import pickle
import os
import urllib2
import sys
import re



def get_nb_attrib(filename):
        f = open(filename,'r')
        line = f.readline()
        n = len(line.split(','))
        return n


infile =  str(sys.argv[1])
print ("Input file name: %s" % infile)


if not os.path.exists(infile):
	print "error: file does not exist: %s" % infile
        

# Dataset init
attrib_dict = {}

nb_attrib = get_nb_attrib(infile)

for ix in range(nb_attrib):
	attrib_dict[ix] = []
records = []

# Caching
print "caching data...",
for l in open(infile, "r").readlines():
	r_ = l.replace('\r', '').replace('\n', '').replace(', ', ',').split(',')

	if len(r_) < 15:
		continue

	r = []
	for ix, a in enumerate(r_):
		try:
			a_ix = attrib_dict[ix].index(a)
		except ValueError:
			a_ix = len(attrib_dict[ix])
			attrib_dict[ix].append(a)
		r.append(a_ix)
	records.append(r)
print "done!"

print "num records:", len(records)

# Writing to disk
outfile = re.sub("\.[a-zA-Z]*",".p",infile)
outdict = "attrib_dict_" + outfile 
print "writing cahce...",
pickle.dump(records, open(outfile, "w+"))
pickle.dump(attrib_dict, open(outdict, "w+"))
print "done!"
