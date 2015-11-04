# Python version 2.7.x
import os
import sys

#----------------------------------------------------------------------#
# Key Setup.
def keySetup():
# Input: an array key[] containing k.len integers.
    key = (83, 101, 99, 114, 101, 116, 32, 107, 101, 121)
    k = range(256)

# Output: a permutation k of the numbers 0...255.

    for i in range(256):
        k[i] = i
    j = 0
    for i in range(256):
      # j = (j + K[i] + key[i mod k.len]) mod 256
        j = (j + k[i] + key[i % len(key)]) % 256
        # swap k[i], k[j]
        k[i], k[j] = k[j], k[i]
    return (k)

#----------------------------------------------------------------------#
# Byte stream generator.
def byteStreamGen(n):
    # k is now assigned via keySetup's k list.
    k = (keySetup())
    i = 0; j = 0

    num = 0
    # open and create a key file (e.g. key.txt)
    key = open(sys.argv[2], 'w')

    # Start...
    while(num < n): 
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        # swap k[i], k[j]
        k[i], k[j] = k[j], k[i]
        # Output...
        byteStream = k[ ( k[i] + k[j] ) % 256 ]
        # Goto start
        num += 1
        # convert all ints to strings on the fly
        byteStream = str(byteStream)
        key.write(byteStream + '\n')

    #close the key file AFTER loop
    key.close()

    

#----------------------------------------------------------------------#

def string_to_integers(s):
    return [ord(c) for c in s]


def integers_to_string(ilist):      # ''.join(mylist) creates a string out of the elements of "mylist"
    return ''.join([chr(i) for i in ilist])

# Open plaintext.txt 
file = open(sys.argv[3], 'r')
input = file.read()
print ("contents of file...")
print (input)
file.close()

hexArrayEncrypted = []

# XOR (and conv. to HEX) the elements of both lists.
def xorEncryption(key, pt):
    for i in range(len(key)):
        encrypted = "%s" % (key[i]^pt[i])
        # Add the hex output to the hexArrayEncrypted
        hexArrayEncrypted.append(encrypted)
        # Write the output file (encypted.txt).
        outputFileEncrypted.write(encrypted)
    return (encrypted)

def xorDecrypted(key,decryptList):
    for i in range(len(key)):
        # XOR the values
        decrypted = "%0d" % (key[i]^decryptList[i])
        # Convert to int, then chr value
        decryptedInt = int(decrypted)
        chrDecryptedVal = chr(decryptedInt)
        # Write the outfile file
        outputFileDecrypted.write(chrDecryptedVal)
    return (decrypted)

if sys.argv[1] == 'e':
    print ("Encrpyting...:\n")
     # Use the size of plaintext as the iterator condition.
    byteStreamGen(os.path.getsize(sys.argv[3]))

    # Open key.txt
    key_file = open(sys.argv[2], 'r')
    key_input = key_file.read()
    key_file.close()

    # Convert the line-separated key.txt values from str to int
    with open(sys.argv[2]) as f:
        keyLines = [line.rstrip('\n') for line in open(sys.argv[2])]
        keyLines = [int(i) for i in keyLines]

    # plaintext to ints
    pt2int = string_to_integers(input)

    # Output of the encryption, write
    outputFileEncrypted = open(sys.argv[4], 'w') 

    # XOR the lines in key with plaintext.  
    xorEncryption(keyLines, pt2int)

    outputFileEncrypted.close()


elif sys.argv[1] == 'd':
    print ("Decrypting...\n")
    # Read the contents of the encrypted file 
    encryptedFileInput = open(sys.argv[3], 'r')
    encryptedFile = encryptedFileInput.read() 
    encryptedFileInput.close()

    # Split encrypted file: 2 digits, into an array (e.g. '4E, 40,...' -> list)
    split = 2
    encryptedFileArray = [encryptedFile[i:i+split] for i in range(0, len(encryptedFile), split)]
    
    # Convert encrypted file from hex to decimal.
    encryptedFileArrayDecs = []
    for e in encryptedFileArray:
        x = int("0x"+e, 0)
        encryptedFileArrayDecs.append(x)

    print (encryptedFileArrayDecs)    

    # Read key.txt (sys.argv[2])
    key_file = open(sys.argv[2], 'r')
    key_input = key_file.read()
    key_file.close()    

    # Convert all lines in key_file, convert to ints
    # Convert the line-separated key.txt values from str to int
    with open(sys.argv[2]) as f:
        keyLines = [line.rstrip('\n') for line in open(sys.argv[2])]
        keyLines = [int(i) for i in keyLines]

    print keyLines    

    # Output of the encryption, write
    outputFileDecrypted = open(sys.argv[4], 'w') 

    # XOR every elem. in encryptedFileArrayDecs with keyLines..
    xorDecrypted(keyLines,encryptedFileArrayDecs)

    outputFileDecrypted.close()
    

elif sys.argv[1] != 'e' or 'd':
    print ("""argv not recognised\n
        Usage:\n
        To encrypt: python parta.py e keyfile inputfile outputfile\n
        To decrypt: python parta.py d keyfile encryptedFile decryptedFile\n""")

















