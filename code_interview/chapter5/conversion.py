#!/usr/bin/python3
def conversion(a, b):
    if a < 0 or b < 0:
        return "Neg"
    count = 0
    n = a ^ b
    while n != 0:
        count += 1
        n = n & (n - 1)

    return n