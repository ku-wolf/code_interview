#!/usr/bin/python3
import unittest

def one_away(s1, s2):

    longer, smaller = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
    if len(longer) - len(smaller) > 1:
        return False
    elif len(longer) == len(smaller):
        return check_for_edit(longer, smaller)
    else:
        return check_for_edit(longer, smaller, t="delete")

def check_for_edit(l, s, t="replace"):
    i = j = 0
    edits_remaining = 1
    while i < len(l) and j < len(s):
        if l[i] == s[j]:
            j += 1
        else:
            edits_remaining -= 1
            if edits_remaining < 0:
                return False
            if t == "replace":
                j += 1

        i += 1

    return True


class TestOneAway(unittest.TestCase):

    def setUp(self):
        self.f = one_away

    def test_1(self):
        self.assertTrue(self.f("", ""))

    def test_2(self):
        self.assertTrue(self.f("a", "a"))

    def test_3(self):
        self.assertTrue(self.f("a", "b"))

    def test_4(self):
        self.assertTrue(self.f("jake", "jake"))

    def test_5(self):
        self.assertFalse(self.f("jaek", "jake"))

    def test_6(self):
        self.assertTrue(self.f("", "a"))

    def test_7(self):
        self.assertFalse(self.f("a", "abcd"))

    def test_8(self):
        self.assertTrue(self.f("a", "ab"))

    def test_9(self):
        self.assertTrue(self.f("jake", "bake"))

    def test_10(self):
        self.assertFalse(self.f("same", "bake"))

    def test_11(self):
        self.assertFalse(self.f("beekj", "baek"))


if __name__ == "__main__":
    unittest.main()