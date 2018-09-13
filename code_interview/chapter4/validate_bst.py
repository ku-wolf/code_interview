#!/usr/bin/python3
from code_interview.trees import BinSearchTree, EmptyTreeNode
from code_interview.trees.min_heap import MinHeap
import unittest

def validate_bst(root_node, min_val = None, max_val = None):
    if root_node.is_empty():
        return True

    if min_val is not None and root_node.val <= min_val:
        print("less than min", min_val)
        return False
    if max_val is not None and root_node.val > max_val:
        print("greater than max", max_val)
        return False


    l = root_node.left if root_node.left else EmptyTreeNode()
    r = root_node.right if root_node.right else EmptyTreeNode()

    return validate_bst(l, min_val, root_node.val) and validate_bst(r, root_node.val, max_val)

class TestValidateBst(unittest.TestCase):

    def setUp(self):
        self.f = validate_bst

    def test_1(self):
        t = BinSearchTree()
        self.assertTrue(self.f(t.root))

    def test_2(self):
        t = BinSearchTree(1, 2, 3, 4)
        self.assertTrue(self.f(t.root))

    def test_3(self):
        t = BinSearchTree(1)
        self.assertTrue(self.f(t.root))

    def test_4(self):
        t = MinHeap(1)
        self.assertTrue(self.f(t.root))

    def test_5(self):
        t = MinHeap(1, 2, 3, 4)
        self.assertFalse(self.f(t.root))

    def test_6(self):
        t = BinSearchTree(1)
        r = BinSearchTree(5)
        t.root.left = r.root
        self.assertFalse(self.f(t.root))

    def test_7(self):
        t = BinSearchTree(1)
        r = BinSearchTree(0)
        t.root.right = r.root
        self.assertFalse(self.f(t.root))

    def test_8(self):
        t = BinSearchTree(20, 10, 30)
        r = BinSearchTree(25)
        t.root.left.right = r.root
        self.assertFalse(self.f(t.root))

if __name__ == "__main__":
    unittest.main()