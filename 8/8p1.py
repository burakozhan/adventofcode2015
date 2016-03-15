from sys import argv

file = open(argv[1])

lines = file.readlines()

sum = int(0)

for line in lines:
	line = line.strip()
	sum += (len(line) - len(eval(line)))

print str(sum)
