from sys import argv

f = open(argv[1])

lines = f.readlines()

reindeers = list()

for line in lines:
	reindeerdata = line.split()
	reindeer = dict()
	reindeer["name"] = reindeerdata[0]
	reindeer["speed"] = int(reindeerdata[3])
	reindeer["duration"] = int(reindeerdata[6])
	reindeer["pause"] = int(reindeerdata[-2])
	reindeer["points"] = 0
	reindeer["distance"] = 0
	reindeers.append(reindeer)

#print reindeers

currentMaxDistance = 0
for i in range (0, 2503):
	for reindeer in reindeers:
		cycleduration = reindeer["duration"] + reindeer["pause"]
#		print "phase = "+str(i % cycleduration)
		if (i % cycleduration) < reindeer["duration"]:
#			print "reindeer " +reindeer["name"]+" is running "+str (i)+" cycledur : " + str (cycleduration)
			reindeer["distance"] += reindeer["speed"]
		if reindeer["distance"] > currentMaxDistance:
			currentMaxDistance = reindeer["distance"]
	for reindeer in reindeers:
		if reindeer["distance"] == currentMaxDistance:
			reindeer["points"] += 1
	currentMaxDistance = 0 

for reindeer in reindeers:
	print reindeer
