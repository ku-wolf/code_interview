#!/usr/bin/python3
from collections import deque
from code_interview.lists import LinkedList
from code_interview.trees import EmptyTreeNode, BinSearchTree
import unittest


#TODO Finish
def paths_with_sum(bst, target_sum)
    paths_with_sum_acc(bst, target_sum, target_sum)

def paths_with_sum_acc(bst, so_far, original_sum):
    if bst.is_empty():
        return 0

    l = bst.left if bst.left else EmptyTreeNode()
    r = bst.right if bst.right else EmptyTreeNode()

    ret = 0
    sum_left = target_sum - bst.val



    if sum_left == 0:
        ret += 1



    return ret

class TestPathsWithSum(unittest.TestCase):

    def setUp(self):
        self.f = bst_sequences

    def general_test(self, bst=None):
        if bst is not None:
            result = self.f(bst.root)
            print(result)
            for r in result:
                l = BinSearchTree()
                for v in r:
                    l.insert(v)

                if l.root != bst.root:
                    self.fail(bst, r)

            if len(set(result)) != len(result):
                self.fail("repeats")

    def test_1(self):
        bst = BinSearchTree(3, 5, 1)
        self.general_test(bst)

    def test_2(self):
        bst = BinSearchTree(50, 20, 60, 10, 25, 5, 15, 65, 80)
        self.general_test(bst)

    def test_3(self):
        bst = BinSearchTree(1)
        self.general_test(bst)
                
if __name__ == "__main__":
    unittest.main()