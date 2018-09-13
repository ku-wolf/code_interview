#!/usr/bin/python3
import pdb
import unittest
import random
import math
from collections import deque, Counter
from code_interview.chapter10.sorting import swap_in_place


class ListY(list):

    def __len__(self):
        return None


def search_no_size_naive(listy, el):
    index = 0
    for e in listy:
        if e == el:
            return index
        index += 1

    return None


def bst_search(listy, el, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    mid_el = listy[mid]

    if mid_el == el:
        return mid
    elif mid_el < el:
        return bst_search(listy, el, mid + 1, end)
    else:
        return bst_search(listy, el, start, mid - 1)


def search_no_size(listy, el, start=0):
    if start < 0:
        return None

    try:
        listy[start]
    except IndexError:
        return None

    mid = 2
    while True:
        try:
            listy[start + mid - 1]
        except IndexError:
            break

        mid *= 2

    mid = int(mid // 2)
    mid_el = listy[start + mid - 1]

    if mid_el == el:
        return start + mid - 1
    elif mid_el < el:
        return search_no_size(listy, el, start + mid)
    else:
        return bst_search(listy, el, start, start + mid - 2)


class TestGroupAnagrams(unittest.TestCase):

    def setUp(self):
        self.f = search_no_size


    def test(self):
        for i in range(100):
            l = ListY([j * 2 for j in range(i)])
            for j in range(i*2):
                if j in l:
                    result = self.f(l, j)
                    try:
                        a = l[result]
                    except IndexError:
                        a = None
                        pdb.set_trace()
                        self.fail()
                    b = j
                else:
                    result = self.f(l, j)
                    a = result
                    b = None

                if a != b:
                    pdb.set_trace()

                self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()