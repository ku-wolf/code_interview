#!/usr/bin/python3
import unittest
from collections import Counter, deque
from bigO_grapher import time_f_on_inputs, graph_times, graph_avg_times
import random
import string
from math import factorial

def check_permutation(strings):
    s1, s2 = strings
    if len(s1) != len(s2):
        return False

    compare_set = Counter(s1)
    for s in s2:
        if s in compare_set:
            compare_set[s] -= 1
            if not compare_set[s]:
                del compare_set[s]
        else:
            return False
    return True


def generate_knuth_shuffle(s):
    l = list(s)
    n = len(s)
    for i in range(factorial(n)):
        for i in range(n - 2):
            j = random.randrange(i, n)
            i_val = l[i]
            l[i] = l[j]
            l[j] = i_val

        ret = ""
        for el in l:
            ret += el

        yield ret


def gen_random_str(length):
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))


def generate_random_string_and_permutation(length):
    s = gen_random_str(length)
    return (s, s.shuffle())


def test_random_at_size(size, number_of_tests=1000, time_result=False, *args, **kwargs):
    random_str = gen_random_str(size)
    perm_gen = iter(generate_knuth_shuffle(random_str))
    inputs = ((random_str, perm) for perm in (next(perm_gen) for i in range(number_of_tests)))

    if time_result:
        yield time_f_on_inputs((check_permutation, inputs), *args, **kwargs)
    else:
        for i in inputs:
            yield check_permutation(i), i

class TestCheckPermutation(unittest.TestCase):

    def setUp(self):
        self.f = check_permutation

    def test_1(self):
        self.assertTrue(self.f(("", "")))

    def test_2(self):
        self.assertTrue(self.f(("a", "a")))

    def test_3(self):
        self.assertFalse(self.f(("a", "")))

    def test_4(self):
        self.assertFalse(self.f(("", "a")))

    def test_5(self):
        self.assertFalse(self.f(("ab", "aa")))

    def test_6(self):
        self.assertTrue(self.f(("aba", "baa")))

    def test_7(self):
        self.assertTrue(self.f(("abba", "abba")))

    def test_8(self):
        self.assertTrue(self.f(("baca", "acab")))

    def test_2_random(self):
        graph_avg_times(
            (
                self.f,
                lambda x: (gen_random_str(x), gen_random_str(x))
            )
        )

    def test_9(self):
        for i in range(1000, 10000, 1000):
            for r, i in test_random_at_size(i, mute=True):
                self.assertTrue(r)
                
if __name__ == "__main__":
    #for i in range(0, 1000):
    #    print(next(test_random_at_size(i, mute=True, time_result=True)))

    unittest.main()
