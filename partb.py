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

# read k1 to k2 as a list (0, 7, 4, 2, D)
k1k2 = ciphertext_inputList[int(sys.argv[2]):int(sys.argv[3])]
print (k1k2)

# read plaintext to be replaced (k1 to k2 = 100GBP)
original = sys.argv[4]

# Convert 100GPB to ints
print (string_to_integers(original))

# Convert k1k2 to ints
k1k2ints = map(ord, k1k2)

print (k1k2ints)


# XOR k1 to k2 (10 to 15 bits) with 999EUR
# xork1k2 = "%0d" % (k1k2 ^ int(sys.argv[5]))

# print (xork1k2)

# Result in Hex

# This is replacement for original ciphertext (100GPB)

