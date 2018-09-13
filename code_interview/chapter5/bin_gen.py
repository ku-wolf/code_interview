#!/usr/bin/python3
from collections import deque

def bin_gen(n):
    yield n & 1
    n >>= 1
    while n != 0:
        yield n & 1
        n >>= 1

def convert_to_bin_str(n, fixed_size=None):
    r = deque()
    for i in bin_gen(n):
        r.appendleft(str(i))

    zero_pad = 0
    if fixed_size is not None:
        zero_pad = fixed_size - len(r)
        if zero_pad < 0:
            zero_pad = 0

    return "0" * zero_pad + "".join(r)