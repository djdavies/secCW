# Python version 2.7.2
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

    print (keySetup())

pt = open("plaintext.txt", "r")

testString = "Transfer 100GBP to account 1234."

# plaintext to binary
plainTextBin = (''.join(format(ord(x), 'b') for x in testString))
print ("plainTextBin...")
print (plainTextBin)
print (type(plainTextBin))
testStr = 'hello'
print ("plainTextBin back to ASCII: " + chr(int(plainTextBin, 2)))

# Byte stream generator.
def byteStreamGen(n):
    # k is now assigned via keySetup's k list.
    k = (keySetup())
    i = 0; j = 0

    num = 0
    # Start...
    while(num < n): 
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        # swap k[i], k[j]
        k[i], k[j] = k[j], k[i]
        # Output...
        byteStream = (k[ ( k[i] + k[j] ) % 256 ])
        # Goto start
        num += 1
        # convert all ints to strings on the fly
        byteStream = str(byteStream)

    #open a text file named key
    key = open('key.txt', 'a')

    # construct string of chars via byteStream, write to file
    keyCharStream = ''.join(str(c) for c in byteStream)
    key.write(keyCharStream)

    # convert keyCharStream to binary
    keyCharBin = (''.join(format(ord(z), 'b') for z in keyCharStream))
    print ("keyCharBin: " + keyCharBin)
    return keyCharStream
    # return (byteStream)

print (byteStreamGen(os.path.getsize('plaintext.txt')))

