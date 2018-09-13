#!/usr/bin/python3
import unittest
import random
import math
from collections import deque

def swap_in_place(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp


def bfs_heap(l):
    if not l:
        return

    to_visit = deque([0])
    visited = set()

    while to_visit:
        el = to_visit.popleft()
        yield l[el]
        visited.add(el)

        l_index = 2 * el + 1
        r_index = 2 * el + 2
        for i in (l_index, r_index):
            if i < len(l) and i not in visited:
                to_visit.append(i)


def digits_of(n):
    if n == 0:
        return 1
    return math.floor(math.log(abs(n), 10)) + 1

def print_tree(l):
    layer = 0
    els_at_layer = 0
    expected_els_at_layer = 1
    for el in bfs_heap(l):
        print(el, end=" ")
        els_at_layer += 1
        if els_at_layer == expected_els_at_layer:
            els_at_layer = 0
            layer += 1
            expected_els_at_layer = 2 ** layer
            print()

def print_tree_list(l):
    if not l:
        print("Empty.")
        return

    m = max(l)
    max_digits = digits_of(m)
    print("max", m)
    print("max digits", max_digits)
    def print_el(el):
        return str(el) + " " * (max_digits - digits_of(el))

    h = int(math.floor(math.log(len(l), 2)) + 1)
    if h == 1:
        print(l[0])
    else:
        # determine width
        width = ((2 * max_digits) + 1) * (2 ** (h - 2))
        print("just leaves", width)
        for i in range(3, h + 1):
            width += (2 ** (h - i)) * max_digits
            print("plus upper", width)
        

        print("width", width)

        # print tree
        layer = 0
        els_at_layer = 0
        expected_els_at_layer = 1
        line = ""
        sep = (width - max_digits) // 2
        for el in bfs_heap(l):
            if layer == h - 1:
                line += print_el(el) + "M" * max_digits
            else:
                line += "|" * sep + print_el(el) + "|" * sep + "M" * max_digits

            els_at_layer += 1
            if els_at_layer == expected_els_at_layer:
                print(line)

                line = ""
                els_at_layer = 0
                layer += 1
                expected_els_at_layer = 2 ** layer
                sep = (sep - max_digits) // 2
                if sep < max_digits:
                    sep = max_digits
        print(line)


def max_heapify(l, root):
    l_child = (2 * root) + 1
    r_child = (2 * root) + 2
    l_val = None
    r_val = None


    try:
        l_val = l[l_child]
    except IndexError:
        pass

    try:
        r_val = l[r_child]
    except IndexError:
        pass

    if l_val is None and r_val is None:
        return
    elif l_val is None or (r_val is not None and r_val > l_val):
        if r_val > l[root]:
            swap_in_place(l, root, r_child)
            max_heapify(l, r_child)
    else:
        if l_val > l[root]:
            swap_in_place(l, root, l_child)
            max_heapify(l, l_child)


def heapify_in_place(l):
    if not l or len(l) == 1:
        return 

    for i in range(len(l)):
        if 2 * i + 1 == len(l) - 1 or 2 * i + 2 == len(l) - 1:
            first_non_leaf = i

    for i in range(first_non_leaf, -1, -1):
        max_heapify(l, i)


def extract_max(l):
    if not l:
        return None

    max_el = l[0]

    if len(l) == 1:
        del l[0]
    else:
        last_leaf = l[-1]
        l[0] = last_leaf
        del l[-1]
        max_heapify(l, 0)

    return max_el

def bubble_sort(l, op=lambda x, y: x > y):
    switched = True
    while switched:
        switched = False
        for i in range(len(l) - 1):
            if op(l[i], l[i + 1]):
                swap_in_place(l, i, i + 1)
                switched = True


def selection_sort(l, op=lambda x, y: x > y):
    for start in range(len(l)):
        smallest = None
        index = None
        for i in range(start, len(l)):
            if smallest is None:
                smallest = l[i]
                index = i
            elif op(smallest, l[i]):
                smallest = l[i]
                index = i

        swap_in_place(l, start, index)


def merge_sort(l, op=lambda x, y: x < y, low=0, high=None):
    if high is None:
        high = len(l) - 1

    if low >= high:
        return

    midpoint = (low + high) // 2

    merge_sort(l, op, low, midpoint)
    merge_sort(l, op, midpoint + 1, high)
    
    merge(l, op, low, midpoint, midpoint + 1, high)


def merge(l, op, l1, h1, l2, h2):
    cop = list(l)

    i = l1
    j = l1
    k = l2
    while j <= h1 and k <= h2:
        if op(cop[j], cop[k]):
            l[i] = cop[j]
            j += 1
        else:
            l[i] = cop[k]
            k += 1
        i += 1

    for a in range(j, h1 + 1):
        l[i] = cop[a]
        i += 1

    for a in range(k, h2 + 1):
        l[i] = cop[a]
        i += 1

def quick_sort(l, op=lambda x, y: x < y, low=0, high=None):
    if high is None:
        high = len(l) - 1

    if low >= high:
        return

    pivot = random.randint(low, high)
    pivot_val = l[pivot]
    i = low
    j = high
    while i < j:
        if op(l[i], pivot_val) and not op(l[j], pivot_val):
            i += 1
            j -= 1
            continue

        if op(l[i], pivot_val):
            i += 1
        elif not op(l[j], pivot_val):
            j -= 1
        elif not op(l[i], pivot_val) and op(l[j], pivot_val):
            swap_in_place(l, i, j)

    quick_sort(l, op, low, j)
    quick_sort(l, op, j + 1, high)


def heap_sort(l):
    heap = heapify_in_place(l)
    heap_copy = list(l)
    for i in range(len(l) - 1, -1, -1):
        l[i] = extract_max(heap_copy)


class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.f = bubble_sort

    def test_1(self):
        tests = [
            #[],
            #[1],
            #[1, 2],
            [5, 4, 0, 2, 3, 4, 5, 1, 100000, 300, 20, 0, -1, -400, 4000000, 1, 2, 8]
        ]

        for t in tests:
            t2 = list(t)
            t2.sort()
            self.f(t)
            self.assertEqual(t, t2)

class TestSelectionSort(TestBubbleSort):

    def setUp(self):
        self.f = selection_sort


class TestMergeSort(TestBubbleSort):

    def setUp(self):
        self.f = merge_sort

class TestQuickSort(TestBubbleSort):

    def setUp(self):
        self.f = merge_sort

class TestHeapSort(TestBubbleSort):

    def setUp(self):
        self.f = heap_sort
                
if __name__ == "__main__":
    unittest.main()