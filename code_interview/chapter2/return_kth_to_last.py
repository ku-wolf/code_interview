#!/usr/bin/python3

from linked_list import LinkedList, Node
import unittest

def return_kth_to_last(ll, k):
    if k < 0:
        return None

    till_slow_start = 0
    kth_last = None
    for node in ll.iter_nodes():
        if till_slow_start == k:
            kth_last = ll.head
        if till_slow_start > k:
            kth_last = kth_last.next
        till_slow_start += 1
    return kth_last


class TestKthToLast(unittest.TestCase):

    def setUp(self):
        self.f = return_kth_to_last

    def test_1(self):
        self.assertEqual(self.f(LinkedList(), 0 ), None)

    def test_2(self):
        l = LinkedList()
        l.add(1)
        self.assertEqual(self.f(l, 0), Node(1))

    def test_3(self):
        l = LinkedList()
        l.add(1)
        self.assertEqual(self.f(l, 1), None)

    def test_4(self):
        l = LinkedList(1, 2, 3, 4, 5)
        l2 = Node(5)
        self.assertEqual(self.f(l, 0), l2)

    def test_5(self):
        l = LinkedList(1, 2, 3, 4, 5)
        l2 = Node(3, 4, 5)
        self.assertEqual(self.f(l, 2), l2)

    def test_6(self):
        l = LinkedList(1, 2, 3, 4, 5)
        l2 = Node(1, 2, 3, 4, 5)
        self.assertEqual(self.f(l, 4), l2)

    def test_7(self):
        l = LinkedList(1, 2, 3, 4, 5)
        self.assertEqual(self.f(l, 5), None)

    def test_8(self):
        l = LinkedList()
        self.assertEqual(self.f(l, 1), None)

    def test_9(self):
        l = LinkedList()
        self.assertEqual(self.f(l, 5), None)

    def test_10(self):
        l = LinkedList(1, 2, 3, 4, 5)
        self.assertEqual(self.f(l, -1), None)

                
if __name__ == "__main__":
    unittest.main()