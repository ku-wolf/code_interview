#!/usr/bin/python3
from collections import defaultdict
import unittest
def resolve_deps(pkgs, deps):
    print(pkgs)
    print(deps)
    depended_on_by = defaultdict(lambda: [])
    number_of_deps = defaultdict(lambda: 0)
    zero_dependencies = []
    install_order = []
    for dependency, depender in deps:
        print(dependency, depender)

        if depender in number_of_deps:
            number_of_deps[depender] += 1
        else:
            number_of_deps[depender] = 1

        if dependency in depended_on_by:
            depended_on_by[dependency].append(depender)
        else:
            depended_on_by[dependency] = [depender]

    print("Pkgs and deps")
    for pkg, deps in number_of_deps.items():
        print(pkg, deps)

    print("Pkgs and dependers")
    for pkg, dependers in depended_on_by.items():
        print(pkg, dependers)


    for p in pkgs:
        if number_of_deps[p] == 0:
            zero_dependencies.append(p)
            del number_of_deps[p]


    while zero_dependencies:
        next_pkg = zero_dependencies.pop()
        install_order.append(next_pkg)
        for depender in depended_on_by[next_pkg]:
            number_of_deps[depender] -= 1
            if number_of_deps[depender] == 0:
                zero_dependencies.append(depender)
                del number_of_deps[depender]

    if number_of_deps:
        return None

    print(install_order)
    return install_order

class TestListOfDepths(unittest.TestCase):

    def setUp(self):
        self.f = resolve_deps

    def general_test(self, pkgs=None, deps=None):
        if pkgs is not None and deps is not None:
            result = self.f(pkgs, deps)

            deps_on = defaultdict(lambda: [])
            for dependency, depender in deps:
                if depender in deps_on:
                    deps_on[depender].append(dependency)
                else:
                    deps_on[depender] = []

            installed = set()
            for pkg in result:
                for deps in deps_on[pkg]:
                    if deps not in installed:
                        self.fail("dependency not installed")

                if pkg in installed:
                    self.fail("installed same pkg twice")
                installed.add(pkg)

    def test_1(self):
        pkgs = ["a", "b", "c", "d", "e", "f"]
        deps = [
            ("a", "d"),
            ("f", "b"),
            ("b", "d"),
            ("f", "a"),
            ("d", "c")
        ]
        self.general_test(pkgs, deps)
                
if __name__ == "__main__":
    unittest.main()