#!/usr/bin/python3
from code_interview.lists import Queue, Stack, EmptyNode
import unittest
from functools import wraps
from abc import ABC, abstractmethod

def depth_search(node, seen=None):
    if seen is None:
        seen = set()
    yield n
    for c in n:
        if id(c) not in seen and c is not None:
            yield c
            seen.add(id(c))
            yield from depth_search(c, seen)

def breadth_search(node):
    explored = set()
    to_explore_next = Queue()
    to_explore_next.add(node)
    while not to_explore_next.is_empty():
        n = to_explore_next.pop().val
        if id(n) not in explored:
            yield n
            for child in n:
                if child is not None:
                    to_explore_next.add(child)
            explored.add(id(n))

def breadth_search_with_depth(node):
    explored = set()
    to_explore_next = Queue()
    to_explore_next.add((node, 0))
    while not to_explore_next.is_empty():
        n, depth = to_explore_next.pop().val
        if id(n) not in explored:
            yield n, depth
            for child in n:
                if child is not None:
                    to_explore_next.add((child, depth + 1))
            explored.add(id(n))


class TreeNode(ABC):

    class Child:
        def __get__(self, instance, owner):
            return instance.__dict__["children"][self.index]

        def __set__(self, instance, value):
            instance.__dict__["children"][self.index] = value

        def __init__(self, index):
            self.index = index


    def is_empty(self):
        return isinstance(self, EmptyTreeNode)
    

    @abstractmethod
    def __init__(self, val, max_children):
        self.val = val
        self.max_children = max_children
        self.children = [None]*max_children
        self.children_descriptors = 0

    def __iter__(self, i=None):
        for c in self.children:
                yield c

    def __repr__(self):
        ret = "["
        index = 0

        ret += str(self.val) + ": "
        for n in self:
            ret += str(n) + ", "
            index += 1

        return ret.rstrip(", ").rstrip(": ") + "]"

    def __eq__(self, other):
        try:
            if isinstance(other, EmptyTreeNode):
                return False

            if self.val == other.val and self.children == other.children:
                return True

        except AttributeError:
            try:
                return self == other.root
            except AttributeError:
                return False
        except:
            return False


class EmptyTreeNode(EmptyNode):
    def __init__(self):
        self.val = None
        self.children = None

    def __repr__(self):
        return "[EmptyTreeNode]"


class AbstractBinTree(ABC):

    def __init__(self, *args):
        self.root = EmptyTreeNode()
        for a in args:
            self.insert(a)
    
    def is_empty(self):
        return self.root.is_empty()

    def insert(self, *vals):
        for v in vals:
            self.insert_single(v)

    @abstractmethod
    def insert_single(self, val):
        pass

    def __repr__(self):
        return type(self).__name__ + repr(self.root)

    def __iter__(self):
        return iter(self.root)

    

class BinTreeNode(TreeNode):
    left = TreeNode.Child(0)
    right = TreeNode.Child(1)

    def __init__(self, val):
        super().__init__(val, 2)

    def add_child(self, val):
        if val < self.val:
            if self.left is not None:
                self.left.add_child(val)
            else:
                self.left = BinTreeNode(val)
        else:
            if self.right is not None:
                self.right.add_child(val)
            else:
                self.right = BinTreeNode(val)


class BinSearchTree(AbstractBinTree):
    
    def insert_single(self, val):
        if self.is_empty():
            self.root = BinTreeNode(val)
        else:
            self.root.add_child(val)








