from sys import argv

filename = argv[1]

input = open(filename)

up = 0
down = 0
currentFloor = 0
counter = 0

try:
	step = input.read(1)
	counter = counter +1
	while step != "":
		if step == "(":
			up = up + 1
			currentFloor = currentFloor +1
		if step == ")":
			down = down + 1
			currentFloor = currentFloor -1
		if currentFloor == -1:
			print "entering basement at : "+ str(counter)
		step = input.read(1)
		counter = counter +1 

finally:
	input.close()

print "up : "+str(up)
print "down : "+str(down)
print "current : "+str(up-down)