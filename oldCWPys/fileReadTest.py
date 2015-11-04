# fileReadTest.py
import os
keyFile = open('plaintext.txt', 'r')

print (keyFile.read())
print (os.path.getsize('plaintext.txt'))
