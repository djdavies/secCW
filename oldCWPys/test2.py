import binascii

key = 'hello'

print (bin(int(binascii.hexlify(key), 16)))