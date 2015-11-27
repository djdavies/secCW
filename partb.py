# Python version 2.7.x
# python partb.py ciphertext.txt 10 15 100GBP 999EUR
# python partb.py ciphertextfile k1 k2 original replacement

import os, sys

def string_to_integers(s):
    return [ord(c) for c in s]

# Read original ciphertext file
ciphertext_file = open(sys.argv[1], 'r')
ciphertext_input = ciphertext_file.read()
ciphertext_file.close() 

# Convert to a list
ciphertext_inputList = list(ciphertext_input)

# read k1 to k2 as a list (0, 7, 4, 2, D) 100GBP, bits 10 to 15 (+1 so it reads the 15th)
k1k2 = ciphertext_inputList[int(sys.argv[2]):int(sys.argv[3])+1]

# plaintext to be replaced (k1 to k2 = 100GBP)
original = sys.argv[4]

# Convert 100GPB to ints
print ("100GPB to ints: ") 
originalInts = string_to_integers(original)
print ("---------------")

# Convert k1k2 to ints (the encrypted 100GBP bits)
k1k2ints = map(ord, k1k2)

print ("bits 10 to 15 (100GPB): ")
print (k1k2ints)
print ("--------------")

# 999EUR
replacement = sys.argv[5]

# Convert replacement to ints
replacementInt = string_to_integers(replacement)

print ("replacement (999EUR): ")
print (replacementInt)

xordArray = []
# XOR k1k2ints with plaintext
for i in range(len(k1k2ints)):
	xork1k2pt = "%0d" % (k1k2ints[i] ^ originalInts[i])
	# Add each XORd value to an array
	xordArray.append(xork1k2pt)

# convert xordArray str values to ints
xordArrayInts = [int(i) for i in xordArray]
print ("xordArrayInts: ")
print (xordArrayInts)

xordArrayReplacementArray = []
# XOR xordArray with replacement (999EUR) -- in Hex
for i in range(len(xordArrayInts)):
	xordArrayReplacement = "%02X" % (xordArrayInts[i] ^ replacementInt[i])
	xordArrayReplacementArray.append(xordArrayReplacement)

print ("xordArray XOR with replacement")
print (xordArrayReplacementArray)	

# Write the new k1 to k2 into the ciphertext file (10 to 15)
print ("array of ciphertext: ")
print (ciphertext_input)
