#!/usr/bin/python3
from collections import deque
from code_interview.lists import LinkedList
from code_interview.trees import EmptyTreeNode, BinSearchTree
import unittest

def bst_sequences(bst):
    if bst.is_empty():
        return [[]]

    l = bst.left if bst.left else EmptyTreeNode()
    r = bst.right if bst.right else EmptyTreeNode()

    l_sequences = bst_sequences(l)
    r_sequences = bst_sequences(r)

    ret = []
    for l_seq in l_sequences:
        for r_seq in r_sequences:
            e =  build_sequences([bst.val], l_seq, r_seq)
            for v in e:
                ret.append(tuple(v))

    return ret

def build_sequences(so_far, l_seq, r_seq):
    if not l_seq and not r_seq:
        return [so_far]

    l = r = []
    if l_seq:
        n = l_seq[0]
        new_l_seq = []
        if len(l_seq) > 1:
            for i in range(1, len(l_seq)):
                new_l_seq.append(l_seq[i])

        new_so_far = []
        for v in so_far:
            new_so_far.append(v)
        new_so_far.append(n)
        l = build_sequences(new_so_far, new_l_seq, r_seq)

    if r_seq:
        n = r_seq[0]
        new_r_seq = []
        if len(r_seq) > 1:
            for i in range(1, len(r_seq)):
                new_r_seq.append(r_seq[i])

        new_so_far = []
        for v in so_far:
            new_so_far.append(v)
        new_so_far.append(n)
        r = build_sequences(new_so_far, l_seq, new_r_seq)

    ret = []
    if l:
        for v in l:
            ret.append(v)
    if r:
        for v in r:
            ret.append(v)

    return ret

class TestBSTSequences(unittest.TestCase):

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