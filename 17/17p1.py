from sys import argv
import itertools

file = open(argv[1])

lines = file.readlines()

containers = list()

for line in lines:
	containers += [int(line)]

containerslist = list(containers)

def sizes(target, l):
	for size in itertools.combinations(containerslist, l):
		if sum (size) == target :	
			yield size

countcontainers = 0 

for l in range(len(containerslist)+1):
	for size in sizes(int(argv[2]),l):
		print str(size)
		countcontainers += 1

print "Combinations of containers " + str(countcontainers)