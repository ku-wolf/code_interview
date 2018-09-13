#!/usr/bin/python3
import unittest
import copy
from code_interview.chapter5.bin_gen import convert_to_bin_str
import random

B_SIZE = 8

def set_i_to_end(i, b=0):
    return b | (2 ** B_SIZE - 1 >> i) & 2 ** 8 - 1

def set_up_to_i(i, b):
    return b | (2 ** B_SIZE - 1 << (7 - i)) & 2 ** 8 - 1

def clear_i_to_end(i, b):
    return b & (2 ** B_SIZE - 1 << (B_SIZE - i)) & 2 ** 8 - 1

def draw_line(screen, width, x1, x2, y, p_screen=False):
    lx = min(x1, x2)
    rx = max(x1, x2)

    b_width = width // B_SIZE
    if len(screen) % b_width:
        raise ValueError("Incomplete screen. Expected screen length to be a multiple of {0}".format(b_width))
    h = len(screen) // b_width
    start_index = b_width * y

    lx_b_index = start_index + lx // B_SIZE
    rx_b_index = start_index + rx // B_SIZE

    lx_p_num = lx % B_SIZE
    rx_p_num = rx % B_SIZE 


    if lx_b_index == rx_b_index:
        b = screen[lx_b_index]
        mask = clear_i_to_end(rx_p_num + 1, set_i_to_end(lx_p_num))
        #print("Oring byte {0} with mask {1}".format(bin(b), bin(mask)))
        screen[lx_b_index] = b | mask
    else:
        screen[lx_b_index] = set_i_to_end(lx_p_num, screen[lx_b_index])
        screen[rx_b_index] = set_up_to_i(rx_p_num, screen[rx_b_index])

        for i in range(lx_b_index + 1, rx_b_index):
            screen[i] |= 2 ** B_SIZE - 1

    if p_screen:
        #print("Line from {0} to {1} at height {2}".format(x1, x2, y))
        #print("Width is {0}. Total screen height is {1}".format(width, h))
        print_screen(screen, width)

    return screen

def print_screen(screen, w):
    b_width = w // B_SIZE
    b_in_row = 0
    for b in screen:
        #print(convert_to_bin_str(b, B_SIZE), end="")
        b_in_row += 1
        if b_in_row == b_width:
            b_in_row = 0
            #print()

class TestDrawLine(unittest.TestCase):

    def setUp(self):
        self.f = draw_line

    def gen_random_byte(self):
        return random.randint(0, 2 ** B_SIZE - 1)

    def gen_random_screen(self, w=None, h=None):
        if w is not None and h is not None:
            w *= 8
            s = []
            bs_per_row = w // B_SIZE
            for i in range(bs_per_row * h):
                s.append(self.gen_random_byte())

            return s, w

    def test_and_verify(self, input_tuple=None):
        #print("t and v", input_tuple)
        if input_tuple is not None:
            s, w, x1, x2, y = input_tuple
            s = copy.deepcopy(s)
            #print(s)
            print_screen(s, w)

            result = self.f(*input_tuple, p_screen=True)

            b_width = w // B_SIZE
            start_row = (b_width * y * 8)

            lx = min(x1, x2)
            rx = max(x1, x2)

            start_bit = (b_width * y * 8) + lx
            end_bit = (b_width * y * 8) + rx

            #print("start bit {0}, end bit {1}".format(start_bit, end_bit))


            for b1, b2, i in zip(result, s, range(len(s))):
                #print(b1, b2, i)
                b1 = convert_to_bin_str(b1, B_SIZE)
                b2 = convert_to_bin_str(b2, B_SIZE)
                for bit1, bit2, j in zip(b1, b2, range(w)):
                    index = i * 8 + j
                    #print(bit1, bit2, index)
                    if index >= start_bit and index <= end_bit:
                        self.assertEqual(bit1, "1")
                    else:
                        self.assertEqual(bit1, bit2)
                #print()

    def main_test(self):
        for w in range(1, 10):
            print(w)
            for h in range(1, 10):
                for y in range(h):
                    for x1 in range(w * 8):
                        for x2 in range(x1, w * 8):
                            s, width = self.gen_random_screen(w, h)
                            self.test_and_verify((s, width, x1, x2, y))


if __name__ == "__main__":
    t = TestDrawLine()
    t.setUp()
    t.main_test()