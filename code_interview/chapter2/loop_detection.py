#!/usr/bin/python3

from linked_list import LinkedList, Node, EmptyNode
import unittest

def loop_detection(ll):
    seen = dict()
    index = 0
    for n in ll.iter_nodes():
        if id(n) in seen:
            return n
        else:
            seen[id(n)] = index

        index += 1

def create_loop(ll, back_to_index):
    i = 0
    back_to_node = None
    last_node = None
    for n in ll.iter_nodes():
        if i == back_to_index:
            back_to_node = n
        last_node = n
        i += 1
    last_node.next = back_to_node

class TestLoopDetection(unittest.TestCase):

    def setUp(self):
        self.f = loop_detection

    def create_loop_and_test(self, ll, loop_index):
        create_loop(ll, loop_index)
        loop_node = ll.get(loop_index)
        result_node = self.f(ll)
        print(id(loop_node), id(result_node))
        self.assertTrue(result_node is loop_node)

    def test_1(self):
        self.create_loop_and_test(
            LinkedList(1),
            0
        )

    def test_2(self):
        self.create_loop_and_test(
            LinkedList(1, 2),
            1
        )

    def test_3(self):
        self.create_loop_and_test(
            LinkedList(1, 2, 3),
            0
        )

    def test_4(self):
        self.create_loop_and_test(
            LinkedList(1, 2, 3, 4),
            1
        )

    def test_5(self):
        self.create_loop_and_test(
            LinkedList(1, 2, 3, 4),
            3
        )

                
if __name__ == "__main__":
    unittest.main()