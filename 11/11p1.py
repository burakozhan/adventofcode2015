from sys import argv

letters = "abcdefghijklmnopqrstuvwxyz"
password = argv[1]

def vovelcheck( str ):
	vovels = {"a","e","i","o","u"}
	vovelcount = 0
	for i in range (0 , len(str)):
		if (str[i] in vovels):
			vovelcount = vovelcount + 1
	return vovelcount>=3

def dupecheck(s,d):
	if d == 0:
		return True
	for i in range (0 , len(s)-1):
		if (s[i] == s[i+1]):
			return dupecheck(s.replace(s[i]+s[i+1],"-"),d-1)
	return False

def badcombocheck(str):
	badcombos = {"ab", "cd", "pq", "xy"}
	for i in range (0 , len(str)-1):
		if (str[i:i+2] in badcombos):
			return False
	return True

def badlettercheck(s):
	badletters = {"i","o","l"}
	for i in range (0, len(s)-1):
		if (s[i] in badletters):
			return False
	return True

def tripletcheck(s):
	for i in range (0, len(s)-2):
		if (s[i:i+3] in letters):
			return True
	return False

def incrementpassword(s):
	lastindex = len(s)-1
	lastletter = s[lastindex]
	value = letters.index(lastletter)
	if value < len(letters)-1:
		newlast = letters[value+1]
		return s[0:lastindex]+newlast
	else:
		newlast = letters[0]
		return incrementpassword(s[0:lastindex])+newlast

while not(badlettercheck(password) & dupecheck(password,2) & tripletcheck(password)):
	password = incrementpassword(password)

print(password)

