from sys import argv

filename = argv[1]

f = open(filename)

lines = f.readlines()

totalPaper = 0

def getSlack(l,w,h):
	big = max(l,w,h)
	if l == big:
		return w*h
	if w == big:
		return l*h
	return l*w


for line in lines:
	line = line.strip()
	values = line.split("x")
	#print values 
	l = int(values[0])
	w = int(values[1])
	h = int(values[2])

	#print getSlack(l,w,h)

	totalPaper = totalPaper + 2*l*w + 2*w*h + 2*h*l + getSlack(l,w,h)

print totalPaper
	#print values[2].



def getBiggest(values):
	ret = 0
	if values[1]>values[0]:
		ret = 1
	if values[2]>values[0]:
		ret = 2
		if values[1]>values[2]:
			ret = 1




'''
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
'''