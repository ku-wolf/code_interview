#!/usr/bin/python3
from code_interview.lists import Queue, Stack, EmptyNode, LinkedList
import unittest
from functools import wraps

# TODO: make graphs a parent of trees (merge treecode and graph code)
# make graphnodes have children and 

def find_min_path_between(s1, s2):
    seen = {}
    for r1, r2 in zip(breadth_search_with_depth(s1), breadth_search_with_depth(s2)):
        n1, d1 = r1
        n2, d2 = r2

        if id(n1) in seen or n1 is n2:
            return d1 + d2

        seen.add(id(n1))
        seen.add(id(n2))


class GraphNode:

    def __init__(self, val):
        self.val = val
        self.children = []

    def add_edge(self, n):
        self.children.add(n)

    def __iter__(self):
        for e in self.children:
            yield e

    def __repr__(self):
        n = self
        ret = str(n.val) + ": "
        for e in n.edges:
            ret += str(e.val) + ", "
        ret.rstrip(", ")

        if not n.edges:
            ret += "no edges"
        ret += "\n"

        return ret
