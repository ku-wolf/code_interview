#!/usr/bin/python3
# Generate file with N number of random integers (excluding a random int)
import random
import os

def generate_int_file(fname="test", number_of_ints = 4 * 10 ** 9):
    lower = 0
    upper = 2 ** 31 - 1
    exclude = random.randint(lower, upper)
    ranges = [(lower, exclude - 1), (exclude + 1, upper)]

    with open(fname, "w") as f:
        for i in range(number_of_ints):
            r = random.randint(0, 1)
            current_range = ranges[r]
            r = random.randint(*current_range)
            f.writelines([str(r)])
            if i % 10 ** 6 == 0:
                print(i // 10 ** 6, "mil ints:", os.path.getsize(fname) // 10 ** 6)

    return exclude


if __name__ == "__main__":
    excluded = generate_int_file(number_of_ints = 4 * 10 ** 7)
    print(excluded)
