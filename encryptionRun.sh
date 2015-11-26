#!/bin/bash
for run in {1..10}
do
python parta.py e key.txt plaintext.txt encrypted.txt
done