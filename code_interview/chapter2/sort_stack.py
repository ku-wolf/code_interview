#!/usr/bin/python3

from linked_list import Stack
import unittest

def sort_stack(s):
    sort = Stack()
    while not s.is_empty():
        top_node = s.pop()
        if sort.is_empty() or sort.peek().val >= top_node.val:
            sort.push(top_node.val)

        else:
            while (not sort.is_empty()) and sort.peek().val < top_node.val:
                n = sort.pop()
                s.push(n.val)
            sort.push(top_node.val)
    s.head = sort.head
    s.tail = sort.tail