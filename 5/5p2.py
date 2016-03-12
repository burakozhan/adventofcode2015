from sys import argv

filename = argv[1]

f = open(filename)

lines = f.readlines()

def doublepaircheck(str):
	end = len(str)-1
	for i in range (0, end):
		ref = str[i:i+2]
		for j in range (i+2, end):
			if ref == str[j:j+2]:
				return True
	return False

def lettercheck(str):
	for i in range (0 , len(str)-2):
		if (str[i] == str[i+2]):
			return True
	return False

nice = 0

for line in lines:
	line = line.strip()
	if (doublepaircheck(line) & lettercheck(line)):
		print line + " : " + str(doublepaircheck(line))
		nice = nice + 1 

print "nice strings : " + str(nice)