#!/usr/bin/python3
from code_interview.trees import breadth_search_with_depth
from code_interview.trees import BinSearchTree, BinTreeNode
from code_interview.trees.min_heap import MinHeap
from code_interview.chapter4.bst_from_sorted_array import bst_from_sorted_array
import unittest

def list_of_depths(t):
    depth_lists = []
    for n, depth in breadth_search_with_depth(t.root):
        while depth >= len(depth_lists):
            depth_lists.append([])

        depth_lists[depth].append(n)

    return depth_lists

class TestListOfDepths(unittest.TestCase):

    def setUp(self):
        self.f = list_of_depths

    def test_general(self, test_tree=None, expected=None):
        if test_tree and expected:
            result = self.f(test_tree)

            if len(result) != len(expected):
                self.fail("Number of depths lists not expected")

            for result_ll, expected_ll in zip(result, expected):
                if len(result_ll) != len(expected_ll):
                    self.fail("depth list different length")

                for r in result_ll:
                    for i in range(len(expected_ll)):
                        if r == expected_ll[i]:
                            del expected_ll[i]
                            break
                    else:
                        self.fail(str(r) + " not in depth list.")

    def test_1(self):
        t = BinSearchTree()
        r = []
        self.test_general(t, r)

    def test_2(self):
        t = BinSearchTree(1)
        r = [[BinTreeNode(1)]]
        self.test_general(t, r)

    def test_3(self):
        t = bst_from_sorted_array([1, 2, 3, 4, 5])
        r = [
            [t.root],
            [t.root.left, t.root.right],
            [t.root.left.right, t.root.right.right]
        ]
        self.test_general(t, r)


                
if __name__ == "__main__":
    unittest.main()