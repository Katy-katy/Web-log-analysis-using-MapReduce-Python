#!/usr/bin/python

import sys

number = 0
oldKey = None

mostPopular = None
mostPopNumber = 0

for line in sys.stdin:
    thisKey = line
   
    if oldKey and oldKey != thisKey:
        if number > mostPopNumber:
            mostPopNumber = number
            mostPopular = oldKey
        oldKey = thisKey
        number = 0

    oldKey = thisKey
    number += 1

if oldKey != None:
    if number > mostPopNumber:
        mostPopNumber = number
        mostPopular = oldKey

print mostPopular, "\t", mostPopNumber

