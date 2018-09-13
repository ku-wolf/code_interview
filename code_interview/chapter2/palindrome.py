#!/usr/bin/python3

from linked_list import LinkedList, Node, EmptyNode
import unittest

def is_palindrome(ll):
    print(ll)
    l = []
    for v in ll:
        l.append(v)
    print(l)
    return is_palindrome_list(l)

def is_palindrome_list(l):
    i = 0
    j = len(l) - 1
    while j >= i:
        if l[i] != l[j]:
            return False
        i += 1
        j -= 1

    return True

class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        self.f = is_palindrome

    def test_1(self):
        self.assertTrue(self.f(
            LinkedList()
        ))
    def test_1(self):
        self.assertTrue(self.f(
            LinkedList(1)
        ))

    def test_2(self):
        self.assertTrue(self.f(
            LinkedList(1, 0, 1)
        ))

    def test_3(self):
        self.assertTrue(self.f(
            LinkedList(1, 0, 0, 1)
        ))

    def test_4(self):
        self.assertTrue(self.f(
            LinkedList(1, 0, 0, 0, 1)
        ))

    def test_4(self):
        self.assertFalse(self.f(
            LinkedList(1, 1, 0, 0, 1)
        ))


if __name__ == "__main__":
    unittest.main()