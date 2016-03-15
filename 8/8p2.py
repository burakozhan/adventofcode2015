from sys import argv

file = open(argv[1])

lines = file.readlines()

sum = int(0)

def escape(s):
	s = s.replace("\\","\\\\")
	s = s.replace("\"","\\\"")
	s = "\""+s+"\""
	return s

for line in lines:
	line = line.strip()
	#print str(len(escape(line))) + "  " + str(len(line))
	sum += (len(escape(line)) - len(line))

print str(sum)
