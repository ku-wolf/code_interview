#!/usr/bin/python3
import unittest
import math
import random
from collections import deque
import copy
from PIL import Image

def surrounding_pixels(x, y, w, h):
    lx = rx = x
    if x > 0:
        lx = x - 1
    if x < w:
        rx = x + 1

    x_range = (lx, rx + 1)

    ty = by = y
    if y > 0:
        ty = y - 1
    if y < h:
        by = y + 1

    y_range = (ty, by + 1)


    for x1 in range(*x_range):
        for y1 in range(*y_range):
            if x1 != x or y1 != y:
                yield (x1, y1)


def paint_fill(screen, sx, sy, new_col):
    print("filling {0}, {1} with {2}".format(sx, sy, new_col))
    if screen:
        width = len(screen[0]) - 1
        height = len(screen) - 1
        start_col = screen[sy][sx]
        print("start color is {0}".format(start_col))
        to_visit_next = deque()
        visited = set()

        to_visit_next.append((sx, sy))
        visited.add((sx, sy))

        while to_visit_next:
            nx, ny = to_visit_next.popleft()
            for x, y in surrounding_pixels(nx, ny, width, height):
                if screen[y][x] == start_col and (x, y) not in visited:
                    to_visit_next.append((x, y))
                    visited.add((x, y))
            screen[ny][nx] = new_col


def path_from(screen, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    col = screen[y1][x1]
    width = len(screen[0]) - 1
    height = len(screen) - 1
    to_visit_next = deque()
    visited = set()

    to_visit_next.append((x1, y1))
    visited.add((x1, y1))

    while to_visit_next:
        nx, ny = to_visit_next.popleft()
        if nx == x2 and ny == y2:
            return True

        for x, y in surrounding_pixels(nx, ny, width, height):
            if (x, y) not in visited and screen[y][x] == col:
                to_visit_next.append((x, y))
                visited.add((x, y))

    return False


def draw_line(screen, x1, x2, y, col):
    bx = max(x1, x2)
    sx = min(x1, x2)

    for i in range(sx, bx + 1):
            screen[y][i] = col


def print_screen(s):
    for w in s:
        print(w)

class TestPaintFill(unittest.TestCase):

    def setUp(self):
        self.f = paint_fill

    def create_blank_screen(self, w, h):
        return [["000000" for _ in range(w)] for _ in range(h)]

    def generic_test(self, screen=None, sx=None, sy=None):
        if screen is not None:
            red_col = "0000FF"
            before_screen = copy.deepcopy(screen)
            print_screen(before_screen)
            print()
            paint_fill(screen, sx, sy, red_col)


            height = len(screen)
            width = len(screen[0])
            print_screen(screen)
            print()

            for i in range(width):
                for j in range(height):
                    if screen[j][i] != before_screen[j][i]:
                        self.assertEqual(before_screen[j][i], before_screen[sy][sx])
                        self.assertTrue(path_from(before_screen, (i, j), (sx, sy)))

    def test_1(self):
        w = h = 8
        col = "FF0000"
        screen = self.create_blank_screen(w, h)
        for x in range(w // 2):
            for y in range(h):
                new_screen = copy.deepcopy(screen)
                print(x, "to", w - x - 1, "at", y)
                draw_line(new_screen, x, w - x - 1, y, col)
                for fx in range(w):
                    for fy in range(x):
                        self.generic_test(new_screen, fx, fy)



if __name__ == "__main__":
    unittest.main()