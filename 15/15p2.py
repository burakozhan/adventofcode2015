# Actually this is a typical optimization problem, iterating through every possible solution is crap.
from sys import argv
import itertools
from sys import exit

f = open(argv[1])

lines = f.readlines()

ingredients = list()

for line in lines:
	ingred = dict()
	ingred["name"], _, ingred["capacity"], _,ingred["durability"],_,ingred["flavor"],_,ingred["texture"],_,ingred["calories"] = line.split()
	ingredients.append(ingred)

#total = 100
#
#for spoons in range (0, total):
#	cap = dur = fla = tex = 0
#	for i in range (0, len(ingredients)-1):
#		ingredients[]

#for a in range(0,100):
#	print a, " ", 100-a

#print list(itertools.product(range(0,20),repeat = 4))

def weights():
	for weight in itertools.product(range(0,100), repeat=len(ingredients)):
		if sum(weight) == 100:
			yield weight #this is new, I now know about generators. (Advent of code has taught me something! YAY!)

maxscore = 0
count = 0 

for weight in weights():
	count += 1
	cap = dur = fla = tex = cal = 0
	for i in range (0,len(ingredients)):
		cal += weight[i] * int(ingredients[i]["calories"].replace(',',''))
	if cal == 500:
		for i in range (0,len(ingredients)):
			cap += weight[i] * int(ingredients[i]["capacity"].replace(',',''))
			dur += weight[i] * int(ingredients[i]["durability"].replace(',',''))
			fla += weight[i] * int(ingredients[i]["flavor"].replace(',',''))
			tex += weight[i] * int(ingredients[i]["texture"].replace(',',''))
		if cap < 0 :
			cap = 0
		if dur < 0 :
			dur = 0
		if fla < 0 :
			fla = 0
		if tex < 0 :
			tex = 0
		score = cap * dur * fla * tex
		if score > maxscore :
	#		print "replacing old maxscore " + str(maxscore) + " with " + str(score)
	#		print "for "+ str(weight[0])
	#		print cap
	#		print dur
	#		print fla
	#		print tex
	#		print score
			maxscore = score
		if count % 1000 == 0:
			print "trying recipe nr: "+ str(count)

print maxscore

		

