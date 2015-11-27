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
split = 2
ciphertext_inputList = [ciphertext_input[i:i+split] for i in range(0, len(ciphertext_input), split)]

print (ciphertext_inputList)

# This is where the problem is, I want "4E", NOT "4", "E"...
# ciphertext_inputList = list(ciphertext_input)

# # read k1 to k2 as a list ('9B', '88', '79', 'E7', '57', '27') 100GBP, bytes 10 to 15 (-1 so it reads the 10th)
k1k2 = ciphertext_inputList[int(sys.argv[2])-1:int(sys.argv[3])]

print (k1k2)

# # plaintext to be replaced (k1 to k2 = 100GBP)
original = sys.argv[4]

# # Convert "100GPB" to ints
print ("100GPB to ints: ") 
originalInts = string_to_integers(original)
print (originalInts)
print ("---------------")

# # Convert k1k2 to ints (the encrypted 100GBP bytes)
k1k2ints = map(int, k1k2)

print ("bytes 10 to 15 (100GPB): ")
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

xordReplacementArray = []
# XOR xordArray with replacement (999EUR) -- in Hex
for i in range(len(xordArrayInts)):
	xordReplacement = "%02X" % (xordArrayInts[i] ^ replacementInt[i])
	xordReplacementArray.append(xordReplacement)

print ("xordArray XOR with replacement")
print (xordReplacementArray)

# Write the new k1 to k2 (xordAr) into the ciphertext file (10 to 15)
print ("array of ciphertext: ")
# Replace elements 10-15 in ciphertext_inputList
ciphertext_inputList[10] = xordReplacementArray[0]
ciphertext_inputList[11] = xordReplacementArray[1]
ciphertext_inputList[12] = xordReplacementArray[2]
ciphertext_inputList[13] = xordReplacementArray[3]
ciphertext_inputList[14] = xordReplacementArray[4]
ciphertext_inputList[15] = xordReplacementArray[5]

# open file for writing new ciphertextfile
newciphertext_file = open('ciphertext_new.txt', 'a')

newciphertext_file.write(''.join(ciphertext_inputList))