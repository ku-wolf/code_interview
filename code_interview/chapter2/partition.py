#!/usr/bin/python3

from linked_list import LinkedList, Node, EmptyNode
import unittest

def partition(ll, v):
    new_ll = LinkedList()
    for val in ll:
        if val < v:
            new_ll.push(val)
        else:
            new_ll.add(val)
    ll.head = new_ll.head

def partition2(ll, v):
    left = EmptyNode()
    right = EmptyNode()
    last_left = None
    for v in ll:
        if val < v:
            left.push(val)
            if last_left:
                last_left = last_left.next
            else:
                last_left = left
        else:
            right.push(val)

    last_left.next = right
    ll.head = left

def correct_partition(ll, v):
    greater_equal = False
    for val in ll:
        if not greater_equal:
            if val < v:
                continue
            else:
                greater_equal = True
        else:
            if val < v:
                return False
    return True


class TestPartition(unittest.TestCase):

    def setUp(self):
        self.f = partition

    def partition_test(self, l, v):
        self.f(l, v)
        self.assertTrue(correct_partition(l, v))

    def test_1(self):
        self.partition_test(
            LinkedList(),
            5
        )

    def test_1(self):
        self.partition_test(
            LinkedList(3),
            5
        )

    def test_2(self):
        self.partition_test(
            LinkedList(7),
            5
        )

    def test_3(self):
        self.partition_test(
            LinkedList(3, 7, 5),
            5
        )

    def test_4(self):
        self.partition_test(
            LinkedList(5, 1, 10, 5, 5, 7, 3, 9, 0, -1, -2, 4, 10, 5),
            5
        )


class TestPartition2(unittest.TestCase):
    
    def setUp(self):
        self.f = partition2




                
if __name__ == "__main__":
    unittest.main()