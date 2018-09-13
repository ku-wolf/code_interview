#!/usr/bin/python3

from linked_list import LinkedList
import unittest

def remove_dups(ll):
    prev = None
    seen_vals = set()
    for n in ll.iter_nodes():
        if n.val in seen_vals:
            if prev:
                prev.next = n.next
        else:
            seen_vals.add(n.val)
        prev = n

    return ll

class TestRemoveDups(unittest.TestCase):

    def setUp(self):
        self.f = remove_dups

    def test_1(self):
        self.assertEqual(self.f(LinkedList()), LinkedList())

    def test_2(self):
        l = LinkedList()
        l.add(1)
        self.assertEqual(self.f(l), l)

    def test_3(self):
        l = LinkedList(1, 1, 2, 2, 1)
        l2 = LinkedList(1, 2)
        self.assertEqual(self.f(l), l2)

                
if __name__ == "__main__":
    unittest.main()