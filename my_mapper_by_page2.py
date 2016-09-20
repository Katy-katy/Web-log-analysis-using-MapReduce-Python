#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        page = data[6]
        page = re.sub("http://www.the-associates.co.uk", "", page)
        print page

