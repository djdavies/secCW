key = range(0,256)

print (key)

str1 = ''.join(str(e) for e in key)

print (str1)


def convert(s):
	return [ord(c) for c in s]

print (convert(str1))

