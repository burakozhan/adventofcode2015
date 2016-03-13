from sys import argv
import json

data = open(argv[1]).read(-1)

datasum = 0

def pi(st):
	global datasum
	datasum += int(st)

j = json.JSONDecoder(parse_int=pi).decode(data)

print datasum
