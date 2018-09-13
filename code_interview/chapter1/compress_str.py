#!/usr/bin/python3
import unittest

def compress_str(s):
    current_char = ""
    count = 0
    result = ""
    for c in s:
        if c == current_char:
            count += 1
        else:
            if count > 0:
                result += current_char + str(count)
            current_char = c
            count = 1
    result += current_char + str(count)
    if len(result) >= len(s):
        return s
    return result


def compress_str_list(s, force=False):
    count = 1
    result = []
    for i in range(len(s)):
        c = s[i]
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            result.append(s[i])
            result.append(str(count))
            if len(result) >= len(s) and not force:
                return s
            count = 1
        else:
            count += 1
    if len(result) >= len(s) and not force:
        return s
    return "".join(result)


def get_compressed_size(s):
    compr_size = 0
    for i in range(len(s)):
        c = s[i]
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compr_size += 2
    return compr_size


def compress_str_space_efficient(s):
    l = get_compressed_size(s)
    if l >= len(s):
        return s
    else:
        return compress_str_list(s, force=True)



class TestCompressString(unittest.TestCase):

    def setUp(self):
        self.f = compress_str_list

    def test_1(self):
        self.assertEqual(self.f(""), "")

    def test_2(self):
        self.assertEqual(self.f("a"), "a")

    def test_3(self):
        self.assertEqual(self.f("ab"), "ab")

    def test_4(self):
        self.assertEqual(self.f("aab"), "aab")

    def test_5(self):
        self.assertEqual(self.f("aaab"), "aaab")

    def test_6(self):
        self.assertEqual(self.f("aaaab"), "a4b1")

    def test_7(self):
        self.assertEqual(self.f("abbbb"), "a1b4")

    def test_8(self):
        self.assertEqual(self.f("aabcccccaaa"), "a2b1c5a3")


class TestCompressStringSpaceEfficient(TestCompressString):

    def setUp(self):
        self.f = compress_str_space_efficient


if __name__ == "__main__":
    unittest.main()