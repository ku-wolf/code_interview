#!/usr/bin/python3
import unittest

def is_unique(s):
    ch = set()
    for c in s:
        if c in ch:
            return False
        ch.add(c)
    return True

def is_unique2(s):
    for i in range(len(s) - 1, 0, -1):
        for j in range(i):
            if s[j] == s[i]:
                return False
    return True

fs_to_test = [is_unique, is_unique2]
class TestIsUnique(unittest.TestCase):

    def setUp(self):
        self.f = is_unique

    def test_1(self):
        self.assertTrue(self.f(""))

    def test_2(self):
        self.assertTrue(self.f("a"))

    def test_3(self):
        self.assertTrue(self.f("abcd"))

    def test_4(self):
        self.assertFalse(self.f("abca"))

    def test_5(self):
        self.assertFalse(self.f("baad"))

    def test_6(self):
        self.assertTrue(self.f("hi猫"))

    def test_7(self):
        self.assertTrue(self.f("hi猫⺁"))


class TestIsUnique2(TestIsUnique):

    def setUp(self):
        self.f = is_unique2

if __name__ == "__main__":
    unittest.main()