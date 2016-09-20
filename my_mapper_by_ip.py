#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip = data[0]
        print ip


