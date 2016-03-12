from sys import argv

filename = argv[1]

input = open(filename)

def isnumber(str):
	if str == "-":
		return True
	try:
		int(str)
		return True
	except ValueError:
		return False

try:
	su = 0
	count = 0 
	while True:
		char = input.read(1)
		if char == "":
			break
		numstr = "";
		while isnumber(char):
			numstr = numstr + char
			char = input.read(1)
		if len(numstr) > 0:
			print numstr
			count = count + 1
			su = su + int(numstr)

	print su
	print count 

finally:
	input.close()
