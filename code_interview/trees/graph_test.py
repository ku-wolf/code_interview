#!/usr/bin/python3

from code_interview.trees.graph import *


g = Graph()
g.add_blank_nodes(1)
print(g)

g.add_blank_edges(number=3, value=0)
g.add_blank_edges(number=3, value=1)
g.add_blank_edges(number=3, value=2)
print(g)

print("depth")
for n in depth_search(g):
    print(n.val)


print("\nbreadth")
for n in breadth_search(g):
    print(n.val)
