#!/usr/bin/python3
import unittest
import copy
import string
from code_interview.chapter1.permutations import check_permutation
import math

def permutations_without_dups(s):
    perms = permutations_without_dups_l(s)

    for i in range(len(perms)):
        perms[i] = "".join(perms[i])

    return perms



def permutations_without_dups_l(s):
    if not s:
        return [[]]

    perms = []
    for i in range(len(s)):
        new_s = []
        for j in range(len(s)):
            if i != j:
                new_s.append(s[j])

        for p in permutations_without_dups_l(new_s):
            p.insert(0, s[i])
            perms.append(p)

    return perms


class TestPermutationsNoDups(unittest.TestCase):

    def setUp(self):
        self.f = permutations_without_dups

    def test_1(self):
        tests = [
            ("", [""]),
            ("a", ["a"]),
            ("ab", ["ab", "ba"]),
            ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ]

        for t,e in tests:
            self.assertEqual(self.f(t).sort(), e.sort(), t)

    def test_2(self):
        alphabet = string.ascii_letters[:6]
        perms = self.f(alphabet)
        self.assertEqual(
            len(set(perms)),
            math.factorial(len(alphabet))
        )

        for p in perms:
            self.assertTrue(check_permutation((p, alphabet)))


if __name__ == "__main__":
    unittest.main()
