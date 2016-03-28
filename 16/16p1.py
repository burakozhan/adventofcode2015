from sys import argv

f1 = open(argv[1])
f2 = open(argv[2])

sueList = f1.readlines()
MFCSAM = f2.readlines()

wanted = dict()

for line in MFCSAM:
	k,v = line.split()
	wanted[k[:-1]] = v

def compareKV(k,v):
	return wanted[k] == v

for line in sueList:
	_, num, k1, v1, k2, v2, k3, v3 = line.split()
	if compareKV(k1[:-1],v1[:-1]):
		if compareKV(k2[:-1],v2[:-1]):
			if compareKV(k3[:-1],v3):
				print num[:-1]
				break

