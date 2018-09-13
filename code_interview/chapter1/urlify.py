#!/usr/bin/python3

from bigO_grapher import graph_avg_times, gen_random_str
from collections import deque
import unittest
import random

def urlify(s, l):
    i = 0
    new_str = ""
    for i in range(l):
        c = s[i]
        if c == " ":
            c = "%20"

        new_str += c

    i = 0
    for c in new_str:
        s[i] = c
        i += 1

    return "".join(s)


def urlify2(s, l):
    print(s, l)
    i = len(s) - 1
    for j in range(l - 1, -1, -1):
        print(j)
        if s[j] == " ":
            s[i] = "0"
            s[i - 1] = "2"
            s[i - 2] = "%"
            i -= 3
        else:
            s[i] = s[j]
            i -= 1

    return "".join(s)


def count_spaces(s):
    spaces = 0
    for c in s:
        if c == " ":
            spaces += 1
    return spaces


def pass_to_urlify(f, s=None):
    def wrapper(s):
        l = len(s)
        num_spaces = count_spaces(s)
        s += " " * num_spaces * 2
        return f(list(s), l)

    if s is not None:
        return wrapper(s)
    return wrapper


def gen_random_str_and_spaces(l):
    remaining = l
    ret = ""
    def char_gen():
        while True:
            yield gen_random_str
            yield lambda l: " "*l
    next_char = char_gen()

    while remaining > 0:
        next_length = random.randrange(1, remaining+1)
        ret += next(next_char)(next_length)
        remaining -= next_length

    return ret




class TestUrlify(unittest.TestCase):
    """
    Test

    - empty string
    - just a space
    - space at start and end
    - string with no spaces
    - multiple spaces in a row
    - multiple spaces at the start and end
    - non-space whitespace
    - long strings
    """

    def setUp(self):
        self.f = urlify

    def test_1(self):
        self.assertEqual(pass_to_urlify(self.f, ""), "")

    def test_2(self):
        self.assertEqual(pass_to_urlify(self.f, " "), "%20")

    def test_3(self):
        self.assertEqual(pass_to_urlify(self.f, "  "), "%20%20")

    def test_4(self):
        self.assertEqual(pass_to_urlify(self.f, "a"), "a")

    def test_5(self):
        self.assertEqual(pass_to_urlify(self.f, "az"), "az")

    def test_6(self):
        self.assertEqual(pass_to_urlify(self.f, " az"), "%20az")

    def test_7(self):
        self.assertEqual(pass_to_urlify(self.f, " az "), "%20az%20")

    def test_8(self):
        self.assertEqual(pass_to_urlify(self.f, "  az  f a o   \t"), "%20%20az%20%20f%20a%20o%20%20%20\t")


class TestUrlify2(TestUrlify):
    """
    Test

    - empty string
    - just a space
    - space at start and end
    - string with no spaces
    - multiple spaces in a row
    - multiple spaces at the start and end
    - non-space whitespace
    - long strings
    """


    def setUp(self):
        self.f = urlify2


def test_and_compare_on_random(*args):
    generate_inputs = lambda x: gen_random_str_and_spaces(x)
    func_with_inputs = ((pass_to_urlify(f), generate_inputs) for f in args)
    graph_avg_times(*func_with_inputs)

if __name__ == "__main__":
    test_and_compare_on_random(urlify, urlify2)
    unittest.main()