from sys import argv

filename = argv[1]

input = open(filename)

santa_x = 0
santa_y = 0
robosanta_x = 0
robosanta_y = 0

houses = set()
houses.add(str(santa_x)+str(santa_y))

try:
	step = input.read(1)
	while step != "":
		if step == ">":
			santa_x = santa_x + 1
		if step == "<":
			santa_x = santa_x - 1
		if step == "^":
			santa_y = santa_y + 1
		if step == "v":
			santa_y = santa_y - 1
		houses.add(str(santa_x)+str(santa_y))
		#print "santa" + str(santa_x)+str(santa_y)
		step = input.read(1)
		if step != "":
			if step == ">":
				robosanta_x = robosanta_x + 1
			if step == "<":
				robosanta_x = robosanta_x - 1
			if step == "^":
				robosanta_y = robosanta_y + 1
			if step == "v":
				robosanta_y = robosanta_y - 1
			houses.add(str(robosanta_x)+str(robosanta_y))
			#print "robosanta" + str(robosanta_x)+str(robosanta_y)
			step = input.read(1)

finally:
	input.close()

print houses
print len (houses)