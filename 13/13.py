from sys import argv
import itertools
import time

file = open(argv[1])

lines = file.readlines()

people = set()
happiness = { }

for line in lines:
	line = line.strip()
	sta, _, sign, units, _, _, _, _, _, _, des = line.split()
	des = des[0:-1]
	people.add(sta)
	people.add(des)
	if (sign =="lose"):
		units = "-"+units
	happiness[sta+"-"+des] = int(units)

peoplelist = list(people) #have a sorted indexable version of all persons

lowest = 100000
highest = 0

biglist = list(itertools.permutations(peoplelist))
size = len(biglist)
count = 0

start = time.time()

print "Found "+str(count)+ " possible seating arrangements."

for order in biglist:
	count += 1
	if count % 10000 == 0:
		print "Tried "+str(count)+ " of " + str(size) + " possible seating arrangements."
	happyunits = 0
	tablesize = len(order)
	for i in range(1, tablesize):
		happyunits += happiness[order[i-1]+"-"+order[i]] 
		happyunits += happiness[order[i]+"-"+order[i-1]] # Add both directions of happiness
	happyunits += happiness[order[0]+"-"+order[tablesize-1]] # Also add end and start of table
	happyunits += happiness[order[tablesize-1]+"-"+order[0]] # in both directions
	#print str(order)+" : "+ str(happyunits) #Printing everything is pretty slow.
	if happyunits < lowest:
		lowest = happyunits
	if happyunits > highest:
		highest = happyunits
print "Duration : " + str(time.time()-start)
print "lowest happyunits -> " + str(lowest)
print "highest happyunits -> " + str(highest)
