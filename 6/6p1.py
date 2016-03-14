from sys import argv
import numpy

f = open(argv[1])

lines = f.readlines()

grid = numpy.zeros((1000,1000))

def getxy(combined):
	xy = combined.split(",")
	x = int(xy[0])
	y = int(xy[1])
	return (x,y)

def ton(command):
	data = command.split()
	topleft = data[2]
	rightbottom = data[4]
	tl = getxy(topleft)
	br = getxy(rightbottom)
	global grid
	for x in range(tl[0],br[0]+1):
		for y in range(tl[1],br[1]+1):
			grid[x][y] = 1

def tog(command):
	data = command.split()
	topleft = data[1]
	rightbottom = data[3]
	tl = getxy(topleft)
	br = getxy(rightbottom)
	global grid
	for x in range(tl[0],br[0]+1):
		for y in range(tl[1],br[1]+1):
			if grid[x][y] == 0:
				grid[x][y] = 1
			else:
				grid[x][y] = 0

def tof(command):
	data = command.split()
	topleft = data[2]
	rightbottom = data[4]
	tl = getxy(topleft)
	br = getxy(rightbottom)
#	print " "+ str(tl[0]) + " "+ str(br[0])
#	print " "+ str(tl[1]) + " "+ str(br[1])
	global grid
	for x in range(tl[0],br[0]+1):
		for y in range(tl[1],br[1]+1):
			grid[x][y] = 0
#			print "turning off x = " + str(x) + " y = " + str(y)

ctr = 1

for line in lines:
	print str(ctr)+" processing: "+ line.replace("\n",".")
	ctr += 1
	if line.startswith("turn on"):
		ton(line)
	if line.startswith("toggle"):
		tog(line)
	if line.startswith("turn off"):
		tof(line)

print str(int(numpy.sum(grid)))

count = int(0)
for x in range(0,1000):
	for y in range(0,1000):
		count += grid[x][y]
		if grid[x][y] not in (0,1):
			print "grid["+str(x)+"]["+str(y)+"]:"+str(grid[x][y])

print count
