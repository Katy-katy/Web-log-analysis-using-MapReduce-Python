#!/usr/bin/python

import sys

number = 0
oldKey = None

for line in sys.stdin:
    thisKey = line
   
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", number
        oldKey = thisKey;
        number = 0

    oldKey = thisKey
    number += 1

if oldKey != None:
    print oldKey, "\t", number

