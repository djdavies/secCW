# Python version 2.7.x
import os

#---------------------------------------------------#
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
#---------------------------------------------------#    

#---------------------------------------------------#    
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
        key.close()
        # print ("Contents of key: " + keyCharStream)
    # end while loop

#---------------------------------------------------#    

# plaintext.txt = 32
byteStreamGen(os.path.getsize('plaintext.txt'))


# Open plaintext
pt = open("plaintext.txt", "r")
inputFile = pt.read()
pt.close()
print ("contents of inputFile: " + inputFile + "\n")

# plaintext to ASCII char val -- produces list of ints.
def string_to_integers(s):
    mylist = [ord(c) for c in s]
    return mylist

ilist =  (string_to_integers(inputFile))

print (ilist)

def integers_to_string(ilist):      # ''.join(mylist) creates a string out of the elements of "mylist"
    return ''.join([chr(i) for i in ilist]) 

# print (integers_to_string(ilist))

# Convert ASCII to HEX
print "Decimal to hex: \n"
# hexFormatStr = "%02X-" *31 + "%02X"
# print "%02X" %  (ilist[0]) # 84
print "%02X" % (ilist[0]^94)