#!/usr/bin/python3
import unittest
import math
import random

def recursive_multiply_1(n1, n2):
    neg1 = n1 < 0
    neg2 = n2 < 0
    bigger = abs(max(n1, n2))
    smaller = abs(min(n1, n2))


    result = recursive_multiply_1_helper(bigger, smaller, 0)
    if neg1 ^ neg2:
        result = -result

    return result

def recursive_multiply_1_helper(n1, n2, acc):
    if not n1 or not n2:
        return acc

    return recursive_multiply_1_helper(n1, n2 - 1, acc + n1)


def recursive_multiply_2(n1, n2):
    neg1 = n1 < 0
    neg2 = n2 < 0
    b = abs(max(n1, n2))
    s = abs(min(n1, n2))


    result = recursive_multiply_2_helper(b, s, 0)
    if neg1 ^ neg2:
        result = -result

    return result


def recursive_multiply_2_helper(n1, n2, acc):
    if not n1 or not n2:
        return acc

    high_bit = math.floor(math.log(n2, 2))
    mask = 2 ** (high_bit + 1) - 1 >> 1

    return recursive_multiply_2_helper(n1, n2 & mask, acc + (n1 << high_bit))


def recursive_multiply_3(n1, n2):
    neg1 = n1 < 0
    neg2 = n2 < 0
    b = abs(max(n1, n2))
    s = abs(min(n1, n2))


    result = recursive_multiply_3_helper(b, s, {})
    if neg1 ^ neg2:
        result = -result

    return result


def recursive_multiply_3_helper(n1, n2, memo):
    if n2 is 0:
        return 0
    if n2 is 1:
        return n1
    if n2 in memo:
        return memo[n2]

    half_n2 = n2 >> 1
    half_mult = recursive_multiply_3_helper(n1, half_n2, memo)

    result = half_mult + half_mult
    if n2 % 2 == 1:
        result += n1

    memo[n2] = result
    return result


class TestRecursiveMultiply(unittest.TestCase):

    def setUp(self):
        self.f = recursive_multiply_3

    def test_1(self):
        tests = [
            ((0, 0), 0),
            ((0, 1), 0),
            ((1, 0), 0),
            ((1, 1), 1),
            ((1, 2), 2),
            ((2, 1), 2),
            ((16, 1), 16),
            ((1, 16), 16),
            ((231, 5), 1155)
        ]

        for t,e in tests:
            self.assertEqual(self.f(*t), e, t)

    def test_2(self):
        num_tests = 1000
        r = - 2 * 65 - 1
        r2 = 2 * 65 - 1
        for i in range(1000000):
            n1 = random.randint(r, r2)
            n2 = random.randint(r, r2)

            self.assertEqual(self.f(n1, n2), n1 * n2, (n1, n2))


class TestRecursiveMultiply2(TestRecursiveMultiply):

    def setUp(self):
        self.f = recursive_multiply_1


class TestRecursiveMultiply3(TestRecursiveMultiply):

    def setUp(self):
        self.f = recursive_multiply_2
                
if __name__ == "__main__":
    unittest.main()