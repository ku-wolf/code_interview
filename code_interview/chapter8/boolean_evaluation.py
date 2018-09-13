#!/usr/bin/python3
import unittest

def boolean_evaluation(exp, val, memo=None):
    if memo is None:
        memo = {}

    if exp == "":
        return 0

    if exp == "0" or exp == "1":
        return 1 if bool(int(exp)) == bool(val) else 0

    if exp in memo:
        return memo[exp]

    ways = 0
    l_exp = ""
    r_exp = ""
    result = 0
    for i in range(0, len(exp) - 2, 2):
        if i > 0:
            l_exp += exp[i - 1]
        l_exp += exp[i]
        r_exp = exp[i + 2:]
        hinge_op = exp[i + 1]



        if (l_exp, True) not in memo:
            memo[(l_exp, True)] = boolean_evaluation(l_exp, True)

        if (l_exp, False) not in memo:
            memo[(l_exp, False)] = boolean_evaluation(l_exp, False)

        if (r_exp, True) not in memo:
            memo[(r_exp, True)] = boolean_evaluation(r_exp, True)

        if (r_exp, False) not in memo:
            memo[(r_exp, False)] = boolean_evaluation(r_exp, False)

        ltrue = memo[(l_exp, True)]
        lfalse = memo[(l_exp, False)]
        rtrue = memo[(r_exp, True)]
        rfalse = memo[(r_exp, False)]


        total_ways = (ltrue + lfalse) * (rtrue + rfalse)
        true_ways = 0
        if hinge_op == "&":
            true_ways += ltrue * rtrue

        if hinge_op == "|":
            true_ways += ltrue * rtrue
            true_ways += ltrue * rfalse
            true_ways += lfalse * rtrue

        if hinge_op == "^":
            true_ways += ltrue * rfalse
            true_ways += lfalse * rtrue

        result += true_ways if bool(val) else total_ways - true_ways
    memo[(exp, bool(val))] = result
    return result


def generate_parened(exp):
    if exp == "":
        yield ""
    if exp == "0":
        yield "(0)"
    elif exp == "1":
        yield "(1)"


    l_exp = ""
    r_exp = ""
    for i in range(0, len(exp) - 2, 2):
        if i > 0:
            l_exp += exp[i - 1]
        l_exp += exp[i]
        r_exp = exp[i + 2:]
        hinge_op = exp[i + 1]

        for p1 in generate_parened(l_exp):
            for p2 in generate_parened(r_exp):
                to_yield = ""
                if len(p1) > 3:
                    to_yield += "(" + p1 + ")"
                else:
                    to_yield += p1

                to_yield += hinge_op

                if len(p2) > 3:
                    to_yield += "(" + p2 + ")"
                else:
                    to_yield += p2

                yield to_yield

def bool_ops_gen():
    yield "&"
    yield "|"
    yield "^"

def generate_test_exps(length, acc=None):
    if acc is None:
        acc = []

    if length == 0:
        yield "".join(acc)
    else:
        if not acc:
            yield from generate_test_exps(length - 1, ["0"])
            yield from generate_test_exps(length - 1, ["1"])

        else:
            yield "".join(acc)
            for op in bool_ops_gen():
                acc.append(op)
                acc.append("0")
                yield from generate_test_exps(length - 1, acc)
                acc.pop()
                acc.append("1")
                yield from generate_test_exps(length - 1, acc)
                acc.pop()
                acc.pop()


class TestBooleanEvaluation(unittest.TestCase):

    def setUp(self):
        self.f = boolean_evaluation

    def generic_test(self, exp, val):
        print(exp, val)
        result = boolean_evaluation(exp, val)
        expected = 0
        for p in generate_parened(exp):
            if eval(p) == val:
                expected += 1

        self.assertEqual(result, expected)

    def test_1(self):
        for exp in generate_test_exps(5):
            self.generic_test(exp, True)
            self.generic_test(exp, False)


if __name__ == "__main__":
    unittest.main()