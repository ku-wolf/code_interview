#!/usr/bin/python3
# check integer rep size
import sys
import math

seen = set()

i = 1
while i < 2 ** 128 - 1:
    s = sys.getsizeof(i)
    if s not in seen:
        print(s, i, math.log(i))
    seen.add(s)
    i *= 2