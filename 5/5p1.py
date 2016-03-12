from sys import argv

filename = argv[1]

f = open(filename)

lines = f.readlines()

def vovelcheck( str ):
	vovels = {"a","e","i","o","u"}
	vovelcount = 0
	for i in range (0 , len(str)):
		if (str[i] in vovels):
			vovelcount = vovelcount + 1
	return vovelcount>=3

def dupecheck(str):
	for i in range (0 , len(str)-1):
		if (str[i] == str[i+1]):
			return True
	return False

def badcombocheck(str):
	badcombos = {"ab", "cd", "pq", "xy"}
	for i in range (0 , len(str)-1):
		if (str[i:i+2] in badcombos):
			return False
	return True

nice = 0

for line in lines:
	line = line.strip()
	#print line + " : " + str(vovelcheck(line)) + " - " + str(dupecheck(line)) + " - " + str(badcombocheck(line))
	if (vovelcheck(line) & dupecheck(line) & badcombocheck(line)):
		nice = nice + 1 

print "nice strings : " + str(nice)