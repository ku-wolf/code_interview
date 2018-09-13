#!/usr/bin/python3
import unittest
from collections import Counter
from bigO_grapher import gen_random_str

def palindrome_permutation(s):
    char_counts = Counter(s)
    num_odd = 0
    for l, c in char_counts.items():
        if not c % 2:
            continue
        else:
            num_odd += 1
            if num_odd > 1:
                return False
    return True

def generate_palindrome_from_str(s, middle_char):
    ret = s + middle_char
    for i in range(len(s) - 1, -1, -1):
        ret += s[i]
    return ret

def generate_random_palindrome(l):
    middle_char = ""
    if not l % 2:
        middle_char = gen_random_str(1)

    l = l // 2
    return generate_palindrome_from_str(gen_random_str(l), middle_char=middle_char)


class TestPalindromePermutation(unittest.TestCase):

    def setUp(self):
        self.f = palindrome_permutation

    def test_many(self):
        for i in range(100):
            print("testing pals at size", i)
            for j in range(10000):
                pal = generate_random_palindrome(i)
                self.assertTrue(palindrome_permutation(pal))

    def test_incorrect(self):
        self.assertFalse(palindrome_permutation("aaabbdbccc"))

if __name__ == "__main__":
    unittest.main()