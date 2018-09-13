#!/usr/bin/python3
from code_interview.lists import Queue, Stack, EmptyNode
from code_interview.trees import AbstractBinTree, BinTreeNode, EmptyTreeNode
import unittest
from functools import wraps


class MinHeapTreeNode(BinTreeNode):

    def is_empty(self):
        return isinstance(self, EmptyTreeNode)
    
    def __init__(self, val, parent_node):
        self.parent = parent_node
        super().__init__(val)

class MinHeap(AbstractBinTree):

    def __init__(self, *args):
        self.next_parents = Queue()
        self.latest_leaves = Stack()
        self.last_leaf = None
        super().__init__(*args)

    def insert_single(self, val):
        def swap_fix_up(to_fix):
            while to_fix.parent is not None and to_fix.val < to_fix.parent.val:
                t = to_fix.val
                to_fix.val = to_fix.parent.val
                to_fix.parent.val = t
                to_fix = to_fix.parent

        next_parent = None if self.is_empty() else self.next_parents.pop().val
        next_node = MinHeapTreeNode(val, next_parent)
        
        if self.is_empty(): 
            self.root = next_node
        else:
            if next_parent.left is None:
                next_parent.left = next_node
            else:
                next_parent.right = next_node

        self.latest_leaves.push(next_node)
        self.next_parents.add(next_node, next_node)
        swap_fix_up(next_node)
            
    def trim_last_leaf(self):
        ll = self.latest_leaves.pop().val
        ll_p = ll.parent

        if ll_p is not None:
            if ll_p.left is ll:
                ll_p.left = None
            if ll_p.right is ll:
                ll_p.right = None
        return ll

    def extract_min(self):
        def swap_fix_down(start_node):
            n = start_node
            while True:
                parent_val = n.val
                branches = (n.left, n.right)
                children = []
                for b in branches:
                    if b is not None:
                        children.append(b)

                smallest_child = None

                local_min = parent_val
                for child in children:
                    if child.val < local_min:
                        smallest_child = child
                        local_min = child.val

                if smallest_child is None:
                    break

                n.val = smallest_child.val
                smallest_child.val = parent_val
                n = smallest_child

        if self.is_empty():
            return

        m = self.root.val
        last_leaf = self.trim_last_leaf()
        if last_leaf.parent is not None:
            self.root.val = last_leaf.val
            swap_fix_down(self.root)
        else:
            self.root = EmptyTreeNode()
        return m

    def __repr__(self):
        return "MinHeap" + repr(self.root)
