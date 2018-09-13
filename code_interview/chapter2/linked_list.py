#!/usr/bin/python3
import unittest
from functools import wraps
from abc import ABC, abstractmethod

def update_head_and_tail(f):

    @wraps(f)
    def wrapper(self, *args, **kwargs):
        head, tail = f(self, *args, **kwargs)
        if head is not None:
            self.head = head
        if tail is not None:
            self.tail = tail

    return wrapper


class NodeObjectBase(ABC):

    def __init__(self, *args):
        self.head = self.tail = EmptyNode()
        for a in args:
            self.init_adder(a)

    @abstractmethod
    def __repr__(self):
        return "NodeObjectBase" + repr(self.head)

    @abstractmethod
    def init_adder(self):
        pass

    def pop(self):
        if self.head.is_empty():
            return
        old_head = self.head
        self.head = self.head.next        
        if self.head is None:
            self.head = self.tail = EmptyNode()
        return old_head

    def peek(self):
        return self.head

    def __iter__(self):
        return iter(self.head)

    def iter_nodes(self, i=None):
        return self.head.iter_nodes(i)

    def __eq__(self, other):
        try:
            return self.head.__eq__(other.head)
        except AttributeError:
            return self.head.__eq__(other)
        except:
            return False

    def get(self, i):
        return self.head.get(i)

    def is_empty(self):
        return self.head.is_empty()

    def iter_pop(self, i=None):
        for n in self.iter_nodes(i):
            yield n
            self.pop()


class Stack(NodeObjectBase):

    def __repr__(self):
        return "Stack" + repr(self.head)

    def init_adder(self, v):
        self.push(v)

    @update_head_and_tail
    def push(self, val):
        head = Node(val)
        tail = None
        if self.is_empty():
            tail = head
        else:
            head.next = self.head

        return head, tail



class Queue(NodeObjectBase):

    def __repr__(self):
        return "Queue" + repr(self.head)

    def init_adder(self, v):
        self.add(v)

    @update_head_and_tail
    def add(self, val):
        head = None
        tail = Node(val)
        if self.is_empty():
            head = tail
        else:
            self.tail.next = tail
        return head, tail

class MinStack(Stack):

    def __init__(self, *args, **kwargs):
        self.min = Stack()
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return "MinStack" + repr(self.head)

    def push(self, val):
        m = self.peek_min()
        if m is None or val < m:
            self.min.push([val, 1])
        if val == m:
            try:
                self.min.peek().val[1] += 1
            except AttributeError:
                pass
        super().push(val)

    def pop(self):
        if self.peek().val == self.peek_min():
            try:
                self.min.head.val[1] -= 1
                if self.min.head.val[1] <= 0:
                    self.min.pop()
            except TypeError:
                pass
        super().pop()

    def peek_min(self):
        try:
            return self.min.peek().val[0]
        except TypeError:
            return None

class StackQueue():
    def __repr__(self):
        return "StackQueue" + repr(self.stack_2.head)

    def __init__(self, *args):
        self.stack_1 = Stack(*args)
        self.stack_2 = Stack()

        n = self.stack_1.pop()
        while n is not None:
            self.stack_2.push(n.val)
            n = self.stack_1.pop()

    def is_empty(self):
        return self.stack_2.is_empty()

    def add(self, v):
        n = self.stack_2.pop()
        while n is not None:
            self.stack_1.push(n.val)
            n = self.stack_2.pop()


        self.stack_1.push(v)

        n = self.stack_1.pop()
        while n is not None:
            self.stack_2.push(n.val)
            n = self.stack_1.pop()

    def pop(self):
        return self.stack_2.pop()

    def peek(self):
        return self.stack_2.peek()



class LinkedList(Queue, Stack):

    def __repr__(self):
        return "LinkedList" + repr(self.head)

    @update_head_and_tail
    def delete(self, val):
        head = None
        tail = None

        prev = None
        to_delete = None
        for n in self.iter_nodes():
            if n.val == val:
                to_delete = n
                break
            prev = n

        if to_delete is not None:
            if prev is None:
                head = to_delete.next if to_delete.next is not None else EmptyNode()
            else:
                prev.next = to_delete.next

            if to_delete.next is None:
                tail = prev if prev is not None else EmptyNode()


        return head, tail


class Node:

    def is_empty(self):
        return isinstance(self, EmptyNode)
    
    def __init__(self, val):
        self.val = val
        self.next = None

    def iter_nodes(self, i=None):
        def gen_next():
            if not self.is_empty():
                head = self
                index = 0
                while head.next is not None and (i is None or index <= i):
                    n = head.next
                    yield head
                    head = n
                    index += 1
                if (i is None or index <= i):
                    yield head

        return gen_next()

    def get(self, i):
        n = None
        for node in self.iter_nodes(i):
            n = node
        return n

    def __len__(self):
        l = 0
        for i in self:
            l += 1
        return l

    def __iter__(self):
        for n in self.iter_nodes():
            yield n.val

    def __repr__(self):
        seen = {}
        ret = "["
        index = 0
        for n in self.iter_nodes():
            if id(n) in seen:
                ret += "loop to index " + str(seen[id(n)]) + " " + str(n.val)
                break
            else:
                seen[id(n)] = index
                ret += str(n.val) + ", "
            index += 1

        return ret.rstrip(", ") + "]"

    def __eq__(self, other):
        try:
            if isinstance(other, EmptyNode):
                return False

            if self.val == other.val and self.next == other.next:
                return True
        except AttributeError:
            try:
                return self == other.head
            except AttributeError:
                return False
        except:
            return False


class EmptyNode(Node):
    instance = None

    def __new__(cls, *args):
        if cls.instance:
            return cls.instance
        else:
            return super().__new__(cls, *args)

    def __init__(self):
        self.val = None
        self.next = None

    def __repr__(self):
        return "[EmptyNode]"

    def __eq__(self, other):
        if isinstance(other, EmptyNode):
            return True
        return False




class TestLLInit(unittest.TestCase):

    def test_init_empty(self):
        l = LinkedList()
        e = EmptyNode()
        self.assertEqual(l.head, e)
        self.assertEqual(l.tail, e)

    def test_init_single(self):
        l = LinkedList(1)
        self.assertEqual(l.head, l.tail)
        self.assertEqual(l.head, l.tail, Node(1))

    def test_init_more(self):
        l = LinkedList(1, 2, 3, 4)
        self.assertEqual(l.head, LinkedList(1, 2, 3, 4))
        self.assertEqual(l.tail, Node(4))

class TestLLEq(unittest.TestCase):

    def test_eq(self):
        l = LinkedList()
        l2 = LinkedList()
        self.assertTrue(l == l2)
        l2.add(1)
        self.assertFalse(l == l2)
        l.push(1)
        self.assertTrue(l == l2)
        l.push(2)
        self.assertFalse(l == l2)
        l2.push(2)
        self.assertTrue(l == l2)
        self.assertFalse(1 == l2)
        self.assertFalse("jake" == l2)

if __name__ == "__main__":
    unittest.main()