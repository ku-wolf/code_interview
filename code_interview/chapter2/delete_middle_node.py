#!/usr/bin/python3

from linked_list import LinkedList, Node, EmptyNode
import unittest

def delete_middle_node(mid_node):
    for n in mid_node.iter_nodes():
        n.val = n.next.val
        if n.next.next is None:
            n.next = None
            break

class TestDeleteMiddleNode(unittest.TestCase):

    def setUp(self):
        self.f = delete_middle_node

    def test_1(self):
        self.assertEqual(self.f(EmptyNode()), None)

    def test_2(self):
        l = LinkedList(1, 2, 3)
        to_delete = l.get(1)
        result = LinkedList(1, 3)
        self.f(to_delete)
        self.assertEqual(l, result)

    def test_3(self):
        l = LinkedList(1, 2, 3, 4, 5)
        to_delete = l.get(1)
        result = LinkedList(1, 3, 4, 5)
        self.f(to_delete)
        self.assertEqual(l, result)

    def test_4(self):
        l = LinkedList(1, 2, 3, 4, 5)
        to_delete = l.get(3)
        result = LinkedList(1, 2, 3, 5)
        self.f(to_delete)
        self.assertEqual(l, result)

    def test_5(self):
        l = LinkedList(1, 2, 3, 4, 5)
        to_delete = l.get(2)
        result = LinkedList(1, 2, 4, 5)
        self.f(to_delete)
        self.assertEqual(l, result)




                
if __name__ == "__main__":
    unittest.main()