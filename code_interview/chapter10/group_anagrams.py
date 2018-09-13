#!/usr/bin/python3
import pdb
import unittest
import random
import math
from collections import deque, Counter
from code_interview.chapter10.sorting import swap_in_place

def create_anagram_signature(s):
    return frozenset(Counter(s).most_common())

def group_anagrams(l):

    anagram_groups = {}

    for s in l:
        anagram_sig = create_anagram_signature(s)
        if anagram_sig in anagram_groups:
            anagram_groups[anagram_sig].append(s)
        else:
            anagram_groups[anagram_sig] = [s]

    i = 0
    for anagram_group in anagram_groups.values():
        for a in  anagram_group:
            l[i] = a
            i += 1


def find_anagram_indexes(l, anagram_signature):
    ret = []
    for i in range(len(l) - 1):
        if create_anagram_signature(l[i]) == anagram_signature:
            ret.append(i)

    return ret


def is_consecutive(l):
    l.sort()
    previous = None
    for e in l:
        if previous is not None and e != previous + 1:
            return False
        previous = e

    return True


def verify_group_anagrams(self, before, after):

    counter_before = Counter(before)
    counter_after = Counter(after)

    self.assertEqual(counter_before, counter_after)

    anagram_sigs = set()

    for s in after:
        anagram_sig = create_anagram_signature(s)
        if anagram_sig not in anagram_sigs:
            indexes = find_anagram_indexes(after, anagram_sig)
            consecutive = is_consecutive(indexes)
            if not consecutive:
                pdb.set_trace()
            self.assertTrue(is_consecutive(find_anagram_indexes(after, anagram_sig)))


class TestGroupAnagrams(unittest.TestCase):

    def setUp(self):
        self.f = group_anagrams

    def test(self):
        tests = [
            [],
            ["1"],
            ["abc", "ab", "acb", "ba", "acbd"],
            ["ab", "abc", "acb", "ba", "acbd"],
            ["abc", "ab", "acb", "bad", "acb"],
            ["a", "ab", "abc", "abcd", "ba"],
            ["abc", "ab", "acb", "ba", "acbd"],
        ]

        for t in tests:
            before = list(t)
            self.f(t)
            verify_group_anagrams(self, before, t)


if __name__ == "__main__":
    unittest.main()