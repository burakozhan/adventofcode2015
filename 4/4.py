from sys import argv
import md5

secret = argv[1]

count = 0

while True:
	count = count + 1
	message = md5.new()
	message.update(secret)
	message.update(str(count))
	digest = message.hexdigest()
	if digest.startswith("00000") :
		break

print "part 1 = " + str(count)

count = 0

while True:
	count = count + 1
	message = md5.new()
	message.update(secret)
	message.update(str(count))
	digest = message.hexdigest()
	if digest.startswith("000000") :
		break
print "part 2 = " + str(count)