#!/bin/bash
for run in {1..10}
do
python parta.py e key.txt plaintext4096.txt encrypted.txt
done
