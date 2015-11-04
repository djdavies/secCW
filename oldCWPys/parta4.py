# Python version 2.7.x
import os

#----------------------------------------------------------------------#
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
    #open and create a key file BEFORE loop
    key = open('key.txt', 'w')

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
        # convert all ints to strings (so we can write to the file)
        byteStream = str(byteStream)
        key.write((byteStream) + '\n')

    #close the key file AFTER loop
    key.close()

    

#----------------------------------------------------------------------#

#calling the function so it creates the key.txt file and it puts the numbers in
byteStreamGen(os.path.getsize('plaintext.txt'))

key_file = open('key.txt', 'r')
key_input = key_file.read()
print ("printing contents of key.txt file..." + key_input)
key_file.close()
with open('key.txt') as f:
    lines = [line.rstrip('\n') for line in open('key.txt')]
lines = [int(i) for i in lines]
print "LINES...."
print (type(lines))
print (lines)

def integers_to_string(ilist):      # ''.join(mylist) creates a string out of the elements of "mylist"
    return ''.join([chr(i) for i in ilist])
def string_to_integers(s):
    return [ord(c) for c in s]

print integers_to_string(lines)
stringtoint = integers_to_string(lines)
print (type(stringtoint))
print ('Printing back from str to int...')
print string_to_integers(stringtoint)


# plaintext to binary
file = open('plaintext.txt', 'r')
input = file.read()
file.close()
print string_to_integers(input)


#XOR-ing 15 and 102
print "%02X" % (34^84)


















