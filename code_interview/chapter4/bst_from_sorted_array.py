#!/usr/bin/python3
from code_interview.trees import BinSearchTree
def bst_from_sorted_array(a):
    if not a:
        return BinSearchTree()
    else:
        b = BinSearchTree()
        mid = (len(a) - 1) // 2

        b.insert(a[mid])

        result_left = bst_from_sorted_array(a[0:mid]).root
        result_right = bst_from_sorted_array(a[mid + 1:]).root

        if result_left.is_empty():
            result_left = None
        if result_right.is_empty():
            result_right = None


        b.root.left = result_left
        b.root.right = result_right
    return b