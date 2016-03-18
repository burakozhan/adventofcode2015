from sys import argv
import itertools

file = open(argv[1])

lines = file.readlines()

cities = set()
distances = { }

for line in lines:
	line = line.strip()
	sta , _, des, _, dist = line.split()
	cities.add(sta)
	cities.add(des)
	distances[sta+"-"+des] = int(dist)
	distances[des+"-"+sta] = int(dist) # risk unused entries

citylist = list(cities) #have a sorted indexable version of all cities

shortest = 100000
longest = 0

for order in list(itertools.permutations(citylist)):
	distance = 0
	for i in range(1, len(order)):
		distance += distances[order[i-1]+"-"+order[i]]
	print str(order)+" : "+ str(distance)
	if distance < shortest:
		print "override shortest "+str(shortest)+" with "+str(distance)
		shortest = distance
	if distance > longest:
		longest = distance
print "shortest distance -> " + str(shortest)
print "longest distance -> " + str(longest)
