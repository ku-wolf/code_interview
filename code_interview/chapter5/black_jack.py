#!/usr/bin/python3
import unittest
import copy
from code_interview.chapter5.bin_gen import convert_to_bin_str
import random

class Card:

    suits = set(["spades", "hearts", "clubs", "diamonds"])
    values = set([i for i in range(1, 14)])
    names = {11: "jack", 12: "queen", 13: "king"}

    def __init__(self, value, suit):
        if value in self.values:
            self.value = value
        else:
            raise ValueError("Invalid Card Value {0}".format(value))
        if suit in self.suits:
            self.suit = suit
        else:
            raise ValueError("Invalid Suit {0}".format(suit))

    def __str__(self):
        try:
            val = Card.names[self.value]
        except KeyError:
            val = str(self.value)
        return "{0} of {1}".format(val, self.suit)


class 

    

class TestBlackJack(unittest.TestCase):

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