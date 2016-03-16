from sys import argv
import numpy as np
import os

f = open(argv[1])

lines = f.readlines()

inputs = {}
gates = {}
tried = set()
known = {}
out = "d"

for line in lines:
	line = line.replace("\n","")

	elem = line.split()

	if (elem.index("->") == 1):
		#FIXME : this might be a direct assignment
		try:
			int(elem[0])
			inputs[elem[2]] = np.uint16(elem[0])
		except ValueError:
			gates[elem[len(elem)-1]] = line
	else:
		gates[elem[len(elem)-1]] = line


known["b"]=46065
inputs["b"]=46065

def writeknown(wanted, value):
	known[wanted]=value
	return value

def run (wanted):
	print "trying: "+ wanted
	if wanted in inputs:
		print "Found input for " + wanted
		return inputs[wanted]
	if wanted in known:
		return known[wanted]
	if wanted in tried:
		print "cyclic"
		os._exit(-1)
	else:
		tried.add(wanted)
	try:
		return writeknown(wanted,int(wanted))
	except ValueError:
		if wanted in inputs:
			return writeknown(wanted,np.uint16(inputs[wanted]))
		line = gates[wanted]
		elem = line.split()
		if (elem.index("->") == 1):
			return writeknown(wanted,run(elem[0]))
		if (elem.index("->") == 2):
			return ~ writeknown(wanted,run(elem[1]))
		if (elem.index("->") == 3):
			x = np.uint16(run(elem[0]))
			if elem[1] == "AND":
				y = np.uint16(run(elem[2]))
				return writeknown(wanted,x & y)
			if elem[1] == "OR":
				y = np.uint16(run(elem[2]))
				return writeknown(wanted,x | y)
			if elem[1] == "LSHIFT":
				y = np.uint16(elem[2])
				return writeknown(wanted,x << y)
			if elem[1] == "RSHIFT":
				y = np.uint16(elem[2])
				return writeknown(wanted,x >> y)

#print inputs
#print gates

print run ("lx")
