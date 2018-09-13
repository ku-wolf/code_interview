#!/usr/bin/python3
import unittest
import math
import random

def parens(pairs):
    return parens_h(pairs, pairs)

def parens_h(l, r):
    if l == 0 and r == 0:
        return set([""])

    results = set()
    if l > 0:
        for p in parens_h(l - 1, r):
            results.add("(" + p)
    if r > l:
        for p in parens_h(l, r - 1):
            results.add(")" + p)

    return results



class TestParens(unittest.TestCase):

    def setUp(self):
        self.f = parens

    def test_1(self):
        tests = [
            (1, set(["()"])),
            (0, set([""])),
            (2, set(["()()", "(())"])),
            (3, set(["()()()", "()(())", "(())()", "((()))", "(()())"])),
        ]

        for t,e in tests:
            self.assertEqual(self.f(t), e, t)


if __name__ == "__main__":
    unittest.main()