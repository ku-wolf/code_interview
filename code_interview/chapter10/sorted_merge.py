#!/usr/bin/python3
import unittest
import random
import math
from collections import deque

def sorted_merge(A, B):
    rightmost_spot = len(A) - 1
    i = len(A) - 1 - len(B)
    j = len(B) - 1

    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[rightmost_spot] = A[i]
            i -= 1
        else:
            A[rightmost_spot] = B[j]
            j -= 1
        rightmost_spot -= 1

    while rightmost_spot >= 0:
        if i >= 0:
            val = A[i]
            i -= 1
        else:
            val = B[j]
            j -= 1

        A[rightmost_spot] = val
        rightmost_spot -= 1


def test(self, A, B):
    A.sort()
    B.sort()
    expected = list(A)
    expected.extend(B)
    expected.sort()

    A.extend([None for _ in range(len(B))])
    sorted_merge(A, B)

    self.assertEqual(A, expected)

class TestSortedMerge(unittest.TestCase):

    def setUp(self):
        self.f = sorted_merge

    def test_random(self):
        for i in range(100):
            for j in range(100):
                for l in range(100):
                    A = [k for k in range(i)]
                    B = [k for k in range(j)]
                    random.shuffle(A)
                    random.shuffle(B)
                    test(self, A, B)


if __name__ == "__main__":
    unittest.main()