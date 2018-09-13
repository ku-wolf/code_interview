#!/usr/bin/python3
import unittest

error_val = "ERROR"
def binary_to_string(num):
    a = []
    for s in binary_to_string_gen(num):
        a.append(s)
        if s == error_val:
            return s

    return "".join(a)


#TODO Finish
def binary_to_string_gen(num):
    digits = 0
    if num <= 0 or num >= 1:
        yield error_val
    else:
        while num != 0:
            if digits >= 32:
                yield "ERROR"
                
            num *= 2
            if num >= 1:
                num -= 1
                yield "1"
            else:
                yield "0"
            digits += 1


class TestBinaryToString(unittest.TestCase):

    def setUp(self):
        self.f = binary_to_string

    def test_1(self):
        tests = [0, 1, 4000, (1 / 2) ** 33]
        for t in tests:
            self.assertEqual(self.f(t), "ERROR", t)
        
    def test_2(self):

        tests = [
            (0.5, "1"),
            (0.25, "01"),
            (0.75, "11"),
            (0.0625, "0001"),
            ((1 / 2) ** 32, "0" * 31 + "1"),
        ]

        for t,e in tests:
            self.assertEqual(self.f(t), e, t)

                
if __name__ == "__main__":
    unittest.main()