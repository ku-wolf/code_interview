#!/usr/bin/python3
import pdb
import unittest
import random
import math
import sys
from collections import deque, Counter
from code_interview.chapter10.sorting import swap_in_place
from code_interview.chapter10.file_chunker import read_file_chunked

def missing_int(fname):
    seen_integers = 0
    for l in read_file_chunked(fname, 5 * 10 ** 6):

        for b in range(0, len(l) - 4, 4):
            i = int.from_bytes(l[b: b + 4], sys.byteorder, signed=False)
            seen_integers |= (1 << i)

    num = 0
    while seen_integers & 1 == 0:
        seen_integers >>= 1
        num += 1

    return num


class TestMissingInt(unittest.TestCase):

    def setUp(self):
        self.f = missing_int

    def test_1(self):
        f = sys.argv[1]
        print(missing_int(f))


if __name__ == "__main__":
    print(sys.argv[1])
    print(missing_int(sys.argv[1]))
