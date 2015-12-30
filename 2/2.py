from sys import argv

filename = argv[1]

f = open(filename)

lines = f.readlines()

totalPaper = 0
totalRibbon = 0

def getSlack(l,w,h):
	big = max(l,w,h)
	if l == big:
		return w*h
	if w == big:
		return l*h
	return l*w

def getRibbon(l,w,h):
	big = max(l,w,h)
	if l == big:
		return (w+h)*2
	if w == big:
		return (l+h)*2
	return (l+w)*2

for line in lines:
	line = line.strip()
	values = line.split("x")
	#print values 
	l = int(values[0])
	w = int(values[1])
	h = int(values[2])

	#print getSlack(l,w,h)

	totalPaper = totalPaper + 2*l*w + 2*w*h + 2*h*l + getSlack(l,w,h)
	totalRibbon = totalRibbon + (l*w*h) + getRibbon(l,w,h)

print "paper : " + str(totalPaper)
print "ribbon : " + str(totalRibbon)

