#!/usr/bin/python3
import unittest

def brute_force_flip_bit(bin_num):
    longest_run = 0
    index = i

    def find_longest_run_of(bin_num, digit):
        longest_run = 0
        run_size = 0
        for b in bin_num:
            if b == "1":
                run_size += 1
            else:
                if run_size > longest_run:
                    longest_run = run_size
                run_size = 0

    for i in range(len(bin_num)):
        if bin_num[i] == "0":
            bin_num[i] = "1"
            r = find_longest_run_of(bin_num, "1")
            if r > longest_run:
                longest_run = r
                index = i
            bin_num[i] = "0"


    return longest_run, index

def flip_bit_to_win(bin_num):
    if bin_num < 0:
        return 0, None

    n = bin(bin_num)[2:]
    print(n)

    has_zero = False
    longest_run_size = 0
    current_ones = 0
    prev_ones = 0
    last_zero_index = None
    flip_index = None

    def set_max_run():
        nonlocal current_ones, prev_ones, longest_run_size, flip_index, last_zero_index
        run_size = current_ones + prev_ones + 1
        if run_size > longest_run_size:
            longest_run_size = run_size
            flip_index = last_zero_index

    for bit, i in zip(n, range(len(n))):
        print(bit, i)
        if bit == "1":
            current_ones += 1

        elif bit == "0":
            has_zero = True
            last_zero_index = i
            set_max_run()
            try:
                next_char = n[i + 1]
            except IndexError:
                next_char = ""

            if next_char == "1":
                prev_ones = current_ones
                current_ones = 0
            else:
                current_ones = 0
                prev_ones = 0
        else:
            raise ValueError("Malformed Binary String")

    if has_zero:
        set_max_run()
    return longest_run_size, flip_index


class TestFlipBit(unittest.TestCase):

    def setUp(self):
        self.f = flip_bit_to_win

    def test_1(self):
        tests = [
            (0, (1, 0)),
            (1, (0, None)),
            (9, (2, 1)),
            (4, (2, 1)),
            (int("111011101111", 2), (8, 7)),
            (int("11100111110", 2), (6, 10))
        ]

        for t,e in tests:
            self.assertEqual(self.f(t), e, t)

                
if __name__ == "__main__":
    unittest.main()