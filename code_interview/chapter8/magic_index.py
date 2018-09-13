#!/usr/bin/python3
import unittest

# assume array sorted in ascending order

def magic_index(arr):
    return magic_index_helper(arr, 0, len(arr) - 1)

def magic_index_helper(arr, start, end):
    if end < start or start > end:
        return None

    mid = start + (end - start + 1) // 2 

    i = arr[mid]
    if i == mid:
        return mid
    elif i < mid:
        return magic_index_helper(arr, mid + 1, end)
    else:
        return magic_index_helper(arr, start, mid - 1)

class TestMagicIndex(unittest.TestCase):

    def setUp(self):
        self.f = magic_index

    def test_1(self):
        tests = [
            ([], None),
            ([1], None),
            ([1, 2, 3, 4], None),
            ([0, 3, 5, 6], 0),
            ([0, 1, 3, 5, 6], 1),
            ([-1, 0, 2, 4, 5], 2),
            ([-1, 0, 1, 3, 5], 3),
            ([-2, -1, 1, 2, 4], 4),
            ([0, 10, 20, 24, 25], 0),
        ]

        for t,e in tests:
            self.assertEqual(self.f(t), e, t)

                
if __name__ == "__main__":
    unittest.main()