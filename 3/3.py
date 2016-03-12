from sys import argv

filename = argv[1]

input = open(filename)

x = 0
y = 0
houses = set()
houses.add(str(x)+str(y))

try:
	step = input.read(1)
	while step != "":
		if step == ">":
			x = x + 1
		if step == "<":
			x = x - 1
		if step == "^":
			y = y + 1
		if step == "v":
			y = y - 1
		step = input.read(1)
		#print str(x)+str(y)
		houses.add(str(x)+str(y))

finally:
	input.close()

print len (houses)