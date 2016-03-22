from sys import argv
import sys

# Trying to get the recursive approach to run somehow
#sys.setrecursionlimit(100000000)

dat = argv[1]
repeat = int(argv[2])

### Recursive approach, running out of speed pretty fast
def rep (d):
	ref = d[0]
	if (len(d) ==1):
		return str(1)+ref
	#print "ref= "+ref
	for i in range(1,len(d)):
		#print "looking in "+str(i)
		if d[i] != ref:
			rest = d[i:]
			#print "recurse with " + rest
			if len(rest) == 0 :
				return str(i)+ref
			return str(i)+ref+str(rep(rest))
		if i == len(d)-1:
			return str(i+1)+ref

#linear approach 
def getIteration(d):
	ret = ""
	count = 1 
	for i in range (0,len(d)-1):
		if d[i] == d[i+1]:
			count += 1
		else :
			ret += str(count)+d[i]
			count = 1
	ret += str(count)+d[-1]
	return ret


for i in range (0, repeat):
	dat = getIteration(dat)
	print "data : " + dat
	print "repeat : "+str(i)

print len(dat)
