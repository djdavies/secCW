import os
# Key Setup.
def keySetup():
	# Input: an array key[] containing k.len integers.
	key = range(0,256)
	k = [None] * 256

	# Output: a permutation K of the numbers 0...255.
	for i in key:
		k[i] = i

	j = 0

	for i in key:
		# j := (j + K[i] + key[i mod k.len]) mod 256
		j = (j + k[i] + key[i % len(k)]) % 256
		# swap k[i], k[j]
		k[i], k[j] = k[j], k[i]

	return (k)

# print (keySetup())

# Byte stream generator.
def byteStreamGen(n):
	# k is now assigned via keySetup's k list.
	k = (keySetup())
	i = 0; j = 0

	num = 0
	# Start...

	plaintext = open("plaintext.txt", 'r')

	# ord accepts chars, so iterate string as chars
	plainTextToChar = ''.join(str(e) for e in plaintext)

	# convert chars to bin
	plainTextBin = (''.join(format(ord(x), 'b') for x in plainTextToChar))
	
	while(num < n): 
		i = (i + 1) % 256
		j = (j + k[i]) % 256
		# swap k[i], k[j]
		k[i], k[j] = k[j], k[i]
		# Output...
		x = (k[ ( k[i] + k[j] ) % 256 ])
		# Goto start
		num += 1
		#print (x)
		# Convert x, the key, to bin
		# Iterate through x as 
		x = ''.join(str(e) for e in x)
		y = ''.join(format(ord(z), 'b') for z in x)
	return (y)

# Set the condition for the while iteration as 
# the file size of the plaintext file.
print (byteStreamGen(os.path.getsize('plaintext.txt')))

print (keySetup)

